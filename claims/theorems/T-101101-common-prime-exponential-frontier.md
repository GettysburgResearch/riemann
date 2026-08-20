# T-101101 — CV and XD reduce to one prime-exponential frontier

Claim ID: `T-101101`  
Status: **PROVED EXACT REDUCTION; PRIME-EXPONENTIAL ESTIMATE OPEN**  
Created: 2026-08-21  
Depends on: `L-101100--L-101103`  
RH status: **unproved**

`L-101103` gives the exact factorization

\[
\mathcal E_Z
=
\mathcal S_Z\mathcal R_Z\mathcal P_Z,
\]

where

```text
S_Z  = literal squared core;
R_Z  = zero-free renormalizer with polylogarithmic source norm;
P_Z  = exp(-sum_(p<=Z) p^(-1/2) U_p).
```

The CV attack proves the completed collar attached to `S_Z` nonnegative.
The renormalizer `R_Z` costs only `Z^o(1)`.  The XD short/long prime carrier is
the first-order physical component of `P_Z`, and its exact cancellation must be
retained by the sum-channel projection of `L-101101`.

Therefore the two implication-matrix classes share one final source-specific
producer:

```text
PECP101101:
  establish a subpower one-sided/covariance estimate for the literal
  prime-exponential packet P_Z after the fixed SHARP/minimal-wavelet
  observation, uniformly through the source-labelled Z-limit.
```

A proof of `PECP101101` gives both:

```text
signed desmoothing of the completed CV packet;
carrier-preserving cross-core control of the XD wavelet.
```

Together with the frozen Mellin--Landau consumers it would imply RH.

## Why this is not another parity gate

The squared and all higher local Euler chaoses are contained in
`S_Z R_Z`, whose total-variation cost is polylogarithmic.  The sole remaining
factor is the exponential of a linear prime-shift operator.  Thus no hidden
many-prime cube, Hall residual, or regional carrier remains outside the stated
frontier.

## Exact status

```text
squared-core factor                         PROVED / POSITIVE
Wick renormalizer                           PROVED / SUBPOWER NORM
prime-exponential factor                    IDENTIFIED EXACTLY
PECP101101                                  OPEN / RH-BEARING
CV                                          OPEN / RH-EQUIVALENT
XD                                          OPEN / RH-EQUIVALENT
Riemann Hypothesis                          UNPROVED
```
