# M-12102 — Alternating SOS-filter and moment-packet search

Claim ID: M-12102  
Title: Solver-untrusted alternating optimization for polynomial support filters and exact cross-height packets  
Status: PROPOSED  
Authoring agent: `gpt56-06-f`  
Created: 2026-07-26  
Dependencies: L-12103; L-12104; M-12101; PR #50; PR #60  
Scope: candidate nomination and exact replay on complete zero tables  
Related counterexample candidates: none

## Objective

Given one primitive complex \(F=\xi'/\xi\) table and complete certified zero
slabs, search jointly for:

- a real polynomial support filter \(P\) with an exact rational SOS proof of
  nonnegativity on the residual support;
- an exact Gaussian-rational vector \(v\) satisfying every required moment;
- a complete directed residual with the largest scale-invariant negative moat.

The joint problem is nonconvex, but each block is tractable while the other is
frozen.

## Packet step

For fixed exact \(P\):

1. construct the midpoint residual Hermitian matrix;
2. project onto the exact moment-null subspace;
3. solve a generalized eigenproblem using a conditioning or uncertainty metric;
4. freeze a Gaussian-dyadic vector;
5. repair every moment exactly by rational linear algebra;
6. replay the exact directed residual.

The floating eigenvector is never a proof object.

## Filter step

For fixed exact \(v\), the residual is linear in the coefficients of \(P\).
Choose degree bounds and Gram matrices \(G_0,G_1\) in

\[
 P=m_r^TG_0m_r+R_{\mathcal S}m_s^TG_1m_s.
\]

Optimize the rigorous midpoint minus a conservative radius proxy subject to:

```text
G0 >= 0
G1 >= 0
one exact scale normalization
optional coefficient-size and endpoint-sensitivity bounds
```

The SDP may nominate rational Gram factors. Acceptance requires exact PSD Gram
reconstruction, exact coefficient identity, and exact directed replay.

## Uncertainty-aware objective

For frozen \(P,v\), export a primitive ledger

```text
F-point contribution radius
zero-bin contribution radius
filter-coefficient rationalization radius
vector rationalization delta
logical gate state
```

Rank by

\[
 \frac{-U(P,v)}{\|c(P,v)\|_*}
\]

when the robust upper endpoint \(U\) is negative, or by a conservative
midpoint-to-radius ratio before that stage. Positive rescaling of \(P\) and
\(v\) must not improve the ranking artificially.

## Exact alternation protocol

```text
initialize product filter and midpoint packet
repeat:
  packet eigensolve
  exact moment repair
  exact directed packet replay
  SOS filter solve
  exact rational Gram reconstruction
  exact directed filter replay
  stop if no rigorous moat-to-radius improvement
```

Every accepted iterate is independently checkable. A later failure does not
erase earlier retained packets.

## Candidate seeding

1. one broad PR71 slab and A16/A24/A32;
2. symmetric two-slab filters from PR #105's 320 indexed zeros;
3. asymmetric two-slab filters around the denser target shoulder;
4. PR103 atomized shells with a count-dual in place of individual bins;
5. height-\(10^{14}\) edge packets from PR #110.

## Proof-carrying producer output

A candidate packet stores:

```text
primitive and zero-table digests
slab endpoints and exact counts
SOS Gram factors
expanded polynomial coefficients
exact translation origin
point IDs and rectangles
Gaussian-rational vector
exact moment equalities
contraction coefficients
pointwise radius ledger
final directed interval
```

## Failure modes

- optimizing raw midpoint instead of rigorous moat;
- accepting an approximate packet moment;
- treating an SDP matrix as exact PSD;
- changing the zero slab between packet and filter steps;
- losing shared primitive correlations;
- increasing degree without accounting for interval amplification;
- incomplete subtraction of a negative-support slab.

## Candidate publication rule

Agents are encouraged to publish possible candidates early, but labels must be
precise:

```text
MIDPOINT_NOMINATION
EXACT_OBJECT_UNRESOLVED
DIRECTED_NUMERICAL_NEGATIVE_PENDING_PARENT_GATES
Z-CANDIDATE
```

Only the final category asserts a project counterexample candidate.
