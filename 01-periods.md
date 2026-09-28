# Problems by period, and how later problems grew out of earlier ones

This file answers the first question of the brief: what the important problems were in each period, why their solutions mattered, and how each period's problems were inherited from the last. The per-problem detail (papers, competing answers, acceptance) is in `02-problems/`; this file refers to those files as P01…P13.

The periodization below is a working device, not a claim that the field experienced clean breaks. The boundaries are placed at events that changed what the next set of papers took for granted: Callendar's paper (1938), the Keeling curve (1960), the Manabe–Wetherald 1-D model (1967), the Charney report (1979), the IPCC's formation and first report (1988–90), the Third Assessment (2001), the Fifth Assessment (2013), and the Sherwood assessment / AR6 (2020–21).

---

## Summary table

| Period | Dominant question | Form of the accepted answer by period's end | Explicit marker |
|---|---|---|---|
| I. 1824–1938 | Could CO₂ change global temperature at all? | "Physically possible, but probably blocked by saturation and the ocean; Callendar's warming is unproven." | Royal Meteorological Society discussion of Callendar (1938) — polite disbelief |
| II. 1955–1965 | Are the objections right? Is CO₂ actually rising? | "The saturation argument is wrong; the ocean will not absorb most of it; CO₂ is measurably rising." | PSAC report appendix (1965) |
| III. 1965–1979 | How much warming per doubling, and by what method? | "About 3 °C ± 1.5 °C, from a hierarchy of models whose members agree on the sign and roughly on the size." | Charney report (1979) |
| IV. 1979–1990 | When will the warming be detectable, and what else is forcing climate? | "Should emerge from noise by ~2000; other trace gases roughly double the CO₂ problem; the ocean delays the response." | Hansen (1981, 1988); Villach (1985); IPCC formed (1988); FAR (1990) |
| V. 1990–2001 | Has it emerged, and is it anthropogenic? | "A discernible human influence; most warming since 1950 likely anthropogenic." | SAR (1995); TAR (2001) |
| VI. 2001–2013 | Why does the sensitivity range not narrow, and how does the carbon cycle change the problem? | "Clouds are the barrier; warming is proportional to cumulative emissions; the water-vapour feedback is confirmed." | AR4 (2007); AR5 (2013) |
| VII. 2013–2026 | How much, how fast, and what could break? | "ECS likely 2.5–4 °C; the human contribution is unequivocal; hot models and recent acceleration are unresolved." | Sherwood et al. (2020); AR6 (2021) |

---

## Period I — Prehistory (1824–1938): is it physically possible?

**The problems.**

1. *Does the atmosphere warm the surface, and which gases do it?* Fourier (1824, 1827) framed planetary temperature as an energy balance and inferred that the atmosphere retains heat. Tyndall (1859, 1861) measured infrared absorption by water vapour, CO₂ and other gases in the laboratory (Foote, 1856, had earlier shown CO₂-filled cylinders warmed more in sunlight, without the infrared mechanism). This was settled by 1861 and never reopened; every later problem takes it as given.
2. *Could changes in CO₂ explain the ice ages?* This — not human emissions — was Arrhenius's question. Arrhenius (1896) computed, from Langley's lunar infrared measurements, that halving CO₂ would cool the Earth by ~4–5 °C and doubling would warm it by ~5–6 °C, with water vapour amplifying the effect and the Arctic warming more. Chamberlin (1899) supplied a geological carbon-cycle mechanism. Arrhenius (1906) revised his estimate downward (to about 1.6 °C without, and about 2.1 °C with, water-vapour feedback in the journal paper; his popular book of 1906/1908 still said "about 4°").
3. *Would human emissions matter?* Arrhenius thought coal burning would take millennia to double CO₂. Callendar (1938), an English steam engineer, compiled ~150 weather stations and argued the warming of 1890–1935 (~0.3 °C) was already being caused by fossil CO₂, estimating ~2 °C per doubling.

**The objections that closed the question.** Three arguments, each reasonable on the evidence of the time, kept the hypothesis marginal for forty years:

