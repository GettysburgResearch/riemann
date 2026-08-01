# Pre-publication review — PRs #64, #65, #67–#74, #76–#79

Reviewer: `gpt56-pro-09-i`  
Date: 2026-08-01  
Scope: frozen-head review only; no expensive computation rerun; no merge action.

## Frozen heads

| PR | Frozen head SHA |
|---:|---|
| #64 | `38d51cc5d95254d98596c83628cd8f859c5464f7` |
| #65 | `7296bf55449a4b510e4823028744deb793516e14` |
| #67 | `8f3cce40048c84f1bfd19e815491790a13e4247b` |
| #68 | `7b0942a83eede8b57d4f28b14a78d80edc295f2a` |
| #69 | `bd05e798cf365a55f5dcd0769e2ed433396184f3` |
| #70 | `c1f4d3aa35e0394a2de3dccf00bd57f40352af94` |
| #71 | `82934cf24ed575e9e554ba4e6c912a447aa1dd4e` |
| #72 | `b8b7b902bd92b4ce648543b0df82fa33913a42cc` |
| #73 | `a90f4c45c7f58f900e9f20bd310258047e7c545b` |
| #74 | `06436abe72cd11dd9ea8b56cdc9c8ffa2186f919` |
| #76 | `464f38d7db8feec7009578522cd0d10f577c7d4c` |
| #77 | `ae4af902ad250cd5f8ba9d5cb02e26987bdfac9c` |
| #78 | `70a94a768708db068abe484fb8c4f6d52d4c4828` |
| #79 | `9a2778f235ca1236768a2fc27b439efd95eb4a13` |

Status meanings:

- **VERIFIED** — every material claim checked at the frozen head is correct within its stated scope.
- **VERIFIED WITH FIXES** — the core mathematical result survives, but named corrections are required before integration.
- **GAP/BLOCKED** — the frozen PR does not establish its advertised production/result objective, or lacks its decisive artifact.
- **REJECTED** — a material theorem or claimed result is false. No assigned PR reached this class.

## Executive classification

| PR | Classification | Scope of verdict |
|---:|---|---|
| #64 | **GAP/BLOCKED** | Sound fallback design, but frozen objective incomplete; superseded by #65. |
| #65 | **VERIFIED** | Exact finite positive fixed-vector certificate under the declared D-0801/T-2801 form. |
| #67 | **VERIFIED WITH FIXES** | Exact obstruction for the declared real/value-only cone; checker hardening and terminology needed. |
| #68 | **VERIFIED** | Complete complex 8×8 Pick-box positive-definiteness certificate at the stated ordinate. |
| #69 | **GAP/BLOCKED** | Trigger-only PR; associated production run failed and no result artifact is in the frozen commit. |
| #70 | **VERIFIED WITH FIXES** | Cross-height matched-pole algebra and retained finite replays pass; publication/scope fixes required. |
| #71 | **VERIFIED** | Complete complex Pick-box closure at a distinct frozen point set; finite only. |
| #72 | **GAP/BLOCKED** | Trigger-only PR; all four associated workflows failed before a usable artifact. |
| #73 | **VERIFIED WITH FIXES** | L-2813/L-2814 and exact remainder moat pass; stale base/status must be repaired. |
| #74 | **GAP/BLOCKED** | Trigger-only PR; run remains queued and is superseded by #65. |
| #76 | **VERIFIED WITH FIXES** | Direct-xi modulus hierarchy is sound; one node-order error and missing prior-art citations. |
| #77 | **GAP/BLOCKED** | Trigger-only PR; no workflow run or result at the frozen head. |
| #78 | **GAP/BLOCKED** | Trigger-only PR; no workflow run or result at the frozen head. |
| #79 | **VERIFIED WITH FIXES** | Toeplitz fixed-vector/Gram/whole-box algebra passes; IDs and artifact binding are not merge-safe. |

## Individual reviews

### PR #64 — GAP/BLOCKED

Reviewed principally:

