# T-105430 — Homotopy-coherent F1 trace and the star–cycle pair frontier

Claim ID: `T-105430`

Status: **PROVED COMPOSITION / TWO ARITHMETIC TRACE ESTIMATES OPEN**

This checkpoint supersedes the positive-energy frontier in `T-105420`.

## 1. Correct conclusion-facing object

The literal completion tangent must be integrated before the primitive square.
Let

\[
\bar A=\int_0^1A_\tau\,d\tau,
\qquad
\bar B=\int_0^1(G_\tau-A_\tau)\,d\tau.
\]

Define

\[
\mathcal Q_{\rm coh}(T)
=
\int_T^{T+1}
\left[
(4\bar A-\bar B)^2
+
\frac{(\bar A+192\bar B)^2}{48}
\right]du.
\tag{T-105430.1}
\]

The source in (T-105430.1) is exactly the complete native-minus-completion
source.  All deterministic chaos carriers are recombined before squaring.

If

\[
\boxed{
\mathcal Q_{\rm coh}(T)=e^{o(T)},
}
\tag{F1HCNC105430}
\]

then the block negative mass of the fixed outer current is \(e^{o(T)}\), and
the frozen Mellin--Landau consumer gives RH.

## 2. Why the previous frontier fails

`R-105430` proves that the isolated Wick remainder has Hodge energy

\[
\asymp \frac{X}{\log^2X}.
\]

The removed carrier has the opposite leading direction.  Hence
`F1WNC105420` is false as a positive-energy statement.  This does not alter any
finite F1 theorem.

## 3. Exact degree-two owner split

Retain an unordered prime pair until equal-product collapse and let
\(v_{ij}\) be its two-coordinate block current.  `L-105431` gives

\[
\left\|\sum_{i<j}v_{ij}\right\|^2
=
\mathcal Q_2(v)
-
\sum_{i<j}\|v_{ij}\|^2
+
\sum_i\left\|\sum_{j\ne i}v_{ij}\right\|^2.
\tag{T-105430.2}
\]

The diagonal is already subpower.  Thus the two explicitly distinct statements

```text
F1STAR105431:
  shared-owner star energy is exp(o(T));

F1CYCLE105431:
  the positive four-distinct-label Hodge-cycle trace is exp(o(T))
```

imply `F1HCNC105430`.

The exact chain is

\[
\boxed{
\mathrm{F1STAR}_{105431}
+
\mathrm{F1CYCLE}_{105431}
\Longrightarrow
\mathrm{F1HCNC}_{105430}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105430.3}
\]

## 4. Two owner gauges

The symmetric Duhamel pair owner is canonical for the exponential source.
`L-105432` proves that it can be transferred, coefficient exactly and at
polylogarithmic free cost, to the least/greatest extreme pair.  This supplies
two complementary attack coordinates:

```text
equal pair:
  best for Wick/Fock and degree-two Hodge algebra;

extreme pair:
  best for endpoint/interior, compensated-prefix and truncated-Dickman
  interval geometry.
```

A successful next pass may prove `F1STAR` in the extreme-pair gauge and
`F1CYCLE` in the symmetric Hodge gauge, provided both are returned to the same
literal source before physical observation.

## Exact status

```text
finite F1 source and Hodge package              PROVED EXACT
isolated Wick positive-energy packing           REFUTED
homotopy-coherent variance identity             PROVED EXACT
degree-two pair Lefschetz decomposition         PROVED EXACT
equal/extreme pair gauge transfer               PROVED EXACT
F1STAR105431 shared-owner estimate              OPEN
F1CYCLE105431 four-label cycle estimate         OPEN
F1HCNC105430 coherent physical trace            OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
