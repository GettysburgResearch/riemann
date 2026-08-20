# Corrected dual endgame after the live graph audit

## Decision

The strongest two routes are:

1. an activation-zero quadratic envelope, because its Euler activities are
   supercritical and its activation geometry is `C1`;
2. a root-free phase-Hasse transport, because the complete neutral residual is
   removed algebraically before physical collapse.

The fixed-shell Hardy/GCD and minimal-wavelet criteria were not selected:
current repository audits prove their complete bounds equivalent to RH.  The
positive priority-flux route was not selected because its claimed subpower
estimate is false.

## New exact findings

- PR #685's cell antiderivative prices `E_2/X`, not `E_2`.  The advertised
  Mellin-Landau arrow is invalid.
- The activation-zero envelope has an exact all-integer source, zero-safe
  Mellin transform, atom-free future identity, and a `C1` quadratic spline on
  every integer cell.
- Every actual prime-label block through four labels is positive.  A
  non-native five-copy label-2 mutation is negative, so no source-blind
  complete-monotonicity claim is made.
- The symmetric phase-Hasse symbol is an exact two-parameter divergence.
  Its degree-zero and degree-one sectors vanish.
- The full free labelled phase packet is polylogarithmic.  The only remaining
  loss is the literal half-order physical cross-core collapse.

## Boundary

Neither final producer is proved.  The packet narrows the two routes without
renaming an RH-equivalent scalar as an elementary estimate.

```text
FAEG100401 / ACAD100400   open
PHPC100410                open
RH                         unproved
```
