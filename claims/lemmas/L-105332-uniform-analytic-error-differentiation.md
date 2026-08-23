# L-105332 — Uniform analytic shifted explicit formula implies Pick-Gram transfer

Claim ID: `L-105332`  
Status: **PROVED ABSTRACT ANALYTIC TRANSFER**  
Created: 2026-08-23  
Depends on: Cauchy's estimate; `L-105330--L-105331`  
RH status: **not assumed**

Let `Z_T(alpha)` and `P_T(alpha)` be matrix-valued functions analytic on
`|alpha|<r_T`, continuous on the closed disk, and suppose

\[
Z_T(\alpha)=P_T(\alpha)+E_T(\alpha),
\qquad
\sup_{|\alpha|\le r_T}\|E_T(\alpha)\|\le\varepsilon_T
\tag{L-105332.1}

in any submultiplicative matrix norm.  Cauchy's integral formula gives

\[
\boxed{
\|Z_T'(0)-P_T'(0)\|
\le{\varepsilon_T\over r_T}.}
\tag{L-105332.2}

Consequently, if `epsilon_T/r_T=o(S_T)` at the conclusion-facing scale
`S_T`, then the parameter derivatives agree to `o(S_T)`.

Apply this with:

```text
Z_T(alpha) = the oriented shifted-zero statistic for xi'-alpha xi;
P_T(alpha) = its archimedean plus prime-side explicit formula;
H_ij'      = -W^2 phi_i phi_j.
```

By `L-105330`, `Z_T'(0)` is the Wick-preconditioned low-order Pick matrix.
By `L-105331`, `P_T'(0)` has the reciprocal coefficient source from T-105320.
Thus a shifted explicit formula uniform on an alpha disk proves the structural
`GRAMFREEZE105320` transfer.

The pinned coefficient re-expansion already supplies a fixed coefficient-side
radius and differentiated `H1/H2/H3` bounds.  The remaining uniformity is on
the zero-side/seam error, horizontal boundaries and canonical-product tail.

## Quantitative admissibility

If the unshifted entrywise error is `O(T^-delta)` and the same bound holds on
`|alpha|<=r_T`, any radius satisfying

\[
r_T^{-1}T^{-\delta}=o(1)
\]

is sufficient at a unit-normalized entry scale.  For example
`r_T=T^{-delta/2}` leaves derivative error `O(T^{-delta/2})`.
