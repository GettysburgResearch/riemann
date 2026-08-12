# R-91101 — Passivity shortcuts that do not close the Brownian–theta network

Claim ID: `R-91101`  
Status: **EXACT SCOPE FIREWALL**  
Created: 2026-08-11  
Depends on: PRs #376, #398; `L-91105`--`L-91108`  
RH status: **unproved**

## 1. Symmetric probability is insufficient

The representation

\[
 M(r)=\mathbb E e^{rZ},\qquad Z\stackrel d=-Z,
\]

implies real-axis positivity and log-convexity, but not the matrix kernel

\[
 \left(\frac{\ell_a(r_i)+\ell_a(r_j)}{r_i+r_j}\right)\succeq0.
\]

Symmetric finitely supported laws can have characteristic functions with nonreal zeros. Any proof must use the specific Brownian/gamma/theta law, not symmetry alone.

## 2. Pointwise multiplier contraction is insufficient

Equation `L-91106.3` uses the bounded multiplier

\[
 |\tanh(aZ)|<1.
\]

After observation, the defect is a noncommutative anticommutator. A contraction before the observation map does not imply contraction of the compressed transfer. This is exactly the old `CKE` failure on PR #202 and the safe one-Green countermodel on PR #398.

## 3. Scalar one-Green positivity is insufficient

PR #398 gives an exact symmetric factor with:

```text
positive completely monotone one-Green kernel;
boundary unitarity;
horizontal cocycle;
actual zeta Jordan factor retained after multiplication;
strictly indefinite target Pick matrices.
```

Therefore the Brownian/theta state identity must couple the archimedean and arithmetic parts before scalarization.

## 4. Finite gamma truncations cannot be required to be globally positive

PR #376 proves high-frequency Bohr instability for the current finite Brownian/Dirichlet producers. A viable gamma construction must either:

```text
retain the infinite Gamma tail exactly as a boundary reservoir;
prove a height-dependent diagonal theorem;
or work directly with the infinite positive generator.
```

Global real-rootedness of every finite partial gamma sum is not a legitimate intermediate claim.

## 5. Log-concavity or TP2 is insufficient

A two-point or diagonal inequality does not imply all finite Pick matrices. The target is complete reflection positivity on exponential polynomials. Any use of log-concavity must be upgraded to a full Dirichlet-to-Neumann or total-positivity theorem at every order.

## 6. Mandatory controls for TDI

A proposed theta-DtN proof must:

1. reproduce the exact Xi ratios, not merely their first derivatives;
2. retain the pairwise theta variance channels of PR #202;
3. retain the half-size bias `(A^2-D^2)^(1/4)` in gamma coordinates;
4. fail on PR #398's planted symmetric factor `F_y xi` at the boundary-identification step;
5. avoid invoking zero-freeness to define the same Weyl function it is meant to prove analytic;
6. avoid finite-truncation global stability.

These controls separate a constructive Hilbert-space object from another RH-equivalent relabeling.
