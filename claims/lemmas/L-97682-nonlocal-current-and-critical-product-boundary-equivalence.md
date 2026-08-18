# L-97682 — Exact nonlocal Bellman and completed-parity Lorenz producer formulations

Claim ID: `L-97682`  
Status: **PROVED EXACT REDUCTION**  
Created: 2026-08-18  
Depends on: `L-97680`, `L-97681`, PR #581, PR #584  
RH status: **unproved**

Let `R` be the literal raw child operator, `b` the local grouped scalar, and
\[
f=(I+R)^{-1}b.
\]
For any source-faithful contraction `0<=T<=R`, the forced current is
\[
\boxed{
c=(I+T)f=b-(R-T)f.
}
\tag{L-97682.1}
\]
The exact sufficient Bellman condition is
\[
\boxed{
c\ge Tc.
}
\tag{L-97682.2}
\]
Then
\[
f=(I+T)^{-1}c=(I-T^2)^{-1}(c-Tc)\ge0.
\]

Theorem `L-97681` proves that no even stopping depth
`L=O(log log log X)` can supply (L-97682.2). PR #587 rules out every
fixed-cutoff `l^1` substitute. Hence any successful proof must control the
critical histories
\[
\omega(m)\asymp\log\log X
\quad\text{and}\quad
m\asymp X,
\]
where product activation and accumulated parity interact.

A distinct source-complete sufficient producer is obtained by fully expanding the owner ledger at a fixed endpoint. Write the even source atoms
as capacities `a_i`, target coordinates `t_i`, and scalar coordinates `r_i`,
with complete odd demands `(T_O,R_O)`. Then existence of a target-exact scalar-superordinate common-source coupling is equivalent to the finite Lorenz inequality
\[
T_O\le\sum_i a_it_i,\qquad R_O\le\Phi_X(T_O),
\]
where
\[
\boxed{
\Phi_X(T)=
\min_{\lambda\in\mathbb R}
\left[\lambda T+\sum_i a_i(r_i-\lambda t_i)_+\right].
}
\tag{L-97682.3}
\]

Thus the following are distinct sufficient producer formulations for the same unresolved arithmetic correlation. They are not interchangeable without an explicit statement-to-use map:

```text
NCBI67       nonlocal Bellman current
CPSL67       completed-parity scalar Lorenz feasibility
GPHT*        global common-source target/scalar packing
GABPT        activation-boundary parity transport
FCBI         future-prime quotient-profile invariant
```

A proof may establish any one of these on the literal completed source, together with its exact downstream map. A local
margin, a finite-depth Bonferroni block, or a PSD trace is insufficient.
