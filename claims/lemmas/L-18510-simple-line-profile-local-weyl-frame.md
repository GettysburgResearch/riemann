# L-18510 — Simple critical-line zeros give a logarithmic frame for compact boundary profiles

Claim ID: `L-18510`  
Title: Positive simple-line density and profile compactness imply `Sigma_R >= c log R` along a cofinal subsequence  
Status: `PROVED CONDITIONAL PROFILE TRANSFER; PRODUCTION PROFILE HYPOTHESIS OPEN`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependencies: the unconditional positive proportion of simple critical-line zeros; Riemann--von Mangoldt; weak compactness of finite measures  
Scope: a quantitative lower bound for the full-complement frame endpoint  
Related candidates: none

## 1. Simple-line counting input

Let

\[
 N_0^*(T)
 =\#\{0<\gamma\le T:
       \zeta(1/2+i\gamma)=0
       \text{ and the zero is simple}\}.                 \tag{L-18510.1}
\]

Use any unconditional constant `kappa_*>0` for which

\[
 N_0^*(T)
 \ge(\kappa_*+o(1))N(T).                                 \tag{L-18510.2}
\]

Pratt--Robles--Zaharescu--Zeindler prove such a statement, with a published
constant exceeding five twelfths for critical-line zeros and an explicit
positive simple-line proportion in their optimization. Only positivity of
`kappa_*` is used below.

Choose one fixed

\[
 K>\kappa_*^{-1}.                                        \tag{L-18510.3}
\]

For `R->infinity`, define the rescaled simple-zero measure on `[1,K]` by

\[
 \nu_R
 =\frac1{R\log R}
  \sum_{\substack{R\le\gamma\le KR\\
                   \gamma\text{ simple line zero}}}
  \delta_{\gamma/R}.                                     \tag{L-18510.4}
\]

## 2. Nonzero diffuse subsequential limits

Fix `kappa'<kappa_*` with `K kappa'>1`. Since

\[
 N_0^*(KR)-N_0^*(R)
 \ge \kappa' N(KR)-N(R)                                  \tag{L-18510.5}
\]

for all sufficiently large `R`, Riemann--von Mangoldt gives

