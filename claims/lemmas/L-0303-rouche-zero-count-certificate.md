# L-0303 — Rouché zero-count certificate

Claim ID: L-0303  
Title: Rouché theorem in certificate form  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: L-0302  
Scope: transfer of a known zero count under a strict boundary inequality  
Related counterexample candidates: local zero enclosures

## Statement

Let `C` be a positively oriented rectifiable Jordan curve.  Let `f` and `g` be
analytic on an open set containing `C` and its interior.  If
\[
 |f(z)-g(z)|<|g(z)|\qquad(z\in C),
\]
then `f` and `g` have the same number of zeros inside `C`, counted with
multiplicity.

In particular, if `g` is an affine function with exactly one zero inside `C`,
the displayed strict inequality certifies exactly one zero of `f` inside.

## Proof

For `0<=t<=1`, define
\[
 F_t(z)=g(z)+t(f(z)-g(z)).
\]
On `C`,
\[
 |F_t(z)-g(z)|=t|f(z)-g(z)|<|g(z)|.
\]
If `F_t(z)=0`, then `|g(z)|=|F_t(z)-g(z)|`, a contradiction.  Thus every
`F_t` is nonzero on `C`.

By L-0302, because `F_t` is analytic,
\[
 N(t)=\frac{1}{2\pi i}\int_C\frac{\partial_zF_t(z)}{F_t(z)}\,dz
\]
is the number of its zeros inside and hence is an integer.  The integrand is
continuous jointly in `(t,z)` on the compact set `[0,1] x C` because the
denominator never vanishes.  Therefore `N(t)` is a continuous
integer-valued function of `t`, so it is constant.  At `t=0`, `F_0=g`; at
`t=1`, `F_1=f`.  Hence `f` and `g` have the same zero count.  ∎

## Motivation

Near an approximate simple zero `z0`, one can choose
`g(z)=f(z0)+f'(z0)(z-z0)` or an exact affine enclosure.  If interval bounds
prove the strict boundary inequality, a numerical seed becomes a rigorous
existence and uniqueness certificate.

## Analytic domain audit

- Both functions must be analytic on the full closed interior.
- Strict inequality is needed everywhere on the continuous boundary.
- If poles are present, first cancel them or use a meromorphic version with
  explicit pole counts.
- No logarithm branch is used.

## Dependency audit

L-0302 supplies the integer-valued zero count.  Compactness and continuity
supply homotopy invariance.

## Gap audit

- Checking finitely many boundary points is insufficient without derivative or
  interval bounds covering the segments.
- An interval inequality whose endpoints touch is not strict.
- A first-order model with interval derivative must enclose the true remainder.
- "One zero" includes multiplicity; simplicity requires more.

## Adversarial tests

- Let `f(z)=z+epsilon z^2`, `g(z)=z` on a small circle.
- Increase the circle until equality occurs; the certificate must stop.
- Use a region containing a pole to confirm the analytic hypothesis catches
  the error.

## Remaining uncertainty

None in the analytic lemma.  Constructing sharp uniform remainder bounds for
`zeta`, `zeta'`, or `H_t` is application-specific.

## Suggested next attack

Develop an interval-Taylor Rouché certificate schema with exact rational
rectangle/disc data and independently checkable coefficient balls.
