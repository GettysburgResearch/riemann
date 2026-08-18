# R-95520 — A polylog-stable scale filter cannot add a zero at `z=1/2`

Claim ID: `R-95520`  
Status: **PROVED EXACT FILTER BARRIER**  
Created: 2026-08-18  
Depends on: `L-95520/L-95521`  
RH status: **not assumed**

Let

\[
 P(S)=\sum_{j=0}^dc_jS^j,
 \qquad c_0\ne0,
\]

be a fixed finite dyadic endpoint filter. Its Mellin multiplier is

\[
 P(2^{-z}).
\]

Suppose `P(S)^{-1}` has coefficient mass bounded by a fixed power of
`log X` at endpoint `X`. Then every zero of the polynomial `P(w)` lies outside
the open unit disk; zeros on the unit circle may occur with finite
multiplicity and produce only polynomial growth in the number of dyadic
scales.

A zero at `z=1/2` would be a zero at

\[
 w=2^{-1/2},
\]

strictly inside the unit disk. The reciprocal power series would then have
coefficients growing at least like

\[
 |w|^{-n}=2^{n/2}.
\]

At endpoint `X=2^n`, this is `X^{1/2}`, not polylogarithmic. Therefore

\[
 \boxed{
 \text{no polylog-stably invertible finite dyadic filter can add a zero at }
 z=1/2.
 }
\tag{R-95520.1}
\]

The double/single zeros in `L-95521` are intrinsic to the Q4 packet. Further
safe filtering can add moments only on the boundary `Re z=0`, as in
`L-95520`; it cannot manufacture additional continuous-prime cancellation at
`z=1/2` without losing the conclusion-producing equivalence by a power of
`X`.
