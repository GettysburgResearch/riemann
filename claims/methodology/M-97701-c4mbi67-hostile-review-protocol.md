# M-97701 - Hostile review protocol for the C4MBI67 critical core

Review in this order.

1. Recompute the sparse scalar dictionary `a_*` from rows two and three.
2. Verify annularization turns every logarithmic ramp into `H_X(n)`.
3. Check the three scale substitutions in `kappa_X` and all square-root factors.
4. Derive the four interval coefficients independently:
   `-3/2`, `(9 sqrt(2)-3)/2`, `(9 sqrt(2)-12)/2`, `-6`.
5. Check `B_(1/2)` uses `mu(n)/sqrt(n)`, not `mu(n)/n` or unweighted Mertens.
6. Reconstruct the root Bellman equality and verify no state-wise quantifier is
   silently inserted into the pointwise equivalence.
7. Verify logarithmic ownership spends every squarefree `n` with total weight
   exactly one.
8. Reject any argument that replaces actual Möbius signs by magnitudes before
   the four-band pairing.
9. Recompute the Mellin consumer only after the producer sign has genuinely
   been established.

Immediate falsifiers are an incorrect factor `9/sqrt(2)`, a missing unit atom,
a duplicated prime owner, an absolute-value Type-II estimate presented as the
one-sided sign, or a claim that the exact reduction itself proves RH.
