# T-90701 — Terminal resolvent derivatives give a fixed-safe-Euler RH criterion

Claim ID: `T-90701`  
Status: **PROPOSED COMPLETE CONDITIONAL CRITERION — PR #364 TERMINAL THEOREM AND INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Depends on: PR #375 heat-residue kernel; PR #364 terminal-pair theorem; completed-zeta zero symmetry and local zero count  
RH status: **unproved**

## Statement

For

\[
 s_x=\frac12+ix,
 \qquad 0<y<\frac12,
\]

put

\[
 \mathscr X(s)=-\xi'(s)/\xi(s),
 \qquad q=\sqrt{1+y^2},
\]

and define

\[
 \mathcal F_{\alpha,y}(s)
 =\frac{\mathscr X(s+\sqrt\alpha)}{\sqrt\alpha}
 -\frac{
   \mathscr X(s+\sqrt{\alpha+y^2}-y)
  +\mathscr X(s+\sqrt{\alpha+y^2}+y)}
 {2\sqrt{\alpha+y^2}}.
\]

For `k>=0`, let

\[
 F_{k,y}(s)=(-\partial_\alpha)^k
 \mathcal F_{\alpha,y}(s)\big|_{\alpha=1}
\]

and

\[
\begin{aligned}
 R_{k,y}(z)=k!\Bigg[&
  (1-z^2)^{-k-1}
 -\frac12(1-z^2-2yz)^{-k-1}\\
 &-\frac12(1-z^2+2yz)^{-k-1}
 \Bigg].
\end{aligned}
\]

Put `r_(k,y)=R_(k,y)(y)<0` and

\[
 \mathfrak C_k(x,y)
 =\frac{\Re F_{k,y}(s_x)}{r_{k,y}}.
\]

Subject to the terminal-pair theorem of PR #364,

\[
\boxed{
 \mathrm{RH}
 \iff
 \mathfrak C_k(x,y)\ge0
 \quad
 \text{for every }k\ge0,\ x\in\mathbb R,\ 0<y<1/2.
}
\]

Dyadic `x,y` suffice.

## Exact zero expansion

The rational Cauchy formula and critical-line contour shift give

\[
\begin{aligned}
 \Re F_{k,y}(s_x)
 ={}&-\sum_{\xi(1/2+i\gamma)=0}
 m_\gamma R_{k,y}(i(\gamma-x))\\
 &-2\sum_{\Re\rho>1/2}
 m_\rho\Re R_{k,y}(\rho-s_x).
\end{aligned}
\]

Since

\[
 R_{k,y}(iu)
 =\int_0^\infty \tau^ke^{-\tau-u^2\tau}
   [1-\cos(2y u\tau)]d\tau\ge0,
\]

RH implies the required sign.

A right-side target at `rho=s_x+y` contributes exactly

\[
 -2m
\]

to `mathfrak C_k`, for every `k`.

## Terminal isolation

For a terminal nuisance `z=d+ir`, PR #364 gives

\[
 d^2-r^2+2yd<3y^2.
\]

Every nuisance denominator in `R_(k,y)(z)` therefore has modulus strictly
larger than the target denominator `1-3y^2`.  Hence

\[
 \frac{R_{k,y}(z)}{r_{k,y}}\to0
\]

exponentially in `k`.  The local zero count upgrades this to the complete zero
sum, while critical-line terms vanish by the same denominator separation.
Thus a terminal pair of multiplicity `m` satisfies

\[
 \mathfrak C_k(x,y)=-2m+o(1).
\]

False RH therefore produces a strict negative finite-order witness.

## Complete-monotone and Hankel equivalents

Let

\[
 G_{x,y}(\alpha)=-\Re\mathcal F_{\alpha,y}(s_x).
\]

Under RH,

\[
 G_{x,y}(\alpha)
 =\int_0^\infty e^{-\alpha\tau}W_{x,y}(\tau)d\tau,
 \qquad W_{x,y}(\tau)\ge0.
\]

Therefore `G_(x,y)` is completely monotone.  The sequence

\[
 A_k(x,y)=(-1)^kG_{x,y}^{(k)}(1)=-\Re F_{k,y}(s_x)
\]

is a Stieltjes moment sequence, and every matrix

\[
 (A_{i+j}(x,y))_{0\le i,j\le d}
\]

is positive semidefinite.  A terminal false-RH pair makes `A_k<0` for all
sufficiently large `k`.  Complete monotonicity and all finite Hankel PSD are
therefore equivalent criteria at this declared scope.

## Safe Euler scope

The three sample points are

```text
s_x+1,
s_x+sqrt(1+y^2)-y,
s_x+sqrt(1+y^2)+y.
```

Their real parts exceed one uniformly for `0<y<1/2`.  Every finite derivative
order is therefore an absolutely convergent prime-power computation plus
explicit rational/polygamma terms.

## Boundary

This theorem does not prove the scalar signs, complete monotonicity, Hankel
positivity, or RH unconditionally.  It replaces the moving large-Gaussian
limit by a fixed-safe-Euler all-order hierarchy and gives a source-ordered
sum-of-squares target.