- `claims/definitions/D-0801-piecewise-autocorrelation-carrier.md`
- `claims/lemmas/L-0801-piecewise-prime-toeplitz.md`
- inherited `claims/theorems/T-2801-d0801-guinand-weil-dictionary.md`
- `claims/lemmas/L-0901-uniform-arch-pole-correction-bound.md`
- `experiments/X-2813-target-directed-toeplitz/directed_toeplitz_shard.c`
- `experiments/X-4202-directed-carrier-finalist/one_pass_finalize.py`

Findings:

1. The Schwarz-product Fourier transform, autocorrelation support, off-diagonal factor `1/2`, prime sign, pole sign, zero coordinate, and `2π` conventions are consistent. T-2801's admissibility argument is sufficient for the piecewise-linear Fourier transform after accepting the classical Guinand–Weil formula.
2. The directed coefficient producer's `log p/(π sqrt(q))` normalization is correct for the lag coefficient whose matrix off-diagonal is half that value. The interval phase widening and segmented prime/higher-power enumeration are conservative.
3. Binary64 hexadecimal export widens the MPFR lag intervals but remains outward and valid.
4. The frozen PR explicitly contains no complete coverage artifact or final sign. Its title/objective is therefore not established at this commit.

Disposition: do not merge as a completed experiment. Preserve/cherry-pick the resumable pipeline only if useful; otherwise close as superseded by #65.

Citation audit: Bombieri (2000) is relevant prior art. Akiva Groskin, arXiv:2607.02828, exists and is relevant to the finite Guinand–Weil dictionary; T-2801 should still cite the exact theorem/normalization rather than only a general paper pointer.

### PR #65 — VERIFIED

Reviewed principally:

- `claims/theorems/T-2801-d0801-guinand-weil-dictionary.md`
- `claims/lemmas/L-2804-sharded-fixed-vector-composition.md`
- `claims/lemmas/L-2806-directed-fixed-vector-prime-enclosure.md`
- `claims/lemmas/L-2807-segmented-prime-power-completeness.md`
- `experiments/X-2805-directed-prime-producer/directed_prime_shard.cpp`
- `experiments/X-2801-piecewise-carrier-corrections/verify_fixed_vector_certificate.py`
- `.../target-c1e11/final/complete-result.json`
- `.../target-c1e11/final/verdict-dual-p192-p256.json`

Findings:

1. The producer includes every ordinary prime exactly once, every higher prime power exactly once, uses directed log/square-root/phase/interpolation arithmetic, and fails on ambiguous support cells.
2. The exact checker enforces contiguous coverage, one higher-power stream, parameter/vector fingerprints, exact alpha/norm/prime composition, and the normalized correction radius.
3. The counts `4,118,054,813 + 28,156 = 4,118,082,969` are internally consistent.
4. The final interval is strictly positive. This rigorously excludes the frozen vector and nothing more.
5. Dual precision is not a second implementation, but independent reproduction is not logically needed to retain a positive finite exclusion after source audit. It would be mandatory before promoting a future negative.

