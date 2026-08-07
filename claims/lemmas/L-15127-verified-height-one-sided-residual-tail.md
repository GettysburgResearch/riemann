# L-15127 — Verified-height one-sided residual tail bound

Claim ID: `L-15127`  
Status: **PROVED FINITE ANALYTIC LEMMA; UNBOUNDED VERIFIED-HEIGHT SCHEDULE OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: the polarized Guinand--Weil zero-side identity in the CCM normalization; `L-15122`; `L-15126`; an explicit upper bound for the zero-counting function  
Scope: a rigorous finite route to

\[
R_p(0)\succeq-\omega M,
\qquad \omega<s,
\]

from a finite verified-zero height and an analytic tail estimate  
Related counterexample candidates: none

## 1. Purpose

`L-15126` isolates the correct one-sided residual gate but leaves its production
open.  This lemma proves that the entire contribution of zeros above one
verified height has an explicit operator lower bound.  Thus a finite directed
calculation below the height, plus one elementary zero-counting tail, can prove
the requested residual LMI without assuming anything about the locations of the
unseen zeros.

The result is finite.  Turning it into an unbounded sequence requires verified
heights growing rapidly enough with the support and dimension; no such
unbounded verification theorem is claimed.

## 2. CCM evaluation vectors

Let the CCM interval length be `L>0`, let

\[
 x_n=\frac{2\pi n}{L},
 \qquad |n|\le N,
 \qquad d=2N+1,
 \qquad \Omega=\frac{2\pi N}{L},
\]

and let `V_n` be the normalized finite Fourier basis.  For a centered complex
zero coordinate

\[
 z_\rho=\frac{\rho-1/2}{i}=\gamma-i\delta,
 \qquad |\delta|<\frac12,
\]

direct integration gives

\[
 \widehat V_n(z_\rho)
 =\frac{2\sin(Lz_\rho/2)}{\sqrt L\,(z_\rho-x_n)}.
 \tag{L-15127.1}
\]

Since

\[
 |\sin(a+ib)|\le \cosh |b|\le e^{|b|},
\]

one has

\[
 |\sin(Lz_\rho/2)|\le e^{L/4}.
 \tag{L-15127.2}
\]

If `|gamma|>H>Omega`, then

\[
 |z_\rho-x_n|\ge ||\gamma|-\Omega|,
\]

and therefore the evaluation vector

\[
 v_\rho=(\widehat V_{-N}(z_\rho),\ldots,
          \widehat V_N(z_\rho))^{\mathsf T}
\]

satisfies

\[
 \boxed{
 \|v_\rho\|_2^2
 \le
 \frac{4d e^{L/2}}
      {L(|\gamma|-\Omega)^2}.}
 \tag{L-15127.3}
\]

## 3. Complete unseen-zero matrix tail

Let `Q_{>H}` denote the complete polarized zero-side matrix contribution of all
nontrivial zeros with `|Im rho|>H`, with multiplicity and with exactly the
normalization used in the finite Guinand--Weil identity.  No RH assumption is
made.  An off-line pair contributes a product of two conjugate evaluation
vectors rather than a positive square, but its operator norm is still bounded
by the product of their Euclidean norms.

Define

\[
 \mathfrak B(H,\Omega)
 =\sum_{|\gamma|>H}
   \frac{m_\rho}{(|\gamma|-\Omega)^2},
 \tag{L-15127.4}
\]

where the sum follows the same zero multiplicities and symmetries as the
zero-side formula.  Then (L-15127.3), the triangle inequality for the operator
norm, and equality of the conjugate-vector norms give

\[
 \boxed{
 \|Q_{>H}\|_2
 \le
 \eta(L,N,H)
 :=\frac{4d e^{L/2}}{L}
   \mathfrak B(H,\Omega).}
 \tag{L-15127.5}
\]

Consequently

\[
 Q_{>H}\succeq-\eta(L,N,H)I.
 \tag{L-15127.6}
\]

This estimate is phase complete: no sign, critical-line location, or positivity
is assigned to an unseen zero.

## 4. Explicit zero-counting envelope

Let `N_+(T)` count all nontrivial zeros with positive ordinate at most `T`, with
multiplicity.  Suppose, for `T>=H`, a certified explicit estimate has the form

\[
 N_+(T)\le aT\log T+bT,
 \qquad a,b>0.
 \tag{L-15127.7}
\]

If `H>=2 Omega`, then

\[
 \frac1{(|\gamma|-\Omega)^2}\le\frac4{\gamma^2}.
\]

Accounting for positive and negative ordinates and using Stieltjes integration,

\[
\begin{aligned}
 \mathfrak B(H,\Omega)
 &\le 8\sum_{\gamma>H}\frac{m_\rho}{\gamma^2}\\
 &=8\int_H^\infty t^{-2}\,dN_+(t)\\
 &\le16\int_H^\infty\frac{N_+(t)}{t^3}\,dt\\
 &\le
 \frac{16}{H}
 \{a(\log H+1)+b\}.
\end{aligned}
 \tag{L-15127.8}
\]

Thus

\[
 \boxed{
 \eta(L,N,H)
 \le
 \frac{64d e^{L/2}}{LH}
 \{a(\log H+1)+b\}.}
 \tag{L-15127.9}
\]

Any sharper explicit `N(T)` or direct Stieltjes-tail certificate may replace
(L-15127.7)--(L-15127.9).

