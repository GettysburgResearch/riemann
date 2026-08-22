# Direct-main critical Taylor

## Integrated scope

**Strongest reviewed result:** Supercritical and Taylor-remainder positivity; fixed critical consumer.

**First open arrow:** Critical negative mass/envelope.

**Relationship to RH:** open nodes: OPEN.DIRECTMAIN.TAYLOR_CRITICAL

**Family state:** `live`

This packet contains 6 reconciled semantic claim rows. It is a reviewed residency manifest. Exact proof bodies remain at the frozen source PR/head/path recorded in `SOURCE_MANIFEST.tsv`.

## Claims

| Claim | Verdict | Statement | Scope | Required fix | Exact source |
|---|---|---|---|---|---|
| `DIRECTMAIN.TAYLOR.L99930` | `VERIFIED_WITH_FIXES` | Activation-zero native powers are globally positive for every real m>=2. | X>=1; real m>=2 | Keep activation-zero and ordinary SHARP objects distinct. | PR #MAIN `677203992eb0` `claims/lemmas/L-99930-activation-zero-supercritical-positivity.md` |
| `DIRECTMAIN.TAYLOR.L99931` | `VERIFIED_WITH_FIXES` | Every Euler–Taylor remainder with effective prime exponent at least 3/2 is positive. | integer m>=3; 1<=k<=m-2 | State absolute convergence and labelled-67 multiplicity. | PR #MAIN `677203992eb0` `claims/lemmas/L-99931-euler-taylor-positive-remainder-ladder.md` |
| `DIRECTMAIN.TAYLOR.L99932_KERNEL` | `VERIFIED_WITH_FIXES` | The first uncontrolled Taylor remainder is an explicit positive kernel whose native Möbius projection has a zero-safe reciprocal-zeta Mellin transform. | one fixed m>=2 | Pin the reviewed Mellin–Landau hypotheses. | PR #MAIN `677203992eb0` `claims/lemmas/L-99932-critical-renormalized-kernel-and-zero-safe-consumer.md` |
| `OPEN.DIRECTMAIN.TAYLOR_CRITICAL` | `OPEN_RH_EQUIVALENT` | Subpower negative mass or the critical upper-envelope estimate for the fixed Taylor scalar is the remaining RH-equivalent theorem. | one fixed m>=2 over all large scales | Keep it explicit as an open premise. | PR #MAIN `677203992eb0` `claims/lemmas/L-99932-critical-renormalized-kernel-and-zero-safe-consumer.md` |
| `DIRECTMAIN.TAYLOR.R99930` | `REFUTED_MECHANISM` | Supercritical positivity and positive smoothing do not cross the critical carrier. | critical prime-harmonic boundary | None | PR #MAIN `677203992eb0` `claims/refutations/R-99930-supercritical-positivity-does-not-cross-the-critical-carrier.md` |
| `DIRECTMAIN.TAYLOR.T99930` | `CONDITIONAL_EXACT` | T-99930 validly synthesizes the supercritical ladder and fixed zero-safe critical consumer, while leaving the critical estimate open. | one fixed m>=2 | Split unconditional results from the open terminal estimate. | PR #MAIN `677203992eb0` `claims/theorems/T-99930-critical-taylor-renormalization-frontier.md` |

## Reading rule

- `VERIFIED_WITH_FIXES` may be used only with the listed repair.
- `CONDITIONAL_EXACT` does not establish its premises.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` remain open.
- Refutations and false edges are retained as mechanism firewalls.
- Family membership never confers a stronger verdict than the claim row.

Canonical registry: `canonical/2026-08-22/claims.tsv` at repository root.
