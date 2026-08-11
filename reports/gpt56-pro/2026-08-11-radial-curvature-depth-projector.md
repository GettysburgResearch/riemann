# Radial xi curvature, exact depth projection, and unit-disc Pick signature

**Date:** 2026-08-11  
**Branch:** `research/gpt56-pro/91004-radial-curvature-depth-projector`  
**Base:** PR #393, single-safe-line Hausdorff/Pick programme  
**Riemann Hypothesis:** **unproved**

## Executive result

The unit-disc function of PR #393 is the twofold Peano integral of one radial logarithmic curvature of the completed xi function. This replaces a large safe-line coefficient hierarchy by one local differential object.

For

\[
 s_x=\frac12+ix,
 \qquad
 J_x(t)=t\frac d{dt}
 \log\left|\xi\left(s_x+\sqrt t\right)\right|,
\]

put

\[
 \mathcal C_x(t)=-J_x''(t).
\]

Then:

\[
 \mathcal A_x(w)
 =\frac4{w^2}\int_0^w(w-u)\mathcal C_x(1-u)\,du,
\]

and

\[
 \frac{d^2}{dw^2}
 \left[\frac{w^2}{4}\mathcal A_x(w)\right]
 =\mathcal C_x(1-w).
\]

The normalized safe-line coefficient `a_k(x)` is exactly

\[
 a_k(x)=\frac{4(-1)^k}{(k+2)!}\mathcal C_x^{(k)}(1).
\]

Thus the safe-line order, Hausdorff differences, Pick function and first-Hermite heat are all transforms of one curvature.

## Exact zero kernel

With `Xcal=-xi'/xi`, `r=sqrt(t)`,

\[
 \mathcal C_x(t)
 =\frac1{8r^3}\Re
 \left[-\mathscr X(s_x+r)
       +r\mathscr X'(s_x+r)
       +r^2\mathscr X''(s_x+r)\right].
\]

Its complete zero expansion is

\[
\begin{aligned}
 \mathcal C_x(t)
={}&\sum_{\rho=1/2+i\gamma}
 m_\rho\frac{(\gamma-x)^2}
 {[t+(\gamma-x)^2]^3}\\
 &-2\sum_{\Re\rho>1/2}m_\rho
 \Re\frac{[\rho-s_x]^2}
 {[t-(\rho-s_x)^2]^3}.
\end{aligned}
\]

The series is absolutely and locally uniformly convergent away from its poles.

## Radial-concavity criterion

Under RH the second sum is absent, so

\[
 \mathcal C_x(t)\ge0
\]

and indeed `C_x` is completely monotone in `t`.

If

\[
 \rho=\frac12+y+i\gamma,
 \qquad0<y<\frac12,
\]

is off the line, then at its own ordinate

\[
 \mathcal C_\gamma(t)
 \sim-\frac{2m_\rho y^2}{(t-y^2)^3}
 \quad(t\downarrow y^2,\ t>y^2).
\]

No other zero can cancel this pole. Hence

\[
 \mathrm{RH}
 \iff
 \mathcal C_x(t)\ge0
 \quad(x\in\mathbb R,\ 0<t<1/4).
\]

Equivalently, `J_x` is concave on `(0,1/4)` for every centre. The real unit-disc ray is already complete:

\[
 \mathrm{RH}
 \iff
 \mathcal A_x(w)\ge0
 \quad(x\in\mathbb R,\ 0<w<1).
\]

Unlike the preceding safe-line and heat criteria, the reverse implication requires no terminal-pair or threat-graph selection.

## First-Hermite connection

If `M(q,x)` is the first-Hermite zero-heat scalar of PR #379, then

\[
 \mathcal C_x(t)
 =\frac12\int_0^\infty q^2e^{-tq}M(q,x)\,dq.
\]

The chain is now

```text
first-Hermite heat
 -> Laplace transform
 -> radial xi curvature
 -> Taylor jet at t=1
 -> safe-line hierarchy
 -> Peano integral
 -> unit-disc Stieltjes/Pick function.
```

