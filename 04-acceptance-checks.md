# Acceptance claims checked against the primary papers

**Status:** v0.4, 2026-10-01 (first pass 2026-09-30; Crossref-resolved checks and eight P13 pairs added 2026-10-01). Item 1 of the README's "how this analysis is meant to evolve" list.

## What was checked, and how

The P-files claim, for each problem, that a particular answer was accepted by a particular time, and they name the later papers whose introductions or methods should show *premise adoption* (criterion B in the README). This file records the direct tests of those claims that could be made in this pass, in two forms:

1. **Citation-link tests.** For 131 pairs "A → B" where a P-file says (or implies) that paper B builds on paper A, I asked whether B actually cites A. The first test used OpenAlex's `referenced_works` for B (`data/citation-pairs.json`, field `openalex`); where OpenAlex said "not in references" or where the pair mattered, I read B's printed reference list on the publisher's page (Nature, PNAS, AGU/Wiley, Tellus, Copernicus) or resolved B's OpenAlex reference ids to titles. Verdict codes: **CITES** / **NOT-IN-REFS** (OpenAlex), and after manual checking **VERIFIED-CITES**, **VERIFIED-NO**, **VARIANT** (B cites a different version or predecessor of A), **UNVERIFIABLE** (B's reference list not reachable from this session — chiefly *Science* and AMS journals, which block automated reading).
2. **Premise quotations.** Where the full text of B was readable (open-access Wiley/AGU, PNAS, Nature reference lists, Copernicus), I extracted the sentence in which A's result is taken as a premise. Tagged **[P]** (read from the primary text this pass), **[S]** (secondary source), **[M]** (from memory, not re-verified) as in `06-assessment-language.md`.

**Headline result.** Of the 131 pairs, OpenAlex confirmed 83 links outright. Of the 48 it did not confirm, manual checking showed 7 to be indexing gaps (the link exists in print or in the publisher's reference deposit at Crossref), 11 to be **variants** (B cites a later or different form of the same result), 28 to be **genuine non-citations**, and 2 could not be verified. The genuine non-citations are the interesting part: none of them overturns a P-file's claim about *what* was accepted, but several correct the *lineage* the P-files drew, and they reveal five recurring patterns in how acceptance is carried in the literature (section 5). Every correction has been applied to the P-files and is listed in section 4.

The full pair-by-pair table is `data/citation-pairs.json`; what follows is organized by problem.

---

## 1. Citation-link results by problem

### P01 Radiative basis

| A → B (claimed lineage) | Verdict | Evidence |
|---|---|---|
| Plass 1956 → Revelle & Suess 1957 | CITES | OpenAlex; 21 of Revelle's references indexed. |
| Möller 1963 → Manabe & Wetherald 1967 | CITES | OpenAlex (MW67 has only 7 indexed references; Möller is among them). Consistent with the P01 narrative that MW67 was written as the answer to Möller's surface-budget paradox. |
| MW67 → Budyko 1969 | VERIFIED-CITES | Budyko's Tellus paper (5 resolved references) cites MW67 — the earliest adoption of the radiative–convective result outside GFDL, one year after publication. |
| MW67 → Manabe & Wetherald 1975 | UNVERIFIABLE | OpenAlex holds no reference list for MW75 and AMS full text is not reachable here. (Known from the paper itself [M].) |
| MW67 → Schneider & Dickinson 1974; → Hansen 1981; → Held & Soden 2000; → Hausfather 2020 | CITES | OpenAlex, all four. |

### P02 Carbon accumulation

| A → B | Verdict | Evidence |
|---|---|---|
| Plass 1956 → Keeling 1960 | VERIFIED-NO | Keeling's 11 references are Revelle & Suess 1957, Callendar 1958, Bray 1959, Slocum 1955, Fonselius et al. 1956, Craig 1954, and his own 1958 paper. P02 §"Inheritance" said Plass's radiative result "made measuring CO₂ worthwhile"; the citation record puts the motive in the measurement literature (Callendar, Slocum, Revelle), not the radiative one. **Corrected.** |
| Revelle & Suess 1957 → Keeling 1960 | CITES | OpenAlex and printed list. |
| Woodwell 1978 → Broecker et al. 1979 | CITES | OpenAlex. |
| Tans et al. 1990 → Sabine et al. 2004 | VERIFIED-NO | Sabine's 17 resolved references anchor to Revelle & Suess 1957, Gruber 1996, Feely 2004; Tans 1990 (the "missing sink") is not cited. The P02 narrative treats them as successive answers to the same question, which they are; the 2004 paper simply does not route through the 1990 one. Note added, no claim changed. |
| Revelle & Suess 1957 → Solomon et al. 2009 | CITES | OpenAlex — the 1957 paper still cited as the origin of the "long tail" idea fifty-two years later. |
| Archer et al. 2009 → Solomon et al. 2009 | VERIFIED-NO | Anachronistic pair (Solomon: February 2009; Archer: *Annual Reviews*, May 2009). Solomon cites Archer 2005 and Archer & Brovkin 2008. |

### P03 Model hierarchy

| A → B | Verdict | Evidence |
|---|---|---|
| MW67 / Budyko 1969 / Sellers 1969 → Schneider & Dickinson 1974 | CITES ×3 | OpenAlex; the 1974 review (176 indexed references) cites all three. |
| Schneider & Dickinson 1974 → Held 2005 | VERIFIED-CITES | OpenAlex indexes only seven of Held's references (Phillips 1956, Hoskins 1983, Held & Suarez 1994, Murphy et al. 2004, Frierson et al. 2006 …), none of them the 1974 review, but the printed text cites it directly: "See, for example, Schneider and Dickinson (1974), and, especially, Hoskins (1983)" [P, GFDL preprint]. An indexing gap; the P03 "bracket" claim is a citation link as well as a link of ideas. |
| Manabe & Bryan 1969 → Stouffer, Manabe & Bryan 1989 | VERIFIED-NO | Stouffer 1989 (21 refs) cites Bryan et al. 1982, Bryan & Spelman 1985, Manabe & Bryan 1985, Manabe & Stouffer 1988, Washington & Meehl 1989 — the coupled-model line is cited from its 1980s papers, not from the 1969 origin. |
| Hansen 1984 → Schlesinger & Mitchell 1987 | CITES | OpenAlex. |
| Kiehl 2007 → Hourdin 2017 → Sherwood 2020 | CITES ×2 | OpenAlex. The "tuning to twentieth-century warming" concern is carried forward by citation, as P03/P04 claim. |
| MW75 → Held & Soden 2006; MW67/MW75 → Hausfather 2020 | CITES | OpenAlex. |

### P04 Climate sensitivity

| A → B | Verdict | Evidence |
|---|---|---|
| Roe & Baker 2007 → Knutti & Hegerl 2008 | CITES | OpenAlex (104 refs). |
| Otto 2013; Armour 2013; Andrews 2015; Gregory & Andrews 2016; Lewis & Curry 2018; Kiehl 2007; PALAEOSENS 2012; Tierney 2020 → Sherwood 2020 | CITES ×8 | OpenAlex; Sherwood et al. cite 521 works and every input the P04 lineage names is among them. |
| Annan & Hargreaves 2011 → Sherwood 2020 | VERIFIED-NO | Not among the 521; Sherwood et al. cite Annan & Hargreaves 2006 (GRL) instead. Trivial; P04 text unchanged. |
| Armour 2013 → Andrews 2015 → Gregory & Andrews 2016 | CITES ×2 | OpenAlex — the pattern-effect chain is a genuine citation chain. |
| Sherwood 2020 → Hausfather 2022; → Lewis 2023; → Hansen 2023 | CITES ×3 | OpenAlex. Both the critique (Lewis) and the high-sensitivity alternative (Hansen) take Sherwood as the reference point, which is the sense in which P04 calls Sherwood the current anchor. |
| Zelinka 2020 → Hausfather 2022; → Myers 2021 | CITES ×2 | OpenAlex. |
| Cess 1989 → Zelinka 2020 | CITES | OpenAlex. |
| Otto 2013 → Lewis & Curry 2018 | CITES | OpenAlex. |

### P05 Feedbacks

| A → B | Verdict | Evidence |
|---|---|---|
| Cess et al. 1989 (Science) → Bony & Dufresne 2005 | VARIANT | Bony & Dufresne cite **Cess et al. 1990** (JGR, the full 19-model intercomparison), not the 1989 *Science* letter. |
| Cess 1989 → Soden & Held 2006 | VARIANT | Same: Cess 1990 and Cess 1996 are cited. The P05 text already lists "Cess et al. (1989, 1990)"; note added that the 1990 JGR paper is the one carried forward in citations. |
| Hansen 1984 → Soden & Held 2006 | VERIFIED-NO | Not among the 18 resolved references; Soden & Held anchor the feedback decomposition to Wetherald & Manabe 1988, Colman 2003 and Webb 2006. The *method* (P03 §"hierarchy as interpretive framework") is Hansen's, but the 2006 paper does not cite it. **Note added to P03.** |
| Bony & Dufresne 2005 → Soden & Held 2006 | CITES | OpenAlex. |
| Lindzen 1990 → Held & Soden 2000; → Soden 2005 | CITES ×2 | OpenAlex: the water-vapour-feedback papers engage Lindzen's 1990 objection directly. |
| Soden 2005 → Dessler & Sherwood 2009 | CITES | OpenAlex. |
| Lindzen 2001 → Hartmann & Michelsen 2002 | CITES | OpenAlex (a reply). |
| Soden & Held 2006; Tan 2016 → Zelinka 2020 | CITES ×2 | OpenAlex. |

### P06 Radiative forcing and aerosols

| A → B | Verdict | Evidence |
|---|---|---|
| Twomey 1977 → Charlson et al. 1992 | VARIANT | All 60 of Charlson's references are indexed: the cloud-albedo effect is cited to **Twomey 1984** (Tellus) and Twomey 1991, with Charlson 1987/1991, Coakley 1987, Radke 1989, and Twomey's 1971 paper and 1977 book *Atmospheric Aerosols* [P: Crossref]; the 1977 *J. Atmos. Sci.* paper is not cited. **Note added.** |
| Charlson 1992 → Mitchell et al. 1995 | VARIANT | Mitchell's 25 references cite Charlson et al. 1991 (Tellus) for the forcing field and **IPCC 1994** (*Radiative Forcing of Climate Change*) for the magnitude of sulphate forcing (ref. 3, supporting the abstract sentence "After greenhouse gases, sulphate aerosols probably exert the next largest anthropogenic radiative forcing of the atmosphere³") [P]. See pattern (a) in §5. |
| Charlson 1992 → Santer 1996 | VARIANT | Santer cites Charlson & Wigley 1994 (*Scientific American*) [P, ref. 19]. |
| Charlson 1992 → Kiehl 2007 | VERIFIED-NO | Kiehl's 26 references cite Anderson et al. 2003, Andreae et al. 2005, Mitchell 1995, Hansen 2005, Kerr 2007 [P]. |
| Stevens 2015 → Bellouin 2020 | CITES | OpenAlex. |
| Ramanathan 1985 → Hansen 1988 | CITES | OpenAlex and printed list. |
| Hansen 1981 → Hansen 1988 | CITES | Printed list. |

### P07 Detection and attribution

| A → B | Verdict | Evidence |
|---|---|---|
| Hasselmann 1976 → Hasselmann 1993 | VARIANT | The 1993 fingerprint paper (21 refs, resolved to titles) cites **Hasselmann 1979** "On the signal-to-noise problem", Bell 1982, Barnett & Schlesinger 1987, Madden & Ramanathan 1980, Karoly 1989 — not the 1976 stochastic-model paper. P07 already names 1979 as the origin of the detection framing; the 1976 → 1993 link in P07 §"problem" is intellectual, not a citation. **Note added.** |
| Hasselmann 1993 → Hegerl 1996 | CITES | OpenAlex. |
| Hasselmann 1993 → Santer 1996 | VARIANT | Santer cites Hasselmann et al. 1995, *MPI Report 168* (the multi-pattern extension) [P, ref. 38]. |
| Hegerl 1996 → Santer 1996 | VERIFIED-CITES | Ref. 42, "Hegerl, G. C. et al. J. Clim. (in press)" [P] — an in-press citation OpenAlex could not resolve. |
| Mitchell 1995 → Santer 1996 | CITES | OpenAlex and printed list (ref. 10) [P]. |
| Santer 1996 → Tett 1999 → Stott 2000; Santer 1996 → Stott 2000 | CITES ×3 | OpenAlex. |
| Madden & Ramanathan 1980 → Hansen 1981 | CITES | OpenAlex. |
| Charney 1979 → Hansen 1981 | VERIFIED-CITES | Reference 1 of the 69 references deposited at Crossref is "Carbon Dioxide and Climate" (NAS 1979), the Charney report [P: Crossref, 2026-10-01]; OpenAlex indexed 53 of the 69 and missed it. Hansen et al. 1988 cites it too (printed list) [P]. |
| Manabe & Wetherald 1975 → Hansen 1981 | VERIFIED-NO | The Manabe papers among Hansen 1981's 69 references are MW64, MW67, Manabe & Stouffer 1979 (*Nature*) and Manabe & Stouffer 1980 (*JGR*) — GISS built on the 1-D model and on the latest GFDL result, not on the 1975 GCM paper [P: Crossref]. |
| Jones et al. 1986 → Hansen 1988 | VERIFIED-NO | Hansen 1988 uses Hansen & Lebedeff 1987/1988 for observations; the CRU series is not cited [P]. Consistent with P08's "two long-running series with different philosophies". |
| Friis-Christensen & Lassen 1991 → Lockwood & Fröhlich 2007 | CITES | OpenAlex. |
| Svensmark & Friis-Christensen 1997 → Lockwood & Fröhlich 2007 | VARIANT | Lockwood & Fröhlich (90 refs) cite Svensmark 2007 "Cosmoclimatology", Carslaw 2002, Harrison & Stephenson 2006; the 1997 paper is not among them. |
| Santer 2017 → McKitrick & Christy 2018 | VERIFIED-NO | McKitrick & Christy's 20 references contain no Santer paper [P]. See pattern (e). |

### P08 Observational record

| A → B | Verdict | Evidence |
|---|---|---|
| Spencer & Christy 1990 → Mears & Wentz 2005 | VARIANT | Mears & Wentz (27 refs, all resolved) cite Christy et al. 2000, 2003 and Spencer & Christy 1992; the 1990 *Science* paper is not cited. |
| Kosaka & Xie 2013; Karl 2015; Cowtan & Way 2014; Fyfe 2013 → Medhaug 2017 | CITES ×4 | OpenAlex (231 refs). The hiatus literature is a genuine citation cluster, as P08 says. |
| Levitus 2000 → Hansen 2005 | CITES | OpenAlex. |
| Hansen 2005 → Loeb 2021 | VERIFIED-NO | Loeb's 29 references cite von Schuckmann et al. 2016, 2020 and Johnson et al. 2016 for the energy-imbalance framing; Hansen 2005 is not cited [P]. Pattern (b). |
| Hays 1976 → Lorius 1990 | CITES | OpenAlex. |

### P09 Paleoclimate

| A → B | Verdict | Evidence |
|---|---|---|
| MBH 1998 → MBH 1999 → McIntyre & McKitrick 2005 | CITES ×2 | OpenAlex. |
| MBH 1998 / MBH 1999 / MM 2005 → Neukom 2019 | VERIFIED-NO ×3 | Neukom et al. (80 refs) cite Mann et al. 2008 (PNAS), Mann et al. 2009 (Science), PAGES 2k 2013/2017/2019; neither the original hockey-stick papers nor their critique appear [P]. This supports P09's marker (B) ("Neukom is now the reference") and adds a marker-(D) observation: by 2019 the 1998–2005 controversy has dropped out of the citation chain of the reference reconstruction altogether. **Note added.** |
| Shakun 2012; PALAEOSENS 2012 → Tierney 2020 | CITES ×2 | OpenAlex. |
| Lorius 1990 → PALAEOSENS 2012 → Sherwood 2020 | CITES ×2 | OpenAlex — the ice-core sensitivity line is a citation chain from 1990 to 2020. |

### P10 Transient response, commitment, cumulative emissions

| A → B | Verdict | Evidence |
|---|---|---|
| Hansen 1985 → Stouffer 1989 | VERIFIED-NO | Stouffer 1989 cites Hansen et al. 1988 (JGR), Thompson & Schneider 1982 and Broecker 1987, not Hansen 1985 [P]. P10 listed Hansen 1985 and Stouffer 1989 as successive steps; they are parallel (GISS and GFDL) lines. **Corrected.** |
| Matthews & Caldeira 2008 → Solomon 2009 | VERIFIED-CITES | Ref. 6, and the premise sentence: "It is not generally appreciated that the atmospheric temperature increases caused by rising carbon dioxide concentrations are not expected to decrease significantly even if carbon emissions were to completely cease (5–7)" — refs 5 Meehl et al. 2007 (AR4 ch. 10), 6 Matthews & Caldeira 2008, 7 Plattner et al. 2008 [P]. (An earlier note in this project's working files said the opposite; it was wrong.) |
| Matthews & Caldeira 2008; Solomon 2009 → MacDougall 2020 | CITES ×2 | OpenAlex; the ZECMIP introduction names Matthews & Caldeira, Plattner 2008, Solomon 2009, Gillett 2011, Frölicher & Paynter 2015, Ehlert & Zickfeld 2017 as the prior results it tests [S: machine-read Copernicus HTML]. |
| Matthews 2009; Allen 2009 → MacDougall 2020 | VERIFIED-NO | The TCRE papers are not cited by the ZEC intercomparison — ZEC and TCRE are treated as separate quantities, as P10 says. |
| Matthews 2009 ↔ Allen 2009 | CITES both ways | OpenAlex: each cites the other (companion papers in the same *Nature* issue). |
| Allen & Ingram 2002 → Held & Soden 2006 | CITES | OpenAlex. |

### P12 Abrupt change, AMOC, ice sheets, sea level

| A → B | Verdict | Evidence |
|---|---|---|
| Stommel 1961 → Rahmstorf 1995 | VERIFIED-CITES | Ref. 5 [P]. OpenAlex missed it because Stommel 1961 exists as three fragmented records (see §6). |
| Stommel 1961 → Lenton 2008 | VERIFIED-CITES | Ref. 45 [P]. Same cause. |
| Stommel 1961 → van Westen 2024 | VERIFIED-CITES | Among the 60 resolved references. The two-box model is cited across 63 years. |
| Broecker 1987 → Rahmstorf 1995 | VERIFIED-NO | Rahmstorf cites Broecker, Peteet & Rind 1985 (ref. 12), not "Unpleasant surprises" [P]. |
| Manabe & Stouffer 1988 → Rahmstorf 1995 → Stocker & Schmittner 1997 | CITES ×2 | OpenAlex. |
| Rahmstorf 1995; Broecker 1997 → Lenton 2008 | VERIFIED-NO ×2 | Lenton cites Rahmstorf 2002 (review), Rahmstorf et al. 2005 and Stocker & Schmittner 1997 (ref. 51); no Broecker paper [P]. Pattern (b). |
| Stocker & Schmittner 1997 → van Westen 2024 | VERIFIED-NO | Not among the 60 resolved references (Rahmstorf 1996/2005, Weijer 2019, Ditlevsen 2023 are). |
| Stocker & Schmittner 1997; van Westen 2024; Baker 2025 → van Westen, Börner & Dijkstra 2026 | VERIFIED-CITES ×2; VERIFIED-NO | The 2026 paper's 84 references, deposited at Crossref [P, 2026-10-01], cite Stocker & Schmittner 1997 and Schmittner & Stocker 1999 and the group's own 2024 paper, but neither Baker et al. 2025 nor Ditlevsen & Ditlevsen 2023. So the rate-dependence result was not rediscovered unawares — the 2026 paper acknowledges the 1997 origin — while the 2025 ensemble result that argued against collapse is not engaged. P12 amended. |
| Ditlevsen 2023 → van Westen 2024 → Baker 2025; Ditlevsen 2023 → Baker 2025 | CITES ×3 | OpenAlex — the 2023–25 AMOC exchange is a tight citation cluster. |
| Lenton 2008 → Armstrong McKay 2022 | CITES | OpenAlex. |
| DeConto & Pollard 2016 → Edwards 2019 | CITES | OpenAlex. |
| Rahmstorf 2007 → Pfeffer 2008 | VERIFIED-NO | Pfeffer's 21 references target Hansen 2007 ("Scientific reticence and sea level rise"; "Climate change and trace gases") and IPCC AR4; the semi-empirical paper is not cited. P12 presented the three 2007–08 answers as competing; they are, but Pfeffer's bound was aimed at Hansen's multi-metre scenarios, not Rahmstorf's. **Note added.** |
| Dansgaard 1993 → Broecker 1997 | CITES | OpenAlex. |

### P13 Predictability and internal variability

| A → B | Verdict | Evidence |
|---|---|---|
| Lorenz 1963 → Hasselmann 1976 | VARIANT | Hasselmann's 20 references (Tellus list read) cite Lorenz 1965 (predictability of a 28-variable model) and **Lorenz 1968 "Climate determinism"**, plus **J. M. Mitchell Jr. 1966** ("Stochastic models of air–sea interaction and climatic fluctuation", RAND memo), Budyko 1969 and Sellers 1969 [P]. The stochastic-climate idea descends from Lorenz's transitivity question and Mitchell's 1966 memo, not from the 1963 chaos paper. **Corrected.** |
| Hasselmann 1976 → Deser 2012 | VERIFIED-NO | Deser et al. (24 refs) cite Hawkins & Sutton 2009, 2011 and their own 2012 Clim. Dyn. paper; Hasselmann is not cited [P]. Pattern (c): the red-noise null is a textbook premise by 2012. |
| Hawkins & Sutton 2009 → Deser 2012 | CITES | OpenAlex and printed list. |
| Hasselmann 1976 → Cohn & Lins 2005 | VERIFIED-NO | Cohn & Lins's 29 references are Hurst 1951, Mandelbrot & Wallis 1968/1969, Klemeš 1974, Koutsoyiannis 2000/2003, Beran — the hydrological long-memory tradition; no Hasselmann [P]. |
| Cohn & Lins 2005 → Laepple & Huybers 2014 | VERIFIED-NO | Laepple & Huybers (47 refs) cite neither Cohn & Lins nor Hasselmann; their lineage is Huybers & Curry 2006 (the "continuum" spectrum) [P]. P13 grouped the two as "mainstream statements of the difficulty"; they are, but they come from **three separate traditions** (stochastic climate models; hydrological statistics; paleoclimate spectra) that do not cite one another. **Corrected.** |
| Laepple & Huybers 2014 → Laepple et al. 2023; → Parsons 2020 | CITES | Added 2026-10-01 for `08` §6: the field's own 2023 review and the CMIP6 variability paper both build on the 2014 result. |
| Cheung 2017 → Mann 2020; → Laepple 2023 | VERIFIED-CITES / CITES | Mann, Steinman & Miller 2020's printed list (nature.com) contains Cheung et al. 2017 [P]. |
| Kravtsov 2018 → Sippel 2021; → Olonscheck 2020 | CITES | The mainstream answers to the missing-global-mode claim cite it: Sippel et al. 2021 (*Science Advances*, detection robust to doubled variability) and Olonscheck, Rugenstein & Marotzke 2020 (*GRL*). |
| Kravtsov 2018 → Mann 2020 | VERIFIED-NO | Mann et al. 2020 (93 refs, nature.com list read) cite Kravtsov & Callicutt 2017 and Cheung 2017 but not Kravtsov, Grimm & Gu 2018, the strongest statement of the position they argue against [P]. Pattern (e), running from the mainstream side. |
| Kravtsov 2018 → Laepple et al. 2023 | VERIFIED-NO | The 2023 review's 105 references (nature.com list) do not include Kravtsov 2018 [P]; its global-scale conclusion (agreement) is reached without engaging the paper that disputes it. |

---

## 2. Premise quotations verified this pass

Quotations read from the primary text ([P]) in which a later paper takes an earlier result as its starting point. These are the direct evidence for criterion (B).

| Later paper | Premise adopted | Quotation |
|---|---|---|
| Solomon et al. 2009 (PNAS), introduction | Zero-emissions commitment ≈ 0 (Matthews & Caldeira 2008; Plattner 2008; AR4) | "It is not generally appreciated that the atmospheric temperature increases caused by rising carbon dioxide concentrations are not expected to decrease significantly even if carbon emissions were to completely cease (5–7)." And, as the paper's own result: "Global average temperatures increase while CO2 is increasing and then remain approximately constant (within ≈ ±0.5 °C) until the end of the millennium despite zero further emissions in all of the test cases shown in Fig. 1. This important result is due to a near balance between the long-term decrease of radiative forcing due to CO2 concentration decay and reduced cooling through heat loss to the oceans." |
| Mitchell et al. 1995 (Nature), abstract | Sulphate aerosols as the second-largest anthropogenic forcing (cited to IPCC 1994) and coupled GCMs over-predicting warming without them | "CLIMATE models suggest that increases in greenhouse-gas concentrations in the atmosphere should have produced a larger global mean warming than has been observed in recent decades, unless the climate is less sensitive than is predicted by the present generation of coupled general circulation models¹,². After greenhouse gases, sulphate aerosols probably exert the next largest anthropogenic radiative forcing of the atmosphere³ … The inclusion of sulphate aerosols significantly improves the agreement with observed global mean and large-scale patterns of temperature in recent decades." (Refs 1–3 are the IPCC 1990, 1992 and 1994 reports.) |
| Stouffer, Manabe & Bryan 1989 (Nature), abstract | Transient coupled experiments as the established problem (Bryan 1982 … Washington & Meehl 1989); the GISS approach as the alternative | "THE transient response of a coupled ocean–atmosphere model to an increase of atmospheric carbon dioxide has been the subject of several studies¹⁻⁸. The models used in these studies explicitly incorporate the effect of heat transport by ocean currents and are different from the model used by Hansen et al.⁹ … The model response exhibits a marked and unexpected interhemispheric asymmetry. In the circumpolar ocean of the Southern Hemisphere, a region of deep vertical mixing, the increase of surface air temperature is very slow." |
| Kiehl 2007 (GRL) | Models with diverse sensitivities all reproduce twentieth-century warming (the P03/P04 tuning concern) | "It is found that the total anthropogenic forcing for a wide range of climate models differs by a factor of two and that the total forcing is inversely correlated to climate sensitivity. Much of the uncertainty in total anthropogenic forcing derives from a threefold range of uncertainty in the aerosol forcing used in the simulations." … "These results explain to a large degree why models with such diverse climate sensitivities can all simulate the global anomaly in surface temperature. The magnitude of applied anthropogenic total forcing compensates for the model sensitivity." |
| MacDougall et al. 2020 (Biogeosciences), introduction | Matthews & Caldeira 2008 as the origin of the ZEC result | "Their experiments used the intermediate-complexity University of Victoria Earth System Climate Model (UVic ESCM) to show that stabilizing global temperature would require near zero CO2 emissions." … "Plattner et al. (2008) used a wide range of different Earth System Models of Intermediate Complexity (EMICs), following a similar experiment, and found that ZEC is close to (or less than) zero." [S: machine-read] |
| Manabe & Wetherald 1967 (J. Atmos. Sci.) | — (the result itself, checked against the P01 wording) | The text states the doubling response as "about 2.3C" (fixed relative humidity) and "about 1.3C" (fixed absolute humidity); 2.36 and 1.33 are the tabulated values [P, from the earlier part of this pass]. |
| Bellouin et al. 2020 (Rev. Geophys.) | — (result checked) | The 16–84 % range for total aerosol ERF is −1.6 to −0.6 W m⁻² [P], not "−0.65" as P06 had it. |
| NRC 2006, *Surface Temperature Reconstructions for the Last 2,000 Years* | — (assessment wording checked) | "Even less confidence can be placed in the original conclusions by Mann et al. (1999) that 'the 1990s are likely the warmest decade, and 1998 the warmest year, in at least a millennium' because the uncertainties inherent in temperature reconstructions for individual years and decades are larger than those for longer time periods" [P, from the earlier part of this pass]. |

Assessment-level premise statements (the IPCC SPMs, cycle by cycle) are tabulated with provenance in `06-assessment-language.md`.

---

## 3. Verdicts on the P-files' acceptance claims

The tests above bear on the P-files' claims as follows. "Stands" means the evidence gathered is consistent with the claim; "stands, lineage corrected" means the claimed acceptance is unaffected but the chain of papers the file drew has been changed.

| Claim (P-file) | Verdict |
|---|---|
| P01: radiative–convective result accepted by ~1970 (marker B) | **Stands.** Budyko 1969 and Schneider & Dickinson 1974 cite MW67; OpenAlex's early-adopter list for MW67 (Budyko 1969, Sellers 1969, Ingersoll 1969, Rasool & Schneider 1971, Sawyer 1972, Dickinson 1975) is exactly the set P01 names. |
| P02: Keeling's measurement settled the accumulation question | **Stands**, motive corrected: Keeling 1960 is a response to Callendar/Slocum/Revelle, not to Plass. |
| P03: the hierarchy became the field's epistemology (Schneider & Dickinson → Held) | **Stands**; Held 2005 cites the 1974 review in print (an OpenAlex indexing gap). |
| P03/P04: tuning-to-observations concern carried from Kiehl 2007 to Hourdin 2017 and Sherwood 2020 | **Stands** (citation chain confirmed). |
| P04: the pattern-effect chain Armour → Andrews → Gregory & Andrews → Sherwood | **Stands** (confirmed at every link). |
| P04: Sherwood 2020 as the anchor for both critics and the high-sensitivity camp | **Stands** (Lewis 2023 and Hansen 2023 both cite it). |
| P05: clouds as the dominant uncertainty from Cess onward | **Stands**; the paper carried forward is Cess 1990 (JGR), not the 1989 letter. |
| P06: Charlson 1992 as the paper that made aerosol forcing a first-order term | **Stands** (3861 citations; adopted in 1992–93 by Hansen 1997, Haywood 2000 …); but the detection papers of 1995–96 cite it *through* IPCC 1994 and Charlson & Wigley 1994 — see pattern (a). |
| P07: fingerprint method Hasselmann 1993 → Hegerl 1996 → Santer 1996 → Tett 1999 → Stott 2000 | **Stands** (every link confirmed, one as in-press). Santer 1996 cites the 1995 MPI report form of the method. |
| P08: hiatus literature as a resolved cluster (Medhaug 2017) | **Stands** (all four inputs cited). |
| P08: energy imbalance as the direct measurement (Hansen 2005 → Loeb 2021) | **Stands** as a claim about the quantity; Loeb does not cite Hansen 2005. |
| P09: Neukom 2019 as the current reference; MBH controversy closed | **Stands and strengthened**: the reference reconstruction no longer cites MBH98/99 or MM05 at all. |
| P10: ZEC ≈ 0 accepted 2008–2020 | **Stands**; Solomon 2009 explicitly builds on Matthews & Caldeira 2008. |
| P10: Hansen 1985 → Stouffer 1989 as steps in one line | **Corrected**: parallel GISS and GFDL lines. |
| P12: Stommel's two-box model as the origin of AMOC bistability | **Stands and strengthened**: cited in 1995, 2008 and 2024. |
| P12: Stocker & Schmittner 1997 rate-dependence "rediscovered" in 2024–26 | **Amended**: van Westen 2024 does not cite it, but the 2026 paper does — "returned to", not rediscovered. |
| P13: Hasselmann 1976 as the settled null hypothesis (marker E) | **Stands and strengthened**: by 2012 it is not even cited (Deser). |
| P13: Cohn & Lins and Laepple & Huybers as related statements of the variability problem | **Corrected**: three independent traditions. |

No claimed acceptance was overturned. Six lineages were corrected and seven notes were added; the corrections are listed next.

---

## 4. Corrections applied to the P-files (2026-09-30)

| File | Change |
|---|---|
| P01 | MW67 result: text now gives "about 2.3 °C … about 1.3 °C" as stated in the abstract, with 2.36/1.33 as the tabulated values. |
| P02 | §"Inheritance": Keeling 1960 cites Revelle & Suess, Callendar 1958, Bray 1959 and Slocum 1955, not Plass 1956; the sentence about Plass "making measurement worthwhile" was reworded. |
| P03 | Note that Held 2005 cites Schneider & Dickinson 1974 in print although OpenAlex misses it, and that Soden & Held 2006 anchor the feedback decomposition to Wetherald & Manabe 1988 / Colman 2003 rather than Hansen 1984. |
| P05 | Note that Cess et al. 1990 (JGR) is the paper cited by Bony & Dufresne 2005 and Soden & Held 2006. |
| P06 | Bellouin 2020 range corrected to −1.6 to −0.6 W m⁻². Note that Charlson 1992 cites Twomey 1984, and that Mitchell 1995 and Santer 1996 cite the aerosol forcing through IPCC 1994 and Charlson & Wigley 1994. |
| P07 | Note on the forms in which Santer 1996 cites its inputs (Hegerl in press; Hasselmann et al. 1995 MPI report; Charlson & Wigley 1994; Mitchell 1995), and that McKitrick & Christy 2018 does not cite Santer 2017. |
| P08 | Note that Loeb 2021 cites von Schuckmann 2016/2020 rather than Hansen 2005; Mears & Wentz 2005 cite Christy 2000/2003 rather than Spencer & Christy 1990. |
| P09 | NRC 2006 wording added ("even less confidence … Mann et al. (1999)"); note that Neukom 2019 cites neither MBH98/99 nor MM05. |
| P10 | Hansen 1985 and Stouffer 1989 re-described as parallel lines; Solomon 2009's premise sentence quoted. |
| P12 | Notes: Rahmstorf 1995 cites Broecker 1985 not 1987; Lenton 2008 cites Stocker & Schmittner 1997 and Rahmstorf 2002/2005; Pfeffer 2008 targets Hansen 2007; van Westen 2024 does not cite Stocker & Schmittner 1997. |
| P13 | Hasselmann 1976's cited antecedents corrected (Lorenz 1968, Mitchell 1966; not Lorenz 1963); Cohn & Lins / Laepple & Huybers / Hasselmann described as three non-citing traditions; note that Deser 2012 does not cite Hasselmann. |

---

## 5. Patterns in how acceptance is carried

The non-citations are more informative than the citations, because they show what "building on" a result looks like once the result is no longer new.

**(a) The assessment as citation carrier.** Mitchell et al. 1995 cite IPCC 1994 for the magnitude of sulphate forcing and IPCC 1990/1992 for the models-warm-too-much premise; Santer 1996 cites the SAR chapter and a *Scientific American* article rather than Charlson 1992. By 1995 the assessment had become the canonical reference for a result three years old. This is the mechanism by which the IPCC "formalizes" consensus at the level of the working literature: it becomes the thing one cites. It also means that a citation-count test of criterion (B) *under-counts* adoption of any result the IPCC has absorbed — relevant to the traces in `05-citation-traces.md` and to the IPCC-role strand (`07-ipcc-role.md`).

**(b) The superseded anchor.** Later papers cite the most recent statement of a lineage rather than its origin: Neukom 2019 cites Mann 2008/2009 and PAGES 2k, not MBH98; Loeb 2021 cites von Schuckmann 2016/2020, not Hansen 2005; Lenton 2008 cites Rahmstorf 2002/2005 and Stocker & Schmittner 1997, not Rahmstorf 1995 or Broecker 1997; Bony & Dufresne 2005 cite Cess 1990, not 1989; Charlson 1992 cites Twomey 1984, not 1977; Mears & Wentz 2005 cite Christy 2000/2003, not Spencer & Christy 1990. A result that has been *re-stated* by its own authors or by an assessment migrates to the newer statement. Consequence for method: the citation curve of an origin paper flattens or falls precisely when its result is most accepted (see the Santer 1996, Mitchell 1995 and Cess 1989 curves in `05-citation-traces.md`), so a falling curve is not evidence of rejection.

**(c) The textbook premise.** Deser 2012 uses the red-noise null without citing Hasselmann 1976; Soden & Held 2006 decompose feedbacks without citing Hansen 1984. These are results that have reached criterion (C): they are no longer attributed. Marker (B) has an expiry date; after it, absence of citation is the evidence.

**(d) Parallel lineages the P-files had fused.** The stochastic-climate-model tradition (Hasselmann), the hydrological long-memory tradition (Hurst–Mandelbrot–Koutsoyiannis–Cohn & Lins) and the paleoclimate spectral tradition (Huybers & Curry–Laepple & Huybers) each argue that natural variability is redder than assumed, and none cites the others. The GISS (Hansen 1981/1984/1985/1988) and GFDL (Bryan 1982, Manabe & Stouffer 1988, Stouffer 1989) transient-response lines cite each other sparingly. Where the P-files described "the field" converging, some of what converged was independent arrival at the same place, which is stronger evidence of acceptance than a citation chain would be — and is exactly the kind of evidence the "manufactured consensus" claim would have to explain away (`08-manufactured-consensus.md`).

**(e) Non-engagement across camps.** McKitrick & Christy 2018 does not cite Santer et al. 2017, the mainstream analysis of the same discrepancy published the year before; Lewis 2023 cites Sherwood 2020 (as its target), and Hansen 2023 cites Sherwood 2020 (as its foil). Whether a critique cites the paper it disputes is itself a datum for the later strands: the sensitivity debate is conducted as a single conversation; the tropical-troposphere debate is, in part, two literatures. The internal-variability exchange (added 2026-10-01) is mixed: Sippel 2021 and Olonscheck 2020 answer Kravtsov 2018 and cite it, but Mann 2020 and Laepple 2023 argue against its conclusion without citing it — the two non-citations found in this strand both run from the mainstream side (`08` §6).

---

## 6. Caveats on the method

- **OpenAlex reference lists are incomplete for older papers and for in-press citations.** MW75, Sellers 1969, Twomey 1977, Broecker 1987, Charney 1979 and Stommel 1961 have no indexed references at all; Hansen 1981 has 53 of roughly 90. Seven of the 48 "NOT-IN-REFS" verdicts were indexing gaps (and three of the 83 "CITES" verdicts were re-confirmed from the printed lists). A NOT-IN-REFS verdict from OpenAlex alone should be read as "not confirmed", never as "does not cite".
- **Fragmented records.** OpenAlex holds Stommel 1961 as three records (1330 + 760 + 34 citations), Hasselmann 1976 as two (1424 + 979), Budyko 1969 as two (1434 + 1041), Keeling 1960 as two (508 + 324), Plass 1956 as two (251 + 126). Citation counts and curves in `05-citation-traces.md` merge these; pair tests were re-checked against the alternates. `data/openalex-traces.json` lists the duplicate ids.
- **What could not be read.** *Science* (Cloudflare challenge) and the AMS journals (CloudFront block) refuse automated reading, so pairs whose B is in those venues (MW75, Hansen 1981/1985, Charlson 1992 as B, Pfeffer 2008, Mears & Wentz 2005, Sabine 2004, Soden & Held 2006, Hasselmann 1993) were checked through OpenAlex's resolved reference titles and, on 2026-10-01, through the publishers' reference deposits at Crossref, which the browser on Steve's computer can reach; the Crossref lists are complete for Hansen 1981 (69 entries), Pfeffer 2008, Mears & Wentz 2005, Sabine 2004 and Soden & Held 2006 and confirmed every verdict in those rows, but are empty for MW75, Sellers 1969, Held 2005, Hasselmann 1993 and Lindzen 1990. (Held 2005 could be read from the GFDL preprint, which is how its indexing gap was caught.) Those are reliable when the count of indexed references is close to the printed count (it is for all of these except MW75 and Hansen 1981) but cannot show in-press or report citations.
- **Scope.** 131 pairs and eight premise quotations are a sample of the P-files' claims, weighted toward the transitions the README singled out. The P-files name several hundred papers; most of their lineages are untested here. The scripts in `scripts/` reproduce the pair test for any list of DOIs.
