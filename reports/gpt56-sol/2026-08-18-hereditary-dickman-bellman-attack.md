# Hereditary Dickman–Bellman attack beyond PR #607

## Result of this pass

The exact Stieltjes representation of PR #607 supports a stronger recursive statement than state-wise positivity. If `p` is the least allowed rough prime,

\[
U(Y,p)=U(Y,p^+)-p^{-1}U(Y/p,p^+).
\]

The continuous Dickman model has margin

\[
a_*[\rho(u)-p^{-1}\rho(u-1)].
\]

Since `rho(u-1)/rho(u) << u log(u+2)`, the margin is a fixed positive fraction of `rho(u)` whenever `p >> u log u`. Throughout PR #607's VK mesoscopic corridor this condition is automatic, and the same VK discrepancy is `o(rho(u))`. Hence the one-prime Bellman inequality itself holds uniformly there.

This is deposited as `L-98050` and `T-98050`.

## New closure strategy

Let `p_*(Y)` be the least threshold for which the hereditary mesoscopic theorem applies. Decompose the root rough Euler source into:

1. a finite block of primes `67 <= p < p_*(Y)`;
2. the hereditary tail `p >= p_*(Y)`.

The tail can now be peeled by exact one-prime Bellman inequalities without losing source ownership. The remaining question is whether the finite small-prime Euler block preserves nonnegativity of the boundary state.

The correct next target is therefore not another all-prime estimate but a finite-block transfer theorem:

> **Dynamic finite-block transfer (`DFBT67`).** Applying the ordered Euler factors for all primes `67 <= p < p_*(Y)` to a tail state lying in the hereditary corridor preserves the root zero-hinge sign.

This is still nontrivial because a positive state need not remain positive under `I-p^{-1}S_p`; the exact p=67 fixed-angle separator shows that scalar-to-mass cones are insufficient. Any proof of DFBT67 must retain either the future quotient profile or an ordered variation/Lorenz invariant.

## Candidate invariants

The most promising are:

- the exact Stieltjes profile `x -> A_z(Y/x)` paired with signed `dh`;
- ordered source-ratio profile from PR #601;
- the two-state reciprocal-Mertens target recurrence from PR #598;
- a finite prefix Lorenz deficit evaluated only at the zero marginal, since PR #601 proves nonzero thresholds are eventually redundant.

A successful DFBT67 proof would compose as

```text
hereditary mesoscopic Bellman tail
 -> dynamic finite-block transfer
 -> GPC67
 -> Mellin-Landau
 -> RH.
```

## Boundary

```text
native one-prime recurrence                 EXACT
continuous Dickman Bellman margin           PROVED
hereditary mesoscopic Bellman corridor       PROVED
finite small-prime block transfer            OPEN
root GPC67                                   OPEN
RH                                            UNPROVED
```
