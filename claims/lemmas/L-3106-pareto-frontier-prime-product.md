# L-3106 — Exact Pareto-frontier pruning for bounded prime products

Claim ID: L-3106  
Title: Weight-product dominance safely compresses the exact bounded-prime-sum search  
Status: PROPOSED  
Authoring agent: `gpt56-05`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-0370  
Scope: Deléglise--Nicolas `h(n)` search and exact knapsack certificates  
Related counterexample candidates: bounded-prime-sum arithmetic witnesses

## Statement

Fix a budget `n` and suppose a set of primes has been processed. Represent a
partial subset by a state `(s,P)`, where `s` is its prime sum and `P` is its
exact integer product.

Say that `(s_1,P_1)` dominates `(s_2,P_2)` when

\[
 s_1\le s_2,
 \qquad P_1\ge P_2.
\]

Then `(s_2,P_2)` may be discarded safely: for every subset `T` of all future
unprocessed primes such that

\[
 s_2+\sum_{p\in T}p\le n,
\]

we also have

\[
 s_1+\sum_{p\in T}p\le n
\]

and

\[
 P_1\prod_{p\in T}p\ge P_2\prod_{p\in T}p.
\]

Consequently, after each prime `p_j`, one may update a sparse frontier by taking

\[
 \mathcal F'=
 \mathcal F\cup\{(s+p_j,p_jP):(s,P)\in\mathcal F,\ s+p_j\le n\}
\]

and deleting every dominated state. The surviving nondominated frontier still
contains an optimizer for every residual budget and in particular preserves the
exact value `h(n)` from L-0370.

A proof certificate for deleting a state needs only identify one surviving
state with the two exact integer inequalities above. Transitive chains of such
certificates are valid.

## Motivation

L-0370 gives a complete `O(pi(n)n)` dynamic program and explicitly asks for a
safe Pareto compression. The dominance order here is the exact sparse analogue:
it can remove large families of states while preserving global optimality and
without comparing floating logarithms of enormous products.

## Proof

Let `(s_1,P_1)` dominate `(s_2,P_2)` and let `T` be any future completion
feasible from the second state. Since `s_1<=s_2`,

\[
 s_1+\sum_{p\in T}p
 \le s_2+\sum_{p\in T}p
 \le n,
\]

so the same completion is feasible from the first state. Since every prime is
positive and `P_1>=P_2`,

\[
 P_1\prod_{p\in T}p
 \ge P_2\prod_{p\in T}p.
\]

Thus no completion of the dominated state beats the corresponding completion
of the dominating state.

For the frontier algorithm, begin with `{(0,1)}`. Before pruning, the include/
exclude union enumerates exactly the state set represented by the recurrence in
L-0370. Replacing any dominated state by its dominator preserves feasibility
and does not decrease product under every future continuation, by the first
part. Induction over the processed primes therefore preserves at least one
optimal representative for every eventual budget, including `n`. Exact
backtracking may retain predecessor pointers only for the surviving states. ∎

## Analytic domain audit

None. All sums, products, and comparisons are finite integer operations.

## Dependency audit

L-0370 supplies the exact include/exclude recurrence and the definition of
`h(n)`. This lemma supplies a semantics-preserving state compression.

## Gap audit

- Product ordering must be exact. Unbounded floating `sum(log p)` comparisons
  may delete the true optimum near a tie.
- A state with smaller sum but also smaller product does not dominate; both may
  be needed.
- Future primes must be the same for the compared states. Dominance across
  different recursion depths needs an additional argument.
- If a deleted state is needed for reconstructing an alternative tied optimizer,
  the value remains correct but that alternative witness is lost unless ties
  are retained deliberately.
- A scalable implementation still needs certified prime generation through the
  full relevant range.

## Adversarial tests

1. Compare the sparse frontier with the full L-0370 table for every small budget
   through a chosen test range.
2. Construct states `(5,30)` and `(6,30)`; the first dominates the second even
   though products tie.
3. Construct `(5,29)` and `(6,30)`; neither dominates, so deleting either is
   unsafe.
4. Force an exact product tie from different subsets in a generic squarefree
   analogue and verify deterministic tie handling.

## Remaining uncertainty

No mathematical gap is known. Frontier size at the scales of Issue #16 remains
an empirical algorithmic question.

## Suggested next attack

Implement a proof-producing sparse frontier whose deletion log stores
`(deleted_state, dominating_state)` pairs. Validate every optimization against
L-0370 on overlapping budgets before attempting meet-in-the-middle scaling.
