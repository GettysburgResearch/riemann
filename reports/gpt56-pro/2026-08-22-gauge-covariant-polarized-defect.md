# Gauge-covariant continuation of the completion-defect route

## Main finding

The Euler completion current and the half-divisor current have the same
endpoints and the same critical first chaos.  Their local ratio is

\[
\frac{[\tau+(1-\tau)\sqrt{1+x}]^2}{1+(1-\tau)x}
=1+O(x^2).
\]

Thus changing coordinates between the owner/activation gauge and the
half-divisor/Hilbert gauge costs only squared activity and is polylogarithmic.

This removes the most important remaining compositional ambiguity in PR #719:
owner cancellation, moving-transfer accounting and half-divisor factorization
can all be used on one literal source.

## Continuous current

The square-root geodesic

\[
\Lambda_\tau
=\prod_p
[\tau\sqrt{1-p^{-1/2}U_p}
 +(1-\tau)\sqrt{1-p^{-1}U_{p^2}}]
\]

has a root-free tangent.  The full completion defect is

\[
H_{\rm def}
=(2D-1)\int_0^1 2\dot G_\tau *_M G_\tau\,d\tau.
\]

All labelled diagonal, tangent, factor-pair, squared-core and same-owner costs
are polylogarithmic or subpower.

## No-go discovered

The two physical half-fields cannot be bounded separately.  Their prime
chaoses satisfy

\[
F_+^{[1]}(X)
\sim-c\frac{\sqrt X}{\log X},
\qquad
F_-^{[1]}(X)
\sim+c\frac{\sqrt X}{\log^2X}.
\]

Taking either field in absolute value before carrier recombination is therefore
power-lossy.  The conclusion-facing object must remain the polarized current.

## Exact frontier

The only unresolved scalar is the balanced, different-owner, distinct-product
part of that current:

```text
PHDNC102710:
  subpower logarithmic negative mass of the carrier-recombined
  polarized Hankel current.
```

This is equivalent up to polylogarithmic gauge transfer to `HDNC102703` and
implies the fixed common-mother Mellin–Landau criterion.

```text
PHDNC102710   OPEN / RH-BEARING
RH             UNPROVED
```