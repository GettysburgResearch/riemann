# L-105250 — The square-root polynomial hierarchy has a positive residual source

Claim ID: `L-105250`  
Status: **PROVED EXACT, FORMAL POWER-SERIES / COMMUTATIVE-ALGEBRA THEOREM**  
Created: 2026-08-24  
Depends on: elementary binomial series  
RH status: not assumed

For `j>=1`, put
\[
b_j=-[x^j]\sqrt{1-x}
=\frac{\binom{2j}{j}}{4^j(2j-1)}>0,
\]
and for `K>=1` define
\[
\boxed{P_K(x)=1-\sum_{j=1}^K b_jx^j.}
\tag{1}
\]
Also put
\[
c_K=\frac{\binom{2K}{K}}{4^K}.
\tag{2}
\]

## 1. Exact positive quotient

There are uniquely determined coefficients `q_(K,m)` such that
\[
\boxed{
\frac{P_K(x)^2}{1-x}=\sum_{m\ge0}q_{K,m}x^m.
}
\tag{3}
\]
They satisfy
\[
\boxed{
q_{K,0}=1,\qquad q_{K,m}=0\ (1\le m\le K),\qquad
q_{K,m}\ge0\ (m\ge K+1).
}
\tag{4}
\]

Proof. Write
\[
S(x)=\sqrt{1-x},\qquad
U_K(x)=P_K(x)-S(x)=\sum_{j>K}b_jx^j.
\]
Both `U_K` and `(1-x)^(-1/2)` have nonnegative coefficients. Hence
\[
V_K(x)=\frac{U_K(x)}{S(x)}
\]
has nonnegative coefficients and starts in degree `K+1`. Therefore
\[
\frac{P_K(x)^2}{1-x}=\left(1+V_K(x)\right)^2
\]
has exactly the properties in (4).

This is the all-degree extension of
\[
\frac{(1-x/2-x^2/8)^2}{1-x}
=1+\frac{x^3}{8}+\frac9{64}\sum_{m\ge4}x^m.
\]

## 2. Monotonicity and the eventual constant

For `K+1<=m<=2K`,
\[
q_{K,m}-q_{K,m-1}=[x^m]P_K(x)^2\ge0,
\]
because every contributing factor has product `(-b_i)(-b_j)>0`. For `m>2K` the difference is zero. Thus
\[
\boxed{
0\le q_{K,m}\le c_K^2,\qquad
q_{K,m}=c_K^2\quad(m\ge2K).
}
\tag{5}
\]
Indeed, the eventual constant is `P_K(1)^2`, and
\[
P_K(1)=1-\sum_{j=1}^K b_j=c_K,
\tag{6}
\]
using `b_j=c_(j-1)-c_j`.

The first surviving coefficient is
\[
\boxed{q_{K,K+1}=2b_{K+1}.}
\tag{7}
\]

## 3. Source congruence

Let `A` be a commutative algebra, let `x in A`, and suppose the geometric resolvent is defined finitely, formally, or by norm convergence. Then
\[
\boxed{
P_K(x)^2(1-x)^{-1}
=1+\sum_{m\ge K+1}q_{K,m}x^m.
}
\tag{8}
\]
Every residual source degree has a nonnegative coefficient. Multiplication by `P_K(x)` is therefore an exact Frobenius-form congruence whenever it is a unit. Unit control is supplied by L-105251.

No scalar pointwise zero-free claim is made. The theorem concerns the source algebra and its congruence representation.
