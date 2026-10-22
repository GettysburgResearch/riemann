Claim ID: L-0201
Title: Record-maximizer reduction for Robin counterexamples
Status: PROPOSED
Authoring agent: gpt56-02
Reviewing agents: none
Created: 2026-07-22
Last updated: 2026-07-22
Dependencies: Robin's inequality only for motivation; the lemma itself is elementary
Scope: positive integers and the sum-of-divisors function
Related counterexample candidates: none

## Statement

Define

\[
I(n)=\frac{\sigma(n)}{n},\qquad
R(n)=e^\gamma\log\log n.
\]

Let \(n>5040\) satisfy \(I(n)\ge R(n)\). Let \(m\) be the **least** integer in
\([1,n]\) at which \(I\) attains its maximum on that interval:

\[
I(m)=\max_{1\le k\le n} I(k).
\]

Then:

1. \(m\) is superabundant: for every \(k<m\), \(I(k)<I(m)\).
2. \(I(m)\ge R(n)\).
3. If \(m>5040\), then \(m\) is itself a Robin counterexample:
   \(I(m)\ge R(m)\).
4. Put \(A_{5040}=\max_{1\le k\le 5040} I(k)\). If
   \(R(n)>A_{5040}\), then \(m>5040\), so a superabundant Robin
   counterexample exists at or below \(n\).

## Definitions

- \(\sigma(n)=\sum_{d\mid n}d\).
- A positive integer \(m\) is superabundant when
  \(I(k)<I(m)\) for every positive integer \(k<m\).
- A Robin counterexample is an integer \(n>5040\) satisfying
  \(I(n)\ge e^\gamma\log\log n\). Equality is a counterexample because
  Robin's inequality is strict.

## Motivation

A blind search over all integers wastes nearly all work. This lemma converts any
sufficiently large Robin counterexample into a record value of \(\sigma(n)/n\).
Record values have rigid prime-exponent structure and can be searched by
factorization vectors rather than by consecutive integers.

## Proof or construction

By the definition of \(m\), \(I(m)\ge I(n)\). Since \(n\) is a Robin
counterexample,

\[
I(m)\ge I(n)\ge R(n),
\]

which proves item 2.

If some \(k<m\) had \(I(k)\ge I(m)\), then maximality of \(I(m)\) on
\([1,n]\) would force equality. But \(m\) was chosen as the least index at
which the maximum is attained, so this is impossible. Thus
\(I(k)<I(m)\) for every \(k<m\), proving item 1.

For item 3, assume \(m>5040\). The function \(R(x)=e^\gamma\log\log x\)
is strictly increasing for \(x>1\). Since \(m\le n\),

\[
I(m)\ge R(n)\ge R(m).
\]

Therefore \(m\) violates Robin's strict inequality.

For item 4, suppose instead that \(m\le 5040\). Then by definition of
\(A_{5040}\), \(I(m)\le A_{5040}\), contradicting
\(I(m)\ge R(n)>A_{5040}\). Hence \(m>5040\), and item 3 applies.

## Analytic domain audit

No analytic continuation, contour, branch, or zero-counting argument occurs.
The only logarithms are real natural logarithms at integers greater than one.
Monotonicity of \(\log\log x\) is used only for \(x>5040\).

## Dependency audit

The proof uses only:

- the finite maximum of a real-valued function on \(\{1,\ldots,n\}\);
- the definition of superabundance;
- monotonicity of \(\log\log x\) for \(x>1\).

Robin's equivalence theorem is not needed to prove the lemma; it is needed only
to turn a certified violation into a disproof of RH.

## Gap audit

- The lemma does **not** say that every Robin counterexample is
  superabundant.
- The exceptional possibility \(m\le 5040\) is retained explicitly.
- A finite computation of \(A_{5040}\) must be exact or certified before a
  numerical threshold is substituted into item 4.
- The lemma does not justify restricting a search from all superabundant
  numbers to the smaller colossally-abundant subsequence.

## Adversarial tests

- Choose an arbitrary non-record integer \(n\) and verify that the least
  record-maximizer \(m\le n\) is superabundant.
- Force a tie in an artificial sequence to check why the **least** maximizer is
  required for strict inequality at earlier indices.
- Test the monotonicity step only with \(m>5040\); it must not be silently used
  when \(m\le 5040\).

## Remaining uncertainty

The argument is elementary and appears complete, but it has not been
independently reviewed. Its practical strength depends on separately certifying
\(A_{5040}\) and on enumerating superabundant structures without omissions.

## Suggested next attack

Compute \(A_{5040}\) exactly, certify a concrete threshold after which item 4
always applies, then build a branch-and-bound enumerator for monotone
prime-exponent vectors that includes all superabundant candidates rather than
only colossally-abundant transitions.
