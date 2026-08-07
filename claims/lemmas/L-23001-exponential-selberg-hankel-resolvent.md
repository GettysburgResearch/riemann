# L-23001 — Exponential Selberg–Hankel adjoint resolvent

Claim ID: `L-23001`  
Title: The centered Selberg operator has an explicit completely monotone adjoint inverse on every exponential test  
Status: **PROPOSED — COMPLETE ABSTRACT PROOF; ZETA NORMALIZATION MUST BE MATCHED TO PR #216**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: the centered logarithmic-prime Riccati identity of PR #216 (`L-21503`); elementary distributional integration by parts  
Scope: real signed measures for which the displayed pairings converge; rigorous first on compact truncations, then by monotone/dominated exhaustion

## 1. Centered Selberg operator

Let

\[
 dP_0(x)=e^{x/2}\mathbf 1_{x\ge0}\,dx
\]

and define

\[
 \mathscr L\nu=y\,d\nu+2dP_0*d\nu.
\]

For a sufficiently decaying test function `f`, the adjoint is

\[
 \boxed{
 (\mathscr L^*f)(y)
 =y f(y)+2\int_0^\infty f(x+y)e^{x/2}\,dx.}
 \tag{L-23001.1}
\]

Suppose the exact centered Selberg equation is

\[
 \boxed{
 \mathscr L\nu+\nu*\nu=R.}
 \tag{L-23001.2}
\]

No positivity of `nu` is assumed.

## 2. Explicit positive resolvent

Fix

\[
 \lambda>\frac12
\]

and put

\[
 \boxed{
 w_\lambda(s)
 =\mathbf 1_{s\ge\lambda}
 \left({\lambda-1/2\over s-1/2}\right)^2.}
 \tag{L-23001.3}
\]

Define

\[
 \boxed{
 f_\lambda(y)
 =\int_\lambda^\infty e^{-sy}w_\lambda(s)\,ds.}
 \tag{L-23001.4}
\]

The integral is finite also at `y=0`, because

\[
 \int_\lambda^\infty w_\lambda(s)\,ds=\lambda-\frac12.
\]

The function `f_lambda` is completely monotone. More precisely,

\[
 \boxed{
 f_\lambda(x+y)
 =\int_\lambda^\infty
 w_\lambda(s)e^{-sx}e^{-sy}\,ds,}
 \tag{L-23001.5}
\]

so its Hankel kernel is a literal positive Gram kernel.

## 3. Exact adjoint identity

In distributions on the `s`-half-line,

\[
 \boxed{
 w_\lambda'(s)+{2\over s-1/2}w_\lambda(s)
 =\delta_\lambda(s).}
 \tag{L-23001.6}
\]

Indeed, the classical derivative above `lambda` is

\[
 -{2\over s-1/2}w_\lambda(s),
\]

and the unit jump at `lambda` contributes `delta_lambda`.

Using

\[
 y e^{-sy}=-\partial_s e^{-sy}
\]

and integrating by parts in (L-23001.4), equations (L-23001.1) and (L-23001.6) give

\[
 \boxed{
 \mathscr L^*f_\lambda(y)=e^{-\lambda y}.}
 \tag{L-23001.7}
\]

This is an exact inverse formula, not an asymptotic parametrix.

## 4. Positive Selberg energy identity

Pair (L-23001.2) with `f_lambda`. Equations (L-23001.5) and (L-23001.7) yield

\[
 \boxed{
 \begin{aligned}
 \int_0^\infty e^{-\lambda y}\,d\nu(y)
 &+\int_\lambda^\infty w_\lambda(s)
   \left|\int_0^\infty e^{-sx}\,d\nu(x)\right|^2ds\\
 &=\langle R,f_\lambda\rangle.
 \end{aligned}}
 \tag{L-23001.8)
\]

For real `nu`, the quadratic term is nonnegative. Consequently

\[
 \boxed{
 \int e^{-\lambda y}\,d\nu(y)
 \le\langle R,f_\lambda\rangle.}
 \tag{L-23001.9}
\]

In Laplace notation

\[
 H(s)=\int e^{-sy}\,d\nu(y),
 \qquad
 \widehat R(s)=\int e^{-sy}\,dR(y),
\]

Fubini gives the equivalent identity

\[
 \boxed{
 H(\lambda)
 +\int_\lambda^\infty w_\lambda(s)H(s)^2ds
 =\int_\lambda^\infty w_\lambda(s)\widehat R(s)ds.}
 \tag{L-23001.10}
\]

This is the positive real-axis energy hidden inside the Selberg Riccati equation.

## 5. Matrix-valued extension

Let `nu` take values in a finite-dimensional real Hilbert space and replace
`nu*nu` by the symmetric tensor convolution paired against a scalar test. Then
(L-23001.8) becomes

\[
 \int e^{-\lambda y}\,d\nu(y)
 +\int_\lambda^\infty w_\lambda(s)
   H(s)^*H(s)\,ds
 =\langle R,f_\lambda\rangle,
\]

in Loewner order. Thus the construction composes directly with finite profile,
Schur, and prime-pair packets after one common normalization is fixed.

## 6. What the lemma accomplishes

The lemma supplies, without a numerical solve:

1. a dimension-free positive Hankel test family;
2. an exact adjoint inverse for every real exponential;
3. a one-sided Selberg inequality retaining the complete quadratic prime-pair
   term;
4. a real-axis energy representation naturally aligned with the proposed
   complete-monotonicity route on PR #218.

It therefore closes the *abstract positive-adjoint construction problem* for
exponential tests.

## 7. What it does not accomplish

The dyadic stop-loss row

\[
 (T-y)_+
\]

is not a positive mixture of exponentials. Passing from (L-23001.8) to the
pointwise dyadic transport margin requires a signed exponential synthesis or a
two-sided correlation estimate. That is the critical gate isolated in
`L-23002` and `R-23001`.

The lemma by itself does not prove a cofinal prime bound or RH.

## 8. Proof boundary

- The algebra of (L-23001.3)--(L-23001.10) is exact.
- A repository integration must independently match the signs and the
  `s -> s+1/2` shift in PR #216.
- Complex vertical-line tests do not inherit the scalar Hankel square: the
  analytic convolution produces `H(z)^2`, whereas Hardy energy requires
  `|H(z)|^2`. A reflected/two-sided arithmetic correlation theorem is still
  necessary.
