# T-0311 — Deléglise--Nicolas bounded-prime-sum criterion

Claim ID: T-0311  
Title: Bounded-prime-sum arithmetic criterion equivalent to RH  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: external theorem of Deléglise--Nicolas  
Scope: imported finite arithmetic-witness criterion  
Related counterexample candidates: Issue #16

## Statement

For an integer \(n\ge1\), define
\[
 h(n)=\max\left\{
   \prod_{p\in S}p:
   S\text{ is a finite set of distinct primes and }
   \sum_{p\in S}p\le n
 \right\}.
\]

Let \(\operatorname{li}^{-1}\) denote the inverse of the increasing real branch
of the logarithmic integral on \(x>1\).  Deléglise and Nicolas proved
\[
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \log h(n)<\sqrt{\operatorname{li}^{-1}(n)}
 \quad\text{for every integer }n\ge1.
\]

Therefore, one explicit integer \(n\ge1\), together with a proof that
\[
 \log h(n)\ge\sqrt{\operatorname{li}^{-1}(n)},
\]
is a finite unconditional counterexample witness.

## Source

Marc Deléglise and Jean-Louis Nicolas, *An arithmetic equivalence of the
Riemann hypothesis*, Journal of the Australian Mathematical Society 106
(2019), no. 2, 235--273, DOI 10.1017/S1446788718000083.

Supporting algorithmic source:

Marc Deléglise and Jean-Louis Nicolas, *Maximal product of primes whose sum is
bounded*, Proceedings of the Steklov Institute of Mathematics 282 (2013),
73--102, arXiv:1207.0603.

Inspection level: the publisher abstract of the 2019 paper was inspected and
states the definition, quantifier \(n\ge1\), strict inequality, inverse
logarithmic integral, and equivalence.  The 2013 algorithm paper was located
and its abstract inspected; its algorithms are not imported as proved claims
here.

## Motivation

This is a genuine one-object witness route.  It replaces the unconstrained
integer factorization search in Robin's criterion with a prime-subset
optimization whose objective and budget are both discrete.  L-0370 supplies a
small, exact verification kernel.

## Proof status

Imported theorem; proof not reproduced.  The finite-witness implication is
the direct contrapositive of the displayed equivalence.

## Analytic/domain audit

- \(n\) is an integer and \(n\ge1\).
- The primes in the product are distinct.
- The empty set is permitted, so the maximum exists and is at least \(1\).
- Only primes \(p\le n\) can occur, hence the maximum ranges over a finite set.
- \(\operatorname{li}^{-1}\) is the increasing real inverse on \(x>1\);
  a certificate must state the precise logarithmic-integral normalization.
- The inequality under RH is strict.  Equality is therefore also a violation.

## Dependency audit

- The equivalence is imported from Deléglise--Nicolas.
- L-0370 independently proves the exact dynamic-programming recurrence for
  computing \(h(n)\) on finite ranges.
- A counterexample certificate additionally needs a rigorous interval
  enclosure for the logarithm and inverse logarithmic integral.

## Gap audit

- Exhibiting a large admissible product does not prove it equals \(h(n)\).
- Floating-point logarithms do not certify either product ordering or the
  final inequality.
- A pruned optimizer must prove that no discarded state can beat the retained
  frontier.
- Different conventions for \(\operatorname{li}\) differ by constants or
  branches; the source normalization must be fingerprinted.
- A computed violation is not a candidate until the maximizing property and
  transcendental comparison are both rigorous.

## Adversarial tests

1. Compare L-0370 against exhaustive subset enumeration for all small \(n\).
2. Verify that the chosen subset uses distinct primes and obeys the sum bound.
3. Recompute the exact product from the certificate.
4. Verify global optimality with an implementation independent of the search.
5. Enclose \(x=\operatorname{li}^{-1}(n)\) by proving
   \(\operatorname{li}(x_-)\le n\le\operatorname{li}(x_+)\) on the chosen
   increasing branch.
6. Reject a final comparison whenever the two enclosures overlap.

## Remaining uncertainty

The exact equivalence is explicit in the inspected primary publisher abstract.
The proof and inverse-function normalization should nevertheless receive an
independent full-text audit before a witness is promoted.

## Suggested next attack

Claim Issue #16.  Begin with a proof-producing implementation of L-0370 and a
separate exact verifier, then replace the quadratic dynamic program by
certified dominance or meet-in-the-middle methods without changing the
certificate semantics.
