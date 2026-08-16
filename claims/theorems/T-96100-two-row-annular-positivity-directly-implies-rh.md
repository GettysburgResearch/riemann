# T-96100 — Two-row annular positivity directly implies the Riemann Hypothesis

Claim ID: `T-96100`  
Status: **PROVED CONDITIONAL IMPLICATION / PRODUCER GATE EXPLICITLY OPEN**  
Created: 2026-08-16  
Depends on: `L-96100--L-96102`; Landau's theorem for Mellin transforms  
RH status: **unproved because TAP4 remains open**

Define the two-row annular positivity statement

\[
 \boxed{
 \mathrm{TAP4}:\qquad
 a_2(X)\ge0\text{ and }a_3(X)\ge0
 \quad\text{for every real }X\ge1.
 }
\tag{T-96100.1}
\]

By `L-96100`, it is equivalent to checking all integer endpoints.

Assume `TAP4`. For each `j in {2,3}`, the function `a_j` has at most square-root times polylogarithmic growth by its finite coefficient formula, so its Mellin transform has a finite abscissa of convergence. Since `a_j>=0`, Landau's theorem says that a positive finite real abscissa would be a singularity. But `L-96101` proves that the continued transform is holomorphic at every positive real point. Hence its defining Mellin integral is holomorphic throughout

\[
 \Re s>0.
\tag{T-96100.2}
\]

Suppose `zeta(rho)=0` with `Re(rho)>1/2`, and put `s_rho=rho-1/2`. By `L-96102`, at least one of `P_2(rho),P_3(rho)` is nonzero. Select that fixed row. Equation `L-96101.3` then has a nonremovable pole at `s_rho`; the annular factor is nonzero by `L-96101.5`. This contradicts (T-96100.2).

Thus zeta has no zero with real part greater than one half. The functional equation excludes the reflected half-strip. Therefore

\[
 \boxed{\mathrm{TAP4}\Longrightarrow\mathrm{RH}.}
\tag{T-96100.3}
\]

The implication is unconditional and complete. `TAP4` itself is not proved in this packet. It is the sole surviving producer theorem.

```text
J/P/F endpoint normalization                  not used
full native-row positivity                    not required
all row indices                               not required
prime-square moat                             not used
large-j noncancellation                       not used
two fixed annular rows                        sufficient
TAP4                                          OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVEN
```
