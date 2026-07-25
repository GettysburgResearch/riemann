# L-8404 — Directed Hardy-Z sign changes certify disjoint critical-line zero bins

Claim ID: L-8404  
Title: Opposite rigorous Hardy-Z endpoint signs give a lower critical-line zero count  
Status: PROPOSED  
Authoring agent: `gpt56-06-e`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: standard Hardy-Z identity and continuity; directed special-function enclosures  
Scope: zero-count inputs for L-8401–L-8403  
Related counterexample candidates: none

## Statement

Let `Z(t)` be a real-valued continuous Hardy function satisfying

\[
 Z(t)=e^{i\vartheta(t)}\zeta\!\left(\frac12+it\right)
 \in\mathbb R
 \qquad(t\in\mathbb R),
\]

where the phase factor never vanishes. Let `a<b` be exact rational or dyadic
ordinates. If directed real enclosures prove

\[
 Z(a)>0>Z(b)
 \qquad\text{or}\qquad
 Z(a)<0<Z(b),
\]

then `[a,b]` contains at least one zero of `xi(1/2+it)`, counted with
multiplicity.

More generally, exact endpoints

\[
 a_0<a_1<\cdots<a_N
\]

with certified nonzero alternating signs produce `N` pairwise interior-disjoint
bins, each with lower count one. If the bins are used closed in a downstream
certificate, the endpoint nonzero signs prove that no endpoint zero is shared.

## Proof

By continuity, opposite endpoint signs force a point `gamma in (a,b)` with
`Z(gamma)=0`. The phase factor is nonzero, so

\[
 \zeta\!\left(\frac12+i\gamma\right)=0.
\]

The completed factors are finite and nonzero at a nontrivial critical-line zero,
so `xi(1/2+i gamma)=0`. Existence gives a lower multiplicity count of at least
one. Alternating signs apply the same argument to every adjacent open interval;
those intervals are disjoint. ∎

## Motivation

L-8401–L-8403 need only lower counts, not a complete zero census. A rigorous
Hardy-Z sign change is therefore an inexpensive proof object: it avoids
multiplicity certification, zero uniqueness, Turing completeness, and exact
ordinate isolation unless sharper contribution bounds are required.

## Certificate interface

A sign-change certificate should contain:

- exact endpoint ordinates;
- outward Hardy-Z intervals excluding zero with opposite signs;
- the completed-zeta normalization and phase convention;
- a producer fingerprint and precision;
- a bin identifier consumed exactly once by the deflation checker.

For a narrower bin, interval Newton or a derivative-assisted bisection may refine
the sign bracket while preserving the original existence certificate.

## Analytic domain audit

Hardy `Z` is continuous and real on the real axis. The proof uses no logarithm
branch and no assertion that the zero is simple. The bin may contain additional
or even-multiplicity zeros; the certified lower count remains one.

## Dependency audit

The theorem uses only the standard nonvanishing phase relation between Hardy `Z`
and zeta on the critical line plus the intermediate value theorem. A production
implementation must audit its exact `theta` convention, but the zero set is
unchanged by any continuous unit-modulus phase.

## Gap audit

- A sampled sign computed without directed error is not a certificate.
- Same-sign endpoints prove nothing about even numbers of zeros.
- Opposite midpoint signs in overlapping bins can charge one zero more than once.
- The statement proves at least one zero, not uniqueness or simplicity.
- Trivial zeros and the pole are absent because the points lie on the nontrivial
  critical line at real ordinates; a production schema should still declare the
  height domain explicitly.

## Adversarial tests

1. Use an exact polynomial Hardy-Z surrogate with one sign-changing root.
2. Use a double root with same endpoint sign and require no count.
3. Let one endpoint interval touch zero and require unresolved status.
4. Chain alternating signs and verify strict bin disjointness.
5. Mutate the Hardy phase by a nonvanishing unit factor and verify the zero set is
   unchanged.

## Remaining uncertainty

At very large heights, the practical cost is rigorous Hardy-Z evaluation and
finding short brackets. The Riemann-Siegel Arb backend already used by Issue #39
is the natural starting point.

## Suggested next attack

For each passivity finalist, scan a narrow ordinate window with ordinary
Riemann-Siegel arithmetic, freeze rational sign-bracket endpoints, and escalate
only those endpoint evaluations to directed Arb. Feed the resulting disjoint
one-zero bins directly into X-8401.
