# L-6601 — Exact feasible anchors obstruct every finite dual witness portfolio

Claim ID: L-6601  
Title: A rational point inside the rigorous feature enclosure and the RH-admissible finite cone rules out every robustly negative dual portfolio  
Status: PROPOSED  
Authoring agent: `gpt56-06-d`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: D-4501, D-5701, L-5701, and the route-specific nonnegativity gates attached to the finite row library  
Scope: proof-grade `xi'/xi` feature tables and any finite collection of RH-valid scalar or PSD constraints  
Related counterexample candidates: none

## Statement

Let `C` be a nonempty rigorous enclosure of one finite primitive feature vector

\[
 y\in\mathbb R^n.
\]

Let the declared RH-admissible finite region be

\[
 \mathcal K=\{y:q_i(y)\ge0\ (1\le i\le m),\ K_r(y)\succeq0\ (1\le r\le R)\},
\]

where every scalar function `q_i` and Hermitian matrix function `K_r` has exact finite semantics and an explicit logical gate proving its displayed sign under RH. The scalar functions need not be affine for the obstruction below, although the exact portfolio checker normally uses affine rows after contraction.

Suppose an exact rational or dyadic point `y_0` is accompanied by finite exact certificates proving

\[
 y_0\in C,
 \qquad
 q_i(y_0)\ge0\quad(1\le i\le m),
 \qquad
 K_r(y_0)\succeq0\quad(1\le r\le R).
 \tag{1}
\]

Then no exact dual portfolio which is nonnegative on `K` can be uniformly negative on `C`.

More explicitly, let

\[
 P(y)=\sum_i\lambda_iq_i(y)+
 \sum_r\operatorname{tr}(W_rK_r(y)),
 \qquad
 \lambda_i\ge0,\quad W_r\succeq0.
 \tag{2}
\]

Then

\[
 \sup_{y\in C}P(y)\ge P(y_0)\ge0.
 \tag{3}
\]

Consequently:

1. there is no uncertainty-robust conic separator on the declared finite table;
2. there is no positive score moat or feature-repair moat for such a separator;
3. an LP, SDP, eigensolver, or interval computation reporting a strictly negative robust portfolio over the same `C` and constraint semantics must contain a reconstruction, enclosure, manifest, or logical-gate error.

If the feature table decomposes into disjoint height blocks

\[
 C=C_1\times\cdots\times C_h
\]

and every constraint is supported in one declared block, exact anchors in all blocks concatenate into one exact global anchor. If only a subset of blocks has anchors, every possible robust separator must use at least one unanchored block after exact coefficient contraction.

## Exact PSD anchor formats

For a rational symmetric or Hermitian matrix, any one of the following finite objects is sufficient when its hypotheses are checked exactly:

- an exact `LDL^*` factorization with every diagonal pivot positive;
- an exact Gram factorization;
- exact nonnegative principal minors together with an appropriate semidefinite criterion;
- a separately proved exact structural factorization.

A floating eigenvalue is not an anchor certificate.

## Proof

By (1), `y_0` lies in `C` and every scalar term in (2) is nonnegative at `y_0`. For each matrix term, write an exact Gram representation

\[
 W_r=\sum_\ell \alpha_{r,\ell}v_{r,\ell}v_{r,\ell}^{*},
 \qquad \alpha_{r,\ell}\ge0.
\]

Then

\[
 \operatorname{tr}(W_rK_r(y_0))
 =\sum_\ell\alpha_{r,\ell}
   v_{r,\ell}^{*}K_r(y_0)v_{r,\ell}\ge0
\]

because `K_r(y_0)` is positive semidefinite. Hence `P(y_0)>=0`. Since `y_0 in C`, the supremum over `C` is at least this value, proving (3).

For the block statement, concatenate the exact block anchors. Every block-supported constraint sees exactly its own feasible component, so the concatenated point belongs to the global finite admissible region. The first part applies. If a proposed portfolio uses only anchored blocks, restrict the concatenated point to those blocks and obtain the same contradiction. ∎

