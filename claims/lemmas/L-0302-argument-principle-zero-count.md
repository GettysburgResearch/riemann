# L-0302 — Argument-principle zero count

Claim ID: L-0302  
Title: Argument-principle zero and pole count  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: residue theorem; local factorization of meromorphic functions  
Scope: exact analytic kernel for contour certificates  
Related counterexample candidates: direct zeta, Speiser, and Newman rectangles

## Statement

Let `C` be a positively oriented rectifiable Jordan curve, and let `f` be
meromorphic on an open set containing `C` and its interior.  Assume `f` has no
zero or pole on `C`.  Then
\[
 \frac{1}{2\pi i}\int_C\frac{f'(z)}{f(z)}\,dz
   =N_C(f)-P_C(f),
\]
where zeros and poles inside `C` are counted with multiplicity/order.

If `f` is analytic inside and on `C`, the integral equals the number of zeros
inside `C`, counted with multiplicity.

## Proof

The zeros and poles inside the compact interior are isolated and hence finite
in number unless `f` is identically zero; the boundary hypothesis and
meromorphicity exclude the identically-zero case.

Let `a` be a zero of order `m`.  On a neighborhood of `a`,
\[
 f(z)=(z-a)^m u(z),
\]
where `u` is analytic and nonzero.  Therefore
\[
 \frac{f'(z)}{f(z)}=\frac{m}{z-a}+\frac{u'(z)}{u(z)},
\]
so `f'/f` has residue `m` at `a`.

Let `b` be a pole of order `n`.  Then
\[
 f(z)=(z-b)^{-n}v(z)
\]
with `v` analytic and nonzero, and
\[
 \frac{f'(z)}{f(z)}=-\frac{n}{z-b}+\frac{v'(z)}{v(z)}.
\]
Thus the residue at `b` is `-n`.

There are no other singularities of `f'/f` inside `C`: where `f` is finite and
nonzero, the quotient is analytic.  The residue theorem now gives
\[
 \frac{1}{2\pi i}\int_C\frac{f'}{f}
 =\sum_{\text{zeros }a}m_a-\sum_{\text{poles }b}n_b.
\]
This is the claimed identity.  ∎

## Motivation

A rigorous positive integer count in a rectangle is a compact existence proof,
unlike a sampled small value or a plotted phase change.  The same kernel
applies to `xi`, `zeta'`, and `H_t`.

## Analytic domain audit

- The open neighborhood must contain the entire closed interior, not only the
  curve.
- No zero or pole may lie on `C`.
- If `f=zeta`, the pole at `1` contributes `-1` unless removed or excluded.
- If `f=xi`, there are no poles.
- The integral is orientation-sensitive.

## Dependency audit

Only local zero/pole factorization and the residue theorem are used.

## Gap audit

A numerical quadrature close to an integer is not yet this theorem's
hypothesis.  A certificate must prove:

1. analyticity/meromorphicity on the closed region;
2. boundary nonvanishing;
3. an enclosure forcing the integral or winding number to one exact integer.

## Adversarial tests

- `f(z)=z^m` on a circle: count `m`.
- `f(z)=1/z^n`: count `-n`.
- Reverse orientation: sign flips.
- Move a zero onto the boundary: theorem becomes inapplicable.

## Remaining uncertainty

No mathematical gap is known.  Certified numerical realization remains a
separate task.

## Suggested next attack

Combine with L-0304 so a polygonal enclosure of the image loop, rather than
direct integration of `f'/f`, can certify the same count.
