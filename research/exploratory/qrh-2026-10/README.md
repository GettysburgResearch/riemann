# QRH research wave (October 2026)

```text
Status: EXPLORATORY (PROPOSED analysis + IMPORTED external claims); no RH claim
Scope: external zero-free half-plane manuscripts; their exponent architecture; conditional consequences
Exact sources or dependencies: see INTAKE.md (OpenAI 7/8 manuscript, Kintali 47/48 manuscript)
What was actually run: scripts listed below (exact ledger, exact LP certificates, exponent model)
Smallest remaining gap: RH itself (sup Re rho = 1/2) is untouched by everything here
```

RH remains unproved. This folder studies the October 2026 *quasi*-RH manuscripts as an imported
object and as a source of mechanisms. The manuscripts claim a zero-free half-plane `Re s > 7/8`;
they are unreviewed.

## Headline findings (PROPOSED; conditional on the manuscript's stated lemma outputs)

1. **The arithmetic checks out.** The rational arithmetic and polynomial identities turning the
   lemmas into margins pass: 53/53 exact checks (`scripts/ledger_check.py`).
2. **7/8 is set by the low (reflection) estimate**, via `σ0 = 1 − lx/2 − h/6 + θ_low`. The high
   side is tight to `2.3·10⁻⁴`, on rows with mid-depth zeros (`a ≈ 0.69`).
3. **7/8 is effectively optimal for the manuscript's own lemmas.** Re-optimizing the geometry gains
   only `4·10⁻⁵`. Iterating the bootstrap from `β* ≤ 7/8` gains nothing.
4. **Barriers, with exact rational certificates:**
   * the low estimate can never certify below **13/15** in any geometry;
   * zero-free rows, which can only be counted trivially, force **≥ 167/192** at the manuscript's
     detector floor for *any* row-counting input, and → **13/15** as the floor → 1/2;
   * the probe family has a hard floor of **5/6**.
5. **The only escape routes** are cancellation across zero-free rows, beating the large-sieve
   diagonal on the reflected side, or a new probe.
6. **For this repository,** every RH-equivalent subpower premise moves from the trivial exponent
   1/2 to 3/8 under the imported claim. RH needs exponent 0.
7. **The Oct 5 (11/12) architecture has its own ceiling.** Its moment ladder depends only on the
   row/column ratio `ρ`, with boundary `1/2 + 5ρ/12`. `ρ = 1` gives 11/12 at every moment order.
   * `ρ < 1` (fewer rows than columns) is the whole difficulty. Row-blind large sieves cannot reach
     it, and any input that does must contain an on-average GRH for the sextic family.
   * The GL(3) cubic theta vanishes on the needed support.
   * Numerically, the true moments are diagonal-sized at every tested `ρ ≥ 0.35`. What is missing is
     a mechanism ([RUNG_STRENGTH.md](RUNG_STRENGTH.md), [A2_LITERATURE.md](A2_LITERATURE.md)).
8. **Zero density:** the imported 7/8 half-plane does not improve `A(σ)` on `[1/2, 7/8)`
   ([ZERO_DENSITY_CONDITIONAL.md](ZERO_DENSITY_CONDITIONAL.md)).
9. **Verification (bounded agent reviews, exact SHA; not integration verdicts).**
   * **Oct 5 (11/12):** three reviews together read every proof line and found no wrong step
     ([reviews/OCT5_REVIEW_SUMMARY.md](reviews/OCT5_REVIEW_SUMMARY.md)).
   * **Sep 30 (7/8):**
     * contour Lemmas 10.3–10.6 hold below 7/8;
     * Lemma 18.1, a sextic fourth moment that would be new as a standalone theorem, shows no error,
       but its common-support step is unverified;
     * 53/53 arithmetic checks pass.
   * **Kintali (47/48):** Lemma 3 and App. B show no error.
10. **What would move 7/8, priced in the paper's own model**
    ([BILINEAR_B2.md](BILINEAR_B2.md); `results/R_shift_*.json`):
    * a bilinear saving `ϑ` on the low side is worth `≈ 0.81ϑ`;
    * a uniform row-count saving `r` is worth `≈ 0.15r`, down to the floor-bin value 0.8698;
    * better energy alone is worth 0.
    No known theorem supplies `ϑ > 0`.

