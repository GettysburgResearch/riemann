# Suzuki/Hardy

## Integrated scope

**Strongest reviewed result:** Amplitude embedding and conditional first-chaos API.

**First open arrow:** Coefficient-one fully polarized domination.

**Relationship to RH:** open nodes: OPEN.OPERATOR.SUZUKI_FIRST_CHAOS_DOMINATION

**Family state:** `live`

This packet contains 4 reconciled semantic claim rows. It is a reviewed residency manifest. Exact proof bodies remain at the frozen source PR/head/path recorded in `SOURCE_MANIFEST.tsv`.

## Claims

| Claim | Verdict | Statement | Scope | Required fix | Exact source |
|---|---|---|---|---|---|
| `OPERATOR.SUZUKI.AMPLITUDE_EMBEDDING` | `VERIFIED_WITH_FIXES` | Suzuki's completed Jordan-Hankel operator gives the explicit amplitude-level scattering isometry. | published safe range and corrected normalization | Pin the primary source and distinguish amplitude isometry from curvature sign. | PR #400 `7dc9fec9eb5f` `claims/lemmas/L-91035-suzuki-hankel-is-the-explicit-completed-jordan-scattering-isometry.md` |
| `API.SUZUKI.FOCK_FIRST_CHAOS` | `CONDITIONAL_EXACT` | A source-linear positive Poisson colligation reduces to first chaos under all-intensity naturality and orthogonal product-system grading. | all r>=0 intensity family with exact K_r=rK_1 and chaos grading | State all-intensity naturality, orthogonal/Wiener-Itô grading, and exact source-linearity; do not apply to an arbitrary r=1 factorization. | PR #400 `7dc9fec9eb5f` `claims/lemmas/L-91036-any-source-linear-poisson-colligation-reduces-to-first-chaos.md` |
| `OPEN.OPERATOR.SUZUKI_FIRST_CHAOS_DOMINATION` | `OPEN_RH_EQUIVALENT` | The complete positive source-side first chaos dominates the fully polarized coefficient-one output tangent, preserving all delay/orientation/bridge terms. | all corrected delayed form-core directions | None | PR #400 `7dc9fec9eb5f` `claims/theorems/T-91008-corrected-delayed-first-chaos-tangent-intertwiner.md` |
| `OPERATOR.PRIME_JULIA_ABSORPTION` | `VERIFIED_WITH_FIXES` | The local prime Julia reserve absorbs the fixed-scale long-jump channel with corrected margin 21587/38416. | declared fixed scale | Correct the printed rational margin and preserve source normalization. | PR #408 `ea3948ea21d9` `claims/theorems/T-91501-prime-julia-reserve-absorbs-the-fixed-scale-oscillatory-long-jump-channel.md` |

## Reading rule

- `VERIFIED_WITH_FIXES` may be used only with the listed repair.
- `CONDITIONAL_EXACT` does not establish its premises.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` remain open.
- Refutations and false edges are retained as mechanism firewalls.
- Family membership never confers a stronger verdict than the claim row.

Canonical registry: `canonical/2026-08-22/claims.tsv` at repository root.
