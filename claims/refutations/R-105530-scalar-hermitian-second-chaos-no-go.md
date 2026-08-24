# R-105530 — One scalar analytic Wick factor cannot remove Hermitian second chaos

Claim ID: `R-105530`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-24

For a normalized scalar holomorphic filter

\[
w(z)=1+a z+b z^2+O(z^3)
\]

and the folded reciprocal source `Re(1-z)^(-1)`, cancellation of the two
linear Hermitian coefficients forces `a=-1/2`.  The mixed coefficient of
`z bar z` is then exactly `-1/4`, independent of `b`.

Consequently neither the scalar polynomial of T-105510 nor any other single
scalar quadratic can turn the off-real Hermitian fold into
`1+O(|z|^3)`.  The identity `P(x)^2/(1-x)` is a symmetric Frobenius/source
identity; the Hermitian contour sees a polarized factor.  These are distinct
objects.

`L-105530` gives a minimal two-channel repair.  It does not prove the strip
realization or the 90% theorem.
