# L-106082 — Minimum-owner long-core geometry and the failed core-only transport

Claim ID: `L-106082`  
Programme aliases: `LFAM1.ALL_BLOCK_PHASE_PACKING`, `STRESS.MINIMUM_OWNER_LONG_CORE`, `LFAM2.CORE_PAID_KUMMER_MOMENT`  
Status: **GEOMETRY AND ABSTRACT KERNEL IDENTITY RETAINED; COMPLETE-SOURCE TRANSPORT RETRACTED BY `R-106080`**  
Created: 2026-08-25  
Corrected: 2026-08-25  
Depends on: parent `L-102882--L-102883`; `L-106080--L-106081`; binding correction `R-106080`  
Programme issues: #743, #736, #737  
RH status: **unproved**

## Binding correction

The first version of this file claimed that every minimum-owner Boolean block
could be inserted directly into the fixed-squareclass corollary of
`L-102883`. The source-level reconstruction `R-106080` proves that this
transport is not valid.

The following statements remain exact:

1. every balanced block satisfies the minimum-owner long-core inequality;
2. the same-family deleted-diagonal identity is an exact algebraic identity
   once the correct physical difference has been fixed.

The former complete-source estimates `(L-106082.3)--(L-106082.5)` are
retracted. The corrected conclusion-facing object is `T-106081 /
MOBOSM106081`.

## 1. Retained minimum-owner range

On one linearly projected balanced block

\[
B\le a<2B,
\qquad
L\le\lambda<2L,
\]

`L-106081` gives

\[
\boxed{L^2<2B.}
\tag{L-106082.1}
\]

This is coefficient-exact. It says that the distinguished owner conductor is
paid by the literal Boolean core.

The corrected theorem `T-106081` further records:

```text
no exceptional label:  P=lambda*Lambda <= a;
unique exceptional label: lambda*a^2 < 4 sqrt(Y), hence lambda^5 < 4 sqrt(Y).
```

## 2. Retained abstract same-family identity

For a prime family `mathcal P` and an integer `d`, put

\[
A_\ell(d)=\mathbf1_{\ell\mid d}-\frac1\ell,
\qquad
K_{\mathcal P}(d)=\sum_{\ell\in\mathcal P}A_\ell(d).
\]

Then exactly

\[
\boxed{
\sum_{\substack{\ell,\rho\in\mathcal P\\\ell\ne\rho}}
A_\ell(d)A_\rho(d)
=
K_{\mathcal P}(d)^2
-
\sum_{\ell\in\mathcal P}A_\ell(d)^2.
}
\tag{L-106082.2}
\]

This identity correctly deletes the shared-prime diagonal. It does not alter
the argument `d` of the centered divisor kernels.

## 3. Exact failed interface

A complete minimum-owner source atom has

\[
n_i=P_i a_i^2,
\qquad
P_i=\lambda_i\Lambda_i,
\]

with varying owner squareclass `P_i` and with the phase modulus selected by the
source atom. For a source-faithful aggregated phase field, exact orthogonality
produces the physical kernel

\[
\boxed{
\mathbf1_{q\mid P_i a_i^2-P_j a_j^2}-\frac1q.
}
\tag{L-106082.3-correct}
\]

The square-core corollary of `L-102883` instead uses, for one fixed
squareclass, the kernel

\[
\mathbf1_{q\mid a_i^2-a_j^2}-\frac1q.
\]

These kernels are not equal and neither dominates the other uniformly when
`P_i` varies. Equation (L-106082.2) only rearranges the modulus sum after `d`
has been fixed; it cannot replace the physical difference by the core
difference.

Likewise, retaining the owner labels in an orthogonal Hilbert coordinate
deletes the cross-owner physical Gram, while retaining them in the physical
Hilbert space makes the required coefficient norm precisely the open
owner-occupancy quantity. Applying `L-102883` separately for each fixed `P`
reopens the coherent recombination obstruction of `R-102840`.

## 4. Binding consequence

```text
L-106082.1 minimum-owner range                 RETAINED EXACT
L-106082.2 abstract same-family identity       RETAINED EXACT
former L-106082.3 phase estimate               RETRACTED
former L-106082.4 all-block conclusion         RETRACTED
former L-106082.5 global balanced energy       RETRACTED
T-106080 RH composition                        RETRACTED
T-106081 selector-tied owner moment             LIVE / OPEN
Riemann Hypothesis                             UNPROVED
```

The independent review target is the selector-tied positive moment in
`T-106081.10`, not a core-only application of `L-102883`.
