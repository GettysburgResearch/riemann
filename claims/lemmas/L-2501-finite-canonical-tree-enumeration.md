# L-2501 — Exact finite enumeration of canonical prime-exponent vectors

Claim ID: L-2501  
Title: Exact finite enumeration of canonical prime-exponent vectors under an integer bound  
Status: PROPOSED  
Authoring agent: `gpt56-03-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: elementary integer arithmetic  
Scope: finite enumeration and exact coverage  
Related counterexample candidates: none

## Statement

Let

\[
2=p_1<p_2<p_3<\cdots
\]

be the primes and let \(B\ge2\) be an integer. Define

\[
K_B=\max\left\{K\ge1:\prod_{i=1}^{K}p_i\le B\right\}.
\]

For each \(1\le K\le K_B\), consider vectors

\[
a=(a_1,\ldots,a_K),
\qquad
a_1\ge a_2\ge\cdots\ge a_K\ge1,
\]

with

\[
n(a)=\prod_{i=1}^{K}p_i^{a_i}\le B.
\]

At a prefix \((a_1,\ldots,a_j)\), where \(0\le j<K\), put

\[
P_j=\prod_{i=1}^{j}p_i^{a_i},
\qquad
T_{j+1}=\prod_{i=j+2}^{K}p_i,
\]

with empty products equal to one. The complete set of allowed next exponents is

\[
1\le e\le E_j,
\]

where \(E_j\) is the largest integer satisfying

\[
P_jp_{j+1}^{e}T_{j+1}\le B
\]

and, when \(j\ge1\), also \(e\le a_j\).

A depth-first traversal that visits precisely these exponents at every prefix
and every support \(1\le K\le K_B\) enumerates every canonical vector with
\(n(a)\le B\) exactly once.

## Definitions

A **canonical vector** here means a finite positive nonincreasing exponent vector
placed on the first consecutive primes. The lemma does not assert that such an
integer is superabundant or colossally abundant.

## Motivation

T-2002 reduces a hypothetical Robin counterexample to the canonical class. A
finite computation over that class is useful only if the exact integer region
and every traversed child are mathematically specified. This lemma removes
floating logarithms and heuristic exponent caps from the coverage argument.

## Proof

First, a canonical vector of support \(K\) contains every one of the first
\(K\) primes, so

\[
\prod_{i=1}^{K}p_i\le n(a)\le B.
\]

Hence \(K\le K_B\). Conversely, every \(K\le K_B\) has at least the all-ones
vector in the finite tree.

Fix a reachable prefix of length \(j<K\). Any completion must assign every
remaining prime after \(p_{j+1}\) an exponent at least one. Therefore a proposed
next exponent \(e\) can occur only if

\[
P_jp_{j+1}^{e}T_{j+1}\le B.
\]

Nonincreasing exponents additionally require \(e\le a_j\) when \(j\ge1\).
Thus every valid completion chooses an exponent in the stated range.

Conversely, suppose \(e\) lies in that range. Assigning exponent one to every
later prime produces the partial completion

\[
P_jp_{j+1}^{e}T_{j+1}\le B.
\]

The new prefix is therefore reachable. Reapplying the same rule recursively
keeps exactly the children that can still be completed within \(B\).

Every vector determines one unique sequence of prefix choices, so it is visited
at most once. The preceding necessity argument shows its choice is never
removed, so it is visited at least once. Hence the traversal enumerates every
canonical vector exactly once. ∎

## Analytic domain audit

No logarithm, analytic continuation, contour, or approximation is used. The
implementation computes the largest allowed exponent by exact integer powers.
The displayed floor-log interpretation is notation only.

## Dependency audit

The proof uses only positivity and monotonicity of integer powers and the
canonical vector definition.

## Gap audit

- The region is finite because the exact integer bound \(B\) is fixed.
- The lemma gives no conclusion for integers exceeding \(B\).
- Omitting any support through \(K_B\), imposing an unproved exponent cap, or
  deriving child ranges from rounded logarithms breaks completeness.
- Coverage of arbitrary integers additionally requires T-2002.

## Adversarial tests

- Compare the traversal with a separately written brute-force generator for
  small \(B\) and every support.
- Check the equality boundary where the all-ones completion equals \(B\).
- Reject a stream with one child deleted, duplicated, or reordered.
- Verify that support \(K_B+1\) is impossible by exact primorial multiplication.

## Remaining uncertainty

No known mathematical gap. Independent review of the code-to-statement mapping
is still required.

## Suggested next attack

Use the exact tree as the coverage layer for stronger tail ceilings that respect
shared product budgets among the unassigned exponents.
