# L-105310 — Confluent critical-residue Pick compression

Claim ID: `L-105310`  
Status: **PROVED EXACT FINITE-MEROMORPHIC EXTENSION**  
Created: 2026-08-23  
Depends on: `L-105300`, `L-105303` on this PR  
RH status: **not assumed**

## 1. Purpose

`L-105303` gives the exact entire-window Hermite--Pick form when every
critical point is simple.  This lemma proves the multiplicity-robust version
needed before importing any asymptotic xi-prime proportion.

Let `R` be a real rational function with partial fraction expansion

\[
R(z)=az+b+
\sum_c\sum_{r=1}^{m_c} a_{c,r}(z-c)^{-r},
\qquad a,b\in\mathbb R,
\tag{L-105310.1}
\]

with the nonreal poles and coefficients paired by conjugation.  Define the
affine-centered Pick kernel

\[
\mathcal K_R(z,w)
=
\frac{R(z)-\overline{R(w)}}{z-\bar w}-a.
\tag{L-105310.2}
\]

For every finite source-fixed family of evaluation/derivative functionals,
the compressed matrix is a Hermitian congruence of the direct sum of the pole
blocks below.

## 2. Simple blocks

For a simple pole `c` of residue `rho_c`,

\[
\mathcal K_c(z,w)
=-\frac{\rho_c}{(z-c)(\bar w-c)}.
\tag{L-105310.3}
\]

At a real critical point of `p`, with `R=p/p'` and
`rho_c=p(c)/p''(c)`, this is positive rank one exactly when `rho_c<0`, the
Rolle-generating orientation.  A wrong extremum is negative semidefinite.
A simple nonreal conjugate pair has coefficient matrix

\[
\begin{pmatrix}0&-\rho_c\\-\bar\rho_c&0\end{pmatrix}
\]

and hence positive index one.

## 3. Confluent real blocks

At a real pole `c` of order `m`, use the jet basis

\[
(z-c)^{-1},\ldots,(z-c)^{-m}.
\]

The coefficient matrix is the symmetric anti-triangular Hankel matrix

\[
H_{ij}=
\begin{cases}
-a_{c,i+j-1},&i+j-1\le m,\\
0,&i+j-1>m.
\end{cases}
\tag{L-105310.4}
\]

Symmetric elimination of the lower principal-part coefficients is a
congruence and reduces the block to a nonzero scalar multiple of the reversal
matrix `J_m`. Therefore

\[
\boxed{n_+(H_c)\le\lceil m/2\rceil.}
\tag{L-105310.5}

## 4. Confluent nonreal blocks

A conjugate pair of order `m` has coefficient matrix

\[
\begin{pmatrix}0&B\\B^*&0\end{pmatrix}.
\tag{L-105310.6}
\]

Its nonzero spectrum is symmetric about zero, so

\[
\boxed{n_+\le m.}
\tag{L-105310.7}

All these bounds survive finite analytic compression because congruence cannot
increase positive index.

## 5. Rank--trace with a nuisance ledger

Let `G` be the number of simple real negative-residue poles and let `nu` bound
the positive index of every confluent or nonreal block.  If `K` is any
source-fixed finite compression, then

\[
n_+(K)\le G+\nu.
\]

The Hermitian rank--trace inequality gives

\[
\boxed{
G\ge
\frac{(\operatorname{tr}K)_+^2}{\|K\|_{\rm HS}^2}-\nu.
}
\tag{L-105310.8}

This is the compressed, multiplicity-robust counterpart of the full trace-form
signature in `L-105300/L-105303`.

## 6. Scope

The theorem is finite algebra.  It does not estimate the Xi contour matrix or
its canonical-product tail.  Those are the open arithmetic inputs in
`T-105310`.
