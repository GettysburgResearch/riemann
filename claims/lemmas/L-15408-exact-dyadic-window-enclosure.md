# L-15408 — Finite rational splines enclose the universal window exactly

Claim ID: `L-15408`  
Title: The dyadic infinite-convolution prime window has a proof-grade finite spline and support-tail evaluator  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15405`; elementary probability convolution and polynomial splines  
Scope: directed evaluation of `F_*`, `G_*`, and notched variants  
Related counterexample candidates: none

## Finite and tail laws

Let

\[
 X=\sum_{j=1}^\infty2^{-j}U_j
 \tag{L-15408.1}
\]

be the random variable of `L-15405`, and split

\[
 X=X_N+T_N,
 \qquad
 X_N=\sum_{j=1}^N2^{-j}U_j,
 \qquad
 T_N=\sum_{j>N}2^{-j}U_j.
 \tag{L-15408.2}
\]

Then

\[
 0\le T_N\le2^{-N}.
 \tag{L-15408.3}
\]

Let `f_N` be the density of `X_N` and `nu_N` the probability law of `T_N`.
The exact density `f` satisfies

\[
\boxed{
 f(x)=\int_{[0,2^{-N}]}f_N(x-t)\,d\nu_N(t).}
 \tag{L-15408.4}
\]

Therefore

\[
\boxed{
 \inf_{t\in[0,2^{-N}]}f_N(x-t)
 \le f(x)\le
 \sup_{t\in[0,2^{-N}]}f_N(x-t).}
 \tag{L-15408.5}
\]

The same statement holds for every derivative order for which the finite spline
is classically differentiable across the interval in question; across knots use
the convex hull of all one-sided polynomial pieces.

## Convolution-square window

Let

\[
 Y=X+X',
 \tag{L-15408.6}
\]

where `X'` is an independent copy. Its density is

\[
 g=f*f.
 \tag{L-15408.7}
\]

Write

\[
 Y=Y_N+S_N,
 \qquad
 Y_N=X_N+X_N',
 \qquad
 0\le S_N\le2^{1-N}.
 \tag{L-15408.8}
\]

If `g_N=f_N*f_N`, then

\[
\boxed{
 \inf_{t\in[0,2^{1-N}]}g_N(y-t)
 \le g(y)\le
 \sup_{t\in[0,2^{1-N}]}g_N(y-t).}
 \tag{L-15408.9}
\]

The universal terminal window is

\[
 F_*(u)=g(u-2).
 \tag{L-15408.10}
\]

Thus every value needed by `T-15403` is enclosed through one finite rational
spline optimization on an interval of width `2^(1-N)`.

The pole-free window

\[
 G_*(u)=F_*(u)-2F_*(u-\log4)
 \tag{L-15408.11}
\]

is enclosed by preserving the two correlated spline intervals separately or by
building their exact common finite-spline representation before widening.

## Exact finite spline

Each `u_j` is a normalized box with dyadic rational width. Therefore `f_N` is a
compact spline of degree `N-1` with dyadic rational knots and rational
coefficients. One explicit formula is the generalized Irwin--Hall identity

\[
\boxed{
 f_N(x)=
 {2^{N(N+1)/2}\over(N-1)!}
 \sum_{S\subseteq\{1,\ldots,N\}}
 (-1)^{|S|}
 \left(x-\sum_{j\in S}2^{-j}\right)_+^{N-1}.}
 \tag{L-15408.12}
\]

For large `N`, a dynamic piecewise-polynomial convolution is preferable to the
exponential subset formula. Both are exact.

Similarly, `g_N` is a rational spline of degree `2N-1`; it may be constructed by
one further exact convolution or by treating the `2N` dyadic box variables
directly.

## Exact interval optimization

On a rational interval, a spline polynomial with rational coefficients has
extrema only at:

1. interval endpoints;
2. internal spline knots;
3. real roots of its derivative inside each polynomial cell.

A proof-producing evaluator may use:

- exact Sturm isolation of the derivative roots;
- rational interval Horner bounds on every isolator;
- Bernstein-basis range bounds with adaptive subdivision;
- exact derivative monotonicity when available.

The final window interval contains no unproved truncation approximation: the
entire infinite tail is represented by the convex probability average in
(L-15408.9).

## Self-similarity control

The distribution also satisfies

\[
 X\stackrel d={U+X'\over2},
 \tag{L-15408.13}
\]

where `U` is uniform on `[0,1]`. Consequently

\[
\boxed{
 f(x)=2\int_{\max(0,2x-1)}^{\min(1,2x)}f(t)\,dt.}
 \tag{L-15408.14}
\]

At interior points this yields

\[
 f'(x)=
 \begin{cases}
  4f(2x),&0<x<1/2,\\
  -4f(2x-1),&1/2<x<1.
 \end{cases}
 \tag{L-15408.15}
\]

Equations (L-15408.14)--(L-15408.15) give an independent recursive evaluator
and mutation check for the finite-spline producer.

## Notched variants

Finitely many notch boxes from `L-15406` simply prepend additional rational or
directed interval widths. The residual dyadic tail remains supported in
`[0,eta 2^-N]`. Thus the same finite-spline/tail enclosure applies, with a
larger but still exact knot set.

## Proof-producing schema

A window-value certificate binds:

1. truncation level `N`;
2. exact box widths and spline construction digest;
3. the rational target argument interval;
4. every intersected spline cell;
5. derivative-root or Bernstein range certificates;
6. the exact tail support width;
7. the final lower and upper window endpoints;
8. an independent self-similarity or Fourier-product spot check.

No floating inverse Fourier transform is part of the trust boundary.

## Wider meaning

The universal one-window RH criterion is not merely existential. Its fixed test
function has an exact, finitely checkable approximation architecture whose error
shrinks geometrically in support width.

This removes the main practical concern about using an infinite convolution in
a directed prime-power computation.

## Gap audit

- Formula (L-15408.12) is exact but computationally exponential; production
  should use dynamic spline convolution.
- Convex-hull bounds can be conservative near steep spline cells and may require
  larger `N`.
- Correlated evaluations at many prime arguments should share one spline proof
  object rather than independently widening the same coefficients.
- The lemma certifies window values, not the prime manifest or the RH-valid
  spectral moat.
