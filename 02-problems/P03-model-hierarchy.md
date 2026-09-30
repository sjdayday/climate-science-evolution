# P03 — How should the response be computed? The model hierarchy

**Active:** 1956–present · **Status:** `ACCEPTED` (GCMs as the primary instrument; the hierarchy as the interpretive framework); `CONTESTED-WITHIN` (model evaluation, tuning, weighting, resolution) · **Related:** P01 (origin), P04/P05 (what the models are used to estimate), P13 (ensembles and variability)

## The problem

Given that CO₂ changes the radiation balance, how should the resulting change in climate be *computed*? The problem has three layers: which physical processes must be represented (radiation, convection, the hydrological cycle, ocean circulation, ice, the carbon cycle); how to represent processes that occur below the resolution of any feasible model (clouds, convection, turbulence); and how to know whether a model's answer is right when the experiment it simulates has not yet happened.

## Why the solution mattered

The models are the field's instrument for every quantitative question in this project: the sensitivity, the feedbacks, the fingerprints used in attribution, the regional projections, the carbon budgets. Their credibility is also the primary target of the manufactured-consensus claim, which holds that models are tuned to produce the expected answer. The history bears on that claim directly, because it shows *which* results depend on which modelling choices, and which results were obtained by models of very different construction.

## Key papers and competing answers

### The three roots (1956–1969)

**General circulation.** Phillips (1956) ran the first numerical general-circulation experiment (a two-layer hemispheric model on the IAS computer); Smagorinsky (1963) built the GFDL primitive-equation model; **Manabe, Smagorinsky & Strickler (1965)** added a hydrological cycle and radiation. Parallel efforts: Mintz and Arakawa at UCLA (1965), Leith at Livermore (1965), Kasahara and Washington at NCAR (1967). None of these were about CO₂; they were weather models run long.

**The vertical column.** Manabe & Möller (1961), Manabe & Strickler (1964), and **Manabe & Wetherald (1967)** — the radiative–convective model described in P01. Its two structural choices — a radiative transfer scheme and a *moist convective adjustment* that restores the lapse rate to a critical value — became the GFDL GCM's physics.

**The horizontal line.** **Budyko (1969)**, *The effect of solar radiation variations on the climate of the Earth* (Tellus), and **Sellers (1969)**, *A global climatic model based on the energy balance of the Earth–atmosphere system* (J. Appl. Meteorol.), independently built one-dimensional (latitude) energy-balance models with a temperature-dependent ice line. Both found that a few per cent reduction in solar constant would send the model to a fully glaciated state — the *ice–albedo instability* — and that the present climate was closer to that threshold than anyone had supposed. North (1975) and Held & Suarez (1974) gave the models a rigorous form. These models introduced multiple equilibria, hysteresis, and the "feedback factor" way of thinking that the field still uses.

**Coupling.** **Manabe & Bryan (1969)**, *Climate calculations with a combined ocean–atmosphere model* (J. Atmos. Sci.), joined the GFDL atmosphere to Bryan's ocean model in a sector geometry. The ocean took centuries to equilibrate; the paper established both the necessity and the cost of coupling.

### The hierarchy as a concept (1974–2005)

