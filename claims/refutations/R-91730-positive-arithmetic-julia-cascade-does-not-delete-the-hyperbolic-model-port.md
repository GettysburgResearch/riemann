# R-91730 — A complete positive arithmetic Julia cascade does not by itself delete the hyperbolic model port

Refutation ID: `R-91730`  
Status: **EXACT OUTPUT-ALLOCATION FIREWALL**  
Created: 2026-08-13  
Depends on: `L-91730/L-91731`  
RH status: **unproved**

Let a one-dimensional source have the exact positive split

\[
1=r+d,
\qquad r,d>0.
\]

For any `0<=h<=d`, the same isometric source vector may be mapped into the
orthogonal model outputs with squared norms

\[
\text{critical/stable}=r+d-h,
\qquad
\text{hyperbolic}=h.
\]

All source identities and total norms are preserved. Positivity of the source
cascade therefore does not determine which model output receives the detail.

The matrix version follows by rotating a positive detail space into the
direct sum of an auxiliary and a hyperbolic space.

Consequently a valid proof must construct the **canonical** source-to-model
intertwiner, or prove an equality condition that identifies the critical and
stable outputs before norms are taken. The existence of some positive
arithmetic dilation is not sufficient.
