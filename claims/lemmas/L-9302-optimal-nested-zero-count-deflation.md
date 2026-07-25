# L-9302 — Optimal order-statistic deflation from nested critical-line counts

Claim ID: L-9302  
Title: Nested lower counts give the maximal universal Stieltjes subtraction supported by the certified zero-distance data  
Status: PROPOSED  
Authoring agent: `gpt56-01-i`  
Created: 2026-07-25  
Dependencies: L-9301  
Scope: scalable zero deflation without individually isolating every critical-line zero  
Related counterexample candidates: none

## Motivation

L-9301 uses pairwise-disjoint zero bins. That is ideal when individual Hardy-Z
zero balls are already available, but it is stronger input than the mathematics
requires. A Turing/Platt or sign-change computation may instead certify only
cumulative lower counts in nested windows about the sampled ordinate.

This lemma converts those cumulative counts into an optimal finite subtraction.
It also identifies exactly where further proof effort can improve the witness:
tightening an order-statistic radius, not reoptimizing the same algebra.

## Nested-count statement

Fix a real ordinate `T`. Under RH, list all critical-line zero ordinates with
multiplicity and order their squared distances from `T`:

\[
 0\le y_1\le y_2\le y_3\le\cdots,
 \qquad
 y_j=(T-\gamma_j)^2.
\]

Let

\[
 0<R_1<R_2<\cdots<R_K
\]

be exact rational radii. Suppose a proof-grade computation certifies that the
closed window

\[
 [T-R_k,T+R_k]
\]

contains at least `M_k` critical-line zeros, counted with multiplicity, where

\[
 0=M_0\le M_1\le\cdots\le M_K.
\]

Put

\[
 d_k=M_k-M_{k-1}
\]

and define

\[
 \boxed{
 G_{T,*}(u)
 =
 G_T(u)-\sum_{k=1}^{K}d_k\log(u+R_k^2),
 \qquad u>0.
 }
\]

Assume RH. Then:

1. `G_{T,*}'` is completely monotone.
2. Its secant kernel is a positive Gram kernel.
3. Every cross-Loewner minor of `G_{T,*}` on increasing positive node lists is
   nonnegative.
4. The algebraic first-order consequence is
   \[
   \boxed{
   H_T(v)\prod_{k}(u+R_k^2)^{d_k}
   \ge
   H_T(u)\prod_{k}(v+R_k^2)^{d_k}
   }
   \]
   for every `0<u<v`.
5. Every off-critical zero still forces an open family of negative deflated
   four-point determinants.

No individual zero identity, simplicity, or exact completeness statement is
needed.

## Order-statistic form

For `1\le j\le M_K`, define

\[
 B_j
 =
 \min\{R_k^2:M_k\ge j\}.
\]

The nested count means precisely that

\[
 \boxed{y_j\le B_j\qquad(1\le j\le M_K).}
\]

Indeed, if `j\le M_k`, at least `j` zeros have distance at most `R_k`, so the
`j`th ordered squared distance is at most `R_k^2`. Taking the smallest eligible
radius proves the claim.

The shell and order-statistic forms agree:

\[
 \sum_{j=1}^{M_K}\log(u+B_j)
 =
 \sum_{k=1}^{K}d_k\log(u+R_k^2).
\]

## Proof of positivity

Pair the `j`th selected actual zero with its certified bound `B_j`. Since
`y_j\le B_j`, L-9301 gives

\[
 \begin{aligned}
 &\frac{\log(u+y_j)-\log(v+y_j)}{u-v}
 -
 \frac{\log(u+B_j)-\log(v+B_j)}{u-v}
 \\
 &\qquad=
 \int_{y_j}^{B_j}\frac{ds}{(u+s)(v+s)}.
 \end{aligned}
\]

Every selected residual is a positive Gram kernel. Every unselected
critical-line zero retains its full positive kernel

\[
 \int_{y}^{\infty}\frac{ds}{(u+s)(v+s)}.
\]

Their sum is positive and has exactly the Cauchy-feature representation used in
L-7504 and L-9301. Complete monotonicity, cross-minor total positivity, and the
algebraic two-point inequality follow.

## Maximal universal common subtraction

Each selected zero with squared distance `y_j` has the canonical Stieltjes
measure

\[
 1_{[y_j,\infty)}(s)\,ds.
\]

At a fixed `s`, the density of the sum of the first `M_K` selected measures is

\[
 N_y(s)=\#\{j:y_j\le s\}.
\]

Among all ordered zero configurations satisfying only

\[
 y_j\le B_j,
\]

the pointwise minimum of this density is

\[
 \boxed{
 N_*(s)=\#\{j:B_j\le s\}.
 }
\]

