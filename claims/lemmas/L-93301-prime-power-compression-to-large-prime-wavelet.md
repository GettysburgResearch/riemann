# L-93301 — Factor-four endpoint kernels compress to one large-prime wavelet

Claim ID: `L-93301`  
Status: **PROVED UNCONDITIONAL COMPRESSION THEOREM**  
Created: 2026-08-16  
Depends on: `L-93300`; elementary Chebyshev bounds  
RH status: **unproved**

For a fixed integer `r>=1`, normalize

\[
W_r(x)=\frac1{r!}\Phi_r(x)
=\frac1{r!}[G_r(x)-4G_r(4x)],
\]

with the convention `G_r(4x)=0` for `x>1/4`. For `r=1`, `W_1=3K-12K(4x)`; dividing once more by `3` recovers the exact cubic normalization of PR #498. Scalar normalizations do not affect zero survival.

## 1. Mellin moments and small-argument order

From `L-93300`,

\[
\widehat W_r(s)
=(1-4^{1-s})
\frac{s-1}{\prod_{j=r}^{2r+1}(s+j)}.
\tag{L-93301.1}
\]

Hence

\[
\int_0^1W_r(x)dx=0,
\qquad
\int_0^1W_r(x)\log x\,dx=0.
\tag{L-93301.2}
\]

Moreover, for `0<x<=1/4`,

\[
|W_r(x)|\le C_r x^r.
\tag{L-93301.3}
\]

For the frozen cubic normalization `W=W_1/3`, the exact polynomial is

\[
W(x)=
\begin{cases}
5x-63x^2+170x^3,&0<x\le1/4,\\
(-x+3x^2-2x^3)/3,&1/4<x\le1.
\end{cases}
\tag{L-93301.4}
\]

## 2. Exact Q4 source rewrite

Let

\[
A_r(N)=\sum_{m\le N}c_\circ(m)G_r(m/N).
\]

Coefficientwise expansion gives

\[
\boxed{
A_r(N)
=r!\sum_{n\le N}\Lambda(n)W_r(n/N)
+3(\log4)\sum_{4^a\le N}G_r(4^a/N).
}
\tag{L-93301.5}
\]

The second term is an explicit two-adic gauge of size `O_r(log(2N))`.

## 3. Prime-power compression

Define

\[
P_{r}(N)=r!\sum_{\sqrt N<p\le N}(\log p)W_r(p/N).
\tag{L-93301.6}
\]

Then

\[
\boxed{
A_r(N)=P_r(N)+O_r(\sqrt N\log(2N)).
}
\tag{L-93301.7}
\]

Indeed, for first powers `p<=sqrt N`, (L-93301.3) and `theta(x)<<x` give a contribution `O_r(1)` when `r=1` and no larger for `r>1`. The complete higher-prime-power mass is

\[
\sum_{k\ge2}\theta(N^{1/k})\ll\sqrt N\log(2N),
\]

and the gauge is logarithmic.

Thus every same-prime tower and the four-adic correction are unconditionally paid before the final arithmetic estimate.
