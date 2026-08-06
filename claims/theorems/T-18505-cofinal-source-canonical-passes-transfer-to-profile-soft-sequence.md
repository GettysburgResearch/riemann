# T-18505 — Cofinal source-canonical passes transfer to a profile-soft sequence

Claim ID: `T-18505`  
Title: An unbounded source-canonical direct ladder makes every exact buffered profile-soft Schur block positive  
Status: `PROVED CONDITIONAL TRANSFER; UNBOUNDED ARITHMETIC LOWER LAW AND EXHAUSTION OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-18512`; `L-18513`; `T-18504`; the complete-frame profile exporter

## Statement

For every level `j`, let `A_j` be the exact finite localized Weil matrix on a
metric space `(U_j,G_j)`. Assume an exact source-canonical split

\[
U_j=W_j\oplus_{G_j}E_j
\]

with

\[
C_j=A_j|_{E_j}\succ0,
\qquad
B_j-Z_j^*C_j^{-1}Z_j\succ0.
\tag{T-18505.1}
\]

Assume independently that a directed profile producer emits a buffered exact
spectral split

\[
U_j=S_j\oplus_{G_j}H_j,
\]

including an exact Riesz projector or interval graph enclosure for `S_j`, a
positive profile Gram, and its amplitude/support-derivative ledger.

Then

\[
\boxed{
A_{j,SS}-A_{j,SH}A_{j,HH}^{-1}A_{j,HS}\succ0.
}
\tag{T-18505.2}
\]

In particular the normalized profile-soft negative part is exactly zero at
every passing level.

### Proof

By `L-18513`, (T-18505.1) implies `A_j\succ0`; positivity transfers to the
Schur complement of every exact `G_j`-orthogonal split. QED.

## Quantitative form

If the source-canonical certificate proves

\[
A_j\succeq\delta_jG_j,
\qquad \delta_j>0,
\tag{T-18505.3}
\]

then

\[
\boxed{
A_{j,SS}-A_{j,SH}A_{j,HH}^{-1}A_{j,HS}
\succeq\delta_jG_{j,S}.
}
\tag{T-18505.4}
\]

Thus projector-angle estimates are needed for provenance and profile-phase
analysis, but not for the finite arithmetic sign once a complete source-
canonical lower matrix has passed.

## Cofinal composition

Suppose the passing levels form an unbounded sequence, the finite packets
exhaust the complete dangerous Suzuki/CCM hierarchy in the declared form
metric, and the radical-row/cross/assembly losses of `T-18504` tend to zero.
Then (T-18505.2), together with the hard-complement floor and the existing
three-block theorem, gives a cofinal localized lower envelope tending to zero
from below. Under the imported cofinal Weil criterion, this would imply RH.

A convenient sufficient arithmetic schedule is

\[
\inf_j
(\log c_j)
\lambda_{\min}
\left(
B_j-Z_j^*C_j^{-1}Z_j,
G_{W,j}
\right)>0,
\tag{T-18505.5}
\]

although weaker positive schedules may suffice if their moat dominates the
remaining cross and assembly losses.

## Exact remaining theorem

The finite transfer is complete. What remains is to prove, rather than infer
from a finite ladder, that:

1. source-canonical direct certificates pass on an unbounded support schedule;
2. their lower moats satisfy a rate sufficient for the global three-block
   assembly; and
3. the chosen finite source-canonical packets exhaust the actual complete
   dangerous hierarchy.

No finite collection of passing levels proves these three asymptotic
statements.
