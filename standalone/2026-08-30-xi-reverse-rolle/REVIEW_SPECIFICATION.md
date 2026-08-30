# Hostile review specification — T-107100

Frozen programme parent:

```text
PR #714
d1a9fea34aa0620a5cb2da41061518638ab8b219
```

Required reconstruction:

1. Re-derive the shared-zero multiplicity contribution
   `N(f')=N(f)-Z_distinct+sum r_c`.
2. Track the sign of `g=f'/f` through every parent zero and every nonshared
   derivative zero.
3. Verify the boundary sign convention in `L-107100.2`.
4. Check that the local weight `r+iota` is always a nonnegative even integer.
5. Verify the simple-Morse specialization and the coefficient `2` on
   `L_f(c)<0`.
6. Recompute the six replay fixtures, including the multiple-parent and
   degenerate-critical examples.
7. Derive the conjugate-pair curvature formula and the exact integral `2/b`.
8. Confirm that the telescoping Xi identity uses real-zero multiplicity and
   does not assume simplicity.
9. Reject any inference from the curvature integral to a discrete defect count
   without an explicit depth/separation theorem.
10. Confirm that neither high-derivative concentration nor RH is claimed.

Immediate falsifiers:

```text
coefficient one on a simple extra extremum;
ignoring shared parent/derivative zeros;
counting a stationary inflection as a Rolle-generated crossing;
dropping interval-boundary signs;
turning the 2/Im(rho) integral budget into a point count source-blindly;
using a global derivative-zero percentage as a local descent theorem.
```
