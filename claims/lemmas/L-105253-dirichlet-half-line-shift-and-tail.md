# L-105253 — Exact half-line Dirichlet-shift representation and growing-degree tail stability

Claim ID: `L-105253`  
Status: **PROVED EXACT AT SAFE-LINE SOURCE SCOPE**  
Created: 2026-08-24  
Depends on: L-105251; elementary Dirichlet convolution  
RH status: not assumed

For `sigma>1`, let
\[
\mathcal A_\sigma
=\left\{a:\sum_{n\ge1}|a(n)|n^{-\sigma}<\infty\right\}
\]
with Dirichlet convolution and norm
\[
\|a\|_\sigma=\sum_{n\ge1}|a(n)|n^{-\sigma}.
\]
This is a commutative Banach algebra.

On `L^2(0,infinity)`, let
\[
(S_tf)(u)=\mathbf1_{u\ge t}f(u-t).
\]
Then `S_t` is an isometry and `S_tS_v=S_(t+v)`. Define
\[
\boxed{
\Pi_\sigma(a)=
\sum_{n\ge1}a(n)n^{-\sigma}S_{\log n}.
}
\tag{1}
\]
The series converges in operator norm and
\[
\boxed{
\Pi_\sigma(a*b)=\Pi_\sigma(a)\Pi_\sigma(b),
\qquad
\|\Pi_\sigma(a)\|\le\|a\|_\sigma.
}
\tag{2}
\]
Thus the safe-line Dirichlet source has an exact one-sided contractive representation with no finite projection edge.

Let
\[
A_X=\sum_{2\le n\le X}\Lambda(n)\delta_n,
\qquad
x_X=A_X/L.
\]
If `|L|>A_abs(sigma):=sum Lambda(n)n^(-sigma)`, then `||x_X||_sigma<1` uniformly in `X`. Therefore `P_K(x_X)` and its half-line realization are invertible with L-105251's bounds for every `K`.

For `sigma>sigma_0>1`,
\[
\|A-A_X\|_\sigma
\le
A_{\rm abs}(\sigma_0)X^{-(\sigma-\sigma_0)}.
\tag{3}
\]
Consequently
\[
\boxed{
\|P_K(A/L)-P_K(A_X/L)\|_\sigma
\le
Kc_K\frac{A_{\rm abs}(\sigma_0)}{|L|}
X^{-(\sigma-\sigma_0)}.
}
\tag{4}
\]
After the inverse bound, the relative source error is at most
\[
\boxed{
K\frac{A_{\rm abs}(\sigma_0)}{|L|}
X^{-(\sigma-\sigma_0)}.
}
\tag{5}
\]

For `sigma_0=9/8`, `sigma=5/4`, and `X=T^lambda`, every degree
\[
K(T)=o\!\left(|L|T^{\lambda/8}\right)
\]
is safe for this omitted-prime row. In particular every fixed degree and every polylogarithmically growing degree are harmless.

This closes polynomial invertibility and the arithmetic safe-line tail. It does not close archimedean freezing, horizontal caps, smooth-taper conditioning, or the map from the safe-line source representation to the actual Xi contour compression.
