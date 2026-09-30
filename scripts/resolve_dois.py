#!/usr/bin/env python3
"""Resolve the journal entries of references.md to DOIs / volume / pages via OpenAlex.

    export OPENALEX_API_KEY=...
    python3 scripts/resolve_dois.py            # writes data/references-resolved.csv
    python3 scripts/resolve_dois.py --apply    # also rewrites references.md in place,
                                               # appending "vol(issue), pages. doi:..." to
                                               # each resolved journal entry

Matching: OpenAlex title.search within publication_year +/- 1, best of 6
candidates by (token Jaccard of titles) + 0.3 if the first author's surname
matches + 0.1 if the year matches exactly.  Entries scoring below 0.55 are
left unresolved and flagged in the CSV; check those by hand.  The delivered
references.md was produced with exactly this procedure in the browser on
2026-09-30 and then hand-checked for the low-score cases.
"""
import csv, json, os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(__file__))
import openalex_common as oa

ROOT = os.path.join(os.path.dirname(__file__), "..")
REFS = os.path.join(ROOT, "references.md")
OUT = os.path.join(ROOT, "data", "references-resolved.csv")
ENTRY = re.compile(r"^- (?P<auth>.+?) \((?P<year>\d{4}[a-z]?)\)\. (?P<title>.+?)\. \*(?P<venue>[^*]+)\*")


def norm(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", t)).strip()


def toks(t):
    return {w for w in norm(t).split() if len(w) > 2}


def jacc(a, b):
    A, B = toks(a), toks(b)
    return len(A & B) / max(1, max(len(A), len(B)))


def parse_entries():
    entries = []
    section = None
    for n, line in enumerate(open(REFS, encoding="utf-8")):
        if line.startswith("## "):
            section = line[3:].strip()
        m = ENTRY.match(line.strip())
        if m and section and section.lower().startswith("journal"):
            d = m.groupdict(); d["line"] = n; d["raw"] = line.rstrip("\n")
            d["surname"] = d["auth"].split(",")[0].strip()
            d["year_int"] = int(d["year"][:4])
            entries.append(d)
    return entries


def resolve(e):
    hits = oa.title_search(e["title"], e["year_int"], per_page=6)
    best = None
    for w in hits:
        sim = jacc(e["title"], w.get("title") or "")
        au = ((w.get("authorships") or [{}])[0].get("author") or {}).get("display_name", "")
        sur_ok = norm(e["surname"]).split()[-1] in norm(au) if norm(e["surname"]) else False
        score = sim + (0.3 if sur_ok else 0) + (0.1 if w.get("publication_year") == e["year_int"] else 0)
        if best is None or score > best["score"]:
            b = w.get("biblio") or {}
            best = {"score": round(score, 3), "sim": round(sim, 3), "surname_ok": sur_ok, "openalex_id": oa.short_id(w["id"]),
                    "doi": (w.get("doi") or "").replace("https://doi.org/", ""), "oa_title": w.get("title"), "oa_year": w.get("publication_year"),
                    "cited_by": w.get("cited_by_count"), "journal": ((w.get("primary_location") or {}).get("source") or {}).get("display_name", ""),
                    "volume": b.get("volume") or "", "issue": b.get("issue") or "", "first_page": b.get("first_page") or "", "last_page": b.get("last_page") or "",
                    "first_author": au}
    return best


def main():
    entries = parse_entries()
    rows = []
    for e in entries:
        r = resolve(e) or {"score": 0}
        r.update({"index": len(rows), "surname": e["surname"], "year": e["year"], "title": e["title"], "venue": e["venue"], "line": e["line"]})
        r["status"] = "ok" if r.get("score", 0) >= 0.55 else "check"
        rows.append(r); print(r["index"], r["status"], r.get("doi", ""), "|", e["title"][:60])
    fields = ["index", "status", "score", "surname", "year", "title", "venue", "doi", "openalex_id", "journal", "volume", "issue", "first_page", "last_page", "oa_title", "oa_year", "cited_by", "first_author", "line"]
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    print("written", OUT, "unresolved:", sum(r["status"] != "ok" for r in rows))
    if "--apply" in sys.argv:
        lines = open(REFS, encoding="utf-8").read().split("\n")
        for r in rows:
            if r["status"] != "ok" or not r.get("doi"):
                continue
            pages = f"{r['first_page']}–{r['last_page']}" if r["first_page"] and r["last_page"] and r["first_page"] != r["last_page"] else (r["first_page"] or "")
            vol = r["volume"] + (f"({r['issue']})" if r["issue"] else "")
            tail = ", ".join(x for x in (vol, pages) if x)
            if "doi:" not in lines[r["line"]]:
                lines[r["line"]] = lines[r["line"]].rstrip(".") + (f", {tail}" if tail else "") + f". doi:{r['doi']}"
        open(REFS, "w", encoding="utf-8").write("\n".join(lines))
        print("references.md updated")


if __name__ == "__main__":
    main()
