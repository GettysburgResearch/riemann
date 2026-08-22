# Direct-main Mellin

## Integrated scope

**Strongest reviewed result:** Fixed-row transform and large-row noncancellation predecessor.

**First open arrow:** Simultaneous native all-row producer.

**Relationship to RH:** open nodes: OPEN.DIRECTMAIN.MELLIN.ALL_ROWS

**Family state:** `historical_support`

This packet contains 4 reconciled semantic claim rows. It is a reviewed residency manifest. Exact proof bodies remain at the frozen source PR/head/path recorded in `SOURCE_MANIFEST.tsv`.

## Claims

| Claim | Verdict | Statement | Scope | Required fix | Exact source |
|---|---|---|---|---|---|
| `DIRECTMAIN.MELLIN.L96000` | `VERIFIED_WITH_FIXES` | Every fixed component row has an explicit reciprocal-zeta Mellin transform. | fixed j>=2; initial half-plane then continuation | Separate convergence, continuation, and producer positivity. | PR #MAIN `677203992eb0` `claims/lemmas/L-96000-fixed-row-mellin-transform-of-the-full-mobius-spline.md` |
| `DIRECTMAIN.MELLIN.L96001` | `VERIFIED_WITH_FIXES` | At any open-strip zero every sufficiently large row numerator is nonzero. | each zero; all sufficiently large fixed rows | State the all-row producer quantifier; prefer fixed rows 2,3 or fixed 5:3 canonically. | PR #MAIN `677203992eb0` `claims/lemmas/L-96001-the-row-kernels-cannot-cancel-an-open-strip-zero.md` |
| `OPEN.DIRECTMAIN.MELLIN.ALL_ROWS` | `OPEN_SUFFICIENT_FOR_RH` | Simultaneous global native positivity of every prime-sieved component row is the open producer premise in T-96000. | all j>=2 and all X>=1 | Do not infer this from PR #537 FRONTIER-CHAIN. | PR #MAIN `677203992eb0` `claims/theorems/T-96000-prime-sieved-row-positivity-directly-implies-rh.md` |
| `DIRECTMAIN.MELLIN.T96000` | `GAP_BLOCKED` | T-96000 is a correct conditional architecture but not a proof because its simultaneous native row producer is absent. | all rows and scales | Extract L-96000/L-96001 only. | PR #MAIN `677203992eb0` `claims/theorems/T-96000-prime-sieved-row-positivity-directly-implies-rh.md` |

## Reading rule

- `VERIFIED_WITH_FIXES` may be used only with the listed repair.
- `CONDITIONAL_EXACT` does not establish its premises.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` remain open.
- Refutations and false edges are retained as mechanism firewalls.
- Family membership never confers a stronger verdict than the claim row.

Canonical registry: `canonical/2026-08-22/claims.tsv` at repository root.
