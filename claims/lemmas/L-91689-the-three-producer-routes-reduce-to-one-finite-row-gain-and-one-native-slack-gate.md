# L-91689 — The three producer routes reduce to one finite row-gain gate and one native-slack gate

Claim ID: `L-91689`  
Status: **PROVED SYNTHESIS / FAIL-CLOSED REDUCTION — FINAL SIGNS OPEN**  
Created: 2026-08-14  
Depends on: `L-91686`, `L-91687`, `L-91688`, PRs #464, #467, #468, #469  
RH status: **unproved**

## 1. Three candidate producers

The current graph contains three non-equivalent positive-entry mechanisms:

1. **native root score-Hall:** Hall only on the certified root window;
2. **target-Lorenz leaf producer:** remove the leftmost even target submeasure;
3. **Hall-free raw residual:** use `G_(p,y)=D_(P61,py)-p^(-1/2)D_(P61,y)`.

They share the same exact ordinary/detail response maps and the same source-ownership requirement.

## 2. What is now uniform and finite

The complete causal score and target profiles are ordered for every `p>=67`; every Lorenz cutoff is one of 185 even divisors below 2000; and `L-91687` proves that the complete `P_61` displacement-eight target and score transport polytopes are nonempty for every stopped leaf.

For a score flow `t_(o,e)`, every component-row gap is exactly
\[
 \sum_{o,e}t_{o,e}
 \left(\frac{K_R(e)}{K_S(e)}-\frac{K_R(o)}{K_S(o)}\right).
\tag{L-91689.1}
\]
All negative contributions are confined to upward edges of length at most eight and to the fixed child/frontier interface. For the target-Lorenz producer the fractional cutoff cancels and the row gate is the finite prefix determinant
\[
 \Pi_{j,c}(p,y)
 =R_{<c}^{(j)}K_T(c)-T_{<c}K_R^{(j)}(c).
\tag{L-91689.2}
\]
Thus the local producer question is finite in source nodes and activation types; the unbounded prime tail has an analytic monotone reduction.

## 3. What the raw-residual route closes and does not close

On rows for which its frozen sign theorem is available, the raw residual bypasses (L-91689.1)--(L-91689.2). But `R-91686` records that the cited universal frontier proof currently exceeds the frozen `L-91364` scope. Even after the row sign is completed, the raw current plus child is measured in canonical finite-Euler capacity, which equals native capacity plus the rough reservoir.

Therefore none of the three routes escapes the final native question:
\[
 \boxed{
 \sum_qY_4(q)
 [\Omega_X(q)-\Xi_{d_X^{\rm cur}}(q)]
 =o(\log^2X)
 }
\tag{L-91689.3}
\]
with source-disjoint children and one-use ports.

## 4. Exact two-gate frontier

A complete proof packet may choose any local producer, but must close both:

### Gate A — finite positive row gain

Return one of:

```text
a directed proof of every Lorenz prefix determinant;
a directed proof of every canonical shift-eight flow gain;
a complete all-frontier raw-residual row theorem.
```

### Gate B — native ownership and weighted slack

Use the rough coaction of `L-91686` to assign every reservoir fiber exactly once, prove current plus children fit one native ordinary/detail/port budget, and establish (L-91689.3). `L-91688` then permits one global endpoint correction.

Gate A is finite/local after the present work. Gate B is the remaining global arithmetic allocation theorem (`NRSLI/NRCT`).

```text
unbounded causal target/score feasibility          CLOSED
finite source cutoff                               CLOSED
formal rough ownership                             CLOSED
formal endpoint correction compatibility           CLOSED
finite row-gain certificate                         OPEN
native Y4-weighted slack and positive entry         OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVEN
```
