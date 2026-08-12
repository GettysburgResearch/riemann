# T-91730 — Canonical completed arithmetic Julia exhaustion would prove RH

Claim ID: `T-91730`  
Status: **FULL CONDITIONAL RH PROPOSAL / CANONICAL MODEL MAP OPEN**  
Created: 2026-08-13  
Depends on: `L-91730/L-91731`, `R-91730`, `T-91630`  
RH status: **unproved**

Fix `0<omega<1/2`. Let

\[
\mathcal S_\omega^{\rm arith}
\]

be the explicit eta/bridge/rational/gamma Julia cascade of `L-91731`.

> **Canonical Arithmetic Julia Exhaustion (`CAJE_omega`).** Construct a
> source-ordered minimal colligation
>
> \[
> \mathfrak U_\omega:
> \mathcal S_\omega^{\rm arith}
> \longrightarrow
> \mathcal H_\omega^{\rm crit}
> \oplus
> \mathcal H_\omega^{\rm st}
> \oplus
> \mathcal H_\omega^{\rm hyp}
> \oplus
> \mathcal E_\omega
> \]
>
> whose visible analytic transfer is exactly
> `xi(s-omega)/xi(s+omega)`, and prove
>
> \[
> \boxed{
> \|\Phi_\omega^{\rm arith}\|^2
> =
> \|k_\omega^{\rm crit}\|^2
> +
> \|k_\omega^{\rm st}\|^2.
> }
> \]

Then the hyperbolic and auxiliary components vanish. The horizontal half-plane

\[
\Re s>\frac12+\omega
\]

is zero free. Proving `CAJE_(omega_j)` for one sequence `omega_j->0` proves
RH.

A cofinal approximate form is also sufficient if its canonical residual
entropy is `o(1/Y)` at the optimized moving node of `L-91720`.
