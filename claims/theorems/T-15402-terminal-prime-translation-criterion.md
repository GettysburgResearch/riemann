# T-15402 — Terminal-prime translation boundedness is equivalent to RH

Claim ID: `T-15402`  
Title: Pole-subtracted terminal von Mangoldt windows give a phase-aware RH criterion and an exponentially sensitive counterexample family  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: the smoothed von Mangoldt explicit formula; `L-15404`; elementary Laplace-transform theory for distributions supported on a half-line  
Scope: phase-aware moving-window criteria and endpoint Weil packets  
Related counterexample candidates: none

## The pole-subtracted logarithmic prime distribution

On `[0,infinity)`, define the distribution

\[
 d\mathcal T(t)
 =e^{-t/2}\,d\psi(e^t)-e^{t/2}\,dt,
 \qquad
 \psi(x)=\sum_{n\le x}\Lambda(n).
 \tag{T-15402.1}
\]

Equivalently,

\[
 d\mathcal T(t)
 =\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
   \delta_{\log n}(dt)-e^{t/2}\,dt.
 \tag{T-15402.2}
\]

For a real test function `F in C_c^infinity(0,infinity)`, define the translated
terminal-window functional

\[
\boxed{
 \mathcal D_F(a)
 =\langle\mathcal T,F(2a-\cdot)\rangle.}
 \tag{T-15402.3}
\]

Explicitly,

\[
\boxed{
\begin{aligned}
 \mathcal D_F(a)={}&
 \sum_{n\ge2}{\Lambda(n)\over\sqrt n}
 F(2a-\log n)\\
 &-e^a\int_0^\infty e^{-u/2}F(u)\,du,
\end{aligned}}
 \tag{T-15402.4}
\]

where only the finite terminal window selected by `supp F` contributes.

## Main equivalence

The following are equivalent.

1. The Riemann Hypothesis is true.
2. For every real `F in C_c^infinity(0,infinity)`,
   \[
    \boxed{\sup_{a\ge1}|\mathcal D_F(a)|<\infty.}
    \tag{T-15402.5}
   \]
3. The distribution `mathcal T` is translation bounded on the right: every
   compactly supported smooth convolution with `mathcal T` is bounded under
   positive translations.

Thus RH is equivalent to an order-one bound for every **fixed-shape relative
prime window** after subtracting only the zeta-pole main term.

## Laplace-transform proof of the converse

For `Re z>1/2`, the Laplace transform of (T-15402.2) is

