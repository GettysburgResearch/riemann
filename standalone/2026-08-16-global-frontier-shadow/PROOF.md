# Standalone proof outline

The row is the stop-loss transform of the global knot measure

\[
 \nu_{r,j}=\sum_{d\mid P_r}\sum_{m\ge j}
 \frac{\mu(d)q_j(m)}{\sqrt{dm}}\delta_{\log(dm)}.
\]

Its coefficient sequence splits exactly into a positive rough reservoir and
finitely supported frontier corrections.  The `GLOBAL-FRONTIER-SHADOW`
algorithm transports the corrections across products, using source-disjoint
edge, shoulder, complete-block, and partial-block stores.  Its outputs are
positive atoms, monotone pairs, and log-barycentric butterflies.  The stop-loss
kernel is decreasing and convex, proving the finite sieve row nonnegative.

Specializing to all active primes gives the full Möbius row.  Its fixed-row
Mellin transform contains `1/zeta(s+1/2)`.  No open-strip zero cancels every row,
and Landau's theorem gives the proposed RH conclusion.
