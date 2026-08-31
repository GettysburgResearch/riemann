# Independent review of the five-node paired-Schwarzian no-go

Verdict: **PASS**, with no blocking mathematical or scope defect found.

This review is frozen against science commit
`1eee9e7d243d416d901620e5be2cbdfb1b38d11c` and preregistration commit
`d593846375390b1ad76c5b5ff129003271009ea3`; the latter is an ancestor of
the former.  The reviewed note at the science commit has blob
`2e3bace6a71b6aa7fa5c73775082ab512cd24ea1`.

## Exact determinant and witness

Writing the five-by-five matrix as

\[
 H=\begin{pmatrix}M&h\\h^T&H_{55}\end{pmatrix},\qquad d=\det M,
 \qquad c=(-\operatorname{adj}(M)h,d)^T,
\]

direct multiplication gives

\[
 Hc=(0,\ dH_{55}-h^T\operatorname{adj}(M)h)^T
    =(0,\det H)^T.
\]

Thus `FN4`, \(c^THc=d\det H\), uses neither \(M^{-1}\) nor an unstated
invertibility premise.  When \(d>0\), the last coordinate of \(c\) is
already nonzero; hence \(d>0>\det H\) supplies a literal negative
quadratic-form witness.

I independently rebuilt `FN2` over the rationals, without importing the
producer.  For \(x=(1,2,3,4,5)\), \(p_0(t)=2/(t+1)+4/(t+4)\), and only
\(p(1)=p_0(1)-\epsilon\), the result is exactly

\[
 \det H=-\frac{243}{2169288277812500}\epsilon
         -\frac{483}{533978653000000}\epsilon^2.
\]

Its roots are \(0\) and \(-1296/10465\), so it is negative for every
\(\epsilon>0\).  At \(\epsilon=1/100\) I also recovered `FN7`, and the
four-node anchor is
\(d=4519731/488410000000000>0\).  Direct substitution reproduced both
\(Hc=(0,0,0,0,\det H)^T\) and \(c^THc=d\det H<0\).

## Proper-minor signs

At \(\epsilon=0\), each atom \((a,s)\) contributes

\[
 a\frac{x_i x_j+s}{(x_i^2+s)(x_j^2+s)},
\]

a Gram kernel with two real features.  For the two distinct atoms the four
feature functions form a Chebyshev system on positive distinct nodes: after
multiplication by the two quadratic denominators, a vanishing linear
combination has a polynomial numerator of degree at most three, and four
distinct zeros force all four coefficients to vanish.  Consequently every
principal submatrix of size at most four is positive definite at the base.
I separately enumerated all 30 proper principal minors at
\(\epsilon=0\) and \(1/100\); every sign is strictly positive.

For the theorem, only the base signs plus continuity are needed.  There are
finitely many selected proper minors, all with strict base margins, so one
common positive perturbation threshold preserves them.  The exact
determinant formula is negative at every positive perturbation and therefore
meets that threshold without a numerical estimate.

## Global bump and lower orders

The strict base inequalities can be checked directly:

\[
\begin{aligned}
p_0&=\frac{6(t+2)}{(t+1)(t+4)},\\
p_0'&=-\frac{6(t^2+4t+6)}{(t+1)^2(t+4)^2},\\
(tp_0)'&=\frac{6(3t^2+8t+8)}{(t+1)^2(t+4)^2},\\
(1/p_0)''&=-\frac{2}{3(t+2)^3},\\
(tp_0)''&=-\frac{36(t+2)(t^2+2t+4)}{(t+1)^3(t+4)^3},\\
Sp_0&=\frac{12}{(t^2+4t+6)^2},\qquad
S(tp_0)=\frac{48}{(3t^2+8t+8)^2}.
\end{aligned}
\]

Choose the bump support inside a compact neighborhood of \(1\) contained in
\((1/4,4)\).  On that compact set, positivity of \(p_0\), the two strict
derivative signs, the two strict concavity signs, and the cleared
Schwarzian numerators all have positive minima; the Schwarzian derivative
denominators are bounded away from zero.  These finitely many jet conditions
are open in the \(C^3\) norm, so \(p_0-\epsilon\psi\) preserves them for all
sufficiently small \(\epsilon>0\).  Off the support it equals \(p_0\)
exactly, and smooth compact support also matches every required boundary
jet.  Thus there is no uncovered transition region.  A positive rational
\(\epsilon\) can be chosen below the common threshold, while the other four
sample values remain unchanged.

The cited lower-order implication is consistent with the exact scalar
factorizations: two-node determinants use the strict signs of \(p\) and
\(tp\); a three-node determinant is the product of the second divided
difference factors for \(tp\) and \(1/p\), both negative under strict
concavity; and `SP16` plus the four-point Schwarzian bridge makes both
four-node factors negative and their product positive.  Hence every proper
principal minor of the selected five-node matrix is positive while its full
determinant is negative.

## Scope

This is an abstract smooth scalar countermodel only.  The bump need not be a
Stieltjes transform, completed \(\Xi\), or source-polarized arithmetic
kernel.  The result shows that the listed lower-order scalar inequalities do
not logically force five-node positivity.  It gives **no negative actual-\(\Xi\)
packet and no conclusion proving or disproving order-five positivity for
\(\Xi\)**; it also makes no RH inference.

As corroborative checks, all 27 committed tests passed in ordinary and
`python -O` modes, and the producer's check and exact fixture/source emission
paths agreed in both modes.  The analytic verdict above does not rely on the
held-out panel.
