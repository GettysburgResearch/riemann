# R-95050 — No source-free linear transfer can recover a reciprocal state from its logarithmic derivative

Claim ID: `R-95050`  
Status: **EXACT ALGEBRAIC NO-GO / HARDY-BOUNDARY FIREWALL**  
Created: 2026-08-16  
Scope: causal Dirichlet-convolution and finite-dilation linear transfers

Let

\[
A(s)=1+\sum_{n\ge2}{a(n)\over n^s}
\]

be normalized, and let

\[
C(s)=-{A'(s)\over A(s)}
=\sum_{n\ge1}{c(n)\over n^s}.
\]

Every logarithmic derivative has

\[
c(1)=0,
\]

whereas the reciprocal state has

\[
a(1)=1.
\]

For every arithmetic kernel `k`,

\[
(k*c)(1)=k(1)c(1)=0.
\]

The same is true for every finite linear combination of dilations `delta_m*c`: no term with `m>=1` creates coefficient one. Therefore

\[
\boxed{
A\ne T(C)
}
\]

for every source-free causal linear Dirichlet-convolution/dilation operator `T`.

This is the coefficient-level form of the familiar fact that a logarithmic derivative determines a function only up to a multiplicative constant.

There is also no bounded multiplier inverse on any right-half-plane Wiener algebra: as `Re s -> +infinity`,

\[
C(s)\to0,
\qquad A(s)\to1,
\]

so the putative multiplier `A(s)/C(s)` is unbounded.

Consequences:

1. the Hardy boundary in PR #474's backward inversion is structural, not bookkeeping;
2. a positive Q4 source cannot linearly generate the root reciprocal state without an external unit channel;
3. any legitimate bridge must be nonlinear/triangular as in `L-95051`, or quadratic/passive with the boundary retained explicitly.
