# L-91730 — Weighted Julia channels admit an exact ordered tensor-cascade identity

Claim ID: `L-91730`  
Status: **PROVED EXACT FULL-POLARIZATION SOURCE CASCADE**  
Created: 2026-08-13  
Depends on: `L-91630/L-91631`, `L-91530`  
RH status: **unproved**

## 1. Abstract weighted Julia channels

For `j=1,...,N`, let `K_j^-` and `K_j^+` be positive kernels on the same
label set and suppose

\[
\boxed{
K_j^-=K_j^++D_j,
\qquad D_j\succeq0.
}
\tag{L-91730.1}
\]

In the applications, `K_j^-` is a hard weighted carrier source, `K_j^+` is
its coefficient-one returned safe source, and `D_j` is the declared Julia
detail.

## 2. Ordered product identity

Use pointwise/Schur products of kernels. Then

\[
\boxed{
\prod_{j=1}^N K_j^-
-
\prod_{j=1}^N K_j^+
=
\sum_{j=1}^N
\left(\prod_{\ell<j}K_\ell^+\right)
D_j
\left(\prod_{\ell>j}K_\ell^-\right).
}
\tag{L-91730.2}
\]

This is the ordinary telescoping identity with a source ordering.

Every term on the right is positive semidefinite by the Schur product theorem.
Thus the complete hard source equals

```text
one returned safe product
+ one positive detail channel for each source factor.
```

No cross-carrier term is discarded.

## 3. Hilbert-space realization

Suppose

\[
\mathcal J_jf=(m_jf,d_jf)
\]

is an isometric Julia column between the corresponding weighted Hilbert
spaces, with `|m_j|^2+|d_j|^2=1` in the resident measure.

Cascading the columns on the returned branch gives an isometry whose returned
component is

\[
m_1m_2\cdots m_N
\]

and whose `j`-th detail is

\[
d_j\prod_{\ell<j}m_\ell.
\]

Its polarized Gram identity is exactly (L-91730.2), after the later hard
source factors are included in the resident tensor space.

## 4. Entropy chain

On every strictly positive diagonal,

\[
\boxed{
\log\frac{\prod_j K_j^-(x,x)}
          {\prod_j K_j^+(x,x)}
=
\sum_j
\log\frac{K_j^-(x,x)}
          {K_j^+(x,x)}.
}
\tag{L-91730.3}
\]

Each summand is the Clark resolvent entropy of the corresponding Julia
detail. Hence the source norm and the source entropy are both coefficient-one
and generation ordered.

## 5. Scope

This theorem completes the arithmetic **source** cascade. It does not identify
the returned and detail channels with the critical, stable, hyperbolic, and
auxiliary outputs of the horizontal Xi model.
