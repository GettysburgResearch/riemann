# L-105621 — The actual two-boundary Turán source is a strict contraction of the Xi current source

Claim ID: `L-105621`  
Status: **PROVED EXACT UNCONDITIONAL WEIGHTED-ENERGY THEOREM**  
Created: 2026-08-25  
Depends on: `L-105620`; `L-105260`; `L-106401`  
RH status: **not assumed**

## 1. Canonical one-sided source coordinates

Retain the notation of `L-105620`. Put

\[
j_h(\xi)=\widehat J_h(\xi),
\qquad
\lambda_2(\xi)=\Lambda_2(\xi).
\]

Define the decaying upper and reflected Turán source densities

\[
\boxed{
\tau_h^+(\xi)
=\mathbf1_{\xi\ge0}e^{-h\xi}\lambda_2(\xi),
}
\tag{L-105621.1}
\]

\[
\boxed{
\tau_h^-(\xi)
=\mathbf1_{\xi\le0}e^{h\xi}\lambda_2(\xi).
}
\tag{L-105621.2}
\]

These are exactly the two causal orientations selected by the
Toeplitz--Hankel polarization of the upper and lower physical boundaries.

`L-105620` gives the pointwise source inequalities

\[
\boxed{
0\le h\tau_h^+(\xi)
\le\mathbf1_{\xi\ge0}j_h(\xi),
}
\tag{L-105621.3}
\]

and

\[
\boxed{
0\le h\tau_h^-(\xi)
\le\mathbf1_{\xi\le0}j_h(\xi).
}
\tag{L-105621.4}
\]

The stronger reserve is

\[
\boxed{
 j_h(\xi)-h e^{-h|\xi|}\lambda_2(\xi)
\ge
 h(1-e^{-h|\xi|})\lambda_2(\xi)
 +{h^3\over6}\Lambda_4(\xi).
}
\tag{L-105621.5}
\]

## 2. Every weighted source energy contracts

Let `w:[0,infinity)->[0,infinity]` be any measurable weight for which the
following integrals are finite. Then

\[
\boxed{
 h^2\int_0^\infty
 w(\xi)|\tau_h^+(\xi)|^2\,d\xi
\le
 \int_0^\infty w(\xi)j_h(\xi)^2\,d\xi.
}
\tag{L-105621.6}
\]

By reflection,

\[
\boxed{
 h^2\int_{-\infty}^0
 w(|\xi|)|\tau_h^-(\xi)|^2\,d\xi
\le
 \int_{-\infty}^0w(|\xi|)j_h(\xi)^2\,d\xi.
}
\tag{L-105621.7}
\]

Adding the two orientations gives

\[
\boxed{
 h^2
 \left(
  \|\tau_h^+\|_{L^2(w)}^2
  +\|\tau_h^-\|_{L^2(w)}^2
 \right)
\le
 \|j_h\|_{L^2(w;\mathbb R)}^2.
}
\tag{L-105621.8}
\]

The proof is only squaring and integrating (L-105621.3)--(L-105621.4). It is
therefore stable under arbitrary diagonal truncation, dyadic partition or
source-owned unitary transform in the coefficient Hilbert space.

## 3. Half-derivative and Hankel specializations

Taking

\[
w(\xi)=\xi
\]

on the positive half-line yields the exact half-derivative comparison

\[
\boxed{
 h^2\int_0^\infty
 \xi e^{-2h\xi}\Lambda_2(\xi)^2\,d\xi
\le
 \int_0^\infty\xi j_h(\xi)^2\,d\xi.
}
\tag{L-105621.9}
\]

Under the Paley--Wiener/Hardy identification, these integrals are the
Hilbert--Schmidt energies of the corresponding one-sided Hankel kernels. Thus
both actual Turán orientations are source-level contractions of the actual
current Hankel source at the topology-sensitive half derivative.

More generally, `w(xi)=xi^(2s)` proves the same comparison at every homogeneous
Sobolev order for which the Xi integrals converge.

## 4. Canonical contraction multiplier

Where `j_h(xi)>0`, define

\[
\boxed{
r_h(\xi)
={h e^{-h\xi}\Lambda_2(\xi)\over j_h(\xi)},
\qquad \xi\ge0.
}
\tag{L-105621.10}
\]

Then

\[
0\le r_h(\xi)\le1
\]

and the positive-frequency Turán source vector factors exactly as

\[
\boxed{
 h\tau_h^+=r_hj_h.
}
\tag{L-105621.11}
\]

The reflected orientation has the mirror factor `r_h(-xi)`. Hence the
source-level denominator whitening is canonical and contractive; it is not an
unknown Gram comparison.

## 5. What remains after the contraction

The physical directional microscope contains

\[
\mathcal T_\Xi(a+ih)
{\overline{\Xi'(a+ih)}\over\Xi'(a+ih)}.
\]

Multiplication by this variable all-pass phase is not diagonal in the Fourier
source coordinate. Nor does the physical two-trace map commute with the
multiplier `r_h`. Therefore the theorem does not promote (L-105621.11) to a
pointwise scalar sign.

It does prove that the following are **not** independent analytic debts:

```text
actual numerator tail;
reflected-source tail;
source-level denominator normalization;
source-level H^(1/2) magnitude comparison.
```

They are paid exactly by the current hierarchy. The sole noncommuting object is
the all-pass/physical-identification map, together with finite-window endpoint
terms.

## 6. Scope

Pointwise kernel domination is not claimed, and a pointwise-positive Hankel
kernel need not define a positive operator. The theorem is a diagonal Fourier
and weighted-energy contraction. Any use after a non-diagonal physical map
must retain its commutator or collision cost explicitly. `MCTPHYS105610`, the
balanced shell transfer and RH remain open.
