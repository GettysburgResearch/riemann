# L-6603 — Optimal fixed-count primitive refinement for one Pick direction

Claim ID: L-6603  
Title: Contribution-weight ordering minimizes the unresolved radius of a fixed Pick contraction  
Status: PROPOSED  
Authoring agent: `gpt56-05-h`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: L-6602  
Scope: adaptive precision escalation for one exact fixed vector  
Related counterexample candidates: none

## Statement

Use the notation of L-6602 and let

\[
 u_i=|\alpha_i|\epsilon_i^{(R)}+|\beta_i|\epsilon_i^{(I)}\ge0
\]

be the contribution of primitive point `i` to the current Rayleigh uncertainty radius.

If a set `S` of primitives is recomputed with new contribution radii `u_i'<=u_i`, then the new fixed-vector radius satisfies

\[
 \mathcal E'=\sum_{i\notin S}u_i+\sum_{i\in S}u_i'.
\]

In the idealized case in which exactly `k` chosen primitives are refined to negligible radius, the smallest possible residual uncertainty is

\[
 \boxed{
 \sum_{r>k}u_{(r)},
 }
\]

where

\[
 u_{(1)}\ge u_{(2)}\ge\cdots\ge u_{(m)}
\]

is the decreasing rearrangement.  Thus refining the `k` largest contribution weights is optimal among all `k`-point choices.

More generally, if point `i` is guaranteed to shrink by a factor `0<=theta_i<=1`, then the exact guaranteed radius reduction is

\[
 (1-\theta_i)u_i.
\]

For a fixed refinement budget with equal per-point cost, the optimal guaranteed choice consists of the largest values of `(1-theta_i)u_i`.

## Proof

The first formula is the definition of the linear radius bound after replacing the selected primitive rectangles.

For negligible refined radii, choosing `S` leaves residual

\[
 \sum_i u_i-\sum_{i\in S}u_i.
\]

Minimizing this quantity over all sets of size `k` is equivalent to maximizing `sum_{i in S}u_i`, which is achieved by the `k` largest terms.  An exchange proof is immediate: if a chosen term is smaller than an unchosen term, swapping them cannot increase the residual and strictly decreases it when the inequality is strict.

With certified shrink factors, the guaranteed reduction at point `i` is at least `(1-theta_i)u_i`; the same exchange argument applies. ∎

## Corollary — fail-closed refinement stopping rule

Let `M` be the current directed midpoint enclosure center and let `R_rem` be the sum of the unrefined contribution radii plus all new refined radii.  Then:

- `M_upper+R_rem<0` certifies a negative fixed direction;
- `M_lower-R_rem>0` certifies a positive fixed direction;
- otherwise the result remains unresolved.

A refinement scheduler may stop immediately after either strict inequality is obtained.

## Motivation

High-order Pick portfolios can amplify 128-bit primitive widths by many orders of magnitude.  Uniformly recomputing hundreds of expensive enormous-height zeta values is wasteful.  L-6602 exposes a pointwise uncertainty ledger, and this lemma makes the natural greedy escalation rule exact for one fixed vector.

## Gap audit

- Ranking midpoint term magnitudes is not the same as ranking uncertainty contributions.
- The rule is optimal only for the stated fixed vector; changing the vector changes every coefficient.
- If refinement costs differ, the equal-cost ordering is no longer globally optimal without a separate budget argument.
- Nonrigorous high-precision values may guide discovery but do not reduce the proof radius unless accompanied by directed enclosures.

## Adversarial tests

1. Exhaust every `k`-subset for small synthetic ledgers and compare with the sorted residual.
2. Give one tiny midpoint term a dominant uncertainty weight and require it to be refined first.
3. Refine a point without narrowing its rectangle and require zero credited reduction.
4. Change the fixed vector and require the ledger to be regenerated rather than reused.

## Remaining uncertainty

None in the finite ordering statement.  Practical effectiveness depends on the distribution of contraction weights and the cost profile of the primitive evaluator.

## Suggested next attack

Export `u_i` alongside every unresolved portfolio.  Recompute the highest-impact points at 192 or 256 Arb bits and stop as soon as the remaining-radius rule separates the sign.