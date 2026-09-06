# Actual-Xi Pick and Loewner

> **Current interpretation:** use the [current xi statements](../CURRENT_RESULTS.md#xi). The earlier safe-axis paper theorem retains its source hypotheses and repairs; the all-positive-node replacement is conditional on a complete, multiplicity-correct entire source. Neither is a completed repaired Lean implementation: see [formal status](../../../FORMAL_STATUS.md). At the Birman–Schwinger threshold use **point spectrum**, with the additional assumptions needed for a statement about spectrum alone; see [R2](../../../reviews/D/REPAIRS.md).

The following manifest and status cells are retained historical source records. In particular, `None` in an old repair column does not waive a later correction.

## Integrated scope

**Strongest reviewed result:** Actual-Xi PSD through order three with mandatory fixes.

**First open arrow:** Order four and all higher packet sizes.

**Relationship to RH:** open nodes: OPEN.OPERATOR.XI.PICK_ORDER4_PLUS

**Family state:** `live`

This packet contains 13 reconciled semantic claim rows. It is a reviewed residency manifest. Exact proof bodies remain at the frozen source PR/head/path recorded in `SOURCE_MANIFEST.tsv`.

## Claims

| Claim | Verdict | Statement | Scope | Required fix | Exact source |
|---|---|---|---|---|---|
| `OPERATOR.BIRMAN_SCHWINGER.NORMAL_FORM` | `VERIFIED` | Negative index of H=A-G*G equals Birman-Schwinger gains above one under the stated coercive hypotheses. | A>=cI with closed bounded coupling | None | PR #438 `bb7327d21c47` `claims/lemmas/L-91900-birman-schwinger-loop-detects-every-bound-state-and-negative-direction.md` |
| `OPERATOR.XI.PICK_ORDER2` | `VERIFIED_WITH_FIXES` | Every actual-Xi infinitesimal safe Pick packet of size at most two is positive. | all safe real nodes | State centered grouping, differentiated local convergence, multiplicity, and exact external input. | PR #438 `bb7327d21c47` `claims/lemmas/L-91905-every-two-node-infinitesimal-safe-xi-pick-matrix-is-unconditionally-positive.md` |
| `OPERATOR.XI.PICK_ORDER3.DETERMINANT` | `VERIFIED` | The 3x3 Caratheodory determinant factors into reciprocal-p and tp divided-difference curvatures. | three positive safe nodes | None | PR #445 `c079c2ef2102` `claims/lemmas/L-92000-three-node-caratheodory-determinant-factors-into-two-scalar-curvatures.md` |
| `OPERATOR.XI.PICK_ORDER3.TP_CURVATURE` | `VERIFIED_WITH_FIXES` | The companion tp curvature has the required nonpositive second divided-difference sign on the safe axis. | t>1/4; grouped actual-Xi zeros | State grouped convergence and multiplicity summation. | PR #445 `c079c2ef2102` `claims/lemmas/L-92001-the-tp-curvature-of-the-actual-xi-logarithmic-derivative-is-unconditionally-negative.md` |
| `OPERATOR.XI.RECIPROCAL_CONCAVITY.SUM` | `VERIFIED` | Positive reciprocal-concave C2 functions are closed under positive sums and locally C2-convergent positive series. | positive C2 functions | None | PR #446 `880d14cb4bcb` `claims/lemmas/L-92100-reciprocal-concavity-is-closed-under-positive-sums.md` |
| `OPERATOR.XI.RECIPROCAL_CONCAVITY.ONE_ORBIT` | `VERIFIED_WITH_FIXES` | One high off-line orbit is absorbed by an explicit O(m/b^2) fraction of one low critical orbit. | t>1/4; c>r; kappa<1 | State the representative and multiplicity convention and the c>r, kappa<1 hypotheses. | PR #446 `880d14cb4bcb` `claims/lemmas/L-92101-one-high-off-line-orbit-is-absorbed-by-a-small-critical-reserve-fraction.md` |
| `OPERATOR.XI.CRITICAL_RESERVE_BUDGET` | `VERIFIED_WITH_FIXES` | The complete hypothetical off-line curvature budget uses less than one coefficient unit of a fixed verified critical orbit. | all hypothetical off-line representatives above the verified height | Correct the Platt-Trudgian bibliographic/source lock; state N(T) bound and orbit counting; do not claim the external computation was rerun. | PR #446 `880d14cb4bcb` `claims/lemmas/L-92102-the-complete-hypothetical-off-line-curvature-budget-uses-less-than-one-critical-orbit.md` |
| `OPERATOR.XI.RECIPROCAL_CONCAVITY.ACTUAL` | `VERIFIED_WITH_FIXES` | The actual-Xi reciprocal Clark coordinate is concave on t>1/4 after grouped zero-orbit assembly. | t>1/4 | Retain the residual (m0-1)R0 if the selected critical orbit has multiplicity m0; state grouped C2 convergence. | PR #446 `880d14cb4bcb` `claims/lemmas/L-92103-the-actual-xi-reciprocal-clark-coordinate-is-concave-through-order-three.md` |
| `OPERATOR.XI.PICK_ORDER3` | `VERIFIED_WITH_FIXES` | Every actual-Xi infinitesimal safe Pick matrix of size at most three is positive semidefinite. | all safe real packets of size <=3 | Replace the corrupt historical replay; repair external lock; retain residual multiplicity; state PSD canonically and omit distinct-node positive-definite strictness unless separately proved. | PR #446 `880d14cb4bcb` `claims/theorems/T-92100-all-three-node-infinitesimal-safe-xi-pick-matrices-are-unconditionally-positive.md` |
| `OPEN.OPERATOR.XI.PICK_ORDER4_PLUS` | `OPEN_RH_EQUIVALENT` | Actual-Xi infinitesimal safe Pick positivity holds for every finite packet size from four upward. | all finite safe rational packets | None | PR #438 `bb7327d21c47` `claims/lemmas/L-91904-the-infinitesimal-safe-pick-kernel-is-a-countable-rh-criterion.md` |
| `OPERATOR.XI.LOEWNER_LOW_ORDER` | `VERIFIED_WITH_FIXES` | Pairwise squared-pole curvature identities and the reciprocal Loewner-Hankel congruence yield the stated low-order Xi monotonicity results. | safe real axis at exact stated orders | Pin exact downstream theorem paths and alias anchor domination to the same critical-reserve ledger as PR #446. | PR #708 `eb1987502ef9` `review/2026-08-21/operator/CLAIMS.tsv` |
| `OPERATOR.XI.FRACTIONAL_STRING_FIXED_ORDER` | `VERIFIED_WITH_FIXES` | For every prescribed fixed order, fractional-string scaling and beta-Hankel high-axis asymptotics hold away from the negative cut. | each fixed order; compact sectors away from cut | Pin the exact source filenames; state derivative uniformity and normalization. | PR #708 `eb1987502ef9` `review/2026-08-21/operator/CLAIMS.tsv` |
| `OPERATOR.XI.FRACTIONAL_STRING_GROWING_ORDER` | `GAP_BLOCKED` | The Xi impedance is eventually matrix monotone to a growing order. | joint order-height limit | Supply quantified moving-band Vandermonde and perturbation bounds uniform in order and height. | PR #461 `ea633d416609` `claims/lemmas/L-92302-the-xi-impedance-is-eventually-matrix-monotone-to-a-growing-order.md` |

## Reading rule

- `VERIFIED_WITH_FIXES` may be used only with the listed repair.
- `CONDITIONAL_EXACT` does not establish its premises.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` remain open.
- Refutations and false edges are retained as mechanism firewalls.
- Family membership never confers a stronger verdict than the claim row.

Canonical registry: `canonical/2026-08-22/claims.tsv` at repository root.
