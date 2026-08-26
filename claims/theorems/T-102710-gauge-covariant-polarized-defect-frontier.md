# T-102710 — Gauge-covariant polarized defect frontier

Claim ID: `T-102710`  
Status: **MAJOR UNCONDITIONAL STRUCTURAL ADVANCE; RH UNPROVED**  
Created: 2026-08-22  
Base: PR #719  
RH status: **unproved**

PR #719 reduced the common-mother programme to the physical cross-owner
occupancy of one root-free half-divisor packet.  `L-102706--L-102709` sharpen
that frontier as follows.

## 1. Two gauges, one critical source

The Euler completion path and the half-divisor path have:

```text
identical squared endpoint;
identical native endpoint;
identical critical first-chaos coefficient.
```

Their ratio is an Euler multiplier with no linear prime term:

\[
G_\tau=I+O(p^{-1}).
\]

Both `G_tau` and its inverse have only polylogarithmic physical cost.

Thus owner/activation cancellation and half-divisor factorization are not
competing source models.  They are subcritically gauge-equivalent descriptions
of the same defect.

## 2. Continuous root-free current

There is one half-divisor geodesic `Lambda_tau` with root-free tangent
`dot Lambda_tau` such that

\[
\beta-\beta^\square
=2\int_0^1\dot\Lambda_\tau*\Lambda_\tau\,d\tau.
\]

With the positive ratio-four spline `A`,

\[
\boxed{
H_{\rm def}
=(2D-1)
\int_0^1 2\,\dot G_\tau *_M G_\tau\,d\tau.
}
\tag{T-102710.1}
\]

The tangent is root-free at every `tau`.

## 3. Closed costs

Uniformly in `tau`:

```text
labelled geodesic energy                 polylogarithmic;
labelled tangent energy                  polylogarithmic;
same-product factor-pair collapse        subpower;
squared/higher-prime-power gauges        polylogarithmic;
same-owner square-core overlap           polylogarithmic;
gauge switching between exact regions   exact, with polylog boundary cost.
```

The source partition may therefore use:

```text
Euler gauge in small/activation/owner regions;
half-divisor gauge in balanced occupancy regions.
```

No source, carrier or reserve is counted twice.

## 4. Binding no-go

`R-102701` proves that the separate physical fields contain deterministic prime
carriers:

\[
F_+^{[1]}(X)
\asymp-\frac{\sqrt X}{\log X},
\qquad
F_-^{[1]}(X)
\asymp+\frac{\sqrt X}{\log^2X}.
\]

Hence separate field energies are power-sized.  The polarized current must be
kept intact until all chaos carriers are recombined.

## 5. Exact remaining theorem

Let `dot G_(tau,bal)` and `G_(tau,bal)` denote the exact balanced,
carrier-recombined, different-owner regional fields after all closed source
terms above have been removed.  Define

\[
\mathcal J_{\rm bal}(X)
=(2D-1)
\int_0^1 2\int_0^\infty
\dot G_{\tau,\rm bal}(Y)
G_{\tau,\rm bal}(X/Y)
\frac{dY}{Y}\,d\tau.
\]

The final arithmetic statement is

```text
PHDNC102710:
  integral_1^Y (J_bal(X))_- dX/X = Y^o(1).
```

Equivalently one may prove the carrier-preserving distinct-product cross-owner
form `HDNC102703`.  The gauge transfer between the two formulations costs only
polylogarithmically.

The exact conclusion is

\[
\mathrm{PHDNC}_{102710}
\Longrightarrow
\mathrm{AR\!-\!DEFECT}_{102600}
\Longrightarrow
\mathrm{RH}.
\]

```text
Euler/half-divisor gauge equivalence      PROVED EXACT/POLYLOG
continuous root-free geodesic             PROVED EXACT
uniform labelled/tangent energies         PROVED POLYLOG
regionwise gauge selection                PROVED EXACT
separate-field energy shortcut            REFUTED
PHDNC102710                                OPEN / RH-BEARING
Riemann Hypothesis                        UNPROVED
```