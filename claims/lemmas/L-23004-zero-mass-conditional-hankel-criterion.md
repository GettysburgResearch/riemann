# L-23004 — Zero-mass conditional Hankel criterion

Claim ID: `L-23004`  
Title: A completely monotone second derivative gives a positive Hankel quadratic on every zero-mass measure, but the compact stop-loss adjoint fails through a negative terminal atom  
Status: **PROPOSED — COMPLETE ABSTRACT PROOF AND EXACT SCOPE TEST**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: `R-23001`; elementary Bernstein representation  
Scope: the difference-squared Selberg continuations of PR #219

## 1. Conditional Hankel positivity

Let `f` be a real distribution on `[0,infinity)` whose second derivative is
completely monotone in the sense

\[
\boxed{
 f''(u)=\int_0^\infty e^{-su}\,d\rho(s),
 \qquad \rho\ge0,}
\tag{L-23004.1}
\]

with the integrability required below.  Integrating twice gives

\[
 f(u)=a+bu+
 \int_0^\infty
 {e^{-su}-1+su\over s^2}\,d\rho(s),
\tag{L-23004.2}
\]

with the usual limiting convention at `s=0`.

Let `mu` be a finite real signed measure satisfying

\[
 \int d\mu=0.
\tag{L-23004.3}
\]

The affine terms in (L-23004.2) vanish from the Hankel quadratic:

\[
 \iint [a+b(x+y)]\,d\mu(x)d\mu(y)=0.
\]

The remaining term gives

\[
\boxed{
 \iint f(x+y)d\mu(x)d\mu(y)
 =\int_0^\infty
 {\left|\int e^{-sx}d\mu(x)\right|^2\over s^2}
 \,d\rho(s)
 \ge0.}
\tag{L-23004.4}
\]

Thus `f(x+y)` need not be positive Hankel on arbitrary vectors.  It is enough
that `f''` be completely monotone when the nonlinear measure has zero total
mass.

More generally, if the first `m` moments of `mu` vanish and `f^(2m)` is
completely monotone, repeated integration gives the corresponding conditional
Hankel square.

## 2. Relevance to the differenced Selberg equation

For

\[
 \mu_h=(I-\tau_h)\nu,
\]

the formal total mass is zero on every compact truncation whose boundary terms
are retained.  The closed equation of PR #219 has nonlinear term

\[
 \mu_h*\mu_h.
\]

Therefore the correct search cone is larger than the globally positive-Hankel
cone of `L-23001/L-21907`: a conditionally positive test satisfying
(L-23004.1) would retain a nonnegative nonlinear square.

This removes one artificial restriction from the continuation.

## 3. Exact test of the compact stop-loss adjoint

Let `f_T` be the exact compact adjoint from `R-23001` for the sign required to
lower-bound

\[
 k_T(y)=(T-y)_+.
\]

That refutation proves

\[
 f_T(y)=-{T-y\over T}+O((T-y)^2)
 \qquad(y\uparrow T),
\tag{L-23004.5}
\]

and `f_T(y)=0` for `y>T`.  Consequently

\[
 f_T'(T-)=\frac1T,
 \qquad
 f_T'(T+)=0.
\]

The distributional second derivative therefore contains the atom

\[
\boxed{
 -{1\over T}\delta_T.}
\tag{L-23004.6}
\]

A completely monotone distribution is a positive measure after every required
Laplace differentiation and cannot contain this negative atom.  Hence

\[
\boxed{
 f_T''\text{ is not completely monotone}.}
\tag{L-23004.7}
\]

The exact compact stop-loss adjoint fails not only global Hankel positivity but
also the natural zero-mass conditional Hankel cone.

## 4. Surviving opportunity

The failure is specific to the undifferenced stop-loss target.  It does not
rule out a conditionally positive adjoint for:

- a higher finite difference of the stop-loss ramp;
- the exact prime-only safe spline;
- a matrix combination whose negative terminal atoms cancel;
- a noncompact test with an explicitly controlled arithmetic tail.

A genuine completion must write the exact target in one of those forms and
verify the moment cancellations and the sign of the highest derivative measure.

## 5. Proof boundary

- The conditional-square identity is exact.
- The negative terminal atom is exact.
- No conditionally positive adjoint for the actual critical prime/Möbius target
  is constructed here.
- RH remains unproved.
