# Carry critical hinge

## Integrated scope

**Strongest reviewed result:** Finite factor-64 payment, response representation, convexity no-go.

**First open arrow:** Square-root weighted signed response cancellation.

**Relationship to RH:** open nodes: OPEN.ARITH.CARRY_WEIGHTED_RESPONSE

**Family state:** `live`

This packet contains 3 reconciled semantic claim rows. It is a reviewed residency manifest. Exact proof bodies remain at the frozen source PR/head/path recorded in `SOURCE_MANIFEST.tsv`.

## Claims

| Claim | Verdict | Statement | Scope | Required fix | Exact source |
|---|---|---|---|---|---|
| `ARITH.CARRY.FACTOR64_PAYMENT` | `VERIFIED_WITH_FIXES` | Factor-64 reward prefixes pay every monotone occupation; the actual critical occupation is not monotone. | finite factor-64 occupation prefixes | Separate the finite monotone-payment theorem from the nonmonotone critical occupation. | PR #381 `8b32a5941a34` `claims/lemmas/L-90701-factor64-reward-prefixes-pay-every-monotone-occupation.md\|claims/refutations/R-90702-critical-uniform-pascal-occupation-is-not-monotone.md` |
| `OPEN.ARITH.CARRY_WEIGHTED_RESPONSE` | `OPEN_SUFFICIENT_FOR_RH` | Square-root weighted cancellation of the signed linear-hinge response would close the surviving critical-hinge route. | critical weighted response on all scales | None | PR #382 `d5630815f685` `claims/lemmas/L-90705-square-root-hinge-is-a-positive-mixture-of-signed-linear-hinge-responses.md` |
| `REFUTATION.CARRY.SOURCE_BLIND_CONVEXITY` | `REFUTED_MECHANISM` | Naive recursive residual monotonicity and generic average-carry convexity fail. | claimed source-blind monotonicity/convexity classes | None | PR #382 `d5630815f685` `claims/refutations/R-90701-naive-recursive-residual-monotonicity-fails.md\|claims/refutations/R-90704-average-carry-inverse-does-not-preserve-the-full-convex-cone.md\|claims/refutations/R-90705-truncated-geometric-atoms-do-not-have-positive-average-carry-inverses.md` |

## Reading rule

- `VERIFIED_WITH_FIXES` may be used only with the listed repair.
- `CONDITIONAL_EXACT` does not establish its premises.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` remain open.
- Refutations and false edges are retained as mechanism firewalls.
- Family membership never confers a stronger verdict than the claim row.

Canonical registry: `canonical/2026-08-22/claims.tsv` at repository root.
