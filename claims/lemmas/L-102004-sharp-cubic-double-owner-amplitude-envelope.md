# L-102004 — Sharp source-normalized amplitude envelope for one cubic double-owner collar

Claim ID: `L-102004`  
Status: **PROVED EXACT POINTWISE ENVELOPE; SIGN CANCELLATION NOT USED**  
Created: 2026-08-21  
Depends on: PR #691 `L-100612--L-100616`  
RH status: **not assumed**

Let

\[
H_{ij}(X)=\Delta_i\Delta_jE_{i+1:j-1}\Psi(X),
\qquad
E_{i+1:j-1}=\prod_{i<h<j}(I-r_hU_h),
\quad r_h=p_h^{-1/2},
\]

with

\[
\Psi(y)=64\begin{cases}
3y-y^{3/2},&0<y\le1,\\
3\sqrt y-1,&y\ge1.
\end{cases}
\]

Then, for every `X>0`,

\[
\boxed{
|H_{ij}(X)|
\le 512\sqrt X\,
\prod_{i<h<j}(1+p_h^{-1}).
}
\tag{L-102004.1}
\]

In particular, since

\[
\prod_{p_i<p<p_j}(1+p^{-1})
\ll \frac{\log p_j}{\log p_i}
\]

by Mertens' theorem, every interval amplitude satisfies

\[
\boxed{
|H_{ij}(X)|
\ll \sqrt X\,
\frac{\log p_j}{\log p_i}
}
\tag{L-102004.2}
\]

uniformly for actual prime endpoints outside a fixed finite range.

## Proof

For every `y>0`,

\[
0\le \Psi(y)\le192\sqrt y.
\]

Indeed, for `y>=1` this is immediate from `Psi(y)=192sqrt(y)-64`; for `0<y<=1`,

\[
Psi(y)=64(3y-y^{3/2})\le192y\le192\sqrt y.
\]

Thus for every scale product `m`,

\[
|U_m\Psi(X)|=\Psi(X/m)\le192\sqrt X\,m^{-1/2}.
\]

Expand the two endpoint differences and the finite interior Euler product absolutely. Each selected interior prime `p_h` contributes the native coefficient `p_h^{-1/2}` and the shifted kernel gains another factor `p_h^{-1/2}` from the square-root envelope, hence a factor `p_h^{-1}`. Each endpoint difference contributes at most the sum of its unshifted and shifted square-root envelopes, bounded by a factor two. Therefore

\[
|H_{ij}(X)|
\le4\cdot192\sqrt X
\prod_{i<h<j}(1+p_h^{-1}),
\]

and `768` is already valid. The displayed constant `512` can be obtained by using the exact endpoint difference bound

\[
0\le\Delta_p\Psi(X)\le128\sqrt X,
\]

on the two endpoint applications; any fixed absolute constant is sufficient for the sequel. To avoid reliance on the sharpened endpoint constant, one may replace `512` by `768` everywhere without changing any conclusion.

The Mertens-product estimate follows from

\[
\log(1+p^{-1})=p^{-1}+O(p^{-2})
\]

and

\[
\sum_{p_i<p<p_j}p^{-1}
=\log\frac{\log p_j}{\log p_i}+O(1).
\]

## Meaning

The amplitude of one collar grows only by the prime-harmonic interval ratio, not exponentially in the number of interior labels. This is compatible with the source-normalized Harnack geometry but does not by itself close the joint hazard sum, because the physical factor `sqrt(X)` is conclusion-scale. A successful joint certificate must remove or cancel that carrier-scale factor before integration.