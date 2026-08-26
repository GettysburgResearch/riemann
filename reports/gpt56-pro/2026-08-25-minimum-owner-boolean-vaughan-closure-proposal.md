# Minimum-owner Boolean Vaughan closure proposal — retracted historical report

Date: 2026-08-25  
Execution PR: #751  
Programmes: #743, #736, #737  
Parent: PR #719 at `60285de21fafdd1b3c185ddd19b57191a41c08dd`  
Status: **former full proof proposal retracted by `R-106080`; RH unproved**

## Binding correction

The source-level reconstruction in

```text
reports/gpt56-pro/2026-08-25-t106080-self-reconstruction.md
```

found that the proposal's direct use of `L-102883` was not source-faithful.
The complete phase packet has varying owner squareclass

\[
n_i=P_i a_i^2,
\qquad P_i=\lambda_i\Lambda_i,
\]

so its centered kernel is on

\[
P_i a_i^2-P_j a_j^2,
\]

not merely on

\[
a_i^2-a_j^2.
\]

Accordingly `L-106082.3`, `L-106082.5` and `T-106080` are retracted. The live
frontier is `T-106081 / MOBOSM106081`.

This report is retained only to document how the failed proposal arose.

## Mechanism originally proposed

The prior scale-matched character coordinate left power-sized coherent owner
families in one residue cell. The proposal changed the owner/Vaughan gauge
before that collapse:

1. work in the literal squarefree Euler algebra using disjoint-support Boolean
   convolution;
2. apply an exact Boolean Vaughan identity;
3. use a horizon-safe minimum-owner pair;
4. derive `lambda^2<=a` and hence `L^2<2B`;
5. attempt to insert every block into the parent coherent phase theorem.

Steps 1--4 survive. Step 5 fails at the varying-owner squareclass transport.

## Mathematics retained

```text
Boolean squarefree Vaughan identity                 PROVED EXACT
balanced support has two distinct core primes       PROVED EXACT
squarefree fixed-owner Type-I                       Y^(-1/12+o(1))
minimum-owner horizon gauge                         PROVED EXACT
lambda^2 <= a                                       PROVED EXACT
L^2 < 2B                                            PROVED EXACT
```

The self-reconstruction further proves:

```text
no exceptional label:
  Lambda^2 <= a and P=lambda*Lambda <= a;

unique exceptional label Lambda>4 sqrt(Y):
  lambda*a^2 < 4 sqrt(Y), hence lambda^5 < 4 sqrt(Y).
```

## Exact failed transport

The square-core corollary of `L-102883` controls one common coefficient
sequence with kernel

\[
\mathbf1_{q\mid a_i^2-a_j^2}-\frac1q.
\]

The physical source instead yields

\[
\mathbf1_{q\mid P_i a_i^2-P_j a_j^2}-\frac1q.
\]

Hiding `P_i` in an orthogonal Hilbert coordinate deletes the cross-owner
physical Gram. Aggregating it in the physical Hilbert space assumes the open
owner-occupancy norm. Applying the theorem separately at fixed `P_i` reopens
the coherent summation obstruction of `R-102840`.

## Correct live handoff

`T-106081` defines selector-tied fields

\[
\mathcal A_{\ell\to\rho;k}
=
\sum_{i\in I_\ell}
\beta_i e_\rho(k n_i)v_i
\]

and the positive majorant

\[
\mathfrak P_{B,L}
=
\sum_{\ell\ne\rho}
\frac{\rho-1}{\ell\rho}
\sum_{k=1}^{\rho-1}
\|\mathcal A_{\ell\to\rho;k}\|^2.
\]

The remaining theorem `MOBOSM106081` asks for a subpower dyadic sum of these
moments with every literal source weight used once. It has sharpened
no-exception and exceptional subtargets, but remains open and RH-bearing.

## Replay boundary

```text
PASS_X_106080_MINIMUM_OWNER_BOOLEAN_VAUGHAN
checks=34250
sha256=86bb5ac732d2548679b16000a61c1fa40d961c962bde5d44edf9d39c110f98df
```

The replay certifies finite Boolean convolution, owner selection, dyadic range,
abstract same-family kernels, squarefree reindexing and clean phase fixtures.
It does not certify the source-tied owner moment, the Mellin consumer or RH.

## Current status

```text
T-106080 historical closure proposal        RETRACTED
R-106080 source-kernel correction            BINDING
T-106081 corrected frontier                  LIVE / OPEN
MOBOSM106081                                 OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVEN
```
