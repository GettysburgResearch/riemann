# T-21701 — Centered infinite-notch annihilator and completed prime criterion

Claim ID: `T-21701`  
Title: Centering the finite critical-line notch cascade produces one smooth subgaussian kernel whose completed Guinand--Weil residual vanishes exactly under RH  
Status: **CORRECTED PROPOSED THEOREM PENDING INDEPENDENT REVIEW — RH is not claimed proved**  
Authoring agent: `gpt56-pro-global-01`  
Created: 2026-08-07  
Corrected: 2026-08-07 after `R-21701`  
Source dependencies: the finite triangular pole-free window on PR #165; the centered Guinand--Weil explicit formula; the ordinary zero-count bound `N(T)=O(T log T)`  
Scope: one fixed global **completed two-sided** prime residual obtained as the centered limit of finite compact notch windows

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
 =\left({1-e^{-hz}\over hz}\right)^2(1-2e^{-hz}).}
 \tag{T-21701.2}
\]

Thus

\[
 \widehat G_{h,L}(1/2)=0,
 \qquad
 \boxed{
 \widehat G_{h,L}(z)\ne0
 \quad(0<\Re z<1/2).}
 \tag{T-21701.3}
\]

Moreover `Ghat_h(delta+it)=O((1+|t|)^(-2))` uniformly when `delta`
ranges over a fixed compact interval.

## 2. The centered line-zero notch product

Enumerate the distinct positive ordinates at which a critical-line zero occurs:

\[
 0<\gamma_1<\gamma_2<\cdots,
 \qquad
 \xi(1/2+i\gamma_k)=0,
\]

and put

\[
 r_k={2\pi\over\gamma_k}.
\]

One factor per distinct ordinate is enough for annihilating the logarithmic
Derivative: even a multiple zero gives a simple pole of `xi'/xi`, with its
multiplicity carried only by the residue.  The ordinary zero-count upper bound
gives

\[
 \boxed{
 \sum_{k\ge1}r_k^2
 =4\pi^2\sum_{k\ge1}\gamma_k^{-2}<\infty.}
 \tag{T-21701.4}
\]

Let `V_k` be independent random variables with

\[
 V_k\sim\operatorname{Unif}[-r_k/2,r_k/2],
 \qquad \mathbb EV_k=0.
\]

Then

\[
 Y=\sum_{k\ge1}V_k
 \tag{T-21701.5}
\]

converges almost surely and in `L2`.  Let `mu_infinity` be its probability law.
Its bilateral Laplace transform is the normally convergent entire product

\[
 \boxed{
 P_\infty(z)
 =\int_{\mathbb R}e^{-zy}\,d\mu_\infty(y)
 =\prod_{k\ge1}
 {\sinh(\pi z/\gamma_k)\over \pi z/\gamma_k}.}
 \tag{T-21701.6}
\]

Every factor is `1+O_K(r_k^2)` on a compact set `K`.  Hence its zero set is
exactly

\[
 z=in\gamma_k,
 \qquad n\in\mathbb Z\setminus\{0\},
 \tag{T-21701.7}
\]

with accumulated multiplicity at coincident harmonics, and

\[
 \boxed{P_\infty(z)\ne0\quad(\Re z\ne0).}
 \tag{T-21701.8}
\]

Hoeffding's lemma gives

\[
 \mathbb E e^{sY}
 \le
 \exp\left({s^2\over8}\sum_kr_k^2\right),
 \tag{T-21701.9}
\]

so the law is subgaussian.  Retaining arbitrarily many finite uniform factors
shows that its characteristic function has arbitrary polynomial decay; hence
`mu_infinity` has a smooth density.  Only rapid decrease and exponential
moments, not a sharp pointwise tail constant, are used below.

## 3. Centered limit of finite compact windows

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

Consequently

\[
 \widetilde G_M\longrightarrow
 G_\infty:=G_h*\mu_\infty
 \tag{T-21701.11}
\]

