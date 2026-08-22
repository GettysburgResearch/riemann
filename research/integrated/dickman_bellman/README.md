# Dickman/Stieltjes/Bellman

## Integrated scope

**Strongest reviewed result:** Mesoscopic hereditary corridor with locked classical inputs.

**First open arrow:** Dynamic critical finite block.

**Relationship to RH:** open nodes: none

**Family state:** `live`

This packet contains 3 reconciled semantic claim rows. It is a reviewed residency manifest. Exact proof bodies remain at the frozen source PR/head/path recorded in `SOURCE_MANIFEST.tsv`.

## Claims

| Claim | Verdict | Statement | Scope | Required fix | Exact source |
|---|---|---|---|---|---|
| `ARITH.DICKMAN.STIELTJES_TRANSFER` | `VERIFIED_WITH_FIXES` | The complete normalized base has an exact source-faithful Stieltjes transfer. | native rough state | State endpoint conventions and the external classical input separately. | PR #607 `a28f8e5b8c90` `claims/lemmas/L-98040-exact-stieltjes-transfer-of-the-complete-p61-base.md` |
| `ARITH.DICKMAN.MESOSCOPIC_BELLMAN` | `VERIFIED_WITH_FIXES` | The native rough state and its one-prime Bellman descendants are positive throughout the declared mesoscopic corridor on standard VK/de Bruijn input. | declared uniform mesoscopic corridor | Pin exact classical Vinogradov-Korobov/de Bruijn statements, ranges, and p^-1 normalization. | PR #608 `f362acf56bbb` `claims/theorems/T-98050-hereditary-mesoscopic-bellman-corridor.md` |
| `ARITH.DICKMAN.FIXED_EXPONENT_INTERVALS` | `CONDITIONAL_EXACT` | Every fixed-exponent prime interval and its compensated double-owner interval are eventually positive. | each fixed A>1; large prime endpoints | Prove joint uniformity in endpoint ratio, moving u, continuity points, tails, and positive margin. | PR #700 `18737409b6fa` `claims/lemmas/L-101220-truncated-dickman-limit-for-prime-interval-prefixes.md\|claims/lemmas/L-101221-all-fixed-exponent-double-owner-intervals-are-positive.md` |

## Reading rule

- `VERIFIED_WITH_FIXES` may be used only with the listed repair.
- `CONDITIONAL_EXACT` does not establish its premises.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` remain open.
- Refutations and false edges are retained as mechanism firewalls.
- Family membership never confers a stronger verdict than the claim row.

Canonical registry: `canonical/2026-08-22/claims.tsv` at repository root.
