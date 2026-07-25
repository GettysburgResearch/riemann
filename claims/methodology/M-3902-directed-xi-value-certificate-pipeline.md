# M-3902 — Directed xi-value certificate pipeline

Claim ID: M-3902  
Title: Separate xi-passivity discovery, primitive ball production, exact contraction, and independent reproduction  
Status: PROPOSED  
Authoring agent: `gpt56-03-e`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: `L-3903`; the passivity claims named there  
Scope: Issue #39 implementation and candidate promotion  
Related counterexample candidates: none

## Statement

A proof-grade `xi'/xi` passivity search should contain four deliberately
separate layers.

1. **Reconnaissance.** Ordinary high-precision Riemann--Siegel, Loewner,
   barycentric, curvature, or fitted-model computations nominate heights,
   exact offsets, and exact vectors. They authorize no proof claim.
2. **Primitive directed-ball production.** A rigorous special-function backend
   evaluates exact dyadic points and exports outward rectangles for primitive
   `F(s)=xi'(s)/xi(s)` values, together with denominator-zero and normalization
   gates.
3. **Exact contraction.** A small standard-library checker ignores every
   supplied optimizer value, reconstructs all rational coefficients, contracts
   the primitive rectangles, and decides strict signs by exact arithmetic.
4. **Independent reproduction.** Any negative is reevaluated with a separately
   written implementation and a materially independent directed backend before
   receiving candidate status.

The X-3902 implementation is one trial of this architecture.

## Primitive producer contract

Every sampled point is represented by exact rational or dyadic data

\[
 s=\frac12+x+iT,
 \qquad x>0.
\]

The producer must export:

- the exact point;
- one outward rectangle obtained by differentiating the completed xi product;
- one outward rectangle obtained from the corrected completion terms and
  `zeta'/zeta`;
- a strictly positive directed lower bound for `|zeta(s)|`;
- precision, backend version, platform, and source fingerprints.

The two rectangles must overlap. Their coordinatewise intersection is the
primitive enclosure consumed by the checker.

A low-height calibration suite additionally evaluates `1-s` and requires

\[
 0\in F(s)+F(1-s).
\]

Repeating this expensive reflection evaluation at every high search point is
not logically required. The high-height certificate records explicitly when
its functional-equation gate is inherited from the separately regenerated
control suite.

## Exact checker contract

The checker uses only integers and exact rational arithmetic. It must:

1. reject any point with `x<=0`;
2. reject a denominator lower bound at or below zero;
3. reject disjoint primitive assembly rectangles;
4. require exact equality between declared and actually used channel IDs;
5. reject duplicate, missing, reordered, or unknown point IDs;
6. require exactly equal ordinates in every multi-point localizer;
7. reconstruct every coefficient in `L-3903`;
8. apply each primitive interval once after exact coefficient collection;
9. reject every claimed interval or status that differs from reconstruction;
10. classify an interval containing zero as unresolved.

The checker does not call a special-function library. This makes its trust
surface small, but it does not make the producer independently verified.

## Search order

At each height, use the following order.

1. scalar `Re F` values;
2. two-point `A/B` and secant values;
3. low-order alternating divided differences;
4. frozen exact real-vector Pick contractions;
5. only then derivative jets, Stieltjes localizers, or nonlinear minors.

This ordering is intentional. Value-only witnesses require fewer primitive
calls, avoid numerical differentiation, and allow exact contraction before
interval evaluation.

## Candidate promotion

A strict negative may receive a provisional candidate ID only after:

- exact dyadic points and vectors are frozen;
- the first producer's outward interval has upper endpoint below zero;
- all primitive gates pass;
- the exact checker reproduces the sign;
- a second directed implementation reproduces the primitive values and final
  sign;
- the relevant analytic passivity implication is independently reviewed.

A fitted pole, negative surrogate eigenvalue, no-remainder Riemann--Siegel
screen, or ordinary arbitrary-precision sign is proposal-only.

## Artifact policy

Workflow artifacts should contain complete primitive rectangles and checker
output. Compact committed summaries should bind:

- artifact and file hashes;
- exact points and channels;
- backend and source fingerprints;
- strict interval endpoints;
- all unresolved or failed gates.

A matching hash without regeneration and arithmetic replay is not independent
verification.

## Motivation

The active branches now contain several existentially complete passivity
criteria, but no actual directed special-function producer. The shortest path
to an unconditional witness is therefore not another theoretical criterion; it
is a narrow, auditable numerical bridge from exact points to rigorous primitive
`F` rectangles and then to one exact negative contraction.

## Gap audit

- Two assemblies using one Arb zeta call share a numerical core.
- An Actions runner is a reproducibility environment, not an independent
  verifier.
- Rigorous low-height controls do not establish a high-height sign.
- A positive high-height sample excludes only that exact finite channel.
- High-height zeta jets may be computationally expensive; timeout is not
  mathematical evidence.
- The final implication inherits the status of the parent passivity claims.

## Adversarial tests

- Inject the historical wrong completion sign and require an assembly or
  functional-equation failure.
- Mutate one endpoint, coefficient, channel ID, or point ordinate and require
  rejection.
- Supply positive scalar values with a negative exact secant or Pick
  contraction and require the negative to survive.
- Widen a decisive interval through zero and require unresolved status.
- Reevaluate controls at multiple precisions and require narrowing or stable
  containment.
- Deliberately disable the rigorous backend and require the workflow to fail,
  not to substitute ordinary high precision.

## Remaining uncertainty

The pipeline has now passed a rigorous low-height end-to-end control. Its main
open questions are high-height runtime, interval width, the absence or presence
of an actual negative channel, and independent backend reproduction.

## Suggested next attack

Run scalar and two-point exact-dyadic batches around the strongest independently
identified carrier basins above `3*10^12`. Any negative should preempt broad
scanning and be escalated immediately to a second implementation.
