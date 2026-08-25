# T-106080 — Retracted minimum-owner Boolean Vaughan closure proposal

Claim ID: `T-106080`  
Programme aliases: `LFAM1.MINIMUM_OWNER_CLOSURE`, `STRESS.ALL_BLOCK_LONG_CORE`, `LFAM2.BOOLEAN_KUMMER_COMPLETION`  
Status: **RETRACTED BY `R-106080`; RETAINED ONLY AS A HISTORICAL PROPOSAL RECORD**  
Created: 2026-08-25  
Retracted: 2026-08-25  
Depends on: `L-106080--L-106082`; binding correction `R-106080`; corrected frontier `T-106081`  
Programme issues: #743, #736, #737  
RH status: **unproved**

## Retraction notice

The first version of this theorem proposed

\[
\text{Boolean squarefree Vaughan}
\wedge
\text{minimum-owner gauge}
\wedge
\text{parent coherent centered phase packing}
\Longrightarrow
\mathrm{RH}.
\]

The internal source-level reconstruction rejects the third edge. The proposal
silently replaced the physical centered kernel on

\[
P_i a_i^2-P_j a_j^2,
\qquad P_i=\lambda_i\Lambda_i,
\]

by the fixed-squareclass core kernel on

\[
a_i^2-a_j^2.
\]

That replacement is false when the owner squareclass `P_i` varies. The exact
firewall is `R-106080`, and the exact corrected open theorem is
`T-106081 / MOBOSM106081`.

Consequently this file must not be cited as a proof of RH or as a live complete
composition.

## 1. Mathematics retained from the proposal

The reconstruction accepts:

```text
Boolean squarefree Möbius inversion              PROVED EXACT
Boolean Vaughan identity                         PROVED EXACT
balanced Boolean support has two core primes      PROVED EXACT
squarefree fixed-owner Type-I                     Y^(-1/12+o(1))
minimum-owner horizon gauge                       PROVED EXACT
lambda^2 <= a                                     PROVED EXACT
L^2 < 2B                                          PROVED EXACT
abstract same-family deleted-diagonal identity    PROVED EXACT
```

It also sharpens the owner geometry:

```text
no exceptional label:
  Lambda^2 <= a and lambda*Lambda <= a;

unique exceptional label Lambda>4 sqrt(Y):
  lambda*a^2 < 4 sqrt(Y), hence lambda^5 < 4 sqrt(Y).
```

These are unconditional source reductions and remain scientifically useful.

## 2. First failed equation

For complete source atoms

\[
n_i=P_i a_i^2,
\qquad P_i=\lambda_i\Lambda_i,
\]

exact phase orthogonality gives

\[
\frac1q\sum_{h=1}^{q-1}
\left\|
\sum_i c_i e_q(hP_i a_i^2)v_i
\right\|^2
=
\sum_{i,j}
\langle c_iv_i,c_jv_j\rangle
\left(
\mathbf1_{q\mid P_i a_i^2-P_j a_j^2}-\frac1q
\right).
\]

The original closure adapter invoked `L-102883` as though the kernel were

\[
\mathbf1_{q\mid a_i^2-a_j^2}-\frac1q.
\]

There is no such identity or uniform one-sided domination for varying `P_i`.

The attempted Hilbert packaging has the exact trilemma recorded in
`R-106080`:

```text
orthogonal owner coordinates:
  delete the open cross-owner physical Gram;

physical owner aggregation:
  assume the open owner-occupancy norm;

fixed-P application followed by recombination:
  reopen the source-blind coherence obstruction of R-102840.
```

Thus the original global balanced-field estimate and the RH conclusion do not
follow.

## 3. Correct replacement

`T-106081` retains the complete source selector. Its clean Gram is expressed
through fields

\[
\mathcal A_{\ell\to\rho;k}
=
\sum_{i\in I_\ell}
\beta_i e_\rho(k n_i)v_i,
\]

and is bounded by the exact positive moment

\[
\boxed{
\mathfrak P_{B,L}
=
\sum_{\substack{\ell,\rho\in\mathcal P_L\\\ell\ne\rho}}
\frac{\rho-1}{\ell\rho}
\sum_{k=1}^{\rho-1}
\|\mathcal A_{\ell\to\rho;k}\|^2.
}
\]

The live theorem is

```text
MOBOSM106081:
  the dyadic sum of the selector-tied positive moments P_(B,L) is X^(o(1)),
  with every literal source weight used exactly once.
```

It has two sharpened sectors:

```text
MOBOSM-NE106081: P_i <= a_i;
MOBOSM-EX106081: lambda_i^5 < 4 sqrt(Y).
```

Neither sector is presently closed.

## 4. Correct implication graph

Let `BSFTI106081` denote the independent global parent-ledger verification of
the fixed-owner Boolean Type-I estimate. Then

\[
\boxed{
\mathrm{BSFTI}_{106081}
\wedge
\mathrm{MOBOSM}_{106081}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\int_1^Y(H_K)_-\frac{dX}{X}=Y^{o(1)}
\Longrightarrow
\mathrm{RH}.
}
\]

The two premises remain review interfaces; `MOBOSM106081` is open and
RH-bearing.

## Binding status

```text
T-106080 full closure                    RETRACTED
R-106080 source-kernel firewall          BINDING
T-106081 corrected owner frontier        LIVE / OPEN
MOBOSM106081                             OPEN / RH-BEARING
BSFTI106081                              INDEPENDENT CHECK REQUESTED
Riemann Hypothesis                       UNPROVEN
```
