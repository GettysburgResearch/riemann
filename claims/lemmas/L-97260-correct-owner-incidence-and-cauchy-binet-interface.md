# L-97260 — Correct owner incidence and conditional Cauchy–Binet propagation

Claim ID: `L-97260`  
Status: **PROVED EXACT FINITE-DIMENSIONAL INTERFACE THEOREM**  
Created: 2026-08-17  
RH status: **not assumed**

Fix a finite endpoint. Let `A` be the original source-atom set and `L` the set
of terminal owners. Each source atom `a` has exactly one owner `o(a)` and one
positive path weight `w_a`.

Define the terminal-by-source matrix
\[
 H_{\ell a}=w_a\,\mathbf 1_{o(a)=\ell},
 \qquad H\in\mathbb R_{\ge0}^{|L|\times|A|}.
\]
Let
\[
 K_{\ell,:}=(t_\ell,r_\ell),\qquad K\in\mathbb R^{|L|\times2}.
\]
The source-feature matrix is
\[
 \boxed{M=H^{\mathsf T}K\in\mathbb R^{|A|\times2}.}
\]

The product `HK` written in the unpublished response is dimensionally
undefined under its own convention that every **source column** of `H` has one
nonzero entry.

Order terminal labels, then source atoms in nondecreasing owner order. Every
\(2\times2\) minor of `H^T` is then zero or a positive path-weight product.
Without this ordering convention the crossing incidence matrix
\[
 \begin{pmatrix}0&a\\ b&0\end{pmatrix}
\]
has determinant `-ab`.

For any two source rows `I`, Cauchy–Binet gives
\[
 \boxed{\det M[I,:]=
 \sum_{\substack{J\subseteq L\\|J|=2}}
 \det H^{\mathsf T}[I,J]\,\det K[J,:].}
\]
Thus target/scalar TP2 of `K` propagates to `M`.

This theorem transports determinant signs only. It says nothing about total
even target capacity, odd target demand, the global Lorenz envelope, or the
existence of a common-source Hall coefficient vector.
