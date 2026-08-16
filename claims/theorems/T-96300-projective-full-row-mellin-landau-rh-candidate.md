# T-96300 — Canonical projective full-row positivity gives a direct Mellin–Landau RH candidate

Claim ID: `T-96300`
Status: **COMPLETE UNCONDITIONAL PROOF CANDIDATE — HOSTILE INDEPENDENT RECONSTRUCTION REQUIRED**
Created: 2026-08-16
Base: frozen PR #534 at `ef18bdda5a65334695008e4c1f5986833160d84f`
RH status: **not treated as established by publication**

The proof candidate is:

```text
#541 normalization correction
 -> discard PR #534 endpoint-packing consumer
canonical native source only
 -> exact paired least-prime stopping tree
 -> no intermediate child observation
complete compact Target-Lorenz determinant
 + MPFR-directed 51,118,080-event tail
 -> every canonical terminal leaf is a nonnegative row
projective one-use gluing
 + directed outer native rows
 -> c_X(j)>=0 for every X,j
fixed rows j=2,3
 -> reciprocal-zeta Mellin transforms
 -> exact two-row noncancellation
 -> Landau
 -> RH candidate.
```

Assume for contradiction that `zeta(rho)=0` with `Re rho>1/2`, and put
`s=rho-1/2`.  By `L-96303`, at least one of rows `j=2,3` has
`P_j(rho)!=0`.  Its meromorphic formula has a nonremovable pole at `s`, while
`L-96302` makes the defining Mellin density nonnegative and Landau makes the
same transform holomorphic throughout `Re s>0`.  This is a contradiction.
The functional equation then places every nontrivial zero on the critical line.

No native endpoint benchmark, `F_Lambda` estimate, factor-67 physical child,
Volterra causal difference, full-child capacity, CPBD, Mertens square-root
bound, power-saving PNT error, zero-density theorem, or `J_Lambda-4sqrt(X)`
bridge is used.

## Immediate falsifiers

Reject the candidate at the first occurrence of:

1. a failed MPFR inclusion or nonpositive tail determinant;
2. an uncovered compact/tail boundary cell;
3. a terminal canonical leaf outside the AVLT hypotheses;
4. a duplicated or omitted squarefree source owner;
5. a change from canonical `Q` to a Volterra derivative family;
6. physical observation of an intermediate oriented child;
7. failure of the projective source identity (L-96302.5);
8. an error in the fixed-row Mellin transform;
9. a common open-strip zero of `P_2,P_3`;
10. failure of the stated Landau hypotheses.

```text
complete unconditional candidate     yes
machine replay proves RH              no
accepted proof                        no
Riemann Hypothesis                    unproved pending review
```
