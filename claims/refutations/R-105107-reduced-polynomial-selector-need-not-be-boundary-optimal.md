# R-105107 — Reduced polynomial selectors need not be boundary-optimal

Claim ID: R-105107

Status: **PROPOSED EXACT REFUTATION**

Created: 2026-08-23

Depends on: L-105106; L-105107

RH status: **unproved**

## Refuted inference

The following implication is false:

> The unique degree-less-than-\(D\) polynomial CRT selector is the best exact
> selector for boundary estimates.

## Exact counterexample

In the unit disk, take target \(0\) of order one and nontargets
\(\pm\varepsilon\), each of order two.  At \(\varepsilon=1/5\), the unique
reduced polynomial selector from L-105106 is

\[
W_{\rm poly}(z)=(1-25z^2)^2
\tag{R-105107.1}
\]

and

\[
\|W_{\rm poly}\|_{|z|=1}=676.
\tag{R-105107.2}
\]

The boundary-optimal exact selector is instead

\[
W_*(z)=625
\left(
\frac{z^2-1/25}{1-z^2/25}
\right)^2,
\tag{R-105107.3}
\]

which has the same target value and the same double nontarget zeros, but

\[
|W_*(e^{i\theta})|=625
\quad\hbox{for every }\theta.
\tag{R-105107.4}
\]

The L-105106 Blaschke lower bound is \(625\), so (R-105107.3) is globally
optimal among all bounded holomorphic exact selectors, not merely rational
ones.

## Full-matrix firewall

After forced-inner factorization, target nodes
\(-1/2,1/2\) with values \(-2,2\) have diagonal lower bound \(u\ge2\).
At \(u=2\), however, the full Pick matrix is

\[
\begin{pmatrix}
0&32/5\\
32/5&0
\end{pmatrix},
\tag{R-105107.5}
\]

which is indefinite.  The exact optimum is \(u=4\), where

\[
P_4=
\begin{pmatrix}
16&16\\
16&16
\end{pmatrix}
\succeq0.
\tag{R-105107.6}
\]

Thus targetwise Blaschke lower bounds do not replace the off-diagonal Pick
conditions.

## Consequence

Polynomial CRT remains useful for exact algebra and manifest verification,
but it can carry avoidable boundary growth.  The finite Pick optimum removes
that avoidable part.  It does not remove intrinsic clustering: the optimal
norm still contains forced pseudohyperbolic products and may diverge
cofinally.

The rational extremal also has reflected poles outside the current disk.
Those poles invalidate blind reuse on a larger contour.  Recompute the
selector for each window or prove a separate pole-exclusion statement.
