# T-106020 — Source-paid owner-conductor L-family frontier

Claim ID: `T-106020`  
Programme aliases: `LFAM1.OWNER_CONDUCTOR_MOMENT`, `LFAM2.KUMMER_TRACE_HANDOFF`, `STRESS.SHORT_CORE_FAMILY_FRONTIER`  
Status: **MAJOR EXACT THREE-PROGRAM REDUCTION; COHERENT MOMENT OPEN**  
Created: 2026-08-24  
Base: PR #719 at `c2e82cfdd254a478731f005b3d83b49d3e1e33ea`  
Depends on: `L-106020--L-106023`; `R-106020`; PR #719 `L-102883`, `L-102886--L-102888`  
Programme issues: #743, #736, #737  
RH status: **unproved**

## 1. Current arithmetic source

The moving parent has reduced the derivative common-mother current to the
horizon-safe owner-excluded balanced row

```text
HBCQDSP102888.
```

The blockwise cutoff is fixed, the Type-I lattice is power-small, and the
largest-two smooth-boundary row is absent. After the existing shared-owner and
owner/core-overlap renewals, every direct packet has

\[
N=pq\,a^2,
\qquad
M=rs\,b^2
\]

with four distinct owner labels and clean opposite cores.

## 2. Exact improvement of the phase interface

The former fixed-packet estimates used generic Cauchy over `rho-1` and `pi-1`
nonzero phases. `L-106020` proves that square support changes the finite Fourier
geometry:

\[
\left\|\sum_{h\ne0}F_h\right\|^2
\le{\rho-1\over\rho+1}
\sum_{h\ne0}\|F_h\|^2.
\]

Thus all phase-cardinality factors disappear. For any opposite owners
`rho in {r,s}` and `pi in {p,q}`,

\[
|\mathcal C_{P,Q}|
\ll
{1\over\sqrt{pqrs}}
\left(1+{\rho\over A}\right)^{1/2}
\left(1+{\pi\over B}\right)^{1/2}.
\tag{T-106020.1}
\]

Choosing the smaller opposite owners gives

\[
\boxed{
|\mathcal C_{P,Q}|
\ll
{1\over\sqrt{pqrs}}
\left(1+{s\over A}\right)^{1/2}
\left(1+{q\over B}\right)^{1/2}.
}
\tag{T-106020.2}
\]

This retains every owner weight. It is a strict fixed-packet improvement, not
yet a coherent owner summation.

## 3. Exact L-family diagonalization

For an opposite owner conductor `rho`, the nonzero additive square-phase energy
is exactly

\[
\boxed{
{\rho+1\over\rho-1}\|F_1\|^2
+{2\rho\over\rho-1}
\sum_{\substack{\eta\ ({\rm mod}\ \rho)\\
                 \eta(-1)=1,\ \eta\ne1}}
\|F_\eta\|^2.
}
\tag{T-106020.3}
\]

Here `F_1` is the native untwisted core field and every `F_eta` is the exact
owner-excluded Vaughan field twisted by an even Dirichlet character. Its full
core Euler product contains

\[
L(2s,\eta)^{-1}
\]

with only the two owner Euler factors removed.

The principal/quadratic square-root fibre supplies the coefficient
`(rho+1)/(rho-1)>1`. Therefore this family has **source-paid principal
leverage**. The separate auxiliary-amplifier premise `PLEV106001` is not needed
on this route.

## 4. Inherited closed sector

The abstract coherent phase-packing theorem `L-102883` applies to every
deterministic clean owner pair. With the literal owner weights retained, it
closes the weighted long-core sector

\[
B\ge L_1L_2
\]

at subpower cost. The horizon-safe transfer changes the labelled source norm by
only the already-recorded polylogarithmic pair-gauge factor.

Thus the open owner-conductor moment may be restricted to the balanced blocks
not covered by that theorem, including the genuinely short-core and
owner-allocation coupling.

## 5. Exact remaining theorem

Define

```text
SOCM106020:
  after carrier recombination, Wick quotient, horizon-safe pair allocation,
  overlap renewals and dyadic-frozen owner-excluded Vaughan decomposition,
  the coherent source-weighted moment of the surviving short-core packets,
  written in the even owner-conductor Dirichlet-character basis of
  T-106020.3, has subpower logarithmic energy/negative mass.
```

The moment must retain in one ledger:

```text
the untwisted principal/quadratic root fibre;
all nonprincipal even L(2s,eta) channels;
the exact Gauss weights;
the smaller-opposite-owner choice or a declared coherent selector;
the literal owner coefficients;
all physical distinct-product restrictions.
```

A bound only for nonquadratic characters does not prove `SOCM106020`, because
the quadratic square root is an exact copy of the untwisted core field.

Then

\[
\boxed{
\mathrm{SOCM}_{106020}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\int_1^Y(H_K)_-{dX\over X}=Y^{o(1)}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106020.4}
\]

`SOCM106020` remains open.

## 6. Function-field handoff

Over `F_q[T]`, the same local family is the Kummer--Fourier transform of the
square map, with exact principal embedding `L-106023.3`. Define

```text
FFSOCM106023:
  control the incomplete owner-excluded Möbius/Vaughan Kummer--Artin--Schreier
  traces coherently over owner irreducibles, with explicit resonant strata and
  memberwise-versus-average scope.
```

A useful proof should export the corresponding number-field hybrid
character/exponential-sum theorem. Function-field RH alone is not the missing
input.

## 7. Exact boundary

```text
horizon-safe pair / no smooth boundary          INHERITED PROVED
square-phase Gauss--Mellin identity             PROVED EXACT
phase-cardinality removal                       PROVED EXACT
all-owner-weight fixed-packet bound              PROVED
owner-conductor even L-family                    PROVED EXACT
local principal leverage                         PROVED EXACT
long-core coherent packing                       INHERITED PROVED
quadratic-root independence                      REFUTED
SOCM106020 coherent short-core moment             OPEN / RH-BEARING
FFSOCM106023 geometric trace moment               OPEN / EXPLORATORY
HBCQDSP102888                                    OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVED
```