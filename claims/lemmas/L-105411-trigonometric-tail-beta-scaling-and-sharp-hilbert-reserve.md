# L-105411 — The trigonometric critical tail has a universal beta scaling and a sharp Hilbert reserve

Claim ID: `L-105411`  
Status: **PROVED EXACT MODEL ASYMPTOTIC**  
Created: 2026-08-24  
Depends on: `L-105382`  
RH status: **not assumed**

## 1. Unified tail atoms

For either trigonometric parity, write the positive atoms as

\[
s_j={1\over\pi^2t_j^2},
\qquad
W_j={2\over\pi^2t_j^2}=2s_j,
\tag{L-105411.1}
\]

where `t_j=j` for the cotangent/even model and `t_j=j+1/2` for the tangent/odd model, with the indexing convention of `L-105382`.

After deleting the first `J` positive atoms, define

\[
\mathsf R_{k,p,J}^{(a)}
=\sum_{j>J}W_js_j^a v_k(s_j)v_k(s_j)^T,
\qquad
v_k(s)=(1,s,\ldots,s^{k-1})^T.
\tag{L-105411.2}
\]

The harmless half-integer shift affects only the relative `O_k(J^-1)` error.

## 2. Entrywise asymptotic

For `q=i+j+a`, the integral test gives

\[
\sum_{t>J}t^{-2q-2}
={J^{-2q-1}\over2q+1}
\left(1+O_q(J^{-1})\right).
\]

Therefore

\[
\boxed{
\left(\mathsf R_{k,p,J}^{(a)}\right)_{ij}
=
{2\over\pi^{2q+2}(2q+1)}
J^{-2q-1}
\left(1+O_k(J^{-1})\right).
}
\tag{L-105411.3}
\]

Put

\[
D_J=\operatorname{diag}\left(
1,(\pi J)^{-2},\ldots,(\pi J)^{-2(k-1)}
\right)
\tag{L-105411.4}
\]

and

\[
\boxed{
\mathsf H_k^{(a)}
=
\left[{1\over2(i+j+a)+1}\right]_{i,j=0}^{k-1}.
}
\tag{L-105411.5}
\]

Then

\[
\boxed{
\mathsf R_{k,p,J}^{(a)}
=
2\pi^{-2a-2}J^{-2a-1}
D_J
\left(
\mathsf H_k^{(a)}+O_k(J^{-1})
\right)
D_J.
}
\tag{L-105411.6}
\]

The error is entrywise and hence operator-norm bounded for fixed `k`.

## 3. Exact positivity and determinant

The matrix is a Gram matrix:

\[
\boxed{
\mathsf H_k^{(a)}
=
\int_0^1
(x^{2(i+a)})_{i=0}^{k-1}
(x^{2j})_{j=0}^{k-1\,T}\,dx.
}
\tag{L-105411.7}
\]

It is positive definite. Its Cauchy determinant is

\[
\boxed{
\det\mathsf H_k^{(a)}
=
{\displaystyle
\prod_{0\le i<j<k}[2(j-i)]^2
\over\displaystyle
\prod_{i,j=0}^{k-1}[2(i+j+a)+1]}
>0.
}
\tag{L-105411.8}
\]

The final Schur complement is

\[
\boxed{
\chi_{k,a}
={\det\mathsf H_k^{(a)}
 \over\det\mathsf H_{k-1}^{(a)}}
=
{4^{k-1}((k-1)!)^2
\over
(4k+2a-3)
\prod_{i=0}^{k-2}[2(i+k-1+a)+1]^2},
}
\tag{L-105411.9}
\]

with the denominator product empty for `k=1`.

## 4. Sharp smallest-eigenvalue exponent

A last-coordinate Schur-complement argument in (L-105411.6) gives

\[
\boxed{
\lambda_{\min}
\left(\mathsf R_{k,p,J}^{(a)}\right)
\sim
2\pi^{-(4k+2a-2)}
\chi_{k,a}\,
J^{-(4k+2a-3)}.
}
\tag{L-105411.10}
\]

In particular,

\[
\boxed{
\lambda_{\min}
\left(\mathsf R_{k,p,J}^{(a)}\right)
\asymp_{k,a}
J^{-q_{k,a}},
\qquad
q_{k,a}=4k+2a-3.
}
\tag{L-105411.11}
\]

The worst of the ordinary and shifted blocks has exponent

\[
\boxed{q_k=4k-1.}
\tag{L-105411.12}
\]

This replaces the deliberately crude exponent `3k(k-1)+4` used in `T-105390`.

## 5. Universal beta-tail limit

Push the tail measure forward by

\[
u=\pi^2J^2s
\]

and multiply its mass by `J`. Then, for both parities,

\[
\boxed{
J\,(u_\#\nu_{p,>J})
\Longrightarrow
{1\over\pi^2}u^{-1/2}\mathbf1_{(0,1)}(u)\,du.
}
\tag{L-105411.13}
\]

Indeed the sum is a Riemann sum in `t/J`, followed by `u=(J/t)^2`. Its moments are

\[
\boxed{
\int_0^1u^n{du\over\pi^2\sqrt u}
={2\over\pi^2(2n+1)}.
}
\tag{L-105411.14}
\]

The Hilbert matrix in (L-105411.5) is exactly the moment Gram of this universal beta law.

## 6. Natural grading of a signed tail error

Let `sigma` be a signed tail discrepancy and

\[
\Delta_n=\int s^n\,d\sigma(s).
\]

Under the congruence in (L-105411.6), its normalized `(i,j)` entry is

\[
\boxed{
{\pi^{2q+2}\over2}
J^{2q+1}\Delta_q,
\qquad q=i+j+a.
}
\tag{L-105411.15}
\]

Thus the scale-invariant fixed-order condition is

\[
\boxed{
\pi^{2n}J^{2n+1}\Delta_n=o(1)
\quad(0\le n\le2k-1),
}
\tag{L-105411.16}
\]

not one common isotropic rate for every moment.

## 7. Scope

This is an exact trigonometric-tail theorem. It does not identify the Xi remote tail with the beta law. Its role is to supply the correct conditioning, moment grading, and smallest-eigenvalue scale for the real-saddle comparison.
