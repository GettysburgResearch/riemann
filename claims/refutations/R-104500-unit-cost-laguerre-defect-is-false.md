# R-104500 — A unit-cost Laguerre-defect converse to Rolle is false

Claim ID: `R-104500`  
Status: **EXACT REFUTATION AND SHARP FACTOR-TWO CORRECTION**  
Created: 2026-08-22  
RH status: **unproved**

Let `f` be real on the real axis and write

\[
\mathcal L_f(t)=f'(t)^2-f(t)f''(t).
\]

At a simple critical point `c`,

\[
\mathcal L_f(c)=-f(c)f''(c).
\]

Thus `mathcal L_f(c)<0` exactly when `c` is a positive local minimum or a
negative local maximum.  Call such a point a **wrong extremum**.

The tempting inequality

\[
N_\mathbb R(f;I)
\ge N_\mathbb R(f';I)
   -\#\{c\in I:f'(c)=0,\ \mathcal L_f(c)<0\}
   -O(1)
\tag{R-104500.1}
\]

is false, even for very rigid real entire functions.

## 1. Polynomial counterexample

Take

\[
p(x)=x^4-2x^2+2.
\]

It has no real zero, while

\[
p'(x)=4x(x^2-1)
\]

has the three real zeros `-1,0,1`.  The points `-1` and `1` are positive
minima and hence wrong extrema, while `0` is a positive maximum and is not
wrong.  Thus the right side of (R-104500.1) grows as `3-2`, although the left
side is zero.

More importantly, the exact complex count is

\[
N_{\rm nr}(p)-N_{\rm nr}(p')=4=2\cdot2.
\]

The defect has coefficient two, not one.

## 2. Even Cartwright counterexample

Take

\[
f(z)=2+\cos z.
\]

This function is real and even on the real axis, entire of exponential type,
and has no real zero.  Its derivative

\[
f'(t)=-\sin t
\]

vanishes at every integer multiple of `pi`.  At even multiples,

\[
f=3,\qquad f''=-1,\qquad \mathcal L_f=3>0,
\]

whereas at odd multiples,

\[
f=1,\qquad f''=1,\qquad \mathcal L_f=-1<0.
\]

Only half of the derivative zeros are wrong extrema.  Therefore subtracting
one unit per wrong extremum leaves a linear excess, despite the parent having
no real zeros.

This counterexample already has the reality, parity, order-one and Cartwright
features often proposed as generic repairs.  They are insufficient.

## Binding correction

For a generic real polynomial, the exact conservation law is

\[
\boxed{
N_{\rm nr}(p)-N_{\rm nr}(p')
=2E(p),
}
\]

where `E(p)` is the number of wrong extrema.  On finite intervals the same
factor two survives, with two explicit endpoint defects.  These statements are
proved in `L-104500`.

The correct reverse-Rolle object is therefore not a unit-cost one-point defect.
It is a factor-two wrong-extremum charge together with adjacent critical-value
edges and boundary winding.
