# L-105390 — The unused trigonometric tail has an explicit polynomial capacity margin

Claim ID: `L-105390`  
Status: **PROVED EXACT QUANTITATIVE MODEL THEOREM**  
Created: 2026-08-23  
Depends on: `L-105382`, `L-105388`  
RH status: **not assumed**

## 1. Tail moment matrices

For parity `p in {odd,even}`, let `(W_j^p,s_j^p)` be the unit-scale tangent or
cotangent atoms of `L-105382`. After deleting the first `J` atoms, define

\[
\mathsf R_{k,p,J}^{(a)}
=
\sum_{j>J}
W_j^p(s_j^p)^a
v_k(s_j^p)v_k(s_j^p)^T,
\qquad a\in\{0,1\},
\tag{L-105390.1}
\]

where

\[
v_k(s)=(1,s,\ldots,s^{k-1})^T.
\]

This is the positive tail reserve in the ordinary or shifted source block.

## 2. Uniform atom scales

For either parity there are positive constants depending only on the parity
such that, for all large `j`,

\[
W_j^p\asymp j^{-2},
\qquad
s_j^p\asymp j^{-2}.
\tag{L-105390.2}
\]

Moreover, for `1<=i<ell<=k` and all large `J`, the `k` consecutive locations

\[
s_{J+1}^p,\ldots,s_{J+k}^p
\]

satisfy

\[
\boxed{
|s_{J+i}^p-s_{J+\ell}^p|
\ge c_{k,p}(\ell-i)J^{-3}.
}
\tag{L-105390.3}
\]

This follows directly from the explicit reciprocal-square formulas.

## 3. A positive k-atom submatrix

Retain only the `k` atoms with indices `J+1,...,J+k`. Their Gram matrix is

\[
\mathsf B_{k,p,J}^{(a)}
=V D V^T,
\tag{L-105390.4}
\]

where the columns of `V` are the Vandermonde vectors
`v_k(s_(J+i)^p)` and

\[
D=\operatorname{diag}
\left(W_{J+i}^p(s_{J+i}^p)^a\right)_{i=1}^k.
\]

The Vandermonde determinant and (L-105390.3) give

\[
\boxed{
|\det V|
\ge c_{k,p}J^{-3k(k-1)/2}.
}
\tag{L-105390.5}
\]

Also,

\[
\prod_{i=1}^kD_{ii}
\ge c_{k,p,a}J^{-k(2+2a)}.
\tag{L-105390.6}
\]

Therefore

\[
\boxed{
\det\mathsf B_{k,p,J}^{(a)}
\ge
c_{k,p,a}
J^{-3k(k-1)-k(2+2a)}.
}
\tag{L-105390.7}
\]

## 4. Smallest-eigenvalue lower bound

The trace of the selected `k`-atom matrix satisfies

\[
\operatorname{tr}
\mathsf B_{k,p,J}^{(a)}
\le C_{k,p,a}J^{-2-2a}.
\tag{L-105390.8}
\]

For a positive definite `k by k` matrix,

\[
\lambda_{\min}
\ge{\det B\over(\operatorname{tr}B)^{k-1}}.
\]

Combining (L-105390.7)--(L-105390.8) yields

\[
\boxed{
\lambda_{\min}
\left(\mathsf B_{k,p,J}^{(a)}\right)
\ge
c_{k,p,a}J^{-d_{k,a}},
}
\tag{L-105390.9}
\]

where

\[
\boxed{
d_{k,a}=3k(k-1)+2+2a.}
\tag{L-105390.10}
\]

Since the full tail matrix dominates the selected submatrix,

\[
\boxed{
\lambda_{\min}
\left(\mathsf R_{k,p,J}^{(a)}\right)
\ge
c_{k,p,a}J^{-d_{k,a}}.
}
\tag{L-105390.11}
\]

This makes the positive tail margin in `L-105388` quantitative.

## 5. Simultaneous two-block exponent

For both `a=0` and `a=1`, it is enough to use

\[
\boxed{
d_k=3k(k-1)+4.}
\tag{L-105390.12}
\]

Then

\[
\lambda_{\min}
\left(\mathsf R_{k,p,J}^{(a)}\right)
\ge c_{k,p}J^{-d_k}
\]

for both blocks after changing the constant.

## 6. Scope

The exponent is deliberately crude and not claimed optimal. It is sufficient
to balance the real-saddle approximation error against a slowly growing
critical prefix. The constants deteriorate with `k`, and no uniform all-order
margin is asserted. This is a model tail theorem, not an Xi critical-tail
estimate.
