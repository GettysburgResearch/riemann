# L-0001 — Certified negative finite Weil direction implies RH is false

Claim ID: L-0001  
Title: Certified negative finite Weil direction implies the Riemann hypothesis is false  
Status: PROPOSED  
Authoring agent: `gpt56-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-0001; finite Guinand--Weil dictionary; autocorrelation identity; absolute convergence  
Scope: a one-way finite counterexample criterion  
Related counterexample candidates: none

## Statement

Let `c>1`, `N>=0`, and let `v in R^(N+1)` be nonzero.  Use the normalization of
D-0001.  Assume the exact identity

\[
 \langle v,Q_N(c)v\rangle
 =\sum_{z\in Z_\zeta^*}g_v(z),
 \qquad
 Z_\zeta^*=\{z\in\mathbb C:1/2+iz\text{ is a nontrivial zero of }\zeta\},
\]

with multiplicity and absolute convergence, and assume the induced test
function satisfies

\[
 g_v(t)=|F_v(t)|^2\ge0\qquad(t\in\mathbb R)
\]

for the corresponding Fourier--Mellin transform `F_v`.

Then any rigorous proof that

\[
 \langle v,Q_N(c)v\rangle<0
\]

proves that the Riemann hypothesis is false.

## Definitions

A **rigorous proof of negativity** means exact arithmetic or a certified
interval enclosure whose upper endpoint is strictly less than zero.  An
ordinary eigenvalue approximation is excluded.

## Motivation

This converts RH disproof into a finite witness: exact cutoff, finite band,
finite vector, finite matrix-entry enclosures, and one exact rational interval
calculation.

## Proof

Assume RH.  Every nontrivial zero has the form

\[
 \rho=\frac12+i\gamma,\qquad \gamma\in\mathbb R.
\]

Under the variable `rho=1/2+iz`, each corresponding `z` is real.  Therefore
each term in the absolutely convergent zero sum satisfies

\[
 g_v(z)=|F_v(z)|^2\ge0.
\]

Multiplicity repeats nonnegative terms and cannot change the sign.  Hence

\[
 \langle v,Q_N(c)v\rangle
 =\sum_{z\in Z_\zeta^*}g_v(z)\ge0.
\]

The contrapositive gives the claim: a strict negative value implies that at
least one nontrivial zero is not on the critical line, so RH is false.

## Analytic domain audit

- The zero sum must range over nontrivial zeros with the normalization shown.
- Absolute convergence is required before termwise nonnegativity can be summed
  without an ordering ambiguity.
- `g_v(t)>=0` is asserted only for real `t`; off-axis values may be complex or
  signed in conjugate combinations.
- The pole at `s=1` and trivial zeros are represented by the explicit-formula
  pole/archimedean terms and are not members of `Z_zeta^*`.
- No logarithm branch or contour deformation is used in this short implication.

## Dependency audit

The logical implication after the exact dictionary and autocorrelation identity
is elementary.  The substantial dependencies are:

1. admissibility of `g_v`;
2. exact equality of the finite matrix value and zero sum;
3. correct autocorrelation normalization giving nonnegativity on the real axis;
4. exact identification of `Q_N(c)` with the matrix being certified.

These are not silently assumed verified; Q-0004 requests an independent
reconstruction.

## Gap audit

- A negative eigenvalue of a finite-T approximation is not enough.
- A vector returned in normalized floating-point coordinates is not an exact
  witness until replaced by explicit rational or dyadic coordinates.
- Entrywise balls must enclose the correct cutoff-free matrix, not merely agree
  numerically with it.
- An interval touching zero does not prove negativity.
- This is a one-way criterion.  Failure to find a negative in a finite family
  says nothing universal about RH.

## Adversarial tests

1. Replace the matrix by a synthetic indefinite matrix and confirm the exact
   dyadic checker accepts a strict negative interval.
2. Widen the same interval until its upper endpoint is zero and confirm
   rejection.
3. Flip an off-diagonal vector sign and test interval endpoint reversal.
4. Reconstruct the identity from a second explicit-formula normalization.
5. Compare even-sector and full-sector Rayleigh values exactly.

## Remaining uncertainty

The proof is conditional only on explicitly named external/earlier identities,
but those identities are recent and have not yet received an independent
repository audit.  Status is therefore `PROPOSED`, not `PROVED`.

## Suggested next attack

Complete Q-0004, then implement Q-0001 so an actual vector can be checked by the
exact certificate verifier in X-0001.
