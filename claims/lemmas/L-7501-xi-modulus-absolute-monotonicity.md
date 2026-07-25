# L-7501 — Direct xi-modulus absolute monotonicity

Claim ID: L-7501  
Title: Under RH, the horizontal completed-xi modulus is absolutely monotone in squared distance  
Status: PROPOSED  
Authoring agent: `gpt56-01-g`  
Created: 2026-07-25  
Dependencies: the standard completed `xi` normalization and its functional equation  
Scope: division-free finite RH counterexample witnesses  
Related counterexample candidates: none

## Definition

Use

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

For a real ordinate `T`, define first in the variable `z`

\[
 F_T(z)=\xi\!\left(\frac12+z+iT\right)
        \xi\!\left(\frac12-z+iT\right).
\]

The function `F_T` is even and entire, so there is a unique entire function
`H_T` satisfying

\[
 H_T(z^2)=F_T(z).
\]

For real `x`, the functional equation and conjugation give

\[
 \boxed{
 H_T(x^2)=
 \left|\xi\!\left(\frac12+x+iT\right)\right|^2.}
\]

## Statement

Assume RH.  Then for every real `T`:

1. every zero of `H_T` is real and nonpositive;
2. `H_T` has order at most `1/2` and a genus-zero factorization
   \[
   H_T(u)=C_Tu^{m_T}
   \prod_{\gamma\ne T}
   \left(1+\frac{u}{(T-\gamma)^2}\right)^{m_\gamma},
   \qquad C_T>0,
   \]
   where `1/2+i gamma` runs over the nontrivial zeros with multiplicity and
   `m_T` is the multiplicity at `u=0`;
3. `H_T` is absolutely monotone on `[0,infinity)`:
   \[
   H_T^{(n)}(u)\ge0
   \qquad(n\ge0,\ u\ge0);
   \]
4. for every strictly increasing nonnegative rational node list
   `u_0<...<u_n`,
   \[
   \boxed{[u_0,\ldots,u_n]H_T\ge0.}
   \]

Consequently, either of the following finite directed inequalities disproves RH:

\[
 H_T(v)<H_T(u),\qquad 0\le u<v,
\]

or, more generally,

\[
 [u_0,\ldots,u_n]H_T<0.
\]

The two-point form needs only two direct completed-`xi` balls and no division by
`xi`, logarithmic derivative, derivative jet, or zero-exclusion denominator.

## Proof

### Entire descent from `z` to `u=z^2`

The product defining `F_T` is entire. Replacing `z` by `-z` exchanges its two
factors, so `F_T` is even. Its Taylor series therefore contains only even
powers,

\[
 F_T(z)=\sum_{n\ge0}a_nz^{2n}.
\]

The series

\[
 H_T(u)=\sum_{n\ge0}a_nu^n
\]

is entire and is the unique function with `H_T(z^2)=F_T(z)`.

For real `x`,

\[
 \xi\!\left(\frac12-x+iT\right)
 =\xi\!\left(1-\left(\frac12-x+iT\right)\right)
 =\xi\!\left(\frac12+x-iT\right)
 =\overline{\xi\!\left(\frac12+x+iT\right)},
\]

which proves the modulus-square identity.

### Order and zeros

The completed `xi` function is entire of order one. Hence `F_T` has order at
most one as a function of `z`. Since `F_T(z)=H_T(z^2)`, maximum-modulus growth
shows that `H_T` has order at most `1/2`.

A zero of `F_T` occurs when one factor is a nontrivial zero `rho` of `xi`. Its
associated `H_T` zero is

\[
 u_\rho=\left(\rho-\frac12-iT\right)^2.
\]

Under RH, `rho=1/2+i gamma`, so

\[
 u_\rho=-(T-\gamma)^2\le0.
\]

The local zero multiplicity descends unchanged from the paired roots in `z` to
the corresponding root in `u`.

An entire function of order strictly below one has a genus-zero canonical
product and no nonconstant exponential factor. Moreover,

\[
 \sum_{|\gamma|\to\infty}\frac1{(T-\gamma)^2}<\infty
\]

by the usual local zero-count estimate. Factoring a possible zero at `u=0`
gives the displayed product. Its constant is positive because the
modulus-square identity implies `H_T(u)>0` for every `u>0` under RH.

### Absolute monotonicity

Every finite partial product

\[
 C_Tu^{m_T}\prod_{j=1}^{J}\left(1+\frac{u}{a_j}\right)^{m_j},
 \qquad a_j>0,
\]

