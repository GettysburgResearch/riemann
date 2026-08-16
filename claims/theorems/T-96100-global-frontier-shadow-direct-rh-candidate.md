# T-96100 — Global frontier-shadow prime sieve and direct Mellin–Landau RH candidate

Claim ID: `T-96100`  
Status: **PROPOSED COMPLETE UNCONDITIONAL RH PROOF CANDIDATE — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-16  
Base: PR #542 at `ca5fb69c15cda29b3b589660f9be44ea2f440677`  
Repository status: **RH is not treated as established**

The corrected chain is

```text
canonical parabolic row
 -> exact global knot measure                    L-96100
 -> source-owned cross-product frontier shadow   L-96101
 -> full Möbius row c_X(j)>=0                    L-96102
 -> fixed-row reciprocal-zeta Mellin transform   L-96000/L-96103
 -> kernel noncancellation                       L-96001/L-96103
 -> Landau real-abscissa theorem
 -> no zero with Re rho>1/2
 -> functional equation
 -> RH candidate.
```

`R-96100` is binding: the old fixed-product proof is not imported.

The proof candidate uses only finite divisor algebra, the four elementary
frontier capacities, classical zeta continuation, Euler--Maclaurin at a fixed
complex exponent, Landau's theorem, and the functional equation.  It does not
use a Mertens square-root estimate, a power-saving PNT error, factor-67
machinery, Target--Lorenz, CPBD, First-Hermite exclusion, or an endpoint
benchmark bridge.

The first review target is `L-96101`, especially global reservoir ownership.
One ownership collision or one negative finite sieve row retracts the proposal.

```text
complete unconditional candidate   yes, on the written global transport
accepted proof                      no
Riemann Hypothesis                  unproved pending reconstruction
```
