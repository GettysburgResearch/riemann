# R-102728 — Free pair energy does not control the physical restriction

Claim ID: `R-102728`  
Status: **PROVED SOURCE-BLIND RESTRICTION COUNTERMODEL**  
Created: 2026-08-23  
Depends on: `L-102748--L-102749`  
RH status: **not assumed**

The polylogarithmic free labelled pair norm in `L-102748` is not, by itself, a
bound for the physical one-parameter observation.

Let \(\phi\in C_c^1(\mathbb R)\) be nonzero.  For each \(N\), choose distinct
frequencies

\[
 \lambda_j=\frac j{N^2},
 \qquad 1\le j\le N,
\]

and orthonormal labels \(e_j\).  Define

\[
 \mathcal F_N(u)
 =\frac1{\sqrt N}
 \sum_{j=1}^N
 \phi(u-\lambda_j)e_j.
\]

Its labelled norm is exactly

\[
 \|\mathcal F_N\|_{L^2\otimes\ell^2}^2
 =\|\phi\|_2^2.
\]

Collapse the labels before taking the physical norm:

\[
 F_N(u)
 =\frac1{\sqrt N}
 \sum_{j=1}^N\phi(u-\lambda_j).
\]

Since \(\max_j|\lambda_j|\le1/N\), translation continuity gives

\[
 \left\|
 F_N-\sqrt N\,\phi
 \right\|_2=o(\sqrt N).
\]

Therefore

\[
 \boxed{
 \|F_N\|_2^2
 =N\|\phi\|_2^2+o(N).
 }
\]

Thus a bounded free pair norm can have an arbitrarily large physical
restriction norm when distinct logarithmic products cluster.

The fixture is source-blind and does not refute the arithmetic statement
`DPWNC102749`.  It proves that any successful argument must use the literal
prime-product geometry, source signs or owner transport; Fock energy and
same-product multiplicity alone are insufficient.