| File | Content |
|---|---|
| [SYNTHESIS.md](SYNTHESIS.md) | **start here**: the two architectures, what is new, where a breakthrough would have to come from |
| [AGENDA.md](AGENDA.md) | bounded open problems with payoffs (moment ladder, 7/8 escape routes, verification, repo bridges) |
| [INTAKE.md](INTAKE.md) | exact claimed statements, architecture, dependencies, what was verified |
| [HEIGHT_LEVELS.md](HEIGHT_LEVELS.md) | what happens as you go higher, in four senses: moment order (same boundary at the same ρ; the dual type goes A₁ → A₂ → affine Ã₂ → Lorentzian, with the k = 3 pair pattern checked), zero height T, reflection rank, half-plane depth |
| [RUNG_STRENGTH.md](RUNG_STRENGTH.md) | the moment ladder depends only on `ρ = h/k`; `ρ = 1` wall at 11/12; a single-row Prop. R; what any `ρ < 1` input must contain; sub-diagonal numerics |
| [A2_LITERATURE.md](A2_LITERATURE.md) | literature check: exact A2 WMDS dictionary (plus an extra quadratic factor); GL(3) cubic theta vanishes on the support; the missing input is a dispersion asymptotic |
| [moments/DUAL_ANATOMY.md](moments/DUAL_ANATOMY.md) | anatomy of the sub-diagonal cancellation: random-sign-like across pairs, no μ-specific cancelling structure; an explicit Galois secondary term (positive, not cancelling); no dual bias at small D |
| [moments/](moments/README.md) | actual sextic-family `M₂, M₄, M₆` at `H = D^{1+θ}` (and sub-diagonal `k = 1`): diagonal-sized up to `D = 64000` (finite) |
| [ZERO_DENSITY_CONDITIONAL.md](ZERO_DENSITY_CONDITIONAL.md) | QRH-conditional zero density via ANTEDB: no `A(σ)` gain below 7/8; exact μ envelope |
| [reviews/KINTALI_LEMMA3_REVIEW.md](reviews/KINTALI_LEMMA3_REVIEW.md) | Kintali Lemma 3 (weak reflection) and App. B: no error found; DR inputs quoted correctly; theta automorphy, cusp reflection and multiplier checked numerically/exactly; first unverified step App. A.2 (high side) |
| [SHORT_PROOF_FRONTIER.md](SHORT_PROOF_FRONTIER.md) | Part II with only classical full-family Hecke density: `σ₀ = (7A−3)/(7A−2)` (exact LP); Hinz gives 29/31 (needs `M+ℓ > 1` and an unchecked Part I re-run); never below 11/12; our model's "DH counts" = `A = 1` |
| [KINTALI_DENSITY_UPGRADE.md](KINTALI_DENSITY_UPGRADE.md) | Kintali needs only the conductor exponent of a Hecke zero count at σ ≥ 4/5 − η; the best citable input is Hinz 1976 (29/30, so 47/48 = 29/30 + his margin); Hecke analogues of Huxley or Heath-Brown would give 113/120 or 941/1002 (not in the literature); 11/12 is the cap |
| [ROBIN_GRADED.md](ROBIN_GRADED.md) | Θ-graded Robin/Nicolas: under QRH, Robin violations have relative size ≤ (log n)^{−1/8+ε}; sharp given Robin's Ω-theorem (so an asymptotic criterion for QRH); repo Robin packet unchanged |
| [SIEGEL_DETERMINANT.md](SIEGEL_DETERMINANT.md) | the third OpenAI paper (Oct 1, Landau–Siegel via interpolation determinants):<br>• budget inequality; method intrinsically logarithmic-scale; no route to complex or middle-strip zeros<br>• effective in principle, with c ≈ 3·10⁻⁴ from the paper's constants<br>• a weak corollary of either QRH claim |
| [NRC32_TWISTS.md](NRC32_TWISTS.md) | the NRC32 coarse kernel generates only the trivial character; twists give no leverage for issue 902's family-relative step; exact twisted checker (1.29M checks) |
| [BILINEAR_B2.md](BILINEAR_B2.md) | the 7/8 low-side bilinear form exactly (TeX l. 3470); no known estimate beats Cauchy–Schwarz; payoff `σ ≈ 7/8 − 0.8125ϑ` in the paper's own model; the precise missing estimate |
| [DISPERSION_GRH_STEP.md](DISPERSION_GRH_STEP.md) | where GRH enters Dunn–Radziwiłł, and why it is circular for the sextic family; the exact `ρ < 1` identity cancels its dual diagonal via `μ(f)`, and the positivity step loses it |
| [reviews/SEP30_VERIFICATION_MAP.md](reviews/SEP30_VERIFICATION_MAP.md) | dependency map of the 7/8 proof: 65 load-bearing results, of which 19 reviewed and 46 not (36 have no check of any kind); top-5 next targets; Part I is load-bearing (replaceable by the reviewed Oct 5 theorem); the Lean proof is a variant |
| [reviews/OCT5_REVIEW_SUMMARY.md](reviews/OCT5_REVIEW_SUMMARY.md) | **combined R1+R2+R3 bounded review of the Oct 5 (11/12) proof: every proof line read, no wrong step found**; imported: Goldmakher–Louvel, Dunn–Radziwiłł expansions, standard theorems |
| [reviews/OCT5_R1_REDUCTION_POISSON.md](reviews/OCT5_R1_REDUCTION_POISSON.md) | R1: reduction, initialization, Möbius absorption, exact Poisson replay at tiny D |
| [reviews/OCT5_R2_ITERATION_TRANSFER.md](reviews/OCT5_R2_ITERATION_TRANSFER.md) | Oct 5 (11/12) transfer recursion (two Poisson steps, cube reduction, ⌈4/ϑ⌉ levels): PASS conditional on Prop R and Lemma arithmetic; 53 checks; regime H > X undocumented but fine |
| [falsification/PR910_HEIGHT_TEST.md](falsification/PR910_HEIGHT_TEST.md) | PR 910's native-height curve condition: not falsified for T ≤ 10⁶ (max statistic 0.121 vs 1); mechanism = large values of ζ, not zeros; heuristic failure near log T ~ 10³–10⁴; Proposition A (RH-conditional) |
| [CUBIC_FOURTH_MOMENT_TRANSFER.md](CUBIC_FOURTH_MOMENT_TRANSFER.md) | does Lemma 18.1's scheme give the open cubic fourth moment? Straight transfer fails (κ = 5/6 vs 1, at (2,1) common primes); a proposed residue repair closes with zero slack; heuristic relaxed bound X^{53/51+ε} vs the known X^{4/3+ε}; cubic is exactly the boundary case 1/n = 1/3 |
| [reviews/LEMMA18_1_REVIEW.md](reviews/LEMMA18_1_REVIEW.md) | 7/8 manuscript's Lemma 18.1 (fourth moment, sextic family): no error found but the common-support bookkeeping is unverified, so cannot tell; structurally plausible. **Case 1 would itself be new**: no unconditional Lindelöf-strength fourth moment is known for any cubic/quartic/sextic family. Numerics flat to K = 3·10⁶ |
| [falsification/NOISE_FLOOR.md](falsification/NOISE_FLOOR.md) | the missing noise floor for PR 910's height route: Prop. A verified (RH); the route survives iff limsup \|ζ·T_Y\| ≤ 1/√8 (RH); linear resonance arguments give 0; onset heuristic 10^35–10^500; the lemma is open |
| [reviews/CONTOUR_LEMMAS_BELOW_7_8.md](reviews/CONTOUR_LEMMAS_BELOW_7_8.md) | Lemmas 10.3–10.6 remain valid at 139999/160000 with PR 910's substitutions (no gap found in the ranges read) |
| [FOURTH_MOMENT_A2.md](FOURTH_MOMENT_A2.md) | the fourth-moment rung (to 17/24) has cubic GL(3)-metaplectic shape; nesting identity (a2/) |
| [BRIDGE_MELLIN.md](BRIDGE_MELLIN.md) | QRH continuation vs the repo's Mellin–Landau premise; graded NRC32 identity; family-relative step |
| [reports/REPO_RECENT_WORK.md](reports/REPO_RECENT_WORK.md) | digest of prior QRH work in PRs 908–910 and branches (read before extending) |
| [FLOOR_BIN_BARRIER.md](FLOOR_BIN_BARRIER.md) | zero-free rows on the Poisson side: payoff of cross-row cancellation θ (σ = max(13/15, (167−225θ)/(192−225θ)) with DH counts) |
| [ALT_PROBES.md](ALT_PROBES.md) | other metaplectic probes: parity/budget heuristic, cubic minimum 5/6, any theta-type probe ≥ 2/3 (HEURISTIC) |
| [reviews/PR910_REPLAY.md](reviews/PR910_REPLAY.md) | independent exact replay of PR 910's 139999/160000 deduction at SHA 670a76c1: exponent arithmetic PASS (margin ~4x conservative); cosmetic decimal error; first unverified step = contour lemmas below 7/8 |
| [reviews/KINTALI_REVIEW.md](reviews/KINTALI_REVIEW.md) | bounded review of the 47/48 paper: no error found; first unverified step Lemma 3 / App. B; density input identified |
| [numerics/](numerics/README.md) | finite checks: Lemma 7.1 local identity, Kintali eq. (1) phases, joint-moment and Patterson-sum reconnaissance |
| [THRESHOLD_CALCULUS.md](THRESHOLD_CALCULUS.md) | the exponent model, barriers 13/15, 167/192 and 5/6, experiments |
| [CONDITIONAL_CONSEQUENCES.md](CONDITIONAL_CONSEQUENCES.md) | graded Mellin lemma (PROPOSED), conditional corollaries, non-improvements, repo hooks |
| [scripts/ledger_check.py](scripts/ledger_check.py) | 53 exact-rational checks of the manuscripts' stated arithmetic |
| [scripts/threshold_calculus.py](scripts/threshold_calculus.py) | exponent model (exact piecewise-affine row counts; self-tests) |
| [scripts/barrier_lp.py](scripts/barrier_lp.py) | exact LP barrier certificates (output in results/barrier_lp.txt) |
| [scripts/energy_lp.py](scripts/energy_lp.py), [energy_lp_validate.py](scripts/energy_lp_validate.py) | LP supremum of the reflected-energy exponent (14.14) vs closed form |
| [scripts/sensitivity.py](scripts/sensitivity.py), [results/](results/) | scenario optimizations |
| [scripts/SOURCES.txt](scripts/SOURCES.txt) | sha256 of the fetched PDFs |
