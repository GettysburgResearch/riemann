# L-0603 — Exact susceptibility threshold for a negative rank-one update

Claim ID: L-0603  
Title: Exact susceptibility threshold for a negative rank-one update  
Status: PROPOSED  
Authoring agent: `gpt56-01-a`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: elementary finite-dimensional linear algebra  
Scope: positive-definite Hermitian matrices  
Related counterexample candidates: none

## Statement

Let `A` be a real symmetric positive-definite matrix and let `r` be nonzero.
For `t>=0`,

\[
 A-t rr^{\mathsf T}\succeq0
 \quad\Longleftrightarrow\quad
 t\le \frac1{r^{\mathsf T}A^{-1}r}.
\]

Strict positive definiteness holds exactly when the inequality is strict. At
equality the nullspace is spanned by `A^{-1}r`.

Applied to `L-0601`, the frozen-background critical edge displacement is

\[
 \delta_{\rm frozen}
 =\frac{a\sqrt q}{2\,r_N^{\mathsf T}Q_N(q)^{-1}r_N}.
\]

This is a prioritization statistic only: the actual matrix path contains smooth
background motion and nonlinear prime-block terms.

## Proof

Let `x=A^{-1/2}r`. Congruence by `A^{-1/2}` gives

\[
 A^{-1/2}(A-trr^{\mathsf T})A^{-1/2}
 =I-txx^{\mathsf T}.
\]

The latter matrix has eigenvalue `1-t||x||^2` in the direction `x` and
eigenvalue `1` on its orthogonal complement. Since

\[
 \|x\|^2=r^{\mathsf T}A^{-1}r,
\]

the equivalence follows. At equality,
`A^{-1/2}x=A^{-1}r` spans the nullspace.

## Analytic domain audit

This is finite-dimensional real linear algebra. No analytic continuation,
branch, or numerical approximation is involved.

## Dependency audit

The general lemma is self-contained. The displayed application uses the
coefficient `2/(a sqrt(q))` from `L-0601` and treats all other motion as frozen.

## Gap audit

The frozen prediction is not a crossing theorem for `Q_N(c)`. In the actual
path, `A` changes with `c`, the new prime block is not exactly linear away from
the threshold, and the minimizing vector can rotate sharply in the nearly
singular metric.

## Adversarial tests

`X-0601` compares the frozen prediction with direct full-path evaluations.
Several frozen models predict an in-interval crossing while the actual matrix
remains positive; this deliberately tests and demonstrates the stated caution.

## Remaining uncertainty

None in the abstract linear-algebra statement. Project status remains
`PROPOSED` until reviewed under repository convention.

## Suggested next attack

Use `r^T A^{-1}r` to rank events, but always evaluate the complete cutoff-free
matrix at the proposed displacement and on a precision ladder before exporting
a candidate.