- *Saturation.* Ångström (1900), using his assistant Koch's measurements, argued the CO₂ band was already saturated and overlapped by water vapour, so added CO₂ could not absorb more. (Hulburt (1931) re-did the calculation and got ~4 °C, but the paper was ignored.)
- *Water-vapour dominance.* If water vapour absorbs most of the infrared, CO₂ is a minor player.
- *Ocean uptake.* The ocean holds fifty times more carbon than the atmosphere; surely it would absorb whatever we emitted.

To these the meteorologists added a fourth, aimed at Callendar: the warming he reported could be natural variability, and his station coverage was poor. The Royal Meteorological Society discussion of his paper is the first recorded instance of a pattern that recurs throughout this history — a claimed detection meeting the objection that the noise has not been characterised.

**Why the solution mattered then.** Ice ages and the origin of climate fluctuations were the live scientific problems; policy was not. But the objections are the important inheritance: they became, almost item by item, the research agenda of Period II.

---

## Period II — Revival (1955–1965): are the objections right?

**The problems.** Each of the pre-war objections was taken up, and each was answered within a decade — partly because of Cold War funding for atmospheric physics, radiocarbon, and digital computing, and partly because of the International Geophysical Year (1957–58).

1. *Saturation and overlap* (→ P01). Plass (1956), using new spectroscopic data and layer-by-layer radiative calculations on early computers, showed that the saturation argument failed: what matters is emission from the upper troposphere, where the band is not saturated and where water vapour is scarce, and the band wings continue to absorb. He estimated 3.6 °C per doubling with no feedbacks. Kaplan (1960) objected that clouds reduced the effect; Möller (1963) found that a surface energy-balance approach with fixed relative humidity gave almost arbitrary results (from small to ~10 °C), which showed not that the effect was negligible but that the method was wrong. That methodological failure is the direct origin of Period III's first problem.
2. *Ocean uptake* (→ P02). Revelle & Suess (1957) showed from radiocarbon and carbonate chemistry that although the surface ocean exchanges CO₂ with the air within a decade, its buffer chemistry lets it absorb only a fraction of the added carbon; Bolin & Eriksson (1959) drew out the implication more sharply than Revelle himself had. Human emissions were, in Revelle's phrase, a "large-scale geophysical experiment."
3. *Is CO₂ actually rising?* (→ P02, P08). Keeling (1960), with continuous infrared gas analysers at Mauna Loa and the South Pole, produced within two years a clean seasonal cycle and a rising baseline. This ended the debate about whether the airborne fraction was non-zero; earlier measurements had been too scattered to tell.
4. *Could the climate be computed at all?* (→ P03). Phillips (1956) ran the first general-circulation experiment; Smagorinsky (1963) and Manabe et al. (1965) built the GFDL model with a hydrological cycle. These were not yet about CO₂.
5. *Ice ages* (→ P09). Emiliani (1955) produced the first deep-sea oxygen-isotope record, suggesting many glacial cycles rather than four; Ewing & Donn (1956) proposed an oceanic ice-age mechanism. The Milankovitch hypothesis was alive but untested.

**Why the solutions mattered.** Together they converted the CO₂ hypothesis from a curiosity into a live problem with a measurable driving variable. What they did not supply was a credible magnitude. The Presidential Science Advisory Committee's 1965 report (appendix by Revelle, Broecker, Craig, Keeling and Smagorinsky) is the first governmental statement that the problem was real, and it is notable for what it did not contain: any confident estimate of the warming.

**Inheritance.** Period II answered Period I's objections and left one methodological problem (Möller's) and one open question (how much warming), which define Period III.

---

## Period III — The modelling foundation (1965–1979): how much, and by what method?

**The problems.**