is a polynomial with nonnegative coefficients. Every derivative is therefore
nonnegative on `[0,infinity)`.

The canonical product converges locally uniformly, and so do all derivatives
on compact sets. Taking the limit proves

\[
 H_T^{(n)}(u)\ge0.
\]

For distinct real nodes, the generalized mean-value theorem for divided
differences gives

\[
 [u_0,\ldots,u_n]H_T
 =\frac{H_T^{(n)}(\theta)}{n!}
\]

for some `theta` between the extreme nodes. This proves the hierarchy.

The counterexample implications are contrapositives.

## Existential completeness

Suppose RH is false. Zero symmetry supplies

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad \delta>0,
\]

with some multiplicity `m`. Put `T=gamma`. Then

\[
 H_\gamma(\delta^2)=0.
\]

Both symmetric xi factors vanish there, so locally

\[
 H_\gamma(u)=A(u-\delta^2)^{2m}\{1+o(1)\},
 \qquad A>0.
\]

Its derivative is strictly negative immediately to the left of `delta^2`.
Hence there are real `0<u<v<delta^2` with

\[
 H_\gamma(v)<H_\gamma(u).
\]

The inequality is strict and all functions are continuous in `(T,u,v)`, so it
persists on an open neighborhood. Dyadic `T` and dyadic positive `x_1<x_2` with
`u=x_1^2`, `v=x_2^2` are dense. Therefore every RH failure creates a finite
exact-point two-value witness of the displayed type.

This completeness statement is existential; it does not give the height or
width of the negative region.

## Certificate schema

A two-point proof object needs only:

1. exact dyadic `T`, `x_1`, and `x_2`, with `0<=x_1<x_2`;
2. directed complex rectangles for
   \[
   \xi(1/2+x_j+iT),\quad j=1,2;
   \]
3. outward rational intervals for each squared modulus;
4. an exact final interval for
   \[
   |\xi(1/2+x_2+iT)|^2-|\xi(1/2+x_1+iT)|^2
   \]
   whose upper endpoint is strictly negative;
5. evaluator, precision, point, and normalization fingerprints.

The checker requires no special function, floating point, or division.

## Numerical advantage

Near a hidden off-line zero, `xi'/xi` is singular. A proof-grade log-derivative
calculation must both exclude zero from the denominator and retain a negative
real-part margin. The modulus witness instead seeks the geometric dip itself.
Arbitrary-precision balls can represent the exponentially small completed-xi
scale without underflow, and any common positive factor depending only on `T`
may be applied to all horizontal samples without changing a sign comparison.

## Analytic domain audit

- `xi` is entire and its zeros are exactly the nontrivial zeta zeros.
- `F_T` and `H_T` are entire; no square-root branch occurs in `H_T` itself.
- Certificate inputs use exact nonnegative `x`, and reconstruct `u=x^2`
  algebraically.
- Under RH, no positive `u` is a zero of `H_T`.
- At a critical-line ordinate `T=gamma`, a zero at `u=0` is handled by the
  explicit factor `u^{m_T}`.
- The product convergence uses only the standard zero-count growth.

## Gap audit

1. A midpoint modulus reversal is not a certificate.
2. Squaring a complex rectangle must use the exact minimum/maximum of the real
   and imaginary square intervals; naive endpoint squaring is wrong when an
   interval crosses zero.
3. A separate normalization may be used only if it is a rigorously positive
   common factor independent of `x`.
4. The theorem depends on the standard xi functional equation and zero
   symmetries; implementations must bind the same normalization.
5. A positive finite scan says nothing outside its exact node family.

## Adversarial tests

- An on-line finite model `prod_j(u+a_j)`, `a_j>0`, must pass every divided
  difference.
- The off-line model `(u-d)^2(u+a)` must produce a negative first difference to
  the left of `d` while remaining nonnegative on `u>=0`.
- Rectangles crossing either coordinate axis must exercise the zero-containing
  square rule.
- Swapping the two horizontal points must reverse the final difference.
- Mutating the completed-xi normalization fingerprint must fail closed.

## Remaining uncertainty

No gap is known in the elementary entire-function reduction. Independent review
should verify the order-halving and multiplicity bookkeeping in the canonical
product before repository promotion.

## Suggested next attack

Extend the PR #56 Arb producer to retain direct completed-xi rectangles at the
same exact points. Start with adaptive two-point horizontal searches, then test
higher nonnegative divided differences only on basins where the two-point margin
is smallest.
