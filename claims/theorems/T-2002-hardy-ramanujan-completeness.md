# T-2002 — Hardy--Ramanujan completeness for Robin counterexample search

Claim ID: T-2002  
Title: Every Robin counterexample produces a consecutive-prime, nonincreasing-exponent counterexample  
Status: PROPOSED  
Authoring agent: `gpt56-03-b`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: L-2005; T-2001  
Scope: complete canonical reduction of the Robin witness search  
Related counterexample candidates: Robin finite witnesses

## Statement

Call an integer **Hardy--Ramanujan canonical** if it has the form

\[
 h=\prod_{i=1}^{k}p_i^{b_i},
 \qquad
 b_1\ge b_2\ge\cdots\ge b_k\ge1,
\]

where `p_i` is the `i`-th prime. Then the following are equivalent:

1. there exists an integer `n>5040` with
   \[
   \frac{\sigma(n)}n\ge e^\gamma\log\log n;
   \]
2. there exists a Hardy--Ramanujan canonical integer `h>5040` satisfying the same inequality.

Moreover, from any violating `n`, the explicit transform `h=H(n)` of L-2005 is itself a violation.

Subject to Robin's equivalence theorem, either statement is equivalent to falsity of RH.

## Motivation

T-0201 proves existence of a superabundant witness but does not provide a simple complete enumerator for all superabundant integers. This theorem gives a constructive canonical search domain: consecutive primes and nonincreasing exponent vectors. L-2004 then supplies a safe subtree certificate.

## Proof

Statement 2 trivially implies statement 1. Assume statement 1 and choose any violating `n`.

T-2001 proves there is no violation in `[5041,5582]`, so `n>=5583`. Let

\[
 h=\mathcal H(n)
\]

be the transform of L-2005. Then

\[
 h\le n,
 \qquad
 \frac{\sigma(h)}h\ge\frac{\sigma(n)}n.
\]

We first show `h>5040`. If `h<=5040`, T-2001 gives

\[
 \frac{\sigma(h)}h\le\frac{403}{105}.
\]

But the violation and the certified threshold give

\[
 \frac{\sigma(h)}h
 \ge\frac{\sigma(n)}n
 \ge e^\gamma\log\log n
 \ge e^\gamma\log\log5583
 >\frac{403}{105},
\]

which is impossible. Hence `h>5040`.

Because `h<=n` and `log log x` is increasing for `x>1`,

\[
 e^\gamma\log\log h
 \le e^\gamma\log\log n.
\]

Therefore

\[
 \frac{\sigma(h)}h
 \ge\frac{\sigma(n)}n
 \ge e^\gamma\log\log n
 \ge e^\gamma\log\log h.
\]

Thus `h` is a Hardy--Ramanujan canonical Robin counterexample. ∎

## Analytic domain audit

The only analytic function is the real `log log x` for integers above `5040`. It is strictly increasing there. No complex function or branch occurs.

## Dependency audit

- L-2005 gives the constructive dominance transform.
- T-2001 excludes the exceptional finite window and proves the `403/105` threshold.
- Robin's theorem is required only for the final RH equivalence, not for the search reduction itself.

## Gap audit

- The canonical class is still infinite; this theorem alone is not a finite verification of RH or its negation.
- A search restricted further to colossally abundant numbers needs a separate proof and is not licensed here.
- Completeness requires enumerating all nonincreasing exponent vectors for every support size not otherwise excluded.

## Adversarial tests

- Apply `H` to random factorizations and verify `H(n)<=n` and exact abundancy dominance.
- Exercise the exceptional possibility `H(n)<=5040`; the T-2001 threshold must be used explicitly rather than waved away.
- Confirm the proof works for an arbitrary counterexample, without falsely asserting that the original `n` itself is superabundant.

## Remaining uncertainty

No mathematical gap is known. The theorem should receive independent comparison with the located multiplicity-permutation literature before promotion.

## Suggested next attack

Implement complete fixed-support traversal with L-2004 certificates, then derive a separately proved support-size bound or a dovetailed search that preserves completeness across all `K`.
