# The evolution of climate science: problems, papers, and acceptance

**Status:** sixth pass (v0.6), 2026-10-01. This is a working analysis, meant to be revised.

## Purpose

This folder characterizes the evolution of climate science — chiefly the science of greenhouse-gas–driven climate change, from its late-nineteenth-century roots through mid-2026 — in terms of three questions:

1. **Problems by period.** What were the important problems at each stage, why did their solutions matter, and how did later problems grow out of earlier ones?
2. **Papers and acceptance.** For each problem, which papers proposed answers, how did competing answers differ, and which answer was accepted — explicitly or implicitly — and roughly when?
3. **Open problems.** Which problems still have no widely accepted answer, how has the discussion of each evolved, and what are the stakes?

A separate, later strand of the project will examine the IPCC's role in formalizing (or prematurely asserting) consensus and the skeptical community's claim that consensus was manufactured. The files here are written to support that strand: wherever a problem became a public flashpoint, the relevant file has a short section flagging it, but the flashpoints are not analysed here.

## How the files are organized

| File | Answers | Contents |
|---|---|---|
| `README.md` | — | This file: scope, method, conventions, status. |
| `01-periods.md` | Q1 | Periodization (seven periods). For each: the central problems, why they mattered, what was inherited from the previous period and handed to the next. Includes an explicit treatment of the one-dimensional → three-dimensional model lineage. |
| `02-problems/P01…P13` | Q2 | One file per problem cluster. Each has the same skeleton: the problem; why it mattered; the key papers and competing answers in chronological order; what was accepted, when, and on what evidence; inheritance to/from other problems; what remains open; flashpoint notes. |
| `03-open-problems.md` | Q3 | The problems without a widely accepted answer, how each discussion evolved, and the stakes. Cross-references the P-files. |
| `04-acceptance-checks.md` | Q2 (test) | Item 1 of the evolution list: 131 citation-link tests of the lineages the P-files draw (OpenAlex `referenced_works`, then the printed reference lists), eight premise quotations read from the primary texts, the corrections applied to the P-files, and five patterns in how acceptance is carried in the literature. |
| `05-citation-traces.md` | Q2 (test) | Item 2: year-by-year citation curves for all 137 pivotal papers and the early adopters of 77 of them (OpenAlex), compared with the acceptance dates and adopters the P-files claim; curve shapes; the citation record of the principal dissenting papers. |
| `06-assessment-language.md` | Q2/strand | Item 3: the IPCC's calibrated statements (FAR–AR6, plus Charney 1979 and NRC 2006) on attribution, sensitivity, projections and sea level, AMOC, paleoclimate, observed warming and commitment, quoted verbatim from the reports with provenance tags. |
| `07-ipcc-role.md` | strand | Item 4: whether the assessments formalized, lagged, or ran ahead of the literature's own premise adoption, problem by problem and cycle by cycle — as a judgment table (§3) and as a table generated from the citation record (§3.1: for each cell, whether the anchoring papers had reached 25 citations before the summary was approved); (§4) the SPM-versus-chapter test — twenty-four comparisons across FAR–AR6 with the chapters' own sentences quoted; (§4.1) the prominence test — what each SPM drew and put first, for attribution, sensitivity, the millennium and sea level, against the chapters' own figures; and (§4.2) the same test for the Working Group II and III summaries — observed-impact attribution, the reasons for concern and their "burning embers" figure, mitigation costs, and benefits against costs — fourteen comparisons, TAR–AR6. |
| `08-manufactured-consensus.md` | strand | Item 4: the manufactured-consensus claim in its institutional, sociological, epistemic and rhetorical forms; which components the record can test and what it shows; the claim's primary statements, read in the original (§4: Seitz 1996 in full, the Wegman report in full, Curry 2017, Lindzen 2008; Edwards & Schneider 1997); what the 2010–11 inquiries found (§5, with Muir Russell read in full); the observational-record adjustments by sign; and the claim's best case — the internal-variability problem — read from its papers (§6). |
| `timeline.md` | — | Compact chronology of papers, assessments, and events. |
| `references.md` | — | Bibliography of every paper cited, with volume, issue, pages and DOI for 670 of the 686 journal entries, all machine-verified against OpenAlex (item 5); the inquiry reports and primary statements used in `08` are listed under assessments and reports. |
| `data/` | — | `openalex-traces.json` (curves and early adopters), `citation-pairs.json` (the 131 link tests with verdicts and notes), `s2-traces.json` (Semantic Scholar cross-check, 8 papers), `pivotal-openalex.csv` (the 137 pivotal papers with DOIs and OpenAlex ids), `pivotal-resolved.csv`, `references-resolved.csv` (match scores for every DOI), `citer-fields.json` (field, domain and venue breakdown of the citers of the consensus-measurement papers and eighteen pivotal physical papers), `problem-cycle.json` (the `07` §3.1 table: anchoring papers, their 25-citation years and the relation to each SPM's cutoff). |
| `scripts/` | — | `openalex_traces.py`, `resolve_dois.py`, `openalex_common.py`: regenerate the data files from OpenAlex; `problem_cycle.py` builds the `07` §3.1 table from the traces file offline. The API key is read from the environment variable `OPENALEX_API_KEY`, or else from a `.env` file at the repository root (`OPENALEX_API_KEY=…`), which `.gitignore` excludes; it is never written into any file here. |

Problem clusters (`02-problems/`):

- **P01** Does added CO₂ change the radiation balance at all? (saturation, water-vapour overlap, the radiative basis)
- **P02** Does emitted CO₂ accumulate? (ocean uptake, the airborne fraction, the carbon cycle)
- **P03** How should the response be computed? (the model hierarchy: 1-D radiative–convective and energy-balance models → GCMs → coupled models → Earth-system models)
- **P04** What is the equilibrium climate sensitivity?
- **P05** Feedbacks (water vapour, lapse rate, clouds, surface albedo)
- **P06** Radiative forcing (trace gases, aerosols, the forcing–feedback framework)
- **P07** Detection and attribution (is warming detectable, and is it anthropogenic?)
- **P08** The observational record (surface, satellite, ocean heat, the "hiatus")
- **P09** Paleoclimate as test and constraint (ice ages, ice cores, the last millennium)
- **P10** Transient response, ocean heat uptake, commitment, and cumulative emissions
- **P11** The hydrological cycle, circulation, regional change, and extremes
- **P12** Abrupt change, tipping points, ice sheets, and sea level
- **P13** Predictability, internal variability, and climate as a statistical object

## Method, and what this first pass is and is not

**Sources for this pass.** The analysis synthesizes the primary literature as it is represented in the standard histories and assessments — Weart's *The Discovery of Global Warming* (and its online expansion), Fleming's *Historical Perspectives on Climate Change*, Edwards's *A Vast Machine*, Manabe & Broccoli's *Beyond Global Warming*, the six IPCC assessment cycles, and the NAS/NRC reports — together with the papers themselves where I know them. Specific numbers and dates that seemed at risk were checked against the papers or reliable secondary sources during drafting; the most recent developments (2023–2026) were checked against the literature as of mid-2026. **The P-files are not a citation-network analysis**; statements of the form "the field adopted X by about year Y" are judgments, and the evidence for them is stated so they can be checked and overturned. In v0.2 they were checked against citation data and the primary texts for the transitions singled out here (`04`, `05`), which is why several lineages now carry a parenthetical correction.

**Criteria for "accepted."** Acceptance is judged by five kinds of evidence, in roughly descending order of how explicit they are:

- **(A) Assessment endorsement.** A NAS/NRC panel or IPCC assessment states the conclusion, with calibrated language where available.
- **(B) Premise adoption.** Later papers cite the result and build on it — using it as a boundary condition, a parameter, or a starting assumption — instead of re-deriving or contesting it. This is the "implicit acceptance" of the project brief and is usually the earliest marker.
- **(C) Textbook incorporation.** The result appears as settled in graduate texts (e.g., Peixoto & Oort 1992; Hartmann 1994/2016; Pierrehumbert 2010).
- **(D) Disappearance of the alternative.** The competing answer stops appearing in the specialist peer-reviewed literature, or migrates to non-specialist venues.
- **(E) Operational adoption.** The result is built into tools everyone uses (a radiation code, a convective scheme, a forcing formula, a dataset).

Each P-file gives the marker(s) that support the claimed acceptance date.

**Status labels** used in the P-files and in `03-open-problems.md`:

- `SETTLED` — accepted for decades; no active research programme contests it.
- `ACCEPTED` — accepted by the field; work continues on refinements or edges.
- `CONTESTED-WITHIN` — mainstream disagreement about magnitude or mechanism, with a shared framework.
- `OPEN` — no widely accepted answer.
- `RESOLVED` — a specific controversy (as opposed to a standing problem) closed by identifiable findings.
- `ABANDONED` — a once-live answer that the field dropped.

**Distinctions kept throughout.** Consensus on a *framework* (e.g., forcing–feedback analysis), on a *sign* (warming, not cooling), on a *magnitude* (about 3 °C per doubling), and on a *range* (2.5–4 °C) are different things that were reached at different times. The files try to say which is meant.

**Scope.** The project brief begins mid-twentieth century. The files go back to 1824–1938 because the problems of the 1950s were answers to objections raised before 1940; nothing is gained by starting the story with the objections already forgotten.

## Conventions

- Papers are cited inline as `Author (Year)` and listed in `references.md`. Where a paper is discussed at length its full title appears in the P-file.
- "Doubling" means a doubling of atmospheric CO₂ from a pre-industrial baseline unless stated otherwise; "ECS" is equilibrium climate sensitivity, "TCR" transient climate response, "ERF" effective radiative forcing.
- IPCC reports: FAR (1990), SAR (1995/96), TAR (2001), AR4 (2007), AR5 (2013/14), SR15 (2018), AR6 (2021–23).
- Dates of "acceptance" are given as approximate ranges, with the marker.

## How this analysis is meant to evolve

The five passes proposed in v0.1 were made in v0.2 (2026-09-30); their state and what remains:

1. **Check the acceptance claims against the primary papers** — done for 131 lineages and eight premise quotations (`04-acceptance-checks.md`). Remaining: most of the several hundred lineages the P-files imply are untested; *Science* and AMS full texts could not be read in this pass, so premise quotations from those venues are missing.
2. **Citation-trace the key transitions** — done for all 137 pivotal papers (`05-citation-traces.md`, `data/openalex-traces.json`). Remaining: the venue breakdown of citers (who adopts — modellers, paleoclimatologists, economists) was read from titles, not classified; the consensus-measurement papers' citers have not been pulled.
3. **Tabulate assessment language across cycles** — done (`06-assessment-language.md`); the AR4/AR6 projection ranges, the TAR/AR4 millennium sentences and the SAR sea-level range were extracted from the SPM PDFs; the SAR sensitivity quotation is now correctly attributed to the Technical Summary (the SAR SPM states no range); the AR6 Table SPM.1 best estimates are still tagged [M].
4. **The IPCC-role and manufactured-consensus strands** — `07` carries the SPM-versus-chapter test (§4), the prominence test (§4.1) and the Working Group II/III test (§4.2); `08` the claim's primary statements read in the original (§4), the inquiry findings with Muir Russell read in full (§5), and the internal-variability problem read as the claim's best case (§6), each with a remaining-work list; the problem × cycle table is now filled both by judgment (`07` §3) and from the citation record (§3.1); the Synthesis Reports and the WG II regional findings are untouched.
5. **`references.md` with volume/page/DOI** — done for 670 of 686 journal entries, all verified against OpenAlex records; 14 entries (book chapters, reports) have no DOI.

Next passes, in order of value: the Synthesis Reports against the three working-group summaries; the IAC 2010 report and the *Nature* editorial of 13 June 1996 in the original, and the critics' objections to the 2010 inquiries sourced; Cheung 2017 and Laepple 2023 in full text; premise quotations from the *Science*/AMS papers once a route to their full text exists; the remaining UNVERIFIABLE pairs (Manabe & Wetherald 1975 as a citer; Budyko → Sellers).

## Revision log

- **v0.1 — 2026-09-27.** First pass: README, periodization, thirteen problem files, open-problems file, timeline, references. Written by Claude at Steve's request; everything here should be treated as a draft to be checked, not a source.
- **v0.2 — 2026-09-30.** Second pass, the five items above: `04-acceptance-checks.md`, `05-citation-traces.md`, `06-assessment-language.md`, scaffolds `07-ipcc-role.md` and `08-manufactured-consensus.md`, `data/` and `scripts/`, `references.md` with DOIs. Corrections applied to P01–P10, P12 and P13 are listed in `04` §4 and `05` §5; no claimed acceptance was overturned, six lineages were corrected. Data sources: OpenAlex (queried with Steve's API key, which is not stored in any file) and Semantic Scholar; publisher pages for reference lists; IPCC PDFs for `06`. Housekeeping: the empty `_to_delete/nested-unzip-2026-09-28/` folder left by the first delivery can be deleted.
- **v0.3 — 2026-09-30.** Third pass. `07` §4: the SPM-versus-chapter test (twenty-four comparisons, FAR–AR6, chapters read from the PDFs; no SPM raised a chapter's likelihood; the TAR's decade/year millennium sentence was the chapter's own). `08` §4–5: the claim's primary statements (Seitz 1996, the GCC pamphlet, Edwards & Schneider 1997, Wegman 2006, Lindzen 2008, Curry 2017, Koonin 2014/2021) and the findings of the eight inquiries of 2010–11 plus the IAC review, with the observational-record adjustments tabulated by sign. `data/citer-fields.json` and `08` §2.4: 51–74 per cent of the consensus-measurement papers' citers are social-science works, against 83–99 per cent physical for the pivotal science papers. `references.md`: the 24 from-memory DOIs verified. Corrections: the Schneider & Dickinson 1974 → Held 2005 verdict in `04` and P03 (Held cites the review; OpenAlex had missed it); `06`'s SAR sea-level range and AR6 AMOC reasoning now [P]. Scripts read the key from `.env` when the environment variable is unset.
- **v0.4 — 2026-10-01.** Fourth pass. `07` §4.1: the prominence test — across the six WG I summaries, attribution rose from the last section (1990) to the first headline (2021) a cycle behind the chapters; the sensitivity range was absent from the SAR SPM and confined to a footnote in the TAR's, and AR5 put its withdrawn best estimate in a footnote; the millennium figure was the TAR's one over-promotion (the single Mann et al. 1999 reconstruction as the report's first figure, in place of the chapter's three-reconstruction comparison), dropped entirely in AR4 and AR5, restored with uncertainty bands in AR6. `08` §6: the internal-variability problem read as the claim's best case — Laepple & Huybers 2014, Kravtsov 2018, Scaife & Smith 2018 and Mann 2020 in full, Cheung 2017, Parsons 2020, Laepple 2023 and Sippel 2021 by abstract, with the assessments' own treatment (AR4 ch. 9, AR5 ch. 10, AR6 ch. 3); the regional under-simulation is conceded by the field, the global claim answered by evidence independent of the models' control-run variance; two non-citations found, both from the mainstream side (eight pairs added to `04` and `data/citation-pairs.json`). `08` §4–5: Seitz 1996 read in full and its three deleted sentences checked against the printed SAR chapter 8 (absent, with equivalent hedges in the chapter's Summary); the Wegman report read in full (its own findings 7 and 10 and its House-committee answers quoted, including "the paleoclimate results of MBH98/99 are essentially irrelevant to the consensus on climate change"); the Muir Russell report read in full (Executive Summary §§13–27, chapter 8 §18, chapter 9 on Wahl & Ammann). Corrections: `06`'s SAR sensitivity row re-attributed to the Technical Summary; P13, `03` §10 and `08` §2 updated accordingly. Four references added with OpenAlex-verified volume and DOI; the inquiry reports listed. OpenAlex usage this pass was small (about $0.002 of the daily $1 limit); the key was used only in the browser.
- **v0.5 — 2026-10-01.** Fifth pass. `07` §4.2: the Working Group II and III summaries against their chapters, fourteen comparisons from the TAR to AR6 read from the PDFs — observed-impact attribution (four cycles), the reasons for concern and the embers figure (four cycles), mitigation-cost headlines (four cycles) and AR6's benefits-against-costs statement. Ten matched; AR6 WG III's headline stated unconditionally what chapter 3 stated conditionally (restored in the sub-statement); AR6 WG II's headline compressed an attribution chain its sub-statements keep; the TAR summary coloured a figure the chapter drew in grey; and the AR4 embers were kept out of the summary at the government stage, by the authors' account at the insistence of four governments — the one documented intervention in a figure, running toward less. The AR4 WG II SPM is confirmed not to carry the Himalayan-glacier date. Sources: Smith et al. 2009 (*PNAS*) read; Schneider's account via a secondary quotation [S].
- **v0.6 — 2026-10-01.** Sixth pass. `07` §3.1: the problem × cycle table generated from the citation record (`scripts/problem_cycle.py`, `data/problem-cycle.json`) — for 43 cells, which pivotal papers anchor each assessment statement and whether they had reached 25 citations before the summary's approval year. Twenty-two cells formalized with lags of 0–16 years, twelve "level" (adopted within a year of publication, nine of them in AR4–AR6), six contested papers engaged, and no cell in which a summary stated a result before its anchoring paper was in print; the FAR detection and AR4 ice-dynamics cells confirmed as the two in which the summary declined a result in print. The AR4 sensitivity cell corrected (Knutti & Hegerl 2008 postdates AR4).
