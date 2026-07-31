# R-15403 — Pointwise Hankel strictness does not yield a uniform moat

Claim ID: `R-15403`  
Title: Boundary convergence, finite offset grids, and pointwise norms below one cannot prove the uniform strict-contraction target  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: `L-15420`  
Scope: false compactness shortcuts for `T-15408`  
Related counterexample candidates: none

## Explicit family

Fix `delta>0`. For `0<epsilon<delta`, put

\[
 p_\epsilon=i\epsilon,
 \qquad
 q_\epsilon=i(2\delta-\epsilon),
 \tag{R-15403.1}
\]

and define

\[
 \phi_\epsilon
 =\overline{b_{p_\epsilon}}b_{q_\epsilon}.
 \tag{R-15403.2}
\]

This is the isolated Blaschke-pair symbol from `L-15420` with crossing
parameter

\[
 \omega=\delta-\epsilon.
 \]

Hence

\[
 \boxed{
 \|\mathsf H_{\phi_\epsilon}\|
 =1-\frac\epsilon\delta<1}
 \tag{R-15403.3}
\]

for every fixed `epsilon>0`, but

\[
 \boxed{
 \sup_{0<\epsilon<\delta}
 \|\mathsf H_{\phi_\epsilon}\|=1.}
 \tag{R-15403.4}
\]

The corresponding Toeplitz floor is

\[
 \boxed{
 \inf_{\|f\|=1}\|T_{\phi_\epsilon}f\|^2
 =\frac{2\epsilon}{\delta}
  -\frac{\epsilon^2}{\delta^2}
 \longrightarrow0.}
 \tag{R-15403.5}
\]

## Strong boundary convergence still fails

For every real `t!=0`,

\[
 \overline{b_{i\epsilon}(t)}\longrightarrow1,
 \]

while

\[
 b_{i(2\delta-\epsilon)}(t)
 \longrightarrow b_{2i\delta}(t).
 \]

Therefore

\[
 \phi_\epsilon(t)\longrightarrow b_{2i\delta}(t)
 \tag{R-15403.6}
\]

pointwise almost everywhere and in every local finite `L^p` norm. The limiting
symbol is inner, so its Hankel operator is zero, whereas

\[
 \|\mathsf H_{\phi_\epsilon}\|\longrightarrow1.
 \tag{R-15403.7}
\]

Thus the map

\[
 \phi\longmapsto\|\mathsf H_\phi\|
 \]

is not continuous in any of these boundary topologies at a shrinking
reciprocal-Blaschke bubble.

## Refuted inferences

The family disproves each of the following proof patterns.

### 1. Pointwise strictness

```text
for every omega, ||H_omega||<1
therefore sup_omega ||H_omega||<1
```

This is false without a uniform mechanism.

### 2. Finite-grid verification

A finite offset grid misses a bubble whose width is controlled by the unknown
quantity `delta-omega`. Refining a grid finitely never proves a symbolic moat.

### 3. Boundary-symbol convergence

Pointwise, local-`Lp`, or finite-Fourier-coefficient convergence to an inner
symbol does not control Hankel norm.

### 4. Compactness away from crossings

Continuity on every closed interval avoiding a pole-crossing offset gives only
local moats. An unknown off-line zero inserts a new endpoint at which those
moats collapse.

### 5. Small finite-rank defect

The defect may have rank one and be supported on an arbitrarily narrow Poisson
scale while retaining norm almost one. Rank, trace on a fixed frame, and weak
convergence do not substitute for operator-norm control.

## Correct positive requirement

A valid positive proof must establish one global statement before knowing any
zero displacement, such as

\[
 T_\omega^*T_\omega\succeq\eta I
 \qquad(0<\omega<1/2)
 \]

with one exact `eta>0`, or an equivalent complete Schur/canonical-system
inequality. `T-15408` proves that this is RH-equivalent.

## Proof boundary

The counterexample family is exact Hardy-space algebra. Its role is procedural:
it blocks invalid compactness arguments. It neither proves nor disproves RH.
