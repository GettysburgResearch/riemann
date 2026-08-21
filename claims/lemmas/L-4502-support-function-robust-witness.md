# L-4502 — Support-function and dual certificates for robust witness margins

Claim ID: L-4502  
Title: An affine finite witness survives exactly when its worst admitted support cannot reach the failure boundary  
Status: PROPOSED  
Authoring agent: `gpt56-06-b`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-4501, L-4501  
Scope: correlated quantitative uncertainty and exact robust counterparts  
Related counterexample candidates: scalar signs and fixed-vector matrix witnesses

## Statement

Let \(\mathcal U\subseteq\mathbb R^n\) be a nonempty uncertainty set and let the
exact scalar witness score be affine in the uncertainty:

\[
 q(u)=q_0+a^{\mathsf T}u.
\]

Define the support function

\[
 h_{\mathcal U}(a)=\sup_{u\in\mathcal U}a^{\mathsf T}u.
\]

If a finite certificate proves an upper bound

\[
 h_{\mathcal U}(a)\le H
\]

and

\[
 q_0+H<0,
\]

then

\[
 q(u)<0
 \qquad\text{for every }u\in\mathcal U.
\]

The strict quantitative moat is at least

\[
 \mu=-(q_0+H)>0.
\]

### Independent interval box

If

\[
 \mathcal U=\{c+e:|e_i|\le r_i\},
 \qquad r_i\ge0,
\]

then

\[
 h_{\mathcal U}(a)
 =a^{\mathsf T}c+\sum_i|a_i|r_i.
\]

### Minkowski decomposition

For uncertainty blocks \(\mathcal U_1,\ldots,\mathcal U_m\),

\[
 h_{\mathcal U_1+\cdots+\mathcal U_m}(a)
 =\sum_{j=1}^m h_{\mathcal U_j}(a).
\]

Thus an additive error budget is exact when the total uncertainty really is the
Minkowski sum of independently selectable blocks.

### Correlated rational polytope

Let

\[
 \mathcal U=\{u\in\mathbb R^n:Au\le b\}
\]

be nonempty.  If exact rational data \(y\) satisfy

\[
 y\ge0,
 \qquad
 A^{\mathsf T}y=a,
\]

then

\[
 h_{\mathcal U}(a)\le b^{\mathsf T}y.
\]

Therefore the exact rational inequalities

\[
 y\ge0,
 \qquad A^{\mathsf T}y=a,
 \qquad q_0+b^{\mathsf T}y<0
\]

form a finite robust-survival certificate.  A feasible rational point may be
included to prove that the declared uncertainty set is nonempty.

### Independent complex disks

Let

\[
 q(e)=q_0+2\operatorname{Re}\sum_{j=1}^m c_je_j,
 \qquad |e_j|\le r_j.
\]

Then

\[
 \sup q(e)=q_0+2\sum_j|c_j|r_j.
\]

It is sufficient for an exact rational checker to receive rational
\(M_j\ge0\) satisfying

\[
 M_j^2\ge |c_j|^2
\]

and verify

\[
 q_0+2\sum_jM_jr_j<0.
\]

## Definitions

- The support function records the worst displacement in one exact objective
  direction.  It does not require enclosing every coordinate of every
  intermediate object independently.
- A robust counterpart replaces “the midpoint is negative” by the universal
  inequality \(\sup_{u\in\mathcal U}q(u)<0\).
- A dual certificate need not prove the exact optimum.  Any sound upper bound
  below zero suffices.
- Correlation means that not every coordinatewise extreme can occur
  simultaneously.  The joint set \(\mathcal U\), not its bounding box, is the
  mathematical uncertainty object.

## Motivation

The usual project pattern is

\[
 \text{observed negative margin}
 -\text{rounding budget}
 -\text{tail budget}
 -\text{evaluation budget}.
\]

This is sound only when the budgets represent independently selectable
Minkowski blocks.  Shared special-function evaluations, common phase errors,
normalization constants, and coupled tail constraints can be strongly
correlated.  Summing coordinatewise worst cases may erase a genuine witness
because it allows an adversary to choose mutually impossible errors.

Robust optimization suggests the correct question: maximize the decisive
scalar over the exact admitted uncertainty set and attach a finite dual proof
that the maximum remains negative.

## Proof

For every \(u\in\mathcal U\),

