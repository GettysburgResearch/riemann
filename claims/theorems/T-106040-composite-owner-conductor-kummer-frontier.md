# T-106040 — Corrected composite owner-conductor Kummer frontier

Claim ID: `T-106040`  
Programme aliases: `LFAM1.COMPOSITE_OWNER_CONDUCTOR_MOMENT`, `LFAM2.PRODUCT_KUMMER_HANDOFF`, `STRESS.MULTI_OWNER_ASSEMBLY`  
Status: **EXACT COMPOSITE-FAMILY REDUCTION; ASSEMBLY OPEN**  
Created: 2026-08-24  
Depends on: `L-106040`; `R-106040`; `T-106020`, `T-106030`; PR #719 `HBCQDSP102888`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The square-phase family can be formed simultaneously at any source-selected
squarefree product of opposite owner primes. The correct frame is the tensor
frame of `L-106040`, not the withdrawn scalar formula in `R-106040`.

## 1. Source-selected composite conductor

On one clean CV/XD packet

\[
N=pq\,a^2,
\qquad
M=rs\,b^2,
\]

choose nonempty source-owned sets

\[
S_N\subseteq\{r,s\},
\qquad
S_M\subseteq\{p,q\}.
\]

Put

\[
Q_N=\prod_{\rho\in S_N}\rho,
\qquad
Q_M=\prod_{\pi\in S_M}\pi.
\]

These conductors are fixed by the physical occurrence before any hypothetical
zero, character, phase, norm or regional estimate is introduced.

For each side, retain the full local quadratic-class vector

\[
\sigma_N\in\{\pm1\}^{|S_N|},
\qquad
\sigma_M\in\{\pm1\}^{|S_M|}.
\]

The complete tensor nonzero-phase moment then has local observation constants

\[
c(Q_N)=\prod_{\rho\in S_N}\frac{\rho-1}{\rho+1},
\qquad
c(Q_M)=\prod_{\pi\in S_M}\frac{\pi-1}{\pi+1}.
\tag{T-106040.1}
\]

No phase-cardinality factor and no family-dimension factor occurs inside one
fixed class sector.

## 2. Composite owner-conductor `L`-channels

After the Gauss--Mellin change of basis, the core channels are tuples of local
even Dirichlet characters. Their reciprocal core Euler product is the exact
multi-conductor version of `L-106022`, with only the deterministic owner Euler
factors removed.

The complete principal/quadratic root fibre has weight

\[
c(Q_N)^{-1}
\quad\text{or}\quad
c(Q_M)^{-1}
\]

on the corresponding side. Thus principal leverage remains source-paid in
every class sector.

The `2^omega(Q)` quadratic roots are one coherent fibre, not independent
oscillating channels. Recombining their local squareclass sectors before the
positive frame would lose the sharp contraction.

## 3. Exact open moment

Define

```text
CCSOCM106040:
  after the full-source completion order of R-106001, carrier recombination,
  Wick quotient, horizon-safe owner allocation, overlap renewals and the
  dyadic-frozen owner-excluded Vaughan decomposition, the coherent assembly of
  the surviving short-core packets has subpower logarithmic energy when
  written in the complete tensor locally-even character bases attached to the
  selected composite opposite-owner conductors, with every local quadratic-
  class vector retained until after the sector frame is applied.
```

The ledger must include:

```text
all principal/quadratic roots;
all nonprincipal locally-even characters;
exact local Gauss weights;
physical owner coefficients;
finite shell projections;
source-selected conductor subsets;
quadratic-class vectors;
all collisions between distinct owner packets.
```

The theorem permits a deterministic selector among the finitely many nonempty
conductor subsets. It does not permit selecting a conductor after seeing a
hypothetical zero or reusing owner weights already spent by a parent packing
theorem.

## 4. Conclusion chain

The prime-conductor route `SOCM106020` is the special case in which each
selected conductor has one prime. Conversely, the composite tensor frame gives
another exact coordinate system for the same physical current. Therefore

\[
\boxed{
\mathrm{CCSOCM}_{106040}
\Longrightarrow
\mathrm{HBCQDSP}_{102888}
\Longrightarrow
\int_1^Y(H_K)_-\frac{dX}{X}=Y^{o(1)}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-106040.2}
\]

`CCSOCM106040` remains open.

## 5. Function-field target

Define `FFCCSOCM106040` to be the corresponding coherent moment for squarefree
polynomial owner conductors. A useful proof must retain the product Kummer
sheaf, all local Artin--Schreier phases, the complete quadratic-root fibre,
resonant strata, conductor growth and the distinction between memberwise and
family-averaged cancellation.

Its purpose is to identify a number-field hybrid character or relative-trace
estimate. Function-field RH alone does not imply (T-106040.2).

## Exact boundary

```text
composite principal Euler completion          PROVED EXACT
tensor local Kummer frame                     PROVED EXACT
quadratic-class sector decomposition          PROVED EXACT
sector principal leverage                     PROVED EXACT
scalar phi(q)/q leverage formula               REFUTED
CCSOCM106040 composite coherent assembly       OPEN / RH-BEARING
FFCCSOCM106040 geometric product moment        OPEN / EXPLORATORY
HBCQDSP102888                                  OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVED
```
