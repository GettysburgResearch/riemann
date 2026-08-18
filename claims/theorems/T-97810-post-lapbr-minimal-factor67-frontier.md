# T-97810 — Corrected post-LAPBR factor-67 frontier

Claim ID: `T-97810`  
Status: **UNCONDITIONAL HARDENING AND SHARP CONDITIONAL REDUCTION — PRODUCER OPEN**  
Created: 2026-08-18  
Frozen base: PR #590 at `223f11259b3e7134f78d6492795e6e94caca8be3`  
Compared: PR #589 and PR #591  
RH status: **unproved**

The following statements are now unconditional.

1. The complete `P_61` annular `5:3` base and complete small-prime cube survive.
2. `LAPBR67` is false.
3. More generally, every even count-depth current with
   `L log(2L)=o(sum_(67<=p<=X)1/p)` is eventually negative (`R-97810`).
4. The exact largest-prime Bellman identity of PR #590 is source faithful.
5. At the root, the remaining scalar theorem is exactly `RBLPTE67`, not its
   stronger state-wise version.
6. In the completed Lorenz formulation, the same scalar is the zero hinge
   `D^+(0)`.  Full `CPSL67` implies it but is strictly stronger in general.

The conclusion-producing chain is

\[
 \boxed{
 \mathrm{RBLPTE67}
 \Longleftrightarrow
 U_{\rm full}(X)\ge0\ \text{eventually}
 \Longrightarrow
 \mathrm{RH}
 }
\tag{T-97810.1}
\]

through the frozen zero-safe annular Mellin--Landau consumer.

This packet does not prove `RBLPTE67`.  It removes two unnecessary burdens from
the target:

- positivity of any shallow count-depth residual;
- all-state/all-hinge feasibility when only the root scalar is being consumed.

A future proof may still choose the stronger Lorenz-Bellman route, but it must
state the implication to the zero hinge explicitly.

```text
complete small-prime cube                  RETAINED
LAPBR67                                    REFUTED
all subcritical count depths               REFUTED
largest-prime source identity              RETAINED EXACT
root-only Bellman budget                   MINIMAL EXACT TARGET
zero-hinge map                             PROVED EXACT
CPSL67 -> root scalar                      PROVED
root scalar -> CPSL67                      FALSE IN GENERAL
RBLPTE67                                   OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVEN
```
