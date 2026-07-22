# T-0302 — Lagarias criterion

Claim ID: T-0302  
Title: Lagarias's elementary harmonic-number criterion for RH  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: external theorem of Lagarias (2002)  
Scope: imported equivalence; proof not reproduced here  
Related counterexample candidates: arithmetic inequality witnesses

## Statement

Let
\[
 H_n=\sum_{j=1}^n\frac1j.
\]
The Riemann hypothesis is equivalent to
\[
 \sigma(n)\le H_n+e^{H_n}\log H_n
 \qquad\text{for every integer }n\ge1,
\]
with equality only for `n=1`.

Thus any `n>=2` for which a rigorous certificate proves
\[
 \sigma(n)>H_n+e^{H_n}\log H_n
\]
is a finite disproof of RH.  For `n>=2`, equality would also contradict the
"equality only at `1`" clause.

## Source

Jeffrey C. Lagarias, *An Elementary Problem Equivalent to the Riemann
Hypothesis*, Amer. Math. Monthly 109 (2002), 534--543,
DOI 10.1080/00029890.2002.11919883; arXiv:math/0008177.

Inspection level: full author manuscript/HTML inspected, including the theorem
statement and relation to Robin's criterion.

## Motivation

This supplies an elementary independent check for any Robin candidate.  Both
criteria use exact `sigma(n)` but have different transcendental right sides,
which is useful for detecting implementation or normalization errors.

## Proof status

Imported theorem.  The published proof is not copied into this claim.  The
finite-witness implication is its direct contrapositive.

## Analytic/domain audit

- The domain includes `n=1`.
- `H_n>0`; for `n=1`, `log H_1=0`.
- All logarithms are natural.
- Exact rational `H_n` can be represented without rounding, though
  `e^{H_n}` and `log H_n` require rigorous enclosure.

## Dependency audit

The theorem depends on Robin's criterion and explicit estimates in Lagarias's
paper.  A repository-level proof would need to reconstruct those steps.

## Gap audit

- Some secondary sources print `<` instead of `<=`; use the primary statement
  and equality clause.
- A large integer makes exact `H_n` naively expensive; a certified analytic
  bound may replace explicit summation only with proof.
- One cannot infer a Robin violation from a Lagarias near miss or conversely
  without exact inequalities.

## Remaining uncertainty

No bibliographic uncertainty.  Independent proof reconstruction is pending.

## Suggested next attack

For any candidate from Issue #2, emit both Robin and Lagarias sign certificates
from independent code paths.
