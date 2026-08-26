# L-105430 — Homotopy recombination must precede the F1 primitive square

Claim ID: `L-105430`

Status: **PROVED EXACT HILBERT/HOCHSCHILD VARIANCE IDENTITY**

Let \(\Sigma_\tau=-\partial_\tau E_\tau\) be the literal completion tangent,
\(0\le\tau\le1\).  For one logarithmic block \(I_T=[T,T+1]\), let

\[
A_\tau,\qquad B_\tau=G_\tau-A_\tau
\]

be the carrier-recombined F1 primitive coordinates, regarded as elements of
\(L^2(I_T)\).  Put

\[
v_\tau
=
\left(
\frac{A_\tau}{\sqrt{24}},
\sqrt2\,B_\tau
\right)
\in
\mathcal H_T:=L^2(I_T;\mathbb R^2).
\]

Then

\[
\|v_\tau\|_{\mathcal H_T}^2
=
\int_{I_T}
\left(
\frac{A_\tau(u)^2}{24}
+
2B_\tau(u)^2
\right)du
\]

is the finite F1 primitive Hodge energy.

## 1. The coherent source

Because the completion path is exact,

\[
\int_0^1\Sigma_\tau\,d\tau
=
E_0-E_1
=
S-E.
\]

Define

\[
\bar v
=
\int_0^1v_\tau\,d\tau.
\]

Up to the fixed global orientation, \(\bar v\) is the physical primitive class
of the complete native-minus-completion source \(E-S\).  No chaos sector or
owner packet has been squared separately.

## 2. Exact variance decomposition

Since the homotopy interval has mass one,

\[
\boxed{
\int_0^1\|v_\tau\|^2\,d\tau
=
\|\bar v\|^2
+
\int_0^1\|v_\tau-\bar v\|^2\,d\tau.
}
\tag{L-105430.1}
\]

Equivalently,

\[
\boxed{
\int_0^1\|v_\tau\|^2\,d\tau-\|\bar v\|^2
=
\frac12
\int_0^1\int_0^1
\|v_\tau-v_\sigma\|^2\,d\tau\,d\sigma.
}
\tag{L-105430.2}
\]

Thus “square each tangent and then integrate” equals the conclusion-facing
coherent square plus a nonnegative homotopy-variance debt.  The variance may
be power-sized even when the coherent square is small.

## 3. Exact conclusion-facing coordinates

Write

\[
\bar A=\int_0^1A_\tau\,d\tau,
\qquad
\bar B=\int_0^1B_\tau\,d\tau.
\]

The coherent Lorentz and complementary Hodge coordinates are

\[
\bar L=4\bar A-\bar B,
\qquad
\bar J=\bar A+192\bar B.
\]

The exact orthogonal identity is

\[
\boxed{
\frac{769}{2}\|\bar v\|^2
=
\int_{I_T}
\left(
\bar L(u)^2+\frac{\bar J(u)^2}{48}
\right)du.
}
\tag{L-105430.3}
\]

Consequently

\[
\int_{I_T}(\bar L(u))_-\,du
\le
\left(
\int_{I_T}\bar L(u)^2\,du
\right)^{1/2}
\le
\sqrt{\frac{769}{2}}\,\|\bar v\|.
\tag{L-105430.4}
\]

A subpower bound for the coherent energy therefore feeds the frozen
Mellin--Landau consumer.

## 4. Firewall

For a decomposition \(v_\tau=p+w_\tau\), one may not replace

\[
\left\|p+\int_0^1w_\tau d\tau\right\|^2
\]

by a bound for \(\int\|w_\tau\|^2\) unless the cross carrier has first been
shown negligible.  `R-105430` proves that in the present source it is
power-sized and cancellation is exact.

The valid order is:

```text
source formation
 -> owner/region recombination
 -> homotopy integration
 -> deterministic-carrier cancellation
 -> primitive square
 -> physical trace.
```
