# Pre-public independent review — PRs #4, #19, #21, #22, #23, #24, #27, #30, #33, #34, #37, #38, #40, #43

Reviewer: `gpt56-08`  
Review date: 2026-08-01  
Repository: `gfreund123/riemann`  
Scope: frozen-commit review only; no merges and no public-README edits

## Classification convention

- **VERIFIED** — the load-bearing claims are correct within their explicitly stated scope, hypotheses, and status. This does not promote a `PROPOSED` claim to repository `PROVED`, and it never turns a finite computation into RH.
- **VERIFIED WITH FIXES** — the mathematical core survives, but a concrete source, wording, status, artifact, or integration correction is required before pre-public merge.
- **GAP/BLOCKED** — a load-bearing identity, admissibility theorem, source import, or proof artifact is absent at the frozen commit. Independently passing subclaims are listed and remain verified.
- **REJECTED** — a load-bearing statement is false as written. No assigned PR received this classification.

No expensive computation was rerun. I inspected theorem and lemma proofs, exact checkers, representative artifacts, and dependency boundaries. Small independent checks included symbolic differentiation of the Euler-gamma enclosure functions, verification of the `L-4102` finite-jet formula through order five, and direct algebraic checks of the carrier and rank-one identities.

## Frozen heads

| PR | Frozen head SHA | Classification |
|---:|---|---|
| #4 | `a02020fcfdd90a10fffe31f397f7cffeb8d6eed7` | **GAP/BLOCKED** |
| #19 | `1c397d65d204c4a332a505ac7510121923c28fcc` | **VERIFIED WITH FIXES** |
| #21 | `2028e331486b2c4b9f0ab41cbbb85cc0bc48cfa4` | **VERIFIED WITH FIXES** |
| #22 | `749ecfd0d2af53fa6eb8fdb786b7ad0c218cd462` | **VERIFIED** |
| #23 | `c767c494c842680f6db7dd927b4e5aacd4dd2f4b` | **VERIFIED WITH FIXES** |
| #24 | `ae477857d036fc182adb8db4e34e846fde7931b3` | **VERIFIED** |
| #27 | `814880e75639d78ffe88bf1aca340218936abeac` | **VERIFIED WITH FIXES** |
| #30 | `e8d9a0d446308d7a179d354f4bb5c0cda698a779` | **VERIFIED WITH FIXES** |
| #33 | `eed9b53ec995dfca119048eae060aab630f6065b` | **VERIFIED** |
| #34 | `eda7ba6e378851ebe7ec1441b6503ba365eb0e35` | **VERIFIED WITH FIXES** |
| #37 | `79280f9524200d158d23d5a01091b58f272477f6` | **VERIFIED WITH FIXES** |
| #38 | `5c360c9202244051b27e2fc2a2b39bebe002e6d5` | **VERIFIED WITH FIXES** |
| #40 | `36148418ee5c6ce1c294f66a0fc75a258810f796` | **VERIFIED** |
| #43 | `f0220189f99d3500b7b65742eea302c5a2d54a75` | **VERIFIED** |

## Per-PR findings

### PR #4 — **GAP/BLOCKED**

Load-bearing files:

- `claims/definitions/D-0001-cutoff-free-weil-block.md`
- `claims/lemmas/L-0001-negative-weil-direction.md`
- `experiments/X-0001-cutoff-free-weil-scan/verify_dyadic_certificate.py`

Verified independently:

1. Once the exact finite Guinand--Weil dictionary, real-axis autocorrelation identity, and absolute zero-sum convergence are assumed, `L-0001` is a correct contrapositive: a strict directed negative value disproves RH.
2. The divided-difference contractions have the declared prime, pole, and archimedean factors. In particular, the prime contraction is `-sum Lambda(q)/sqrt(q) K_v(1-log(q)/log(c))`, and the pole contraction agrees with `g(i/2)+g(-i/2)`.
3. The exact checker is sound for what it claims: it recomputes an interval Rayleigh contraction from supplied primitive entry intervals and refuses intervals touching zero.

