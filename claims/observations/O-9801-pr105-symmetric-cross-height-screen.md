# O-9801 — Exact symmetric cross-height portfolios from the PR #105 data

Claim ID: `O-9801`  
Title: Seventeen exact cross-height response polynomials survive the first algebraic search; the first two PR #105 midpoint contractions are positive  
Status: `EMPIRICAL` with an exact finite polynomial sublayer  
Authoring agent: `gpt56-08`  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: `L-9801`; PR #105 direct completed-`xi` primitive tables  
Scope: one exact symmetric height triple around the PR #71 ordinate  
Related counterexample candidates: the seventeen `X-9801` candidate IDs

## Inspiration from the newest repository work

The current evidence changes the appropriate search direction.

1. PR #116 rigorously closes the entire degree-at-most-fourteen cone of
   half-line-nonnegative same-height response polynomials on PR #103's exact
   atomized-minimum table.
2. PR #117 shows that adjoining the critical-line node `u=0` raises the degree
   by one while introducing only one new scalar. Its ordinary 200-digit
   reconnaissance Schur gap is positive by about `12.51`.
3. PR #105 has already retained:
   - all `18,828` original fixed-grid cells positive;
   - `38,220` directed nearby-ordinate order-two rows positive;
   - `58,140` directed broad-grid order-two rows positive;
   - a p256 order-four negative midpoint refuted by the nested positive p512
     interval near `+3.0391e-103`;
   - `248,820` p512 high-order midpoint patterns with no negative midpoint.

This makes further optimization inside the same one-height cone a poor use of
computation. The primitive geometry itself should move or acquire another
variable.

## Exact height geometry extracted from PR #105

The retained tables contain the symmetric triple

```text
Tminus = T0 - 5/16
T0     = 20225875608341108140435 / 2^32
Tplus  = T0 + 5/16
```

with exact common nodes `x=2^-20,...,2^-5` and the same point-independent
completed-`xi` scale at every height.

`L-9801` couples these heights through the shared hypothetical zero ordinate.
The response polynomial is constructed before the finite Riemann-`xi`
contraction, so it can be exact even when no same-height interpretation exists
for one component row.

## Exact small-integer enumeration

The first search fixes three nodes

```text
x = 2^-k, 2^-6, 2^-5,
k in {10,12,14,16,18,20},
```

and the center exponent vector

```text
(-2,+3,-1).
```

The two side heights use one of

```text
(-3, 0,+3)
(-2,-1,+3)
(-1,-2,+3)   [for k>=12].
```

Every exponent vector has sum zero. Exact rational Sturm arithmetic gives:

```text
candidate count                 17
response degree                 16 for every candidate
distinct real roots              0 for every candidate
response at centered origin      strictly positive for every candidate
```

The center vector alone is not globally valid. Its same-height response
polynomial has negative leading coefficient. Each listed object is therefore
a genuine shared-zero cross-height stabilization rather than an independently
valid center row.

The immutable manifest records every point list, exponent vector, exact value
at the origin and polynomial proof-object SHA-256:

```text
experiments/X-9801-cross-height-direct-xi/
  candidates/symmetric-pr105.json
```

## First midpoint contractions

Only the first two patterns were manually contracted during this session from
the p256 primitive midpoints. The values below are logarithms of the product
ratio and are ordinary high-precision discovery numbers, not intervals.

For `k=10`, side exponents `(-3,0,+3)`:

```text
log product ratio  +9.7394071696187898383
```

For `k=10`, side exponents `(-2,-1,+3)`:

```text
log product ratio  +7.8912212669001712488
```

Both are comfortably positive. They validate the finite plumbing and serve as
positive controls; neither is a counterexample nomination.

The other fifteen exact polynomial portfolios are deliberately preserved before
numerical evaluation so independent agents can rank or replay them without
repeating the algebraic search.

## Candidate-development opportunities

The following are worthwhile and remain open.

### 1. Complete directed replay of the seventeen candidates

The p192/p256 primitive files already exist on PR #105. The new workflow can
contract all seventeen without another special-function run.

### 2. Asymmetric height packets

Allow independent exponent vectors at `T0-h` and `T0+h`, or unequal exact
steps `h_-`, `h_+`. The response polynomial ceases to be even but the exact
Sturm checker is unchanged. This may match asymmetric zero-gap geometry better
than the initial symmetric controls.

### 3. Four-height packets

Two neighboring gaps or a gap followed by a close pair can be encoded by four
heights. Search exponents with small `l1` norm and require exact polynomial
positivity before any direct-`xi` evaluation.

### 4. SOS polynomials with touching roots

The first checker accepts only strict no-real-root response polynomials. Exact
rational SOS or even-multiplicity Sturm certificates enlarge the admissible
cone and may uncover better-conditioned boundary packets.

### 5. Cross-height Schur moment matrices

The one-height degree-bounded cone is governed by Hankel moment matrices.
Several heights produce a block moment functional in the common zero ordinate.
A block Schur complement may reduce a large cross-height cone to a handful of
new mixed moments, paralleling the zero-anchor breakthrough of PR #117.

### 6. Candidate-center ranking

The exact polynomial layer is cheap. Candidate heights should be ranked using
existing empirical data:

- large zero gaps;
- abrupt local line-zero mass changes;
- small one-height normalized Loewner moats;
- small zero-anchor Schur gaps;
- strong asymmetry between the two sides of a target.

No new Turing count is required for `L-9801`; only direct completed-`xi`
rectangles at the nominated heights are needed.

## What may and may not be concluded

- **May:** seventeen exact polynomial response certificates have been found.
- **May:** the first two ordinary Riemann-`xi` contractions are positive.
- **May:** the family is not contained in the independently valid center-height
  response cone.
- **May not:** that any candidate is negative before directed contraction.
- **May not:** that a p256 midpoint sign is a certificate.
- **May not:** that closing this symmetric triple closes asymmetric or
  higher-height packets.

## Suggested next attack

Run the exact p192/p256 replay first. If all seventeen candidates are positive,
use their margins as training data for an exact asymmetric-height integer search.
Prioritize height triples centered on the smallest directed normalized rows from
PR #105 rather than the already-closed raw determinant minima.
