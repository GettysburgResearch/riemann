# L-91415 — Hall row provenance is exactly a local edge-gain ledger

Claim ID: `L-91415`  
Status: **PROVED EXACT TRANSPORT IDENTITY — CANONICAL FLOW SIGN OPEN**  
Created: 2026-08-13  
Depends on: causal score Hall; `L-91410`; `L-91413`  
RH status: **unproved**

## 1. Score-mass transport

Let `E` and `O` be the positive even and odd causal score measures.  Let

\[
 t_{o,e}>=0
\]

be any score-mass transport satisfying

\[
 \sum_e t_{o,e}=S_o,
 \qquad
 \sum_o t_{o,e}<=S_e.
 \tag{L-91415.1}
\]

Write

\[
 q_d=\frac{R_d}{S_d}.
\]

The positive residual row after transport is

\[
 R_{\rm res}
 =E_R-\sum_{o,e}t_{o,e}q_e.
 \tag{L-91415.2}
\]

The literal signed arithmetic row is

\[
 R_{\rm sig}
 =E_R-O_R
 =E_R-\sum_{o,e}t_{o,e}q_o.
 \tag{L-91415.3}
\]

Subtracting gives the exact identity

\[
 \boxed{
 R_{\rm sig}-R_{\rm res}
 =\sum_{o,e}t_{o,e}(q_e-q_o).
 }
 \tag{L-91415.4}
\]

Thus a chosen Hall flow is literally row-subordinate if and only if its total row gain is nonnegative.

## 2. Shift-eight localization

The causal Hall theorem supplies a flow with

\[
 e<=o+8.
 \tag{L-91415.5}
\]

For child-inactive sources `e,o>y`, `L-91359` gives

\[
 e<=o\Longrightarrow q_e>=q_o.
 \tag{L-91415.6}
\]

For child-active sources whose child rows are both inactive, `L-91413` gives the same implication.  Across the child/frontier interface, `L-91410` gives the strict orientation

\[
 o<=y<e\Longrightarrow q_o>=q_e.
 \tag{L-91415.7}
\]

Consequently every unresolved negative term in (L-91415.4) is confined to:

```text
local upward edges o<e<=o+8;
activation-straddling inner comparisons;
active-child comparisons in rows 2,...,33.
```

All source nodes involved in the latter two classes lie below `67`.  The unbounded source tail is child-inactive and already ordered.

## 3. Canonical left-greedy route

Choose the left-greedy Ferrers transport: process odd demands in increasing source order and fill the earliest available even capacities.  The flow is uniquely determined away from ties and changes only when:

```text
an arithmetic source activates;
an even capacity is exhausted;
an odd demand is exhausted;
the child endpoint crosses a divisor;
the parent endpoint crosses a divisor.
```

On each resulting cell, every `t_(o,e)` is obtained by repeated minima of affine score masses, and the gain in (L-91415.4) is an explicit piecewise analytic function.

Therefore the all-parameter proof can be organized as:

1. exact symbolic checks for every local edge type;
2. directed cell checks only where competing capacities exchange order;
3. an analytic tail after all local source patterns stabilize.

No global nonlinear Hall-commutation theorem is required.

## 4. Relation to the determinant route

The Lorenz residual of `L-91411` is the unconstrained leftmost score removal.  Its row gap is controlled by one cutoff determinant.  Equation (L-91415.4) gives an independent route: retain the actual radius-eight causal flow and certify its aggregate gain directly.

A failure of one route does not imply failure of the other because the two residual measures are different.

## 5. Boundary

```text
transport row-gap identity                    EXACT
outer no-upward edge gains                    NONNEGATIVE EXACT
inactive-child no-upward edge gains            NONNEGATIVE EXACT
unbounded adverse-edge family                  ELIMINATED
remaining local edge family                    FINITE
canonical left-greedy aggregate gain           OPEN / DIRECTED
literal row provenance after nonnegative gain  IMMEDIATE
Riemann Hypothesis                             UNPROVEN
```