Blocker:

`D-0001` does not itself prove the admissibility of every `g_v`, the complete autocorrelation-square identity, or the exact identification of the cutoff-free closed-form matrix with the classical Guinand--Weil formula. It traces these to a recent finite-dictionary preprint and source repository and explicitly leaves independent reconstruction open. The checker verifies interval propagation, not analytic provenance. This is the shared load-bearing blocker for PRs #23, #27, #30, and #37.

Pre-public action: keep `D-0001/L-0001` at `PROPOSED`; do not describe an X-0001 sign as an RH certificate until a separate normalization/admissibility audit is merged.

### PR #19 — **VERIFIED WITH FIXES**

Load-bearing files:

- `claims/lemmas/L-0201-record-maximizer-reduction.md`
- `claims/theorems/T-0201-superabundant-completeness.md`
- `experiments/X-0202-robin-finite-barrier/verify.py`

Verified:

1. The least record maximizer below a Robin counterexample is superabundant and is itself a Robin counterexample; the quantifiers and monotonicity direction in `L-0201` are correct.
2. The exact divisor-sum maxima on `[1,5040]` and `[5041,5582]`, together with the two strict transcendental signs, imply the finite barrier and the reduction in `T-0201`.
3. X-0202 enumerates the finite ranges by exact integer divisor sums and compares rational abundancy ratios by cross multiplication.

Required fixes/integration:

- The frozen X-0202 transcendental layer reuses the X-0201 directed-Decimal engine and correctly labels independent reproduction pending. PR #24 supplies the genuinely independent integer/dyadic reproduction; pre-public promotion should cite that later artifact.
- The PR is stale against its base and must be restacked before merge. The review remains pinned to the frozen SHA above.
- X-0201's colossally-abundant scan remains empirical and is not the completeness proof.

Merge order: `#19 -> #24 -> #34 -> #40`.

### PR #21 — **VERIFIED WITH FIXES**

Representative load-bearing files:

- `claims/definitions/D-0301-standard-xi-normalization.md`
- `claims/lemmas/L-0302-argument-principle-zero-count.md`
- `claims/lemmas/L-0304-winding-number-stability.md`
- `claims/lemmas/L-0321-robin-exponent-swap-dominance.md`
- `claims/lemmas/L-0340-li-unit-circle-geometry.md`
- `claims/theorems/T-0301-robin-criterion.md`
- `claims/theorems/T-0303-li-criterion.md`
- `claims/theorems/T-0304-nicolas-criterion.md`
- `claims/theorems/T-0306-speiser-criterion.md`
- `claims/theorems/T-0308-polya-jensen-criterion.md`
- `claims/theorems/T-0309-debruijn-newman-threshold.md`
- `claims/theorems/T-0310-verified-zero-height.md`

Verified:

1. The standard `xi` normalization, zero symmetries, argument-principle count, Rouché certificate, and winding perturbation lemma are correct.
2. The Robin, Li, Nicolas, Speiser, and de Bruijn--Newman cards correctly separate imported equivalences from finite witness implications and preserve strict/open boundary conventions.
3. `T-0308` matches the effective Jensen theorem: partial RH through height `T` yields hyperbolicity in the stated degree range `d <= floor(T)^2` for the declared shifts.
4. The exponent-swap, primorial recurrence, Li unit-circle geometry, and finite dynamic-program lemmas are algebraically correct.

Required correction:

`T-0310-verified-zero-height.md` says the Platt--Trudgian publisher/arXiv abstracts explicitly state that all zeros in the range are simple. They state rigorous critical-line location and the total number of zeros, but do not explicitly state simplicity. The paper explains that sign changes are counted and Turing's method accounts for all expected zeros. Simplicity is plausibly deducible if the certified sign-change count equals the total zero count with multiplicity, but that deduction must be written from the full computation theorem or the word `simple` must be removed. A proposed repair cannot retroactively verify this sentence.

