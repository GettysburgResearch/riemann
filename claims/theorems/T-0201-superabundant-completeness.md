Claim ID: T-0201
Title: Superabundant completeness of Robin counterexample search
Status: PROPOSED
Authoring agent: gpt56-02
Reviewing agents: none
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: Robin's 1984 criterion; L-0201; X-0202; X-0201 certificate engine
Scope: positive integers and Robin's inequality
Related counterexample candidates: none

## Statement

The following statements are equivalent:

1. The Riemann hypothesis is false.
2. There exists an integer \(n>5040\) such that
   \[
   \frac{\sigma(n)}n\ge e^\gamma\log\log n.
   \]
3. There exists a **superabundant** integer \(m>5040\) satisfying the same
   inequality.

Consequently, a search for a finite Robin counterexample is complete in
principle when restricted to superabundant numbers. This statement does not
justify restricting further to the colossally-abundant subsequence.

## Definitions

Set

\[
I(n)=\frac{\sigma(n)}n,
\qquad
R(n)=e^\gamma\log\log n.
\]

A positive integer \(m\) is superabundant if \(I(k)<I(m)\) for every
positive integer \(k<m\).

## Motivation

Experiment X-0201 scans the colossally-abundant spine, which is not known here
to contain every possible first Robin counterexample. T-0201 closes the safe
structural reduction at the larger superabundant class: no genuine Robin
counterexample can exist without a superabundant one.

## Proof or construction

Robin's theorem gives the equivalence of statements 1 and 2. Statement 3
implies statement 2 trivially. It remains to prove that statement 2 implies
statement 3.

Experiment X-0202 performs exact divisor-sum enumeration and obtains

\[
\max_{1\le k\le 5040} I(k)=I(5040)=\frac{403}{105},
\]

with 5040 the unique maximizer, and

\[
\max_{5041\le k\le 5582} I(k)=I(5460)=\frac{224}{65},
\]

with 5460 the unique maximizer.

The same experiment gives directed interval certificates for

\[
R(5041)>\frac{224}{65}
\]

and

\[
R(5583)>\frac{403}{105}.
\]

Since \(R(x)\) is strictly increasing for \(x>1\), every integer
\(5041\le n\le 5582\) satisfies

\[
I(n)\le \frac{224}{65}<R(5041)\le R(n),
\]

so no Robin counterexample lies in that finite window.

Now suppose \(n>5040\) is a Robin counterexample. The preceding paragraph
forces \(n\ge 5583\). Let \(m\le n\) be the least integer at which \(I\)
attains its maximum on \(\{1,\ldots,n\}\). Then

\[
I(m)\ge I(n)\ge R(n)\ge R(5583)>\frac{403}{105}.
\]

But every \(k\le5040\) has \(I(k)\le403/105\), so \(m>5040\). By L-0201,
\(m\) is superabundant and

\[
I(m)\ge R(n)\ge R(m).
\]

Thus \(m\) is a superabundant Robin counterexample, proving statement 3.

## Analytic domain audit

All logarithms are real natural logarithms at arguments greater than one.
There are no complex branches, contours, poles, zeros, or analytic
continuation steps. Monotonicity of \(R(x)\) follows from monotonicity of
\(\log\log x\) on \(x>1\).

## Dependency audit

- Robin's theorem is used only for the equivalence of statements 1 and 2.
- L-0201 supplies the least-record-maximizer conclusion.
- X-0202 supplies two exact finite maxima and two directed transcendental
  comparisons.
- X-0202 reuses the X-0201 Decimal interval engine.

## Gap audit

- The exact maxima are computationally enumerated; reviewers must inspect the
  divisor-sum sieve and independently reproduce the maxima.
- The transcendental signs inherit the CPython Decimal rounding dependency of
  X-0201 and require reproduction with an independent interval backend.
- `superabundant` must not be silently replaced by `colossally abundant`.
- The theorem reduces the search space but does not make it finite.
- No assumption about RH is used in the reduction from statement 2 to 3.

## Adversarial tests

- Recompute every \(\sigma(n)\) for \(1\le n\le5582\) with a separate
  factorization-based implementation.
- Verify the unique maxima at 5040 and 5460 by exact cross multiplication.
- Reproduce both strict transcendental inequalities with Arb or MPFI.
- Check the boundary integers 5040, 5041, 5582, and 5583 separately.
- Attempt to construct a non-superabundant violating integer and verify that
  the least earlier record maximizer supplied by the proof also violates.

## Remaining uncertainty

The logical reduction appears complete. Its status remains PROPOSED because the
finite certificate and Decimal transcendental enclosures have not been
independently reproduced.

## Suggested next attack

Enumerate superabundant prime-exponent vectors with a complete branch-and-bound
algorithm. Derive a rigorous upper bound on the largest possible future increase
of \(I(n)/R(n)\) from each partial exponent vector so that discarded subtrees
are accompanied by checkable certificates.
