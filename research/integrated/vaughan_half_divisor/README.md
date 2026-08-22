# Owner/Vaughan/half-divisor

## Integrated scope

**Strongest reviewed result:** Mixed coboundary, large-divisor rewrite, half-divisor and Gram diagonal.

**First open arrow:** Signed near-collision HCNC.

**Relationship to RH:** open nodes: OPEN.ARITH.HCNC

**Family state:** `live`

This packet contains 6 reconciled semantic claim rows. It is a reviewed residency manifest. Exact proof bodies remain at the frozen source PR/head/path recorded in `SOURCE_MANIFEST.tsv`.

## Claims

| Claim | Verdict | Statement | Scope | Required fix | Exact source |
|---|---|---|---|---|---|
| `ARITH.OWNER.DOUBLE_OWNER_COBBOUNDARY` | `VERIFIED` | Least/greatest-owner blocks form an exact bi-triangular decomposition and mixed coboundary; rectangles and staircases telescope to boundary currents. | all finite ordered prime rectangles | None | PR #695 `5b549abb560e` `claims/lemmas/L-100700-double-owner-mixed-coboundary-and-rectangle-telescope.md` |
| `ARITH.CVXD.CARRIER_PRESERVATION` | `VERIFIED` | Power-sized short/long carriers cancel only after projection to the physical sum channel. | common physical source and detector | None | PR #699 `f23dd8174856` `claims/lemmas/L-101101-carrier-preserving-short-long-projection.md\|claims/lemmas/L-101102-exact-sharp-to-minimal-wavelet-derivative-bridge.md` |
| `ARITH.VAUGHAN.LARGE_DIVISOR` | `VERIFIED` | The balanced Vaughan remainder is the exact large-divisor Hankel form with corrected signs and squarefree/gcd constraints. | finite compact kernel | None | PR #696 `f4016db548af` `claims/lemmas/L-102001-balanced-vaughan-large-divisor-hankel-form.md` |
| `ARITH.VAUGHAN.HALF_DIVISOR` | `VERIFIED_WITH_FIXES` | The ratio-four packet factors through two fields and eta*eta=1 reduces them to one field with Hardy norm 3. | finite endpoint fields | Use product AB in the Cauchy gate and truncate before applying the full-line Hardy inequality. | PR #696 `f4016db548af` `claims/lemmas/L-102009-ratiofour-two-field-factorization-of-balanced-vaughan.md\|claims/lemmas/L-102010-half-divisor-symmetric-one-field-reduction.md` |
| `ARITH.VAUGHAN.HAAR_GRAM_DIAGONAL` | `VERIFIED` | The half-completed field has an exact ratio-four Haar autocorrelation Gram, and its diagonal is unconditionally subpower. | finite U<N and dyadic averages | None | PR #702 `89f995450977` `claims/lemmas/L-103100-exact-half-completed-haar-gram.md\|claims/lemmas/L-103101-diagonal-is-unconditionally-subpower.md` |
| `OPEN.ARITH.HCNC` | `OPEN_SUFFICIENT_FOR_RH` | The oriented signed ratio-four off-diagonal near-collision has the required subpower one-sided bound. | dyadic averaged endpoints | None | PR #702 `89f995450977` `claims/lemmas/L-103102-fractional-nyman-and-near-collision-equivalence.md` |

## Reading rule

- `VERIFIED_WITH_FIXES` may be used only with the listed repair.
- `CONDITIONAL_EXACT` does not establish its premises.
- `OPEN_SUFFICIENT_FOR_RH` and `OPEN_RH_EQUIVALENT` remain open.
- Refutations and false edges are retained as mechanism firewalls.
- Family membership never confers a stronger verdict than the claim row.

Canonical registry: `canonical/2026-08-22/claims.tsv` at repository root.
