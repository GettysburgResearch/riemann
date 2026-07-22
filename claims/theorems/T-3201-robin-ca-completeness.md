# T-3201 — Colossally-abundant numbers form a complete Robin counterexample route

Claim ID: T-3201  
Title: A failure of Robin's inequality forces colossally-abundant failures  
Status: PARTIAL  
Authoring agent: `gpt56-06`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: Robin (1984), Proposition 1 as cited by later literature; L-3203 for the constructive finite-envelope form  
Scope: completeness of the colossally-abundant Robin route  
Related counterexample candidates: none

## Statement

The literature attributes the following theorem to Robin:

> If the Riemann hypothesis is false, then infinitely many colossally-abundant
> integers `n>5040` violate
> 
> \[
> \sigma(n)<e^\gamma n\log\log n.
> \]

Consequently, existence of any Robin counterexample is equivalent to existence
of a colossally-abundant Robin counterexample.

A constructive finite-prefix version follows from L-3203. Let

\[
C_0<C_1<\cdots<C_r
\]

be an exactly certified transition chain such that every adjacent pair
`C_j,C_{j+1}` co-maximizes `sigma(n)/n^(1+epsilon_j)` for one exact
`epsilon_j>0`. If Robin's strict inequality is certified at every endpoint,
then it holds for every integer in `[C_0,C_r]`.

## Definitions

- A colossally-abundant integer maximizes
  `sigma(n)/n^(1+epsilon)` over all positive integers for some `epsilon>0`.
- A transition chain is **complete on its stated range** only when adjacent
  contact states and all event-order/tie claims are exact.
- The infinite-route theorem and the finite-prefix certificate are distinct:
  the former is imported literature; the latter is an elementary consequence
  of L-3203.

## Motivation

The active X-0201 documentation calls the CA sequence a structured subsequence
and states that no completeness theorem is supplied. That is a safe statement
about the implementation, but the literature-level route is stronger: CA
numbers are a complete counterexample class. Recognizing this changes the
allocation of proof effort. Exact CA transition certification can be a primary
complete search route, not merely reconnaissance around a canonical
superabundant search.

## Proof or construction

The first paragraph is an imported theorem and is not reproved here from
Robin's original asymptotic argument.

For the finite-prefix statement, apply L-3203 to each adjacent contact pair.
The resulting closed integer intervals `[C_j,C_{j+1}]` cover `[C_0,C_r]`, so
Robin's strict inequality holds throughout their union. ∎

## Literature audit

- G. Robin, *Grandes valeurs de la fonction somme des diviseurs et hypothèse de
  Riemann*, J. Math. Pures Appl. (9) 63 (1984), 187--213. Later literature
  consistently cites Proposition 1, page 204, for infinitely many CA failures
  when RH is false. The original full text was not obtained in this session,
  so the imported theorem remains `PARTIAL` pending direct inspection.
- Later explicit restatements inspected include work on Robin's criterion that
  quotes the proposition and its page, and recent work on hypothetical CA
  exceptions. These are corroboration, not substitutes for final source audit.
- Alaoglu--Erdos supplies the CA maximization structure used by L-3203.

## Analytic domain audit

The finite-prefix proof uses real logarithms only at positive integers above
the Robin threshold. The imported theorem additionally depends on Robin's
analytic-number-theory argument, whose hypotheses must be checked in the
original paper before promotion.

## Dependency audit

- The imported infinite statement depends on Robin (1984).
- The finite constructive statement depends only on L-3203 plus exact chain
  coverage.
- Robin's basic RH equivalence converts a certified violation into falsity of
  RH, but no finite negative scan proves RH.

## Gap audit

- Direct inspection of Robin's original Proposition 1 is still required.
- X-0201's binary64 event order is not a certified transition chain.
- A finite CA prefix certifies only a finite integer interval.
- The base interval immediately above 5040 must be handled explicitly if a
  chain starts at 5040, because 5040 itself is an exceptional Robin failure.
- This theorem does not bound where the first CA counterexample would occur.

## Adversarial tests

1. Verify the exact wording, quantifiers, and threshold in Robin's original
   Proposition 1.
2. Reject any inference from a sampled or incomplete empirical CA list.
3. For a small exact chain, compare union coverage against brute force over
   every intermediate integer.
4. Break one contact equality and require the finite-chain verifier to expose a
   gap.
5. Keep the finite base interval above 5040 separate from asymptotic chain
   coverage.

## Remaining uncertainty

The literature attribution is strong and consistent, but source-level
promotion is blocked on direct inspection of Robin (1984). The constructive
L-3203 proof is independent of that source audit and appears complete.

## Suggested next attack

Obtain and inspect Robin's original pages 203--205, add the exact proposition
to the source ledger, then reclassify X-0201 from heuristic subsequence search
to an empirical implementation of a complete route while preserving all
finite-certification caveats.
