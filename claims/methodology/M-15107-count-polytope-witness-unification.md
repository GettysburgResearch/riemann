# M-15107 — One source-bound count polytope for radial, portfolio, and shifted-support witnesses

Methodology ID: `M-15107`  
Status: **PROPOSED PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: the reviewed finite ideas in PRs #104, #109, #110, and #111  
Scope: integration and proof-producing architecture; no RH or counterexample claim

## 1. Proposed unification

Fix one source-bound ordered atom partition and one exact family of interval-count equations. Write

\[
 \mathcal P(m)=\{x\in\mathbf R_{\ge0}^{J}:Ax=m\}.
\]

Here `x_j` is the multiplicity in atom `j`, `A` is the consecutive-interval incidence matrix, and `m` is the vector of exact window counts.

The following constructions are instances of the same finite optimization problem with different nonnegative cost vectors:

1. the pointwise radial/count envelope of PR #104;
2. the witness-adapted two-point dual of PR #109;
3. the logarithmic portfolio dual of PR #111;
4. the count-only support-gap response of PR #110 after expressing its inside-gap floor atomwise.

For a witness response with certified atom lower costs `c_j`, the sharp subtraction supplied by the frozen count table is

\[
 \boxed{
 \inf_{x\in\mathcal P(m)} c^Tx
 =\sup_{\lambda:A^T\lambda\le c}m^T\lambda.}
\]

A single count artifact can therefore be reused. Each new witness should emit only:

- its exact atom-cost vector;
- one rational primal feasible point;
- one rational unrestricted dual feasible point;
- exact objective equality, when optimality is claimed.

The source table, atom order, incidence matrix, endpoint convention, and count proof hashes should not be rebuilt separately by each consumer.

## 2. Why this is more than code deduplication

A pointwise radial profile minimizes a restricted family of cumulative costs one radius at a time. A witness-adapted dual minimizes the complete response cost while preserving correlations among overlapping count windows. Both are projections of the same integral polytope.

This viewpoint explains why the witness-adapted subtraction may strictly exceed the integral of the pointwise profile without contradiction: pointwise minima at different radii may be attained by different feasible count vectors, whereas one witness dual uses a single feasible count vector across all atoms.

It also gives one semantic trust boundary. A malformed atom ordering, overlapping atoms, endpoint ambiguity, or inconsistent count digest is then rejected once before any analytic witness is evaluated.

## 3. Shifted-support portfolios

The three-node support-gap chord can be written as a zero-sum log portfolio. For

\[
 0<u_0<u_1<u_2,
 \qquad A>0,
\]

put

\[
 L_1=\log\frac{u_1+A}{u_0+A},
 \qquad
 L_2=\log\frac{u_2+A}{u_0+A},
\]

and

\[
 \beta=(L_2-L_1,-L_2,L_1).
\]

Then `sum beta_i=0`, the response vanishes at `y=A`, and the support-gap theorem asserts its nonnegativity for `y>=A`.

This suggests a shifted extension of the PR #111 response certificate: set `z=y-A` and certify the negative-derivative numerator as nonnegative on `z>=0`, using exact monomial, Bernstein, or sum-of-squares data. Such a shifted cone would contain the support-gap chord while remaining compatible with the same count-polytope dual.

This extension is **not proved here**.

## 4. Suggested source schema

A reusable source artifact should contain:

```text
schema
normalization_id
ordinate / count center
atom endpoints in strict order
endpoint convention and zero-free gates
incidence matrix A
exact count vector m
primitive/count artifact SHA-256 bindings
integrality/TU declaration
```

Every consumer should bind the source artifact by content hash and report:

```text
witness kind
atom cost lower intervals
primal counts
unrestricted dual multipliers
primal/dual objective
residual interval
finite verdict
```

## 5. Connection to saturated sign chains

A saturated sign chain supplies disjoint simple critical-line bins whose union exhausts a counted slab. The same bins can be transformed once into:

- selected factors for exact factor removal;
- atom boundaries for count-polytope consumers;
- a complete-support gate for support-gap witnesses.

This avoids maintaining incompatible zero-bin formats across the selected-factor, count-dual, and support-gap branches.

## 6. Proof boundary

This note is a proposed integration theorem and schema, not a reviewed strengthening of any frozen PR.

It does not:

- repair PR #111's overlapping-atom or source-binding defects;
- verify PR #112's reliance on `L-9309`;
- prove that any finite witness is negative;
- turn finite nonnegative tables into RH;
- replace independent reproduction of direct-`xi` or total-count primitives.

Any implementation or shifted-support theorem derived from this note must be reviewed separately before it changes a PR classification.
