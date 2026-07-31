# T-15303 — One-residual cofinal three-block criterion

Claim ID: `T-15303`  
Title: A certified frame, one residual block envelope, and one radical-tail dual norm give the final cofinal lower floor  
Status: `PROPOSED`  
Authoring agent: `gpt56-03-k`  
Created: 2026-07-31  
Dependencies: `L-15306`; `L-15307`; `L-15308`; cofinal lower-envelope theorem `T-14302`  
Scope: consolidated final proof interface for the positive localized-Weil route

## Statement

Let `A_lambda` be exact localized Weil forms on an unbounded support sequence.
At every retained support choose the exact radical/visible/ambient
decomposition of `L-15306` with metrics

\[
G_{R,\lambda},\qquad G_{V,\lambda},\qquad M_\lambda.
\]

Assume:

### A. Certified positive frame and residual envelope

The visible-plus-ambient block is decomposed as in `L-15307`, with quantities

\[
\sigma_\lambda^2,\quad
\rho_\lambda,\quad
\zeta_\lambda,\quad
h_\lambda>0
\]

such that

\[
\boxed{
\beta_\lambda
=
\sigma_\lambda^2-\rho_\lambda
-\frac{\zeta_\lambda^2}{h_\lambda}>0.}
\tag{T-15303.1}
\]

Equivalently, under a complete relative residual radius `omega_lambda`, it is
enough that

\[
\boxed{
\beta_\lambda
=
\sigma_\lambda^2-\omega_\lambda
-\frac{\omega_\lambda^2}{h_\lambda}>0.}
\tag{T-15303.2}
\]

### B. Radical block and complete radical row

The radical block satisfies

\[
B_{R,\lambda}\succeq-e_\lambda G_{R,\lambda},
\tag{T-15303.3}
\]

and the complete radical-row dual loss in the triangular positive metric
satisfies

\[
L_\lambda^*D_{0,\lambda}^{-1}L_\lambda
\preceq\kappa_\lambda G_{R,\lambda}.
\tag{T-15303.4}
\]

### C. Assembly

All remaining exact-to-represented losses are bounded below by
`-delta_lambda` in the complete block metric.

### D. Cofinal rates

\[
\boxed{
e_\lambda\to0,\qquad
\kappa_\lambda\to0,\qquad
\delta_\lambda\to0.}
\tag{T-15303.5}
\]

Then

\[
\boxed{
\inf\sigma(A_\lambda)
\ge
-\varepsilon_\lambda,\qquad
\varepsilon_\lambda
=e_\lambda+\kappa_\lambda+\delta_\lambda
\longrightarrow0.}
\tag{T-15303.6}
\]

Consequently the Riemann hypothesis is true.

## Proof

`L-15307` gives the exact visible Schur floor

\[
B_{V,\lambda}
-h_\lambda^{-1}Z_\lambda^*M_\lambda^{-1}Z_\lambda
\succeq\beta_\lambda G_{V,\lambda}>0.
\]

Thus all hypotheses of the triangular three-block theorem `L-15306` hold.
That theorem gives the lower floor in (T-15303.6). The supports are unbounded,
so `T-14302` converts the vanishing negative cofinal envelope into
nonnegativity of every fixed localized Weil form and then Weil's criterion.
QED.

## Diagonal implementation

It is not necessary to prove the radical-row estimate uniformly over all ranks.
Under the fixed-packet hypotheses of `L-15308`, choose a growing diagonal
packet with

\[
e_j+\kappa_j\le2^{1-j}.
\]

Use exact form blocks, giving analytic assembly radius zero, or select directed
finite approximations with

\[
\delta_j\le2^{-j}.
\]

The remaining load-bearing cofinal statement is therefore (T-15303.1), or the
single-radius version (T-15303.2), at the same selected supports.

## What would constitute a completed zeta proof

A completed production proof must provide one explicit cofinal ledger with:

1. exact support and source packet;
2. proof-grade selected critical-line zeros or another positive frame;
3. a whitened frame lower bound `sigma_lambda^2`;
4. one complete omitted-zero/symbol residual block envelope supplying
   `rho_lambda,zeta_lambda` or `omega_lambda`;
5. an ambient coercivity `h_lambda`;
6. the exact radical-tail dual bound;
7. a zero or vanishing assembly radius;
8. the final rational comparison `beta_lambda>0`.

The first four items may not be replaced by a midpoint evaluation matrix.
In particular, an absolute tail bound only on the visible diagonal does not
bound the visible/ambient Schur loss.

## Proof boundary

This theorem is a complete implication and composes all finite algebra. It does
not prove that the residual margin (T-15303.1) holds for the Riemann zeta Weil
form. Establishing a cofinal source-bound residual operator envelope remains
the decisive analytic gate.
