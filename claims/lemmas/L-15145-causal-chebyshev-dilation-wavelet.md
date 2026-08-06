# L-15145 — Causal Chebyshev dilation wavelet

Claim ID: `L-15145`  
Title: A one-parameter causal safe filter converts the global prime-energy problem into an exact multiplicative difference of the Chebyshev function  
Status: **PROPOSED PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: elementary Laplace transforms and the definition of the Chebyshev function  
Scope: exact source simplification and finite Gram identity; no RH conclusion by itself

## 1. The causal dilation wavelet

Fix a real scale

\[
 a>1,
 \qquad h=\log a,
\]

and define

\[
 g(u)=e^{-u/2}\mathbf 1_{[0,\infty)}(u).
\]

Put

\[
 \boxed{
 W_a(u)=g(u)-\sqrt a\,g(u-h).}
 \tag{L-15145.1}
\]

Equivalently,

\[
 W_a(u)=
 \begin{cases}
 0,&u<0,\\
 e^{-u/2},&0\le u<h,\\
 (1-a)e^{-u/2},&u\ge h.
 \end{cases}
 \tag{L-15145.2}
\]

Thus `W_a` is causal, exponentially decaying, and belongs to every ordinary
`L^p` space on the half-line. It is not compactly supported, but at every fixed
prime translation only finitely many prime powers occur.

With the bilateral Laplace convention

\[
 \widehat f(z)=\int_{\mathbb R}f(u)e^{-zu}\,du,
\]

one has, initially for `Re z>-1/2`,

\[
 \boxed{
 \widehat W_a(z)
 =\frac{1-\sqrt a\,a^{-z}}{z+1/2}.}
 \tag{L-15145.3}
\]

Its zeros are exactly

\[
 \boxed{
 z=\frac12-\frac{2\pi i k}{\log a},
 \qquad k\in\mathbb Z.}
 \tag{L-15145.4}
\]

They all lie on the boundary line `Re z=1/2`. In particular,

\[
 \widehat W_a(1/2)=0
\]

and

\[
 \boxed{
 \widehat W_a(z)\ne0
 \qquad(0<\Re z<1/2).}
 \tag{L-15145.5}
\]

On every closed vertical strip contained in `Re z>-1/2`,

\[
 \widehat W_a(\sigma+it)=O_{a,\sigma}((1+|t|)^{-1}).
 \tag{L-15145.6}
\]

One inverse power is enough for the half-plane `H^2` transfer because the zeta
logarithmic derivative has only polylogarithmic vertical growth on a fixed
zero-free half-plane.

## 2. Exact prime signal

Let

\[
 \psi(x)=\sum_{n\le x}\Lambda(n)
\]

with `psi(x)=0` for `x<2`, and define

\[
 \boxed{
 Q_a(x)=
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 W_a(x-\log n).}
 \tag{L-15145.7}
\]

The sum is finite for every real `x`, because `W_a(x-log n)=0` unless
`n\le e^x`.

The two terms of (L-15145.1) may be summed exactly. The first gives

\[
 e^{-x/2}\psi(e^x),
\]

while the shifted term gives

\[
 a e^{-x/2}\psi(e^x/a).
\]

Therefore

\[
 \boxed{
 Q_a(x)=e^{-x/2}
 \left[\psi(e^x)-a\psi(e^x/a)\right].}
 \tag{L-15145.8}
\]

Writing

\[
 P(t)=\frac{\psi(t)}{t},
\]

this becomes the multiplicative scale difference

\[
 \boxed{
 Q_a(\log t)=\sqrt t\,[P(t)-P(t/a)].}
 \tag{L-15145.9}
\]

Thus the safe prime filter is exactly a continuous Chebyshev dilation wavelet.
No numerical convolution or prime-pair expansion is needed to produce it.

## 3. Exact energy identity

For `Y>2`, put

\[
 \mathcal E_a(Y)
 =\int_{\log2}^{\log Y}|Q_a(x)|^2dx.
 \tag{L-15145.10}
\]

The substitution `t=e^x` and (L-15145.9) give

\[
 \boxed{
 \mathcal E_a(Y)
 =\int_2^Y
 \left|
 \frac{\psi(t)}t-
 \frac{\psi(t/a)}{t/a}
 \right|^2dt.}
 \tag{L-15145.11}
\]

More generally, for `sigma>0`,

