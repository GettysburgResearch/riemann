# L-102742 — The carrier-quotiented defect is a root-free second-chaos Wick square

Claim ID: `L-102742`  
Status: **PROVED EXACT SOURCE FACTORIZATION**  
Created: 2026-08-23  
Depends on: `L-102741`  
RH status: **not assumed**

Retain the commuting finite-horizon operators

\[
L=\sum_\ell x_\ell,
\qquad
x_\ell=p_\ell^{-1/2}e^{-i\vartheta_\ell}U_\ell.
\]

The scalar Taylor remainder identity

\[
 e^{-x}-1+x
 =x^2\int_0^1(1-t)e^{-tx}\,dt
\]

is an exact identity in the finite commutative operator algebra. Therefore

\[
 \boxed{
 e^{-L}-1+L
 =L^2\int_0^1(1-t)e^{-tL}\,dt.
 }
 \tag{L-102742.1}
\]

Because all operators commute,

\[
 L^2e^{-tL}
 =\left(Le^{-tL/2}\right)^2.
\]

Define the root-free Wick field

\[
 \boxed{
 W_t:=Le^{-tL/2}.
 }
 \tag{L-102742.2}
\]

Its constant coefficient is zero for every \(t\). Combining (L-102742.1)
with `L-102741` gives

\[
 \boxed{
 \mathcal D_{\ge2}
 =RS\int_0^1(1-t)W_t^2\,dt
 +(R-1)S.
 }
 \tag{L-102742.3}
\]

Thus, after one exact prime-carrier quotient, the only critical part of the
native-completion defect is a continuous average of **squares of one root-free
labelled field**. The remaining gauge term `(R-1)S` begins at squared activity
and has polylogarithmic source norm.

## 1. Diagonal and distinct-prime pieces

Writing

\[
L^2
 =\sum_\ell x_\ell^2
 +2\sum_{\ell<k}x_\ell x_k,
\tag{L-102742.4}
\]

shows explicitly that:

```text
repeated-label diagonal:
  activity p^{-1} on the shift p^2;

distinct-label second chaos:
  activity (pq)^{-1/2} on the shift pq.
```

The two labelled copies of `67` remain distinct until final physical collapse.
The diagonal belongs to the already subcritical prime-power/squared gauge. The
conclusion-bearing geometry is the distinct-label component together with the
higher native factors contained in `exp(-tL)`.

## 2. Relation to the half-divisor current

The half-divisor geodesic of `L-102707` and the Wick field `W_t` are two
root-free gauges of the same carrier-quotiented defect. Their endpoint source
is identical, and the gauge transfer begins at squared activity. Therefore an
exact source partition may use:

```text
Wick gauge:
  chaos degree, prime-carrier quotient and free labelled energy;

half-divisor gauge:
  ratio-four physical factorization and balanced cross-owner geometry.
```

No source term or positive reserve is duplicated.

## Boundary

The square in (L-102742.3) is a square in the labelled convolution algebra. It
is not automatically a nonnegative scalar after the fixed signed outer-ray
observation or after one-dimensional physical collapse. The free and
same-product costs are addressed in `L-102743`; distinct-product physical
restriction remains arithmetic.