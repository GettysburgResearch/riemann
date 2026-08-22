# R-105200 — High-derivative residue coherence does not descend to Xi for free

Claim ID: `R-105200`  
Status: **BINDING SCOPE FIREWALL**  
Created: 2026-08-23  
Depends on: `L-105200--L-105203`; PRs #716, #720  
RH status: **unproved**

The natural-scale theorems prove that the Xi derivative tail is asymptotically
Gaussian, real-rooted and residue-coherent. None of the following promotions is
valid without a new theorem.

## 1. Tail coherence is not fixed-order coherence

`L-105202` takes `M->infinity` and is uniform for `m>=M`. It does not imply
anything about a fixed derivative order `m` as the height tends to infinity.
The quantifiers cannot be exchanged:

```text
for every high lower cutoff M, all m>=M are coherent in a growing box
```

is not

```text
for every fixed m, residues are coherent at all heights.
```

The latter would already contain an RH-strength input.

## 2. Real-rooted high entry does not remove wrong extrema below it

The exact reverse-Rolle conservation law is

\[
N_{\rm nr}(p)
=N_{\rm nr}(p^{(r)})+2\sum_{j<r}E(p^{(j)}).
\]

Even when the high derivative is completely real-rooted, every lower wrong
extremum still creates one nonreal conjugate pair. The high entry only removes
the terminal term; it does not control the sum.

## 3. A positive one-step transfer constant is insufficient

A bound

\[
\mathfrak C_j\ge {1+c\over2}
\]

at every step transfers real-zero proportions by a factor `c`, but iterating a
fixed `c<1` through `O(T^2 log T)` levels loses exponentially. The exact useful
quantity is the additive defect budget

\[
\sum_j R_j(1-\mathfrak C_j),
\]

not a fixed multiplicative proportion.

## 4. The polynomial moment ledgers are global

`L-104524` and `L-105100` are complete finite-polynomial identities. A
height-truncated Xi application requires exterior residues, canonical-product
passage and boundary terms. Neither identity may be inserted directly into
`CRDB105200` without a localization theorem.

## 5. Boundary winding remains load bearing

The complex transport contains

\[
\sum_j(B_j+W_j-1).
\]

Residue coherence controls wrong extrema only. It does not sign, suppress or
remove the Levinson/Hermite--Biehler boundary flux. Any proof that drops this
term is invalid.

```text
natural-scale high entry                 PROPOSED COMPLETE
high-tail RCMV                           PROPOSED COMPLETE
fixed low-order RCMV                     UNPROVED
cumulative coherence defect              UNPROVED
boundary/winding budget                  UNPROVED
Riemann Hypothesis                       UNPROVED
```