Disposition: merge after its correction/theorem base (#49). Retain the exact statement `CERTIFIED_POSITIVE_FIXED_VECTOR`; never summarize it as evidence for RH or matrix positivity.

### PR #67 — VERIFIED WITH FIXES

Reviewed principally:

- `claims/lemmas/L-6601-feasible-anchor-obstructs-dual-witness.md`
- inherited `claims/lemmas/L-3903-exact-contraction-of-xi-value-balls.md`
- `experiments/X-6601-arb-xi-dual-portfolio/analyze_feature_cone.py`
- `.../results/feature-cone-closure.json`
- parent Arb completed-xi producer.

Verified core:

- A feasible point in the primitive uncertainty box and every declared convex cone blocks every robust negative conic separator over that exact library.
- The 65 rational midpoint anchors are valid for the real/value-only rows actually constructed.
- Scalar, A/B, alternating divided-difference, real same-height Pick, and disjoint cross-Loewner checks are finite rational calculations.

Required fixes:

1. Replace “full Pick matrix/cone” by **real same-height Pick restriction** wherever the analysis uses only `Re F`. Complex directions require the imaginary rectangles and are handled by #68/#71, not #67.
2. Harden `parse_int`: it currently applies `int(value)` after rejecting booleans and can silently coerce a nonintegral JSON float. Require an actual integer or decimal-integer string.
3. Fail closed on the input schema, duplicate point IDs, positive denominator gates, and expected certificate classification inside `analyze_feature_cone.py`, rather than relying only on an upstream artifact.
4. Keep the conclusion exactly finite: no separator over the declared value-only library, not no xi counterexample at that height.

The immutable committed result remains valid because its inputs are integer strings from the reviewed producer; these fixes concern publication-grade fail-closed reuse.

### PR #68 — VERIFIED

Reviewed principally:

- `experiments/X-6602-barycentric-nearzero/verify_pick_box_pd.py`
- `.../pick-j1-192-positive-definite.json`
- `.../pick-j1-192-positive-definite.verification.json`

Findings:

- The checker reconstructs the genuine complex Hermitian matrix
  `(F_i + conjugate(F_j))/(x_i+x_j)` at one exact height.
- The Gaussian-rational unpivoted `LDL*` proof of `M-δI>0` is exact.
- The rectangle-to-entry radius and Hermitian maximum-row-sum operator bound are conservative.
- The final lower eigenvalue moat is strictly positive, so every admitted complex direction is excluded on this exact 8-point set.

Disposition: merge after #67 and its primitive-value base. Scope remains one finite matrix box.

### PR #69 — GAP/BLOCKED

Only `.github/C1E11_DIRECTED_TRIGGER.md` changes. Workflow run `30169169981` completed with failure across the attempted shard jobs and produced no frozen final result. #65 later supplies the actual completed certificate.

Disposition: close as superseded; do not merge a trigger-only commit as a scientific result.

### PR #70 — VERIFIED WITH FIXES

Reviewed principally:

- `claims/lemmas/L-3905-cross-height-matched-pole-packets.md`
- `experiments/X-3904-cross-height-pick/cross_height.py`
- exact candidate/checker code
- `binary64-ghost-replay.json`
- `grid-nominee-128-replay.json`

Verified core:

- The arbitrary-height contraction `c* K c = 2 Re sum a_j F(s_j)` is correct.
- The Gaussian-rational barycentric vector has the claimed moment cancellations.
- The modeled same-ordinate reflected pair contracts to `-2md`, and the two-parameter mismatch formula is correct.
- The distant-line-zero suppression follows from the cancelled Laurent expansion.
- The binary64 negative is rigorously refuted; the 128-bit grid nominee correctly remains zero-touching/unresolved.

Required fixes:

1. Repair the malformed `\frac` token in the pair-matrix proof.
2. State explicitly that equation (9) is the contribution of the same-ordinate reflected pair, with the conjugate half supplied through the Hermitian Pick numerator; this prevents readers from confusing it with a two-zero truncation of the full zeta orbit.
3. Keep the result classification as method + refutation + unresolved nominee. The failed production trigger is #72, not evidence about this theorem.

### PR #71 — VERIFIED

Reviewed principally:

- `claims/lemmas/L-7101-rational-midpoint-radius-pick-pd.md`
- `experiments/X-3904-complex-pick-recheck/verify_complex_pick.py`
- `.../frozen-candidate-full-matrix-summary.json`
- `.../jm15-independent-precision-ladder.json`

Findings:

- The complete 512-bit complex matrix box at the frozen point set is rigorously positive definite by exact `LDL*` plus an operator-radius moat.
- The former one-vector positive result is strengthened to all complex directions on that set.
- The independent Riemann–Siegel ladder is only ordinary high precision and is correctly not used as the proof.
- This point set is distinct from #68; the two certificates are complementary, not duplicates.

Disposition: merge after the common primitive producer (#56 stack). No RH/global conclusion.

### PR #72 — GAP/BLOCKED

Only `PRODUCTION_REQUEST.md` changes. At the frozen head, all four associated workflows completed with failure (`30169264447`, `30169264438`, `30169264421`, `30169264431`) and no proof artifact was retained.

Disposition: do not merge as a result. Keep #70; close #72 or replace it with a result-bearing PR.

### PR #73 — VERIFIED WITH FIXES

Reviewed principally:

- `claims/lemmas/L-2813-rigorous-phase-grid-compression.md`
- `claims/lemmas/L-2814-single-pass-selective-precision-escalation.md`
- `experiments/X-2814-rigorous-phase-grid/verify_target_remainder.py`
- `.../results/target-remainder-output.json`

Verified core:

- The Taylor remainder `W exp(η) η^(R+1)/(R+1)!` is correct.
- The exact target specialization with `M=32768`, `R=3` proves `<1/21,816,000,000<1/20,000,000,000`.
- One complete outward pass is already a proof; selective higher-precision intersections are valid.

Required fixes:

1. Rebase onto the final #65 head. The frozen base SHA predates #65's completed positive certificate.
2. Update the stale PR body/proof boundary saying the #65 directed pass is pending.
3. Keep `X-2814` described as a remainder checker; no proof-producing phase-grid moment backend is present.

### PR #74 — GAP/BLOCKED

Only `RUN_FIXED_VECTOR_TARGET.md` changes. The associated single-host run `30169591643` is still queued at review time, while #65 already completed the target through another route.

Disposition: close as superseded unless the run is retained explicitly as independent reproduction.

### PR #76 — VERIFIED WITH FIXES

Reviewed principally:

- `claims/lemmas/L-7501-xi-modulus-absolute-monotonicity.md`
- `claims/lemmas/L-7502-xi-modulus-log-bernstein-hierarchy.md`
- `claims/lemmas/L-7503-odd-log-divided-difference-localizers.md`
- `verify_modulus_certificate.py`
- `verify_log_localizer.py`

Verified core:

- The even entire descent `F_T(z)=H_T(z^2)`, order halving, genus-zero product under RH, nonpositive zero set, and absolute monotonicity are correct.
- `G_T'=d(log H_T)/du` is completely monotone under RH.
- The two-point modulus reversal is existentially complete against false RH.
- Integer-power concavity and odd logarithmic divided-difference certificates are algebraically sound.
- The interval square/modulus and exact product checkers fail closed correctly.

Required fixes:

1. In L-7503, `r_0<...<r_n` together with `u_i=d-epsilon r_i` produces decreasing, not increasing, nodes. Reverse the `r` ordering or reindex the `u_i`. Divided differences are symmetric, so the theorem survives, but the statement/proof must agree with the checker.
2. Add prior-art positioning for the two-point horizontal modulus monotonicity: Sondow–Dumitrescu, arXiv:1005.1104, and Matiyasevich–Saidak–Zvengrowski, arXiv:1205.2773. The stronger squared-distance absolute-monotonicity hierarchy can still be presented as the new contribution.
3. Reserve the existing `L-7501`/`X-7501` IDs for this earlier PR; #79 must be renumbered.

### PR #77 — GAP/BLOCKED

Only `RUN_MODULUS_SCAN.md` changes. No workflow run or immutable production result is associated with the frozen head.

Disposition: close trigger-only PR; retain #76 as the theorem/method contribution.

### PR #78 — GAP/BLOCKED

Only `RUN_CROSS_PICK` changes. No workflow run or immutable result is associated with the frozen head.

Disposition: close trigger-only PR; any future scan should be a result-bearing child of #70 with frozen vectors and exact interval output.

### PR #79 — VERIFIED WITH FIXES

Reviewed principally:

- `claims/lemmas/L-7501-toeplitz-box-gram-spectral-closure.md`
- `experiments/X-7501-toeplitz-box-spectral-closure/verify_toeplitz_box.py`
- `from_target_artifacts.py`
- synthetic certificate/tests

Verified core:

- Fixed-vector autocorrelation contraction has the correct orientation and off-diagonal normalization.
- For PSD `W`, `|tr(WC)|<=epsilon tr(W)` is correct.
- A strictly negative Gram-portfolio trace proves the matrix is not PSD even if each listed vector interval is unresolved.
- The whole-matrix midpoint/radius certificate is conservative and correct.
- Postselection after simultaneous lag-box production is rigorous.

Required fixes:

1. **Identifier collision:** this PR reuses `L-7501` and `X-7501`, already allocated by #76. Rename throughout (suggest `L-7901`/`X-7901`) before integration.
2. Rebase onto final #65 and then the repaired #73; the frozen base predates the completed target certificate.
3. `from_target_artifacts.py` records but does not verify cross-artifact consistency. Require equality of cutoff, carrier, cell count, normalization fingerprint, precision/coverage identity, and input SHA-256s; make `verify_toeplitz_box.py` validate those bindings. It must not be possible to combine lag boxes from one target with alpha/correction data from another.
4. No production lag-box artifact exists in this PR; retain the claims as exact interfaces plus synthetic regression, not a target closure.

## Integration / merge order

### Carrier stack

1. Review/merge the exact correction dictionary base (#49).
2. Merge **#65**. Treat **#64** as superseded pipeline history, not an additional result.
3. Rebase and repair **#73** onto #65.
4. Rename, bind, and rebase **#79** onto the repaired #73.
5. Close trigger-only **#69** and **#74** unless retained solely as independent-reproduction records.

### xi-log-derivative / direct-xi stack

1. Merge the common directed primitive producer (#56 stack) first.
2. Merge repaired **#67**, then **#68**.
3. **#71** may merge after the common producer independently of #68; it certifies a different point set.
4. Merge repaired **#70**; close failed trigger **#72**.
5. Merge repaired **#76**; close trigger **#77**.
6. Close trigger **#78**.
7. Resolve the #76/#79 claim-ID collision before either integration series reaches a shared base.

## Connections missed by the original PRs

1. **Direct-modulus / log-derivative bridge.** For `u=x^2`,
   `G_T(u)=log |xi(1/2+x+iT)|^2` satisfies
   `G_T'(u)=Re(xi'/xi)(1/2+x+iT)/x`.
   Thus #67's scalar/A/divided-difference hierarchy is the differential shadow of #76's direct-modulus hierarchy. This is pushed separately as **PROPOSED** and is not used to retroactively promote either PR.
2. **Real versus complex closure.** #67 closes a real/value-only cone. #68 and #71 are the genuine complex Hermitian lifts because they use the imaginary primitive rectangles. Their roles should be documented explicitly to prevent “full Pick cone” overstatement.
3. **One expensive carrier stream, many exact consumers.** #65 supplies a fixed-vector scalar result; #73 supplies an independent compression moat; #79 supplies reusable postselection/Gram logic. They become one coherent stack only after rebasing and fail-closed artifact binding.

## SERIOUS RESOLUTION PATH

**No presently complete path to a proof or disproof of RH is contained in these fourteen frozen PRs.**

There is, however, a serious and mathematically sound **finite disproof interface**:

- #76 proves that false RH creates an open two-point direct-xi modulus reversal at exact dyadic points.
- #70 and the Pick stack give additional finite negative interfaces.
- #65/T-2801 give a finite Weil negative interface.

Exact missing steps for an unconditional disproof are:

1. produce one strict directed negative interval for the actual Riemann `xi` or exact D-0801 form;
2. freeze the exact points/vector before precision escalation;
3. reproduce the primitive special-function or prime arithmetic with an independently structured directed backend;
4. retain the normalization/admissibility proof and exact artifact bindings.

What is absent is an effective a priori search bound guaranteeing where such a witness lies if RH is false. Passing finite grids cannot prove RH. A proof of RH would require a genuinely global/cofinal positivity theorem, not another finite positive matrix or fixed-vector result.
