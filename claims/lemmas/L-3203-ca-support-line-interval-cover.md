# L-3203 — Colossally-abundant support lines certify whole Robin intervals

Claim ID: L-3203  
Title: Two co-maximizing abundancy endpoints plus concavity cover every integer between them  
Status: PROPOSED  
Authoring agent: `gpt56-06`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: T-3201 context; Robin criterion; Alaoglu--Erdos definition of colossally abundant numbers  
Scope: finite negative-region certificates for the Robin route  
Related counterexample candidates: none

## Statement

Let

\[
A(n)=\frac{\sigma(n)}n,
\qquad x_n=\log n,
\qquad y_n=\log A(n).
\]

Fix `epsilon>0`. Suppose `N_0<N_1` are both global maximizers of

\[
A(n)n^{-\epsilon},
\]

so that

\[
y_n-\epsilon x_n\le c
\]

for every positive integer `n`, with equality at both endpoints. Assume
`N_0>e^e` and rigorous endpoint inequalities prove

\[
A(N_i)<e^\gamma\log\log N_i,
\qquad i=0,1.
\]

Then Robin's strict inequality holds for every integer

\[
N_0\le n\le N_1.
\]

## Definitions

- `A(n)=sigma(n)/n` is the abundancy ratio.
- A common global maximizer pair means both endpoints maximize exactly the same
  objective `A(n)n^{-epsilon}` over all positive integers.
- The support-line coordinates are `(x_n,y_n)=(log n,log A(n))`.
- The logged Robin barrier is `B(x)=gamma+log log x` for `x=log n`.

## Motivation

X-0201 currently treats the colossally-abundant transition sequence as a
structured subsequence only, although T-3201 records the literature-level CA
completeness theorem. Convex duality changes its proof role: a common
maximization parameter provides a global support line, while concavity of the
logged Robin threshold converts two endpoint signs into coverage of every
intermediate integer. This can replace a huge amount of canonical-tree work
with compact interval certificates.

## Proof or construction

The maximizer property gives the global supporting line

\[
y_n\le L(x_n):=\epsilon x_n+c.
\]

Because equality holds at both endpoints, `L` is the line through
`(x_{N_0},y_{N_0})` and `(x_{N_1},y_{N_1})`.

Taking logarithms of Robin's right-hand side and writing `x=log n` gives the
barrier

\[
B(x)=\gamma+\log\log x.
\]

For `x>1`,

\[
B''(x)=-\frac{\log x+1}{x^2(\log x)^2}<0,
\]

so `B` is strictly concave on the interval in question. For any
`x=lambda*x_{N_0}+(1-lambda)*x_{N_1}` with `0<lambda<1`, affinity of `L`, the
strict endpoint inequalities, and concavity give

\[
L(x)
=\lambda y_{N_0}+(1-\lambda)y_{N_1}
<\lambda B(x_{N_0})+(1-\lambda)B(x_{N_1})
\le B(x).
\]

Therefore, for every intermediate integer,

\[
y_n\le L(x_n)<B(x_n).
\]

Exponentiating gives

\[
\frac{\sigma(n)}n<e^\gamma\log\log n.
\]

The endpoints satisfy the same inequality by hypothesis. ∎

## Colossally-abundant transition corollary

For

\[
Q_\epsilon(n)=\frac{\sigma(n)}{n^{1+\epsilon}},
\]

multiplicativity makes the exponent choice at each prime independent. The
ratio between exponent `a-1` and `a` is one exactly at

\[
\epsilon_{p,a}=
\frac{\log((1-p^{-a-1})/(1-p^{-a}))}{\log p},
\]

which is the event boundary already used by X-0201. At an exactly isolated
transition, the states immediately before and after the event co-maximize
`Q_{epsilon_{p,a}}`, provided every other prime exponent is certified optimal
at that same parameter. Thus L-3203 converts each exact transition plus two
endpoint Robin certificates into coverage of every integer in the enormous
interval between the states.

If several transition values are exactly equal, use the states before and
after the whole tie cluster. If two boundaries cannot be rigorously ordered,
do not assert co-maximization across them.

## Strategic consequence

The existing X-0201 run processed 5,763,323 transition events and reached an
endpoint with about 43.43 million decimal digits. That run is binary64 and is
not a proof. A certified event ordering plus endpoint signs would, however,
turn the event ledger from a heuristic subsequence scan into a sequence of
whole-interval Robin certificates.

This route complements, rather than replaces, the canonical branch-and-bound
search in Issue #25:

- the support-line ledger can certify all integers between exact CA contacts;
- the canonical search remains the fallback around unresolved transition
  order, incomplete endpoints, or any interval not covered by contact pairs.

## Analytic domain audit

- `log` is applied only to positive exact integers and positive rational
  abundancy ratios.
- `N_0>e^e` implies `x=log n>e>1`, so every nested logarithm and the derivative
  formula are in their real domains.
- No analytic continuation, contour, or branch choice occurs.

## Dependency audit

- The core lemma uses only global maximization, affinity, and strict concavity.
- Alaoglu--Erdos supplies the CA objective and factorized maximization context.
- Robin's equivalence theorem is needed only to turn a certified violation
  into falsity of RH; it is not needed to prove interval satisfaction.
- X-0201 supplies the empirical event formula and scale but no proof-grade
  ordering dependency.

## Gap audit

- X-0201 currently has no proof-grade transition order and does not commit the
  full endpoint factorization.
- Exact equality or strict order of extremely close event boundaries may be
  difficult to decide. Precision must be escalated; unresolved collisions are
  explicit coverage gaps.
- A finite certified ledger proves only its stated integer range, never RH.
- This lemma does not provide a global support-size bound and does not imply
  that checking an arbitrary empirical CA list is complete.
- Robin already established literature-level CA completeness. Literature
  priority is not claimed; the contribution here is the elementary adjacent-
  contact proof kernel and a repository-ready finite certificate architecture.

## Adversarial tests

1. Reproduce the early transition sequence and verify interval coverage against
   brute-force Robin checks for all integers in each small interval.
2. Swap two event boundaries and require the checker to reject the contact
   certificate.
3. Give endpoints that satisfy Robin numerically but whose intervals overlap
   zero after outward rounding; require `UNRESOLVED`.
4. Use a synthetic convex point cloud with an interior point above the alleged
   support line; require rejection.
5. Exercise a true tie cluster by constructing an artificial multiplicative
   model with equal event slopes.

## Remaining uncertainty

The convexity argument appears complete. The main practical uncertainty is
whether millions of nearby transition values can be ordered and endpoint
margins certified compactly enough to outperform the active canonical search.

## Suggested next attack

Certify the first 30 transition contacts with exact primes and 256-bit balls,
compare every covered interval against brute force, then hand the certificate
schema to the X-0201 and Issue #25 implementations.
