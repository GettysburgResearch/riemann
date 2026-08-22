# Historical native-source assets

## Integrated scope

**Strongest reviewed result:** Finite Farkas, Y4 repair/null gauge, live marginal, Volterra and conditional integration APIs.

**First open arrow:** Live source-owned feasibility/producer.

**Relationship to RH:** open nodes: none

**Family state:** `supporting`

This packet contains 7 reconciled semantic claim rows. It is a reviewed residency manifest. Exact proof bodies remain at the frozen source PR/head/path recorded in `SOURCE_MANIFEST.tsv`.

## Claims

| Claim | Verdict | Statement | Scope | Required fix | Exact source |
|---|---|---|---|---|---|
| `ARITH.CAUSAL_PACKET_BUDGET` | `VERIFIED_WITH_FIXES` | Constant-mode first-hazard weights give an exact nonduplicating causal packet identity with total recursive child mass below 1/8. | finite ordered-prime packet | Preserve literal physical packet typing; Hall does not commute automatically with the tree. | PR #439 `706445c01d4a` `claims/lemmas/L-91355-constant-mode-hazard-weights-give-a-nonduplicating-causal-packet-budget.md` |
| `ARITH.FINITE_FARKAS` | `VERIFIED_WITH_FIXES` | Atomwise root-ledger sufficiency and the finite rational primal/Farkas alternative. | finite/local declared scope | State that the theorem is a sufficiency/fail-closed finite alternative, not feasibility of the live allocation. | PR #454 `a0409d54250b` `claims/lemmas/L-91671-atomwise-provenance-partition-is-the-exact-native-root-ledger-certificate.md` |
| `ARITH.Y4_REPAIR_CONE` | `VERIFIED_WITH_FIXES` | The Y4-zero repair LP and triangular score-free transfer are exact response-space constructions. | finite/local declared scope | Preserve the response-space/source-ownership distinction and the possible new negative lower rows. | PR #470 `89af3206ea18` `claims/lemmas/L-91687-y4-zero-columns-are-score-free-triangular-repair-directions.md` |
| `ARITH.Y4_RADIAL_NULL_GAUGE` | `VERIFIED_WITH_FIXES` | A Y4-zero detail repair is invisible to the prime-radial dictionary. | finite/local declared scope | Keep dictionary invisibility separate from source-owned feasibility and model allocation. | PR #472 `bb364396e097` `claims/lemmas/L-19881-y4-zero-repair-is-a-null-gauge-for-the-prime-radial-dictionary.md` |
| `ARITH.LIVE_MARGINAL_FARKAS` | `VERIFIED_WITH_FIXES` | The actual live Target-Lorenz marginal is one joint finite primal/Farkas problem, with feasibility open. | finite/local declared scope | State explicitly that the theorem is an exact finite reduction and that feasibility is open. | PR #521 `b4a60a54b1d7` `claims/lemmas/L-94023-the-anchored-native-interface-is-one-exact-joint-primal-farkas-problem.md` |
| `ARITH.VOLTERRA_GREEN` | `VERIFIED_WITH_FIXES` | The factor-67 endpoint inverse has an exact distributional Green formula with both boundary modes and all activation-knot atoms. | finite/local declared scope | Retain both boundary modes and every activation-knot atom; smooth-cell density alone is incomplete. | PR #638 `73ee57ccc684` `claims/lemmas/L-99230-distributional-volterra-green-formula.md` |
| `ARITH.DIRECT_INTEGRAL_COMMON_ROW` | `CONDITIONAL_EXACT` | Given a valid positive endpoint measure and correctly typed packets, direct integration and finite cubature preserve one supplied common physical row and listed linear coordinates. | conditional local realization | Delete the unsupported literal-score=4sqrt(X) assignment and state the valid positive-measure/typed-packet hypotheses. | PR #620 `493e12fcba3f` `claims/lemmas/L-99022-direct-integration-and-exact-cubature.md` |

## Reading rule

- `VERIFIED_WITH_FIXES` may be used only with the listed repair.
- `CONDITIONAL_EXACT` does not establish its premises.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` remain open.
- Refutations and false edges are retained as mechanism firewalls.
- Family membership never confers a stronger verdict than the claim row.

Canonical registry: `canonical/2026-08-22/claims.tsv` at repository root.