1. *A correct method for the one-dimensional problem* (→ P01, P03). Manabe & Wetherald (1967) replaced the surface energy balance with a radiative–convective equilibrium of the whole column: radiation warms and cools each layer, and where the lapse rate becomes unstable, convection adjusts it. With relative humidity held fixed (so water vapour rises with temperature) they obtained 2.36 °C per doubling; with absolute humidity fixed, 1.33 °C. This is the first credible estimate, and the fixed-relative-humidity assumption is the first quantitative statement of the water-vapour feedback. The paper also predicted stratospheric cooling, which became a fingerprint of CO₂-driven change thirty years later (Period V).
2. *Climate stability and the ice–albedo feedback* (→ P03, P05, P12). Budyko (1969) and Sellers (1969), independently, built latitudinally resolved energy-balance models and found that a small reduction in solar constant could trigger a runaway to a fully glaciated Earth. This introduced the ideas of multiple equilibria, instability, and the feedback formalism that the field still uses to decompose model results.
3. *Three-dimensional simulation* (→ P03). Manabe & Wetherald (1975) doubled CO₂ in a GCM with idealized geography and a swamp ocean: 2.93 °C, with polar amplification, an intensified hydrological cycle, and stratospheric cooling. Manabe & Bryan (1969) had already coupled an atmosphere to an ocean; the coupled transient problem is Period IV's.
4. *What paces the ice ages?* (→ P09). Hays, Imbrie & Shackleton (1976) found spectral peaks in deep-sea cores at the orbital periods. The Milankovitch hypothesis was accepted within a few years — one of the fastest acceptances in this history — and it recast climate as a system that amplifies small forcings.
5. *What is climate noise?* (→ P13). Lorenz (1963, 1968, 1975) established that weather is chaotic and distinguished predictability of the first kind (initial conditions) from the second (boundary conditions). Hasselmann (1976) showed that the ocean, integrating random weather forcing, produces red-noise climate variability without any external cause. These two results define the statistical problem — separating signal from noise — that every later detection debate is about.
6. *Will aerosols cool more than CO₂ warms?* (→ P06). Northern Hemisphere temperatures had fallen from the 1940s to the 1970s. Rasool & Schneider (1971) computed that aerosols could cool and that CO₂ warming was small (their CO₂ calculation was later found to be in error by a factor of several; Schneider 1975). Bryson's "human volcano" argued for cooling. The literature as a whole nonetheless favoured warming — Peterson, Connolley & Fleck (2008) count 44 warming, 7 cooling and 20 neutral papers over 1965–79 — and Broecker (1975) predicted the cooling would soon reverse.
7. *Other gases, and the carbon budget* (→ P06, P02). Ramanathan (1975) showed chlorofluorocarbons were potent greenhouse gases; Wang et al. (1976) extended this to methane, nitrous oxide and ozone. Woodwell et al. (1978) claimed deforestation released as much carbon as fossil fuels, which was arithmetically incompatible with the ocean's known uptake — the "missing sink" problem that took twenty years to resolve.

**Why the solutions mattered.** By 1979 the field had a number (about 3 °C), a hierarchy of models that agreed on sign and roughly on magnitude, and a physical explanation for why simple models and complex models gave similar answers. The Charney report (1979) reviewed the Manabe and Hansen GCMs and stated ECS as "near 3 °C with a probable error of ± 1.5 °C" — the first explicit expert consensus on magnitude, and one whose range would survive unchanged through five IPCC assessments.

**Inheritance.** Period III took Möller's methodological failure and the Keeling curve from Period II and produced the number. It handed to Period IV three problems that its own results created: the ocean's delay (Charney's report explicitly noted that the ocean would postpone the warming), the question of when the warming would be detectable (which required Hasselmann's noise), and the role of the non-CO₂ gases.

---

## Period IV — Consolidation and the detection problem (1979–1990): when will we see it?

**The problems.**

