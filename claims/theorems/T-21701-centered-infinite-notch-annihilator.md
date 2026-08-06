# T-21701 — Centered infinite-notch annihilator and one-signal RH criterion

Claim ID: `T-21701`  
Title: Centering the finite critical-line notch cascade produces one smooth subgaussian kernel that annihilates every line zero and no off-line zero  
Status: **PROPOSED PENDING INDEPENDENT REVIEW — analytic theorem; RH is not claimed proved**  
Authoring agent: `gpt56-pro-global-01`  
Created: 2026-08-07  
Source dependencies: the finite triangular pole-free window on PR #190; the square/prime explicit-formula conventions on PRs #190 and #202; the standard zero-count bound `N(T)=O(T log T)`  
Scope: one fixed global prime-side residual obtained as the centered limit of finite, compactly supported notch windows

## 1. A self-contained pole-free base window

Put

\[
 h=\log4,
 \qquad
 b_h(u)=h^{-1}\mathbf1_{[0,h]}(u),
 \qquad
 F_h=b_h*b_h,
\]

and define

\[
 G_h(u)=F_h(u)-2F_h(u-h).
 \tag{T-21701.1}
\]

It is continuous, piecewise linear, compactly supported, and its bilateral
Laplace transform is

\[
 \boxed{
 \widehat G_{h,L}(z)
 =\left(\frac{1-e^{-hz}}{hz}\right)^2(1-2e^{-hz}).}
 \tag{T-21701.2}
\]

Thus `Ghat_h(1/2)=0`, canceling the shifted zeta pole, while

\[
 \boxed{
 \widehat G_{h,L}(z)\ne0
 \qquad(0<\Re z<1/2).}
 \tag{T-21701.3}
\]

Moreover `Ghat_h(delta+it)=O((1+|t|)^(-2))` uniformly on every fixed vertical
strip.

## 2. Why centering changes the infinite-notch question

Enumerate the distinct positive ordinates at which a critical-line zero occurs:

\[
 0<\gamma_1<\gamma_2<\cdots,
 \qquad
 \xi(1/2+i\gamma_k)=0,
\]

and put

\[
 r_k=\frac{2\pi}{\gamma_k}.
\]

One factor per distinct ordinate is enough because even a multiple zero gives a
simple pole of `xi'/xi`.  The uncentered lengths have divergent sum, but their
centered variances are summable:

\[
 \boxed{
 \sum_{k\ge1}r_k^2
 =4\pi^2\sum_{k\ge1}\gamma_k^{-2}<\infty.}
 \tag{T-21701.4}
\]

The convergence follows from the ordinary zero-count upper bound; line zeros
are a subset of all zeros.

## 3. Limiting probability kernel

Let `V_k` be independent with

\[
 V_k\sim\operatorname{Unif}[-r_k/2,r_k/2],
 \qquad \mathbb EV_k=0.
\]

Since

\[
 \sum_k\operatorname{Var}(V_k)
 =\frac1{12}\sum_kr_k^2<\infty,
\]

the random series

\[
 Y=\sum_{k\ge1}V_k
 \tag{T-21701.5}
\]

converges almost surely and in `L^2`.  Let `mu_infty` be its law.  Its bilateral
Laplace transform is the normally convergent entire product

\[
 \boxed{
 P_\infty(z)
 =\int e^{-zy}\,d\mu_\infty(y)
 =\prod_{k\ge1}
   \frac{\sinh(\pi z/\gamma_k)}{\pi z/\gamma_k}.}
 \tag{T-21701.6}
\]

Every factor is `1+O_K(r_k^2)` on a compact set `K`.  Therefore the zero set is
exactly

\[
 z=i n\gamma_k,
 \qquad n\in\mathbb Z\setminus\{0\},
 \tag{T-21701.7}
\]

with accumulated multiplicities at coincident harmonics, and

\[
 \boxed{P_\infty(z)\ne0\quad(\Re z\ne0).}
 \tag{T-21701.8}
\]

Hoeffding's lemma gives

\[
 \mathbb E e^{sY}
 \le\exp\left(\frac{s^2}{8}\sum_kr_k^2\right),
 \tag{T-21701.9}
\]

so the law is subgaussian.  Keeping arbitrarily many finite uniform factors
shows that its characteristic function decays faster than every prescribed
power; hence it has a smooth density.  Splitting off a finite compactly
supported convolution and applying (T-21701.9) to the tail gives a pointwise
Gaussian tail for that density.

## 4. Centered limit of finite compact windows

Let

\[
 u_r(t)=r^{-1}\mathbf1_{[0,r]}(t),
 \qquad
 G_M=G_h*u_{r_1}*\cdots*u_{r_M},
 \qquad
 S_M=\sum_{k\le M}r_k.
\]

If `mu_M` is the law of `sum_(k<=M)V_k`, then exactly

\[
 \boxed{
 \widetilde G_M(t):=G_M(t+S_M/2)=G_h*\mu_M(t).}
 \tag{T-21701.10}
\]

Thus

\[
 \widetilde G_M\longrightarrow
 G_\infty:=G_h*\mu_\infty
 \tag{T-21701.11}
\]

locally uniformly and in every fixed exponentially weighted `L^1` norm needed
below.  The limit is smooth with Gaussian tails, and

