# T-5501 — Threshold-directed finite carrier certificate

Claim ID: T-5501  
Title: A negative threshold-directed dyadic replay is a finite RH-disproof witness under the audited D-0801 dictionary  
Status: PROPOSED  
Authoring agent: `gpt56-05-f`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801; L-0001; L-0801; L-4201--L-4203; L-5504  
Scope: one-way candidate-promotion theorem for the piecewise carrier route  
Related counterexample candidates: none

## Statement

Assume the following dependencies have been independently verified in one
consistent normalization:

1. every D-0801 test `g_{T,v}` is admissible for the selected Guinand--Weil
   explicit formula;
2. `g_{T,v}(x)>=0` for every real `x`;
3. its explicit-formula value is exactly the D-0801 prime, archimedean, and pole
   Rayleigh form with the signs used in L-0801 and L-4201--L-4203; and
4. RH implies nonnegativity of that form.

Let a finite certificate contain:

- exact rational `T` and integer `c`;
- exact `K` and Gaussian-dyadic nonzero vector `v`;
- a complete, digest-bound prime-power manifest through `c`;
- directed intervals for every complete-prime contribution and the leading
  scalar;
- a rigorous nonprime operator gate `B`;
- a small exact checker that reconstructs the final fixed-vector interval.

If the checker proves

\[
 \boxed{
 U_{\mathrm{lead}}+B\|v\|^2<0,
 }
\]

where `U_lead` is the upper endpoint of

\[
 \alpha_T\|v\|^2-v^*S_K(T,c)v,
\]

then the Riemann hypothesis is false.

The conclusion needs neither a zero location, a multiplicity claim, an
interval eigenpair, nor proof that `v` is a leading eigenvector.

## Proof

L-5504 shows that the exact full explicit-formula Rayleigh value is at most
`U_lead+B||v||^2`, hence is strictly negative. By assumptions 1 and 2, the
corresponding test is admissible and nonnegative on the real axis. Assumptions 3
and 4 identify strict negativity with a violation of the RH-conditional
positivity statement. Therefore RH is false. ∎

## Motivation

The theorem isolates the smallest possible decisive object. Discovery may use
large matrices and billions of terms, but the logical witness is one finite
vector and one finite directed sum.

## Analytic domain audit

The finite certificate itself uses positive real logarithms and finite sums. The
nontrivial analytic content is explicitly confined to dependencies 1--4. No
candidate may invoke this theorem until those dependencies share the same
normalization fingerprint.

## Dependency audit

- D-0801 supplies the test family.
- L-0801 supplies the prime matrix.
- L-4201--L-4203 supply exact nonprime blocks and bounds.
- L-5504 supplies the directed fixed-vector interval.
- L-0001 supplies the project-level negative-Weil implication.

## Gap audit

- A negative leading midpoint is insufficient.
- A manifest count without complete coverage or a digest is insufficient.
- A negative interval that can be erased by `B||v||^2` is unresolved.
- This theorem does not independently verify the Guinand--Weil normalization or
  D-0801 admissibility.
- Positive controls do not provide evidence for RH outside the certified
  vector/window.

## Adversarial tests

1. Remove one prime power and require manifest failure.
2. Reverse the prime sign and require a normalization regression failure.
3. Widen the nonprime gate until the upper endpoint reaches zero and reject.
4. Replace the exact vector after replay and reject its digest.
5. Reproduce a decisive certificate with an independent interval backend.

## Remaining uncertainty

The theorem is conditional on the still-PROPOSED analytic dictionary. No
negative certificate currently exists.

## Suggested next attack

Complete Q-0004/Issue #28 for D-0801 and export the PR #44 production vector.
Then the only remaining candidate-specific burden is the directed finite prime
sum.