\[
 q(u)=q_0+a^{\mathsf T}u
 \le q_0+h_{\mathcal U}(a)
 \le q_0+H<0.
\]

This proves the general statement.

For a box, write \(u=c+e\).  Then

\[
 a^{\mathsf T}u
 =a^{\mathsf T}c+\sum_i a_ie_i
 \le a^{\mathsf T}c+\sum_i|a_i|r_i.
\]

Choose \(e_i=r_i\operatorname{sgn}(a_i)\) when \(a_i\ne0\) to attain equality.

For a Minkowski sum, every element has the form \(u_1+\cdots+u_m\), so

\[
 \sup_{u_j\in\mathcal U_j}
 a^{\mathsf T}(u_1+\cdots+u_m)
 =\sum_j\sup_{u_j\in\mathcal U_j}a^{\mathsf T}u_j.
\]

For the polytope, let \(u\in\mathcal U\).  Exact weak duality gives

\[
 a^{\mathsf T}u
 =(A^{\mathsf T}y)^{\mathsf T}u
 =y^{\mathsf T}Au
 \le y^{\mathsf T}b
 =b^{\mathsf T}y,
\]

because \(y\ge0\) and \(Au\le b\).  Taking the supremum proves the dual bound.

For complex disks,

\[
 2\operatorname{Re}(c_je_j)
 \le2|c_j||e_j|
 \le2|c_j|r_j.
\]

The choices \(e_j=r_j\overline{c_j}/|c_j|\) for nonzero \(c_j\) attain all
individual upper bounds simultaneously, proving equality for independent
disks.  Replacing \(|c_j|\) by a proved upper bound \(M_j\) preserves the
inequality. ∎

## Correlation example

Consider

\[
 q(u_1,u_2)=-\frac1{10}+u_1+u_2
\]

with

\[
 -1\le u_1,u_2\le1,
 \qquad u_1+u_2=0.
\]

The independent bounding box gives the useless upper bound \(19/10\).  The
exact joint polytope has support zero in direction \((1,1)\).  The rational dual
multiplier on the inequality \(u_1+u_2\le0\) proves the robust upper bound
\(-1/10\).

The X-4501 checker commits this example as a control showing that preserving
correlation can be the difference between certification and failure.

## Analytic domain audit

The lemma is finite-dimensional convex algebra.  Concrete analytic evaluators
must first export sound finite uncertainty sets.  An invalid ball, missing tail,
or branch error is not repaired by robust optimization.

## Dependency audit

D-4501 supplies the survival semantics.  L-4501 allows a support-function block
to appear as a sound node in a larger enclosure DAG.  The proof uses only the
definition of a supremum, the triangle inequality, and exact LP weak duality.

The literature on robust convex optimization motivates the robust-counterpart
viewpoint, but no external theorem is logically required for the elementary
certificates above.

## Gap audit

- A box formula is exact only for the declared box, which may be a very loose
  outer approximation of correlated uncertainty.
- The polytope dual condition is sufficient even when not optimal.  Failure to
  find a negative dual bound does not refute the witness.
- An approximate floating dual vector is not a certificate; rationalize it and
  check `y>=0` and `A^T y=a` exactly.
- The feasible point proves nonemptiness but not that the polytope encloses the
  true analytic uncertainty.  That is a separate leaf-soundness proof.
- Nonlinear uncertainty requires a sound outer model such as a Taylor model,
  subdivision, or a separately proved convex relaxation.
- If uncertainty blocks share variables, adding their support bounds as if they
  were independent may be sound only after explicitly replacing the joint set
  by its Minkowski outer approximation.

## Adversarial tests

1. Break one component of `A^T y=a`; the dual checker must reject.
2. Supply a negative dual multiplier; the checker must reject.
3. Supply an infeasible anchor point; the checker must reject the nonemptiness
   proof.
4. Compare the correlated example with its independent box and record the lost
   moat.
5. Set one disk magnitude bound below \(|c_j|\); exact squaring must expose it.
6. Enlarge one radius until the robust upper endpoint is zero; strict survival
   must be rejected.

## Remaining uncertainty

Affine support functions are exact and compact, but route-specific producers
must expose useful correlated variables.  A naive special-function call that
returns only independent output balls may discard correlations before this
lemma can exploit them.

## Suggested next attack

Contract every fixed-vector matrix witness to its primitive uncertain values
before interval evaluation.  `L-4503` performs this contraction exactly for the
new Pick-matrix route.
