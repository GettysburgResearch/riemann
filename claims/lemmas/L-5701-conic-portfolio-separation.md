# L-5701 — Robust conic portfolio separation

Claim ID: L-5701  
Title: A robustly negative exact dual portfolio separates every admitted realization from the RH-valid finite cone  
Status: PROPOSED  
Authoring agent: `gpt56-06-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-5701; D-4501; L-4502 for support-function certificates  
Scope: finite conic witness libraries with rigorous joint uncertainty  
Related counterexample candidates: none

## Statement

Let `C subset R^n` be nonempty. Suppose RH implies every member of a finite
library of affine rows is nonnegative:

\[
q_i(y)=b_i+a_i^{\mathsf T}y\ge0,
\qquad i=1,\ldots,m.
\]

Let `lambda in Q_+^m` be exact and define

\[
P_\lambda(y)=\sum_i\lambda_iq_i(y)
=\beta+c^{\mathsf T}y.
\]

If a finite exact certificate proves

\[
U=\sup_{y\in C}P_\lambda(y)<0,
\]

then every `y in C` violates at least one imported RH-valid row. Conditional on
the logical gates for those rows and on the proof that the exact primitive
feature vector belongs to `C`, RH is false.

More generally, the same conclusion holds when the portfolio includes exact
PSD Gram multipliers from D-5701.

### Independent interval features

If

\[
C=\{z+e:|e_j|\le r_j\},
\]

then

\[
U=
\beta+c^{\mathsf T}z+
\sum_j|c_j|r_j.
\]

The coefficients must be combined before this formula is applied.

### Correlated rational polytope

If

\[
y=z+Bu,
\qquad Gu\le h,
\]

and exact rational `v>=0` satisfies

\[
G^{\mathsf T}v=B^{\mathsf T}c,
\]

then

\[
U\le\beta+c^{\mathsf T}z+h^{\mathsf T}v.
\]

A strict negative right-hand side is an exact weak-duality portfolio
certificate. The optimizer that proposed `lambda` and `v` is not trusted.

## Motivation

A witness can survive because uncertainty is shared across rows. For example,

\[
q_1=-\frac25+u,
\qquad q_2=-\frac25-u,
\qquad |u|\le1.
\]

Each row separately has robust upper `3/5`, so neither is certifiable. The exact
nonnegative portfolio has

\[
q_1+q_2=-\frac45
\]

for every allowed `u`. Treating the two appearances of `u` as independent would
erase this certificate.

The same principle applies to several `xi'/xi` inequalities evaluated from one
Arb series, several matrix contractions sharing the same prime blocks, or
arithmetic inequalities sharing one enclosure of Euler's constant or one
recurrence state.

## Proof or construction

Under RH every `q_i(y)>=0`. Since every `lambda_i>=0`,
`P_lambda(y)>=0` for every RH-admissible feature vector. The certified robust
upper says `P_lambda(y)<0` for every `y in C`; therefore `C` and the finite
RH-admissible region are disjoint.

For an interval box, substitute `y=z+e` and maximize the linear functional
coordinatewise. For a rational polytope,

\[
c^{\mathsf T}Bu
=v^{\mathsf T}Gu
\le v^{\mathsf T}h
\]

by `v>=0` and `Gu<=h`. This proves the displayed upper bound by exact rational
arithmetic.

For PSD terms, use the Gram expansion in D-5701. Each frozen-vector quadratic
form is affine in the primitive features, so after exact contraction the same
support-function argument applies.

## Analytic domain audit

This is finite-dimensional affine and conic duality. All analytic and domain
claims belong to the imported rows and matrix cones. The lemma does not infer
that a numerical sample is exact or that a special-function enclosure is sound.

## Dependency audit

- D-5701 defines the finite RH-valid cone and exact dual portfolio.
- D-4501 supplies the exact feature object, declared uncertainty set, and strict
  disproof-region semantics.
- L-4502 supplies the one-score support-function and weak-duality machinery.
- L-5701 adds conic aggregation and shared-feature contraction before enclosure.

## Gap audit

- Independent row intervals may be much wider than the contracted portfolio and
  should not be used when primitive dependencies are known.
- A negative coefficient in `lambda` invalidates the RH implication.
- The polytope must be nonempty; include a feasible anchor or a separate proof.
- An LP or SDP optimum is not the certificate. Only exact rational replay is.
- A negative robust portfolio over a malformed row library is not evidence
  against RH; every logical gate remains explicit.

## Adversarial tests

1. Verify the shared-cancellation example exactly.
2. Split `u` into two independent features and require `NOT_CERTIFIED`.
3. Mutate one dual equality in the polytope certificate.
4. Widen one feature radius until the robust endpoint reaches zero.
5. Retain a negative midpoint but break one logical gate; require failure.
6. Compare rowwise interval aggregation against contract-before-enclose and
   confirm the latter is never wider for the same primitive box.

## Remaining uncertainty

No mathematical gap is known. The practical problem is choosing and
rationalizing a portfolio with a strong normalized repair moat while keeping the
primitive coefficient vector small enough for available ball radii.

## Suggested next attack

Modify the Issue #39 proof-grade producer to export one canonical feature table
and a row-coefficient table. Optimize portfolio weights against the actual Arb
radii, not midpoint values alone. Freeze rational weights and verify the exact
robust endpoint independently.