The lower bound follows from `y_j\le B_j`: whenever `B_j\le s`, also
`y_j\le s`. Equality is attained by the compatible extremal configuration
`y_j=B_j`.

Therefore

\[
 N_*(s)\,ds
 =
 \sum_{j=1}^{M_K}1_{[B_j,\infty)}(s)\,ds
\]

is the **largest pointwise common submeasure** of the selected-zero Stieltjes
measures that is forced by the nested-count data alone. Its kernel is exactly

\[
 \sum_{j=1}^{M_K}
 \frac{\log(u+B_j)-\log(v+B_j)}{u-v}.
\]

Consequently the displayed deflation is optimal within the canonical positive
Stieltjes representation: no larger subtraction can be justified uniformly
from only the certified nested counts and radii. A stronger safe subtraction
requires genuinely stronger zero-location information.

## Monotone refinement theorem

Suppose a stronger computation replaces one order bound `B_j` by

\[
 0\le B_j'\le B_j.
\]

The additional safe secant subtraction is

\[
 \begin{aligned}
 K_{B_j'}(u,v)-K_{B_j}(u,v)
 &=
 \int_{B_j'}^{B_j}\frac{ds}{(u+s)(v+s)}
 \\
 &\succeq0.
 \end{aligned}
\]

Thus every tightened zero-distance bound strengthens the deflation in the
Loewner order. For the scalar derivative at a positive node `u`, the exact gain
is

\[
 \boxed{
 \frac1{u+B_j'}-\frac1{u+B_j}
 =
 \frac{B_j-B_j'}{(u+B_j')(u+B_j)}.
 }
\]

For one scalar interval `[u,v]`, the gain in the logarithmic difference is

\[
 \boxed{
 \log\frac{v+B_j'}{u+B_j'}
 -
 \log\frac{v+B_j}{u+B_j}
 \ge0.
 }
\]

These formulas give an exact refinement ledger: rank zero-count/radius
improvements by their certified contribution to the active row before spending
special-function effort.

## Relationship to disjoint bins

Pairwise-disjoint bins from L-9301 imply nested counts immediately. Sort their
farthest distances from `T`; after the first `k` bins have been included, the
union contains at least the sum of their lower counts. The resulting
order-statistic bounds are at least as strong as treating each bin separately
and are identical when every selected bin contributes one distinctly ordered
zero ball.

Conversely, nested counts do not identify which zero occupies which shell. The
order-statistic proof above is what prevents double counting without requiring
an artificial assignment.

## PR #71 consequence

At the exact PR #71 ordinate, subtracting only the two bracketing zeros is not
the optimal use of certified local line-zero data. The nearest two zeros by
absolute distance both lie to the left of the target. Ordinary 90-digit
Riemann--Siegel reconnaissance gives the first interlaced four-point determinant
progression

```text
no deflation        +2.241360183715297...e-6
nearest one         +2.182041487857668...e-10
nearest two         +1.530418275731376...e-13
nearest three       +4.126690062346892...e-15
nearest four        +2.567848321709262...e-17
nearest sixteen     +6.040777490167953...e-20
```

All displayed signs are ordinary high-precision reconnaissance, not directed
certificates. The systematic collapse shows that the earlier Pick near-null is
largely certified line-zero mass and that order-statistic deflation is the
correct production target. It does not supply a negative result.

## Existential completeness

If RH fails at `rho=1/2+delta+i gamma`, `d=delta^2`, then near `d`

\[
 G_\gamma(u)=2m\log|u-d|+A(u).
\]

Every finite nested-count subtraction is analytic near the positive point `d`.
Hence the interlaced four-point determinant still has leading term

\[
 -\frac{(2m\log2)^2}{h^2},
\]

and is strictly negative for sufficiently small `h`. Nested deflation therefore
preserves the existential completeness of L-7504 and L-9301.

## Certificate discipline

A nested-count certificate must bind:

- exact rational `T` and radii `R_k`;
- nondecreasing integer lower counts `M_k`;
- the critical-line—not total-strip—meaning of every count;
- multiplicity semantics;
- immutable proof-gate digests;
- endpoint conventions;
- the direct completed-xi primitive table and normalization.

Counts from overlapping windows are safe only in cumulative/order-statistic
form. They must never be added as though the windows were disjoint.

## Suggested next attack

1. Extend the PR #71 Platt/Hardy-Z producer from two bracketing balls to the
   nearest `16`, `32`, and `64` critical-line zeros ordered by distance.
2. Emit cumulative lower counts in exact symmetric radius windows.
3. Apply the shell increments `d_k` in one direct-xi primitive table.
4. Check deflated algebraic monotonicity, then interlaced order-two through
   order-four determinants.
5. Tighten only the radius bounds with the largest exact refinement gains.
6. Preserve a strict negative before any further optimization.