1. *When does the signal emerge from the noise?* (→ P07, P13). Madden & Ramanathan (1980) posed detection as a statistical problem. Hansen et al. (1981) projected that the CO₂ signal would rise out of the noise by about 2000 and, in the same paper, presented the first global temperature record to show that the Northern Hemisphere cooling had been a hemispheric, not global, phenomenon. The observational infrastructure — Jones et al. (1986), Hansen & Lebedeff (1987) — was built to answer this question.
2. *How does the ocean delay the response?* (→ P10). Hoffert et al. (1980), Hansen et al. (1985), and Wigley & Schlesinger (1985) developed upwelling–diffusion models of ocean heat uptake; Hansen et al. (1985) showed that the delay depends on the sensitivity itself, so that a high-sensitivity climate hides more "unrealized" warming. Stouffer, Manabe & Bryan (1989) ran the first coupled transient experiment and found the interhemispheric asymmetry (Southern Ocean lags) that later became central.
3. *What are the feedbacks in a GCM?* (→ P04, P05). Hansen et al. (1984) formalized feedback analysis for a 3-D model (4 °C per doubling, decomposed into water vapour, lapse rate, cloud and albedo contributions). Schlesinger & Mitchell (1987) compared GCMs and found cloud feedback to be the main discriminator — the first statement of what remains the central open problem.
4. *How big is the non-CO₂ problem?* (→ P06). Ramanathan et al. (1985) showed that the trace gases together could contribute as much as CO₂; the "CO₂ problem" became the "greenhouse-gas problem." The Vostok ice core (Barnola et al. 1987) showed CO₂ and temperature moving together through a glacial cycle, which both supported the sensitivity estimate (Lorius et al. 1990) and raised the question of cause and effect that skeptics later seized on.
5. *Could the climate change abruptly?* (→ P12). Broecker (1987) argued from the Younger Dryas and the Greenland cores that the thermohaline circulation could switch states; Manabe & Stouffer (1988) found two stable equilibria in a coupled model.
6. *Should anything be done yet?* The National Academy's *Changing Climate* (1983) accepted the science and counselled caution on policy; the Villach conference (1985) called for action; Hansen's Senate testimony (1988) asserted "99 percent confidence" that the warming was real and probably anthropogenic, which many colleagues thought premature. The IPCC was formed in 1988 and issued its First Assessment in 1990.

**Why the solutions mattered.** Period IV turned a projection into a detection programme and built the observational and statistical apparatus for it. The disagreement between Hansen and his peers in 1988 was not about the physics but about whether the detection standard had been met — the same disagreement as in the 1938 discussion of Callendar.

**Inheritance.** Period IV took the number and the noise model from Period III and asked when the signal would appear. It handed Period V two things: a detection method that needed a *spatial* fingerprint rather than a global mean (because the global mean could always be attributed to something else), and an unexplained mismatch — models forced with greenhouse gases alone warmed the twentieth century more than observed.

---

## Period V — Attribution and the assessment era (1990–2001): has it emerged, and is it us?

**The problems.**

1. *Why do the models warm too much?* (→ P06). Charlson et al. (1992) quantified the direct cooling by sulphate aerosols; Mitchell et al. (1995) added it to a coupled model and reproduced the twentieth-century record. This closed the mismatch — and opened a permanent problem, because a strong aerosol cooling paired with a high sensitivity fits the record as well as weak cooling with low sensitivity (Kiehl 2007 later showed the anti-correlation across models).
2. *Fingerprinting* (→ P07). Hasselmann (1993), Hegerl et al. (1996) and Santer et al. (1996) developed optimal fingerprint methods and applied them to the three-dimensional pattern of temperature change, including the stratospheric cooling that Manabe & Wetherald had predicted in 1967. Tett et al. (1999) and Stott et al. (2000) showed that the twentieth century could be reproduced only with anthropogenic forcing included. The SAR (1995) wrote "the balance of evidence suggests a discernible human influence on global climate"; the TAR (2001) wrote that "most of the observed warming over the last 50 years is likely to have been due to the increase in greenhouse gas concentrations."
3. *Natural experiments.* Pinatubo (1991) provided a test: Hansen et al. (1992) predicted the cooling in advance and the GISS model matched it; Soden et al. (2002) later used it to confirm the water-vapour feedback.
4. *Is the present warmth unusual?* (→ P09). Mann, Bradley & Hughes (1998, 1999) reconstructed Northern Hemisphere temperature over 600, then 1000, years, and the TAR made the "hockey stick" its emblem. This was the most publicly contested result of the decade, for reasons that have as much to do with its prominence as its methods.
5. *Do the satellites disagree?* (→ P08). Spencer & Christy (1990) reported no tropospheric warming from the MSU instruments, in apparent conflict with the surface record. The NRC (2000) concluded the discrepancy was real but did not invalidate the surface record; the resolution (orbital-drift corrections) came in 2005.
6. *Solar alternatives* (→ P07). Friis-Christensen & Lassen (1991) correlated solar-cycle length with temperature; Svensmark & Friis-Christensen (1997) proposed a cosmic-ray–cloud mechanism. Both were taken seriously enough to be tested and were found wanting (Laut 2003; Lockwood & Fröhlich 2007; the CERN CLOUD experiment 2011–2016).
7. *Abrupt change* (→ P12). The GRIP and GISP2 cores (Dansgaard et al. 1993) established Dansgaard–Oeschger events; Rahmstorf (1995) and Manabe & Stouffer (1993, 1995) explored thermohaline bistability; Broecker (1997) called the circulation "the Achilles heel of our climate system."
8. *Model infrastructure* (→ P03). The Atmospheric and Coupled Model Intercomparison Projects (AMIP from 1990; CMIP from 1995) turned the model ensemble into the standard object of assessment; HadCM3 (Gordon et al. 2000) was the first major coupled model to run stably without flux adjustment, removing a standing objection.

