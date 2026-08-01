# L-15131 — One coherent finite-window family gives every cyclic coefficient and the Hilbert--Schmidt limit

Claim ID: `L-15131`  
Status: **PROVED ABSTRACT ALL-ORDERS THEOREM; CLASSICAL PULLBACK REMAINS A SEPARATE GATE**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15129`, `L-15130`; Schatten ideal inequalities  
Scope: generalizes the same-matrix identity from order three to all determinant orders  
Related counterexample candidates: none

## 1. Coherent family

For every finite window `M`, let `H_M` be a Hilbert space, let

\[
K_M=K_M^*\in\mathfrak S_2(H_M),
\]

and let `Gamma_M` be a self-adjoint involution satisfying

\[
\Gamma_MK_M\Gamma_M=-K_M.
\tag{L-15131.1}
\]

Choose finite-rank orthogonal projections `P_(M,N)` such that

\[
P_{M,N}\uparrow I,
\qquad
[P_{M,N},\Gamma_M]=0,
\tag{L-15131.2}
\]

and define one, and only one, compressed matrix family

\[
\boxed{K_{M,N}=P_{M,N}K_MP_{M,N}.}
\tag{L-15131.3}
\]

In arbitrary finite readout coordinates, let `G_(M,N)` be the Gram matrix and `B_(M,N)` the matrix of the compressed seam form. They must represent exactly this operator:

\[
G_{M,N}^{-1}B_{M,N}\sim K_{M,N}.
\tag{L-15131.4}
\]

No separate matrix may be chosen for different tensor orders.

## 2. Finite all-orders identity

For every `ell>=2`, define the finite scalar coefficient by the Gram-cyclic contraction of `L-15129`:

\[
c_{\ell,M,N}=\mathfrak c_\ell(G_{M,N},B_{M,N}).
\tag{L-15131.5}
\]

Then

\[
\boxed{c_{\ell,M,N}=\operatorname{Tr}(K_{M,N}^{\ell})\quad(\ell\ge2).}
\tag{L-15131.6}
\]

The associated finite scalar Cauchy--Laplace family is

\[
\mathscr C_{M,N}(w)
=w\operatorname{Tr}\left(K_{M,N}^2(I+iwK_{M,N})^{-1}\right),
\tag{L-15131.7}
\]

and

\[
\mathscr C_{M,N}(w)
=\sum_{\ell\ge2}(-i)^{\ell-2}c_{\ell,M,N}w^{\ell-1}.
\tag{L-15131.8}
\]

Because the projections preserve the grading,

\[
\boxed{c_{2r+1,M,N}=0\quad(r\ge1).}
\tag{L-15131.9}
\]

## 3. Finite-rank limit at fixed window

Since `K_M` is Hilbert--Schmidt and `P_(M,N)` converges strongly to the identity,

\[
\boxed{\|K_{M,N}-K_M\|_2\longrightarrow0.}
\tag{L-15131.10}
\]

For any two Hilbert--Schmidt operators `A,B` and every `ell>=2`, telescoping and Schatten Hölder give

\[
\boxed{
\left|\operatorname{Tr}(A^\ell)-\operatorname{Tr}(B^\ell)\right|
\le \ell C^{\ell-1}\|A-B\|_2,}
\tag{L-15131.11}
\]

where

\[
C=\max\{\|A\|_2,\|B\|_2\}.
\]

Hence

\[
\boxed{c_{\ell,M,N}\longrightarrow c_{\ell,M}:=\operatorname{Tr}(K_M^\ell).}
\tag{L-15131.12}
\]

Moreover, on every disk

\[
|w|<r<\|K_M\|^{-1},
\]

the scalar families converge uniformly:

\[
\mathscr C_{M,N}\longrightarrow
w\operatorname{Tr}\left(K_M^2(I+iwK_M)^{-1}\right).
\tag{L-15131.13}
\]

## 4. Window limit

Suppose there is a self-adjoint Hilbert--Schmidt operator `K` and isometric identifications of the window spaces into one ambient Hilbert space such that

\[
\boxed{\|K_M-K\|_2\longrightarrow0.}
\tag{L-15131.14}
\]

Then, for every fixed `ell>=2`,

\[
\boxed{
\lim_{M\to\infty}\lim_{N\to\infty}c_{\ell,M,N}
=\operatorname{Tr}(K^\ell).}
\tag{L-15131.15}
\]

The corresponding scalar functions converge locally uniformly near the origin:

\[
\boxed{
\lim_{M\to\infty}\lim_{N\to\infty}\mathscr C_{M,N}(w)
=w\operatorname{Tr}\left(K^2(I+iwK)^{-1}\right)
=\frac d{dw}\log\det{}_2(I+iwK).}
\tag{L-15131.16}
\]

A single diagonal sequence `(M_j,N_j)` may be selected by requiring both Hilbert--Schmidt errors to be at most `2^-j`.

## 5. Grading in the limit

Assume the finite/window gradings are transported from one ambient involution `Gamma` and every embedding/projection commutes with it. Then

\[
\Gamma K\Gamma=-K,
\]

and all odd limiting traces vanish. The determinant is even:

\[
\boxed{
\det{}_2(I+iwK)=\prod_{\lambda>0}(1+w^2\lambda^2)^{m(\lambda)}.}
\tag{L-15131.17}
\]

The order-three equality is therefore

\[
[w^2]\frac d{dw}\log\det{}_2(I+iwK)
=-i\operatorname{Tr}(K^3)=0,
\tag{L-15131.18}
\]

matching the centered classical parity coefficient.

## 6. Exact classical comparison hypothesis

Let `A_(ell,M,N)` denote a scalar coefficient obtained independently from the classical Cauchy--Laplace/explicit-formula ledger. The determinant target identification follows if one proves, for the same family above,

\[
\boxed{
A_{\ell,M,N}
=c_{\ell,M,N}
=\mathfrak c_\ell(G_{M,N},B_{M,N})
\quad\text{for every }\ell,M,N,}
\tag{L-15131.19}
\]

and if the classical coefficients have one analytic majorant permitting the limits and the power-series sum to be interchanged.

Equation (L-15131.19) is now an explicit finite tensor identity. It cannot be replaced by the assertion that scalar and cyclic tests are both pullbacks of a universal object unless the two pullback maps are written down and their values are shown to be the contraction (L-15129.3).

## 7. What this theorem closes

The following parts of the proposed determinant programme are completely settled by the construction above:

1. the order-three operator scalar coefficient equals `Tr(K_(M,N)^3)`;
2. one transported grading forces it to vanish;
3. the same coefficient construction works at every order;
4. finite-rank and window limits preserve every trace moment under `S_2` convergence;
5. the limiting scalar family is the logarithmic derivative of one `det_2`.

The only remaining target-identification obligation is (L-15131.19) on the **classical** realization. `R-15108` proves that this is independent data and cannot be inferred from the operator construction alone.
