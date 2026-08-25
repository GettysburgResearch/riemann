# L-105481 — The F1 square is an exact positive Gram with one oriented distinct-product off-diagonal

Claim ID: `L-105481`

Status: **PROVED EXACT GRAM/NEAR-COLLISION REDUCTION; OFF-DIAGONAL ESTIMATE OPEN**

Retain

\[
\delta_m=\frac14\sum_n a_nK_L(m/n)
\]

and the square energy `mathcal E_M` of `L-105480`.  Define

\[
\boxed{
G_M(n,r)
=\frac1{16}
\sum_{m=M}^{2M}
\frac{K_L(m/n)K_L(m/r)}m.
}
\tag{L-105481.1}
\]

Finite expansion gives

\[
\boxed{
\mathcal E_M
=\sum_{n,r}a_n\overline{a_r}G_M(n,r).
}
\tag{L-105481.2}
\]

## 1. Positivity and exact support

For every finite scalar sequence `(c_n)`,

\[
\sum_{n,r}c_n\overline{c_r}G_M(n,r)
=\frac1{16}\sum_{m=M}^{2M}
\frac{\left|\sum_nc_nK_L(m/n)\right|^2}{m}
\ge0.
\tag{L-105481.3}
\]

Thus `G_M` is positive semidefinite.

If one summand in (L-105481.1) is nonzero, then

\[
1\le m/n<8,
\qquad1\le m/r<8.
\]

Therefore

\[
\boxed{
G_M(n,r)=0
\qquad\text{unless}\qquad
\frac18<\frac nr<8.
}
\tag{L-105481.4}
\]

The square is a compact multiplicative near-collision Gram.

## 2. The diagonal is closed

The fixed kernel satisfies

\[
\|K_L\|_\infty=8\sqrt2.
\]

Consequently

\[
0\le G_M(n,n)
\le8\sum_{m=M}^{2M}\frac1m
\ll1.
\tag{L-105481.5}
\]

Put

\[
D_M=\sum_n|a_n|^2G_M(n,n).
\]

The frozen coefficient energy gives

\[
\boxed{D_M=M^{o(1)}.}
\tag{L-105481.6}
\]

## 3. Exact oriented off-diagonal frontier

Put

\[
\mathcal N_M
=\sum_{n\ne r}a_n\overline{a_r}G_M(n,r).
\tag{L-105481.7}
\]

The quantity is real because `G_M` is Hermitian, and

\[
\mathcal E_M=D_M+\mathcal N_M\ge0.
\]

Hence

\[
(\mathcal N_M)_+\le\mathcal E_M
\le D_M+(\mathcal N_M)_+.
\tag{L-105481.8}
\]

Define

```text
F1HCNC105481:
  (N_M)_+ = M^(o(1)) on every frozen dyadic source block.
```

Equations (L-105481.6)--(L-105481.8) give

\[
\boxed{
\mathrm{F1HCNC}_{105481}
\Longleftrightarrow
\mathrm{F1GRAM}_{105480}.
}
\tag{L-105481.9}
\]

This is an **oriented signed** off-diagonal statement.  Replacing it by the
absolute sum of all distinct-product overlaps is a strictly stronger and
unsupported theorem.

## 4. Relation to the inherited near-collision programmes

The algebra is the same physical mechanism isolated in `L-102703` and in the
half-completed Haar criterion `L-103100--L-103102`, now for the canonical
F1/Boolean equal-pair source and the fixed derivative-outer kernel.

All finite owner, Hodge, completion, repeated-label, equal-product and endpoint
layers have disappeared from (L-105481.7).  The unproved term is cancellation
between **different physical products** in a fixed ratio-eight overlap.