locally uniformly and in every fixed exponentially weighted `L1` norm.  Its
transform is

\[
 \boxed{
 \widehat G_{\infty,L}(z)
 =\widehat G_{h,L}(z)P_\infty(z).}
 \tag{T-21701.12}
\]

Therefore

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

because it is the transform of a symmetric probability law.  The base
`O(t^-2)` vertical envelope is therefore retained.

## 4. The completed translated Guinand--Weil identity

The centered limit is two-sided.  For a real rapidly decreasing `G`, define

\[
 H_{G,x}(z)=e^{zx}\widehat G_L(z)
 \tag{T-21701.15}
\]

and the completed prime stream

\[
 \boxed{
 \mathcal P_G(x)=
 \sum_{n\ge2}{\Lambda(n)\over\sqrt n}
 \bigl[G(x-\log n)+G(x+\log n)\bigr].}
 \tag{T-21701.16}
\]

Both sums converge absolutely for `G=G_infinity`.

In the standard centered Guinand--Weil convention, put

\[
 \boxed{
 \begin{aligned}
 \mathcal A_G(x)={}&H_{G,x}(1/2)+H_{G,x}(-1/2)-G(x)\log\pi\\
 &+{1\over2\pi}\int_{\mathbb R}
 H_{G,x}(it)
 \Re {\Gamma'\over\Gamma}
 \left({1\over4}+{it\over2}\right)dt.
 \end{aligned}}
 \tag{T-21701.17}
\]

The integral is absolutely convergent for `G_infinity`.  With multiplicities,
the completed explicit formula is

\[
 \boxed{
 \sum_\rho m_\rho
 H_{G,x}(\rho-1/2)
 =\mathcal A_G(x)-\mathcal P_G(x).}
 \tag{T-21701.18}
\]

The exact overall normalization may be checked against the chosen definition of
`xi`; multiplying `xi` by a nonzero constant changes neither side.  Equation
(T-21701.18), including both prime streams, is the interface used in the rest
of the theorem.

For the annihilator kernel define

\[
 \boxed{
 \mathcal R_\infty(x)
 :=\mathcal P_{G_\infty}(x)-\mathcal A_{G_\infty}(x).}
 \tag{T-21701.19}
\]

Then

\[
 \boxed{
 \mathcal R_\infty(x)
 =-\sum_\rho m_\rho
 \widehat G_{\infty,L}(\rho-1/2)
 e^{(\rho-1/2)x}.}
 \tag{T-21701.20}
\]

The zero series is absolutely convergent on every compact real `x` interval:
`Ghat_h=O(t^-2)`, (T-21701.14) is uniform for
`|Re rho-1/2|<=1/2`, and the unit-interval zero count is `O(log t)`.

`R-21701` explains why the one-sided terminal stream from the first version of
this claim had to be replaced by (T-21701.16).

## 5. Exact one-signal RH equivalence

Assume RH.  Every nontrivial zero has centered coordinate `+-i gamma_k`, and
`P_infinity` vanishes there.  Hence every term in (T-21701.20) is zero and

\[
 \boxed{\mathrm{RH}\Longrightarrow\mathcal R_\infty\equiv0.}
 \tag{T-21701.21}
\]

Conversely, suppose `mathcal R_infinity` vanishes identically on the real line.
For `Re z>1/2`, termwise integration on `x>=0` gives

\[
 0=
 -\sum_\rho{m_\rho\widehat G_{\infty,L}(\rho-1/2)
 \over z-(\rho-1/2)}.
 \tag{T-21701.22}
\]

The right side extends meromorphically, and the residue at a distinct centered
zero `w=rho-1/2` is

\[
 -m_\rho\widehat G_{\infty,L}(w).
\]

For a critical-line zero this residue is zero.  For every zero with
`Re rho>1/2`, (T-21701.13) makes it nonzero.  Thus the identically zero
meromorphic function can have no such pole.  The functional equation excludes
the reflected half, proving RH.  Therefore

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathcal R_\infty(x)=0
 \quad\hbox{for every real }x.}
 \tag{T-21701.23}
