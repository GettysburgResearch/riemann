# 2026-08-13 — Adversarial repair of the candidate factor-54 closure

## Freeze

```text
live candidate PR: #424
reviewed head:     7c0927e9364e191c720d5a618928d99847ac8edd
parent PR:         #399 at 22d7f2f3f3668f664c09708838f6a738e4398eef
producer PR:       #416 at 23aa9adc48a6c3176b799944dfbac11e665407ef
RH status:         UNPROVED
```

## Executive verdict

PR #424 contains the strongest factor-54 composition yet written, but its
physical child-lift chain is not valid as stated.

`L-91540/L-91547` prove positivity after retaining the contracted child at the
same component-row indices.  `L-91547.5`, `L-91549` and `T-91551` then replace
that child by the affine Pascal lift.  The replacement does not preserve the
positive residual.  The exact witness is

\[
 p=67,\quad Y=201,\quad j=2,\quad \Phi_{67}(2)=200,
\]

for which

\[
 Q_{201}(200)<\frac1{2000}
 \quad\text{but}\quad
 67^{-1/2}Q_3(2)>\frac1{10}.
\]

Therefore the candidate chain does not yet establish RH.

The failure is repairable: after Hall residualization has deliberately erased
arithmetic color provenance, recursively chosen child packings can be included
at the same physical indices.  The radix-four target is monotone in the
endpoint, so this inclusion is capacity-faithful and exactly preserves entropy
score.

## I. Exact firewall against the affine composition

The same-index type identity is

\[
 Q_Y(j)=Q_{Y/67}(j)+[Q_Y(j)-Q_{Y/67}(j)],
 \qquad Q_Y(j)-Q_{Y/67}(j)\ge0.
\]

The affine lift is

\[
 j\mapsto67(j+1)-1,
 \qquad d(j)\mapsto67^{-1/2}d(j).
\]

They are separate valid operations.  `R-91560` proves that they cannot be
identified while keeping the same positive residual.

## II. Loss-isometric same-index replacement

The explicit detail target

\[
 \Omega_X(q)=
 \begin{cases}
 0,&X<q,\\
 q^{-1/2}\log(X/q),&q\le X<4q,\\
 q^{-1/2}\log4,&4q\le X
 \end{cases}
\]

is nondecreasing in `X`.  Consequently every detail-feasible child packing at
`Y<=X` remains detail feasible at `X` without moving a row index.  Its entropy
score is unchanged.

For child target weights `omega_b` with `sum omega_b<=1`,

\[
 d_X^{child}=\sum_b\omega_bd_b
\]

is parent feasible and its inherited loss is exactly

\[
 \sum_b\omega_b\ell_{Y_b}(d_b).
\]

This closes the arbitrary-child lift required by the substochastic consumer,
without an affine normalization joint.

## III. Correct actual-loss dictionary

A paired kernel packet carries three ledgers:

```text
T: carry/SHARP target;
S: native entropy-score source;
H(row): actual entropy of the finite row.
```

The native loss is

\[
 S-H(row),
\]

not `T-S`.  The one-atom type

\[
 (a_T,b_T,a_S,b_S,\kappa)=(1,0,1,0,0)
\]

has `T=S>0`, zero row entropy, and therefore positive actual loss despite zero
`[T-S]_+` debt.

The correct local debt is

\[
 [D_S-H(D_R)]_+.
\]

For the physical survival/hazard corridor,

\[
 0\le D_S\le2D_T,
\]

so target normalization gives a uniform local debt at most two.  A
substochastic factor-67 tree still yields `O(log X)` loss.

## IV. Exact component-row entropy bridge

For the exact component row and average-binomial entropy,

\[
 \mathcal H(Y)=\sum_jQ_Y(j)G_j,
\]

swapping the triangular sums yields

\[
 \boxed{
 \mathcal H(Y)
 =\sum_{2\le m\le Y}
  \frac{\log m}{\sqrt m}\log\frac Ym.
 }
\]

The coefficient collapse is exact: the coefficient of the atom at `m` is
`log m`.  It follows from

\[
 \frac{P_mP_{m-2}}{P_{m-1}^2}
 =\left(\frac m{m-1}\right)^{m-1},
 \qquad
 P_j=\prod_{r=0}^j\binom jr.
\]

A directed certificate gives

\[
 \mathcal H(67)>5\sqrt{67}-3
\]

with certified margin greater than `1.2764`.  A last-two-thirds derivative
bound then proves

\[
 \mathcal H(Y)>5\sqrt Y-3
 \qquad(Y\ge67).
\]

More strongly, for every `p>=67` and `Y>=p`,

\[
 \boxed{
 \mathcal H(Y)-\mathcal H(Y/p)
 >5(1-p^{-1})(1-p^{-1/2})\sqrt Y.
 }
\]

This is exactly the survival score residual in the canonical unscaled row type;
the hazard score residual is smaller.  Hence the actual inherited component-row
residual has favorable entropy whenever the Hall producer normalization is
`kappa=1`.

## V. Corrected proof DAG

```text
native finite forcing
 -> target-exact survival/hazard Hall entry
 -> hereditary positive residual sources + positive Hall row bonuses
 -> fixed target split to X/67
 -> same-index inclusion of arbitrary child packings
 -> actual loss S-H(row), local debt <=2 residual target
 -> target-subprobability factor-67 tree
 -> O(log X)=o(log^2 X) native loss
 -> PR #352 consumer
 -> RH.
```

Every arrow after the first producer is now an exact abstract theorem in this
packet.

## VI. Sole remaining producer audit

The factor-54 proof is not established until one reconstructs, from definitions,
all of the following in one normalization:

1. the score of each Hall residual is literally its contribution to
   `J_Lambda`;
2. every Hall bonus and common-port row is detail feasible before its entropy is
   counted;
3. current rows consume only the complement of the same-index child target;
4. the finite safety factor, top omission, collar and common endpoint port are
   charged once;
5. the Hall residual component-row coefficient is the canonical `kappa=1`;
6. the finite target-normalized base is uniform for both hereditary types.

The first failed affine joint has been removed.  The remaining problem is now a
finite source-to-detail-capacity reconstruction, not a branching or mass-to-score
problem.

## Verification

```text
PASS_FACTOR54_ACTUAL_ENTROPY_AND_CHILD_LIFT_REPAIR
checks: 10476
K_m=log m exact range: 2..201
certified H(67) margin: >1.2764007195
```

## Status

```text
PR #424 affine child composition                    REFUTED EXACTLY
same-index arbitrary child inclusion                EXACT REPAIR
actual loss dictionary                              CORRECTED EXACTLY
component-row entropy identity                      EXACT
rough residual entropy domination                   EXACT
actual-entropy branching consumer                    EXACT CONDITIONAL
native Hall/port/detail producer                     OPEN / FINAL AUDIT
Riemann Hypothesis                                   UNPROVEN
```
