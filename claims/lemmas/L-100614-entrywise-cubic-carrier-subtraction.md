# L-100614 — Every double-owner cubic entry has an explicit nonnegative carrier and a collar-only residual

Claim ID: `L-100614`  
Status: **PROVED EXACT CARRIER/COLLAR DECOMPOSITION**  
Created: 2026-08-20  
Depends on: `L-100610--L-100613`; PR #676 cubic kernel  
RH status: **not assumed**

Let

\[
H_{ij}(X)
=
\Delta_i\Delta_jE_{i+1:j-1}\Psi(X),
\qquad i<j,
\tag{L-100614.1}
\]

where the labels have prime values `p_h`, native activities
`r_h=p_h^(-1/2)`, and

\[
\Psi(y)=64
\begin{cases}
3y-y^{3/2},&0<y\le1,\\
3\sqrt y-1,&y\ge1.
\end{cases}
\]

The deep homogeneous carrier is

\[
P(X)=192\sqrt X.
\tag{L-100614.2}
\]

Since

\[
U_pP=p^{-1/2}P,
\]

one has exactly

\[
\boxed{
M_{ij}(X)
:=
\Delta_i\Delta_jE_{i+1:j-1}P(X)
=
192\sqrt X
(1-p_i^{-1/2})(1-p_j^{-1/2})
\prod_{i<h<j}(1-p_h^{-1}).
}
\tag{L-100614.3}
\]

Thus

\[
M_{ij}(X)\ge0.
\tag{L-100614.4}
\]

Define the centered interval residual

\[
\boxed{
\widetilde H_{ij}(X)=H_{ij}(X)-M_{ij}(X).
}
\tag{L-100614.5}
\]

## 1. The carrier may be removed before the Schur estimate

In the two-ended hazard decomposition, the coefficient of `H_(ij)` is

\[
r_ir_jL_iR_j\ge0.
\]

Therefore

\[
\sum_{i<j}r_ir_jL_iR_jM_{ij}(X)
\ge0.
\tag{L-100614.6}
\]

The negative part of the complete cubic scalar is consequently bounded by the
matrix formed from `widetilde H_(ij)`, not by the raw interval matrix. No
absolute value should be placed around the positive carrier.

This is a necessary hardening of `T-100610`: using raw row and column absolute
sums would ask the arithmetic estimates to pay a known power-sized positive
term.

## 2. The centered entry is supported only on partial activation

Suppose every shifted argument occurring in

\[
\Delta_i\Delta_jE_{i+1:j-1}\Psi(X)
\]

is at least one. Then every kernel term is on the deep branch

\[
\Psi(y)=192\sqrt y-64.
\]

The endpoint differences annihilate the constant `-64`, while the square-root
part is exactly (L-100614.3). Hence

\[
\boxed{
\widetilde H_{ij}(X)=0
}
\tag{L-100614.7}
\]

throughout every fully active interval cell.

In particular, for a finite interval label set,

\[
X\ge\prod_{h=i}^{j}p_h
\quad\Longrightarrow\quad
\widetilde H_{ij}(X)=0.
\tag{L-100614.8}
\]

More generally, expansion of the interval Euler product shows that
`widetilde H_(ij)` is a finite sum over exactly those subsets whose product
crosses one of the physical activation thresholds. It is an endpoint-collar
object, not an interior homogeneous Euler-product object.

## 3. Refined matrix frontier

Define

\[
\widetilde A_{ij}^{(k)}(X)
=
\sqrt{r_ir_j}\,\widetilde H_{ij}(X).
\tag{L-100614.9}
\]

The row/column Schur conditions in the implication matrix may be restricted to
`widetilde A`, and after `L-100613` they may additionally discard every
ratio-eight interval whose complete uncentered entry is already nonnegative.
Thus the only possible negative matrix entries are:

```text
long endpoint interval;
partial activation inside that interval;
explicit native divisor sign before positive renewal.
```

All deep carriers, constants, root channels, singleton channels, adjacent
intervals, and short ratio-eight intervals are already paid with the correct
sign.