## Exact depth projector

The line kernel

\[
 K_t(u)=\frac{u^2}{(t+u^2)^3},
 \qquad a=\sqrt t,
\]

has Fourier transform

\[
 \widehat K_t(\ell)
 =\frac\pi{8a^3}
 (1+a|\ell|-a^2\ell^2)e^{-a|\ell|}.
\]

For one reflected pair of depth `d`, the centre integral is exactly

\[
 \int_{\mathbb R}
 -2\Re\frac{(d+iu)^2}{[t-(d+iu)^2]^3}\,du
 =\frac\pi{4t^{3/2}}
 \mathbf1_{d<\sqrt t}.
\]

Therefore a finite symmetric packet obeys

\[
 \frac{8t^{3/2}}\pi
 \int\mathcal C_{Z,x}(t)\,dx
 =N_0(Z)+2N_{<\sqrt t}^{\rm off}(Z).
\]

This is a sharp cumulative projector onto horizontal zero depth. It also proves a method firewall: the unweighted centre average is nonnegative even under false RH and therefore cannot close the pointwise problem.

## Exact Pick signature

For a right-side zero coordinate `z`, put

\[
 a=1-z^2,
 \qquad R=2mz^2/a^2.
\]

Its reflected-pair unit-disc block is

\[
 F_z(w)=\frac R{w-a}+\frac{\bar R}{w-\bar a}.
\]

The Pick kernel factors through

\[
 \begin{pmatrix}0&-R\\-\bar R&0\end{pmatrix},
\]

whose eigenvalues are `+|R|` and `-|R|`. Thus every complex off-line pair is exactly one hyperbolic Pick block of signature `(1,1)`.

At the matched ordinate the two poles coalesce into a negative rank-one Pick block. All continuous cut mass comes from critical-line zeros and is positive. This is the scalar unit-disc analogue of the Zeta23 signature decomposition.

## Unconditional annular penetration

The direct Euler expression is absolutely convergent only in `|w|<3/4`. Nevertheless any conventional zero-free region

\[
 \beta\le1-\eta(|\gamma|+3)
\]

implies

\[
 \mathcal A_x\text{ holomorphic in }
 |w|<3/4+\eta(2|x|+6)/2.
\]

A Vinogradov--Korobov region consequently gives an unconditional penetration of size

\[
 \gg
 [\log(|x|+3)]^{-2/3}
 [\log\log(|x|+3)]^{-1/3}
\]

past radius `3/4` at high centre. This proves that analytic continuation into the annulus is possible unconditionally; what remains is its Pick/concavity sign and cofinal continuation to radius one.

## Verification

The finite replay is resident at

```text
experiments/X-91004-radial-curvature-depth-projector/
```

and returns

```text
PASS_RADIAL_CURVATURE_DEPTH_PROJECTOR
```

It checks the Peano formula, curvature Taylor jet, Fourier polynomial identity, both sides of the sharp depth threshold, hyperbolic Pick eigenvalues, negative matched-pole Pick value and cubic curvature blow-up. The current replay uses only `mpmath` beyond the Python standard library.

It proves finite algebra and synthetic numerical controls only.

## Correct frontier

Closed here, subject to independent review:

```text
unit-disc generator = Peano integral of radial curvature;
safe-line hierarchy = normalized radial-curvature jet;
RH -> complete radial curvature monotonicity;
one off-line pair -> local negative curvature blow-up;
RH <=> radial xi concavity;
RH <=> positivity on the real unit-disc ray;
exact parabolic depth projector;
exact hyperbolic Pick block per off-line pair;
classical zero-free region -> annular holomorphy past 3/4.
```

Still open:

```text
unconditional prime-side radial concavity for 0<t<1/4;
pointwise elimination of every hyperbolic block;
cofinal Pick continuation through 3/4<|w|<1;
Riemann Hypothesis.
```