**Schneider & Dickinson (1974)**, *Climate modeling* (Rev. Geophys. Space Phys.), is the review that named the *hierarchy* — energy-balance, radiative–convective, statistical-dynamical, and general-circulation models — and argued that its levels answer different questions. **Held (2005)**, *The gap between simulation and understanding in climate modeling* (BAMS), restated the case thirty years later, arguing that the field had let its comprehensive models outrun its ability to understand them and needed to cultivate the intermediate rungs. The two papers bracket the period in which the hierarchy went from a research strategy to the accepted epistemology of the field. (Held cites the earlier review directly — "See, for example, Schneider and Dickinson (1974), and, especially, Hoskins (1983)" — a link OpenAlex misses because it indexes only seven of the essay's references; `04-acceptance-checks.md`.)

### CO₂ in three dimensions (1975–1988)

**Manabe & Wetherald (1975)**, *The effects of doubling the CO₂ concentration on the climate of a general circulation model* (J. Atmos. Sci.): idealized geography, a "swamp" ocean with no heat capacity, annual-mean insolation, fixed clouds. Result: 2.93 °C, polar amplification (from the albedo and lapse-rate feedbacks the column could not capture), a ~7 per cent intensification of the hydrological cycle, and stratospheric cooling. **Manabe & Stouffer (1980)** added realistic geography and a seasonal cycle with a mixed-layer ocean and got ~2 °C. **Hansen et al. (1983)** described the GISS Model II; **Hansen et al. (1984)** obtained 4.2 °C and introduced the formal feedback decomposition. **Washington & Meehl (1984)** (NCAR) and **Wilson & Mitchell (1987)** (UK Met Office) added further GCMs. **Schlesinger & Mitchell (1987)**, *Climate model simulations of the equilibrium climatic response to increased carbon dioxide* (Rev. Geophys.), compared them: the recent seasonal-cycle simulations gave 3.5–4.2 °C, roughly twice the earliest seasonal simulation (Manabe & Stouffer 1980), "apparently as a result of a positive cloud feedback" — the first explicit identification of clouds as the discriminator. **Wetherald & Manabe (1988)** isolated the cloud feedback in the GFDL model. *Competing answers were about magnitude (2–5 °C), not sign; the models differed in cloud schemes, ocean treatment, and resolution.*

### Coupled transients and flux adjustment (1988–2000)

**Stouffer, Manabe & Bryan (1989)**, *Interhemispheric asymmetry in climate response to a gradual increase of atmospheric CO₂* (Nature), and **Washington & Meehl (1989)** ran the first transient coupled experiments: the Southern Ocean warms slowly, and the transient response is well below the equilibrium response. To keep coupled models from drifting, **Sausen, Barthel & Hasselmann (1988)** introduced *flux adjustment* — adding fixed corrections to the surface heat and freshwater fluxes. Most 1990s coupled models used it; critics (inside and outside the field) called it a fudge, and the SAR discussed it at length. **Gordon et al. (2000)** showed that HadCM3 ran stably without it; by CMIP3 (2005–07) most models had dropped it. *Competing answers: flux adjustment as a legitimate expedient vs. a symptom of missing physics — resolved by making it unnecessary.*

### The ensemble as the object of assessment (1989–2013)

**Cess et al. (1989, 1990)** organized the first coordinated intercomparison (fourteen atmospheric GCMs under a prescribed SST perturbation) and found that cloud feedback explained most of the threefold spread in sensitivity. **Gates (1992)** launched AMIP; **Meehl et al. (2000, 2007)** CMIP and CMIP3; Taylor et al. (2012) CMIP5; Eyring et al. (2016) CMIP6. The assessment convention became "the multi-model ensemble is the projection, its spread is the uncertainty" — *model democracy* (Knutti 2010 asked whether it should end). This convention broke in AR6 (below).

### Earth-system models (2000–present)

**Cox et al. (2000)** coupled a carbon cycle to a GCM (P02); C4MIP (Friedlingstein et al. 2006) made carbon-cycle feedbacks a standard model component; CMIP5 and CMIP6 added interactive aerosols, chemistry, ice sheets, and vegetation. The "Earth-system model" is the current top of the hierarchy, and it is where the CMIP6 "hot model" problem arose (P04).

### Evaluation, tuning, and skill (1994–present)

**Oreskes, Shrader-Frechette & Belitz (1994)**, *Verification, validation, and confirmation of numerical models in the Earth sciences* (Science), argued that open-system models cannot be verified, only confirmed by matching observations — a position the field accepted and the skeptical literature cites. **Mauritsen et al. (2012)**, *Tuning the climate of a global model* (JAMES), and **Hourdin et al. (2017)**, *The art and science of climate model tuning* (BAMS), described tuning practice openly: models are tuned mainly to the top-of-atmosphere radiation balance and to climatological fields, and — the important point — some groups do and some do not tune to the twentieth-century temperature record. **Kiehl (2007)** (P06) had shown that the models that fit the century did so with anti-correlated sensitivities and aerosol forcings. **Hausfather et al. (2020)**, *Evaluating the performance of past climate model projections* (GRL), compared seventeen projections published 1970–2007 with subsequent observations and found fourteen consistent once the difference between projected and realized forcing was removed — the strongest retrospective evidence that the models' *transient* behaviour has been about right for fifty years.

### Weighting and resolution (2018–present)

The AR6 (2021) broke with model democracy: its projections were constrained by observed warming (Tokarska et al. 2020; Ribes et al. 2021) and its sensitivity range was assessed independently of the CMIP6 spread. **Hausfather et al. (2022)** argued this should be standard practice. On resolution, the argument since **Stevens et al. (2019)** (the DYAMOND intercomparison of km-scale global models) and Palmer & Stevens (2019) is that convection must be resolved rather than parameterized to make progress on clouds; whether km-scale models change the sensitivity answer is unknown.

## What was accepted, when, and on what evidence

- **GCMs as the primary instrument for the CO₂ problem:** by 1979. Marker (A): the Charney report rested its number on the Manabe and Hansen GCMs and used the 1-D models to explain them. Marker (C): Washington & Parkinson's textbook (1986).
- **The hierarchy as the interpretive framework:** Schneider & Dickinson (1974) → Held (2005); marker (B): the feedback-decomposition practice (Hansen et al. 1984; Soden & Held 2006; radiative kernels, Soden et al. 2008) reads 3-D output through a 1-D energy balance — though by 2006 the practice is cited to Wetherald & Manabe 1988, Colman 2003 and Webb et al. 2006 rather than to Hansen 1984, i.e. it had reached criterion (C); marker (E): the two-layer energy-balance emulators (Held et al. 2010; Geoffroy et al. 2013) used in AR6 are 0-D models calibrated to GCMs.
- **Flux adjustment abandoned:** ~2000–2007 (marker D).
- **Model democracy abandoned in favour of observational constraint:** 2020–21 (marker A: AR6).
- **The models' transient skill:** Hausfather et al. (2020) is the marker most often cited; there is no serious mainstream dissent from it, though there is dissent about the tropical troposphere (P08).

## Inheritance

- *From:* P01 (Möller's failure → RCE); numerical weather prediction (Charney, von Neumann, Phillips).
- *To:* P04 (every sensitivity estimate before 2013 was a model result or a model-informed one); P05 (feedback decomposition); P07 (fingerprints are model-generated patterns); P11 (regional projections); P13 (large ensembles).

## What remains open

Cloud and convection parameterization (the reason the sensitivity spread persists — P05); how to weight or constrain an ensemble; whether km-scale resolution changes the answer; the representation of Antarctic ice-sheet and AMOC stability (P12); the magnitude of simulated internal variability on multidecadal scales (P13).

## Flashpoint notes

Three model-related claims recur in the skeptical literature: (1) "models are tuned to the twentieth century" — partly true and openly discussed (Hourdin 2017; Kiehl 2007), but it does not explain the sensitivity, which is set by cloud physics, not by tuning to the record, and the AR6 constraint on projections is the field's own response to the concern; (2) "models cannot be validated" — the field's own position (Oreskes 1994), which is why the retrospective tests (Hausfather 2020) and the paleoclimate tests (P09) matter; (3) "models run hot" — true of a subset of CMIP6 models (Zelinka 2020; Hausfather 2022) and of the tropical upper troposphere (Santer 2017; McKitrick & Christy 2018, 2020), not of the global-mean transient response. The interesting structural fact for the later strand is that the field's most visible self-correction in this period (AR6's rejection of model democracy) was triggered by models that were *too* sensitive, not too insensitive.
