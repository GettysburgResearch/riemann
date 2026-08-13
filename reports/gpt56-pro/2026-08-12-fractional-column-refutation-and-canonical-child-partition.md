# 2026-08-12 — Fractional-column refutation and canonical rough-child partition

## Status

**RH remains unproved.** This continuation corrects one proposed complete
composition and replaces it with an exact parent-coordinate assembly theorem,
a branching consumer, and a new one-prime source partition for the native SHARP
block.

## 1. Blocking audit

`L-91325.16` used the exact covariance

\[
 \overline\beta_{m(n+1)-1}(Q)=\overline\beta_n(Q/m)
\]

and then applied child feasibility at `Q/m`. The latter is generally a
noninteger column. `L-91324` explicitly proves only positive functoriality of
port domination, not arbitrary finite real-column or radix-four feasibility.

`R-91304` therefore blocks the proposed complete composition at this step.

## 2. Sum before quantization

`L-91329` gives the correct order:

```text
partition continuum sources and targets;
push all branch endpoint measures to the parent coordinate;
sum colors there;
quantize once;
apply one finite collar repair at physical integer columns.
```

This construction never evaluates an arbitrary finite child packing at a
fractional column and spends the parent target only once.

The remaining input is an exact positive parent-coordinate source partition for
the parallel least-prime branches.

## 3. Branching consumer

`T-91302` allows a reset to produce many children. If

\[
 Y_b\le c_0X+O(1),
 \qquad
 \theta_b\ge0,
 \qquad
 \sum_b\theta_b\le1,
\]

and

\[
 \mathfrak L_X
 \le E_X+\sum_b\theta_b\mathfrak L_{Y_b},
\]

then the total path weight at every tree depth is at most one. The factor-54
tree has `O(log X)` levels, so bounded local debt still gives

\[
 \mathfrak L_X=o(\log^2X)
\]

and RH.

## 4. Native positive SHARP atom

The RH-sensitive source has the positive atom

\[
 w_\Psi(x,n)
 =w_2(x,n)+2w_1(x,n)
 =\frac{4\sqrt x}{n}-\frac3{\sqrt n}>0.
\]

The existing directed Hall corridors give the no-upward SHARP-source margin

\[
 \mathcal H_{\Psi,t}>rac35
\]

throughout the reset window.

For one rough prime,

\[
\boxed{
 w_\Psi(x,n)-w_\Psi(x,pn)
 =(1-p^{-1/2})w_\Psi(x/p,n)
 +4(1-p^{-1/2})\frac{\sqrt x}{n}.
}
\]

Thus one factor is one canonical child at the actual endpoint `x/p`, one
positive square-root slack, and one positive activation frontier.

## 5. Parallel overdraw firewall

`R-91305` proves that the one-prime partition cannot be applied independently
to every branch. At `x=10000`, the fifteen primes

```text
67,71,73,79,83,89,97,101,103,107,109,113,127,131,137
```

already demand more canonical-child source mass than the parent atom:

\[
 \sum_p(1-p^{-1/2})w_\Psi(10000/p,1)
 >\frac{9555}{24}
 >397
 =w_\Psi(10000,1).
\]

The missing source partition must therefore use disjoint least-prime labels
before the one-prime identity is applied. Branch-local positivity, by itself,
does not imply a subprobability tree.

## 6. Exact frontier

```text
branch-local physical port projection              CLOSED
fractional finite-child feasibility inference       REFUTED
sum-before-quantize parent assembly                 EXACT
branching reset consumer                            EXACT CONDITIONAL
native positive SHARP source atom                   EXACT
one-prime canonical child/slack/frontier split      EXACT
parallel independent one-prime allocation           REFUTED
least-prime positive source disintegration          OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVEN
```

The next legitimate attack is a source-level least-prime disintegration—most
likely a measure-valued Hall/Schur flow—not another branchwise norm estimate.
