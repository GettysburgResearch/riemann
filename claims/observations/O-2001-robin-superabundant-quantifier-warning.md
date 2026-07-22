# O-2001 — Robin superabundance quantifier warning

Claim ID: O-2001  
Title: Do not replace a least- or existence-level superabundance statement by a claim about every Robin counterexample  
Status: PROPOSED  
Authoring agent: `gpt56-03-b`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: located sources `ChoieLichiardopolMoreeSole2007`, `Vojak2020`; T-0201; T-2001  
Scope: logical quantifiers in structural Robin reductions  
Related counterexample candidates: Robin finite witnesses

## Statement

The project must distinguish the following statements:

1. the **least** Robin counterexample, if one exists, is superabundant;
2. the **existence** of any Robin counterexample implies the existence of a superabundant Robin counterexample;
3. **every particular** Robin counterexample is superabundant.

Statements 1 and 2 have valid routes in the located literature and repository. Statement 3 must not be used: it does not follow from the record-maximizer argument, and the arXiv record for Choie--Lichiardopol--Moree--Solé explicitly says that an early version falsely asserted such a superabundance claim and thereby invalidated its proof.

The safe repository formulation is T-0201/T-2001: from any violating `n`, construct a possibly earlier superabundant violating record maximizer `m<=n`. No property of the original `n` is inferred.

## Evidence

- The arXiv page for `math/0604314`, revised 2006-09-07, records that version 1's main theorem falsely asserted the relevant `n` had to be superabundant; version 2 replaced that proof.
- Vojak's arXiv:2005.09307 states and proves structural properties of the **least** counterexample, including superabundance.
- T-0201 and T-2001 prove the weaker but sufficient existence implication through a least record maximizer.

Exact bibliographic and inspection details are in `literature/robin-structural-second-pass.md`.

## Motivation

This is not cosmetic wording. A branch-and-bound search can silently become incomplete if an existence theorem is misread as a pointwise characterization. The historical version correction shows that this exact mistake has already occurred in the literature.

## Proof or construction

The logical distinction is immediate. From

\[
 \forall n\,(V(n)\Rightarrow\exists m\le n\,[S(m)\land V(m)])
\]

one may conclude

\[
 (\exists n\,V(n))\Rightarrow(\exists m\,[S(m)\land V(m)]),
\]

but not

\[
 \forall n\,(V(n)\Rightarrow S(n)).
\]

Here `V` denotes violation and `S` superabundance. T-0201 constructs the existential `m`; it does not identify it with the input `n`. The located arXiv correction independently confirms that the stronger pointwise assertion cannot be treated as established. ∎

## Analytic domain audit

None. This is a quantifier and source-provenance audit.

## Dependency audit

The observation depends on the exact wording of the located arXiv version history and on the explicit construction in T-0201/T-2001.

## Gap audit

- This file does not claim that statement 3 is mathematically false by exhibiting an RH counterexample; none is known.
- It states that the assertion is unproved here, does not follow from the valid argument, and was explicitly withdrawn from a cited proof.
- Colossally abundant completeness is a separate question and is not inferred either way.

## Adversarial tests

- Rewrite every structural theorem with explicit quantifiers before using it to prune.
- Given a hypothetical nonrecord violating `n`, verify that T-0201 returns an earlier record `m` rather than claiming `n=m`.
- Reject issue or PR text that silently changes “there exists a superabundant counterexample” into “all counterexamples are superabundant.”

## Remaining uncertainty

The exact historical proposition in the original journal proof should still be independently read in full before any stronger attribution is made.

## Suggested next attack

Add an automated lint rule for theorem summaries containing `all`, `every`, `least`, or `exists`, requiring the claim card to repeat the full quantified statement.
