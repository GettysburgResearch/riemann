# M-23601 — Adversarial review protocol for the reflected Brion--Möbius proposal

Claim ID: `M-23601`  
Title: Freeze, emit, and falsify the complete balanced threshold-polytope grammar before accepting the full RH proposal  
Status: **PROPOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-final-02`  
Created: 2026-08-07  
Dependencies: `L-23601`--`L-23604`, `T-23601`  
Scope: source completeness, polyhedral geometry, algebraic cancellation, and final scalar mutation

## 1. Review principle

Do not begin by estimating the final recurrence.  First decide whether the
source grammar actually has the two properties claimed in `T-23601`:

```text
BRANK: bounded rank of genuinely global constraints;
BLINE: complete line/toggle and cone-denominator matching.
```

Every accepted object must be emitted by a producer and reconstructed by an
independent consumer.  Human prose saying that a row is “similar,” “terminal,”
“lower order,” or “a null companion” is not evidence.

## 2. Frozen dependencies

At the start of review, record the exact current heads of:

```text
PR #158  high-order safe window, Euler and source grammar
PR #165  corrected analytic/Farey and Type-I path
PR #226  reflected Selberg identity
PR #229  first-cell Mertens decoder
PR #233  finite resolvent and corrected BTP interface
PR #234  fixed-ratio shell and terminal-only refutation
PR #235  full-tuple terminal partition
PR #236  this proposal
```

No mutable-head theorem may silently replace the frozen dependency during the
review.

## 3. Required production manifests

Produce complete manifests for `K=6` and `K=8`, plus a symbolic grammar for
arbitrary `K`.  Each source row must expose:

```text
unique source ID;
Heath--Brown or Möbius-resolvent parent;
all ordered residual factors;
all actual Möbius/divisor/binomial signs;
left/right reflected identity indices;
product and ratio supports;
first-crossing index and reserve;
cutoff and transition conventions;
destination type and complexity rank;
null companions;
prime-power/pole/archimedean provenance.
```

The consumer must prove completeness by recombining the manifest back to the
parent coefficient identity on an exhaustive small endpoint.

## 4. Prefix-coordinate audit

For every cell:

1. construct the triangular cumulative-prefix matrix;
2. transform every inequality exactly;
3. label each transformed row as:
   - coordinate lower/upper bound;
   - order/prefix bound;
   - global product row;
   - reflected-product row;
   - factor-ratio row;
   - orientation row;
   - shell/auxiliary row;
   - unclassified;
4. reject any unclassified row;
5. row-reduce all non-coordinate rows over exact rationals or formal integer
   coefficients;
6. require rank at most ten.

Record both the raw number of rows and the reduced rank.  A large row count is
allowed; rank growth is not.

## 5. Polyhedral face audit

For each exact cell polytope:

1. enumerate all vertices and active constraint sets for `K=6,8`;
2. enumerate positive-dimensional faces or their tangent-lineality bases;
3. construct a lexicographic simplicial refinement of every degenerate vertex;
4. bind each cone edge to its source coordinate or global row;
5. preserve open/closed boundary conventions through the complete valuation.

The review must include deliberately `Omega(K)`-dimensional faces.  Their mere
existence does not reject the proposal; they must be shown to have zero
valuation by `BLINE`.

## 6. Line/toggle matching audit

For every nonvertex tangent cone, emit:

```text
one explicit lineality vector;
its coordinate/prefix interpretation;
the exact pair or family of source rows producing the Möbius toggle;
the numerator factor 1-exp(-<z,v>);
the null-moment or total-product identity used;
and the signed destination recombination digest.
```

Reject if the match uses:

- a row not present in the manifest;
- an assumed sibling across a cutoff;
- a sign changed after recombination;
- a null companion imported from an unproved family;
- a terminal-only row to cancel a balanced line.

## 7. Vertex denominator audit

For every vertex cone:

1. construct the exact geometric denominator list;
2. construct the complete signed numerator before cancellation;
3. perform exact polynomial/divisibility checks;
4. record each canceled denominator and its source toggle;
5. count the unmatched factors;
6. require the count to be at most ten.

No numerical near-zero evaluation counts as divisibility.  Cancellation must be
symbolic or exact in the group algebra of translations.

## 8. Scale and positivity audit

Every localized vertex must receive exactly one label:

```text
STRICT_LOWER_SCALE
EULER_SMALL
REFLECTED_NONNEGATIVE_DIAGONAL
SAME_SCALE_ENDPOINT
```

For `STRICT_LOWER_SCALE`, verify the exact bound

\[
 u\le(1-\delta)J+C_K.
\]

For `EULER_SMALL`, verify that the lattice variable is complete on the active
cell and that the declared Euler order exceeds the critical threshold.

For the reflected diagonal, reconstruct `L-9516` from the three Selberg
coefficient packets and verify the sign after every normalization adapter.

For same-scale endpoints, verify that only unmatched cone denominators incur
`V`-cost and that all fixed-`K` multiplicities are `exp(o_K(J))`.

## 9. First-cell mutation

Export the exact first critical cell from the **complete balanced source** and
verify

\[
 B_{D,1}
 =\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
  [M(D)-M(\lfloor2D/3\rfloor)].
\]

Required controls:

```text
noncoprime q=v=5,r=5 chain;
correct lattice step (q/g,v/g);
odd--odd cotangent residue;
all reduced-frequency multiplicities;
exact geometric-difference floors;
exact cell-to-energy adapter.
```

Run the full localization after projecting to this cell and require the bound in
`L-23604`.  This is the strongest check that signed Möbius coherence has not
been lost.

## 10. Mandatory mutations

The verifier suite must reject each of the following independently:

1. delete one balanced source tuple;
2. replace every Möbius sign by its absolute value;
3. reverse one reflected factor orientation;
4. omit one cutoff transition row;
5. classify a balanced row using the withdrawn old `L-23203` step;
6. delete one numerator factor at a vertex;
7. add an eleventh independent global constraint;
8. send one strict destination above the reserve;
9. delete the first-cell decoder;
10. use the old determinant spacing in a noncoprime chain;
11. drop the odd--odd residue;
12. estimate the three Selberg packets separately before forming the Hermitian
    square.

A correct fail-closed consumer reports the first broken invariant and never
continues to the RH verdict.

## 11. Suggested finite checker schema

A compact JSON proof object should contain:

```text
frozen_heads
source_manifest
cell_constraints
prefix_transform
global_rank_certificate
face_lineality
line_toggle_matches
vertex_cones
numerator_factorizations
scale_labels
reflected_diagonal_certificate
first_cell_projection
recurrence_constants
mutation_results
```

The independent checker need not recompute large prime sums.  It checks the
finite symbolic source grammar and exact identities.  Numerical or interval
producers remain responsible for source coefficients imported from analytic
normalizations.

## 12. Verdicts

Use only:

```text
VERIFIED_BRION_BALANCED_SCHEMA
VERIFIED_WITH_EXPLICIT_FIXES
GAP_AT_SOURCE_COMPLETENESS
GAP_AT_GLOBAL_RANK
GAP_AT_LINE_MATCHING
GAP_AT_VERTEX_DIVISIBILITY
GAP_AT_SCALE_ROUTING
GAP_AT_FIRST_CELL
REJECTED
```

Do not call the proposal a proof of RH unless every schema gate passes and all
imported analytic dependencies have independently passed at their frozen
heads.

## 13. Binary review value

The proposal is designed to be decisively reviewable.

One unmatched positive-dimensional balanced face, one rank growing with `K`, or
one vertex with `Omega(K)` uncancelled denominators rejects the proposed
closure.  Conversely, complete source manifests plus the symbolic-`K` rank and
divisibility induction reduce the remaining argument to the exact scale and
Mertens compositions in `L-23604/T-23601`.