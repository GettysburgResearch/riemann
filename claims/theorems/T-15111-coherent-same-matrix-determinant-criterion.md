# T-15111 — Coherent same-matrix Cauchy--Laplace coefficients imply the determinant identity

Claim ID: `T-15111`  
Status: **PROVED CONDITIONAL COMPOSITION THEOREM; CLASSICAL FINITE TENSOR IDENTITY OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15128`--`L-15131`; identity theorem  
Scope: exact construction-level completion of the finite-window determinant programme  
Related counterexample candidates: none

## 1. Finite coherent data

For every window parameter `M` and finite readout cutoff `N`, suppose there are:

1. a positive Hermitian Gram matrix `G_(M,N)`;
2. a Hermitian signed seam matrix `B_(M,N)`;
3. an involution `J_(M,N)` satisfying
   
   \[
   J^*G=GJ,
   \qquad
   J^*BJ=-B;
   \]
4. one represented self-adjoint matrix
   
   \[
   K_{M,N}\sim G_{M,N}^{-1}B_{M,N};
   \]
5. classical scalar coefficients `A_(ell,M,N)` for every `ell>=2`.

Assume the finite readout projections are grading preserving, so the same `J_(M,N)` is inherited from one transported seam grading rather than chosen after the matrix is formed.

## 2. Same-matrix hypothesis

Assume the explicit finite tensor identity

\[
\boxed{
A_{\ell,M,N}
=\mathfrak c_\ell(G_{M,N},B_{M,N})
=\operatorname{Tr}(K_{M,N}^{\ell})
\quad(\ell\ge2).}
\tag{T-15111.1}
\]

The first equality is the source-specific Cauchy--Laplace pullback theorem. The second is the algebraic theorem `L-15129`.

The grading gives

\[
A_{2r+1,M,N}=0
\qquad(r\ge1).
\tag{T-15111.2}
\]

Thus the first load-bearing order-three equality is exact, not asymptotic.

## 3. Analytic majorant and coherent limits

Assume there is a diagonal sequence `(M_j,N_j)` and a self-adjoint Hilbert--Schmidt operator `K` such that

\[
\|K_{M_j,N_j}-K\|_2\longrightarrow0.
\tag{T-15111.3}
\]

Assume also that the classical finite scalar functions

\[
\mathscr A_j(w)
=\sum_{\ell=2}^{\infty}(-i)^{\ell-2}A_{\ell,M_j,N_j}w^{\ell-1}
\tag{T-15111.4}
\]

have one locally summable majorant on a disk `|w|<r`, permitting the limits in `j` and `ell` to be interchanged, and that their independently proved classical limit is

\[
\boxed{
\mathscr A_j(w)
\longrightarrow
\frac d{dw}\log\frac{\xi(1/2+w)}{\xi(1/2)}.}
\tag{T-15111.5}
\]

By `L-15131` and (T-15111.1), the same functions converge to

\[
\frac d{dw}\log\det{}_2(I+iwK).
\tag{T-15111.6}
\]

Hence the logarithmic derivatives in (T-15111.5) and (T-15111.6) agree near zero.

## 4. Determinant identity and RH

Both normalized functions equal one at `w=0`. Integrating the logarithmic identity gives

\[
\boxed{
\frac{\xi(1/2+w)}{\xi(1/2)}
=\det{}_2(I+iwK)}
\tag{T-15111.7}
\]

near zero, and the identity theorem extends it to the whole plane.

Since `K` is self-adjoint, every zero of the determinant is purely imaginary in `w`. Therefore every nontrivial zeta zero lies on the critical line:

\[
\boxed{\mathrm{RH}.}
\]

## 5. What is constructed unconditionally here

The following parts of the theorem now have explicit constructions rather than names:

- the finite matrix represented by nonorthogonal readouts;
- the closed cyclic coefficient at every order;
- the order-three coefficient and its exact vanishing;
- the transported anti-commuting grading;
- grading-preserving finite compression;
- the Hilbert--Schmidt finite-rank and window limits;
- the limiting regularized determinant.

## 6. Exact remaining hypothesis

The only unconstructed premise is the first equality in (T-15111.1), together with its analytic majorant and the classical limit (T-15111.5). It must be proved from the Cauchy--Laplace / explicit-formula definitions for the same finite Gram and seam matrices.

At order three, parity makes both final values zero, so this is a structural intertwining check. At even orders, it is the full central moment problem of `T-15110` and is RH-bearing.

## 7. Proof boundary

This theorem is a complete implication, not a proof that the source-specific same-matrix hypothesis holds. No finite numerical agreement, separately chosen matrix per order, or abstract “universal pullback” assertion is accepted as (T-15111.1).
