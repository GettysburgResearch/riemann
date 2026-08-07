# D-24901 — Reflected boundary-charge certificate

Claim ID: `D-24901`  
Title: A fail-closed source-specific certificate for converting the reflected top Möbius corner into a strict lower-scale recurrence  
Status: **PROPOSED EXACT DEFINITION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #249  
Frozen base: PR #236 at `1c9a749a1648c4772509eb3b056598c7044f4393`  
Scope: finite certificate interface for one order `K` and one logarithmic block; no claim that certificates exist for an unbounded sequence

## 1. Source and energy

Fix an integer `K>=4`, a logarithmic block `J`, and

\[
X=e^{J+O_K(1)},\qquad V=\lceil X^{1/K}\rceil.
\]

Use a compact safe window

\[
W_K=W_{m_K,R_K},\qquad R_K=K^3,
\]

from `L-15160`, with enough half-pole moments to annihilate every declared
polynomial source term. Let

\[
h_{K,J}\in\mathcal H_{K,J}
\]

be the **complete signed top-top reflected source vector** obtained after:

1. expanding the finite Möbius resolvent on both reflected sides;
2. recombining all rows with their exact Möbius/residual signs;
3. removing only rows certified by `L-24901` to be Euler-small;
4. retaining every cutoff, support, and first-crossing contribution.

Its physical block energy is

\[
E_K(J)=\|h_{K,J}\|_{\mathcal H_{K,J}}^2.
\tag{D-24901.1}
\]

The Hilbert space and Gram must be source-bound. An arbitrary-vector Farey or
cluster operator is not an admissible substitute.

## 2. Certificate data

An `RBC(K,J)` proof object contains the following exact data.

### A. Source manifest

A duplicate-free finite tuple manifest with:

```text
source tuple ID
reflected side and residual depth
all truncated and unrestricted coordinates
exact Möbius/residual/binomial coefficient
normalization and window hash
output and ratio-support cells
```

The manifest must reconstruct the complete source coefficientwise on the active
block.

### B. Oriented incidence ledger

Every partition-created internal face is listed twice, with identical source
content and opposite induced orientation. The checker contracts these pairs
before any absolute value or norm.

### C. Euler ledger

Every row declared Euler-small identifies:

```text
selected unrestricted coordinate
frozen complementary product
residual-support lower cutoff
active lattice interval
moment order and Euler order
endpoint regularity
explicit exponent bound
```

The selected active lattice must be complete. A coordinate cut by an undeclared
residual or first-crossing boundary is rejected.

### D. Lower-scale routes

Every nonboundary surviving row has an explicit source map

\[
T_\gamma:\mathcal H_{K,J}\longrightarrow
\mathcal H_{K,u_\gamma},
\qquad
u_\gamma\le(1-\delta)J+C_K,
\tag{D-24901.2}
\]

for one fixed `delta>0`. The route is an actual identity or a certified operator
inequality on the represented source span. Merely assigning a balanced label is
not a route.

### E. Boundary-charge rows

Every remaining row is represented as a sum over `q_gamma` **paid truncated
coordinates**,

\[
b_\gamma
=\sum_{\mathbf a\in[1,V]^{q_\gamma}}
 c_\gamma(\mathbf a)\,g_{\gamma,\mathbf a},
\tag{D-24901.3}
\]

where all uncharged coordinates remain inside a positive reflected Gram or an
explicit lower-scale source. The normalized coefficient ledger must prove

\[
\sum_{\mathbf a}|c_\gamma(\mathbf a)|
\le V^{q_\gamma/2+o_K(J)}.
\tag{D-24901.4}
\]

The charge count is

\[
q_K=\max_\gamma q_\gamma.
\tag{D-24901.5}
\]

Counting the number of faces is irrelevant. What matters is the maximum number
of coordinates simultaneously paid outside positive or lower-scale structure.

### F. Strict reflected reserve

The reflected identity must yield a genuine reserve

\[
\boxed{
\kappa_0 E_K(J)
\le
C_K\left(
1+E_K^{\rm low}(J)+\sum_\gamma\|b_\gamma\|^2
\right)
+e^{-c_KJ},}
\tag{D-24901.6}
\]

where

\[
\kappa_0>0
\]

is independent of `J` and bounded away from zero along the proposed unbounded
sequence of `K`, and

\[
E_K^{\rm low}(J)
\le
\max_\upsilon\max_{u\le(1-\delta)J+C_K}E_{K,\upsilon}(u).
\tag{D-24901.7}
\]

The right side may not contain an undeclared same-scale copy of `E_K(J)`.

Equation (D-24901.6) is the load-bearing reserve. The identity

\[
2E_K=2E_K+0
\]

is not a certificate.

### G. Scalar firewall

The proof object exports one exact map to a fixed-ratio Möbius shell, for
example

\[
Q_{1/2}(t)=e^{-t/2}\left[M(e^t)-M(e^t/2)\right],
\tag{D-24901.8}
\]

or to the `2/3` first Farey cell. The causal shell transfer of `L-23008` may be
used after one shell is controlled. Increasing the packet order is not itself a
fixed-ratio difference operator.

## 3. The `RBC(K)` assertion

`RBC(K)` means that there are constants

\[
\delta>0,\qquad \kappa_0>0,\qquad C_{\rm ref}<\infty
\]

independent of `J`, with `delta` and `kappa_0` uniform along the proposed order
sequence, such that an `RBC(K,J)` proof object exists for every sufficiently
large block and

\[
q_K\le C_{\rm ref}.
\tag{D-24901.9}
\]

The certificate is source-specific and proof-producing. It is stronger than a
face-count slogan and weaker than a uniform theorem for arbitrary coefficient
vectors.

## 4. Automatic rejection conditions

A checker rejects a purported certificate if any of the following occurs:

- a balanced row is removed only by citing the abstract induction of
  `L-23203`;
- total variation is taken before signed sibling recombination;
- an internal face occurs once, or twice with the same orientation;
- an Euler coordinate has a live undeclared cutoff inside its active window;
- a lower-scale destination exceeds `(1-delta)J+C_K`;
- the reserve has `kappa_0<=0` or hides a same-scale target on the right;
- a charge row pays an unlisted coordinate or understates its normalized
  coefficient mass;
- the scalar shell/Farey projection is missing;
- finitely many orders are promoted to RH.

## 5. Proof boundary

This definition makes `RBC(K)` finite and falsifiable. The abstract implication
from such certificates to RH is proved in `T-24901`. Construction of the strict
reserve and charge map for the actual top-top Möbius source remains the central
arithmetic theorem of the proposal.
