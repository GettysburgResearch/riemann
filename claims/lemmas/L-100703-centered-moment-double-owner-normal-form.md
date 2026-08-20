# L-100703 — The centered minimal-wavelet moment tower has an exact double-owner normal form

Claim ID: `L-100703`  
Status: **PROVED EXACT ROOT-FREE HILBERT REDUCTION; BLOCK PACKING OPEN**  
Created: 2026-08-20  
Depends on: PRs #674--#675; PR #682 `L-100211--L-100213`; `L-100700`  
RH status: **not assumed**

Let `K_0` be the minimal ratio-eight ordinary-Mobius wavelet. Its activation
zero permits the bounded compact kernel

\[
J_0(y)={K_0(y)\over\log y},
\qquad J_0(1)=\lim_{y\downarrow1}{K_0(y)\over\log y}.
\]

For `X>8`, put

\[
\ell_{X,n}=\log(X/n),
\qquad
M_k(X)=
\sum_{X/8\le n\le X}
{\mu(n)\over\sqrt n}
J_0(X/n)\ell_{X,n}^k.
\tag{L-100703.1}
\]

Then

\[
G_\mu(X)=M_1(X).
\tag{L-100703.2}
\]

For `0<rho<=1` and integer `K>=1`, define the Hilbert-valued observation

\[
\mathcal O_{X,\rho,K}f
=
\left(
 {\rho^k\over k!}\,O_{X,k}f
\right)_{1\le k\le K}.
\tag{L-100703.3}
\]

Because `J_0` is supported on `[1,8]`,

\[
\mathcal O_{X,\rho,K}\delta_1=0
\qquad(X>8).
\tag{L-100703.4}
\]

Apply `L-100700` to the literal finite Euler source and then pass to the finite
source limit. One obtains

\[
\boxed{
\begin{aligned}
\sum_{k=1}^{K}{\rho^{2k}\over(k!)^2}|M_k(X)|^2
\le{}&
\sum_iw_{i,i}\,\mathcal Q_{i,i}^{(K,\rho)}(X)\\
&+
\sum_{i<j}w_{i,j}\,\mathcal Q_{i,j}^{(K,\rho)}(X),
\end{aligned}}
\tag{L-100703.5}
\]

where

\[
\mathcal Q_{i,j}^{(K,\rho)}(X)
=
\left\|
\mathcal O_{X,\rho,K}
\mathfrak D_{i,j}\delta_1
\right\|^2.
\tag{L-100703.6}
\]

Thus every interaction between different least/greatest-owner blocks is
removed exactly. The `k=0` root is absent before any estimate.

Choose

\[
\rho_X={1\over\log(3X)},
\qquad
K_X=
\left\lceil {4\log(3X)\over\log\log(9X)}\right\rceil.
\tag{L-100703.7}
\]

The compact bound `0<=ell_(X,n)<=log 8` gives a factorially small tail beyond
`K_X`; all truncation and Cauchy-derivative costs are `X^(o(1))`. In
particular,

\[
|G_\mu(X)|^2
\le \rho_X^{-2}
\sum_{k=1}^{K_X}{\rho_X^{2k}\over(k!)^2}|M_k(X)|^2
+O(X^{-2}).
\tag{L-100703.8}
\]

## Oscillatory terminal estimate

Define `DOMC100703` by

\[
\boxed{
\int_{2^L}^{2^{L+1}}
\left[
\sum_iw_{i,i}\mathcal Q_{i,i}^{(K_X,\rho_X)}(X)
+
\sum_{i<j}w_{i,j}\mathcal Q_{i,j}^{(K_X,\rho_X)}(X)
\right]^{1/2}
{dX\over X}
=2^{o(L)}.
}
\tag{DOMC100703}
\]

Then (L-100703.8), Cauchy--Schwarz on logarithmic blocks, and the exact
minimal-wavelet detector give

\[
\boxed{\mathrm{DOMC100703}\Longrightarrow RH.}
\tag{L-100703.9}
\]

The remaining energy is entirely within one explicit double-owner interval.
There is no neutral root, cross-owner interference, far-support term, or high
moment tail left to estimate.
