# R-105400 — Pointwise critical-cell convergence does not control the remote tail moments

Claim ID: `R-105400`  
Status: **PROVED EXACT SCOPE REFUTATION**  
Created: 2026-08-23  
Depends on: `L-105387`, `T-105400`  
RH status: **not assumed**

Compact or growing-prefix convergence must not be promoted to remote-tail
moment matching without a separate tail theorem.

## 1. An escaping extra atom

Let `nu_p` be either complete unit-scale trigonometric critical measure. For
integer `r>=1`, define

\[
\boxed{
\widetilde\nu_r
=
\nu_p+\delta_{1/r^2}.
}
\tag{R-105400.1}
\]

Every fixed trigonometric atom is present with exactly the correct location and
weight. Thus every fixed central-cell comparison is perfect, and any prefix
whose indexing ignores the inserted remote atom is unchanged.

Nevertheless, the total-mass discrepancy is

\[
\boxed{
\int1\,d(\widetilde\nu_r-\nu_p)=1
}
\tag{R-105400.2}
\]

for every `r`. Hence the order-one unshifted tail moment does not converge at
all.

For every fixed `n>=1`, the same extra atom contributes only

\[
r^{-2n}\longrightarrow0.
\]

Thus even convergence of all strictly positive moments can coexist with a
persistent zeroth-moment capacity defect.

## 2. Matrix consequence

At order one, the source-normalized unshifted critical matrix receives the
extra scalar `[1]`. If the trigonometric model already saturates the source
capacity, the added atom produces

\[
\boxed{
A_1^{(0)}-\widetilde C_{1,r}^{(0)}=[-1].
}
\tag{R-105400.3}
\]

The boundary reserve is negative despite exact convergence of every fixed
original critical cell.

## 3. Consequence for the Xi programme

The following implications are invalid without an additional tail estimate:

```text
fixed-cell trigonometric convergence
  -> RTMH105400(k);

growing-prefix capacity
  -> complete capacity;

pointwise residue asymptotics
  -> remote-tail total-mass control.
```

The remote-tail gate must include at least the zeroth moment and, at order `k`,
all moments through `2k-1` or a stronger weighted-measure bound.

## 4. Scope

The added atom is an abstract escaping-tail separator, not an Xi critical
point. It proves that no source-free compactness argument supplies the missing
remote-tail moments. Special Xi structure may exclude such escaping mass, but
that exclusion is exactly the open analytic theorem.