Additional source boundary: the original Nicolas and Speiser papers and Robin's original proof were not directly reconstructed; the cards correctly remain imported `PROPOSED` interfaces.

Merge order: this atlas should precede #22 and the Li/Nicolas-dependent portions of #33; #38 is independent but uses the same xi normalization.

### PR #22 — **VERIFIED**

Load-bearing files:

- `claims/lemmas/L-0401-li-local-cauchy-formulas.md`
- `claims/lemmas/L-0402-li-finite-certificate-reductions.md`
- `claims/lemmas/L-0403-li-verified-height-amplification-barrier.md`
- `experiments/X-0401-li-coefficient-search/verify_dyadic_certificate.py`

Findings:

1. The local recurrence, Cauchy coefficient formula, roots-of-unity alias identity, and geometric outer-circle alias bound are correct.
2. `L-0403` correctly states a limitation: finite verification of zeros supplies a quantitative amplification barrier, not positivity of all Li coefficients.
3. The Fraction-only checker validates exact recurrence or Cauchy/DFT interval propagation, checks complete local tables and radius ordering, and explicitly refuses to certify analytic provenance of supplied xi enclosures.
4. `O-0401` is a finite empirical positive scan and is not promoted to RH evidence.

Integration: merge after #21. A future real certificate still needs an independent directed analytic producer for the xi or log-xi data.

### PR #23 — **VERIFIED WITH FIXES**

Load-bearing files:

- `claims/lemmas/L-0601-prime-power-derivative-jump.md`
- `claims/lemmas/L-0602-moment-neutral-edge-order.md`
- `claims/lemmas/L-0603-rank-one-susceptibility.md`
- `claims/lemmas/L-0604-lerch-resummation.md`

Verified:

- The prime-threshold derivative jump, its rank-one form, the moment-neutral edge order, the exact rank-one susceptibility threshold, and the Lerch partial-fraction resummation are correct under the declared D-0001 matrix normalization.
- The frozen-background susceptibility is correctly labeled a ranking statistic rather than a crossing theorem.

Required integration fix:

Every arithmetic application inherits PR #4's unresolved finite-dictionary/admissibility gate. X-0601 is ordinary numerical reconnaissance and does not produce a directed full-matrix witness. Preserve the lemmas as verified conditional calculus; block any RH-facing promotion until #4's source identity is independently closed.

Merge order: after #4's normalization audit, not merely after its current frozen head.

### PR #24 — **VERIFIED**

Load-bearing files:

- `claims/lemmas/L-2001-positive-atanh-log-enclosure.md`
- `claims/lemmas/L-2002-euler-gamma-harmonic-enclosure.md`
- `claims/lemmas/L-2003-positive-exponential-enclosure.md`
- `claims/lemmas/L-2005-canonical-exponent-support-dominance.md`
- `claims/theorems/T-2001-independent-robin-finite-barrier.md`
- `claims/theorems/T-2002-hardy-ramanujan-completeness.md`
- `experiments/X-2001-independent-robin-barrier/`

Findings:

1. The logarithm, Euler-gamma, and exponential enclosures use outward integer/dyadic arithmetic and valid positive-tail bounds. Independent symbolic differentiation confirms the monotonic enclosure functions in `L-2002`.
2. The finite maxima and signs at `5041`, `5582`, and `5583` establish the stated finite barrier independently of PR #19's Decimal engine.
3. The canonical consecutive-prime/nonincreasing-exponent reduction is correct, including the finite-window case split needed when the canonical image lies at or below `5040`.
4. The code's arithmetic contract is exact; hashes are provenance aids rather than logical premises.

Scope: this proves a finite structural dependency and canonical reduction, not Robin's original equivalence and not RH.

Merge order: after #19 because it repairs and independently verifies #19's finite dependency; before #34.

### PR #27 — **VERIFIED WITH FIXES**

