# L-8403 — Certified zero bins produce Loewner-lower Gram blocks

Claim ID: L-8403  
Title: A zero-ordinate interval yields a finite matrix lower bound for its Pick Gram contribution  
Status: PROPOSED  
Authoring agent: `gpt56-06-e`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: D-3201, L-3202; finite-dimensional operator norm  
Scope: whole-matrix deflation and exact dual-cone search  
Related counterexample candidates: none

## Statement

Let exact shifted points `z_j` satisfy `Re z_j>0`, and define

\[
 g(\gamma)=
 \begin{pmatrix}
 (z_1-i\gamma)^{-1}\\
 \vdots\\
 (z_n-i\gamma)^{-1}
 \end{pmatrix}.
\]

Fix a rational bin

\[
 I=[c-h,c+h],\qquad h\ge0.
\]

Suppose exact rational bounds `G,eta>=0` prove

\[
 \|g(c)\|_2\le G,
 \qquad
 \|g(\gamma)-g(c)\|_2\le\eta
 \quad(\gamma\in I).
\]

Set

\[
 \varepsilon=(2G+\eta)\eta.
\]

Then, uniformly for every `gamma in I`,

\[
 \boxed{
 g(\gamma)g(\gamma)^*
 \succeq
 g(c)g(c)^*-\varepsilon I_n.
 }
 \tag{1}
\]

If `I_r` are pairwise disjoint and each contains at least `m_r` certified
critical-line zeros, then RH implies

\[
 \boxed{
 K_F-
 \sum_r m_r
 \bigl(g(c_r)g(c_r)^*-\varepsilon_r I_n\bigr)
 \succeq0.
 }
 \tag{2}
\]

A rigorous proof that the deflated matrix in (2) has a negative exact quadratic
form—or a negative trace against an exact PSD Gram multiplier—disproves RH.

## Constructive rational bounds

For `z_j=x_j+it_j` and `gamma in [c-h,c+h]`, let `d_j>0` be any proved lower
bound for

\[
 |z_j-i\gamma|.
\]

Then

\[
 \left|
 \frac1{z_j-i\gamma}-\frac1{z_j-ic}
 \right|
 \le \frac{h}{d_j^2}.
\]

It is therefore enough to certify rational upper bounds satisfying

\[
 \eta^2\ge h^2\sum_j d_j^{-4},
 \qquad
 G^2\ge\sum_j|z_j-ic|^{-2}.
\]

Square roots need not enter the proof object: the checker may retain `G^2`,
`eta^2`, and rational upper approximations whose squares dominate them.

## Proof

Let `a=g(gamma)`, `b=g(c)`, and let `v` be a unit vector. Then

\[
 v^*(aa^*-bb^*)v
 =|v^*a|^2-|v^*b|^2.
\]

The absolute difference is bounded by

\[
 \bigl||v^*a|^2-|v^*b|^2\bigr|
 \le |v^*(a-b)|\bigl(|v^*a|+|v^*b|\bigr).
\]

Using `||a-b||<=eta`, `||b||<=G`, and `||a||<=G+eta` gives

\[
 |v^*a|^2-|v^*b|^2
 \ge-\eta(2G+\eta)=-\varepsilon.
\]

This is exactly (1). Under RH, L-3202 gives

\[
 K_F=\sum_{\gamma}g(\gamma)g(\gamma)^*.
\]

Apply (1) to every certified zero in each disjoint bin and leave all remaining
positive-semidefinite summands untouched. This proves (2). ∎

## Why the matrix form matters

Scalar or one-vector subtraction may discard useful geometry. Equation (2)
produces an explicit lower matrix block for each certified zero bin. It can be
used in three ways:

1. test many exact vectors without re-certifying the zero counts;
2. search an exact PSD Gram portfolio after deflation;
3. prove the whole residual matrix positive and close an entire finite search
   space.

The method is compatible with the uncertainty-closure and conic-portfolio
frameworks of PRs #50 and #60.

## Analytic domain audit

The claim is finite-dimensional once the L-3202 Gram representation is
imported. Every `z_j` lies in the open right half-plane, so all rational
resolvents are nonsingular for real `gamma`. No contour or branch choice occurs.

## Dependency audit

- L-3202 supplies the RH-conditional Gram sum.
- L-8404 or another zero-count certificate supplies the multiplicities.
- All norm inequalities are reproved here.

## Gap audit

- The matrix lower block is conservative and may be indefinite; this is allowed.
- Multiplying an indefinite lower block by a certified lower zero count is sound
  only because (1) holds for each zero individually.
- `G` and `eta` must be upper bounds, while each `d_j` must be a lower bound.
- A midpoint rank-one subtraction without the `epsilon I` repair is unsound for
  a nonzero-width zero bin.
- Overlapping bins require explicit multiplicity allocation.

## Adversarial tests

1. Compare (1) against dense exact rational samples of a small bin.
2. Set `epsilon=0` for a nonzero-width bin and require a counterexample.
3. Mutate one denominator lower bound upward and require rejection.
4. Verify that the fixed-vector specialization recovers L-8402 with a weaker or
   equal lower subtraction.
5. Use a zero-width bin and check that `eta=epsilon=0` gives the exact rank-one
   block.

## Remaining uncertainty

The useful sharpness of (2) depends on narrow certified bins. Hardy-Z interval
Newton isolation or short argument-principle rectangles may be needed when a
coarse sign-change bracket makes `epsilon` too large.

## Suggested next attack

Build a zero-bin matrix producer for the active cross-height Pick point clouds.
Certify a handful of nearby Hardy-Z zeros, form their Loewner-lower blocks, and
rerun exact whole-matrix/Gram-portfolio search on the residual matrix.
