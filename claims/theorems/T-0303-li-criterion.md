# T-0303 — Li criterion

Claim ID: T-0303  
Title: Li coefficient positivity criterion for RH  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: external theorem of Li (1997); Bombieri--Lagarias (1999)  
Scope: imported equivalence and finite negative witness  
Related counterexample candidates: Issue #14

## Statement

Use D-0301 and define, for every integer `n>=1`,
\[
 \lambda_n=
 \frac{1}{(n-1)!}
 \left.\frac{d^n}{ds^n}\left[s^{n-1}\log\xi(s)\right]\right|_{s=1},
\]
where the analytic logarithm is taken near `s=1`.

Then RH is equivalent to
\[
 \lambda_n\ge0\qquad(n=1,2,\ldots).
\]
The original/standard zeta formulation is also commonly stated with strict
positivity; Bombieri--Lagarias state `lambda_n>0` for every `n`.  For this
project the unambiguous one-way implication is:

> If a rigorous enclosure proves `lambda_n<0` for one positive integer `n`,
> then RH is false.

With the standard symmetric zero-ordering convention,
\[
 \lambda_n=\sum_\rho\left[1-\left(1-\frac1\rho\right)^n\right],
\]
where zeros are counted with multiplicity.  This zero-side formula must not be
used with an arbitrary finite truncation.

## Sources

- Xian-Jin Li, *The Positivity of a Sequence of Numbers and the Riemann
  Hypothesis*, J. Number Theory 65 (1997), 325--333,
  DOI 10.1006/jnth.1997.2137.
- Enrico Bombieri and Jeffrey C. Lagarias, *Complements to Li's Criterion for
  the Riemann Hypothesis*, J. Number Theory 77 (1999), 274--287,
  DOI 10.1006/jnth.1999.2392.

Inspection level: Li publisher abstract; exact zeta formula and strict
positivity wording in the Bombieri--Lagarias publisher abstract; derivative
normalization cross-checked in later primary literature.

## Motivation

The witness consists of one index and one strict sign.  Independent evaluation
from the derivative definition and an arithmetic explicit formula gives a
strong error-detection architecture.

## Proof status

Imported theorem; proof not reproduced.

## Analytic/domain audit

- `xi(1)=1/2!=0`, so `log xi` has an analytic local branch.
- The derivative formula is branch-independent for derivatives of positive
  order once the local branch is fixed up to an additive constant; the
  displayed branch convention removes ambiguity.
- The zero sum is generally not absolutely convergent term-by-term and requires
  the source's symmetric limit.
- Multiplicity must be included.

## Dependency audit

L-0340 supplies only the unit-circle geometry, not the criterion.  Issue #14
must prove any recurrence, truncation, and ball arithmetic independently.

## Gap audit

- A negative truncated zero sum is not a negative `lambda_n`.
- Severe cancellation can make nominal precision meaningless.
- `>=0` versus `>0` does not affect a strict negative witness but must be
  handled precisely in theorem import.
- Computing coefficients of `xi` and coefficients of `log xi` are different
  operations.

## Remaining uncertainty

An independent reviewer should reconcile the nonnegative wording in Li's
Dedekind-zeta formulation with the strict-positive zeta wording in
Bombieri--Lagarias and record the strongest exact theorem.  The strict negative
disproof implication is unaffected.

## Suggested next attack

Claim Issue #14 and implement two independent interval evaluations with a
shared exact certificate schema but no shared numerical core.
