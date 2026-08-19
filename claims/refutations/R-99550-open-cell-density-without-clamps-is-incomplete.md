# R-99550 — Open-cell density without activation clamps is still incomplete

Claim ID: `R-99550`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-19  
Depends on: `R-99230`, `L-99550`  
RH status: **unproved**

The conclusion of `T-99550` is not a generic consequence of the open-cell
identity

\[
V\Phi=2\sqrt y-1.
\]

For arbitrary \(a,b\),

\[
\Phi_{a,b}(y)
=
4y\log y+2\sqrt y\log y+ay+b\sqrt y
\]

has exactly the same open-cell inverse density, because \(y\) and \(\sqrt y\)
lie in the Volterra nullspace. But

\[
\Phi_{a,b}(1)=a+b,
\qquad
\Phi'_{a,b}(1+)=6+a+\frac b2.
\]

Unless

\[
(a,b)=(-12,12),
\]

zero extension across \(y=1\) creates a boundary-value defect, a
first-derivative jump, or both. The generic knot atom and homogeneous
coefficients of PR #638 then reappear.

Therefore:

```text
smooth density positivity alone       insufficient
one activation clamp only             insufficient
arbitrary homogeneous adjustment      forbidden
both exact clamps                      load-bearing
```

The double-clamping calculation does not invalidate `R-99230`; it supplies the
additional data that its firewall requires.
