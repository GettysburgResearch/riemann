# Agent report addendum — complete superabundant reduction

Agent: gpt56-02  
Issue: #2  
Branch: `agent/gpt56-02/2-robin-witness-search`  
Date: 2026-07-22

## Starting hypothesis

The first X-0201 report identified a central gap: a CA scan is not a complete
search of all possible Robin counterexamples. The follow-up hypothesis was that
L-0201's finite exceptional case could be closed exactly, yielding a complete
reduction to superabundant numbers.

## Approaches attempted

1. Enumerated exact divisor sums through 5582.
2. Located exact abundancy maxima on 1–5040 and 5041–5582.
3. Reused the directed-decimal verifier to isolate two strict comparisons.
4. Combined the finite certificate with L-0201.

## New results

- X-0202 exactly finds `403/105` at 5040 as the unique maximum through 5040.
- X-0202 exactly finds `224/65` at 5460 as the unique maximum on 5041–5582.
- Directed intervals certify
  `R(5041) > 224/65` and `R(5583) > 403/105`.
- T-0201 (PROPOSED): RH is false iff a superabundant integer above 5040 violates
  Robin's inequality.

## Candidate counterexamples

None.

## Certified computations

The finite maxima use exact integers. The two transcendental signs use the
X-0201 directed-decimal engine. Four new tests pass and signs are stable under
precision changes.

## Failed approaches

No mathematical dead end occurred in this addendum. The CA-only completeness
idea remains rejected: T-0201 does not reduce all counterexamples to CA numbers.

## Potential errors

- Independent exact enumeration is still needed.
- The Decimal interval backend needs Arb/MPFI reproduction.
- The boundary value 5583 is close enough to the threshold that directed
  rounding must be audited carefully.

## Files changed

- `claims/theorems/T-0201-superabundant-completeness.md`
- `experiments/X-0202-robin-finite-barrier/*`
- this report

## Claims affected

- T-0201 — added, status PROPOSED
- X-0202 — added, certified computation pending independent reproduction

## Recommended next actions

Develop a complete superabundant exponent-vector enumerator with proof-carrying
branch pruning. The immediate technical target is an upper bound on the maximum
possible abundancy gain from unassigned primes, compared against the monotone
Robin denominator.

## Organizational improvement ideas

When an empirical search uses a proper subsequence of a rigorously justified
search class, require the experiment README to name both classes explicitly and
state the missing completeness implication.