**Why the solutions mattered.** The question changed from "will it warm?" to "has it warmed because of us?", and the IPCC's calibrated language became the field's instrument for saying how sure it was. This is also the period in which the IPCC's process — and the Santer chapter-8 affair of 1996 — became the object of the manufactured-consensus claim.

**Inheritance.** Period V inherited the detection problem and the model–observation mismatch and solved both — one by fingerprints, the other by aerosols. It handed Period VI the aerosol–sensitivity degeneracy, the still-unnarrowed sensitivity range, and the hockey-stick and satellite controversies.

---

## Period VI — The sensitivity impasse and the Earth system (2001–2013)

**The problems.**

1. *Why will the range not narrow?* (→ P04, P05). Cess et al. (1989, 1990) had already shown that cloud feedback explained most inter-model spread; Bony & Dufresne (2005) localized it to marine boundary-layer clouds; Soden & Held (2006) decomposed the AR4 ensemble. Roe & Baker (2007) argued that the fat upper tail of ECS is a structural consequence of the feedback arithmetic and cannot be removed by modest improvements in the feedbacks; Knutti & Hegerl (2008) reviewed all the constraints and concluded that the range 2–4.5 °C was robust and the tail hard to cut. The AR4 (2007) gave "likely 2–4.5 °C, best estimate 3 °C"; the AR5 (2013) widened it back to 1.5–4.5 °C and, for the first time, declined to give a best estimate, because energy-budget estimates from the observed record had come in low (Otto et al. 2013).
2. *Is the water-vapour feedback real?* (→ P05). Lindzen (1990) had argued for upper-tropospheric drying; Soden et al. (2005) and Dessler & Sherwood (2009) settled it observationally. Lindzen's "adaptive iris" (Lindzen, Chou & Hou 2001) was tested and rejected (Hartmann & Michelsen 2002); Lindzen & Choi (2009, 2011) were rebutted by several groups. The low-sensitivity programme moved from feedbacks to energy budgets (Period VII).
3. *Is the Earth out of energy balance?* (→ P08, P10). Levitus et al. (2000, 2005) and Argo floats (from 2000) measured ocean heat content; Hansen et al. (2005) called the imbalance the "smoking gun." Ocean heat content became the primary metric of global warming, replacing surface temperature for many purposes.
4. *The satellite and hiatus controversies* (→ P08). Mears & Wentz (2005) found the orbital-drift error in the UAH record and the CCSP (2006) declared the discrepancy resolved. Then surface warming slowed after 1998; Easterling & Wehner (2009), Meehl et al. (2011), Kosaka & Xie (2013), and others explained it as Pacific variability plus small forcings; Fyfe et al. (2013) said the models had overestimated the trend. This was unresolved at AR5.
5. *What does the carbon cycle do?* (→ P02, P10). C4MIP (Friedlingstein et al. 2006) showed carbon-cycle feedbacks amplify warming; Matthews & Caldeira (2008) and Solomon et al. (2009) showed that warming would not reverse for a millennium after emissions stopped; Allen et al. (2009), Matthews et al. (2009) and Meinshausen et al. (2009) showed that peak warming is nearly proportional to cumulative CO₂ emissions regardless of path. This "transient climate response to cumulative emissions" reframed the policy problem as a budget and was adopted by AR5 as its headline figure.
6. *Sea level and ice sheets* (→ P12). AR4 (2007) excluded rapid ice-sheet dynamics from its sea-level projections because they could not be modelled; Rahmstorf (2007) and Pfeffer et al. (2008) offered semi-empirical and kinematic bounds; Arctic sea ice fell faster than any model (Stroeve et al. 2007).
7. *Extremes and tipping points* (→ P11, P12). Stott, Stone & Allen (2004) attributed the 2003 European heatwave probabilistically; Lenton et al. (2008) catalogued tipping elements.