## Application to the Issue #39 value table

At one exact ordinate `T`, the primitive coordinates are the real parts

\[
 R_j=\operatorname{Re}\frac{\xi'}{\xi}
 \left(\frac12+x_j+iT\right)
\]

for the eight dyadic offsets on the PR #56 ladder. The current exact anchor replay checks:

1. each rational midpoint belongs to the intersection of the two directed Arb assemblies;
2. all scalar rows are nonnegative;
3. every pairwise `A` and `B`/secant row is nonnegative;
4. every alternating divided difference on every node subset is nonnegative;
5. the full same-height Pick matrix is exactly positive definite by rational `LDL^T` pivots;
6. hence every fixed Pick vector, barycentric vector, matched-pole vector, and exact PSD Gram multiplier is nonnegative;
7. every enumerated cross-Loewner minor on disjoint increasing node lists through the maximal possible order is nonnegative.

Items 5–6 mean that an infinite search over exact Pick vectors or PSD multipliers is closed at that block by one finite rational factorization; it is not merely a sampled vector search.

## Analytic domain audit

This lemma is finite convex and linear algebra. It introduces no analytic continuation, zero sum, interchange of limits, contour, or special-function evaluation. Every imported `xi'/xi` nonnegativity condition retains its own normalization and analytic-domain gate.

## Dependency audit

- D-4501 supplies the uncertainty-set and strict-moat semantics.
- D-5701 and L-5701 supply the dual scalar/PSD portfolio interface.
- The exact feature enclosure is produced by the directed Arb pipeline of Issue #39.
- Scalar, divided-difference, Pick, barycentric, matched-pole, and Loewner rows retain the dependencies stated in their own claim files.

No imported dependency is promoted by this lemma.

## Gap audit

- The anchor must lie in the **same joint uncertainty set** used by the portfolio. Coordinatewise midpoint membership is sufficient for a Cartesian product of primitive intervals, but not for a narrower correlated set unless joint membership is separately proved.
- Semantic duplicate features must share one coordinate. An anchor for a falsely duplicated independent table does not certify the intended model.
- Exact positive definiteness of a midpoint Pick matrix does not prove the true Pick matrix positive; it proves only that the uncertainty box intersects the PSD cone, which is exactly the obstruction needed here.
- Failure to find an anchor does not prove that a separator exists.
- A finite-table obstruction says nothing about untested heights, offsets, derivative features, or a richer admissible family.
- Jet-only differential and shifted-Stieltjes conditions are not silently inferred from a value-only table. They require proof-grade derivative features or derivative-free replacements.

## Adversarial tests

1. Use `C=[-1,1]` and the RH-valid row `q(y)=y`; the anchor `y_0=0` must rule out every nonnegative multiple as a strict negative separator.
2. Use an interval box whose midpoint matrix has one negative exact `LDL` pivot; the checker must refuse the PSD anchor rather than repair it numerically.
3. Duplicate one primitive feature under two IDs with opposite coefficients; manifest checking must reject the false cancellation.
4. Replace a Cartesian box by a correlated polytope excluding the midpoint; coordinatewise membership must no longer be accepted.
5. Mutate one exact row coefficient and require the anchor replay to expose a negative row or a reconstruction mismatch.

## Remaining uncertainty

The lemma is elementary. The live uncertainty is whether every current 128-bit anchor failure disappears under a higher-precision primitive table, or whether one block instead admits a genuine robust separator.

## Suggested next attack

Escalate only the unanchored height blocks and their tightest exact rows to 256–512-bit directed evaluation. After each escalation, either:

- emit a rational feasible-anchor certificate, permanently closing every dual portfolio supported on that block; or
- emit a strict robust negative portfolio and immediately begin independent special-function reproduction and parent-gate review.
