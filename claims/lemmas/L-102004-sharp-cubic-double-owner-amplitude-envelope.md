# L-102004 — Exact bounded endpoint kernel after cubic carrier subtraction

Claim ID: `L-102004`
Status: **PROVED EXACT POINTWISE ENVELOPES**
Created: 2026-08-21
Audited: 2026-08-21
Depends on: PR #691 `L-100612--L-100614`
RH status: **not assumed**

Let

\[
\Psi(y)=64\begin{cases}
3y-y^{3/2},&0<y\le1,\\
3\sqrt y-1,&y\ge1,
\end{cases}
\qquad
P(y)=192\sqrt y,
\]

and define the carrier-subtracted scalar kernel

\[
G(y)=\Psi(y)-P(y).
\]

For `0<y<=1`, writing `x=sqrt(y)` gives

\[
G(y)
=-64\bigl(3x-3x^2+x^3\bigr)
=-64\bigl[1-(1-x)^3\bigr],
\]

whereas `G(y)=-64` for `y>=1`. Hence

\[
\boxed{-64\le G(y)\le0\qquad(y>0).}
\tag{L-102004.1}
\]

For endpoint primes `p_i<p_j`, put

\[
\widetilde K_{ij}
=(I-U_{p_i})(I-U_{p_j})G.
\]

Then

\[
\boxed{\|\widetilde K_{ij}\|_{L^\infty(0,\infty)}\le256.}
\tag{L-102004.2}
\]

This is the correct conclusion-scale envelope after subtracting the explicit
positive `sqrt(X)` carrier. No factor `sqrt(X)` remains in the endpoint
kernel.

For the full centered interval residual

\[
\widetilde H_{ij}(X)
=\prod_{i<h<j}(I-p_h^{-1/2}U_{p_h})
\widetilde K_{ij}(X),
\]

absolute expansion gives

\[
\boxed{
|\widetilde H_{ij}(X)|
\le256\prod_{i<h<j}(1+p_h^{-1/2}).
}
\tag{L-102004.3}
\]

The product in (L-102004.3) is generally power-sized. Thus boundedness of the
centered endpoint kernel does not license source-blind absolute collapse.
After source-side squaring of a set `Q` of interior primes, the corresponding
factors improve from `1+p^-1/2` to `1+p^-1` for `p in Q`.

## Safe uncentered envelope

For completeness, the original uncentered entry

\[
H_{ij}(X)
=(I-U_{p_i})(I-U_{p_j})
\prod_{i<h<j}(I-p_h^{-1/2}U_{p_h})\Psi(X)
\]

satisfies the exact safe bound

\[
\boxed{
|H_{ij}(X)|
\le
192\sqrt X\,(1+p_i^{-1/2})(1+p_j^{-1/2})
\prod_{i<h<j}(1+p_h^{-1}).
}
\tag{L-102004.4}
\]

Indeed `0<=Psi(y)<=192sqrt(y)`. Every selected interior prime contributes
`p^-1/2` from the native coefficient and another `p^-1/2` from the shifted
square-root envelope. The endpoint differences contribute the displayed
factors.

In particular, the universal coarser constant `768` is valid in front of
`sqrt(X) prod(1+p^-1)`. The earlier displayed constant `512` relied on the
false inequality

\[
\Delta_p\Psi(X)\le128\sqrt X;
\]

on the deep branch the leading coefficient approaches `192`, so that
sharpening is withdrawn.

The Mertens estimate

\[
\prod_{p_i<p<p_j}(1+p^{-1})
\ll \frac{\log p_j}{\log p_i}
\]

may be applied to (L-102004.4), but not to the unsquared centered product
(L-102004.3).
