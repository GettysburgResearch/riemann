# Mellin–Landau consumers

## Integrated scope

**Strongest reviewed result:** Fixed rows 2,3; fixed 5:3; zero-safe smoothing and negative-mass API.

**First open arrow:** Literal fixed source-faithful sign or negative mass.

**Relationship to RH:** open nodes: OPEN.ARITH.ROWS23_NATIVE, OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS, OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS

**Family state:** `live`

This packet contains 12 reconciled semantic claim rows. It is a reviewed residency manifest. Exact proof bodies remain at the frozen source PR/head/path recorded in `SOURCE_MANIFEST.tsv`.

## Claims

| Claim | Verdict | Statement | Scope | Required fix | Exact source |
|---|---|---|---|---|---|
| `CONSUMER.MELLIN.FIXED_ROW` | `VERIFIED_WITH_FIXES` | A fixed row has a reciprocal-zeta Mellin transform after separating initial convergence from continuation. | fixed row; initially convergent half-plane then meromorphic continuation | State z=s+1/2, finite abscissa, positive-real removability, and multiplicity. | PR #652 `24ab64551225` `claims/lemmas/L-99602-exact-two-row-mellin-landau-consumer.md` |
| `CONSUMER.MELLIN.TWO_ROW` | `VERIFIED` | Fixed rows 2 and 3 have no common numerator zero in Re z>0. | Re z>0; two fixed detectors | None | PR #652 `24ab64551225` `claims/lemmas/L-99602-exact-two-row-mellin-landau-consumer.md` |
| `CONSUMER.MELLIN.FIVE_THREE` | `VERIFIED` | The fixed scalar 5c_X(2)+3c_X(3) has numerator -3(2^-z-1)(2^-z-2), zero-free in Re z>0. | Re z>0; one fixed scalar | None | PR #649 `433fd3662f7b` `claims/lemmas/L-99261-five-three-row-zero-free-mellin-witness.md` |
| `CONSUMER.MELLIN.ANNULAR_ROWS23` | `VERIFIED_WITH_FIXES` | The fixed annular rows 2 and 3 retain reciprocal-zeta pole detection and common-zero exclusion. | fixed annular detector family | Use the corrected P_Lambda normalization and split the two source files. | PR #547 `d60f93b0e207` `claims/lemmas/L-96010-fixed-annular-row-reciprocal-zeta-mellin-transform.md\|claims/lemmas/L-96011-exact-two-row-open-strip-noncancellation.md` |
| `CONSUMER.MELLIN.ZERO_SAFE_BOX` | `VERIFIED` | A fixed logarithmic box has a multiplier zero-free in Re s>0. | one fixed width A>1 | None | PR #653 `e928fd615d75` `claims/lemmas/L-99270-zero-free-smoothing-and-negative-mass.md` |
| `CONSUMER.MELLIN.SPECIALIZED_LANDAU` | `VERIFIED_WITH_FIXES` | A nonnegative Mellin density is singular at its finite abscissa; the specialized application handles positive-real removability and multiplicities. | nonzero locally integrable density with finite abscissa | State local integrability, nonzero density, finite abscissa, and functional-equation reflection. | PR #653 `e928fd615d75` `claims/lemmas/L-99272-specialized-landau-and-scalar-firewall.md` |
| `CONSUMER.MELLIN.HOLOMORPHIC_DEFECT` | `VERIFIED_WITH_FIXES` | A fixed signed defect with Mellin transform holomorphic in Re s>0 cannot cancel a reciprocal-zeta pole. | one fixed source, row, and defect | Keep source, row, and signed defect fixed; do not relabel the defect as positive source. | PR #650 `3f9e80f09fe1` `claims/lemmas/L-99282-holomorphic-perturbation-landau-transfer.md` |
| `API.MELLIN.SUBPOWER_NEGATIVE_MASS` | `VERIFIED_WITH_FIXES` | For a fixed zero-safe detector, subpower logarithmic negative mass plus the verified consumer implies RH. | fixed detector; every epsilon>0 | Represent the arithmetic estimate as a separate open premise. | PR #653 `e928fd615d75` `claims/lemmas/L-99270-zero-free-smoothing-and-negative-mass.md\|claims/lemmas/L-99272-specialized-landau-and-scalar-firewall.md` |
| `CONSUMER.MELLIN.MOVING_ROW_SELECTION` | `GAP_BLOCKED` | Selecting a sufficiently large row after introducing a hypothetical zero is not a fixed detector. | zero-dependent row selection | Replace with fixed rows 2,3 or the fixed 5:3 scalar. | PR #641 `19cd3939a54c` `claims/lemmas/L-99242-positive-surrogate-preserves-reciprocal-zeta-poles.md` |
| `OPEN.ARITH.ROWS23_NATIVE` | `OPEN_SUFFICIENT_FOR_RH` | The literal native source supplies the two fixed rows with eventual nonnegativity or admissible fixed holomorphic defects. | global fixed detector | None | registry node (review/2026-08-22/reconciliation/OPEN_CUTS.md) |
| `OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS` | `OPEN_SUFFICIENT_FOR_RH` | The fixed 5:3 scalar has eventual sign or subpower logarithmic negative mass. | global fixed detector | None | registry node (review/2026-08-22/reconciliation/OPEN_CUTS.md) |
| `OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS` | `OPEN_SUFFICIENT_FOR_RH` | One fixed zero-safe native detector has subpower logarithmic negative mass. | global fixed detector | None | registry node (review/2026-08-22/reconciliation/OPEN_CUTS.md) |

## Reading rule

- `VERIFIED_WITH_FIXES` may be used only with the listed repair.
- `CONDITIONAL_EXACT` does not establish its premises.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` remain open.
- Refutations and false edges are retained as mechanism firewalls.
- Family membership never confers a stronger verdict than the claim row.

Canonical registry: `canonical/2026-08-22/claims.tsv` at repository root.
