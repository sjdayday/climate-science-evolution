#!/usr/bin/env python3
"""Build the problem x cycle table of 07-ipcc-role.md section 3.1 from data/openalex-traces.json.

For each problem cluster and assessment cycle, the cell lists the pivotal papers that anchor the
result the SPM stated, the year each paper's cumulative OpenAlex citations reached 25 ("y25", from
the traces file), and the gap to the cycle's cutoff year (the last full year before the SPM was
approved). A result whose anchoring papers had all reached 25 citations by the cutoff is marked
"formalized (+n)" with n the smallest gap; one whose papers reached 25 citations only after the
cutoff is marked "level" (the assessment adopted the result within a year of its publication).
Contested papers are listed with the same marker and the cycle that answered them.

Usage: python3 scripts/problem_cycle.py  (writes data/problem-cycle.json and prints the table)
"""
import json, os, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
TRACES = os.path.join(ROOT, "data", "openalex-traces.json")
OUT = os.path.join(ROOT, "data", "problem-cycle.json")

# Last full year before each SPM was approved: FAR May 1990, SAR Nov 1995, TAR Jan 2001,
# AR4 Feb 2007, AR5 Sep 2013, AR6 Aug 2021.
CUTOFF = {"FAR": 1989, "SAR": 1995, "TAR": 2000, "AR4": 2006, "AR5": 2013, "AR6": 2020}
CYCLES = ["FAR", "SAR", "TAR", "AR4", "AR5", "AR6"]

NAMES = {
    "plass1956": "Plass 1956", "moller1963": "Möller 1963", "mw1967": "Manabe & Wetherald 1967",
    "keeling1960": "Keeling 1960", "revelle1957": "Revelle & Suess 1957", "broecker1979": "Broecker et al. 1979",
    "tans1990": "Tans et al. 1990", "sabine2004": "Sabine et al. 2004", "friedlingstein2006": "Friedlingstein et al. 2006",
    "manabebryan1969": "Manabe & Bryan 1969", "mw1975": "Manabe & Wetherald 1975", "manabestouffer1988": "Manabe & Stouffer 1988",
    "schlesingermitchell1987": "Schlesinger & Mitchell 1987", "hansen1981": "Hansen et al. 1981",
    "zelinka2020": "Zelinka et al. 2020", "hausfather2022": "Hausfather et al. 2022",
    "charney1979": "Charney et al. 1979", "hansen1984": "Hansen et al. 1984", "otto2013": "Otto et al. 2013",
    "sherwood2020": "Sherwood et al. 2020", "lewiscurry2018": "Lewis & Curry 2018", "knuttihegerl2008": "Knutti & Hegerl 2008",
    "roebaker2007": "Roe & Baker 2007",
    "soden2005": "Soden et al. 2005", "sodenheld2006": "Soden & Held 2006", "bonydufresne2005": "Bony & Dufresne 2005",
    "sherwood2014": "Sherwood et al. 2014", "cess1989": "Cess et al. 1989",
    "charlson1992": "Charlson et al. 1992", "twomey1977": "Twomey 1977", "stevens2015": "Stevens 2015",
    "bellouin2020": "Bellouin et al. 2020",
    "hansen1988": "Hansen et al. 1988", "mitchell1995": "Mitchell et al. 1995", "hegerl1996": "Hegerl et al. 1996",
    "santer1996": "Santer et al. 1996", "tett1999": "Tett et al. 1999", "stott2000": "Stott et al. 2000",
    "stott2004": "Stott et al. 2004",
    "jones1986": "Jones et al. 1986", "spencerchristy1990": "Spencer & Christy 1990", "mearswentz2005": "Mears & Wentz 2005",
    "kosakaxie2013": "Kosaka & Xie 2013", "fyfe2013": "Fyfe et al. 2013", "karl2015": "Karl et al. 2015",
    "cowtanway2014": "Cowtan & Way 2014", "medhaug2017": "Medhaug et al. 2017",
    "lorius1990": "Lorius et al. 1990", "dansgaard1993": "Dansgaard et al. 1993", "mbh1998": "Mann, Bradley & Hughes 1998",
    "mbh1999": "Mann, Bradley & Hughes 1999", "mm2005": "McIntyre & McKitrick 2005", "neukom2019": "Neukom et al. 2019",
    "allen2009": "Allen et al. 2009", "matthews2009": "Matthews et al. 2009", "matthewscaldeira2008": "Matthews & Caldeira 2008",
    "solomon2009": "Solomon et al. 2009", "macdougall2020": "MacDougall et al. 2020",
    "alleningram2002": "Allen & Ingram 2002",
    "rahmstorf1995": "Rahmstorf 1995", "stockerschmittner1997": "Stocker & Schmittner 1997", "rahmstorf2007": "Rahmstorf 2007",
    "pfeffer2008": "Pfeffer et al. 2008", "decontopollard2016": "DeConto & Pollard 2016", "lenton2008": "Lenton et al. 2008",
    "armstrongmckay2022": "Armstrong McKay et al. 2022", "ditlevsen2023": "Ditlevsen & Ditlevsen 2023",
    "vanwesten2024": "van Westen et al. 2024",
    "hasselmann1976": "Hasselmann 1976", "lorenz1963": "Lorenz 1963", "hawkinssutton2009": "Hawkins & Sutton 2009",
    "deser2012": "Deser et al. 2012", "laepplehuybers2014": "Laepple & Huybers 2014", "cohnlins2005": "Cohn & Lins 2005",
    "lindzen1990": "Lindzen 1990", "lindzen2001": "Lindzen et al. 2001", "svensmark1997": "Svensmark & Friis-Christensen 1997",
    "lindzenchoi2009": "Lindzen & Choi 2009", "mckitrickchristy2018": "McKitrick & Christy 2018", "santer2017": "Santer et al. 2017",
}

