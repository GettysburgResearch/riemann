# R-105510 — A pointwise quadratic Wick multiplier is not automatically safe

Claim ID: `R-105510`  
Status: **PROVED FIREWALL**

The polynomial

\[
P_2(z)=1-z/2-z^2/8
\]

has the two real zeros `-2+2 sqrt(3)` and `-2-2 sqrt(3)`.  Consequently one
may not multiply every analytic observation pointwise by `P_2(A_X/L)` and
claim inertia preservation without proving that this scalar factor is nonzero
on every relevant pole jet.

`L-105510` avoids this false step.  It applies `P_2` as a unit in a finite
nilpotent **projected source algebra**, where the nonconstant part is
nilpotent and the coordinate change is triangular with diagonal one.  The
remaining obligation is to transport that projected coordinate congruence to
the actual Xi contour matrix and price the projection edge.

Pointwise zero-freeness and triangular algebraic invertibility are distinct
interfaces and must not be conflated.
