# L-107120 — The stationary beta square is a calibrated additive Chowla average

**Claim ID:** `L-107120`  
**Status:** proved exact finite arithmetic identity  
**Date:** 2026-08-31  
**RH:** not assumed

Let `q=67`, `L=log q`, and

\[
\mu_q(n)=\mu(n)\mathbf 1_{q\nmid n}.
\]

Retain the fixed triangular kernel of `T-107110`,

\[
\Lambda_q(v)=\left(1-\frac{|v|}{L}\right)_+,
\]

and write

\[
\mathcal Q_q(Y)=
\sum_{m,n\le Y}
\frac{\mu_q(m)\mu_q(n)}{\sqrt{mn}}
\Lambda_q\!\left(\log\frac mn\right).
\tag{1}
\]

## 1. Exact additive-shift form

The diagonal is

\[
\mathcal D_q(Y)=\sum_{n\le Y}\frac{\mu_q(n)^2}{n}=O(\log(2Y)).
\tag{2}
\]

For `h>=1`, put

\[
\begin{aligned}
\mathcal C_{q,h}(Y)
={}&\sum_{\substack{1\le n\le Y-h\\ h\le(q-1)n}}
\frac{\mu_q(n)\mu_q(n+h)}{\sqrt{n(n+h)}}
\left(1-\frac{\log(1+h/n)}{L}\right).
\end{aligned}
\tag{3}
\]

Grouping `(m,n)` by the positive additive gap and using symmetry gives

\[
\boxed{
\mathcal Q_q(Y)=\mathcal D_q(Y)+2\sum_{1\le h<Y}\mathcal C_{q,h}(Y).
}
\tag{4}
\]

The support condition in (3) is exactly the multiplicative ratio condition
`n+h<=qn`; no endpoint smoothing or asymptotic replacement is used.

## 2. Primitive additive-gap form

For a nonzero term of (3), write uniquely

\[
g=(n,h),\qquad n=ga,\qquad h=gr.
\]

Then `(a,r)=1`, equivalently `(a,a+r)=1`. On squarefree support,
`g`, `a`, and `a+r` are pairwise coprime, and

\[
\mu(ga)\mu(g(a+r))=\mu(a)\mu(a+r).
\]

Therefore the complete off-diagonal aggregate is

\[
\boxed{
\begin{aligned}
\sum_{h<Y}\mathcal C_{q,h}(Y)
={}&\sum_{\substack{g,r,a\ge1\\
 g(a+r)\le Y\\
 r\le(q-1)a\\
 (a,r)=1\\
 (g,a(a+r))=1\\
 q\nmid g a(a+r)}}
\frac{\mu(a)\mu(a+r)}{g\sqrt{a(a+r)}}
\left(1-\frac{\log(1+r/a)}{L}\right).
\end{aligned}
}
\tag{5}
\]

Thus the multiplicative common core is the divisor `g|h`, while the remaining
source is a literal primitive two-point Möbius correlation in the additive
variable `r`.

## 3. Quantitative zero-abscissa calibration

Define

\[
\mathfrak C_q(X)=
\max_{2\le Y\le X}
\left|\sum_{1\le h<Y}\mathcal C_{q,h}(Y)\right|.
\tag{6}
\]

Since (2) is subpower and `T-107110` proves

\[
\operatorname{pexp}\max_{Y\le X}\mathcal Q_q(Y)=2\Theta-1,
\]

identity (4) gives

\[
\boxed{
\operatorname{pexp}\mathfrak C_q=2\Theta-1.
}
\tag{7}
\]

Equivalently, for every `1/2<=sigma<=1`,

\[
\boxed{
\zeta(s)\ne0\ (\Re s>\sigma)
\Longleftrightarrow
\mathfrak C_q(X)\ll_\varepsilon X^{2\sigma-1+\varepsilon}.
}
\tag{8}
\]

In particular, RH is equivalent to a subpower bound for the one assembled
additive Chowla aggregate (5). No individual fixed-shift estimate is asserted
or required.

## 4. Scope

The lemma changes coordinates but does not estimate (5). It preserves the
maximal horizon, every additive gap up to the physical ratio boundary, the
literal factor-67 deletion, all common cores, and the Möbius signs. The
resulting correlation aggregate remains exactly RH-bearing.