\[
 \boxed{
 \int_{\log2}^{\infty}
 e^{-2\sigma x}|Q_a(x)|^2dx
 =\int_2^{\infty}t^{-2\sigma}
 |P(t)-P(t/a)|^2dt.}
 \tag{L-15145.12}
\]

This is a multiplicative Besov-type energy of the normalized Chebyshev
function.

## 4. Exact finite Gram kernel

For `Y>1` and positive thresholds `r,s`, define

\[
 \kappa_Y(r,s)=
 \begin{cases}
 \displaystyle {1\over\max(r,s)}-{1\over Y},
   &\max(r,s)<Y,\\
 0,&\max(r,s)\ge Y.
 \end{cases}
 \tag{L-15145.13}
\]

For positive integers `m,n`, put

\[
 \boxed{
 \begin{aligned}
 K_{a,Y}(m,n)
 ={}&\kappa_Y(m,n)
 -a\kappa_Y(am,n)\\
 &-a\kappa_Y(m,an)
 +a^2\kappa_Y(am,an).
 \end{aligned}}
 \tag{L-15145.14}
\]

Then

\[
 K_{a,Y}(m,n)
 =\int_1^Y
 \frac{(\mathbf1_{t\ge m}-a\mathbf1_{t\ge am})
       (\mathbf1_{t\ge n}-a\mathbf1_{t\ge an})}{t^2}\,dt.
 \tag{L-15145.15}
\]

Hence every finite matrix `(K_(a,Y)(m_i,m_j))` is positive semidefinite, and

\[
 \boxed{
 \mathcal E_a(Y)
 =\sum_{m,n<Y}
 \Lambda(m)\Lambda(n)K_{a,Y}(m,n).}
 \tag{L-15145.16}
\]

For integer `a` and rational `Y`, the complete kernel is rational. It requires
no logarithmic primitive and admits exact standard-library replay.

## 5. The diagonal is elementary

The complete, untruncated diagonal norm is

\[
 \int_1^{\infty}
 \frac{(\mathbf1_{t\ge n}-a\mathbf1_{t\ge an})^2}{t^2}\,dt
 =\frac{a-1}{n}.
 \tag{L-15145.17}
\]

Therefore

\[
 0\le K_{a,Y}(n,n)\le\frac{a-1}{n}
\]

and the diagonal prime-power contribution obeys

\[
 \boxed{
 \mathcal D_a(Y)
 \le(a-1)\sum_{n<Y}{\Lambda(n)^2\over n}
 =O_a((\log Y)^3),}
 \tag{L-15145.18}
\]

using only `Lambda(n)<=log n`. All possible positive exponential growth is
therefore carried by the coherent off-diagonal term.

## 6. Exact relation to PR #216's compact triangle

Let `G_tri` denote the compact triangular safe window of `L-21501` at scale
`a=4`:

\[
 \widehat G_{\rm tri}(z)
 =e^{-z}\left({1-e^{-z}\over z}\right)^2
  (1-2\,4^{-z}).
\]

Let

\[
 k(u)=\left({d\over du}+{1\over2}\right)\phi(u-1),
\]

where `phi=1_[0,1]*1_[0,1]`. Then

\[
 \widehat k(z)
 =e^{-z}\left({1-e^{-z}\over z}\right)^2(z+1/2),
\]

so (L-15145.3) gives the exact factorization

\[
 \boxed{
 G_{\rm tri}=k*W_4.}
 \tag{L-15145.19}
\]

Moreover,

\[
 \|k\|_1=2.
 \tag{L-15145.20}
\]

Consequently the compact PR #216 signal is the finite signed smoothing

\[
 \boxed{
 Q_{G_{\rm tri}}=k*Q_4.}
 \tag{L-15145.21}
\]

This identifies the observed compact-window cancellation as a smoothed version
of the more elementary two-scale Chebyshev cancellation. The two filters have
the same open-strip zero-free property, but the causal representation replaces
a prime-pair spline by one exact difference of `psi`.

## 7. Proof boundary

Closed in this lemma:

- the safe zero geometry of `W_a`;
- the exact Chebyshev dilation identity;
- the weighted and unweighted energy identities;
- the exact finite positive Gram kernel;
- the polynomial diagonal bound;
- the compact-to-causal factorization at scale four.

Not closed:

\[
 \mathcal E_a(Y)=Y^{o(1)}.
\]

That global energy estimate is RH-bearing and is stated separately in
`T-15119`.