# L-105510 — Boundary-tame triangular polynomial Wick congruence

Claim ID: `L-105510`  
Status: **PROVED EXACT IN A FINITE NILPOTENT SOURCE ALGEBRA**  
Created: 2026-08-24  
Depends on: `L-105320`, `L-105500`

## 1. Finite source algebra

Let `A` be a finite-dimensional commutative unital algebra over `R` or `C`,
let `x in A` be nilpotent, and let `ell:A->C` be a linear functional.  Define
the symmetric Frobenius-type form

\[
B_R(u,v)=\ell\!\left((1-x)^{-1}uv\right),
\qquad
(1-x)^{-1}=\sum_{j\ge0}x^j,
\tag{L-105510.1}
\]

where the sum is finite by nilpotence.

Put

\[
\boxed{P_2(x)=1-\frac{x}{2}-\frac{x^2}{8}.}
\tag{L-105510.2}
\]

Because `P_2(x)=1+n` with `n` nilpotent, `P_2(x)` is a unit of `A`.  Thus
multiplication by `P_2(x)` is an invertible change of source coordinates and
preserves the inertia of every real Hermitian realization of `B_R`.

## 2. Exact cancellation identity

Direct expansion gives

\[
P_2(x)^2=1-x+\frac{x^3}{8}+\frac{x^4}{64}.
\tag{L-105510.3}
\]

Therefore, in the finite nilpotent algebra,

\[
\boxed{
\frac{P_2(x)^2}{1-x}
=
1+\frac{x^3}{8}
+\frac9{64}\sum_{m\ge4}x^m.
}
\tag{L-105510.4}
\]

Both degree one and degree two vanish exactly, and every remaining source
degree is nonnegative.  Moreover

\[
\boxed{
B_R(P_2u,P_2v)
=
\ell\!\left(
\left[1+\frac{x^3}{8}+\frac9{64}\sum_{m\ge4}x^m\right]uv
\right).
}
\tag{L-105510.5}
\]

Equation (L-105510.5) is an exact congruence, not a formal coefficient
comparison.

## 3. Why this is boundary-tame

The exponential factor in `T-105500` is globally zero-free but contains
`exp(-A_X^2/(4L^2))`, whose horizontal growth is a load-bearing open cost.
The present preconditioner uses only the identity, one source shift, and two
source shifts.  In a one-sided projected translation module all positive
translations are jointly nilpotent, so (L-105510.2) is automatically
invertible in the projected finite algebra and has no exponential boundary
growth.

This does **not** say that the scalar entire function
`1-A_X/(2L)-A_X^2/(8L^2)` is zero-free.  The congruence is algebraic and
triangular after source projection.

## 4. Actual-contour interface

To use (L-105510.5) for Xi, one must prove that the chosen smooth one-sided
Paley--Wiener frame realizes the projected source multiplication as an
invertible coordinate change of the actual contour compression, with the
projection/taper edge and coefficient-freezing discrepancy `o(N_1)` in trace
and Hilbert--Schmidt norm.  This is `TRIEDGE105510`; it is not proved here.
