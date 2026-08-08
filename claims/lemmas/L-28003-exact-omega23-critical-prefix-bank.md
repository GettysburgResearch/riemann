# L-28003 — Exact critical prefix bank for the binary–ternary Euler source

Claim ID: `L-28003`  
Title: The positive inverse of the binary–ternary Euler source yields an exact finite hyperbola Calderón bank with critical-order conditioning  
Status: **PROPOSED COMPLETE EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-28002`; finite Dirichlet convolution and Hilbert-space algebra

## 1. Source and positive inverse

Retain

\[
\omega_{2,3}
=\mu*(\varepsilon-\delta_2)*(\varepsilon-\delta_3)
\]

and its positive inverse

\[
a_{2,3}(n)=(v_2(n)+1)(v_3(n)+1).
\]

They satisfy exactly

\[
\boxed{
\omega_{2,3}*a_{2,3}=\varepsilon.}
\tag{L-28003.1}
\]

For a real number `Y>1`, define the strict inverse prefix

\[
A_{<Y}(s)
=\sum_{1\le n<Y}\frac{a_{2,3}(n)}{n^s}.
\tag{L-28003.2}
\]

## 2. Exact finite hyperbola identity

Fix an integer `R>=2`.  Then

\[
\boxed{
\sum_{1\le d<R}
\frac{\omega_{2,3}(d)}{d^s}
A_{<R/d}(s)
=1.}
\tag{L-28003.3}
\]

Indeed, the coefficient of `m^-s` on the left is

\[
\sum_{dn=m\atop d<R,\ n<R/d}
\omega_{2,3}(d)a_{2,3}(n).
\]

The strict inequalities are equivalent to `m<R`.  Hence the coefficient is

\[
(\omega_{2,3}*a_{2,3})(m)
=\mathbf1_{m=1}
\]

for `m<R`, and no coefficient with `m>=R` occurs.

This is an exact finite identity.  There is no analytic remainder and no
infinite inverse.

## 3. Physical translation identity

Let

\[
(\tau_n f)(t)=f(t-\log n)
\]

on an `L2` space with values in an arbitrary Hilbert space.  Put

\[
\mathcal A_Y
=\sum_{1\le n<Y}
\frac{a_{2,3}(n)}{\sqrt n}\tau_n.
\tag{L-28003.4}
\]

Evaluating (L-28003.3) at `s=z+1/2` gives the exact operator identity

\[
\boxed{
I
=\sum_{1\le d<R}
\frac{\omega_{2,3}(d)}{\sqrt d}
\tau_d\mathcal A_{R/d}.}
\tag{L-28003.5}
\]

Every synthesis coefficient and every positive prefix is finite and declared.
The identity remains valid componentwise for Hilbert-valued fields and after
applying any derivative commuting with translations.

## 4. Critical-order observability

Define

\[
w_d=\frac{|\omega_{2,3}(d)|}{\sqrt d},
\qquad
W_R=\sum_{1\le d<R}w_d.
\tag{L-28003.6}
\]

Triangle inequality and weighted Cauchy--Schwarz in (L-28003.5) give

\[
\boxed{
\|f\|_2^2
\le
W_R\sum_{d<R}w_d
\|\mathcal A_{R/d}f\|_2^2.}
\tag{L-28003.7}
\]

If `pi_R(d)=w_d/W_R`, then

\[
\|f\|_2^2
\le W_R^2
\sum_{d<R}\pi_R(d)
\|\mathcal A_{R/d}f\|_2^2.
\tag{L-28003.8}
\]

The local Euler coefficients at `2` and `3` are `1,-2,1`; every other
nonzero prime exponent is squarefree.  Consequently

\[
\boxed{|\omega_{2,3}(n)|\le4.}
\tag{L-28003.9}
\]

Using

\[
\sum_{1\le n<R}n^{-1/2}<2\sqrt R,
\]

one obtains

\[
W_R<8\sqrt R.
\tag{L-28003.10}
\]

Therefore

\[
\boxed{
\|f\|_2^2
\le64R
\sum_{d<R}\pi_R(d)
\|\mathcal A_{R/d}f\|_2^2.}
\tag{L-28003.11}
\]

The same inequality holds for the `H1` norm.  The loss is exactly critical
order `R`, rather than an exponential, factorial, or unspecified inverse loss.

## 5. Finite-horizon collar

Let `chi_J` be the indicator of `[0,J]`, and suppose `f` is causal.  Every
translation occurring in one term of (L-28003.5) has total multiplicative delay

\[
dn<R.
\]

Thus

\[
[\tau_d\mathcal A_{R/d},\chi_J]f
\]

is supported in the explicit upper collar

\[
\boxed{
J<t<J+\log R.}
\tag{L-28003.12}
\]

There is no interior localization remainder.  The finite-horizon form of the
bank therefore consists of:

```text
complete interior observations
+ one upper collar of width log R.
```

This collar is exactly where a source-bound boundary recurrence must act; it
may not be discarded or called a lower-order term without an estimate.

## 6. Compatibility with the factor-eighteen source

The synthesis coefficients in (L-28003.5) are precisely `omega_(2,3)`.  By
`L-28002`, their pointwise binary–ternary carry image is supported in

\[
m\le n<18m-2,
\]

has a positive generalized-prime synthesis, and has an absolute carry-feature
Schur reserve.

Consequently the inversion side of `BTEBC` is now explicit:

```text
identity field
-> exact critical prefix bank
-> omega_(2,3) synthesis
-> finite factor-eighteen carry transition.
```

The remaining theorem is an **upper** estimate for the bank observations in the
correct independent-frequency physical block, together with its endpoint
collar.  No infinite source inversion remains.

## 7. Why the bank does not itself prove RH

Equation (L-28003.11) is a lower observability inequality.  It does not bound the
prefix observations.  Applying triangle inequality again to those observations
would reintroduce the reciprocal-zeta source and lose the required signs.

A full proof must show that the weighted bank observation energy decomposes as

```text
nonnegative generalized-prime carry transition
+ strict physical reserve
+ lower-scale source outputs
+ a controlled upper collar.
```

This is the production content of `BTEBC`.

## 8. Proof boundary

Closed exactly or elementarily:

1. finite hyperbola reconstruction of the identity;
2. the physical translation bank;
3. critical `O(R)` observability;
4. finite-horizon collar support;
5. compatibility with the compact binary–ternary Euler source.

Open:

1. the physical upper estimate for the bank observations;
2. the strict source-image boundary recurrence;
3. RH.
