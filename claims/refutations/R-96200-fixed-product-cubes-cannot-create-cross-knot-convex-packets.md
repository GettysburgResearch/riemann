# R-96200 — Fixed-product divisor cubes cannot create cross-knot convex packets

Claim ID: `R-96200`  
Status: **PROVED EXACT SCOPE CORRECTION**  
Created: 2026-08-17  
Frozen target: PR #537 / imported `L-94200` at `2c2d4dd834ee61c54a6f8bdd7ba204a01896d593`

For a fixed physical product `n=dm`, every divisor-cube occurrence lies at the same logarithmic knot

\[
\log d+\log m=\log n.
\]

Consequently no operation that remains inside one fixed-product cube can create a nontrivial packet

\[
\lambda\delta_a+(1-\lambda)\delta_c-\delta_b,
\qquad a<b<c.
\]

The fixed-product cube can perform exact equal-knot cancellation only. Any proof that invokes distinct-knot convexity while simultaneously asserting that it never mixes products has a scope gap.

This correction does **not** refute the row-positivity statement. It forces the transport to be global across products and requires one-use ownership of every cross-product reservoir.

```text
same-product sign reversal       valid
same-product cross-knot packet   impossible
row positivity                   not decided by this correction
RH                               unproved
```
