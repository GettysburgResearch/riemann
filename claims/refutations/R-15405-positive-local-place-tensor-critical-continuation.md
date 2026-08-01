# R-15405 — The positive Jordan tensor cannot continue through the critical Mellin boundary

Claim ID: `R-15405`  
Title: The zeta pole is canceled only in an indefinite archimedean channel, so the naive positive isometry diverges  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: `L-15425`, `L-15426`; the pole of zeta at one  
Scope: exact obstruction to the requested direct positive Mellin/continuum intertwiner  
Related counterexample candidates: none

## Boundary point

Fix `omega>0` and put

\[
 u_0=1+\omega.
 \tag{R-15405.1}
\]

The arithmetic feature norm from `L-15425` is

\[
 A_\omega(u)
 ={\zeta(u-\omega)\over\zeta(u+\omega)}.
 \tag{R-15405.2}
\]

As `u` tends to `u_0` from the right,

\[
 \boxed{
 A_\omega(u)
 ={1\over\zeta(1+2\omega)}{1\over u-u_0}+O(1).}
 \tag{R-15405.3}
\]

Thus the positive Jordan coherent feature has unbounded norm.

## Exact archimedean zero

Let

\[
 B_\omega(u)=\widehat b_\omega(u)
 =\pi^\omega
 {\Gamma((u-\omega)/2+1)
  \over\Gamma((u+\omega)/2+1)}.
 \tag{R-15405.4}
\]

At `u_0`, put

\[
 B_0=B_\omega(u_0)
 =\pi^\omega{\Gamma(3/2)\over\Gamma(3/2+\omega)}.
 \tag{R-15405.5}
\]

Equations `L-15426.14`--`L-15426.15` give

\[
 \widehat b_\omega(u_0)
 =\widehat v_\omega(u_0)=B_0,
 \tag{R-15405.6}
\]

\[
 \widehat g_\omega(u_0)=0,
 \qquad
 \widehat\ell_\omega(u_0)=2B_0>0.
 \tag{R-15405.7}
\]

Moreover,

\[
 \boxed{
 \widehat g_\omega(u)
 ={B_0\over2\omega}(u-u_0)
 +O((u-u_0)^2).}
 \tag{R-15405.8}
\]

Therefore the signed scalar product has the finite limit

\[
 \boxed{
 \lim_{u\downarrow u_0}
 A_\omega(u)\widehat g_\omega(u)
 ={B_0\over2\omega\zeta(1+2\omega)}.}
 \tag{R-15405.9}
\]

But its positive Hilbert majorant diverges:

\[
 \boxed{
 A_\omega(u)\widehat\ell_\omega(u)
 ={2B_0\over\zeta(1+2\omega)}
  {1\over u-u_0}+O(1).}
 \tag{R-15405.10}
\]

## No positive-feature continuation

Suppose a Hilbert-valued map `a(u)` agreed with the Jordan--archimedean positive
feature of `L-15426` for `u>u_0` and extended locally boundedly through `u_0`.
Its squared norm would equal the left side of (R-15405.10) on an open interval,
which diverges. Such an extension is impossible.

The cancellation in (R-15405.9) occurs because the two positive archimedean
channels become equal at `u_0` and are subtracted in the Krein metric. It is not
an ordinary Hilbert-space cancellation.


## The regular arithmetic remainder is intrinsically signed

Write

\[
 q=u-u_0,
 \qquad
 a_n={J_{2\omega}(n)\over n^{1+2\omega}}.
 \tag{R-15405.11}
\]

For `q>0`,

\[
 A_\omega(u_0+q)
 =\sum_{n\ge1}a_ne^{-q\log n}.
 \tag{R-15405.12}
\]

The principal part is

\[
 {1\over\zeta(1+2\omega)q}
 =\int_0^\infty e^{-qt}
 {dt\over\zeta(1+2\omega)}.
 \tag{R-15405.13}
\]

Hence the regularized kernel `A_omega^reg` is the Laplace transform of

\[
 \boxed{
 d\nu_\omega(t)
 =\sum_{n\ge1}a_n\,\delta_{\log n}(dt)
 -{dt\over\zeta(1+2\omega)}.}
 \tag{R-15405.14}
\]

This measure is not positive: every open interval containing no logarithm of an
integer has strictly negative `nu_omega`-mass. By uniqueness of Laplace
transforms for locally finite measures of exponential order, the same scalar
regular remainder cannot be represented by a different positive measure.

Therefore scalar conditional expectation/Jensen cannot control the regularized
critical channel. A successful continuation must retain its signed discrepancy
inside a coupled operator, renewal, or boundary-tail energy.

## Consequence

The requested physical isometry cannot be obtained by tensoring:

1. the positive Jordan conditional-expectation dilation; and
2. a positive majorant of `g_omega`;

then taking a conventional Hilbert closure at the critical abscissa. A
boundary trace or equivalent renormalized quotient must perform the pole-zero
cancellation before the physical norm is taken.

## Scope

This refutes only the naive positive local-place tensor continuation. It does
not refute a nonlocal augmented-trace intertwiner. In fact `L-15427` identifies
the singular boundary channel that such an intertwiner must contain.