## 5. Target-pinned unseen tail

Let the real target vector `p` have no zero coordinate, and put

\[
 p_{\min}=\min_i|p_i|,
 \qquad
 \kappa_p=\frac{\|p\|_2}{p_{\min}}.
 \tag{L-15127.10}
\]

At boundary scalar zero, the target-pinning map gives

\[
 \mathcal T_p(Q_{>H},0)
 =Q_{>H}
 -\operatorname{diag}\!\left(
   \frac{(Q_{>H}p)_i}{p_i}
  \right).
 \tag{L-15127.11}
\]

Equation (L-15127.5) implies

\[
 |(Q_{>H}p)_i|
 \le\eta(L,N,H)\|p\|_2.
\]

Therefore

\[
 \left\|
 \operatorname{diag}\!\left(
   \frac{(Q_{>H}p)_i}{p_i}
  \right)
 \right\|_2
 \le\eta(L,N,H)\kappa_p.
\]

Combining with (L-15127.6) proves the one-sided residual bound

\[
 \boxed{
 \mathcal T_p(Q_{>H},0)
 \succeq
 -\omega_H I,
 \qquad
 \omega_H
 =\eta(L,N,H)(1+\kappa_p).}
 \tag{L-15127.12}
\]

This is exactly the requested first LMI with `M=I` for the unseen-zero tail.

## 6. Finite verified-height completion theorem

Let `Q_{\le H}` be the complete zero-side contribution of all zeros with
`|Im rho|<=H`, independently certified and assembled in the same normalization.
Suppose a directed complement calculation proves

\[
 \boxed{
 \mathcal T_p(Q_{\le H},0)
 \succeq s_H I
 \quad\text{on }p^\perp,
 \qquad s_H>0.}
 \tag{L-15127.13}
\]

By linearity of target pinning,

\[
 \mathcal T_p(Q_W,0)
 =\mathcal T_p(Q_{\le H},0)
  +\mathcal T_p(Q_{>H},0).
 \tag{L-15127.14}
\]

Hence, if

\[
 \boxed{
 \eta(L,N,H)(1+\kappa_p)<s_H,}
 \tag{L-15127.15}
\]

then

\[
 \boxed{
 \mathcal T_p(Q_W,0)\succeq0,
 \qquad
 \ker\mathcal T_p(Q_W,0)=\mathbb Rp.}
 \tag{L-15127.16}
\]

Indeed, on `p^perp`, the lower floor is at least

\[
 s_H-\eta(L,N,H)(1+\kappa_p)>0.
\]

This proves the desired strict pair

\[
 R_j(0)\succeq-\omega_jI,
 \qquad
 \omega_j<s_j
\]

at every finite level satisfying (L-15127.13)--(L-15127.15).

If every zero below `H` has been certified simple and on the critical line, then
`Q_(<=H)` is a finite positive Cauchy sum before target pinning.  The theorem,
however, only needs the directed target-pinned floor (L-15127.13); it does not
silently infer that floor from raw positivity.

## 7. Cofinal verified-height schedule

For levels `(L_j,N_j,p_j,H_j)`, a sufficient cofinal condition is

\[
 H_j\ge2\Omega_j,
 \tag{L-15127.17}
\]

\[
 \mathcal T_{p_j}(Q_{\le H_j},0)
 \succeq s_jI
 \quad\text{on }p_j^\perp,
 \tag{L-15127.18}
\]

and

\[
 \boxed{
 \frac{64(2N_j+1)e^{L_j/2}}
      {L_jH_j}
 \{a(\log H_j+1)+b\}
 (1+\kappa_{p_j})
 <s_j.}
 \tag{L-15127.19}
\]

Then the requested one-sided residual LMI holds at every retained level.
Combined with the smooth-target convergence and the finite real-zero theorem,
an unbounded sequence of such certificates implies RH.

The currently published verification that all zeros through height
`3,000,175,332,800` are simple and on the critical line supplies one enormous
finite value of `H`; it does not supply an unbounded sequence of heights.

## 8. Production interface

A finite proof object needs:

1. exact `L,N,Omega,H` and target coefficients;
2. the target minimum `p_min` and norm `||p||_2`;
3. either a directed Stieltjes tail `mathfrak B(H,Omega)` or explicit constants
   `a,b` in (L-15127.7);
4. an independently assembled low-zero matrix or an equivalent directed
   low-zero source;
5. an exact complement basis and directed lower `LDL^T` proof of (L-15127.13);
6. the strict rational comparison (L-15127.15).

The low-zero matrix and the prime-side complete matrix should be cross-checked,
not inferred from each other.

## 9. Gap audit

1. This lemma closes the **finite unseen-height tail**, not the unbounded-height
   theorem.
2. The factor `exp(L/2)` is the worst-case cost of an unseen zero at horizontal
   displacement almost `1/2`; improving it cofinally would require new
   horizontal zero information.
3. The conditioning factor `kappa_p` is genuine.  Tiny target coordinates can
   amplify a small raw tail through the target-pinning diagonal.
4. A fixed verified height cannot support an unbounded sequence once the other
   parameters grow without a compensating floor.
5. Claiming verified heights `H_j->infinity` would itself exclude every finite
   off-line zero.  No such claim is made.
6. The July 2026 operator/determinant proof preprints are not imported: the most
   directly relevant record is non-peer-reviewed, and an earlier official
   version explicitly carries a fatal-error disclaimer.
