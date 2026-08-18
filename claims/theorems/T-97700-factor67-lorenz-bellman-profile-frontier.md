# T-97700 — Exact factor-67 Lorenz-Bellman profile frontier

Claim ID: `T-97700`  
Status: **UNCONDITIONAL REDUCTION + INVARIANT CONE; ARITHMETIC MEMBERSHIP OPEN**  
Created: 2026-08-18  
RH status: **unproved**

## Frozen inputs

```text
main             f789265569013ebff254b082c2e0428970bdaf57
PR #576          0f6ea6eae813c1d867ae50744cf5fd57e2720bb7
PR #581          62aaa54ac49f0aa89fd58f14a539cc53089f884c
PR #582          699f9f119a66823702e96fba95cc8b14b8251c60
PR #584          e919c6afd1e95fffa505f7ba3f532cb12b8c410c
PR #587          8a0f074c5b96600b461fdd6e23b47ee2162c4a70
```

Let `D_0^+` be the forward Lorenz dual slack of the complete small-prime `P_61` source and

\[
\mathcal P_Q^-=\prod_{p\in Q}(I-p^{-1/2}U_p)
\]

for a finite rough-prime set `Q`. If

\[
\boxed{\mathrm{LBP}_{67}:\quad \mathcal P_Q^-D_0^+(X,\lambda)\ge0}
\]

for every finite `Q`, real `X>0`, and real `lambda`, then

\[
\boxed{\mathrm{LBP}_{67}\Longrightarrow\mathrm{CPSL}_{67}\Longrightarrow R_X=5c_X(2)+3c_X(3)\ge0\text{ eventually}\Longrightarrow\mathrm{RH}.}
\tag{T-97700.1}
\]

The first implication is `L-97701`; the second is the exact scalar consequence of completed-parity Lorenz feasibility; the final implication is the fixed `5:3` Mellin-Landau consumer reconstructed in PR #584.

## Closed in this packet

```text
literal completed-parity owner ledger                 imported exact
finite Lorenz primal/dual                              proved exact
source-faithful D^plus,D^minus                         proved exact
rough-prime recurrence                                 proved exact
universal odd-subset cushion                           proved exact
future-prime product quotient recurrence               proved exact
LBP67 invariant-cone mechanism                         proved exact
NCBI67/CPSL67 theorem map                              proved exact
NCBI67 <-> CPSL67                                      refuted abstractly
smallest two-sided cone                                refuted at X=1
finite separator localization                          proved exact
```

## First open theorem

The remaining arithmetic theorem is exact membership of the `P_61` forward Lorenz slack in the complete rough-prime Euler-minus cone:

\[
\prod_{p\in Q}(I-p^{-1/2}U_p)D_0^+(X,\lambda)\ge0.
\]

It is stronger than CPSL away from `lambda=0`, but at zero the universal cushion vanishes and the identity becomes the actual completed scalar. No RH-equivalent sign estimate is imported under another name.

The retained diagnostic finds no Bellman-cone failure through horizon `256`. The complete global Lorenz LP at the mandatory odd-history endpoint `X=61841` is also feasible with positive floating slack. These are falsification diagnostics, not all-scale proofs.

```text
LBP67                 OPEN / RH-BEARING
CPSL67                OPEN / IMPLIED BY LBP67
NCBI67                OPEN / INDEPENDENT SUFFICIENT ROUTE
Riemann Hypothesis    UNPROVED
```