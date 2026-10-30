# Riemann research swarm — 30 October 2026

Status: **RESEARCH EXPLORATION / PROVED SCOPED LEMMAS / OPEN ANALYTIC GATES**.  
Scope: three parallel mechanism attacks, independent cross-review, and a fourth heat-trace calculation. No new individual zero-free region, critical-line verification, or proof of RH is claimed.  
Exact baseline: [`main` at f99d9e3](https://github.com/GettysburgResearch/riemann/tree/f99d9e3908dde4865377c75d9ca051c1f545bf4f), following the [literature pass, PR #1024](https://github.com/GettysburgResearch/riemann/pull/1024).  
What was run: analytic derivations, primary-source overlap checks, exact integer/rational replays, and separately labeled floating-point experiments. See [VALIDATION.md](VALIDATION.md).  
Smallest remaining gaps: a Mellin/contour estimate for the corrected arithmetic detector; a cofinal source-specific factor-removal invariant; and an integration-constant inequality for actual xi.

## What survived the attack

| Lane | Concrete result | What it does not establish |
|---|---|---|
| **Arithmetic detector** | An averaged logarithmic derivative retains every zeta zero with positive residue. An explicit divisor-switching profile corrects an order-scale error in its naive main term. | The corrected error has not been bounded on contours inside the critical strip. |
| **Reciprocal-density factor removal** | An exact fourth-order preservation condition; a finite Sra-derived extension allowing deletion through U−70 at the supplied verified height; an explicit reciprocal-entire countermodel to automatic iteration. | Finite deletion does not imply positivity after an arbitrarily long deletion sequence. |
| **Jensen / root dynamics** | An exact integration-constant gate, a hidden-quartet model with all sufficiently high derivatives real-rooted, and an exact polynomial heat-bath law. | The models do not have xi's complete arithmetic source or zero-density asymptotic. |
| **Heat-trace audit appendix** | An independently derived, reviewed finite derivative theorem and a local-versus-global countermodel. | The derivative range is strictly weaker than an existing Polson–Sokolov theorem found during review. It is not a new frontier result. |

These are derivations made in this pass, with limited prior-art screening. **“New to this pass” is not a certified claim of worldwide novelty.** Classical ingredients, existing repository programmes, and newly discovered overlap are documented in [PRIOR_ART.md](PRIOR_ART.md).

## Start here

1. [SYNTHESIS.md](SYNTHESIS.md) explains the surviving mechanisms, their exact missing estimates, and the priority decision.
2. [Arithmetic profile and compensator](arithmetic/progression_profile.md) is the main constructive lead. Read it with the [detector and contour contract](arithmetic/report.md) and the [conditional continuation gate](arithmetic/normality_gate.md).
3. [Factor-removal report](positivity/report.md) gives the local preservation inequality and its countermodel; [near-cutoff removal](positivity/NEAR_CUTOFF_REMOVAL.md) sharpens the finite result through a direct bilateral construction.
   The [Gaussian posterior diagnostic](positivity/GAUSSIAN_POSTERIOR.md) translates the local condition into four conditional moments and identifies the signed-reweighting obstruction.
4. [Dynamics report](dynamics/report.md) gives the exact integration gate and detection scale.
5. [Heat-trace current status](heat_trace/README.md) records the prior-art demotion before linking to the frozen derivation.
6. [VALIDATION.md](VALIDATION.md) separates analytic review, exact finite checks, floating probes, and external work not replayed.

All material is additive and standalone. The repository's integrated result ledger and earlier source audits are unchanged.