# Cell definitions: (problem, cycle) -> dict(origin=[keys], contest=[keys], note=str)
CELLS = {
    ("P01 radiative basis", "FAR"): dict(origin=["plass1956", "moller1963", "mw1967"], note="settled since the 1960s–70s; not re-assessed later"),
    ("P02 carbon accumulation", "FAR"): dict(origin=["revelle1957", "keeling1960", "broecker1979"]),
    ("P02 carbon accumulation", "SAR"): dict(origin=["tans1990"], note="the 'missing sink'"),
    ("P02 carbon accumulation", "AR4"): dict(origin=["sabine2004", "friedlingstein2006"], note="ocean sink; carbon–climate feedback"),
    ("P03 model hierarchy", "FAR"): dict(origin=["manabebryan1969", "mw1975", "hansen1981", "schlesingermitchell1987", "manabestouffer1988"]),
    ("P03 model hierarchy", "AR6"): dict(origin=["zelinka2020"], after=["hausfather2022"], note="constrained projections rather than the raw ensemble; the 'hot model' name came after"),
    ("P04 sensitivity", "FAR"): dict(origin=["charney1979", "hansen1984"], override="formalized (report)", note="the 1.5–4.5 °C range was carried by the NAS report, which OpenAlex under-indexes (102 citations); Hansen 1984 anchors the feedback analysis"),
    ("P04 sensitivity", "AR4"): dict(origin=["roebaker2007"], after=["knuttihegerl2008"], note="the 3 °C best estimate synthesized the 2002–06 probabilistic estimates (not in the traced set); Knutti & Hegerl 2008 restated it after AR4"),
    ("P04 sensitivity", "AR5"): dict(origin=["otto2013"], note="best estimate withdrawn in deference to the energy-budget estimates"),
    ("P04 sensitivity", "AR6"): dict(origin=["sherwood2020", "zelinka2020"], contest=["lewiscurry2018"]),
    ("P05 feedbacks", "AR4"): dict(origin=["soden2005", "bonydufresne2005", "sodenheld2006"], note="water vapour/lapse rate robust; low clouds the largest spread"),
    ("P05 feedbacks", "AR6"): dict(origin=["sherwood2014", "zelinka2020"], note="emergent constraints; CMIP6 cloud feedback"),
    ("P06 aerosol forcing", "SAR"): dict(origin=["twomey1977", "charlson1992"]),
    ("P06 aerosol forcing", "AR6"): dict(origin=["bellouin2020"], contest=["stevens2015"], note="Stevens 2015 is a lower-bound argument from within the field, taken up by Bellouin 2020"),
    ("P07 attribution", "FAR"): dict(origin=["hansen1988"], override="declined (lagged)", note="the FAR declined the detection Hansen 1988 claimed; by the citation record the paper was already a reference"),
    ("P07 attribution", "SAR"): dict(origin=["mitchell1995", "hegerl1996", "santer1996"], note="'discernible human influence' preceded the 25-citation mark of all three fingerprint papers"),
    ("P07 attribution", "TAR"): dict(origin=["tett1999", "stott2000"]),
    ("P07 attribution", "AR4"): dict(origin=["stott2004"], contest=["lindzen2001"], note="Stott 2004: event attribution; Lindzen 2001 answered in ch. 8"),
    ("P08 observational record", "FAR"): dict(origin=["jones1986"]),
    ("P08 observational record", "SAR"): dict(contest=["spencerchristy1990"], note="the satellite discrepancy, discussed in the SAR and closed by 2005"),
    ("P08 observational record", "AR4"): dict(origin=["mearswentz2005"]),
    ("P08 observational record", "AR5"): dict(origin=["kosakaxie2013", "fyfe2013", "cowtanway2014"], note="the 'hiatus' box"),
    ("P08 observational record", "AR6"): dict(origin=["karl2015", "medhaug2017"]),
    ("P09 paleoclimate", "SAR"): dict(origin=["lorius1990", "dansgaard1993"], note="ice-core CO₂–temperature coupling; abrupt change"),
    ("P09 paleoclimate", "TAR"): dict(origin=["mbh1998", "mbh1999"], override="formalized (+0); premature on the decade/year claim", note="the century claim had been adopted; the decade/year claim is the chapter's over-reach (§4) and is invisible to a citation measure"),
    ("P09 paleoclimate", "AR4"): dict(contest=["mm2005"], note="answered in ch. 6 (Wahl & Ammann, Huybers, von Storch & Zorita); NRC 2006"),
    ("P09 paleoclimate", "AR6"): dict(origin=["neukom2019"]),
    ("P10 TCRE / ZEC", "AR5"): dict(origin=["matthewscaldeira2008", "allen2009", "matthews2009", "solomon2009"]),
    ("P10 TCRE / ZEC", "AR6"): dict(origin=["macdougall2020"], note="ZEC intercomparison"),
    ("P11 hydrological cycle", "AR4"): dict(origin=["alleningram2002", "sodenheld2006"], note="thermodynamic scaling; wet-get-wetter"),
    ("P12 AMOC", "TAR"): dict(origin=["rahmstorf1995", "stockerschmittner1997"]),
    ("P12 AMOC", "AR6"): dict(after=["armstrongmckay2022", "ditlevsen2023", "vanwesten2024"], note="the next cycle's test case"),
    ("P12 ice sheets / sea level", "AR4"): dict(origin=["rahmstorf2007"], after=["pfeffer2008"], override="excluded (lagged)", note="AR4 excluded ice dynamics 'because a basis in published literature is lacking'; Rahmstorf 2007 was in print (Science, December 2006) but not yet adopted"),
    ("P12 ice sheets / sea level", "AR5"): dict(origin=["rahmstorf2007", "pfeffer2008", "lenton2008"]),
    ("P12 ice sheets / sea level", "AR6"): dict(origin=["decontopollard2016"], note="the low-likelihood, high-impact storyline"),
    ("P13 internal variability", "FAR"): dict(origin=["lorenz1963", "hasselmann1976"]),
    ("P13 internal variability", "AR4"): dict(contest=["cohnlins2005"], note="long-memory argument; AR4 ch. 9 relies on the residual-consistency test"),
    ("P13 internal variability", "AR5"): dict(origin=["hawkinssutton2009", "deser2012", "kosakaxie2013"]),
    ("P13 internal variability", "AR6"): dict(origin=["laepplehuybers2014"], note="cited in AR6 ch. 3's attribution assessment (`08` §6)"),
    ("Contested papers (engagement cycle)", "SAR"): dict(contest=["lindzen1990"]),
    ("Contested papers (engagement cycle)", "TAR"): dict(contest=["svensmark1997"]),
    ("Contested papers (engagement cycle)", "AR5"): dict(contest=["lindzenchoi2009"], note="cited in AR5 ch. 10 §10.8.2 as 'based on problematic assumptions'"),
    ("Contested papers (engagement cycle)", "AR6"): dict(contest=["mckitrickchristy2018"], origin=["santer2017"], note="the one exchange in which the two sides do not cite each other (`04` §5e)"),
}

