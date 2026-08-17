# T-97500 — The repaired factor-67 route reduces to one nonlocal Bellman current inequality

Claim ID: `T-97500`  
Status: **PROVED EXACT REDUCTION; PRODUCER OPEN**  
Created: 2026-08-18  
Depends on: `L-97500--L-97502`, `R-97500`, PR #576, the fixed scalar Mellin-Landau consumer  
RH status: **unproved**

Let `R` be the literal raw parity child operator on the finite activated rough
history tree, `b` the complete local grouped scalar, and

\[
 f=(I+R)^{-1}b
\]

the actual `5:3` scalar. Choose any source-faithful contracted operator `T`
whose child mass is below the factor-67 threshold. The exact positive paired
source current is supplied by `L-97501`; its scalar is

\[
 \boxed{
 c=b-(R-T)f.
 } \tag{T-97500.1}
\]

A sufficient fail-closed producer is

\[
 \boxed{
 \mathrm{NCBI}_{67}:
 \qquad c\ge Tc
 } \tag{T-97500.2}
\]

coordinatewise on every activated state. Indeed, the finite positive
`M`-matrix identity

\[
 (I+T)^{-1}=(I-T)(I-T^2)^{-1}
\]

gives

\[
 f=(I+T)^{-1}c\ge0
\]

after (T-97500.2).

Equation (T-97500.1) is nonlocal: it contains the complete raw child scalar
`f`. `R-97500` proves that no universal source-local one-channel replacement
can remove this dependence when `T<R`. `L-97502` proves that the repaired P61
bias and the `<1/8` contracted budget alone do not establish it.

At scalar scope, `NCBI67` is a resolvent form of the same global arithmetic
frontier represented by `CPSL67`, `GPHT*`, `ASHP67`, `GABPT`, `TFPE`, and
`ACBI`. A proof of any one of those statements, with an exact statement-to-use
map into (T-97500.2), yields eventual nonnegativity of the zero-safe `5:3`
scalar and then the existing Mellin-Landau implication to RH.

```text
literal paired-source contracted identity     PROVED
raw coefficient preservation                  PROVED
one-channel local contracted current           IMPOSSIBLE IN GENERAL
raw exposure invariance                       PROVED
NCBI67                                         OPEN / RH-BEARING
NCBI67 -> scalar positivity -> RH              PROVED CONDITIONAL
Riemann Hypothesis                             UNPROVEN
```
