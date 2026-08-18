# L-97902 — Zero-hinge maps and the exact classification of Bellman states

Claim ID: `L-97902`  
Status: **PROVED EXACT INTERFACE THEOREM**  
Created: 2026-08-18  
Depends on: `L-97700--L-97703`, `L-97900--L-97901`  
RH status: **unproved**

For a completed paired source `P=(E,O)`, the oriented Lorenz slacks satisfy

\[
D_P^+(0)=R_E-R_O,
\qquad
D_P^-(0)=R_O-R_E=-D_P^+(0).
\tag{L-97902.1}
\]

For the logarithmic completed source, `D^+(0)` is the native scalar `R_X`. For
the scale-four difference of that source, it is `F_P^{A_*}(X)` of `L-97900`.
Thus the fixed-angle condition

\[
D_P^+(0)\ge\eta M_P
\tag{L-97902.2}
\]

is an auxiliary mass cone. It is neither `CPSL67` nor `NCBI67`.

The exact theorem-level maps inherited from PR #591 are

\[
\mathrm{LBP}_{67}\Longrightarrow\mathrm{CPSL}_{67}
\Longrightarrow D^+(0)\ge0,
\]

\[
\mathrm{NCBI}_{67}\Longleftrightarrow(I-T^2)f\ge0
\Longrightarrow f\ge0.
\tag{L-97902.3}
\]

`R-97900` proves that no condition of the stronger form (L-97902.2), with fixed
`eta>0`, can be invariant under every actual future-prime completion. It does
not alter the valid maps in (L-97902.3).

The smallest exact Markov state remains the two-orientation future-product
quotient profile

\[
\mathbf Z_Q(m,\lambda)=
\left(D_Q^+(X/m,\lambda),D_Q^-(X/m,\lambda)\right),
\]

with update

\[
\mathbf Z_{Q\cup\{p\}}(m,\lambda)
=
\mathbf Z_Q(m,\lambda)
+p^{-1/2}J\mathbf Z_Q(mp,\lambda),
\qquad
J(u,v)=(v,u).
\tag{L-97902.4}
\]

At `lambda=0` the positive Lorenz cushion vanishes. Hence no target-coordinate
reserve can hide the scalar failure of a proposed fixed-angle cone. Any complete
proof must control the signed Euler-minus profile itself.