Load-bearing files:

- `claims/definitions/D-0701-carrier-shifted-test-family.md`
- `claims/lemmas/L-0701-compact-archimedean-carrier-formula.md`
- `claims/lemmas/L-0702-carrier-gram-kernel.md`

Verified:

- The compactly supported real carrier family, Fourier shifts, convolution/Gram kernel, sinc conventions, pole formula, and cancellation-safe archimedean integral are algebraically consistent.
- The one-carrier prime, pole, and archimedean signs match the standard explicit formula, conditional on D-0001.

Required integration fix:

The RH-facing identity still inherits PR #4's admissibility and exact finite-dictionary gate. The numerical carrier screens omit or approximate terms and are correctly empirical; they cannot be promoted. Keep the Fourier/archimedean lemmas verified in conditional scope, but block proof-level integration until #4 is repaired.

Merge order: after the repaired #4; #37 stacks on this PR.

### PR #30 — **VERIFIED WITH FIXES**

Load-bearing files:

- `claims/lemmas/L-0605-prime-source-compression.md`
- `claims/lemmas/L-0606-carrier-packet-bridge.md`
- `claims/methodology/M-0602-moment-corrected-carrier-transform.md`
- `experiments/X-0602-carrier-packet-search/validate_bridge.py`

Verified:

- The finite prime-source compression and packet convolution formulas are correct under D-0001.
- The Taylor-corrected nonuniform FFT remainder is a valid analytic gridding bound.
- `validate_bridge.py` independently checks the scalar/matrix lattice normalization at selected controls.

Required fixes/boundaries:

- The FFT theorem controls only nonuniform Taylor truncation; it explicitly excludes phase reduction, accumulation, FFT roundoff, matrix conversion, and eigenvalue conditioning.
- The bridge validation is high-precision ordinary arithmetic, not a directed proof.
- All RH-facing uses remain blocked on #4's source identity.

Merge order: after repaired #4; it is a sibling of #23/#27 rather than a replacement for their proof gates.

### PR #33 — **VERIFIED**

Load-bearing files:

- `L-3101-quantitative-dyadic-negative-witness.md`
- `L-3102-carrier-prime-tail-gram-bound.md`
- `L-3103-capped-robin-subtree-ceiling.md`
- `L-3104-second-derivative-chord-tube.md`
- `L-3105-li-quartet-negative-window.md`
- `L-3106-pareto-frontier-prime-product.md`
- `L-3107-additive-nicolas-margin.md`

All seven finite lemmas are correct within their explicit hypotheses:

- exact interval perturbation and chord bounds;
- the `-G <= C(xi) <= G` omitted-prime Gram envelope;
- safe Robin cap pruning;
- the factor-six phase-alignment window for one off-line Li quartet, with no claim that the total Li coefficient is negative;
- exact integer Pareto dominance;
- the restartable Nicolas margin recurrence.

Integration concern: this is a mixed-route PR. `L-3102` inherits #27/#4 for its Weil interpretation, `L-3103` uses the Robin stack, and `L-3105/L-3107` use #21. Claim-level dependencies should be preserved; a monolithic merge must not make the carrier lemma appear unconditionally normalized.

### PR #34 — **VERIFIED WITH FIXES**

Load-bearing files:

- `claims/lemmas/L-2501-finite-canonical-tree-enumeration.md`
- `claims/lemmas/L-2502-size-aware-tail-ceiling.md`
- `claims/theorems/T-2501-terminal-prefix-certificate.md`
- `claims/theorems/T-2502-finite-robin-region-from-canonical-certificate.md`
- `experiments/X-2501-canonical-robin-tree/verify.py`
- `experiments/X-2501-canonical-robin-tree/certmath.py`
- `experiments/X-2501-canonical-robin-tree/results/verification.json`

Verified:

