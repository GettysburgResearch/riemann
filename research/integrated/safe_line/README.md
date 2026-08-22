# Safe-line transforms

## Integrated scope

**Strongest reviewed result:** Hausdorff/Pick, radial, Catalan/VK and Green-removal local results.

**First open arrow:** Critical annular/radial sign.

**Relationship to RH:** open nodes: OPEN.OPERATOR.RADIAL_CURVATURE

**Family state:** `live`

This packet contains 4 reconciled semantic claim rows. It is a reviewed residency manifest. Exact proof bodies remain at the frozen source PR/head/path recorded in `SOURCE_MANIFEST.tsv`.

## Claims

| Claim | Verdict | Statement | Scope | Required fix | Exact source |
|---|---|---|---|---|---|
| `OPERATOR.SAFE_LINE.HAUSDORFF_PICK` | `VERIFIED_WITH_FIXES` | Safe-line normalized scalars have exact Hausdorff moment, square-root, and Stieltjes/Pick transforms; the complete positivity criterion remains RH-equivalent. | declared safe-line transform scope | Separate unconditional transforms from the RH-equivalent sign criterion. | PR #393 `ec118df8a133` `claims/lemmas/L-91001-safe-line-beta-finite-difference-kernels.md\|claims/lemmas/L-91002-safe-line-laguerre-euler-weights.md\|claims/lemmas/L-91003-safe-line-square-root-generating-transform.md\|claims/theorems/T-91001-single-safe-line-hausdorff-pick-rh-criterion.md` |
| `OPEN.OPERATOR.RADIAL_CURVATURE` | `OPEN_RH_EQUIVALENT` | Completed-Xi radial curvature is nonnegative for every center and 0<t<1/4. | all centers and 0<t<1/4 | None | PR #394 `82ee32348b05` `claims/theorems/T-91002-rh-is-radial-concavity-of-completed-xi-modulus.md` |
| `OPERATOR.CATALAN_VK_SAFE_DISC` | `CONDITIONAL_EXACT` | High-carrier safe-disc geometry converges to the Catalan/Stieltjes law, and VK input transports a limited positivity region. | high carrier and declared annulus | Pin exact external VK theorem and quantifiers. | PR #395 `7106b3b2e06b` `claims/lemmas/L-91008-high-carrier-safe-disc-is-catalan-stieltjes.md\|claims/lemmas/L-91009-log-derivative-control-transfers-to-annular-pick-positivity.md\|claims/theorems/T-91004-vinogradov-korobov-penetrates-the-pick-sign-annulus.md` |
| `OPERATOR.GREEN_REMOVAL_PORTS` | `VERIFIED_WITH_FIXES` | Finite Green orders, Green-removal density, terminal-scale positivity, and the crossed critical-port dictionary survive. | declared finite orders and small/large scales | Keep the crossed hyperbolic-port exclusion open/RH-equivalent and pin the corrected threshold artifact separately. | PR #396 `a7e140614a25` `claims/lemmas/L-91023-weighted-harris-fkg-all-green-jordan-hierarchy.md\|claims/lemmas/L-91026-green-removal-is-one-explicit-boundary-density.md\|claims/lemmas/L-91027-green-removal-is-unconditionally-positive-at-terminal-scales.md\|claims/lemmas/L-91028-green-removal-is-positive-at-all-sufficiently-small-scales.md\|claims/lemmas/L-91033-horizontal-contour-crossing-selects-exactly-zeros-deeper-than-the-cauchy-scale.md\|claims/lemmas/L-91034-krein-langer-cauchy-source-critical-port-decomposition.md` |

## Reading rule

- `VERIFIED_WITH_FIXES` may be used only with the listed repair.
- `CONDITIONAL_EXACT` does not establish its premises.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` remain open.
- Refutations and false edges are retained as mechanism firewalls.
- Family membership never confers a stronger verdict than the claim row.

Canonical registry: `canonical/2026-08-22/claims.tsv` at repository root.
