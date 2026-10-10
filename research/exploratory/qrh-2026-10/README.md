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

| File | Content |
|---|---|
| [SYNTHESIS.md](SYNTHESIS.md) | **start here**: the two architectures, what is new, where a breakthrough would have to come from |
| [AGENDA.md](AGENDA.md) | bounded open problems with payoffs (moment ladder, 7/8 escape routes, verification, repo bridges) |
| [INTAKE.md](INTAKE.md) | exact claimed statements, architecture, dependencies, what was verified |
| [RUNG_STRENGTH.md](RUNG_STRENGTH.md) | the moment ladder depends only on `ρ = h/k`; `ρ = 1` wall at 11/12; a single-row Prop. R; what any `ρ < 1` input must contain; sub-diagonal numerics |
| [A2_LITERATURE.md](A2_LITERATURE.md) | literature check: exact A2 WMDS dictionary (plus an extra quadratic factor); GL(3) cubic theta vanishes on the support; the missing input is a dispersion asymptotic |
| [moments/](moments/README.md) | actual sextic-family `M₂, M₄, M₆` at `H = D^{1+θ}` (and sub-diagonal `k = 1`): diagonal-sized up to `D = 64000` (finite) |
| [ZERO_DENSITY_CONDITIONAL.md](ZERO_DENSITY_CONDITIONAL.md) | QRH-conditional zero density via ANTEDB: no `A(σ)` gain below 7/8; exact μ envelope |
| [reviews/KINTALI_LEMMA3_REVIEW.md](reviews/KINTALI_LEMMA3_REVIEW.md) | Kintali Lemma 3 (weak reflection) and App. B: no error found; DR inputs quoted correctly; theta automorphy, cusp reflection and multiplier checked numerically/exactly; first unverified step App. A.2 (high side) |
| [NRC32_TWISTS.md](NRC32_TWISTS.md) | the NRC32 coarse kernel generates only the trivial character; twists give no leverage for issue 902's family-relative step; exact twisted checker (1.29M checks) |
| [BILINEAR_B2.md](BILINEAR_B2.md) | the 7/8 low-side bilinear form exactly (TeX l. 3470); no known estimate beats Cauchy–Schwarz; payoff `σ ≈ 7/8 − 0.8125ϑ` in the paper's own model; the precise missing estimate |
| [DISPERSION_GRH_STEP.md](DISPERSION_GRH_STEP.md) | where GRH enters Dunn–Radziwiłł, and why it is circular for the sextic family; the exact `ρ < 1` identity cancels its dual diagonal via `μ(f)`, and the positivity step loses it |
| [reviews/OCT5_REVIEW_SUMMARY.md](reviews/OCT5_REVIEW_SUMMARY.md) | **combined R1+R2+R3 bounded review of the Oct 5 (11/12) proof: every proof line read, no wrong step found**; imported: Goldmakher–Louvel, Dunn–Radziwiłł expansions, standard theorems |
| [reviews/OCT5_R1_REDUCTION_POISSON.md](reviews/OCT5_R1_REDUCTION_POISSON.md) | R1: reduction, initialization, Möbius absorption, exact Poisson replay at tiny D |
| [reviews/OCT5_R2_ITERATION_TRANSFER.md](reviews/OCT5_R2_ITERATION_TRANSFER.md) | Oct 5 (11/12) transfer recursion (two Poisson steps, cube reduction, ⌈4/ϑ⌉ levels): PASS conditional on Prop R and Lemma arithmetic; 53 checks; regime H > X undocumented but fine |
| [falsification/PR910_HEIGHT_TEST.md](falsification/PR910_HEIGHT_TEST.md) | PR 910's native-height curve condition: not falsified for T ≤ 10⁶ (max statistic 0.121 vs 1); mechanism = large values of ζ, not zeros; heuristic failure near log T ~ 10³–10⁴; Proposition A (RH-conditional) |
| [reviews/LEMMA18_1_REVIEW.md](reviews/LEMMA18_1_REVIEW.md) | 7/8 manuscript's Lemma 18.1 (fourth moment, sextic family): no error found but the common-support bookkeeping is unverified, so cannot tell; structurally plausible. **Case 1 would itself be new**: no unconditional Lindelöf-strength fourth moment is known for any cubic/quartic/sextic family. Numerics flat to K = 3·10⁶ |
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
