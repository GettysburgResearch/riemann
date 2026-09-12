# T-14202 — Form-dense finite-element completeness for localized Weil negativity

Claim ID: T-14202  
Title: Every negative localized Weil ground state is detected by a finite rational hat-function matrix  
Status: PROPOSED  
Authoring agent: `gpt56-05-k`  
Created: 2026-07-29  
Dependencies: Suzuki arXiv:2606.09096, Theorem 1.1, equations (1.6)--(1.8), and Corollary 1.2; standard `H_0^1` finite-element density  
Scope: localized Weil form at one fixed finite support radius  
Related counterexample candidates: none

## Statement

Fix `a>0`. Let `Q_a` be Suzuki's localized closed Weil form on `L^2(-a,a)`
and let

\[
 \lambda(a)=\inf_{0\ne v}\frac{Q_a(v)}{\|v\|_2^2}.
\]

For each `m>=2`, let `V_m(a)` be the continuous piecewise-linear functions on
the uniform partition

\[
 -a=x_0<x_1<\cdots<x_m=a
\]

that vanish at both endpoints. Define the finite generalized Ritz value

\[
 \lambda_m(a)
 =\min_{0\ne v\in V_m(a)}
   \frac{Q_a(v)}{\|v\|_2^2}.
\]

Then

\[
 \boxed{\lambda_m(a)\downarrow\lambda(a)}
\]

along every nested refinement sequence of meshes.

Consequently, if RH is false, there exist:

- a positive rational support `a`;
- a finite rational mesh;
- a real rational, and hence dyadic after approximation, coefficient vector;

such that the corresponding finite localized Weil quadratic value is strictly
negative.

For fixed rational support and mesh, the mass matrix is exact rational and every
Weil matrix entry is rigorously computable from:

1. finitely many prime powers `q<=exp(2a)`;
2. compact real integrals of the smooth nonprime kernel;
3. outward interval arithmetic.

Thus the localized Weil route also admits a countable finite proof-producing
search that is existentially complete under the imported source theorems.

## Proof

Suzuki proves that for `v in H_0^1(-a,a)`,

\[
 Q_a(v)=\langle G_aDv,Dv\rangle_{L^2},
\]

where `G_a` is the bounded integral operator obtained from the continuous screw
kernel on the compact square `[-a,a]^2`. Hence `Q_a` is continuous under
`H_0^1` convergence:

\[
 |Q_a(v)-Q_a(w)|
 \le \|G_a\|\,\|D(v-w)\|_2
      (\|Dv\|_2+\|Dw\|_2).
\]

Suzuki's Corollary 1.2 states that `lambda(a)` is already the infimum over
`C_c^infty(-a,a)`. Standard one-dimensional finite-element interpolation
approximates every such smooth function in `H_0^1`. Therefore every Rayleigh
quotient within `epsilon` of `lambda(a)` is approximated by a hat-function
Rayleigh quotient within `o(1)`. Since every finite Ritz value is bounded below
by `lambda(a)`, nestedness gives

\[
 \lambda_m(a)\downarrow\lambda(a).
\]

If RH is false, L-14201 gives a rational `a` with `lambda(a)<0`. A sufficiently
fine mesh has `lambda_m(a)<0`. The corresponding finite real matrix has a strict
negative direction; rational and dyadic vectors are dense, so a rational or
dyadic direction retains the sign.

For the computational statement, `|x-y|<=2a` on the integration square. In
Suzuki's explicit screw kernel, only prime powers with `log q<=|x-y|` occur, so
only `q<=exp(2a)` can contribute. Splitting the compact integration domain at
the finitely many lines `|x-y|=log q` reduces the prime part to elementary
piecewise-polynomial/exponential integrals, while the remaining continuous
terms admit directed quadrature. ∎

## Relationship to the Connes finite matrices

This theorem proves completeness for an explicit form-dense hat-function
family. It does **not** prove that the particular Connes--van Suijlekom or
Connes--Consani--Moscovici Galerkin spaces are form-dense.

Groskin's July 2026 dictionary proves that every vector in those particular
finite spaces gives an exact Guinand--Weil zero sum and supplies a sharp
archimedean tail budget. That is an excellent certificate interface, but a
separate Mosco/form-density theorem is still required before that specific
matrix sequence can be called existentially complete.

## Gap audit

- The result has no rate in `m` and no practical support bound.
- Interval quadrature and prime enumeration still require independent
  implementations for a promoted counterexample.
- A finite positive hat matrix does not certify the complete form positive.
- The source identification of `Q_a` and all normalizations must be reviewed.

## Suggested next attack

Implement a small `a,m` directed control and compare it against the existing
CvS/CCM matrix at the same support. Then investigate whether the latter spaces
contain or stably approximate the hat-function form core.
