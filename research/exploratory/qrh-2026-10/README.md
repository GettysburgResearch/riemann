# QRH research wave (October 2026)

```text
Status: EXPLORATORY (PROPOSED analysis + IMPORTED external claims); no RH claim
Scope: external zero-free half-plane manuscripts; their exponent architecture; conditional consequences
Exact sources or dependencies: see INTAKE.md (OpenAI 7/8 manuscript, Kintali 47/48 manuscript)
What was actually run: scripts listed below (exact ledger, exact LP certificates, exponent model)
Smallest remaining gap: RH itself (sup Re rho = 1/2) is untouched by everything here
```

RH remains unproved. This folder studies the October 2026 *quasi*-RH manuscripts as an imported
object and as a source of mechanisms. The manuscripts claim zero-free half-planes (`Re s > 7/8`
Sep 30; `Re s > 11/12` Oct 5; Kintali `47/48`) and, separately, a Landau–Siegel exclusion (Oct 1);
they are unreviewed by humans. The Lean statement of the Sep 30 claim, `ζ(s) ≠ 0` for `Re s > 7/8`
(Mathlib's `riemannZeta`), has been kernel-checked here with comparator
([reviews/LEAN_BUILD_ATTEMPT.md](reviews/LEAN_BUILD_ATTEMPT.md), Addendum B).

## Headline (end of wave)

* **Formal.** The Lean statement `ζ(s) ≠ 0` for `Re s > 7/8` (Mathlib's `riemannZeta`), and its
  Dirichlet and Hecke-family versions, are accepted by comparator with Lean's kernel; the zeta
  statement also by the independent nanoda kernel. Only the
  standard axioms are used, under the trust assumptions in
  [reviews/LEAN_BUILD_ATTEMPT.md](reviews/LEAN_BUILD_ATTEMPT.md). The wave adds formal corollaries:
  * the strip `1/8 ≤ Re s ≤ 7/8` for nontrivial zeros of `ζ` and of primitive Dirichlet `L`;
  * the Oct 1 Siegel-zero statement with explicit `c = (log 3)/8`.
* **Structure.** The formal proof uses no Part I. On paper, a Part-I-free route is PROPOSED with
  two same-family reviews ([reviews/PART1_FREE_ROUTE.md](reviews/PART1_FREE_ROUTE.md)).
* **Limits.** Both architectures have ceilings for known inputs, 13/15 and 11/12. Numerics show
  that the needed cancellation exists and is random-like. What is missing is a mechanism. RH is
  untouched.

Start with [SYNTHESIS.md](SYNTHESIS.md) §0.

## Headline findings of the analysis (PROPOSED; conditional on the manuscript's stated lemma outputs)

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
     it, and any input that does must imply the large-values count of RUNG_STRENGTH §4 item 3 (an
     on-average GRH for the sextic family).
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
     * Lemma 18.1, a sextic fourth moment that would be new as a standalone theorem: every proof
       line read by bounded reviews, no wrong step found (its zero-slack centred stage was re-read
       separately; see the review rows below);
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
| [HEIGHT_LEVELS.md](HEIGHT_LEVELS.md) | what happens as you go higher, in four senses: moment order (same boundary at the same ρ; the dual coefficient shape on coprime support goes A₁ → A₂ → affine Ã₂ → Lorentzian (PROPOSED analogy), with the k = 3 pair pattern checked), zero height T, reflection rank, half-plane depth |
| [LEVERAGE_FAMILIES.md](LEVERAGE_FAMILIES.md) | is leverage c = 5/6 forced? μ-absorption = the sign of one cubic Jacobi sum (checked exactly); every other examined family fails absorption, the theta step or the leverage (HEURISTIC pipeline model); the only escape found is a GL(2) theta on an n-fold cover, n ∈ {6, 4, 10}, with Hecke × order-n Gauss-sum coefficients (would give 5/6, 7/8, 9/10) |
| [SEXTIC_THETA_S6.md](SEXTIC_THETA_S6.md) | the one escape hatch from 11/12 (S6: explicit sextic GL(2) theta coefficients) is unknown. Bröker–Hoffstein's numerics contradict it for one theta; general case is a finite but cluster-scale computation; bias experiment inconclusive (cubic control reproduces Patterson) |
| [RUNG_STRENGTH.md](RUNG_STRENGTH.md) | the moment ladder depends only on `ρ = h/k`; `ρ = 1` wall at 11/12; a single-row Prop. R and an every-member extraction Prop. R′ (PROPOSED); the endpoint Mom(1, ρ) ∀ρ > 0 ⟺ family GRH; what any `ρ < 1` input must contain; sub-diagonal numerics |
| [A2_LITERATURE.md](A2_LITERATURE.md) | literature check: exact A2 WMDS dictionary (plus an extra quadratic factor); GL(3) cubic theta vanishes on the support; the missing input is a dispersion asymptotic |
| [moments/DUAL_ANATOMY.md](moments/DUAL_ANATOMY.md) | anatomy of the sub-diagonal cancellation: random-sign-like across pairs, no μ-specific cancelling structure; an explicit Galois secondary term (positive, not cancelling); no dual bias at small D |
| [moments/](moments/README.md) | actual sextic-family `M₂, M₄, M₆` at `H = D^{1+θ}` (and sub-diagonal `k = 1`): diagonal-sized up to `D = 64000` (finite) |
| [ZERO_DENSITY_CONDITIONAL.md](ZERO_DENSITY_CONDITIONAL.md) | QRH-conditional zero density via ANTEDB: no `A(σ)` gain below 7/8; exact μ envelope |
| [reviews/KINTALI_LEMMA3_REVIEW.md](reviews/KINTALI_LEMMA3_REVIEW.md) | Kintali Lemma 3 (weak reflection) and App. B: no error found; DR inputs quoted correctly; theta automorphy, cusp reflection and multiplier checked numerically/exactly; first unverified step App. A.2 (high side) |
| [SHORT_PROOF_FRONTIER.md](SHORT_PROOF_FRONTIER.md) | Part II with only classical full-family Hecke density: `σ₀ = (7A−3)/(7A−2)` (exact LP); Hinz gives the model value 29/31, not a theorem (needs `M+ℓ > 1` and an unchecked re-run of Sep 30 Prop. 6.3 and Part I at `X = Y = Z^{16/31}`); never below 11/12; our model's "DH counts" = `A = 1` |
| [KINTALI_DENSITY_UPGRADE.md](KINTALI_DENSITY_UPGRADE.md) | Kintali needs only the conductor exponent of a Hecke zero count at σ ≥ 4/5 − η; the best citable input is Hinz 1976 (29/30, so 47/48 = 29/30 + his margin); Hecke analogues of Huxley or Heath-Brown would give 113/120 or 941/1002 (not in the literature); 11/12 is the cap |
| [ROBIN_GRADED.md](ROBIN_GRADED.md) | Θ-graded Robin/Nicolas: under QRH, Robin violations have relative size ≤ (log n)^{−1/8+ε}; sharp given Robin's Ω-theorem (so an asymptotic criterion for `Θ ≤ 7/8`, the ζ-part of QRH); repo Robin packet unchanged |
| [SIEGEL_DETERMINANT.md](SIEGEL_DETERMINANT.md) | the third OpenAI paper (Oct 1, Landau–Siegel via interpolation determinants):<br>• budget inequality; method intrinsically logarithmic-scale; no route to complex or middle-strip zeros<br>• effective in principle (PROPOSED reading), with c ≈ 3·10⁻⁴ (2.8·10⁻⁴ at the paper's H) from the paper's constants<br>• a weak corollary of either QRH claim |
| [NRC32_TWISTS.md](NRC32_TWISTS.md) | the NRC32 coarse kernel generates only the trivial character; twists give no leverage for issue 902's family-relative step; exact twisted checker (1.29M checks) |
| [BILINEAR_B2.md](BILINEAR_B2.md) | the 7/8 low-side bilinear form exactly (TeX l. 3470); no known estimate beats Cauchy–Schwarz; payoff `σ ≈ 7/8 − 0.8125ϑ` in the paper's own model; the precise missing estimate |
| [Q_RHO_ANALYSIS.md](Q_RHO_ANALYSIS.md) | the reflected-side reformulation (Q_ρ) is circular by duality. Poisson and theta reflection preserve \|cols − rows\| = 1 − ρ, so the ρ = 1 wall is invariant under the whole Oct 5 toolbox. Quadratic-twist moment methods over number fields (Li 2024 etc.) stop at degree 4 |
| [CONDITIONAL_B2.md](CONDITIONAL_B2.md) | 7/8 low side under conjectural inputs, priced exactly (LP) and in the paper's model. **The published de Faveri–Dunn–Hoffstein sieve conjecture buys nothing** (σ stays 7/8), because its extra term *is* the manuscript's Gram excess. Bias-free sieves give 0.837–0.860. Only a sub-diagonal diagonal-size hypothesis (H-diag) moves far, to ≈ 0.686 (barrier 2/3) |
| [DISPERSION_GRH_STEP.md](DISPERSION_GRH_STEP.md) | where GRH enters Dunn–Radziwiłł, and why it is circular for the sextic family; the exact `ρ < 1` identity cancels its dual diagonal via `μ(f)`, and the positivity step loses it |
| [reviews/SEP30_INVMOMENT_REVIEW.md](reviews/SEP30_INVMOMENT_REVIEW.md) | 7/8 inverse-moment engine (Lemmas 17.1–17.6): all three ledgers pass exactly (120/120, with failing controls); the statements reduce to reviewed Oct 5 results at z = 0 but the proof is a different recursion; 11 new Poisson identities; first unverified: eq. (C) (10214–10245) |
| [numerics/COEFF74_CHECK.md](numerics/COEFF74_CHECK.md) | 7/8 coefficient (7.4) equals the product of the (7.10) local summands on 141k tuples (7e-13; all 16 controls fail); remaining gaps listed |
| [reviews/SEP30_REFLECTION_DIFF.md](reviews/SEP30_REFLECTION_DIFF.md) | 7/8 reflection engine (Prop 5.1, Lemmas 5.2–5.7): no discrepancy. Its arithmetic core matches the R3-reviewed Oct 5 appendix, and the remainder was reviewed line by line. Lemma 5.5 is new mathematics ((K+NB)NB, stronger than Oct 5's route) and checks out; 125,820 multiplier values match exactly |
| [reviews/SEP30_LOWSIDE_REVIEW.md](reviews/SEP30_LOWSIDE_REVIEW.md) | 7/8 low-side chain (Cor 14.1 to Prop 15.3), which sets the constant: no wrong step found; the zero excess (exactly lx/2 + b/12 − d) re-derived; 76 checks; first unverified step is the branch-compatibility clause of Prop 5.1 (addressed in SEP30_REFLECTION_DIFF) |
| [reviews/SEP30_JUNCTION_CHECK.md](reviews/SEP30_JUNCTION_CHECK.md) | 7/8 row-count junction: every quantitative lemma-hypothesis instance certified in exact rationals (84/84, 8 failing controls). Lemma 18.1 is used on its boundary. Qualitative side conditions unchecked |
| [reviews/SEP30_EQC_CHECK.md](reviews/SEP30_EQC_CHECK.md) | 7/8 eq. (C) (first-Poisson CRT/reciprocity identification in Lemma 17.2): verified by hand, on 900 exact tuples and by an end-to-end replay; 14 controls fail |
| [reviews/SEP30_DETECTOR_QUANTIFIERS.md](reviews/SEP30_DETECTOR_QUANTIFIERS.md) | 7/8 zero detector (Lemmas 8.1–8.3), quantifier order of Prop 20.3, Prop 16.1: no gap found (114 exact checks). **The detector floor 51/100 is a convention: any 1/2+η works.** Four independence claims in Prop 20.3 are accepted without proof |
| [reviews/LEAN_BUILD_ATTEMPT.md](reviews/LEAN_BUILD_ATTEMPT.md) | Lean build of the 7/8 comparator closure (pinned toolchain and Mathlib; cache; patches): **complete** (7061 jobs, 0 errors, 0 `sorry`); `#print axioms` = `[propext, Classical.choice, Quot.sound]` for the zeta, Dirichlet and Hecke 7/8 theorems; **comparator accepts the upstream zeta (Addendum B), Dirichlet and Hecke challenges, and the wave's Siegel and strip corollaries (Addendum C)**, with trust assumptions; the upstream Oct 1 Siegel proof is also accepted; the zeta challenge is also accepted by the independent **nanoda** kernel (Addendum C) |
| [reviews/SEP30_LEAN_CORRESPONDENCE.md](reviews/SEP30_LEAN_CORRESPONDENCE.md) | paper-to-Lean map for the 7/8 theorem: the Lean route has **no Part I** (`β ≤ 1` plus an extended endpoint count replaces the 11/12 bootstrap), proves its own instances of the cited theorems, and otherwise uses the paper's exponent bookkeeping; 65 nodes coded F 6 / Fv 8 / C 37 / B 8 / N 6; lexical trust scan clean |
| [reviews/PART1_FREE_ROUTE.md](reviews/PART1_FREE_ROUTE.md) | **PROPOSED Part-I-free paper route to 7/8**: Part II as written plus an extended endpoint count (`(1+5r)/6 − δr − (1−δ) = (5/6−δ)(r−1)`) would prove 7/8 from `β* ≤ 1` (PROPOSED; bounded same-family review only); no Part I and no 11/12 import; 32/32 exact gates, 10/10 controls; junction replay on `Δ ≤ 1/8`. Second agent review: "(A) with corrections" ([reviews/PART1_FREE_ROUTE_REVIEW2.md](reviews/PART1_FREE_ROUTE_REVIEW2.md)). A new composition that still needs independent review |
| [EXPLICIT_PNT_7_8.md](EXPLICIT_PNT_7_8.md) | **explicit** consequences of the Lean-checked `H(7/8)` (PROPOSED derivations; imported explicit inputs: Platt–Trudgian, Büthe, Hasanalizade–Shen–Wong, Cully-Hugill–Johnston, Nicolas): `\|ψ(x)−x\| ≤ 0.0026 x^{7/8} log² x` (x ≥ 227), `π − li`, short-interval primes, and ROBIN_GRADED's envelope with explicit thresholds; interval arithmetic; crossover with unconditional tables near `10^{110}` |
| [proposed/PART1_FREE_7_8/](proposed/PART1_FREE_7_8/README.md) | **PROPOSED** Part-I-free 7/8 composition: Remark 19.3 as Lemma P1F.0 with full proof (no use of `δ ≤ 5/6` before 15303), P1F.1-P1F.2 with review-2 correction, Lean counterparts (`no_slot_inverse_count`, `high_bin_count`, `high_source_margin`); 43/43 exact gates, 14 controls. Needs independent review |
| [reviews/HECKE_LEAN_FIDELITY.md](reviews/HECKE_LEAN_FIDELITY.md) | fidelity of the Lean Hecke-family definitions (written into the challenge file): `Character` = ray class characters of `Q(ω)` trivial on units; `LFunction` = the continued Hecke `L`-function; matches the paper's Thm 1.1 Hecke clause with the same pole exception (reading + float cross-checks to about 1e-11; no Lean run) |
| [DETECTOR_DENSITY.md](DETECTOR_DENSITY.md) | mechanism: the 7/8 contradiction detects **one** zero and cannot count (more witnessed rows raise the high-side error); the inner detector gives a family zero-density exponent `f(σ) = (31−32σ)/(21−12σ)`, `f(7/8) = 2/7`, beating de Faveri's 2026 sextic large-sieve density (0.466) but not density-hypothesis quality (PROPOSED; exact model, 21/21 gates) |
| [lean/](lean/README.md) | formal corollaries built on the 7/8 theorem: nontrivial zeros of `ζ` lie in `1/8 ≤ Re s ≤ 7/8` (in the shape of Mathlib's `RiemannHypothesis`); the same for primitive Dirichlet `L`; the Oct 1 Siegel-zero challenge statement with `c = (log 3)/8`. Axioms standard; comparator accepted the Siegel corollary and the zeta strip (Addendum C) |
| [numerics/B2_NUMERICS.md](numerics/B2_NUMERICS.md) | the 7/8 low-side bilinear form numerically: the true form is ≈ Q^{−1/2} below Cauchy–Schwarz, exactly as for random phases. The relevant Gram sits at its diagonal, far below the large-sieve constant. The gap is provability, not truth |
| [proposed/OCT5_11_12_PACKET/](proposed/OCT5_11_12_PACKET/README.md) | **PROPOSED** integration-packet draft for the Oct 5 (11/12) proof (statement, dependency chain, review record, proof outline, rerunnable checks, integrator gaps). Not an integrated packet |
| [reviews/SEP30_L13_L45_REVIEW.md](reviews/SEP30_L13_L45_REVIEW.md) | 7/8 common-support correlations (Lemmas 13.3, 13.4; 13.2 now exact) and smooth calculus (Lemma 4.5): no wrong step. Millions of exact local values brute-forced in Z[ω]; 12 mutation controls detected; 33/33 checks |
| [reviews/PART1_SUBSTITUTION.md](reviews/PART1_SUBSTITUTION.md) | the 7/8 proof uses Part I only through β* ≤ 11/12, which the Oct 5 theorem supplies, so the substitution is valid at statement level. **Eight Part-I-only nodes leave the 7/8 critical path.** Lemmas 11.1 and 19.1 show no wrong step. Caveat: the reflection inputs are shared, so the risk is not diversified |
| [reviews/SEP30_L17_IDENTITIES.md](reviews/SEP30_L17_IDENTITIES.md) | all 11 new identities of the 7/8 inverse-moment engine check out. The second Poisson transform in child form reproduces the direct lattice sum to 8.7e-16. Lemmas 17.3–17.6 are correct (55/55 checks). Remaining: the analytic Fourier separations, and 17.1's initialization transform |
| [reviews/SEP30_SEC4_REVIEW.md](reviews/SEP30_SEC4_REVIEW.md) | 7/8 Section 4 helper lemmas (4.1, 4.6–4.10) and Lemma 13.1: no wrong step found; mechanical checks |
| [reviews/SEP30_MISC_REVIEW.md](reviews/SEP30_MISC_REVIEW.md) | 7/8 Lemma 17.1 initialization (replayed to 3e-15, 9 controls break), Lemma 15.1 (exponent level, worst case exactly 0), Lemma 20.1, Prop 2.1, and the Thm 1.1 final contradiction: no error found (48/48 checks) |
| [reviews/SEP30_VERIFICATION_MAP_V2.md](reviews/SEP30_VERIFICATION_MAP_V2.md) | **updated 7/8 verification map**. v2 + addendum v2.1 (§10): as written R 49, partial 6, I 2, A 3, U 5 (65 nodes). With the Oct 5 substitution: R 49, partial 6, I 2 of 57, **0 A/U**; by lines 67% R and 99% R+partial. Bounded agent reviews only, not an integration verdict |
| [reviews/SEP30_VERIFICATION_MAP.md](reviews/SEP30_VERIFICATION_MAP.md) | dependency map of the 7/8 proof: 65 load-bearing results, of which 19 reviewed and 46 not (36 have no check of any kind); top-5 next targets; Part I is load-bearing (replaceable by the reviewed Oct 5 theorem); the Lean proof is a variant |
| [reviews/OCT5_REVIEW_SUMMARY.md](reviews/OCT5_REVIEW_SUMMARY.md) | **combined R1+R2+R3 bounded review of the Oct 5 (11/12) proof: every proof line read, no wrong step found**; imported: Goldmakher–Louvel, Dunn–Radziwiłł expansions, standard theorems |
| [reviews/OCT5_RESIDUAL_ITEMS.md](reviews/OCT5_RESIDUAL_ITEMS.md) | Oct 5 residual items closed: the Goldmakher–Louvel use matches their Thm 1.1; the contour shift is complete; R1's minor points are harmless |
| [reviews/OCT5_REFLECTION_E2E.md](reviews/OCT5_REFLECTION_E2E.md) | **end-to-end numerical confirmation of Oct 5 eq:reflection** (the key theta reflection): 56 runs, X up to 20000, relative error 6.5e-15 to 3.6e-10; all cusps and local cases j = 0..5; 6 controls break agreement. Schwartz weights only; compact-support W out of budget |
| [reviews/OCT5_R1_REDUCTION_POISSON.md](reviews/OCT5_R1_REDUCTION_POISSON.md) | R1: reduction, initialization, Möbius absorption, exact Poisson replay at tiny D |
| [reviews/OCT5_R2_ITERATION_TRANSFER.md](reviews/OCT5_R2_ITERATION_TRANSFER.md) | Oct 5 (11/12) transfer recursion (two Poisson steps, cube reduction, ⌈4/ϑ⌉ levels): PASS conditional on Oct 5 prop:R and Lemma arithmetic; 53 checks; regime H > X undocumented but fine |
| [falsification/PR910_HEIGHT_TEST.md](falsification/PR910_HEIGHT_TEST.md) | PR 910's native-height curve condition: not falsified for T ≤ 10⁶ (max statistic 0.121 vs 1); mechanism = large values of ζ, not zeros; heuristic failure near log T ~ 10³–10⁴; Proposition A (RH-conditional) |
| [reviews/LEMMA18_1_COMMON_SUPPORT.md](reviews/LEMMA18_1_COMMON_SUPPORT.md) | the previously unverified common-support allocations of Lemma 18.1 (l. 13192–13349, 13686–13933): no error found; 24/24 checks including an end-to-end exact-symbol bridge test with failing variants; one unused f/6 of slack |
| [reviews/LEMMA18_1_CASE2_SEC188.md](reviews/LEMMA18_1_CASE2_SEC188.md) | Lemma 18.1 case 2 and Sec. 18.8: no wrong step (50/50 exact, 17 controls fail). With the two earlier reviews, **every proof line of Lemma 18.1 has now been read with no wrong step found**. A fourth zero-slack point was identified. Helper Lemmas 4.x and the Sec. 13 lemmas are imported |
| [CUBIC_FOURTH_MOMENT_TRANSFER.md](CUBIC_FOURTH_MOMENT_TRANSFER.md) | does Lemma 18.1's scheme give the open cubic fourth moment? Straight transfer fails (κ = 5/6 vs 1, at (2,1) common primes); a proposed residue repair closes with zero slack; heuristic relaxed bound X^{53/51+ε} vs the known X^{4/3+ε}; cubic is exactly the boundary case 1/n = 1/3 |
| [CUBIC_RELAXED_INDUCTION.md](CUBIC_RELAXED_INDUCTION.md) | cubic fourth moment via Lemma 18.1's scheme (exponent ledgers only, conditional): X^{53/51} in the paper's order (optimal); X^{1+ε} with the (2,1) forcing at zero slack; **X^{1+ε} with margin M/12 under a PROPOSED nested induction order, which reproduces Heath-Brown's quadratic K^{1+ε} as a calibration**. Literature best is X^{4/3}; six steps unproved |
| [reviews/CUBIC_NESTED_REDTEAM.md](reviews/CUBIC_NESTED_REDTEAM.md) | adversarial check of the nested induction for the cubic fourth moment: **no break found**. The order is well-founded (lexicographic, 2 same-width stages). The uniform margin is ≈ 0.018M. Patterson bias is modelled, not ignored, and GLH rules out a genuine X^{4/3} term. The quadratic calibration matches only the exponent. Smallest gap: the n = 3 centred-stage saving |
| [reviews/SEP30_L42_44_REVIEW.md](reviews/SEP30_L42_44_REVIEW.md) | 7/8 Lemmas 4.2-4.4 (prime Gauss identities, quadratic four-term formula, sextic reciprocity and the fixed Gauss phase): no wrong step found (bounded, one agent); 65/65 exact checks with failing controls; imports classical cubic reciprocity |
| [reviews/LEMMA18_THETA_ROW_REVIEW.md](reviews/LEMMA18_THETA_ROW_REVIEW.md) | fresh-eyes review of Lemma 18.1's centred Θ-row stage (Lemmas 18.2-18.3, (2.15)-(2.19)): no wrong step found; the zero-slack point `v = L` does not use Lemma 18.3; exact ledger 19/19, float64 lattice model 14/14 (EMPIRICAL) |
| [proposed/SEXTIC_FOURTH_MOMENT/](proposed/SEXTIC_FOURTH_MOMENT/README.md) | **PROPOSED packet draft**: Lemma 18.1 case 1 of the 7/8 manuscript as a standalone sextic fourth moment (imported claim; bounded agent reviews only; not integrated) |
| [reviews/CUBIC_CENTRED_ATTACK.md](reviews/CUBIC_CENTRED_ATTACK.md) | adversarial attack on the cubic route's centred stage: survives at the level of the displayed steps; 18/19 checks (one scale-limited, uninformative FAIL); open: identical action on both rectangles |
| [reviews/CUBIC_BOTH_RECTANGLES.md](reviews/CUBIC_BOTH_RECTANGLES.md) | the cubic route's "both rectangles" condition: closed at the level of the displayed steps (the rectangles are the original and comparison products; every Θ-row step acts identically; the non-Θ split costs `0·M`; `n = 3` adds no asymmetry); exact model 12/12 |
| [reviews/END_WAVE_REDTEAM.md](reviews/END_WAVE_REDTEAM.md) | red team of the end-of-wave additions (26 issues; all addressed in the following commit) |
| [proposed/CUBIC_FOURTH_MOMENT/](proposed/CUBIC_FOURTH_MOMENT/README.md) | **PROPOSED proof sketch** of Σ_{Nc≤X}\|L(1/2,χ_c)\|⁴ ≪ X^{1+ε} for cubic Hecke characters of Q(ω) (open; literature X^{4/3}).<br>• Conditions: (H-A) the order-independent parts of Lemma 18.1 case 1 transfer to n = 3; (H-B) a nested induction order<br>• Contents: application step written out; margin (11−147δ)/612 ≈ 0.018 (exact check); risk register |
| [CUBIC_N3_GAPS.md](CUBIC_N3_GAPS.md) | the three cubic-specific gaps: none hides an order-M loss (38/38 exact Z[ω] checks, 14 controls caught). **Status: conditional on Lemmas 4.5/4.7 + Lemma 18.1 case 1 ledgers and the PROPOSED nested order, Σ\|L(1/2,χ_c)\|⁴ ≪ X^{1+ε}** (open problem; literature X^{4/3}). Steps still needing human-level proof are listed |
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
