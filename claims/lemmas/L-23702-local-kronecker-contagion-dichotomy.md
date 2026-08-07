# L-23702 — Local Kronecker contagion dichotomy for the actual balanced packet

Claim ID: `L-23702`  
Title: A large local restriction of a fully recombined balanced Bohr packet must propagate to an exact collision, an Euler-eligible lattice face, a strict lower scale, or a bounded-rank resonance face  
Status: **FULL-PROPOSAL HINGE — `BCT(K)` OPEN PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #237  
Dependencies: `L-23701`; direct full-tuple partition on PR #235; high-order Euler closure on PRs #158/#233; reflected identity on PR #226  
Literature context: Matomäki–Radziwiłł–Shao–Tao–Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Invent. Math. 244 (2026), especially its type-II contagion/scaling mechanism.  The theorem below is deterministic and stronger; it is not quoted from that paper.

## 1. Why a new inverse theorem is needed

The full-torus identity

\[
 \|\mathcal D\|_{L^2(\mathbb T^{P_J})}^2=\sum_n|a(n)|^2
\]

is elementary.  RH requires control of the same polynomial on the exceptional
one-parameter orbit

\[
 p\mapsto p^{-it}.
\]

A generic restriction theorem is false: the first critical Farey cell is a
fixed-ratio Mertens increment, and arbitrary cluster matrices have rows of norm
`gg sqrt(D)`.  The theorem must use the actual signed packet and its exact
factorization history.

## 2. Logarithmic factor cells

Fix order `K` and a fully recombined balanced type `tau`.  Retain the exact tuple
manifest before projecting to the product `n`.  Partition every active factor
coordinate into multiplicative cells

\[
 e^{rJ/K}\le v<e^{(r+1)J/K}
 \tag{L-23702.1}
\]

with the fixed support slack recorded separately.  A **face** is obtained by
fixing a subset of cell indices, endpoint equalities, truncation states, and
product relations in this manifest.

The rank of a face is the number of factor-cell coordinates that remain free
after:

1. exact product equalities;
2. the output-product constraint;
3. every divisor relation already present in the tuple manifest;
4. every source recombination identity;
5. every fixed endpoint or cutoff equality.

This is a combinatorial rank in the actual source dictionary, not the number of
variables in an arbitrary parametrization.

## 3. Four admissible outcomes

`BCT(K)` asserts that the complete local Hermitian packet can be partitioned,
before any absolute value, into finitely many source-bound pieces of the
following four classes.

### 3.1 Exact collision

The two reflected monomials have the same integer product.  All tuple
coefficients at that product are recombined first.  The resulting contribution
is the exact Bohr diagonal or a declared zero coefficient.

### 3.2 Euler-eligible free-lattice face

After freezing a small complementary product, one unrestricted positive-integer
variable remains on a complete active lattice.  High-order half-pole moments
annihilate its continuous main term, and the periodic-Bernoulli remainder is
exponentially small by the reviewed terminal Euler mechanism.

### 3.3 Strict lower-scale face

The complete source contraction is identified with an auxiliary packet at
logarithmic scale at most

\[
 (1-\delta)J+O_K(1),
 \qquad \delta>0
 \tag{L-23702.2}
\]

with every cutoff and transition source retained.

### 3.4 Bounded-rank resonance face

The face remains genuinely balanced and same-scale, but its source rank is at
most

\[
 \boxed{C_0}
 \tag{L-23702.3}
\]

for one absolute constant independent of `K`, `J`, and the packet type.
Every free coordinate ranges over at most

\[
 \exp\{J/K+o_K(J)\}
 \tag{L-23702.4}
\]

source values.  Its complete source contraction is bounded by a declared
lower-scale energy after paying the finite enumeration factor

\[
 \exp\{(C_0/K+o_K(1))J\}.
 \tag{L-23702.5}
\]

## 4. The contagion assertion

The load-bearing assertion is that a same-scale face of rank larger than `C_0`
cannot remain isolated.  The factor equations and the prime Kronecker phases
force the same approximate multiplicative relation on a positive-dimensional
family of neighboring factor cells.  Iterating the relation has one of three
outcomes:

1. it becomes an exact integer-product identity and enters 3.1;
2. one coordinate acquires a complete lattice range and enters 3.2;
3. the product scale drops and enters 3.3.

The iteration is called **contagion**.  Its certificate must contain the actual
integer relation, every scaled cell, and the terminal outcome.  An appeal to
“almost all intervals” without this deterministic propagation is invalid.

## 5. Proposed proof mechanism

The intended proof has four source-specific stages.

1. **Hermitian inverse step.**  Use the reflected Selberg identity to replace an
   algebraic square by the actual ratio Gram of `L-23701`.
2. **Major/minor structural split.**  Apply the nilsequence contagion/scaling
   technology only to the exact divisor-bounded factor words.  Minor-arc pieces
   route to lower-scale normal energies; major-arc pieces expose a finite system
   of approximate logarithmic product relations.
3. **Arithmetic promotion.**  Because all phases are logarithms of integers and
   the cell widths are source bound, repeated approximate relations either
   promote to exact product relations or force a complete free-lattice
   coordinate.  Every promotion threshold is recorded with outward rational or
   directed bounds.
4. **Rank count.**  The remaining independent relations have rank at most a
   fixed `C_0`; otherwise contagion continues.  This is the only place an
   order-independent bound is claimed.

The 2026 higher-uniformity paper motivates stage 2 but does not establish stages
3–4 for this packet.  Those stages are new arithmetic content.

## 6. Fail-closed production object

For each balanced packet and block, a `BCT` object must contain:

```text
complete tuple and product-collision manifest
Bohr monomials and Kronecker phases
major/minor labels with hypotheses
all approximate integer relations
contagion parent/child cell graph
exact-collision promotions
Euler-eligible free-lattice records
strict lower-scale destinations
surviving resonance faces
rank computation for every face
absolute rank ceiling C0
source contractions and enumeration factors
first-cell/Mertens projection when available
```

The consumer rejects:

- a face whose rank exceeds `C_0`;
- a relation stated only in floating point;
- a use of arbitrary coefficients;
- deletion of an exact collision or boundary source;
- an Euler classification without a complete lattice variable;
- a lower-scale destination above the declared reserve;
- an almost-all theorem substituted for deterministic contagion;
- a finite list of orders presented as an all-order rank theorem.

## 7. Proof boundary

`BCT(K)` is not proved in this file.  The file makes the reflected endpoint idea
honest: endpoint rank is the **conclusion** of a source-specific contagion
argument, not an assumption that balanced packets have already disappeared.

A single family of surviving faces with rank `Omega(K)` rejects this proposal.
A verified absolute rank bound supplies the missing `C_0/K` exponent and closes
the balanced recurrence through `L-23703`.