**Why the solutions mattered.** The sensitivity range's failure to narrow over thirty years became, for skeptics, evidence that the science was not progressing, and for the field, the motivation for the multiple-lines-of-evidence approach that finally narrowed it in 2020. The cumulative-emissions result changed what "the answer" is for policy: not a temperature per doubling but a budget in tonnes.

**Inheritance.** Period VI took the aerosol–sensitivity degeneracy and the unnarrowed range from Period V and diagnosed why (clouds, structural tails, energy-budget degeneracy). It handed Period VII the diagnosis, the hiatus, the hot-end tail, and the ice-sheet problem.

---

## Period VII — Narrowing, hot models, and acceleration (2013–2026): how much, how fast, and what could break?

**The problems.**

1. *Reconciling the energy-budget estimates* (→ P04, P10). Armour, Bitz & Roe (2013), Andrews et al. (2015), Gregory & Andrews (2016) and Zhou, Zelinka & Klein (2016) showed that the feedback measured over the historical period is not the equilibrium feedback because the *pattern* of ocean warming (eastern Pacific and Southern Ocean lagging) temporarily strengthens the negative cloud feedback. This "pattern effect" explains why observational estimates were low, and it is now accepted; its magnitude is not.
2. *Narrowing the range* (→ P04). Sherwood et al. (2020) combined process understanding, the historical record and paleoclimate in a single Bayesian framework and obtained 2.6–3.9 °C (likely) — the first narrowing since 1979. AR6 (2021) adopted 2.5–4.0 °C likely, 3 °C best estimate, and, for the first time, did not use the CMIP ensemble range as the sensitivity range.
3. *The hot models* (→ P03, P04, P05). CMIP6 produced a subset of models with ECS above 5 °C (Zelinka et al. 2020), traced mostly to cloud microphysics and aerosol–cloud interactions. Hausfather et al. (2022) argued that projections should be weighted by consistency with observed warming, and AR6 did so. The result is a break between "the models" and "the assessment" that did not exist before.
4. *Was the hiatus real?* (→ P08). Cowtan & Way (2014), Karl et al. (2015), Hausfather et al. (2017) and Medhaug et al. (2017) resolved it as a combination of coverage bias, a sea-surface-temperature bias and Pacific variability; the 2015–16 El Niño ended the observational question.
5. *Attribution completed* (→ P07). AR6 stated that human influence on warming is "unequivocal" — a change in kind from the probabilistic language of 1995–2013 — and that observed warming is entirely explained by human forcing (best-estimate human contribution ≈ observed warming).
6. *AMOC and ice sheets* (→ P12). Rahmstorf et al. (2015) and Caesar et al. (2018) inferred a twentieth-century AMOC slowdown; Ditlevsen & Ditlevsen (2023) and van Westen et al. (2024) argued for a tipping course within this century; Baker et al. (2025) found no full collapse in 34 models under extreme forcing; 2026 work suggests the outcome depends on the rate of warming. DeConto & Pollard (2016) proposed marine ice-cliff instability and metre-scale Antarctic contributions by 2100; Edwards et al. (2019) found it unnecessary to explain the past. AR6 handled both with "low-likelihood, high-impact" storylines — a new genre of assessment statement.
7. *Is warming accelerating?* (→ P06, P08, P13). The 2023–24 temperature surge exceeded what models and ENSO predicted (Schmidt 2024). Explanations proposed: reduced planetary albedo from fewer low clouds (Goessling et al. 2024); the 2020 cut in ship sulphur emissions (several 2024 papers, giving ~0.03–0.05 °C); solar maximum; Hunga Tonga; Pacific and Atlantic variability. Hansen et al. (2023, 2025) argued that aerosol forcing had been underestimated and that sensitivity is ~4.8 °C; Forster et al. (2025, 2026) found the human-induced warming rate at 0.27 °C/decade over 2016–2025, up from ~0.18 °C/decade; Foster & Rahmstorf (2026) found statistically significant acceleration after removing ENSO, volcanic and solar effects, though not in the raw series (Beaulieu et al. 2024). Farago et al. (2026) reconstruct 2023–24 "fairly well" from known factors. This is the live problem as of mid-2026.

