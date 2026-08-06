# L-9507 — Exact Bessel–Möbius decomposition of the semicircle observable

Claim ID: `L-9507`  
Title: Poisson summation converts the semicircle totient error into a Bessel transform of Möbius cancellation  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `T-9501`; Poisson summation for the compact semicircle kernel; elementary Möbius inversion  
Scope: direct analytic attack on the full RH-equivalent error term  
Related counterexample candidates: none

## Semicircle kernel

Let

\[
\kappa(u)=2\sqrt{1-u^2}\,\mathbf1_{|u|<1}.
\tag{L-9507.1}
\]

With the Fourier convention

\[
\widehat\kappa(\xi)
=\int_{\mathbb R}\kappa(u)e^{-2\pi i\xi u}\,du,
\]

one has

\[
\boxed{
\widehat\kappa(\xi)
=\frac{J_1(2\pi\xi)}{\xi},
\qquad
\widehat\kappa(0)=\pi.}
\tag{L-9507.2}
\]

Here `J_1` is the Bessel function of the first kind.

For every real `y>1`, Poisson summation gives the absolutely convergent identity

\[
\boxed{
\sum_{1\le m<y}2\sqrt{1-\frac{m^2}{y^2}}
=\frac{\pi y}{2}-1
+\sum_{\ell\ge1}\frac{J_1(2\pi\ell y)}\ell.}
\tag{L-9507.3}
\]

The endpoint causes no half-weight ambiguity because the semicircle kernel
vanishes at `|u|=1`.

## Möbius insertion

Use

\[
\frac{\varphi(n)}n
=\sum_{d\mid n}\frac{\mu(d)}d.
\tag{L-9507.4}
\]

Substitution into the finite observable of `T-9501` gives

\[
\mathcal V(x)
=\frac1x\sum_{d<x}\frac{\mu(d)}d
 \sum_{m<x/d}2\sqrt{1-\frac{d^2m^2}{x^2}}.
\tag{L-9507.5}
\]

Applying (L-9507.3) with `y=x/d` yields the exact decomposition

\[
\boxed{
\begin{aligned}
\mathcal V(x)-\frac3\pi
={}&-\frac\pi2\sum_{d\ge x}\frac{\mu(d)}{d^2}
-rac1x\sum_{d<x}\frac{\mu(d)}d\\
&+\frac1x\sum_{d<x}\frac{\mu(d)}d
 \sum_{\ell\ge1}
 \frac{J_1(2\pi\ell x/d)}\ell.
\end{aligned}}
\tag{L-9507.6}
\]

The first infinite tail is convergent absolutely; the Bessel series is
absolutely convergent for every fixed `x/d>0` because

\[
J_1(u)=O(u^{-1/2}).
\]

Equation (L-9507.6) is a direct full-problem attack surface: the elementary main
area has disappeared, and every remaining term is controlled by Möbius
cancellation against an explicit oscillatory Bessel kernel.

## Proof of the Poisson identity

The classical disk-section integral gives

\[
\int_{-1}^1 2\sqrt{1-u^2}\,e^{-2\pi i\xi u}\,du
=\frac{J_1(2\pi\xi)}\xi.
\]

Poisson summation at scale `y` gives

\[
\sum_{m\in\mathbb Z}\kappa(m/y)
=y\sum_{\ell\in\mathbb Z}\widehat\kappa(y\ell)
=\pi y+2\sum_{\ell\ge1}\frac{J_1(2\pi\ell y)}\ell.
\]

The left side is

\[
2+2\sum_{1\le m<y}2\sqrt{1-m^2/y^2}.
\]

Division by two proves (L-9507.3). The Möbius calculation is finite before the
last absolutely convergent Bessel expansion, so all rearrangements are
justified.

## RH-scale interpretation

Under the classical RH-equivalent Mertens estimate

\[
M(X)=\sum_{n\le X}\mu(n)
=O_\varepsilon(X^{1/2+\varepsilon}),
\tag{L-9507.7}
\]

partial summation gives

\[
\sum_{d\ge x}\frac{\mu(d)}{d^2}
=O_\varepsilon(x^{-3/2+\varepsilon}),
\]

and

\[
\frac1x\sum_{d<x}\frac{\mu(d)}d
=O_\varepsilon(x^{-3/2+\varepsilon}).
\]

The Bessel term is the remaining oscillatory transform of the same Mertens
measure. Summation by parts, using uniform bounds for the Bessel kernel and its
scale derivative, recovers the `T-9501` RH bound.

Conversely, `T-9501` proves that cancellation of the **combined** expression at
this scale already implies RH. It is therefore unnecessary, and potentially too
strong, to demand the three lines of (L-9507.6) satisfy the RH bound separately.

## Connection to Farey geometry

The factor `phi(n)` counts reduced residues of denominator `n`. The kernel is
the vertical chord of the unit disk. Thus `V(x)` is a smooth visible-lattice or
Farey discrepancy, and (L-9507.6) is its Möbius/Poisson dual.

This imports geometric and harmonic-analysis tools into the terminal-prime and
square-screw programs without changing the exact zeta-zero exponent.

## Gap audit

- Poisson summation must be used with the stated continuous compact kernel, not a sharp disk indicator.
- Bounding the three terms independently may lose cancellation present in the exact observable.
- Ordinary asymptotics for `J_1` do not by themselves prove the required uniform double-sum bound.
- The identity is exact, but the RH-scale estimate remains open.

## Suggested attack

1. Treat the inner Bessel series as one periodic/circle-problem kernel rather than termwise absolute values.
2. Apply a dyadic decomposition in `d` and `ell`, retaining the phase `2*pi*ell*x/d`.
3. Combine exponent-pair or spectral large-sieve estimates with explicit Mertens-energy bounds.
4. Compare the resulting exponent directly with the exact rightmost-zero exponent in `T-9501`, not merely with numerical decay.
