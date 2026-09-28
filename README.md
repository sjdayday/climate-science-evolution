# The evolution of climate science: problems, papers, and acceptance

**Status:** first pass (v0.1), 2026-09-27. This is a working analysis, meant to be revised.

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
| `timeline.md` | — | Compact chronology of papers, assessments, and events. |
| `references.md` | — | Bibliography of every paper cited (author, year, title, venue). |

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

**Sources for this pass.** The analysis synthesizes the primary literature as it is represented in the standard histories and assessments — Weart's *The Discovery of Global Warming* (and its online expansion), Fleming's *Historical Perspectives on Climate Change*, Edwards's *A Vast Machine*, Manabe & Broccoli's *Beyond Global Warming*, the six IPCC assessment cycles, and the NAS/NRC reports — together with the papers themselves where I know them. Specific numbers and dates that seemed at risk were checked against the papers or reliable secondary sources during drafting; the most recent developments (2023–2026) were checked against the literature as of mid-2026. **It is not a citation-network analysis.** Statements of the form "the field adopted X by about year Y" are judgments, and the evidence for them is stated so they can be checked and overturned.

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
- `ABANDONED` — a once-live answer that the field dropped.

**Distinctions kept throughout.** Consensus on a *framework* (e.g., forcing–feedback analysis), on a *sign* (warming, not cooling), on a *magnitude* (about 3 °C per doubling), and on a *range* (2.5–4 °C) are different things that were reached at different times. The files try to say which is meant.

**Scope.** The project brief begins mid-twentieth century. The files go back to 1824–1938 because the problems of the 1950s were answers to objections raised before 1940; nothing is gained by starting the story with the objections already forgotten.

## Conventions

- Papers are cited inline as `Author (Year)` and listed in `references.md`. Where a paper is discussed at length its full title appears in the P-file.
- "Doubling" means a doubling of atmospheric CO₂ from a pre-industrial baseline unless stated otherwise; "ECS" is equilibrium climate sensitivity, "TCR" transient climate response, "ERF" effective radiative forcing.
- IPCC reports: FAR (1990), SAR (1995/96), TAR (2001), AR4 (2007), AR5 (2013/14), SR15 (2018), AR6 (2021–23).
- Dates of "acceptance" are given as approximate ranges, with the marker.

## How this analysis is meant to evolve

Natural next passes, roughly in order of value:

1. **Check the acceptance claims against the primary papers.** Each P-file names the papers whose introductions or methods should show premise-adoption; reading them is the direct test.
2. **Citation-trace the key transitions.** OpenAlex or Semantic Scholar can supply citation counts and citing-paper lists for the pivotal papers (e.g., Manabe & Wetherald 1967; Hasselmann 1976; Hays et al. 1976; Charlson et al. 1992; Santer et al. 1996; Matthews et al. 2009; Sherwood et al. 2020), which would replace judgment with data for criterion (B).
3. **Tabulate assessment language across cycles.** The IPCC's calibrated statements on attribution, sensitivity, sea level, and AMOC changed cycle by cycle; a table would make the "formalizing vs. asserting" question in the project brief tractable.
4. **Add the IPCC-role and manufactured-consensus strands** as separate files, using the flashpoint notes in the P-files as the index.
5. **Fill in `references.md`** with volume/page/DOI (currently author–year–title–venue).

## Revision log

- **v0.1 — 2026-09-27.** First pass: README, periodization, thirteen problem files, open-problems file, timeline, references. Written by Claude at Steve's request; everything here should be treated as a draft to be checked, not a source.
