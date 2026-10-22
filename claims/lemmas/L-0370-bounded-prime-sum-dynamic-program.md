# L-0370 — Bounded-prime-sum dynamic program

Claim ID: L-0370  
Title: Exact dynamic program for the maximal product of distinct primes  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: definition of `h(n)` in T-0311  
Scope: proof-producing finite kernel for Issue #16  
Related counterexample candidates: Deléglise--Nicolas arithmetic witnesses

## Statement

For an integer `n>=0`, let
\[
 h(n)=\max\left\{\prod_{p\in S}p:
    S\text{ is a finite set of primes and }\sum_{p\in S}p\le n\right\},
\]
where the empty product is `1`.

Let `p_1<...<p_r` be all primes at most `n`.  Define `H_0(s)=1` for
`0<=s<=n`.  For `1<=j<=r`, define
\[
 H_j(s)=
 \begin{cases}
  H_{j-1}(s),&0\le s<p_j,\\
  \max\{H_{j-1}(s),\,p_jH_{j-1}(s-p_j)\},&p_j\le s\le n.
 \end{cases}
\]
Then `H_j(s)` is exactly the largest product of a subset of
`{p_1,...,p_j}` whose sum is at most `s`, and
\[
 h(n)=H_r(n).
\]

A certificate may additionally store, for each selected state, whether the
maximum came from excluding or including `p_j`; backtracking yields an
optimizing prime set.

## Proof

We prove the interpretation of `H_j(s)` by induction on `j`.

For `j=0`, the only subset is empty.  Its sum is `0<=s` and its product is
`1`, so `H_0(s)=1` is correct.

Assume the claim for `j-1`.  Any admissible subset of
`{p_1,...,p_j}` either excludes `p_j` or includes it.

- If it excludes `p_j`, its product is at most `H_{j-1}(s)`.
- If it includes `p_j`, this is possible only when `s>=p_j`; removing `p_j`
  leaves a subset of the first `j-1` primes with sum at most `s-p_j`, whose
  product is at most `H_{j-1}(s-p_j)`.  Restoring `p_j` gives product at most
  `p_j H_{j-1}(s-p_j)`.

Both upper bounds are attained by the inductively optimal subsets, so their
maximum is exactly the optimum.  This proves the recurrence.

No prime larger than `n` can occur in a subset of sum at most `n`, so the list
`p_1,...,p_r` contains every possible factor.  Therefore `H_r(n)=h(n)`.  ∎

## Motivation

Issue #16 needs not merely a high-product subset but proof of global optimality.
This recurrence is an exact verifier kernel and a baseline against which safe
pruning can be tested.

## Analytic domain audit

None.  The dynamic program uses finite integer comparisons.

## Dependency audit

Only the definition of `h(n)` and induction are used.

## Gap audit

- A log-domain approximation can choose the wrong maximum near a tie.
- A scalable pruned search must prove that every discarded state is dominated.
- A claimed optimizing subset needs certified primality and a proof no prime
  was omitted.
- The `O(pi(n)n)` baseline is not proposed as a practical large-scale search;
  it is the correctness oracle for small instances and certificates.

## Adversarial tests

- Exhaustively enumerate all prime subsets for small `n` and compare.
- Force exact ties in a generic knapsack analogue and verify deterministic
  handling.
- Compare backtracked product, sum, and stored optimum.
- Validate every pruning optimization against the unpruned recurrence on
  overlapping ranges.

## Remaining uncertainty

The recurrence is complete.  The specialized scalable algorithms and compact
global-optimality certificates from the literature remain to be reconstructed.

## Suggested next attack

Implement a small exact verifier first; then derive Pareto-frontier dominance
and meet-in-the-middle certificates without replacing exact product ordering
by unbounded floating logarithms.
