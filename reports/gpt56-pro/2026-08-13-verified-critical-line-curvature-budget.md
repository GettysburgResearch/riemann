# Verified critical-line curvature budget closes the proposed Xi order-three theorem

Date: 2026-08-13  
Parent: PR #445 at `c079c2ef21022be951027de1316aecf1168422c1`  
Branch: `research/gpt56-pro/92100-critical-reserve-absorption`  
Status: **proposed unconditional theorem; RH unproved**

## Executive result

PR #445 reduced actual-Xi three-node infinitesimal Pick positivity to
reciprocal concavity of

\[
 p(t)=\frac1{\sqrt t}
 \frac{\xi'}{\xi}\left(\frac12+\sqrt t\right).
\]

A single off-line zero orbit has the wrong sign, so an orbitwise proof is
impossible.  The new observation is that one rigorously verified low
critical-line orbit supplies enough positive cross-curvature to pair with
**every** possible off-line orbit above the verified height.

For one off-line orbit `a+ib` of multiplicity `m`, the required share of one
critical orbit is

\[
 \epsilon
 =\frac{2m\kappa}{1-\kappa},
 \qquad
 \kappa=\frac{4a^2b^2}{(b^2-a^2-r_0)^2}.
\]

If `b` is above the Platt--Trudgian verification height, then

\[
 \epsilon\le\frac{9m}{b^2}.
\]

The complete budget obeys

\[
 \sum\epsilon
 \le\frac{18(\log H_*+1)}{H_*}
 <1.8\times10^{-10}.
\]

Thus less than one billionth of one verified critical orbit is needed.  The
remaining part of that orbit and all other critical orbits are retained with
coefficient one.

## 1. Differential closure

For

\[
 \mathcal E[f]=ff''-2(f')^2,
\]

reciprocal concavity is `E[f]>=0`.  If `E[f],E[g]>=0`, then

\[
\begin{aligned}
 \mathcal E[f+g]
 &\ge\mathcal E[f]+\mathcal E[g]\\
 &\quad+2\left(
 \sqrt{g/f}\,f'-\sqrt{f/g}\,g'
 \right)^2\ge0.
\end{aligned}
\]

So reciprocal-concave blocks are closed under positive sums.

## 2. Exact one-orbit calculation

Write

\[
 q(t)=\frac{4mU}{U^2+B^2},
 \qquad
 R(t)=\frac2{t+r},
\]

with

\[
 U=t+b^2-a^2,
 \qquad B=2ab.
\]

Then

\[
 \mathcal E[q]
 =-\frac{32m^2B^2}{(U^2+B^2)^3},
 \qquad
 \mathcal E[R]=0.
\]

Let

\[
 s=\frac{b^2-a^2-r}{U},
 \qquad
 \kappa=\frac{B^2}{(b^2-a^2-r)^2}.
\]

The cross curvature is

\[
 \mathcal C[q,R]
 =\frac{16m s^2Q_\kappa(s)}
 {U^4(1+\kappa s^2)^3(1-s)^3},
\]

where

\[
 Q_\kappa(s)
 =1-\kappa+3\kappa s(2-s)
 +\kappa^2s^2(3-2s)
 \ge1-\kappa.
\]

Taking

\[
 \epsilon=\frac{2m\kappa}{1-\kappa}
\]

gives

\[
 \mathcal E[q+\epsilon R]\ge0.
\]

## 3. Global assembly

Choose one verified critical-line zero with squared ordinate
`r_0<=H_*^2/4`.  Split its contribution as

\[
 R_0=\epsilon_0R_0+\sum_\alpha\epsilon_\alpha R_0,
 \qquad
 \epsilon_0=1-\sum_\alpha\epsilon_\alpha>0.
\]

Pair every hypothetical off-line orbit with its assigned share.  Every paired
block has concave reciprocal; every remaining critical orbit has affine
reciprocal.  The closure theorem and locally `C^2` convergence of the grouped
Hadamard series give

\[
 \left(\frac1p\right)''\le0
 \qquad(t>1/4).
\]

Combined with the determinant factorization on PR #445, this yields proposed
unconditional positivity of every actual-Xi packet of size at most three.

## 4. Review boundary

The finite rational algebra is exact.  The load-bearing review joints are:

1. the cross-curvature simplification;
2. the `9m/b^2` estimate;
3. the global zero-tail budget;
4. the existence and allocation of one verified line orbit;
5. locally `C^2` convergence after regrouping all orbit blocks;
6. multiplicity and symmetry bookkeeping.

## 5. Exact state

```text
parallel-sum curvature closure                  EXACT
one-orbit line-share calculation                EXACT
verified-height global budget                   PROPOSED COMPLETE
actual-Xi reciprocal concavity                  PROPOSED COMPLETE
all actual-Xi packets of size <=3               PROPOSED UNCONDITIONAL
first remaining interpolation order             FOUR
all finite packet sizes                         OPEN / RH-EQUIVALENT
Riemann Hypothesis                              UNPROVED
```