\[
 \liminf_{R\to\infty}\nu_R([1,K])
 \ge\frac{K\kappa'-1}{2\pi}>0.                          \tag{L-18510.6}
\]

The total masses are also uniformly bounded. Hence every sequence `R_j->infty`
has a subsequence for which

\[
 \nu_{R_j}\overset{*}{\rightharpoonup}\nu              \tag{L-18510.7}
\]

for a finite nonzero measure `nu` on `[1,K]`.

Moreover, for every interval `[a,b] subset [1,K]`, the total zero count gives

\[
 \limsup_{j\to\infty}\nu_{R_j}([a,b])
 \le\frac{b-a}{2\pi}.                                    \tag{L-18510.8}
\]

Consequently

\[
 \boxed{
 0<\nu([1,K])<\infty,
 \qquad
 \nu\le\frac1{2\pi}\,dx.}                              \tag{L-18510.9}
\]

In particular `nu` has no atoms and its support has an accumulation point.

## 3. Compact analytic profile family

Let `Omega` be a complex neighborhood of `[1,K]`. For each `j`, let `W_j` be a
finite-dimensional metric space with harmonic lift `J_j` and frequency scale
`R_j`. Assume that for every `w in W_j` with `||w||_(G_j)=1` there is a
holomorphic profile

\[
 \Phi_{j,w}\in\mathcal O(\Omega)                         \tag{L-18510.10}
\]

such that

\[
 \sup_{x\in[1,K]}
 \left|
  R_j^{1/2}\widehat{J_jw}(R_jx)-\Phi_{j,w}(x)
 \right|
 \le r_j,                                                 \tag{L-18510.11}
\]

where `r_j->0`.

Assume also that the profile family

\[
 \mathcal P
 =\{\Phi_{j,w}:j\ge1,\ \|w\|_{G_j}=1\}       \tag{L-18510.12}
\]

is relatively compact in `O(Omega)` for locally uniform convergence and that
zero is not in its closure:

\[
 \boxed{
 0\notin\overline{\mathcal P}.}                          \tag{L-18510.13}
\]

This is the normalized full-profile Gram condition. It is stronger than a
pointwise bound on individual basis vectors and is invariant under changes of
basis in `W_j`.

## 4. Uniform sampling by the limiting simple-zero measure

For every nonzero holomorphic `Phi`, its real zeros in `[1,K]` are discrete.
Since `nu` is nonzero and nonatomic,

\[
 \int_{1}^{K}|\Phi(x)|^2d\nu(x)>0.                       \tag{L-18510.14}
\]

Compactness of `overline(P)` and (L-18510.13) therefore give

\[
 \boxed{
 c_{\mathcal P,\nu}
 :=\min_{\Phi\in\overline{\mathcal P}}
   \int_1^K|\Phi(x)|^2d\nu(x)>0.}                        \tag{L-18510.15}
\]

Indeed, a minimizing sequence has a locally uniformly convergent subsequence;
if the minimum were zero, its nonzero holomorphic limit would vanish on the
support of `nu`, which has an accumulation point.

Weak convergence of `nu_(R_j)` and compactness of the profile family imply the
uniform convergence

\[
 \inf_{\Phi\in\mathcal P_j}
 \int|\Phi|^2d\nu_{R_j}
 \longrightarrow
 \inf_{\Phi\in\mathcal P_\infty}
 \int|\Phi|^2d\nu,                                       \tag{L-18510.16}
\]

along the selected subsequence. A finite epsilon-net in
`C([1,K])` gives the elementary proof. Hence eventually

\[
 \inf_{\Phi\in\mathcal P_j}
 \int|\Phi|^2d\nu_{R_j}
 \ge\frac12c_{\mathcal P,\nu}.                           \tag{L-18510.17}
\]

## 5. Logarithmic selected-zero frame

Let `Z_j` be the finite simple-line-zero block in `[R_j,KR_j]`. Equations
(L-18510.4), (L-18510.11), and (L-18510.17) give, uniformly for
`||w||_(G_j)=1`,

\[
 \begin{aligned}
 \sum_{\gamma\in Z_j}|\widehat{J_jw}(\gamma)|^2
 &=\log R_j
   \int_1^K|\Phi_{j,w}(x)|^2d\nu_{R_j}(x)
   +o(\log R_j)\\
 &\ge\frac14c_{\mathcal P,\nu}\log R_j
 \end{aligned}                                           \tag{L-18510.18}
\]

for every sufficiently large `j`. The error estimate uses the uniform bound on
the compact profile family, `r_j->0`, and the bounded masses of `nu_(R_j)`.

Therefore the selected-zero Gram has the cofinal lower bound

\[
 \boxed{
 K_{Z_j}^C|_{W_j}
 \succeq c_0\log R_j\,G_j|_{W_j},
 \qquad c_0>0,}                                          \tag{L-18510.19}
\]

and hence

\[
 \boxed{
 \Sigma_j\ge c_0\log R_j}                               \tag{L-18510.20}
\]

along an unbounded subsequence.

## 6. Frame–tail consequence

If the complete one-sided residual and radical endpoint satisfy

\[
 B_{T,j}+2\epsilon_j=o(\log R_j),                         \tag{L-18510.21}
\]

then (L-18510.20) gives

\[
 B_{T,j}+2\epsilon_j<\Sigma_j                            \tag{L-18510.22}
\]

cofinally. `L-18508` then produces the explicit `beta_j` and the requested
strict inequalities. More economically, if

\[
 B_{T,j}=o(\log R_j),                                    \tag{L-18510.23}
\]

then `T-18503` gives a positive direct visible Schur moat of order `log R_j`.

## 7. Interpretation for endpoint packets

For a shrinking endpoint profile

\[
 (U_{R,x_0}f)(t)=R^{1/2}f(R(t-x_0)),
\]

one has exactly

\[
 \widehat{U_{R,x_0}f}(Rx)
 =R^{-1/2}e^{-iRx x_0}\widehat f(x).                     \tag{L-18510.24}
\]

A same-end packet therefore has the required `R^-1/2` scale after removing one
unit-modulus phase. A full two-end packet contains the moving relative phase
`exp(2iRxx_0)`. That phase destroys profile compactness unless it is removed by
harmonic minimization, proved negligible, or incorporated into a separate
matrix-valued oscillatory theorem.

Thus (L-18510.20) closes the same-end/profile part of the quantitative frame,
while the terminal/opposite-end phase remains a distinct load-bearing gate.

## 8. Proof boundary

- The measure compactness and analytic-profile argument are unconditional under
  (L-18510.2).
- The correct simple-line input is the Pratt--Robles--Zaharescu--Zeindler
  positive-proportion theorem, not a multiplicity-only critical-line count.
- No current artifact proves (L-18510.10)--(L-18510.13) for the complete
  harmonically lifted two-end packet.
- No current one-sided omitted-zero theorem proves (L-18510.21) on the same
  sequence.
- Therefore the lemma supplies a concrete quantitative route to the requested
  moat, but does not by itself prove RH.
