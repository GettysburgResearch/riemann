# L-105320 — Reciprocal coefficients and exact zero-free Wick cancellation

Claim ID: `L-105320`  
Status: **PROVED EXACT IN THE FINITE DIRICHLET ALGEBRA**  
Created: 2026-08-23  
Depends on: the von Mangoldt convolution definitions used by the frozen
xi-prime explicit formula  
RH status: **not assumed**

## 1. Frozen reciprocal coefficients

Let `Lambda` denote the von Mangoldt arithmetic function and let `*` be
Dirichlet convolution. Freeze a nonzero scalar `L`. Formally put

\[
A(s)=\sum_{n\ge2}{\Lambda(n)\over n^s}.
\]

The reciprocal frozen logarithmic derivative is

\[
R_L(s)={1\over L-A(s)}.
\tag{L-105320.1}
\]

Its Dirichlet coefficients are finite at every integer:

\[
b_L(1)=L^{-1},
\]

and, for `N>1`,

\[
\boxed{
b_L(N)=\sum_{m=1}^{\Omega(N)}
 L^{-m-1}\Lambda^{*m}(N).
}
\tag{L-105320.2}
\]

The sum stops at `Omega(N)` because every von Mangoldt factor consumes at
least one prime factor counted with multiplicity.

## 2. Exact bridge to the xi-prime coefficient family

The frozen xi-prime coefficient family is

\[
C(N;L)=-\Lambda(N)+
\sum_{j=0}^{\Omega(N)-1}
L^{-j-1}\bigl[(\Lambda\log)*\Lambda^{*j}\bigr](N).
\tag{L-105320.3}
\]

For every `m>=1`, logarithmic differentiation of a Dirichlet convolution gives

\[
\boxed{
\log N\,\Lambda^{*m}(N)
=m\bigl[(\Lambda\log)*\Lambda^{*(m-1)}\bigr](N).
}
\tag{L-105320.4}
\]

Indeed, in every ordered factorization `N=n_1...n_m`, the sum
`log n_1+...+log n_m` is `log N`; symmetry makes the `m` differentiated
positions equal.

Differentiating (L-105320.3) in the frozen parameter and using
(L-105320.4) yields, for every `N>1`,

\[
\boxed{
-\partial_L C(N;L)=\log N\,b_L(N).
}
\tag{L-105320.5}
\]

Thus the low-order reciprocal source is the frozen-parameter derivative of the
already formalized xi-prime coefficient source, followed by the positive
Hardy divisor `1/log N`. It is not an unrelated coefficient family.

## 3. Finite entire preconditioner

For a finite cutoff `X`, define the entire Dirichlet polynomial

\[
A_X(s)=\sum_{2\le n\le X}{\Lambda(n)\over n^s}
\]

and the zero-free entire function

\[
\boxed{
W_{L,X}(s)=\exp\!\left(-{A_X(s)\over2L}\right).
}
\tag{L-105320.6}
\]

Put `x=A_X/L`. Then the exact identity

\[
\boxed{
{L W_{L,X}(s)^2\over L-A_X(s)}
={e^{-x}\over1-x}
=1+\sum_{m\ge2}c_mx^m
}
\tag{L-105320.7}
\]

holds as an analytic identity wherever `L-A_X` is nonzero and as a formal
power-series identity everywhere. Here

\[
\boxed{
c_m=\sum_{j=0}^m{(-1)^j\over j!}={!m\over m!}.}
\tag{L-105320.8}
\]

In particular,

\[
c_0=1,
\qquad c_1=0,
\qquad 0<c_m\le{1\over2}\quad(m\ge2).
\tag{L-105320.9}
\]

The vanishing `c_1=0` is exact first-chaos cancellation.

## 4. Inertia preservation

Let a finite Pick/Hermite compression be built from observation functions
`phi_j`. Replacing them by `W_(L,X) phi_j` multiplies every real simple
critical residue atom by `|W_(L,X)(c)|^2>0`; at nonreal or confluent blocks it
is an invertible congruence. Therefore the complete positive and negative
indices are unchanged.

This is not an inverse completion and does not cancel the zero detector. It is
a finite source-fixed congruence on the low-order critical-residue matrix.

## 5. Higher-order variant

For a fixed integer `K>=1`, the entire zero-free function

\[
W_{K,L,X}(s)=
\exp\!\left[-{1\over2}
\sum_{j=1}^K{1\over j}
\left({A_X(s)\over L}\right)^j\right]
\]

satisfies

\[
{L W_{K,L,X}^2\over L-A_X}
=
\exp\!\left(\sum_{j>K}{x^j\over j}\right).
\tag{L-105320.10}
\]

Thus all source degrees `1,...,K` vanish. The present packet uses `K=1`,
which already has enough quantitative reserve and the mildest boundary cost.

## 6. Scope

The identity is exact. It does not identify the finite frozen reciprocal with
the actual `xi/xi'` contour observable. The entry-dependent freezing,
archimedean variation, horizontal boundaries and canonical-product tail are
the open transfer theorem `WXFER105320`.