**Why the solutions matter.** The narrowing of ECS after forty-one years is the strongest evidence in this history that the field's method converges; the hot-model problem and the acceleration debate are the strongest evidence that the models remain incomplete in exactly the place (clouds and aerosols) identified in 1987.

---

## Lineages: how later problems grew out of earlier ones

The periods above can be re-read as eight lineages, each a chain in which one problem's accepted answer becomes the premise of the next.

### 1. The radiative question → sensitivity → feedbacks → clouds
Does CO₂ absorb (Tyndall)? Enough to matter (Arrhenius; Ångström's objection; Plass)? How much warming, computed correctly (Manabe & Wetherald 1967)? What amplifies it (Hansen et al. 1984's decomposition)? Which amplifier is uncertain (Cess 1989; Schlesinger & Mitchell 1987: clouds)? Which clouds (Bony & Dufresne 2005: marine boundary-layer)? What controls them (Sherwood et al. 2014; Zelinka et al. 2020; Myers et al. 2021)? Each step takes the previous answer as fixed. The question has narrowed from "the atmosphere" to "the top few hundred metres of the marine boundary layer in the subtropics," which is where the field is now.

### 2. The model hierarchy: one dimension to three, and back
The brief's example — whether the field moved from one-dimensional to three-dimensional characterizations that assume a particular one-dimensional model as a starting point — is broadly right, with two refinements.

*Forward inheritance.* There were two one-dimensional models, not one. The *vertical* model (radiative–convective equilibrium, Manabe & Wetherald 1967) supplied the GCMs with their radiative transfer code, their moist convective adjustment, and the expectation that relative humidity is roughly conserved; the *horizontal* model (energy balance in latitude, Budyko 1969; Sellers 1969) supplied the ice–albedo feedback and the concept of stability. Manabe & Wetherald (1975) is explicitly the 1967 column model extended to three dimensions, and its introduction says so; the GCM was expected to reproduce the 1-D result and did (2.93 vs 2.36 °C, the difference attributed to the albedo feedback the column could not represent).

*Backward inheritance.* The more important relationship runs the other way. Three-dimensional models are *interpreted* through a zero-dimensional energy balance: N = F − λΔT (imbalance equals forcing minus feedback times warming). Hansen et al. (1984), Schlesinger (1985) and Wetherald & Manabe (1988) developed the practice of decomposing GCM output into feedback parameters that are, formally, coefficients in a 1-D model; Gregory et al. (2004) turned it into the standard regression method for extracting ECS from a GCM run; and the pattern-effect literature of 2013–2020 is about the failure of that zero-dimensional description (λ is not constant). Held (2005) named the resulting situation "the gap between simulation and understanding": the field simulates in three dimensions and understands in one. The hierarchy is not a ladder that was climbed and abandoned; the lower rungs are the instruments by which the upper ones are read.

*Validation rather than mere inheritance.* The 1-D model's key assumption (fixed relative humidity) was later checked independently — in GCMs, then against satellite observations (Soden et al. 2005) and Pinatubo (Soden et al. 2002) — so the dependency of 3-D on 1-D is not an unexamined premise.

