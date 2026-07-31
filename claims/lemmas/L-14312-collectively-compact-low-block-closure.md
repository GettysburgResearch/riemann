# L-14312 — Uniform tightness closes a growing corrected low block

Claim ID: `L-14312`  
Title: Fixed-mode decay plus a common finite-rank tightness modulus forces norm decay of growing self-adjoint low blocks  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: elementary Hilbert-space approximation; `T-14302` for the RH lower-envelope application  
Scope: the growing corrected low matrices in PR #152 and any nested finite-section lower-floor argument  
Related counterexample candidates: none

## Purpose

The statement

```text
every fixed row and column tends to zero
```

does **not** control the norm of a matrix whose dimension tends to infinity. A
negative direction may move to a new coordinate at every level. This lemma
identifies the exact additional condition that rules out such an escaping mode.

The condition is a common finite-rank tightness estimate, equivalently a
collective-compactness gate after the changing low spaces are embedded in one
Hilbert space.

## Setup

Let `H` be a separable Hilbert space. For each `j`, let

\[
 J_j:\mathbb C^{d_j}\longrightarrow H
\]

be an isometry, and let `K_j` be a Hermitian `d_j x d_j` matrix. Extend the
matrix to `H` by

\[
 \widetilde K_j=J_jK_jJ_j^*.
 \tag{L-14312.1}
\]

Let

\[
 P_1\preceq P_2\preceq\cdots\longrightarrow I
 \quad\hbox{strongly}
\]

be fixed finite-rank orthogonal projections on `H`.

## Main theorem

Assume:

1. **uniform boundedness**
   \[
     \sup_j\|\widetilde K_j\|<\infty;
     \tag{L-14312.2}
   \]
2. **fixed-core decay**: there is a dense set `D subset H` such that
   \[
     \widetilde K_jx\longrightarrow0
     \qquad(x\in D);
     \tag{L-14312.3}
   \]
3. **uniform tightness in a common frame**
   \[
     \boxed{
     \lim_{m\to\infty}
     \sup_j\|(I-P_m)\widetilde K_j\|=0.}
     \tag{L-14312.4}
   \]

Then

\[
 \boxed{\|K_j\|=\|\widetilde K_j\|\longrightarrow0.}
 \tag{L-14312.5}
\]

Consequently,

\[
 \boxed{\lambda_{\min}(K_j)\ge-\varepsilon_j,
 \qquad \varepsilon_j\downarrow0.}
 \tag{L-14312.6}
\]

### Proof

Uniform boundedness and convergence on the dense core imply strong convergence
on all of `H`. Indeed, for `x in H`, choose `x_0 in D`; then

\[
 \|\widetilde K_jx\|
 \le \|\widetilde K_j(x-x_0)\|+\|\widetilde K_jx_0\|,
\]

and first choose `x_0` close to `x`, then let `j` tend to infinity.

Fix `epsilon>0`. By (L-14312.4), choose `m` such that

\[
 \sup_j\|(I-P_m)\widetilde K_j\|<\epsilon.
\]

Since every `widetilde K_j` is self-adjoint,

\[
 \|\widetilde K_j(I-P_m)\|
 =\|(I-P_m)\widetilde K_j\|<\epsilon.
\]

Moreover,

\[
 \widetilde K_j-P_m\widetilde K_jP_m
 =(I-P_m)\widetilde K_j
 +P_m\widetilde K_j(I-P_m),
\]

so

\[
 \|\widetilde K_j-P_m\widetilde K_jP_m\|<2\epsilon.
 \tag{L-14312.7}
\]

The range of `P_m` is finite-dimensional. Strong convergence therefore
implies

\[
 \|P_m\widetilde K_jP_m\|\longrightarrow0.
\]

Hence `limsup_j ||widetilde K_j|| <= 2 epsilon`. Since `epsilon` was arbitrary,
(L-14312.5) follows. The eigenvalue bound is immediate. QED.

## Collective-compactness formulation

Condition (L-14312.4) implies that

\[
 \bigcup_j\widetilde K_j\{x:\|x\|\le1\}
\]

is relatively compact. Conversely, for a uniformly bounded self-adjoint
family, collective compactness supplies projections `P_m` satisfying
(L-14312.4). Thus the theorem may be summarized as

```text
strong convergence to zero
+ collective compactness
=> operator-norm convergence to zero.
```

The self-adjointness is load-bearing: it turns one-sided range tightness into
both left and right tightness.

## Quantitative finite certificate

Suppose a proof packet gives, for one fixed `m`,

\[
 \|(I-P_m)\widetilde K_j\|\le\delta_{j,m}
 \tag{L-14312.8}
\]

and a directed finite-dimensional enclosure

\[
 \|P_m\widetilde K_jP_m\|\le\rho_{j,m}.
 \tag{L-14312.9}
\]

Then

\[
 \boxed{
 \|K_j\|\le\rho_{j,m}+2\delta_{j,m}.}
 \tag{L-14312.10}
\]

This is the proof-producing form. No eigensolver is required: `rho` may be
certified by exact rational `LDL*` tests for

\[
 -\rho P_m\preceq P_m\widetilde K_jP_m\preceq\rho P_m.
\]

## Application to the PR #152 corrected low matrix

Let

\[
 K_j
 =B_j-h_j^{-1}R_j^*M_j^{-1}R_j
 \tag{L-14312.11}
\]

be the corrected low matrix in `L-14308`. Embed every low space in one fixed
scaled-coordinate Hilbert space. If

1. every fixed exact radical mode has vanishing corrected matrix action;
2. the family `K_j` is uniformly bounded;
3. one proves the common-frame tightness (L-14312.4);

then

\[
 \lambda_{\min}(K_j)\ge-o(1).
\]

Together with a complement floor `gamma_j>=-o(1)` and an assembly radius
`delta_j=o(1)`, `T-14302` gives a cofinal lower envelope and therefore RH.

The theorem removes matrix dimension from the final estimate. The actual
analytic burden is precisely the tightness gate: no low-energy direction may
escape to ever-new generalized-prolate coordinates.

## Why fixed rows are insufficient

Let `H=ell^2(N)` with standard basis `e_1,e_2,...`, and put

\[
 \widetilde K_j=e_je_j^*.
 \tag{L-14312.12}
\]

Then for every fixed `x in ell^2`,

\[
 \widetilde K_jx=x_je_j\longrightarrow0,
\]

and every fixed matrix entry tends to zero. Nevertheless

\[
 \|\widetilde K_j\|=1
\]

for every `j`. The family fails (L-14312.4): its unit images contain the
noncompact set `{e_j}`.

Thus entrywise decay, fixed-vector decay, bounded rank, or decay of every
previously named mode does not close the growing block.

## Gap audit

- The theorem is exact but does not prove tightness for the arithmetic low
  packet.
- The embeddings `J_j` must use one coherent scaled-coordinate normalization;
  comparing unrelated bases is meaningless.
- A bound on singular values alone is insufficient if the corresponding
  singular vectors can wander, as (L-14312.12) shows.
- Finite numerical spectra do not establish (L-14312.4).
- Proving tightness for the actual corrected low blocks is an RH-strength
  global statement unless it is obtained from an independent radical-frame or
  symbol-compactness theorem.

## Suggested next attack

Construct exact radical local frames for the generalized-prolate packet and
bound the **operator norm of the whole tail synthesis map**, not the tails of
fixed columns. `L-14313` gives the dimension-free Schur estimate once that
operator norm is available.
