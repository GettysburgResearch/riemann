# L-5505 — Dyadic freezing with direct-replay validation

Claim ID: L-5505  
Title: A floating carrier mode can be frozen to finite dyadic data without trusting the rounding step  
Status: PROPOSED  
Authoring agent: `gpt56-05-f`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: continuity of finite quadratic forms; L-5504  
Scope: transition from discovery eigenvectors to exact proof inputs  
Related counterexample candidates: none

## Statement

Let `w in C^K` be any floating discovery vector and choose a bit depth `b>=0`.
Round each real and imaginary coordinate independently to an integer multiple of
`2^{-b}`, obtaining the exact Gaussian-dyadic vector `v_b`.

Then:

1. `v_b` is a finite exact proof input, regardless of whether it remains an
   eigenvector;
2. the coordinatewise construction gives
   \[
   \|v_b-w\|_2\le 2^{-b-1}\sqrt{2K};
   \]
3. if a Hermitian discovery matrix `H` satisfies `||H||_2<=M`, then
   \[
   |v_b^*Hv_b-w^*Hw|
   \le M\left(2\|w\|_2\delta+\delta^2\right),
   \qquad
   \delta=2^{-b-1}\sqrt{2K};
   \]
4. most importantly, a complete L-5504 replay on `v_b` certifies the exact
   vector directly and makes the floating vector, eigensolver, and perturbation
   estimate logically irrelevant to the final sign.

A vector artifact should store exact integer coordinate numerators, `b`, `K`,
the nomination metadata, and a canonical digest computed after all metadata is
finalized.

## Proof

Each real coordinate changes by at most `2^{-b-1}`, and the same is true for
each imaginary coordinate. Summing `2K` squared coordinate errors proves the
norm bound.

Write `e=v_b-w`. Then

\[
 v_b^*Hv_b-w^*Hw=w^*He+e^*Hw+e^*He.
\]

Apply the operator-norm inequality and `||e||<=delta`. Point 4 follows because
L-5504 evaluates the exact quadratic form of `v_b`; it does not infer that value
from `w`. ∎

## Motivation

Eigenvector rationalization is often treated as a fragile final step. Direct
fixed-vector replay reverses the logic: rounding only nominates a compact exact
vector, and the complete arithmetic is rerun on that vector. No continuity
margin need be trusted for acceptance.

## Analytic domain audit

Pure finite-dimensional algebra. No complex branches or analytic continuation.

## Dependency audit

The perturbation estimate is elementary. L-5504 supplies the final exact-vector
certificate interface.

## Gap audit

- The canonical digest must be computed after adding rounding diagnostics.
- Coordinates must fit the exact integer backend's proved overflow contract.
- Renormalizing a dyadic vector by an irrational norm destroys dyadic exactness;
  retain the exact unnormalized vector and scale the gate by its exact norm.
- A small floating rounding error is not itself a proof of a sign.

## Adversarial tests

1. Mutate one numerator after digest creation and reject.
2. Use a vector whose norm differs slightly from one and verify gate scaling.
3. Round a nearly degenerate eigenvector at several bit depths.
4. Compare direct replay values, not floating residuals.

## Remaining uncertainty

No mathematical gap is known.

## Suggested next attack

For production candidates, export several bit depths and choose the smallest one
whose directed replay keeps the desired margin. Smaller exact vectors reduce
certificate size and checker cost.
