# O-91416 — Three independent routes attack the last literal row-provenance gate

Claim ID: `O-91416`  
Status: **CURRENT RESEARCH CAMPAIGN — NEW STRENGTHENINGS PENDING REVIEW**  
Created: 2026-08-13  
Depends on: `L-91410` through `L-91415`  
RH status: **unproved**

The live factor-54 path no longer uses the refuted positive binary return.  Its first open physical statement is literal row provenance for the causal `P_61` packet.  Three independent routes now attack that statement.

## Route A — actual-cutoff determinant

`L-91411` proves that the exact Lorenz residual is row-subordinate once

\[
\Delta_{j,c}=R_{sig}^{(j)}S_c-S_{sig}R_c^{(j)}>=0
\]

at the actual cutoff.  `L-91412` shows that the centered source kernel has one sign change there.

The discrete domain has 65 rows and 184 possible cutoff nodes.  `O-91414` derives a positive first surviving asymptotic term

\[
5(-\lambda_j)\sqrt y(A/\sqrt c-B/c)\sqrt p\log p.
\]

Remaining work:

1. make the common remainder effective and obtain `P_0`;
2. certify `67<=p<P_0` by directed activation cells.

This is currently the shortest direct route.

## Route B — discrete Lorenz/Monge theorem

The stronger full determinant is

\[
D_j^{full}=E_R^{(j)}O_S-E_SO_R^{(j)}.
\]

`L-91410` orders every child-active ratio above every frontier ratio.  `L-91413` proves monotonicity whenever the child row is inactive; no odd active-child comparison exists in rows `34,...,66`.  The unresolved order family is therefore confined to rows `2,...,33` and finitely many divisors below `67/j`.

Let

\[
A_- =\prod_{q\le61}(1-q^{-1}),
\quad B_- =\prod_{q\le61}(1-q^{-1/2}),
\]

\[
A_+ =\prod_{q\le61}(1+q^{-1}),
\quad B_+ =\prod_{q\le61}(1+q^{-1/2}).
\]

The proposed first surviving full-determinant term is

\[
\frac{5(-\lambda_j)\sqrt y}{2}
(B_+A_- -B_-A_+)\sqrt p\log p>0.
\]

The sign follows from `B_+/A_+>B_-/A_-`.

Remaining work:

1. directed proof of finite active-child divisor ordering;
2. effective full-determinant tail;
3. compact full-determinant replay.

This route is stronger than Route A and may yield the cleanest structural theorem.

## Route C — canonical shifted-eight Hall gain

`L-91415` gives

\[
R_{sig}-R_{res}=\sum_{o,e}t_{o,e}(q_e-q_o)
\]

for any score-mass Hall flow.  Use the canonical left-greedy radius-eight flow instead of the unconstrained Lorenz removal.

Every unbounded no-upward sector is already favorable.  The unresolved gain is confined to local upward edges, activation-straddling pairs below `67`, and active-child pairs in rows `2,...,33`.  On each Hall cell, the greedy coefficients are repeated minima of affine score masses, so the aggregate gain is piecewise analytic and directly certifiable.

Remaining work:

1. generate the exact greedy flow basis on every causal cell;
2. certify the aggregate row gain rather than each edge separately;
3. isolate a stabilized analytic tail.

This route bypasses both determinant conditions.

## Empirical comparison

`X-91410` is explicitly non-proof reconnaissance.  On 120 sparse-grid cases, all five monitored quantities were positive:

```text
actual cutoff determinant;
full even/odd determinant;
literal Lorenz row gap;
inner discrete-order gap;
left-greedy shifted-eight row gain.
```

The smallest sampled point was the first-cell high-row case `p=67,y=1,j=66`, where the cutoff row is inactive and Route A is automatic.  These values guide proof engineering only.

## Priority

Recommended attack order:

1. Route A for the fastest source-bound certificate;
2. Route C as an independent constructive packet proof;
3. Route B for a stronger structural theorem and cross-check.

A failure in one route does not refute the others.

```text
secant/interface theorem          PROVED / L-91410
cutoff determinant reduction      PROVED / L-91411
one-crossing centered kernel      PROVED / L-91412
inactive-child monotonicity        PROVED / L-91413
asymptotic determinant signs      PROPOSED ANALYTIC
Hall edge-gain identity           PROVED / L-91415
one complete all-parameter route  OPEN
Riemann Hypothesis                UNPROVEN
```
