# L-23704 — Four-band logarithmic renewal kernel

Claim ID: `L-23704`  
Title: The sharp constant four is a conserved critical Mellin mass of the outer carry frame  
Status: `PROPOSED — COMPLETE CONTINUUM REDUCTION; POSITIVE RENEWAL OPEN`  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Scope: continuum scaling model for `L-23703`  
Depends on: `L-23703`, elementary Mellin calculus

## 1. Explicit outer profile

For `1/5<y<=1`, put

\[
r(y)=\left\lfloor\frac1y\right\rfloor
\tag{L-23704.1}
\]

and

\[
U(y)=y^{-1/2}
\sum_{k\le r(y)}\frac{\mu(k)}{\sqrt k}
 \log\frac1{ky}.
\tag{L-23704.2}
\]

Define

\[
S(y)=\frac{yU(y)+\int_y^1U(t)dt}{y^2},
\qquad
\phi(y)=-yS'(y).
\tag{L-23704.3}
\]

The calculation in `L-23703` gives

\[
\phi(y)\ge0
\qquad(1/5<y<1),
\tag{L-23704.4}
\]

with piecewise elementary formulas on the four intervals

\[
\left(\frac1{r+1},\frac1r\right],
\qquad r=1,2,3,4.
\]

This is the scaling density of `T^{3/2}c_T(floor(yT))` in the outer region.
Moreover,

\[
S(y)=\int_y^1\frac{\phi(t)}{t}dt.
\tag{L-23704.5}
\]

## 2. Continuum carry kernel

For `0<x<=y<=1`, let

\[
a=\left\lfloor\frac yx\right\rfloor,
\qquad
B(y,x)=\frac{a((a+1)x-y)}{y}.
\tag{L-23704.6}
\]

This is the scale limit of `beta_(floor(yT),floor(xT))` away from quotient
boundaries.

Let

\[
\phi_r(y)=\phi(y)
\mathbf1_{(1/(r+1),1/r]}(y)
\tag{L-23704.7}
\]

and define the four coverage kernels

\[
b_r(x)=\int_x^1\phi_r(y)B(y,x)dy.
\tag{L-23704.8}
\]

Passing to logarithmic scale,

\[
k_r(v)=e^{-v/2}b_r(e^{-v}),
\qquad v\ge0.
\tag{L-23704.9}
\]

Because the four outer bands are the complete inverse whenever `x>1/5`,

\[
\boxed{
\sum_{r=1}^{4}k_r(v)=v
\qquad(0\le v<\log5).}
\tag{L-23704.10}
\]

For `v>=log5`, the kernels are the positive lower-scale spill that must be
recombined rather than discarded.

## 3. Entropy masses and Mellin conservation

Define the leading binomial-entropy mass of the band by

\[
h_r=\frac12\int_{1/(r+1)}^{1/r}y\phi(y)dy>0.
\tag{L-23704.11}
\]

The continuum cumulative carry operator acting on `S` has Mellin symbol,
initially for `Re s>1`,

\[
\widehat{\mathcal D S}(s)
 =\zeta(s)\frac{s-1}{s}\widehat S(s+1).
\tag{L-23704.12}
\]

By (L-23704.5),

\[
\widehat S(s+1)=\frac{\widehat\phi(s+1)}{s+1},
\]

so the coefficient-density form is

\[
\widehat b(s)
 =\zeta(s)\frac{s-1}{s(s+1)}\widehat\phi(s+1).
\tag{L-23704.13}
\]

At `s=1`, the pole of `zeta(s)` cancels `s-1`, giving

\[
\widehat b_r(1)=\frac12\widehat\phi_r(2)=h_r.
\]

Equivalently,

\[
\boxed{
\int_0^\infty e^{-v/2}k_r(v)dv=h_r.}
\tag{L-23704.14}
\]

This identity can also be checked directly by Fubini from
(L-23704.6)--(L-23704.9).

## 4. Why the constant is exactly four

Let `lambda_r` be nonnegative measures on `[0,infinity)`. Suppose they solve the
positive phase-renewal equation

\[
\boxed{
\sum_{r=1}^{4}(k_r*\lambda_r)(v)=v
\qquad(v\ge0).}
\tag{L-23704.15}
\]

Taking the Laplace transform at the critical exponent `1/2` and using
(L-23704.14) gives

\[
\boxed{
\sum_{r=1}^{4}h_r
 \int_0^\infty e^{-u/2}d\lambda_r(u)
 =\int_0^\infty ve^{-v/2}dv
 =4.}
\tag{L-23704.16}
\]

More generally, if the left side of (L-23704.15) is a minorant and the residual
is `R(v)>=0`, then the entropy deficit is exactly

\[
\boxed{
4-\sum_rh_r\int e^{-u/2}d\lambda_r(u)
 =\int_0^\infty R(v)e^{-v/2}dv.}
\tag{L-23704.17}
\]

Thus the leading constant is not fitted numerically and is not imported from the
prime number theorem. It is forced by one conserved Mellin mass of the carry
operator.

## 5. The open positive-renewal statement

The missing assertion is not ordinary scalar renewal with the four bands tied
together. The scalar outer kernel equals `v` on `[0,log5)` but has an oscillatory
positive spill afterward, and its inverse renewal measure need not be positive.

The proposed repair is the **four-input phase renewal** (L-23704.15), or a
minorant whose residual has critical mass tending to zero. Independent band
weights allow corrections to enter at the four quotient phases before the next
`log5` scale transition.

This is the continuum form of the finite phase-frame theorem in `T-23701`.

## 6. Proof boundary

The definitions, local identity (L-23704.10), Mellin symbol, and critical-mass
identity are proposed complete elementary calculations. Existence of the
nonnegative measures in (L-23704.15), or of asymptotically sharp finite-horizon
minorants, is open and is the load-bearing new theorem.