PROBLEM_ORDER = ["P01 radiative basis", "P02 carbon accumulation", "P03 model hierarchy", "P04 sensitivity", "P05 feedbacks",
                 "P06 aerosol forcing", "P07 attribution", "P08 observational record", "P09 paleoclimate", "P10 TCRE / ZEC",
                 "P11 hydrological cycle", "P12 AMOC", "P12 ice sheets / sea level", "P13 internal variability",
                 "Contested papers (engagement cycle)"]


def y25(p):
    v = p.get("y25")
    return None if v in (None, "None") else int(v)


def fmt_paper(key, papers, cutoff, role):
    p = papers[key]
    y = y25(p)
    name = NAMES.get(key, key)
    if y is None:
        return f"{name} [<25 citations]", None
    gap = cutoff - y
    return f"{name} [25 by {y}]", gap


def build(papers):
    rows = {}
    for (prob, cyc), spec in CELLS.items():
        cutoff = CUTOFF[cyc]
        parts, gaps, contests = [], [], []
        for k in spec.get("origin", []):
            s, g = fmt_paper(k, papers, cutoff, "origin")
            parts.append(s)
            if g is not None:
                gaps.append(g)
        for k in spec.get("contest", []):
            s, g = fmt_paper(k, papers, cutoff, "contest")
            contests.append(s)
        afters = [NAMES.get(k, k) for k in spec.get("after", [])]
        if gaps:
            mn = min(gaps)
            relation = f"formalized (+{mn})" if mn >= 0 else "level"
        elif contests and not spec.get("origin"):
            relation = "engaged"
        else:
            relation = "—"
        if spec.get("override"):
            relation = spec["override"]
        cell = {"cutoff": cutoff, "relation": relation, "origin": parts, "gaps": gaps,
                "contest": contests, "after": afters, "note": spec.get("note", "")}
        rows[(prob, cyc)] = cell
    return rows