### 3. The carbon question → airborne fraction → feedbacks → budgets
Does the ocean take it up (Revelle & Suess)? What fraction stays airborne (Keeling; Oeschger et al. 1975)? Where does the rest go (Woodwell vs Broecker; Tans et al. 1990)? Does the sink weaken as the planet warms (C4MIP 2006)? What follows for policy (Matthews et al. 2009: proportionality to cumulative emissions → carbon budgets; MacDougall et al. 2020: zero-emissions commitment ≈ 0)? The last step inverted an earlier belief ("warming in the pipeline" under constant concentrations) into its policy-relevant opposite (warming stops roughly when emissions stop).

### 4. Detection → attribution → extremes
Is there a trend (Callendar; Jones 1986)? Is it outside the noise (Madden & Ramanathan 1980; Hasselmann 1976)? Does its pattern match the cause (Santer 1996)? Can the same logic be applied to a single event (Stott et al. 2004)? The statistical problem is the same at each step; what changes is the object (global mean → spatial pattern → single event).

### 5. The ocean: delay → transient response → commitment → pattern effect
Charney's report noted the ocean would delay warming; Hansen et al. (1985) made the delay depend on sensitivity; Stouffer et al. (1989) found the Southern Ocean lags; the TCR was defined to describe the delayed response; the pattern effect (2013–) is the discovery that the delay also changes the apparent feedback. The ocean is thus the source of both remaining large uncertainties — aerosols aside — in relating the historical record to the future.

### 6. Ice ages → paleo-sensitivity → abrupt change
Milankovitch pacing (Hays 1976) showed the climate amplifies small forcings; Vostok (1987) supplied the amplifier's identity (CO₂ and ice); Lorius et al. (1990) used it to estimate sensitivity; the Greenland cores (1993) showed the amplifier can switch abruptly; the tipping-point literature (Lenton 2008; Armstrong McKay 2022) is the attempt to enumerate the switches.

### 7. Noise: the same statistical problem, five times
Callendar's critics (1938), Hansen's critics (1988), the hiatus (2009–2015), the acceleration debate (2024–2026), and the AMOC early-warning debate (2023–2026) are all instances of one question: how large is internal variability relative to the forced signal, and how many years of data are needed to tell? Hasselmann (1976) answered it in principle; large initial-condition ensembles (Deser et al. 2012; Kay et al. 2015) answered it in practice for models; whether the models' variability is right remains a premise rather than a finding.

### 8. Aerosols: from cooling scare to termination shock
Rasool & Schneider (1971) asked whether aerosols would win; Charlson (1992) quantified them; Mitchell (1995) used them to fit the record; Kiehl (2007) showed they were being used, in effect, as a free parameter; AR6 still gives aerosol forcing the widest error bar of any forcing; and the 2020 ship-fuel regulation turned the problem inside out — the removal of a cooling forcing is now a candidate explanation for recent acceleration. The aerosol problem has never been solved; it has been repeatedly re-posed.

---

## Observations across the whole sequence

- **Acceptance was fastest where a single new measurement answered a yes/no question** (Keeling's curve; Hays et al.'s spectral peaks; Mears & Wentz's diurnal correction) and slowest where the answer is a continuous quantity limited by a sub-grid process (sensitivity; aerosol forcing; regional precipitation).
- **The Charney range (1.5–4.5 °C) persisted for 41 years** not because nothing was learned but because what was learned (clouds are the barrier; the tail is structural) explained why it could not be narrowed with the tools then available. Narrowing came from combining independent lines of evidence, not from better models.
- **Each period's central problem was created by the previous period's solution**: Möller's failure produced Manabe's method; Manabe's number produced the detection problem; detection produced the aerosol mismatch; the aerosol fix produced the sensitivity degeneracy; the degeneracy produced the multiple-lines-of-evidence programme; that programme's success exposed the hot models.
- **The disagreements that became public flashpoints** (Callendar 1938, Hansen 1988, the satellite record, the hockey stick, the hiatus, the acceleration) were almost all about detection statistics and data handling, not about radiative physics — which has been uncontested within the field since 1956.
