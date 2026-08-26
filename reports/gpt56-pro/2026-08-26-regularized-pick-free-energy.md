# Regularized Pick free energy: an asymptotically lossless scalar endpoint frontier

Date: 2026-08-26  
Branch target: `research/gpt56-pro/105210-simple-zero-record-and-descent`  
Verified parent head: `433490c133b26bce4163f4edf7ad04aeda9d33e3`

## Remote audit

The earlier T-106610 residue packet is present on PR #731.  The branch has
since advanced through T-106650, whose retained replay explicitly records that
the required Xi estimate, 90%, density one, and RH remain unproved.

## New exact reduction

Let `Q_j` be the positive contraction whose trace is the exact adverse
canonical charge on a mesoscopic window.  For `0<tau<1`, define

\[
Z_j(\tau)=\det(I-\tau Q_j),
\qquad
F_j(\tau)=-\tau^{-1}\log Z_j(\tau).
\]

Spectrally,

\[
\operatorname{tr}Q_j
\le F_j(\tau)
\le { -\log(1-\tau)\over\tau}\operatorname{tr}Q_j.
\]

A deterministic `tau_T -> 0` therefore makes the summed free energy
asymptotically equal to the exact charge at every pole-height cutoff, including
the full denominator factor.

In the actual denominator kernel frame,

\[
Z_j(\tau)
=
{\det(G_j-\tau V_j^*G_jV_j)\over\det G_j},
\]

where

\[
(V_j)_{rr}=B_{+,j}(b_{j,r})
={2i\lambda_j(hDH_5-(Dh)H_5)(b_{j,r})\over O_j(b_{j,r})}.
\]

The complete many-pole whitening, including T-106650 nonnormality, is thus
packaged into one positive source-evaluation Pick determinant.

## Full and cutoff gates

The full endpoint determinant carries the entire exact allowance

\[
{97\over1000}.
\]

The height theorem also gives a one-parameter family.  At cutoff `eta`, the
deep charge is at most

\[
{3\over4000\eta}N+o(N),
\]

so the determinant allowance is

\[
{97\over1000}-{3\over4000\eta}.
\]

In particular,

```text
eta = 1/100    allowance = 11/500
eta = 1/10     allowance = 179/2000
eta = 1        allowance = 77/800
eta = infinity allowance = 97/1000
```

The fixed `0.01` split is therefore optional, not load-bearing.

## Global target

For the full factor, put

\[
\mathscr Z_T=\prod_j Z_j(\tau_T).
\]

The exact surviving target is

\[
-{1\over\tau_T}\log\mathscr Z_T+E_{\rm reg}(T)
<\left({97\over1000}-\epsilon\right)N(T,2T).
\]

At cutoff `eta`, replace `97/1000` by
`97/1000-3/(4000 eta)`.  Each form is asymptotically equivalent to its exact
canonical-charge gate and implies more than 90% by the pinned fifth-derivative
input.

## Why regularization is load-bearing

At `tau=1`, one orthogonal direction makes the overlap determinant zero, so
`-log det` is infinite even when the exact charge is only one.  The regularized
free energy charges that direction by

\[
{-\log(1-\tau)\over\tau},
\]

independent of ambient dimension, and tends to the exact unit charge as
`tau -> 0`.

The equal-rank `tau=1` endpoint remains geometrically useful:

\[
-\log Z_1
=
\int_0^\infty
{\left|\sum e^{-z_j\xi}-\sum e^{-w_j\xi}\right|^2\over\xi}\,d\xi.
\]

It exposes the horizontal degree-zero phase geometry, but is not the live
consumer.

## Honest boundary

```text
regularized free-energy sandwich                    PROVED EXACT
source-evaluation Pick determinant                  PROVED EXACT
conditional pivot / global product factorization    PROVED EXACT
full and cutoff-family gate equivalences             PROVED EXACT
Xi lower bound for the global determinant            OPEN / 90%-BEARING
more than 90%                                        UNPROVED
density one / RH                                     UNPROVED
```
