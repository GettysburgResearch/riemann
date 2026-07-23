# L-5702 — Scale-invariant feature-repair moat

Claim ID: L-5702  
Title: A strict conic portfolio gives a lower bound on the primitive perturbation required to erase it  
Status: PROPOSED  
Authoring agent: `gpt56-06-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-5701; L-5701  
Scope: normalized robustness ranking of finite witness portfolios  
Related counterexample candidates: none

## Statement

Let the RH-admissible finite-feature region `K` satisfy

\[
P(y)=\beta+c^{\mathsf T}y\ge0
\qquad\text{for every }y\in K.
\]

Let `C` be nonempty and suppose

\[
\sup_{x\in C}P(x)\le-\mu<0.
\]

For any norm `||.||` with dual norm `||.||_*`, if `c!=0`, then

\[
\operatorname{dist}(C,K)
\ge
\frac{\mu}{\|c\|_*}.
\]

Thus for `Y=R^n`,

\[
\operatorname{dist}_{\infty}(C,K)
\ge\frac{\mu}{\|c\|_1},
\qquad
\operatorname{dist}_{1}(C,K)
\ge\frac{\mu}{\|c\|_\infty}.
\]

If `c=0` and `mu>0`, the imported finite constraints are inconsistent with every
feature vector in the declared affine model; no finite perturbation of those
features can repair the certificate.

The ratio `mu/||c||_*` is invariant under positive rescaling of the complete
portfolio.

## Motivation

The raw score moat can be made arbitrarily large by multiplying every portfolio
weight by a large positive rational. It is therefore unsuitable for comparing
candidates.

The feature-repair moat answers the geometric question:

> how much additional primitive-data movement would an adversary need before
> the uncertainty set could possibly touch the RH-admissible finite cone?

This is the quantity an uncertainty closer should use to rank survivors.

## Proof or construction

For any `x in C` and `y in K`,

\[
\mu
\le P(y)-P(x)
=c^{\mathsf T}(y-x)
\le\|c\|_*\|y-x\|.
\]

Take the infimum over `x` and `y`. If `c=0`, then `P` is constant and the two
inequalities `P<=-mu` on `C` and `P>=0` on `K` force `K` to be empty in the
declared feature model.

Positive rescaling multiplies both `mu` and `||c||_*` by the same factor.

## Analytic domain audit

Finite-dimensional normed-space geometry only.

## Dependency audit

D-5701 supplies `K` and the affine portfolio. L-5701 supplies strict robust
separation of `C`.

## Gap audit

- The bound is norm and parameterization dependent. The feature coordinates
  must have physically meaningful scaling.
- A crude feature basis can make the bound weak. Reparameterization must be
  declared rather than used cosmetically.
- The result measures only perturbations represented in the chosen feature
  space; wrong theorems and missing terms remain logical or semantic defects.
- A positive repair moat does not by itself prove implementation independence.

## Adversarial tests

1. Rescale all portfolio weights and verify invariance.
2. Use a one-dimensional coefficient `1/2` and moat `3/10`; verify the exact
   `L-infinity` repair lower bound `3/5`.
3. Use exact coefficient cancellation and require the infinite-in-feature-space
   result.
4. Change feature units by an invertible diagonal map and verify that the
   coordinate norm changes consistently.

## Remaining uncertainty

Selecting a canonical feature norm across heterogeneous quantities—special-
function samples, matrix blocks, and arithmetic constants—requires route-level
judgment. Weighted norms or exact support functions may be sharper.

## Suggested next attack

Have every candidate producer export both the robust score endpoint and one
scale-invariant feature-repair lower bound. Use the latter, not an arbitrarily
scaled eigenvalue or portfolio score, to prioritize independent reproduction.
