# L-100700 — Two-sided convex owner decoupling removes every cross-block interaction

Claim ID: `L-100700`  
Status: **PROVED EXACT HILBERT-SPACE INEQUALITY**  
Created: 2026-08-20  
Depends on: PR #660 `L-99722`; PR #691 `L-100605`  
RH status: **not assumed**

Let `H,K` be Hilbert spaces, let `O:H->K` be linear, and let
`U_1,...,U_k` be commuting isometries on `H`. Fix `0<r_i<1` and put

\[
F_{a,b}=\prod_{a\le h\le b}(I-r_hU_h),
\qquad F_{a,b}=I\quad(a>b).
\]

Define

\[
w_\varnothing=\prod_{h=1}^k(1-r_h),
\]

\[
w_{i,i}=r_i\prod_{h<i}(1-r_h)\prod_{h>i}(1-r_h),
\]

and, for `i<j`,

\[
w_{i,j}=r_ir_j
\prod_{h<i}(1-r_h)
\prod_{h>j}(1-r_h).
\tag{L-100700.1}
\]

The weights have the probability interpretation

```text
w_empty   = no selected label;
w_(i,i)   = i is the unique selected label;
w_(i,j)   = i and j are the least and greatest selected labels,
            while labels strictly between them are unresolved.
```

Consequently

\[
\boxed{
 w_\varnothing+
 \sum_iw_{i,i}+
 \sum_{i<j}w_{i,j}=1.
}
\tag{L-100700.2}
\]

For `i<j` put

\[
\mathfrak D_{i,j}f
=(I-U_i)(I-U_j)F_{i+1,j-1}f,
\]

and put `mathfrak D_(i,i)f=(I-U_i)f`. Then

\[
\boxed{
\begin{aligned}
\left\|O F_{1,k}f\right\|^2
\le{}&w_\varnothing\|Of\|^2
 +\sum_iw_{i,i}\|O\mathfrak D_{i,i}f\|^2\\
&+\sum_{i<j}w_{i,j}\|O\mathfrak D_{i,j}f\|^2.
\end{aligned}}
\tag{L-100700.3}
\]

## Proof

The scalar convexity identity of `L-99722` is

\[
\|a-rb\|^2
\le(1-r)\|a\|^2+r\|a-b\|^2.
\tag{L-100700.4}
\]

Apply it first in the increasing order `1,...,k`. This gives

\[
\|OF_{1,k}f\|^2
\le s_k\|Of\|^2+
\sum_i\lambda_i
\|O(I-U_i)F_{i+1,k}f\|^2,
\]

where

\[
s_k=\prod_h(1-r_h),
\qquad
\lambda_i=r_i\prod_{h<i}(1-r_h).
\]

For each fixed `i`, apply (L-100700.4) to the remaining factors in the
reverse order `k,k-1,...,i+1`. One obtains

\[
\begin{aligned}
\|O(I-U_i)F_{i+1,k}f\|^2
\le{}&\left(\prod_{h>i}(1-r_h)\right)
 \|O(I-U_i)f\|^2\\
&+\sum_{j>i}
 r_j\left(\prod_{h>j}(1-r_h)\right)
 \|O\mathfrak D_{i,j}f\|^2.
\end{aligned}
\]

Multiplying by `lambda_i` gives exactly the weights in (L-100700.1),
and proves (L-100700.3).

## Meaning

`L-100605` is an exact coefficient decomposition. Equation (L-100700.3) is
its Hilbert-space companion: every interference term between different
least/greatest-owner blocks is removed **before** the arithmetic estimate.
The middle Euler product remains literal and source-faithful.

The theorem is valid simultaneously for:

- a scalar compact-wavelet observation;
- a Cauchy/Poisson phase space;
- a direct sum of logarithmic moments;
- a finite family of component rows.

It does not estimate the middle block. That is the only remaining place where
arithmetic cancellation can occur.
