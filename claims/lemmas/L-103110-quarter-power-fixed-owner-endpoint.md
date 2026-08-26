# L-103110 — Quarter-power Type-I is subpower in every fixed owner fibre

Claim ID: `L-103110`  
Status: **PROVED AT FIXED-OWNER/ORTHOGONAL-FIBRE SCOPE**  
Created: 2026-08-26  
Depends on: `L-102880`, `L-102953`  
RH status: **not assumed**

Work on

\[
Y\le X<2Y,
\qquad A\le P<2A,
\]

and retain the complete owner product `P` as a fixed source label. Put

\[
W=X/P,
\qquad
V_A=\left\lfloor(2Y/A)^{1/4}\right\rfloor.
\]

For a fixed owner/exclusion set `R`, the squarefree zero-moment lattice theorem
is uniform in the Boolean cutoff and gives

\[
\left|\mathcal T_{V_A,\mathrm{sf}}^{K,(R)}(W)\right|
\ll
Y^{o(1)}W^{-1/4}
\left(\sum_{d\le V_A}d^{-1/2}\right)^2
\ll
Y^{o(1)}V_AW^{-1/4}.
\]

Since

\[
\frac{Y}{2A}<W<\frac{2Y}{A},
\]

one has

\[
V_AW^{-1/4}\le\sqrt2.
\]

Therefore

\[
\boxed{
\left|\mathcal T_{V_A,\mathrm{sf}}^{K,(R)}(X/P)\right|
=Y^{o(1)}
}
\tag{L-103110.1}
\]

uniformly in one fixed owner fibre and, equivalently, in the orthogonal direct
sum of the labelled owner fibres.

For large `W`, the finite `2 mu_V` component is inactive because
`d<=V_A=O(W^(1/4))` while nonzero support of `K_L(W/d^2)` requires
`d asymp W^(1/2)`. Bounded `W` belongs to a finite-coordinate estimate.

## Scope

Equation (L-103110.1) does **not** estimate the physical sum over different
owner products. Passing from the orthogonal owner-fibre packet to the coherent
physical field is the restriction map in `R-103110`. No claim beyond the
fixed-fibre scope is made here.