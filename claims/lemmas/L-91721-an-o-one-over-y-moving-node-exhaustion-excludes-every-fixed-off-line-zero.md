# L-91721 — An o(1/Y) moving-node exhaustion excludes every fixed off-line zero

Claim ID: `L-91721`  
Status: **EXACT CONDITIONAL COFINAL ZERO-EXCLUSION THEOREM**  
Created: 2026-08-13  
Depends on: `L-91720`, `L-91620/L-91621`  
RH status: **unproved**

## 1. One dyadic annulus

Fix one dyadic horizontal annulus

\[
a_j<x\le a_{j-1},
\qquad
a_j=2^{-j-1}.
\]

Put

\[
\delta_j=a_j,
\qquad
b_j=a_{j-1},
\qquad
\eta_j(Y)=\sqrt{b_j^2+Y^2}.
\]

Suppose a canonical source-to-model calculation gives the genuine upper bound

\[
0\le
\Lambda_j^{\rm ann}(\eta_j(Y))
\le
\varepsilon_j(Y).
\tag{L-91721.1}
\]

If

\[
\boxed{
\varepsilon_j(Y)=o_j(Y^{-1}),
}
\tag{L-91721.2}
\]

then the annulus contains no crossed zero.

## 2. Proof

Assume a crossed zero of depth `x>=a_j` and height `y_0` exists. For every
`Y>=|y_0|`, `L-91720` gives

\[
\Lambda_j^{\rm ann}(\eta_j(Y))
\ge
\frac{2a_j}
     {\sqrt{b_j^2+Y^2}+b_j}.
\]

The right side is

\[
\frac{2a_j}{Y}+O_j(Y^{-2}),
\]

contradicting (L-91721.2) for large `Y`.

## 3. Completion to RH

If (L-91721.1)--(L-91721.2) hold for every dyadic annulus, then no zero has
positive depth. Functional-equation symmetry excludes negative depth, and RH
follows.

Thus exact entropy exhaustion is stronger than necessary. A source-identified
cofinal error with rate `o(1/Y)` suffices.

## 4. Quantitative finite-height version

If

\[
\varepsilon_j(Y)
<
\frac{2a_j}
     {\sqrt{b_j^2+Y^2}+b_j},
\]

then the entire depth-height box

\[
a_j\le x\le b_j,
\qquad |y|\le Y
\]

is zero free.

This gives a directed finite certification target once the entropy error is
computed in the correct source/model normalization.
