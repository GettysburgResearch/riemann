# T-106121 — Bilateral physical-squareclass family frontier

Claim ID: `T-106121`  
Programme aliases: `LFAM1.BILATERAL_SQUARECLASS_REPAIR`, `LFAM2.KUMMER_PC2_QD2_FRONTIER`, `STRESS.COPRIME_BOOLEAN_PHYSICAL_FAMILY`  
Status: **CORRECTED PREFERRED BILATERAL FRONTIER; THREE PHYSICAL-SQUARECLASS MOMENTS OPEN**  
Created: 2026-08-25  
Depends on: retained `L-106120--L-106121`; binding corrections `R-106122`, `R-106123`; local `L-106124`; parent `T-102990`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The source-symmetric bilateral tensor construction survives its hostile audit.
Its first owner-only collision interpretation does not.  This theorem records
the exact corrected family geometry.

## 1. Retained bilateral tensor

Every live coprime two-sided Boolean pair has

\[
 N=P g^2c^2,
 \qquad
 M=Q g^2d^2,
 \qquad
 c,d>1,
 \qquad
 (c,d)=1,
\]

with canonical phase primes

\[
 \ell=P^-(c),
 \qquad
 \rho=P^-(d).
\]

The two same-occurrence nonzero phases give

\[
 1=
 \sum_{h=1}^{\ell-1}
 \sum_{k=1}^{\rho-1}
 e_\ell(h(N-M))e_\rho(k(N-M)).
\]

Both complete source sides are amplified before squaring.  The tensor Gauss
identity of `L-106120` and the source-dual moment

\[
 \mathfrak M_{\rm BT}(Y)
\]

of `L-106121`, with external weight `g^2 ell rho`, remain exact.  In
particular,

\[
\boxed{
 \mathfrak M_{\rm BT}(Y)=Y^{o(1)}
 \Longrightarrow
 \mathrm{BCI}_{102990}
 \Longrightarrow
 \mathrm{RH}.
}
\tag{T-106121.1}
\]

The atomic diagonal of `mathfrak M_BT` is unconditionally subpower.

## 2. Correct character variables

On the anchor side, a root character `psi` modulo `rho` sees

\[
 \psi(P)\psi^2(c)=\psi(Pc^2).
\]

On the opposite side, a root character `chi` modulo `ell` sees

\[
 \chi(Q)\chi^2(d)=\chi(Qd^2).
\]

Therefore the correct multiplicative family coordinates are the complete
physical squareclasses

\[
\boxed{
 X=Pc^2,
 \qquad
 Y=Qd^2.
}
\tag{T-106121.2}
\]

They are exactly the two Kummer maps attached to the physical source.

## 3. Correct four tensor channels

### Principal--principal

The principal member is the native untwisted coprime Boolean incidence current.
No character collision is imposed.

### Principal--nonprincipal

Even-character orthogonality modulo `ell` imposes

\[
\boxed{
 Qd^2\equiv\pm Q'd'^2\pmod\ell.
}
\tag{T-106121.3}
\]

### Nonprincipal--principal

Even-character orthogonality modulo `rho` imposes

\[
\boxed{
 Pc^2\equiv\pm P'c'^2\pmod\rho.
}
\tag{T-106121.4}
\]

### Nonprincipal--nonprincipal

Both physical-squareclass collisions occur:

\[
\boxed{
 Pc^2\equiv\pm P'c'^2\pmod\rho,
 \qquad
 Qd^2\equiv\pm Q'd'^2\pmod\ell.
}
\tag{T-106121.5}
\]

Equal physical products, repeated labels, shared owners and owner/core overlaps
remain in the inherited diagonal/renewal ledger.  The strict region consists
of (T-106121.3)--(T-106121.5) after those exact source strata are deleted.

## 4. What owner Wick factorization still supplies

For one fixed core, the canonical equal-pair owner field remains

\[
 {1\over2}
 \left[
  \mathcal P_\chi^2-\mathcal D_\chi
 \right].
\]

This removes repeated owner labels and exposes the prime-owner variables
inside each Kummer fibre.  It does not replace `Pc^2` by `P` when two different
cores are paired.

Similarly, the function-field theorem `L-106130` proves normalized square-root
size for one complete nonprincipal owner shell.  Transport through varying
core characters and incidence masks remains part of the global Kummer moment.

## 5. Valid local theorem and invalid global promotion

`L-106124` proves the fixed-core bilateral additive large-sieve estimate.
`R-106123` proves that power-many least-prime conductor fibres can remain even
when each fixed fibre is cheap.  Therefore no positive sum over fixed cores or
conductors is declared closed without a global family theorem.

## 6. Exact live gates

Define:

```text
BTPS106121:
  the off-atomic principal--principal physical-squareclass tensor moment is
  subpower;

BTMS106121:
  the sum of the two mixed strict physical-squareclass collision moments
  (T-106121.3)--(T-106121.4) is subpower;

BTDS106121:
  the strict double physical-squareclass collision moment (T-106121.5) is
  subpower.
```

The tensor decomposition is positive, so

\[
\boxed{
 \mathrm{BTPS}_{106121}
 \wedge
 \mathrm{BTMS}_{106121}
 \wedge
 \mathrm{BTDS}_{106121}
 \Longrightarrow
 \mathfrak M_{\rm BT}(Y)=Y^{o(1)}
 \Longrightarrow
 \mathrm{BCI}_{102990}
 \Longrightarrow
 \mathrm{RH}.
}
\tag{T-106121.6}

None of the three first premises is proved.

## 7. Correct function-field target

Define

```text
FFPS106121:
  over F_q[T], construct the two Kummer maps

      (P,c) -> P*c^2,
      (Q,d) -> Q*d^2,

  with the source-selected Artin--Schreier phases at rho and ell;
  classify and remove diagonal, quadratic-root, shared-incidence and
  geometrically constant constituents;
  prove the mixed and double physical-squareclass trace moments;
  export a number-field hybrid large-sieve, exponential-sum or relative-trace
  theorem retaining the varying core characters.
```

An owner-only prime-shell estimate is an input to this geometry, not the whole
geometry.

## 8. Binding status

```text
bilateral source partition and double phases            PROVED EXACT
two-sided amplification before square                   PROVED EXACT
tensor Gauss identity                                    PROVED EXACT
source-dual moment and implication to BCI102990          PROVED EXACT
atomic diagonal                                          PROVED SUBPOWER
fixed-core local owner phase energy                      PROVED
owner Wick factorization at fixed core                   PROVED EXACT
owner-only global collision description                 RETRACTED
near-prime/local-to-global closure                       RETRACTED
physical-squareclass collision description              PROVED EXACT
BTPS106121 / BTMS106121 / BTDS106121                    OPEN
BCI102990                                                OPEN / RH-BEARING
Riemann Hypothesis                                       UNPROVEN
```
