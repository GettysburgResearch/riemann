# L-99722 — Convex first-owner decoupling and a uniform compact-kernel diagonal

Claim ID: `L-99722`  
Status: **PROVED EXACT OPERATOR INEQUALITY**  
Created: 2026-08-20  
Depends on: `L-99720`; PR #659 compact ratio-eight filter  
RH status: **not assumed**

Let `U_1,...,U_k` be commuting isometries, let `0<r_i<1`, and put

\[
s_0=1,
\qquad
s_i=\prod_{h\le i}(1-r_h),
\qquad
\lambda_i=r_i s_{i-1}.
\]

For a linear observation `O` with values in a Hilbert space, define

\[
F_i=\prod_{h=i}^k(I-r_hU_h)f,
\qquad
\Delta_i=(I-U_i)F_{i+1}.
\]

## 1. Scalar one-prime convexity

For arbitrary Hilbert-space vectors `a,b` and `0<=r<=1`,

\[
\boxed{
\|a-rb\|^2
\le
(1-r)\|a\|^2+r\|a-b\|^2.
}
\tag{L-99722.1}
\]

The right side minus the left side is exactly

\[
r(1-r)\|b\|^2\ge0.
\]

Applying (L-99722.1) successively to the observed future profiles gives

\[
\boxed{
\left\|O\prod_{i=1}^k(I-r_iU_i)f\right\|^2
\le
s_k\|Of\|^2
+
\sum_{i=1}^k\lambda_i\|O\Delta_i\|^2.
}
\tag{L-99722.2}
\]

Since

\[
s_k+\sum_i\lambda_i=1,
\]

this is a genuine convex first-owner decomposition. In particular, every
cross term between different first owners has been removed before any
arithmetic estimate is made.

## 2. Compact ratio-eight observation

Let `K` be the zero-safe compact kernel of PR #659:

\[
K(y)=
\begin{cases}
4\sqrt y-3,&1\le y<2,\\
(4-2\sqrt2)\sqrt y,&2\le y<4,\\
6-2\sqrt2\sqrt y,&4\le y<8,\\
0,&\text{otherwise}.
\end{cases}
\]

Then `|K(y)|<=3` and `supp K` is contained in `[1,8]`.
For a free future-prime profile write

\[
n_A=\prod_{p\in A}p,
\qquad
r_A=n_A^{-1/2},
\]

and for an owner prime `p_i>=67` put

\[
d_{i,A}(X)=K(X/n_A)-K(X/(p_i n_A)).
\]

The same subset atom cannot activate both terms because `p_i>8`. Hence the
literal diagonal of the owner observation is

\[
D_i(X)=\sum_A r_A^2|d_{i,A}(X)|^2.
\]

Unique factorization and the harmonic-interval estimate give

\[
\begin{aligned}
D_i(X)
&\le
9\sum_{X/8\le n\le X}\frac1n
+9\sum_{X/(8p_i)\le n\le X/p_i}\frac1n\\
&\le 18(1+\log8)<60.
\end{aligned}
\tag{L-99722.3}
\]

The restriction to future squarefree products can only decrease these sums.
Consequently

\[
\boxed{
\sum_i\lambda_iD_i(X)<60.
}
\tag{L-99722.4}
\]

Thus the compact physical packet has two interfaces already closed:

```text
cross-owner interference     removed exactly by convex first ownership;
diagonal owner energy        bounded by an absolute constant.
```

## 3. Exact residual Gram

For each owner write

\[
O_X\Delta_i
=
\sum_A(-1)^{|A|}r_A d_{i,A}(X).
\]

Then

\[
|O_X\Delta_i|^2=D_i(X)+C_i(X),
\]

where

\[
\boxed{
C_i(X)=
\sum_{A\ne B}
(-1)^{|A|+|B|}r_Ar_B
\,d_{i,A}(X)d_{i,B}(X).
}
\tag{L-99722.5}
\]

All remaining difficulty is therefore the signed near-collision Gram among
incomparable future products. Neither the exact Littlewood--Paley identity nor
the compact diagonal estimate bounds (L-99722.5). The universal failure is
proved in `R-99721`; the corrected source-orbit frontier is recorded in
`T-99722`.