def markdown(rows):
    out = ["| Problem | " + " | ".join(f"{c} ({CUTOFF[c]})" for c in CYCLES) + " |",
           "|---|" + "---|" * len(CYCLES)]
    for prob in PROBLEM_ORDER:
        cells = []
        for cyc in CYCLES:
            r = rows.get((prob, cyc))
            if not r:
                cells.append("—")
                continue
            s = f"**{r['relation']}**"
            if r["origin"]:
                s += ": " + "; ".join(r["origin"])
            if r["contest"]:
                s += ("; " if r["origin"] else ": ") + "contested by " + "; ".join(r["contest"])
            if r["after"]:
                s += "; later: " + "; ".join(r["after"])
            if r["note"]:
                s += f" — {r['note']}"
            cells.append(s)
        out.append(f"| **{prob}** | " + " | ".join(cells) + " |")
    return "\n".join(out)


def main():
    papers = json.load(open(TRACES, encoding="utf-8"))["papers"]
    rows = build(papers)
    serial = {f"{p} | {c}": v for (p, c), v in rows.items()}
    json.dump({"generated": "from data/openalex-traces.json by scripts/problem_cycle.py", "cutoff": CUTOFF,
               "legend": {"[25 by Y]": "year the paper's cumulative OpenAlex citations reached 25",
                          "formalized (+n)": "every anchoring paper had reached 25 citations n or more years before the cutoff",
                          "level": "at least one anchoring paper reached 25 citations only after the cutoff year"},
               "cells": serial}, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(markdown(rows))
    n_form = sum(1 for v in rows.values() if v["relation"].startswith("formalized"))
    n_level = sum(1 for v in rows.values() if v["relation"] == "level")
    n_eng = sum(1 for v in rows.values() if v["relation"] == "engaged")
    print(f"\ncells: {len(rows)}  formalized: {n_form}  level: {n_level}  engaged: {n_eng}", file=sys.stderr)


if __name__ == "__main__":
    main()