\]

Equivalently,

\[
 \boxed{
 \mathcal P_{G_\infty}=\mathcal A_{G_\infty}.}
 \tag{T-21701.24}
\]

This is one fixed completed prime identity, not an order-of-limits assertion.

## 6. A positive completed prime-energy endpoint

For any `sigma>1/2`, define

\[
 \boxed{
 \mathscr E_\sigma
 =\int_0^\infty e^{-2\sigma x}
 |\mathcal R_\infty(x)|^2dx.}
 \tag{T-21701.25}
\]

It is a nonnegative completed prime-pair functional.  Expanding the absolutely
convergent zero series gives the exact Cauchy Gram

\[
 \boxed{
 \mathscr E_\sigma
 =\sum_{\rho,\rho'}
 {c_\rho\overline{c_{\rho'}}
  \over 2\sigma-(\rho-1/2)-\overline{(\rho'-1/2)}},
 \qquad
 c_\rho=m_\rho\widehat G_{\infty,L}(\rho-1/2).}
 \tag{T-21701.26}
\]

This is the Gram of the functions

\[
 c_\rho e^{(\rho-1/2)x}
 \quad\hbox{in }L^2(\mathbb R_+,e^{-2\sigma x}dx).
\]

All critical-line coefficients vanish.  Distinct exponentials are linearly
independent, so

\[
 \boxed{
 \mathscr E_\sigma=0
 \iff \mathrm{RH}.}
 \tag{T-21701.27}
\]

Thus the corrected prime-annihilator endpoint can be phrased as one positive
identity: prove the completed finite-prime-pair energy (T-21701.25) is zero.
The theorem identifies the endpoint; it does not prove that zero value.

## 7. Rightmost-zero exponent

Let

\[
 \Theta_\zeta
 =\sup_{\zeta(\rho)=0}(\Re\rho-1/2).
\]

If RH is false, the nonvanishing property (T-21701.13) leaves every off-line zero
visible.  The same Hardy/Laplace abscissa argument as for compact pole-free
windows gives

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{X\to\infty}
 {\log\left(1+\int_X^{X+1}
 |\mathcal R_\infty(x)|^2dx\right)\over2X}.}
 \tag{T-21701.28}
\]

Under RH the energy is identically zero.  Hence the fixed completed signal has
the sharp dichotomy

```text
RH:
  the all-line-zero annihilator leaves zero completed prime residual.

not RH:
  the same residual has positive exponential block-energy exponent Theta_zeta.
```

## 8. Finite centered approximants

For finite `M`, replace `mu_infinity` by `mu_M` and
`P_infinity` by its finite product.  The centered compact test
`G_h*mu_M` must already be consumed through the completed two-sided formula
(T-21701.18).  Uniform exponential moments and the vertical `O(t^-2)` envelope
permit passage to the limit in the prime, archimedean, and zero terms on every
compact `x` interval.

Thus all proof-producing calculations can remain finite, while their limit is
the fixed residual in (T-21701.19).

## 9. Proof boundary and serious path

Proved within the claim, subject to independent normalization review:

- normal convergence and zero geometry of `P_infinity`;
- the centered finite-window limit;
- the completed Guinand--Weil residual formula;
- the equivalence between residual vanishing and RH;
- the positive Cauchy-Gram energy formulation.

Not proved:

\[
 \mathcal R_\infty\equiv0
 \qquad\hbox{or}\qquad
 \mathscr E_\sigma=0.
\]

By (T-21701.23) and (T-21701.27), either statement is precisely RH.  A valid
positive proof must force the **completed two-sided** prime and archimedean
functional to vanish; a one-sided terminal-prime estimate cannot establish the
centered endpoint.
