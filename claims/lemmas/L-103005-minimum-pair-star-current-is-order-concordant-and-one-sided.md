# L-103005 — The minimum-pair star current is order-concordant and one-sided

Claim ID: `L-103005`  
Status: **PROVED EXACT STAR-SECTOR CLOSURE**  
Created: 2026-08-25  
Depends on: `L-102961`; `L-103001--L-103003`; PR #730 `T-105440`  
RH status: **not assumed**

Fix one squarefree labelled occurrence

\[
S=\{p_1<\cdots<p_k\},
\qquad k\ge4,
\]

and retain the minimum-pair/equal-pair Hodge decomposition of `L-102961`.

The star potential is

\[
s_i={r_i\over k-2},
\]

where

\[
r_1=r_2={k-2\over k},
\qquad
r_i=-{2\over k}\quad(i\ge3).
\]

Hence

\[
\boxed{
s_1=s_2={1\over k},
\qquad
s_i=-{2\over k(k-2)}\quad(i\ge3).
}
\tag{L-103005.1}
\]

In particular,

\[
\sum_{i=1}^k s_i=0
\]

and the sequence is nonincreasing in the declared prime order:

\[
s_1=s_2>s_3=\cdots=s_k.
\tag{L-103005.2}
\]

Let `C_i` be the source-complete radial actual-owner packets of PR #730. The star current is

\[
\mathcal S=\sum_i s_i C_i.
\]

The zero-sum condition gives the complete-graph gradient identity

\[
\boxed{
\mathcal S
={1\over k}
\sum_{i<j}
(s_i-s_j)(C_i-C_j).
}
\tag{L-103005.3}
\]

Indeed the coefficient of `C_i` on the right is

\[
{k s_i-\sum_j s_j\over k}=s_i.
\]

## 1. Every active gradient coefficient is concordant

For `i<j`,

\[
s_i-s_j\ge0.
\]

The coefficient is nonzero only when

\[
i\in\{1,2\},
\qquad
j\ge3.
\]

Thus every active radial edge points from a smaller physical prime label to a larger one.

## 2. Common-mother observation

PR #730 gives the exact endpoint factorization

\[
C_i-C_j
=(x_j-x_i)H^{(1)}_{ij}
-(x_j^2-x_i^2)H^{(2)}_{ij}.
\]

The squared endpoint term belongs to the already-closed squared/higher-prime-power ledger.

For the remaining native endpoint boundary, the common-mother factorization of `L-102701` and the Plücker/Wronskian identity `L-103003` produce the fixed kernel

\[
\mathcal W_{p_i,p_j}(X).
\]

Since `p_i<p_j`, `L-103001` gives

\[
\mathcal W_{p_i,p_j}(X)\le0.
\]

Multiplying by the nonnegative coefficient `(s_i-s_j)/k` preserves this one-sided orientation.

Therefore

\[
\boxed{
\text{the complete minimum-pair star current is pointwise one-sided,
modulo the inherited polylogarithmic squared boundary.}
}
\tag{L-103005.4}
\]

Its adverse logarithmic mass is `Y^{o(1)}` without a new arithmetic estimate.

## Consequence

The minimum-owner/equal-pair gauge correction no longer has two open Hodge components. Its radial star component is closed exactly. Only the row-zero cycle component of `L-102961` can remain conclusion-bearing.