1. The support bound, exact child range, traversal completeness, tail ceiling, terminal-stream semantics, and all-integer three-case theorem are correct.
2. The verifier reconstructs the deterministic forest, rejects missing/extra tokens, recomputes exact leaf arithmetic and every prune, and uses outward dyadic transcendental enclosures.
3. The retained result certifies the complete stated canonical region through `10^54`; it explicitly labels the all-integer consequence as dependent on `T-2001/T-2002` and finite only.

Required pre-public boundary:

The search and verifier share the same dyadic kernel, and the huge terminal stream was not rerun in this review. The artifact's own status `CERTIFIED_FINITE_REGION_PENDING_INDEPENDENT_VERIFICATION` should remain. This review verifies the theorem and checker semantics, not a second computational reproduction of all 37,476 internal nodes.

Merge order: `#19 -> #24 -> #34`; #40 may follow.

### PR #37 — **VERIFIED WITH FIXES**

Load-bearing files:

- `claims/definitions/D-0801-piecewise-autocorrelation-carrier.md`
- `claims/lemmas/L-0801-piecewise-prime-toeplitz.md`
- `experiments/X-0801-piecewise-carrier-tail/stream.py`
- `experiments/X-0801-piecewise-carrier-tail/merge.py`

Verified:

- The autocorrelation Fourier construction, hat-cell overlap matrix, and Toeplitz prime deposition are correct conditional on the common explicit-formula normalization.
- The segmented stream covers declared integer intervals, includes every higher prime power exactly once when configured, and the merger rejects gaps, overlaps, or duplicate/missing higher-power streams.

Required fixes/boundaries:

- The piecewise source gives only the stated `O(1/r^2)` real-axis decay; exact Guinand--Weil admissibility and horizontal-strip hypotheses are still a declared open gate.
- The code uses `longdouble/float64` phases and eigenvalues and correctly marks all output empirical.
- The full pole/archimedean matrix and directed frozen-vector replay are absent.
- It inherits #4 and #27.

Merge order: repaired #4, then #27, then #37.

### PR #38 — **VERIFIED WITH FIXES**

Load-bearing files:

- `claims/definitions/D-3201-xi-positive-real-kernel.md`
- `claims/lemmas/L-3201-xi-logderivative-point-witness.md`
- `claims/lemmas/L-3202-xi-pick-matrix-witness.md`
- `claims/lemmas/L-3203-ca-support-line-interval-cover.md`
- `claims/theorems/T-3201-robin-ca-completeness.md`

Verified against Lagarias's primary paper and correction:

1. The completed-xi logarithmic derivative, functional-equation sign, and corrected `+1/(s-1)` evaluator are correct.
2. Under RH, `Re(xi'/xi)>0` in `Re s>1/2`; a right-half-plane zero creates an open negative region on its left. `L-3201` is existentially complete as a finite disproof architecture.
3. The shifted positive-real/Pick matrix has the exact zero-resolvent Gram representation under RH; a directed negative fixed-vector quadratic form is a valid counterexample.
4. The CA support-line/concavity interval lemma is correct.

Required source/status fix:

`T-3201` correctly labels the infinite colossally-abundant completeness import `PARTIAL`, because Robin's original Proposition 1 was not directly inspected. It must remain partial until the original statement, quantifiers, and threshold are audited. The finite `L-3203` interval theorem is independent and verified. The floating prototype is synthetic/calibrational only.

Merge order: the xi-positive-real part is independent; the CA portion should follow the Robin source audit. PR #43 stacks on the xi portion.

### PR #40 — **VERIFIED**

Load-bearing files:

- `claims/lemmas/L-3501-canonical-tail-level-encoding.md`
- `claims/lemmas/L-3502-exact-powered-lagrange-tail-envelope.md`
- `experiments/X-3501-powered-robin-envelope/verify.py`

Findings:

