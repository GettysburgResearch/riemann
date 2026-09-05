# L-106673 — The unregularized Cauchy volume is logarithmic Laplace transport

Claim ID: `L-106673`  
Status: **PROVED EXACT FOR EQUAL-RANK SIMPLE BLOCKS**  
Created: 2026-08-26  
Depends on: `L-106670`; Cauchy determinant and Frullani identity  
RH status: **not assumed**

Let

\[
z_j=y_j+ia_j,
\qquad
w_k=v_k+ic_k,
\qquad y_j,v_k>0,
\]

for `j,k=1,...,r`, and let

\[
e_z(\xi)=\sqrt{2\operatorname{Re}z}\,e^{-z\xi}
\]

be the normalized exponential vectors in `L^2(0,infinity)`.  Write `G_z,G_w`
for the self Grams and `C` for the cross Gram.  At the endpoint `tau=1`,

\[
\boxed{
\mathfrak Z_1
={|\det C|^2\over\det G_z\det G_w}.
}
\tag{L-106673.1}
\]

The Cauchy determinant formula gives

\[
\boxed{
\mathfrak Z_1
=
{\displaystyle
\prod_j(2y_j)\prod_k(2v_k)
\prod_{j<\ell}|z_j+\overline{z_\ell}|^2
\prod_{k<q}|w_k+\overline{w_q}|^2
\over
\displaystyle
\prod_{j,k}|z_j+\overline{w_k}|^2}.
}
\tag{L-106673.2}
\]

Put

\[
S_z(\xi)=\sum_j e^{-z_j\xi},
\qquad
S_w(\xi)=\sum_k e^{-w_k\xi}.
\]

Equal cardinality cancels the singularity at zero.  Expanding the square and
using Frullani's identity gives

\[
\boxed{
-\log\mathfrak Z_1
=
\int_0^\infty{|S_z(\xi)-S_w(\xi)|^2\over\xi}\,d\xi.
}
\tag{L-106673.3}
\]

For one pole pair,

\[
1-\mathfrak Z_1
={
(a-c)^2+(y-v)^2
\over
(a-c)^2+(y+v)^2
},
\tag{L-106673.4}
\]

which is the exact squared pseudohyperbolic cost.

This identity explains the surviving degree-zero geometry: the horizontal
coordinates appear as oscillatory phases in a diagonal logarithmic Laplace
energy.  The live gate uses `tau<1` because `-log Z_1` can overpay a finite
canonical charge without bound.