\[
 \boxed{
 \widehat G_{\infty,L}(z)
 =\widehat G_{h,L}(z)P_\infty(z).}
 \tag{T-21701.12}
\]

Consequently

\[
 \widehat G_{\infty,L}(1/2)=0,
 \qquad
 \boxed{
 \widehat G_{\infty,L}(z)\ne0
 \quad(0<\Re z<1/2).}
 \tag{T-21701.13}
\]

For `delta` in a fixed real interval,

\[
 |P_\infty(\delta+it)|
 \le P_\infty(|\delta|),
 \tag{T-21701.14}
\]

because it is the transform of a symmetric probability law.  Hence the base
`O(t^-2)` vertical decay is retained.

## 5. One globally defined prime signal

The Gaussian tail makes

\[
 \boxed{
 Q_\infty(x)
 =\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
  G_\infty(x-\log n)}
 \tag{T-21701.15}
\]

absolutely convergent for every real `x`, locally uniformly in `x`.  Let
`E_infty^known(x)` be the explicit trivial-zero, endpoint, and initial-segment
term in the same convention as the finite pole-free formula, and put

\[
 \boxed{R_\infty(x)=Q_\infty(x)-E_\infty^{\rm known}(x).}
 \tag{T-21701.16}
\]

The rapidly decreasing explicit formula follows directly or by passing to the
limit in the finite centered identities:

\[
 \boxed{
 R_\infty(x)
 =-\sum_{\rho}m_\rho
  \widehat G_{\infty,L}(\rho-1/2)
  e^{(\rho-1/2)x}.}
 \tag{T-21701.17}
\]

The series is absolutely convergent in the standard symmetric convention:
`Ghat_h=O(t^-2)`, (T-21701.14) is uniform for
`|Re rho-1/2|<=1/2`, and the unit-interval zero count is `O(log t)`.

The finite centered prime residuals converge locally uniformly to
`R_infty`.  Thus every computation may remain finite even though the theorem
has one fixed limiting object.

## 6. Exact one-signal RH equivalence

Assume RH.  Every nontrivial zero has centered coordinate `+-i gamma_k`, and the
corresponding factor in (T-21701.6) vanishes.  Hence every term in
(T-21701.17) is zero and

\[
 \boxed{\mathrm{RH}\Longrightarrow R_\infty\equiv0.}
 \tag{T-21701.18}
\]

Conversely, suppose `R_infty` is identically zero.  The unilateral Laplace
identity, after the known terms are removed, is

\[
 \mathcal LR_\infty(z)
 =-\widehat G_{\infty,L}(z)
   \frac{\zeta'}{\zeta}(z+1/2).
 \tag{T-21701.19}
\]

The left side is holomorphic.  By (T-21701.13), no pole of `zeta'/zeta` in the
open shifted strip can be canceled.  Thus there is no zero with
`Re rho>1/2`; the functional equation gives RH.  Therefore

\[
 \boxed{
 \mathrm{RH}
 \iff R_\infty(x)=0\ \text{for every real }x}
 \tag{T-21701.20}
\]

or, equivalently,

\[
 \boxed{
 \mathrm{RH}
 \iff Q_\infty=E_\infty^{\rm known}.}
 \tag{T-21701.21}
\]

This is one fixed prime identity, not an order-of-limits criterion.

## 7. Rightmost-zero exponent of the limiting residual

Let

\[
 \Theta_\zeta
 =\sup_{\zeta(\rho)=0}(\Re\rho-1/2).
\]

If RH is false, (T-21701.13) leaves every off-line zero visible.  The elementary
Hardy/Laplace abscissa argument gives

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{X\to\infty}
 \frac{\log\left(
 1+\int_X^{X+1}|R_\infty(x)|^2dx
 \right)}{2X}.}
 \tag{T-21701.22}
\]

Under RH the same energy is identically zero.  Thus the fixed signal has a sharp
dichotomy:

```text
RH:
  the all-line-zero annihilator leaves exactly zero nontrivial prime signal.

not RH:
  the same residual has positive exponential energy exponent Theta_zeta.
```

## 8. What centering adds

The uncentered compact supports expand because `sum r_k` diverges.  The present
renormalization separates

```text
divergent part:  deterministic translation S_M/2,
convergent part: centered random spread with sum r_k^2<infinity.
```

After centering, there is one canonical noncompact subgaussian profile.  It
annihilates the complete critical-line spectrum and no point in the open
counterexample strip.

## 9. Proof boundary and serious path

The probability product, limiting window, explicit-formula passage, and
analytic equivalence are the new theorem submitted for review.  They do **not**
prove the arithmetic identity `R_infty=0`; by (T-21701.20), that identity is
exactly RH.

The serious positive target is the fixed convolution identity

\[
 \boxed{
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 G_\infty(x-\log n)
 =E_\infty^{\rm known}(x)
 \quad\text{for all }x.}
 \tag{T-21701.23}
\]

Unlike a moving matrix moat, this is one smooth subgaussian prime kernel with an
explicit entire transform.  Its finite centered approximants use only finitely
many certified line-zero balls and finite prime-power manifests.

No proof of (T-21701.23), no counterexample, and no resolution of RH is claimed.