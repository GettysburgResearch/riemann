# T-98900 — Corrected status of the fractional Julia–Tao–Hermite candidate

Claim ID: `T-98900`  
Status: **PROVED REJECTION OF T-98700 AS SUBMITTED; REPAIRED ROUTE OPEN**  
Created: 2026-08-18  
Frozen input: PR #613 at `f28aa51a6d6740067202611d8ebda4be2ef0a1c9`  
RH status: **unproved**

The submitted fractional Julia–Tao–Hermite chain does not prove the Riemann
Hypothesis.

1. `L-98900` proves that the exact packet written in `L-98702` has unavoidable
   center-zero energy exponent `1/2`, arising from the branch at the real zeta
   pole `s=1`.
2. `R-98900` proves that this contradicts `L-98703.1` whenever
   `0<theta<1/192`.
3. `L-98901` proves that the unphased Tao completion is not covariant under the
   logarithmic phase used by the heat packet; an exact one-prime fixture has
   determinant `-80/81`.
4. `R-98901` proves that the claimed phase-ready Fock direct limit and uniform
   trace bound do not follow from the local Tao atoms.

Therefore `L-98703`, `L-98704`, and `T-98700` are rejected in their submitted
forms. The exact positive-chaos coefficient identities of `L-98700` and the
unphased local Tao decomposition of `L-98701` remain valid within their stated
algebraic scopes.

A future fractional-heat proof must construct a different observable satisfying
all gates in `M-98900`: complete pole subtraction, a new off-line-zero lower
interface, a phase-covariant positive source, a uniform heat-rate upper bound,
and a proof-grade cutoff exhaustion.

```text
fractional coefficient algebra                 RETAINED
unphased Tao port                               RETAINED
submitted heat upper bound                      FALSE
submitted phase-ready Fock interface            FALSE
T-98700 RH candidate                            REJECTED AS SUBMITTED
pole-subtracted phase-covariant replacement     OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
