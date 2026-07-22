# T-0301 — Robin criterion

Claim ID: T-0301  
Title: Robin's divisor-sum criterion for RH  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: external theorem of Robin (1984)  
Scope: imported equivalence; proof not reproduced  
Related counterexample candidates: Issue #2 Robin witnesses

## Statement

Let `sigma(n)=sum_{d|n}d` and let `gamma` be Euler's constant.  The Riemann
hypothesis is equivalent to
\[
 \sigma(n)<e^\gamma n\log\log n
 \qquad\text{for every integer }n>5040.
\]

Therefore one exactly specified integer `n>5040` with a certified inequality
\[
 \sigma(n)\ge e^\gamma n\log\log n
\]
is a finite unconditional disproof of RH.

## Source

Original:

Guy Robin, *Grandes valeurs de la fonction somme des diviseurs et hypothèse de
Riemann*, Journal de Mathématiques Pures et Appliquées 63 (1984), 187--213.

The exact displayed criterion was checked in the full text of Jeffrey
Lagarias, *An Elementary Problem Equivalent to the Riemann Hypothesis*,
arXiv:math/0008177 / Amer. Math. Monthly 109 (2002), and in Choie et al.,
*On Robin's criterion for the Riemann hypothesis*, J. Théor. Nombres Bordeaux
19 (2007), DOI 10.5802/jtnb.591.

Inspection note: original Robin metadata was located; the exact statement used
here is a later-primary restatement.  The original proof has not been
reconstructed in this repository.

## Motivation

This is the active finite arithmetic route in Issue #2.  The witness is compact
because `sigma(n)` is exact from a factorization and only the right-hand
transcendental expression requires interval enclosure.

## Proof status

Imported theorem only.  No proof is claimed here.  The elementary
contrapositive from a single violation to `not RH` is immediate from the
equivalence.

## Analytic/domain audit

- The domain is the strict integer range `n>5040`.
- Natural logarithms are used.
- Since `n>5040`, `log log n` is positive.
- Strictness matters: equality is a violation.

## Dependency audit

Issue #2 additionally depends on exact factorization, L-0320, safe pruning, and
certified enclosures for `gamma` and logarithms.  Those are not supplied by
Robin's theorem itself.

## Gap audit

- A floating comparison is not a certified violation.
- A search restricted to a special integer family requires a separate theorem.
- Verifying the inequality for a finite range does not prove RH.
- Confusing `n>=5040` with `n>5040` changes the boundary.

## Remaining uncertainty

Independent review should inspect Robin's original paper and verify theorem
number, boundary convention, and any translation nuance before status
advancement.

## Suggested next attack

Use L-0321 to audit monotone-exponent pruning and independently reconstruct the
colossally abundant reduction used by Issue #2.
