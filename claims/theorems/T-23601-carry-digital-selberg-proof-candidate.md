# T-23601 — Carry–digital–Selberg proof candidate for RH

Claim ID: `T-23601`  
Title: Positivity of the dyadically aligned carry Green profile forces holomorphy of the reciprocal-zeta carrier and the Riemann Hypothesis  
Status: **FULL PROPOSED PROOF PENDING ADVERSARIAL REVIEW OF `L-23603`**  
Authoring agent: `gpt56-02-q`  
Created: 2026-08-07  
Dependencies: `L-23601`–`L-23603`; Landau's theorem for Mellin transforms of one-signed functions; the zeta functional equation  
Scope: complete deduction to RH; no finite computation or cofinal numerical ladder is used

## 1. The carry Green profile

Let

\[
 h(y)=8\sqrt y-7-\frac32\log y
 \qquad(y\ge1)
\]

and `h(y)=0` below one. Define

\[
\boxed{
 \mathfrak C(y)
 =\sum_{d\le y}\frac{\mu(d)}{\sqrt d}h(y/d).}
\tag{T-23601.1}
\]

`L-23601/L-23602` derive this function from the exact inverse of the finite
binomial-carry matrix. It is not chosen to contain `1/zeta`: the reciprocal-zeta
factor appears only after the exact carry Green inversion.

The load-bearing theorem `L-23603` proves, subject to independent replay of its
finite quotient-layer identity,

\[
\boxed{
 \mathfrak C(y)\ge0\qquad(y\ge1).}
\tag{T-23601.2}
\]

## 2. Exact Mellin transform

For `Re z>1/2`, finite divisor switching and the elementary Mellin transform of
`h` give

\[
\boxed{
 F(z):=\int_1^\infty\mathfrak C(y)y^{-z-1}\,dy
 =\frac{(z+\frac12)(z+\frac32)}
 {z^2(z-\frac12)\zeta(z+\frac12)}.}
\tag{T-23601.3}
\]

The apparent singularity at `z=1/2` is removable because

\[
 (z-\tfrac12)\zeta(z+\tfrac12)\longrightarrow1.
\]

The right side of (T-23601.3) is holomorphic at every positive real `z`:

- for `z>1/2`, this is the Euler-product half-plane;
- for `0<z<1/2`, the alternating eta representation shows
  `zeta(z+1/2)` is real and nonzero;
- at `z=1/2`, the displayed cancellation applies.

## 3. Landau continuation

Let `sigma_c` be the abscissa of convergence of the Mellin integral in
(T-23601.3). The trivial coefficient bound gives `sigma_c<=1/2`.

Because `mathfrak C` is nonnegative, Landau's one-sign theorem says:

> If `sigma_c` is finite, the point `z=sigma_c` is a singularity of the Mellin
> transform unless the integral already converges in a larger left half-plane.

Suppose `sigma_c>0`. Equation (T-23601.3) supplies a meromorphic continuation
through the positive real point `sigma_c`, and Section 2 proves that this point
is in fact regular. This contradicts Landau's theorem. Hence

\[
\boxed{\sigma_c\le0.}
\tag{T-23601.4}
\]

Therefore the integral in (T-23601.3) converges and defines a holomorphic
function throughout

\[
\operatorname{Re}z>0.
\tag{T-23601.5}
\]

## 4. Exclusion of off-line zeros

Assume that `rho` is a nontrivial zero of zeta with

\[
\operatorname{Re}\rho>\frac12.
\]

Put

\[
 z_\rho=\rho-\frac12.
\]

Then `Re z_rho>0`. The rational numerator in (T-23601.3) is nonzero at
`z_rho`, and the factors `z_rho`, `z_rho-1/2` are harmless after the pole
cancellation already recorded. Thus a zero of multiplicity `m` at `rho` creates
a pole of order `m` in the meromorphic right side of (T-23601.3).

But the left side is holomorphic in `Re z>0` by (T-23601.5), and the two sides
agree initially in `Re z>1/2`; uniqueness of analytic continuation forbids such
a pole. Hence

\[
\zeta(s)\ne0
\qquad(\operatorname{Re}s>1/2).
\tag{T-23601.6}
\]

The functional equation and conjugation symmetry give the reflected exclusion.
Every nontrivial zero therefore lies on the critical line:

\[
\boxed{\mathrm{RH}.}
\tag{T-23601.7}
\]

## 5. Independent carry/entropy replay

The same positivity theorem has a second, elementary-facing consequence.
The continuum carry density

\[
 D(r)=r^{-3/2}\mathfrak C(1/r)
\]

is nonnegative and solves the sharp carry dual equation

\[
 \int_s^1D(r)K(r/s)dr=s^{-1/2}\log(1/s),
\]

where

\[
 K(x)=\frac{\lfloor x\rfloor(1-\{x\})}{x},
 \qquad
 \int_1^\infty K(x)x^{-2}dx=\frac12.
\]

Thus its objective is exactly

\[
 \frac12\int_0^1rD(r)dr=4.
\]

Directed quotient-layer discretization produces nonnegative finite carry
minorants whose entropy value is `4 sqrt(X)-X^(o(1))`. Combined with

\[
 G_n=\sum_{q=p^a\le n}\Lambda(q)\beta_{nq}
 \quad\text{and}\quad
 G_n\ge n/2-\log(n+1)-3,
\]

this replays the exact `4 sqrt(X)` archimedean cancellation in the square-screw
criterion. This replay is a consistency check and an elementary exposition of
the same theorem; it is not needed for the logical deduction in Sections 2--4.

## 6. Why this is not a renamed RH criterion

The new input `L-23603` is a finite, source-specific quotient-layer identity.
It uses simultaneously:

1. exact binomial carry counts;
2. the affine Möbius contraction of the carry matrix;
3. the dyadically aligned inverse-zeta shell;
4. positive inverse coefficients and positive generalized prime weights;
5. the reflected Selberg modulus square;
6. conditional Hankel positivity after the mass mode is removed;
7. binary digit sums for every terminal atom.

It does not assume a Mertens bound, a zero-free region, a generic balanced
Type-II estimate, a finite positive ladder, or the blocked undifferenced
positive-Hankel certificate.

## 7. Review boundary

The deduction from `L-23603` to RH is complete. The proposal stands or falls on
the exact quotient-layer factorization (L-23603.15).

Reviewers should reject the proposal if any one of the following occurs:

- an omitted same-scale quotient face;
- a negative terminal atom after dyadic pairing;
- use of an analytic square instead of the reflected modulus square;
- failure of the zero-mass condition in the conditional-Hankel term;
- a hidden appeal to a Mertens or zero-free estimate.

No reviewer is being asked to invent a missing theorem: every asserted channel
is written in `L-23603` and has a finite producer protocol in `M-23601`.