\[
\begin{aligned}
 \mathcal L\mathcal T(z)
 &=-{\zeta'\over\zeta}\left(z+\frac12\right)
   -{1\over z-1/2}.
\end{aligned}
 \tag{T-15402.6}
\]

The second term cancels the pole of zeta at `s=1`.  Every nontrivial zero `rho`
produces a pole at

\[
 z=\rho-\frac12.
 \tag{T-15402.7}
\]

A right-translation-bounded distribution supported on a half-line has a
holomorphic Laplace transform throughout `Re z>0`.  Hence (T-15402.5) excludes
every zero with `Re rho>1/2`.  The functional equation excludes the reflected
left half, proving RH.

It is enough to test a fixed countable dense family of rational smooth profiles.
Indeed, if a pole is present, one may select a profile whose Laplace transform
is nonzero at that pole; the vanishing condition is one proper continuous
hyperplane in the test-function space.

## Smoothed explicit formula

Let

\[
 \widehat F_L(z)=\int_0^\infty e^{-zu}F(u)\,du.
 \tag{T-15402.8}
\]

The smoothed explicit formula gives, with the usual symmetric zero convention,

\[
\boxed{
\begin{aligned}
 \mathcal D_F(a)={}&
 -\sum_\rho
 e^{2a(\rho-1/2)}
 \widehat F_L(\rho-1/2)\\
 &-\sum_{m\ge1}
 e^{-2a(2m+1/2)}
 \widehat F_L(-2m-1/2).
\end{aligned}}
 \tag{T-15402.9}
\]

There is no `log(2 pi)` endpoint term because `F(2a-t)` is supported away from
`t=0` for all sufficiently large `a`.

Under RH, the first exponentials have modulus one.  Since the Laplace transform
of a smooth compactly supported function decays faster than every power on
vertical lines, while the zero counting function is `O(T log T)`, the zero sum
converges absolutely and uniformly in `a`.  This proves the forward implication
in (T-15402.5).

## Boundary Hankel specialization

For a real endpoint profile `phi` from `L-15404`, put

\[
 F=C_\phi=\phi*\phi
 \quad\hbox{on }[0,2R].
 \tag{T-15402.10}
\]

Its Laplace transform factors:

\[
\boxed{
 \widehat F_L(z)=\Phi_\phi(z)^2,
 \qquad
 \Phi_\phi(z)=\int_0^R e^{-zr}\phi(r)\,dr.}
 \tag{T-15402.11}
\]

The terminal prime contribution minus the leading polar channel is exactly

\[
 2\mathcal D_{C_\phi}(a)
 \tag{T-15402.12}
\]

up to the exponentially small second polar exponential and the fixed
small-prime overlap from `L-15404`.

By polarization, finite Hermitian packets of endpoint profiles recover
cross-convolutions

\[
 C_{\phi,\psi}(u)
 =\int\phi(u-r)\overline{\psi(r)}\,dr.
 \tag{T-15402.13}
\]

Finite sums of such convolutions are dense in the smooth test-function space.
Thus the endpoint-packet family is phase-complete for detecting failure of
(T-15402.5).

## False-RH growth and negative packets

If a zero

\[
 \rho=\beta+i\gamma,
 \qquad \beta>\frac12,
\]

is detected by a profile, its contribution is

\[
 -e^{2a(\beta-1/2)}
 e^{2ia\gamma}
 \widehat F_L(\rho-1/2)
 \tag{T-15402.14}
\]

plus its conjugate.  It therefore has exponentially growing oscillatory real
part.  By choosing a finite polarized profile packet and a sequence of supports
that fixes the phase, one obtains a strictly negative endpoint-packet quadratic
value whose magnitude dominates all polynomially growing archimedean and fixed
small-prime terms.

Consequently, under the standard explicit-formula normalization,

\[
\boxed{
 \text{RH false}
 \Longrightarrow
 \text{some finite endpoint packet has }q_a<0.}
 \tag{T-15402.15}
\]

This is an existential statement.  It does not supply the unknown support or
profile without locating the responsible pole.

## Computational significance

A certificate for one boundary packet needs:

1. an exact rational or dyadic profile basis;
2. the fixed small-prime prefix `log n<=R`;
3. the terminal window
   \[
    e^{2a-2R}\le n\le e^{2a};
   \]
4. the exact polar rank-one subtraction;
5. cancellation-safe archimedean integrals;
6. a frozen rational vector and a strict directed final interval.

No prime power in the middle range contributes.  The candidate matrix is a
pole-subtracted Hankel matrix, and its unstable directions are exactly the
phase information erased by scalar Barta.

## Wider interpretation

`L-15403` and the present theorem together give a sharp dichotomy.

```text
scalar local potential:
    exponentially negative and unusable;
phase-aware terminal Hankel block:
    pole cancels exactly, residual spectrum is the zeta-zero spectrum.
```

The scalar obstruction is therefore not merely a failed estimate.  It identifies
where the arithmetic spectral information resides.

## Proof boundary

- The explicit formula and every normalization require independent source-level
  review.
- Formula (T-15402.9) is stated for smooth compact profiles; nonsmooth window
  indicators need separate endpoint and growth budgets.
- Boundedness of finitely many windows is not RH.
- The equivalence is a new interface, not a proof of the boundedness condition.
- A negative midpoint in a terminal-prime matrix is not a certificate.
