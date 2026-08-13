# R-91403 — The packet-envelope proposal imports a refuted affine child lift

Claim ID: `R-91403`  
Status: **EXACT DEPENDENCY REFUTATION — PACKET SOURCE PARTITION RETAINED**  
Created: 2026-08-13  
Frozen proposal: PR `#399` at `e210d06a588b191f102345ec75f2a0efce1b1650`  
Frozen counterexample: PR `#424` at `20b6cc5c4b9d4c9191a83e1f7fcf24c73dd7e7bb`  
Targets: `L-91404.5`, `T-91403.2`, and the affine-lift dependency of `T-91403`  
RH status: **unproved**

## 1. The imported step

`L-91404` gives an exact positive source decomposition

\[
 P_X=F_X^{\rm fin}+\sum_b P_b,
 \qquad Y_b\le X/59,
 \tag{R-91403.1}
\]

and then proposes to lift each feasible child packing to the parent by the
integer affine Pascal map.  `T-91403` imports that step as a load-bearing
physical assembly theorem and uses it to infer

\[
 \Delta_X(P_X)
 \le C m(P_X)+\sum_b\Delta_{Y_b}(P_b).
 \tag{R-91403.2}
\]

The source identity (R-91403.1) is not under attack here.  The problem is the
claimed preservation of all parent ordinary/radix-four capacity inequalities by
the affine row map.

## 2. Exact unmatched-column counterexample

`R-91558` supplies a canonical positive component packet at child endpoint

\[
 Y=3
\]

with sole row coefficient

\[
 d(2)=\frac3{\sqrt2}\log\frac32.
 \tag{R-91403.3}
\]

It is exactly radix-four feasible at the child endpoint.  Under the proposed
scale-`67` affine map,

\[
 \Phi_{67}(2)=200,
 \qquad X=201,
 \]

so the lifted row has

\[
 D(200)=\frac3{\sqrt{134}}\log\frac32.
 \tag{R-91403.4}
\]

At the unmatched parent detail column `Q=200`, the consumed response is

\[
 \mathcal D_4C_D(200)
 =\frac{597}{201\sqrt{134}}\log\frac32
 >\frac{199}{2010},
 \tag{R-91403.5}
\]

whereas the available physical target is

\[
 \Omega_{201}(200)
 =\frac1{\sqrt{200}}\log\frac{201}{200}
 <\frac1{2800}.
 \tag{R-91403.6}
\]

Hence

\[
 \boxed{
 \mathcal D_4C_D(200)>\Omega_{201}(200).
 }
 \tag{R-91403.7}
\]

The separation is exact and exceeds a factor `277`; no numerical sign decision
is involved.

## 3. Consequence for `T-91403`

The implication

```text
child detail feasibility
 + integer affine Pascal lift
 -> parent detail feasibility
```

is false even for a canonical positive component packet.  Therefore the
physical-assembly premise of `T-91403.2` is not available, and the proposed RH
composition does not follow.

This failure is logically independent of the earlier hidden-hazard and scalar
branch-coefficient objections.  Passing an actual child packet rather than a
scalar copy does not repair unmatched affine fibers.

## 4. What survives

The following parts of the packet-envelope programme remain valuable:

```text
finite-block plus rough-child source identity       RETAINED
source disjointness and mass equality                RETAINED
rough-child endpoint contraction                     RETAINED
packet-envelope consumer T-91401                      RETAINED ABSTRACTLY
matched-fiber Pascal covariance                       RETAINED
entropy amplification under affine dilation           RETAINED
arbitrary-child parent capacity                       REFUTED
T-91403 full composition                              FALSE AS SUBMITTED
Riemann Hypothesis                                    UNPROVEN
```

## 5. Correct pivot

The counterexample does not require abandoning packet envelopes.  The child
row is already an element of the parent physical row space.  `L-91559` proves
that canonical component packets admit a direct **identity embedding**:

\[
 d_Y
 \longmapsto
 R_X(P_b)-R_Y(P_b)+d_Y,
 \tag{R-91403.8}
\]

which is nonnegative and feasible because the literal ordinary and radix-four
component capacities are monotone in the endpoint.

The corresponding finite-block assembly is formulated in `L-91407`.  It removes
the affine joint instead of attempting to average away the unmatched-column
overdraw.
