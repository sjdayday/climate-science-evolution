# The evolution of climate science: problems, papers, and acceptance

**Status:** second pass (v0.2), 2026-09-30. This is a working analysis, meant to be revised.

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
| `04-acceptance-checks.md` | Q2 (test) | Item 1 of the evolution list: 123 citation-link tests of the lineages the P-files draw (OpenAlex `referenced_works`, then the printed reference lists), eight premise quotations read from the primary texts, the corrections applied to the P-files, and five patterns in how acceptance is carried in the literature. |
| `05-citation-traces.md` | Q2 (test) | Item 2: year-by-year citation curves for all 137 pivotal papers and the early adopters of 77 of them (OpenAlex), compared with the acceptance dates and adopters the P-files claim; curve shapes; the citation record of the principal dissenting papers. |
| `06-assessment-language.md` | Q2/strand | Item 3: the IPCC's calibrated statements (FAR–AR6, plus Charney 1979 and NRC 2006) on attribution, sensitivity, projections and sea level, AMOC, paleoclimate, observed warming and commitment, quoted verbatim from the reports with provenance tags. |
| `07-ipcc-role.md` | strand (scaffold) | Item 4: whether the assessments formalized, lagged, or ran ahead of the literature's own premise adoption, problem by problem and cycle by cycle; evidence so far and work to do. |
| `08-manufactured-consensus.md` | strand (scaffold) | Item 4: the manufactured-consensus claim in its institutional, sociological, epistemic and rhetorical forms; which components the record can test and what it shows; where the claim is strongest. |
| `timeline.md` | — | Compact chronology of papers, assessments, and events. |
| `references.md` | — | Bibliography of every paper cited, now with volume, issue, pages and DOI for 665 of the 681 journal entries (item 5). |
| `data/` | — | `openalex-traces.json` (curves and early adopters), `citation-pairs.json` (the 123 link tests with verdicts and notes), `s2-traces.json` (Semantic Scholar cross-check, 8 papers), `pivotal-openalex.csv` (the 137 pivotal papers with DOIs and OpenAlex ids), `pivotal-resolved.csv`, `references-resolved.csv` (match scores for every DOI). |
| `scripts/` | — | `openalex_traces.py`, `resolve_dois.py`, `openalex_common.py`: regenerate the data files from OpenAlex (`OPENALEX_API_KEY` read from the environment; never stored). |

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

1. **Check the acceptance claims against the primary papers** — done for 123 lineages and eight premise quotations (`04-acceptance-checks.md`). Remaining: most of the several hundred lineages the P-files imply are untested; *Science* and AMS full texts could not be read in this pass, so premise quotations from those venues are missing.
2. **Citation-trace the key transitions** — done for all 137 pivotal papers (`05-citation-traces.md`, `data/openalex-traces.json`). Remaining: the venue breakdown of citers (who adopts — modellers, paleoclimatologists, economists) was read from titles, not classified; the consensus-measurement papers' citers have not been pulled.
3. **Tabulate assessment language across cycles** — done (`06-assessment-language.md`); the AR4/AR6 projection ranges and the TAR/AR4 millennium sentences were extracted from the SPM PDFs; the SAR SPM sea-level range and the AR6 Table SPM.1 best estimates are still tagged [M].
4. **The IPCC-role and manufactured-consensus strands** — scaffolded (`07`, `08`) with the evidence from 04–06 and a work list in each; the primary statements of the claim (Seitz 1996, Wegman 2006, the 2010 inquiries, Koonin 2021) have not yet been read for this project.
5. **`references.md` with volume/page/DOI** — done for 665 of 681 journal entries; 24 DOIs were supplied from memory and are marked; 14 entries (book chapters, reports) have no DOI.

Next passes, in order of value: the SPM-versus-chapter comparison in `07` §4; the unread primary sources for `08` §4; P13's internal-variability problem written up as the strongest skeptical case; premise quotations from the *Science*/AMS papers once a route to their full text exists.

## Revision log

- **v0.1 — 2026-09-27.** First pass: README, periodization, thirteen problem files, open-problems file, timeline, references. Written by Claude at Steve's request; everything here should be treated as a draft to be checked, not a source.
- **v0.2 — 2026-09-30.** Second pass, the five items above: `04-acceptance-checks.md`, `05-citation-traces.md`, `06-assessment-language.md`, scaffolds `07-ipcc-role.md` and `08-manufactured-consensus.md`, `data/` and `scripts/`, `references.md` with DOIs. Corrections applied to P01–P10, P12 and P13 are listed in `04` §4 and `05` §5; no claimed acceptance was overturned, six lineages were corrected. Data sources: OpenAlex (queried with Steve's API key, which is not stored in any file) and Semantic Scholar; publisher pages for reference lists; IPCC PDFs for `06`. Housekeeping: the empty `_to_delete/nested-unzip-2026-09-28/` folder left by the first delivery can be deleted.
