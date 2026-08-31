# T-107120 — Additive Chowla and square-root frequency frontier for native beta

**Claim ID:** `T-107120`  
**Status:** two unconditional normal forms; final cancellation estimate open  
**Date:** 2026-08-31  
**RH:** unproved

The stationary ratio-67 square of `T-107110` now has two exact conclusion-facing
coordinates.

## A. Additive two-point Möbius coordinate

`L-107120` proves

\[
\mathcal Q_{67}(Y)
=\mathcal D_{67}(Y)+2\sum_{h<Y}\mathcal C_{67,h}(Y),
\]

where the diagonal is `O(log Y)` and the off-diagonal is the literal weighted
aggregate of two-point Möbius correlations

\[
\mu(n)\mu(n+h)
\]

through the physical range `h<=66n`. Grouping by `g=(n,h)` gives a primitive
additive-gap form with coefficient

\[
\frac{\mu(a)\mu(a+r)}{g\sqrt{a(a+r)}}.
\]

The maximal absolute aggregate has exact power exponent

\[
\boxed{2\Theta-1.}
\]

Thus any fixed power saving for this calibrated additive Chowla average gives
the corresponding zero-free half-plane, and a subpower bound is equivalent to
RH.

## B. Square-root spectral coordinate

`L-107121` proves the exact Fourier identity

\[
\mathcal Q_{67}(Y)
=\frac{\log67}{2\pi}\int_{\mathbb R}
\operatorname{sinc}^2\!\left(\frac{t\log67}{2}\right)
\left|\sum_{n\le Y,67\nmid n}\frac{\mu(n)}{n^{1/2+it}}\right|^2dt.
\]

The classical mean-value theorem pays the complete tail beyond

\[
|t|>Y^{1/2}(\log(2Y))^B,
\qquad B>1/2,
\]

with a subpower error. The retained low-frequency integral has the same exact
power exponent `2 Theta-1`.

## Revised beta execution map

```text
literal beta source
  -> stable 67-free source
  -> fixed stationary tent square
  -> either:
       additive primitive Chowla aggregate
     or
       square-root frequency Dirichlet-polynomial window
  -> power saving gives a zero-free half-plane
  -> subpower gives RH.
```

The two normal forms are equivalent consequences of one fixed source and one
fixed compact kernel; neither replaces the other by an absolute bound.

## Current frontier

```text
stationary q-adic coarea                         PROVED EXACT
high-primitive common-core reduction             PROVED EXACT
additive two-point Möbius normal form             PROVED EXACT
square-root frequency-tail deletion              PROVED UNCONDITIONALLY
quantitative exponent 2 Theta-1                   PROVED
low-frequency/additive signed cancellation       OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVEN
```
