#!/usr/bin/env python3
"""Regenerate data/openalex-traces.json and data/citation-pairs.json from OpenAlex.

Reads  data/pivotal-openalex.csv   (key, doi, year, ... for the pivotal papers)
       data/citation-pairs.json    (the A -> B pairs to test; only "A"/"B" keys are read)
Writes data/openalex-traces.json   (citation curves, early adopters)
       data/citation-pairs.json    (OpenAlex verdicts refreshed; manual notes preserved)

    export OPENALEX_API_KEY=...   # never written to disk by this script
    python3 scripts/openalex_traces.py [--no-pairs] [--early-only KEY,KEY,...]

About 137 + 137 + ~80 + ~75 requests (a few cents with a key).  The
per-paper fields mirror the ones produced in the browser session of
2026-09-30, so the output can replace the delivered file directly.
"""
import csv, json, os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
import openalex_common as oa

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA = os.path.join(ROOT, "data")


def load_pivotal():
    with open(os.path.join(DATA, "pivotal-openalex.csv"), newline="") as f:
        return list(csv.DictReader(f))


def summarize(work_id, year):
    by = oa.citation_curve(work_id)
    years = sorted(y for y in by if y > 1800)
    cum = 0; marks = {}; peak = (None, 0); bins = {}
    for y in years:
        c = by[y]; cum += c
        for n in (10, 25, 50, 100, 500):
            if n not in marks and cum >= n:
                marks[n] = y
        if c > peak[1]:
            peak = (y, c)
        b = (y // 5) * 5; bins[b] = bins.get(b, 0) + c
    early, ec = oa.early_adopters(work_id, int(year), per_page=8)
    return {"first": years[0] if years else None, "y10": marks.get(10), "y25": marks.get(25),
            "y50": marks.get(50), "y100": marks.get(100), "y500": marks.get(500),
            "peak": list(peak), "bins": sorted(bins.items()), "ec": ec,
            "e": [[e["year"], e["cited_by"], e["authors"].split(";")[0][:24], (e["title"] or "")[:60], e["venue"][:26]] for e in early]}


def main():
    argv = sys.argv[1:]
    do_pairs = "--no-pairs" not in argv
    pivotal = load_pivotal()
    out = {"generated": str(datetime.date.today()), "source": "OpenAlex API via scripts/openalex_traces.py", "papers": {}}
    for row in pivotal:
        key = row["key"]; doi = row.get("doi", "")
        w = oa.resolve_doi(doi) if doi else None
        if not w:
            hits = oa.title_search(row["title"], row.get("year_claimed"))
            w = hits[0] if hits else None
        if not w:
            out["papers"][key] = {"error": "unresolved"}; print("unresolved", key); continue
        wid = oa.short_id(w["id"])
        p = {"id": wid, "y": w.get("publication_year"), "c": w.get("cited_by_count"), "r": w.get("referenced_works_count")}
        p.update(summarize(wid, row.get("year_claimed") or p["y"]))
        # duplicate records of the same paper (fragmented citations)
        alts = [h for h in oa.title_search(row["title"], row.get("year_claimed"))
                if oa.short_id(h["id"]) != wid and abs((h.get("publication_year") or 0) - int(row.get("year_claimed") or p["y"])) <= 1 and (h.get("cited_by_count") or 0) >= 15]
        if alts:
            p["alt"] = []
            for h in alts:
                aid = oa.short_id(h["id"]); by = oa.citation_curve(aid); bins = {}
                for y, c in by.items():
                    b = (y // 5) * 5; bins[b] = bins.get(b, 0) + c
                p["alt"].append({"id": aid, "total": h.get("cited_by_count"), "bins": sorted(bins.items())})
        out["papers"][key] = p
        print(key, wid, p["c"], "cites;", p.get("first"), "->", p.get("y100"))
    with open(os.path.join(DATA, "openalex-traces.json"), "w") as f:
        json.dump(out, f, indent=1)

    if do_pairs:
        path = os.path.join(DATA, "citation-pairs.json")
        pairs = json.load(open(path))
        refs = {}
        for pr in pairs["pairs"]:
            b = pr["B"]; a = pr["A"]
            if b not in refs and out["papers"].get(b, {}).get("id"):
                refs[b] = oa.referenced_works(out["papers"][b]["id"])
            aid = out["papers"].get(a, {}).get("id")
            alt_ids = [x["id"] for x in out["papers"].get(a, {}).get("alt", [])]
            if aid and b in refs:
                pr["openalex"] = "CITES" if (aid in refs[b] or any(x in refs[b] for x in alt_ids)) else "NOT-IN-REFS"
                pr["B_refs_indexed"] = len(refs[b])
        pairs["generated"] = str(datetime.date.today())
        with open(path, "w") as f:
            json.dump(pairs, f, indent=1)
        print("pairs refreshed:", len(pairs["pairs"]))


if __name__ == "__main__":
    main()
