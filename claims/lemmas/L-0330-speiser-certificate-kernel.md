# L-0330 — Speiser finite-certificate kernel

Claim ID: L-0330  
Title: A certified left-half-strip zero of `zeta'` disproves RH  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: T-0306, L-0302; optionally L-0303/L-0304  
Scope: one-way finite witness for Issue #17  
Related counterexample candidates: derivative-zero rectangles

## Statement

Let `R` be a bounded Jordan domain whose closure satisfies
\[
 0<\operatorname{Re}s<\frac12,
 \qquad
 \operatorname{Im}s>0.
\]
Assume `zeta'` is nonzero on `boundary R` and a rigorous argument-principle or
winding-number certificate proves that `zeta'` has at least one zero in `R`.
Then RH is false.

It is enough to certify one of the following:

1. a positive integer value of
   \[
    \frac{1}{2\pi i}\int_{\partial R}\frac{\zeta''(s)}{\zeta'(s)}\,ds;
   \]
2. a positive winding number of the loop `zeta'(boundary R)` about zero;
3. a Rouché comparison with an analytic function having a known positive zero
   count in `R`.

## Proof

Because the closure of `R` lies in `Im(s)>0`, every point of `R` is nonreal.
Because it also lies in `0<Re(s)<1/2`, any zero of `zeta'` in `R` is a nonreal
zero strictly left of the critical line.

By L-0302, the first certificate counts zeros of `zeta'` in `R` because
`zeta'` is analytic there and nonzero on the boundary.  The winding-number
form is the same argument principle expressed as the winding of the image
loop.  L-0303 supplies the Rouché alternative.

Thus any of the certificates proves the existence of a nonreal zero of
`zeta'` with real part less than `1/2`.  T-0306 (Speiser's criterion) says RH
is equivalent to the absence of such zeros.  Therefore RH is false.  ∎

## Motivation

This isolates the exact logical bridge needed by Issue #17.  Search heuristics
can change without changing the compact final certificate.

## Analytic domain audit

- `zeta'` is analytic on the critical strip; the pole of `zeta` at `1` lies
  outside the closure by hypothesis.
- The rectangle must be separated from both `Re(s)=1/2` and `Im(s)=0`.
- No zero may lie on the boundary.
- A completed derivative such as `xi'` has a different zero set and cannot be
  substituted without proof.

## Dependency audit

T-0306 supplies the imported equivalence.  L-0302/L-0303/L-0304 supply
standard certificate mechanisms.

## Gap audit

- A small value of `zeta'` does not prove a zero.
- Sampling only vertices does not prove boundary nonvanishing.
- A zero count may include multiplicity; uniqueness or simplicity requires
  additional work.
- The theorem needs a zero of `zeta'`, not a pole/zero of `zeta''/zeta'` caused
  by an implementation branch error.

## Adversarial tests

- Test the contour verifier on polynomials with known multiple zeros.
- Perturb every rectangle edge and increase precision.
- Compare direct `zeta'` winding with integration of `zeta''/zeta'`.
- Reject any contour image ball containing zero.

## Remaining uncertainty

The exact Speiser statement was verified through later primary restatements;
the original German proof has not been reconstructed in the repository.

## Suggested next attack

Implement the generic certificate schema proposed in L-0304, then specialize
the analytic evaluator to `zeta'`.
