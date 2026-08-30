# L-105660 — Sharp universal 32/27 phase-reserve domination

**Claim ID:** `L-105660`  
**Status:** proved exact operator theorem; constant sharp  
**Date:** 2026-08-31

Let `0<=T<=I`, let `P` project onto a finite-dimensional subspace `K`, and let
`Q` project onto `T^2K`. Define

\[
\mathfrak P=\operatorname{tr}P(I-Q),\qquad
\mathfrak R=\operatorname{tr}P(I-T)P.
\]

Then

\[
\boxed{\mathfrak P\le\frac{32}{27}\mathfrak R.}\tag{1}
\]

For an orthonormal basis `e_j` of `K`, projection optimality gives
`dist(e_j,T^2K)^2<=||(I-T^2)e_j||^2`. Sum and use functional calculus with

\[
\frac{32}{27}(1-y)-(1-y^2)^2
=\frac{(1-y)(3y-1)^2(3y+5)}{27}\ge0.
\]

Sharpness: take `T=diag(1,y)` and
`K_epsilon=span(sqrt(1-epsilon),sqrt(epsilon))`. As `epsilon->0`, the ratio
`P/R` tends to `(1-y)(1+y)^2`, whose maximum is `32/27` at `y=1/3`.

For the Cauchy packet, `T=M_{e^{-Hxi}}`,

\[
\boxed{n-\mathcal O_H\le\frac{32}{27}(n-\mathcal T_H).}\tag{2}
\]

The unresolved universal improvement is therefore the sharp constant change
`32/27 -> 1`, not an unbounded conditioning loss.
