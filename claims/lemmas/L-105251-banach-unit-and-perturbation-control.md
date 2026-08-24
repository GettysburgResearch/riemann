# L-105251 — Uniform Banach-algebra invertibility and growing-degree stability

Claim ID: `L-105251`  
Status: **PROVED EXACT**  
Created: 2026-08-24  
Depends on: L-105250; Neumann series  
RH status: not assumed

Let `A` be a unital Banach algebra and let `x in A` satisfy `||x||<=1`. The algebra need not be commutative for the invertibility and perturbation statements below.

With `P_K` and `c_K` from L-105250,
\[
P_K(x)=1-\sum_{j=1}^K b_jx^j.
\]

## 1. Uniform unit bound

Since
\[
\left\|\sum_{j=1}^K b_jx^j\right\|
\le\sum_{j=1}^K b_j=1-c_K<1,
\]
the Neumann series gives
\[
\boxed{
P_K(x)\text{ is invertible},\qquad
\|P_K(x)^{-1}\|\le c_K^{-1}.
}
\tag{1}
\]
Also
\[
\boxed{\|P_K(x)\|\le2-c_K<2.}
\tag{2}
\]
The condition cost is only
\[
c_K^{-1}=\frac{4^K}{\binom{2K}{K}}
\sim\sqrt{\pi K}.
\tag{3}
\]

## 2. Exact coefficient-derivative sum

One has
\[
\boxed{\sum_{j=1}^K j b_j=Kc_K.}
\tag{4}
\]
This follows from `b_j=c_(j-1)-c_j` and
\[
\sum_{j=0}^{K-1}c_j=2Kc_K.
\]

## 3. Perturbation stability

If `||x||,||y||<=1`, then
\[
x^j-y^j=\sum_{h=0}^{j-1}x^h(x-y)y^{j-1-h}
\]
gives
\[
\boxed{
\|P_K(x)-P_K(y)\|
\le Kc_K\|x-y\|.
}
\tag{5}
\]
Consequently
\[
\|P_K(x)^{-1}(P_K(y)-P_K(x))\|
\le K\|x-y\|.
\]
If `K||x-y||<1`, then `P_K(y)` is invertible and
\[
\boxed{
\|P_K(y)^{-1}\|
\le\frac{1}{c_K(1-K\|x-y\|)}.
}
\tag{6}
\]

Thus a growing degree `K=K(T)` is stable under any source-representation error `e_T` satisfying `K(T)e_T->0`. For fixed `K`, every `o(1)` source error is harmless.
