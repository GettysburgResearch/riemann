# R-14301 — Fixed radical rows do not close a growing corrected low block

Claim ID: `R-14301`  
Title: Entrywise or fixed-mode decay is insufficient when the low-space dimension grows  
Status: `REFUTATION / SCOPE CORRECTION`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: none  
Scope: the final inference proposed after the scalar radical-tail ratio estimates on Issue #143  
Related counterexample candidates: none

## Refuted inference

The following implication is false:

```text
every fixed exact radical row and column tends to zero
therefore
lambda_min(B_j-h_j^-1 R_j^* M_j^-1 R_j) -> 0 from below.
```

The failure is purely infinite-dimensional. A bad mode may move to a new
coordinate at every level and therefore escape every fixed-row test.

## Exact counterexample

Let

\[
 H=\ell^2(\mathbb N)
\]

with standard basis `e_1,e_2,...`, and define

\[
 K_j=-e_je_j^*.
 \tag{R-14301.1}
\]

Then for every fixed pair `m,n`,

\[
 \langle K_je_m,e_n\rangle=0
\]

for all sufficiently large `j`. More strongly, for every fixed
`x in ell^2`,

\[
 K_jx=-x_je_j\longrightarrow0.
 \tag{R-14301.2}
\]

Nevertheless

\[
 \boxed{\lambda_{\min}(K_j)=-1}
 \tag{R-14301.3}
\]

for every level.

Thus even strong-operator convergence to zero, uniform norm boundedness, fixed
rank, and eventual vanishing of every fixed matrix entry do not imply a
shrinking negative spectral floor.

## Radical-tail version

Let the coefficient space at level `j` be

\[
 C_j=\operatorname{span}\{e_1,\ldots,e_j\}
\]

and define a tail synthesis map

\[
 V_je_m=0\quad(m<j),
 \qquad
 V_je_j=t_j,
 \qquad
 \|t_j\|=1.
 \tag{R-14301.4}
\]

Then every previously fixed tail column eventually vanishes, while

\[
 \|V_j\|=1.
\]

For a tail form with `Q(t_j,t_j)=-1`, the exact radical identity of `L-14309`
produces the matrix (R-14301.1). The example is abstract and does not assert
that the zeta Weil form has such a sequence; it proves that fixed-column decay
cannot exclude one.

## Correct replacement

There are two safe replacements.

### 1. Common-frame collective compactness

Embed all changing matrices in one Hilbert space and prove the uniform tail
condition

\[
 \lim_{m\to\infty}\sup_j
 \|(I-P_m)K_j\|=0
\]

for fixed finite-rank projections `P_m`. Then `L-14312` upgrades fixed-core
decay to operator-norm decay.

### 2. Whole-packet radical synthesis

Construct exact radical extensions of the entire low packet and prove

\[
 \|V_j\|_{coeff\to tail}\to0
\]

in a norm controlling both tail--tail and tail--complement Weil pairings.
`L-14313` then bounds the complete corrected matrix independently of its
dimension.

## Consequence for Issue #143

The scalar estimates

\[
 \mathfrak T_j/h_j\to0
\]

or

\[
 \mathfrak T_j^2/(h_j\|k_j\|^2)\to0
\]

control one chosen radical direction. They do not control every direction in
a support-dependent packet unless they are promoted to an operator-norm tail
synthesis estimate.

Therefore the growing low matrix is not a routine finite leftover. It is the
place where a hypothetical negative mode can escape. Any completed positive
proof must include one of the two uniform gates above.

## Classification

This refutes only an inference in the proof architecture. It is not evidence
for or against RH and it does not invalidate the exact scalar radical identity,
the complement floor, or the block Temple--Schur theorem.
