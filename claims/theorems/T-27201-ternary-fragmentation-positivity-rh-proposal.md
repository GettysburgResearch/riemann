# T-27201 — Conditional ternary fragmentation implication; positivity refuted

Claim ID: `T-27201`  
Title: Ternary Fragmentation Positivity would imply RH, but the positivity hypothesis is false  
Status: **CONDITIONAL IMPLICATION RETAINED; PROPOSED CLOSING HYPOTHESIS REFUTED BY `R-27201`**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-27201`, `L-27202`, `R-27201`, `T-26202`, `L-23808`, `L-23809`

## 1. Conditional implication

For the logarithmic target

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

let `A_X(n)` be the deterministic ternary coefficients of `L-27201`. If

\[
A_X(n)\ge0\qquad(2\le n\le X)
\tag{T-27201.1}
\]

held cofinally, then the flow

\[
d_{n,j}=A_X(n)\mathbf1_{j=\lceil n/3\rceil}
\]

would be a nonnegative, uniformly balanced, zero-slack MFT certificate. The
atomized carry/entropy theorem would give

\[
\sum_{p^a\le X}\frac{\Lambda(p^a)}{\sqrt{p^a}}
\log(X/p^a)
\ge4\sqrt X-O(\log^2X),
\]

and the reviewed square-screw/Landau transfer would imply RH.

This conditional chain remains correct.

## 2. Refuted hypothesis

`R-27201` proves

\[
A_{10^7}(63)<0.
\]

Therefore (T-27201.1) is false and this theorem is not an unconditional RH
proposal.

## 3. Surviving use

The ternary flow remains an exact signed equality solution and a useful base
point for the full fragmentation cone. Any corrected MFT construction may add
Pascal four-cycles or additional balanced split channels while preserving:

- the node divergence;
- every carry column;
- the complete logarithmic binomial objective.

The exact surviving theorem is now:

```text
nonnegative Pascal-cycle repair of the signed ternary flow
=> MFT
=> sharp prime ramp
=> RH.
```

Existence of such a cofinal repair remains open.
