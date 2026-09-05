# T-105230 — Companion-index budget for 90% and density one

Claim ID: `T-105230`  
Status: **PROVED CONDITIONAL IMPLICATION; companion boundary estimate open**  
Depends on: L-105221; L-105230; L-105231

For each `1<=k<=K`, choose `lambda_k>=0`, `delta_k>0`, and a regular thin
collar `Omega_k(T)` as in L-105231.  Let
\[
I_k(T)=\frac1{2\pi i}
\int_{\partial\Omega_k(T)}
\mathscr S_{k,\lambda_k,\delta_k}(z)\,dz
\]
and let
\[
P_k(T)=
\sum_{G_{k,\delta_k}(\zeta)=0,\ \zeta\in\Omega_k(T)}
\pi_{k,\lambda_k,\delta_k}(\zeta).
\]
Because the collar contains only real zeros of `F_k`, L-105230 gives
\[
\mathcal D_k(\lambda_k)=\Re I_k(T)-\Re P_k(T).
\]
Therefore
\[
\boxed{
\mathcal D_k(\lambda_k)
\le
(\Re I_k(T))_+ + (-\Re P_k(T))_+.
}
\tag{1}
\]
Summing the exact reverse--Rolle loss gives
\[
\boxed{
R_0(T)
\ge
R_K(T)
-2\sum_{k=1}^K
\left[(\Re I_k(T))_+ + (-\Re P_k(T))_+\right]
-K.
}
\tag{2}
\]

If `R_K(T)/N(T)>=p_K-o(1)` and
\[
\limsup\frac1{N(T)}
\sum_{k=1}^K
\left[(\Re I_k(T))_+ + (-\Re P_k(T))_+\right]
<\frac{p_K-0.9}{2},
\]
then more than 90% of the zeros lie on the critical line.  If the same charge
is `o(N)`, `p_K->1`, and all endpoint/multiplicity ledgers are `o(N)`, then the
critical-line proportion tends to one.

The exact remaining statement is

```text
CIBF105230:
control the one-sided companion boundary flux and negative companion-pole
amplitude in the matching derivative windows.
```

The advance over `IBFC105222` is structural: arbitrary interpolation and its
coalescing-node norm are gone.  Every new pole is a canonical companion zero,
and its lower-half-plane count is owned by the nonreal-pair index of `F_k`.
`CIBF105230` is open; 90%, density one, and RH are not established.