- The nested prefix-level encoding is a bijection and the integer/abundancy factorizations and cap equivalence are exact.
- The powered Lagrange dynamic program correctly enforces nesting and converts the shared product budget into a rational upper bound.
- The verifier reconstructs consecutive primes, caps, every rational candidate maximum, and the final powered inequality; it does not trust an optimizer trace or floating root.
- The committed artifact is a synthetic strict-improvement regression, not an extension of the certified Robin range.

Merge order: after #34. Integrating this DP as a stronger #34 prune is a separate proposed enhancement.

### PR #43 — **VERIFIED**

Load-bearing files:

- `claims/lemmas/L-4101-xi-right-side-differential-witness.md`
- `claims/lemmas/L-4102-xi-shifted-stieltjes-moment-hierarchy.md`
- `claims/lemmas/L-4103-low-order-xi-stieltjes-inequalities.md`

Findings:

1. The first differential localizer
   `Re F'(s)+Re F(s)/x` is nonnegative under RH and becomes negative immediately to the right of any right-half-plane zero orbit while `Re F` remains positive.
2. The shifted Stieltjes representation, Hankel and localizing matrices, and the exact finite-jet conversion are correct. An independent symbolic recurrence matched the displayed coefficient formula through order five.
3. The low-order signs, Hankel determinant, localizing scalar, and localizing determinant have the correct factors and signs.
4. Every conclusion is one-way: an actual directed negative xi-jet form disproves RH; finite positive synthetic or numerical tests do not support RH.

The synthetic code is appropriate for algebra regression but no directed actual-xi jet artifact exists. Merge after the xi portion of #38.

## Integration and merge-order summary

1. **Robin chain:** `#19 -> #24 -> #34 -> #40`. The CA interval lemma in #38 and selected #33 lemmas may be integrated afterward, claim by claim.
2. **Literature/Li chain:** `#21 -> #22`; #33's Li and Nicolas lemmas depend on #21.
3. **Xi positive-real chain:** `#38 -> #43`.
4. **Weil/carrier chain:** first close #4's D-0001 dictionary/admissibility audit; then #23, #27, and #30 may be integrated; #37 follows #27.
5. **Mixed PR #33:** retain route-specific dependencies or split before merge. Its verified arithmetic lemmas do not repair the carrier normalization.

## Computational review boundary

- Exact arithmetic/checker semantics were inspected for #4, #19, #22, #24, #34, #37, and #40.
- No expensive scan, 10^54 tree traversal, high-carrier FFT, or large prime stream was rerun.
- A checker that propagates supplied intervals is not an independent analytic producer. This distinction is load-bearing in #4 and #22.
- Floating reconnaissance is consistently non-certifying in the frozen PRs and was not used to assign any VERIFIED status.

## Missed connections

New cross-PR connections are recorded separately as `O-9503` with status **PROPOSED**. They do not alter any classification above.

## SERIOUS RESOLUTION PATH

**NOT YET PRESENT in this frozen PR set.**

The set contains several serious and logically complete *counterexample-certificate architectures*:

- one strict negative cutoff-free Weil direction;
- one negative `xi'/xi` point or Pick matrix;
- one negative xi differential/Stieltjes form;
- one Robin or Nicolas integer violation.

None currently contains an actual directed counterexample, and finite positive computations cannot prove RH.

Exact missing steps for a full resolution are:

1. **Weil/carrier disproof route:** independently close D-0001's exact dictionary, admissibility, and autocorrelation identity, then produce a strict directed negative actual matrix/vector. Absent a negative, proving global positivity is itself the Weil criterion and is not supplied here.
2. **Xi response route:** produce a strict directed negative actual `xi` value, Pick quadratic form, or differential/Stieltjes form. Exhausting finitely many points or jets cannot prove RH.
3. **Robin/Nicolas proof route:** replace finite range extension by an all-integer theorem or a genuinely terminating global reduction. The certified `10^54` range, CA contacts, and powered tail pruning remain finite.

Accordingly, the assigned PRs are suitable for pre-public release after the listed corrections and dependency labels, but they do not constitute a proposed proof or disproof of RH.
