# Audit of `SH(L)` and exact difference-Selberg repair

Author: `gpt56-02-p`  
Date: 2026-08-07  
Branch: `agent/gpt56-02-p/215-prime-polygon-rh-attack`  
Status: **research report; RH not proved**

## Executive result

I attempted to complete the sole arithmetic hinge `SH(L)` of `T-21901` rather
than leave it to a reviewer.  The attempt found a structural obstruction.

Every globally positive Hankel test admissible for the centered Selberg adjoint
has a positive spectral representation supported in `s>1/2`.  Its adjoint image
therefore obeys

```text
0 <= L*F(y) <= exp(-y/2) L*F(0).
```

The constant coordinate of the finite Weil kernel is the stop-loss ramp

```text
2(1-y/L)_+,
```

which is still equal to `1` at `y=L/2`.  Any decomposition of this ramp into a
positive-Hankel adjoint plus a residual has residual size at least

```text
(1-2 exp(-L/4))/(1+exp(-L/4)) -> 1
```

at the pair of points `{0,L/2}`.

Thus the proposed construction in `T-21901`—positive exponential adjoints,
cellwise spline interpolation, and a vanishing local residual—cannot work.  The
residual necessarily retains a macroscopic copy of the scalar square-screw
kernel.  Proving its centered-prime pairing is `o(1)` is the full RH-sensitive
arithmetic theorem, not a routine endpoint estimate.

This does not invalidate the implication `SH(L) => RH`; it shows that the stated
positive-Hankel ingredients do not construct `SH(L)`.

## New exact repair

The correct way to introduce finite differences is to change the nonlinear
Selberg equation before taking a positive square.

For right translation `tau_h`, put

```text
Delta_h = I-tau_h,
mu_h    = Delta_h nu.
```

The exact commutator

```text
L tau_h = tau_h L+h tau_h
```

and convolution algebra give

```text
[L Delta_h+2h tau_h] mu_h+mu_h*mu_h=Delta_h^2 R.
```

The quadratic term is now the literal square of the same first-difference
measure.  No undifferenced `nu` remains.

For every `s>1/2`, the positive density

```text
m_(h,s)(u)
 =(1-exp(-hs))(s-1/2)^2
  /[(1-exp(-hu))^2(u-1/2)^2],  u>=s,
```

produces a completely monotone test

```text
f_(h,s)(y)=integral_s^infinity m_(h,s)(u) exp(-uy) du
```

satisfying exactly

```text
L_h* f_(h,s)=exp(-s y).
```

Pairing gives the positive energy identity

```text
M_h(s)+integral_s^infinity m_(h,s)(u) M_h(u)^2 du
 =integral_s^infinity m_(h,s)(u) R_h(u) du,
```

where

```text
M_h(s)=(1-exp(-hs))H(s),
R_h(s)=(1-exp(-hs))^2 R(s).
```

This is the exact square-preserving nonlinear identity underlying the
prime-only boundary difference and Haar routes.

## What remains

The repaired equation still does not prove RH.  Its positive exponential cone
controls real Laplace tests.  The remaining RH-bearing step is one of:

1. a conditionally positive adjoint for the actual finite-difference spline,
   with all annihilated moments proved;
2. a signed Type-II factorization converting the factor-ratio channel into a
   nonnegative square;
3. an all-order theorem promoting the real energy identities to the required
   Stieltjes/vertical-Hardy positivity.

These obligations are smaller and correctly typed, but none was proved in this
pass.

## Files

```text
claims/refutations/
  R-21903-positive-hankel-adjoint-decay-barrier.md

claims/lemmas/
  L-21906-difference-squared-centered-selberg-equation.md
  L-21907-positive-hankel-adjoints-for-difference-selberg.md
```

## Honest conclusion

A complete proof of RH was not obtained.  The attempted final hinge was not
merely unfinished; its advertised positive-Hankel construction has a precise
constant-coordinate decay obstruction.  The difference-squared equation is a
genuine repair and should replace the old `SH(L)` construction in subsequent
work.
