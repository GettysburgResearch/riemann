# L-0360 — Positive-time Newman witness

Claim ID: L-0360  
Title: A nonreal zero of `H_t` at positive time disproves RH  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: T-0309  
Scope: one-way finite witness for Issue #18  
Related counterexample candidates: positive-time de Bruijn--Newman rectangles

## Statement

Use the de Bruijn--Newman normalization in T-0309.  Let `t0>0`.  If a rigorous
certificate proves that the entire function `H_{t0}` has a nonreal zero, then
\[
 \Lambda>t_0>0
\]
and RH is false.

A positive zero count in any bounded domain disjoint from the real axis is
such a certificate.

## Proof

T-0309 states that all zeros of `H_t` are real if and only if `t>=Lambda`.
If `H_{t0}` has a nonreal zero, it is not true that all its zeros are real.
Therefore `t0` cannot satisfy `t0>=Lambda`; hence
\[
 t_0<\Lambda.
\]
Since `t0>0`, this gives `Lambda>0`.

The same theorem states that RH is equivalent to `Lambda<=0`.  The inequality
`Lambda>0` contradicts that condition, so RH is false.  ∎

## Motivation

The witness is local and finite: rational `t0`, a rational rectangle separated
from the real axis, and a winding/zero-count certificate.  No direct zeta zero
needs to be isolated.

## Analytic domain audit

The proof assumes the exact `H_t` and threshold direction of T-0309.  In a
numerical application:

- prove the chosen representation defines an entire function of `z`;
- uniformly bound the infinite integral/series on the complete contour;
- account for the exponential growth of `cos(zu)` when `Im(z)!=0`;
- prove boundary nonvanishing.

## Dependency audit

The implication is elementary after T-0309.  Rodgers--Tao's `Lambda>=0` is not
needed for the disproof direction, although it shows RH would force
`Lambda=0`.

## Gap audit

- A nonreal approximate root is not a certificate.
- A rectangle intersecting the real axis does not prove its enclosed zero is
  nonreal.
- Reversing the threshold inequality would reverse the conclusion; source
  normalization is critical.
- A nonreal zero at `t<0` is compatible with the known threshold and does not
  disprove RH.

## Adversarial tests

- Test the contour pipeline on a heat-flow family with known complex zeros.
- Vary `t0` by a rational interval and ensure the evaluator encloses every
  permitted value or fixes one exact rational.
- Independently recompute integral tails and polygon winding.

## Remaining uncertainty

No gap in the conditional implication.  The hard unresolved step is a
certified complex evaluation of `H_t` at positive time.

## Suggested next attack

Begin Issue #18 with explicit uniform tail estimates for the `Phi` series and
the outer integral on a complex rectangle.
