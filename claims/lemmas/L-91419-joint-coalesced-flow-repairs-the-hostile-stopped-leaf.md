# L-91419 — Joint coalescence repairs the hostile stopped leaf

Claim ID: `L-91419`  
Status: **PROVED DIRECTED FINITE LEAF THEOREM — ALL-PARAMETER PRODUCER SEPARATE**  
Created: 2026-08-14  
Depends on: exact `P_61` causal target/score atoms; positive component row `Q_Y(j)`; displacement-eight score Hall architecture  
Companion replay: `X-91412-joint-hostile-leaf-left-greedy`  
RH status: **unproved**

## 1. The reviewed counterexample

Independent review of PR `#451` proves that the **survival branch by itself** fails its stopped-leaf target Hall inequality at

```text
p = 67,
y = 13,
x = py = 871,
t = 13.
```

That refutes the universal branchwise Hall theorem. It does not rule out a producer which first coalesces survival and hazard in their common score currency.

## 2. Joint score transport

For every active squarefree divisor `d | P_61`, let

\[
K_T(d),\qquad K_S(d),\qquad K_R^{(j)}(d)\quad(2\le j\le66)
\]

be the exact causal one-prime target, score, and row atoms at `(p,y)=(67,13)`.
Split the positive score masses by Möbius parity. Process odd demands in increasing source order and fill the earliest available even capacities subject to

\[
e\le o+8.
\]

This is the deterministic left-greedy displacement-eight flow.

## 3. Exact gain ledger

For a score-mass flow `t_(o,e)`, define

\[
G_T=\sum_{o,e}t_{o,e}
\left(\frac{K_T(e)}{K_S(e)}-\frac{K_T(o)}{K_S(o)}\right)
\]

and, for each row,

\[
G_j=\sum_{o,e}t_{o,e}
\left(\frac{K_R^{(j)}(e)}{K_S(e)}-\frac{K_R^{(j)}(o)}{K_S(o)}\right).
\]

The interval replay reconstructs every greedy exhaustion decision and proves

\[
\boxed{G_T>1.9395281350378766}
\]

and

\[
\boxed{G_j>0\qquad(2\le j\le66).}
\]

The smallest row gain occurs at `j=66` and satisfies

\[
\boxed{G_{66}>0.008381548275463338.}
\]

The certified flow contains 151 source-labelled pieces and its largest upward displacement is only four.

## 4. Consequence

At this exact leaf, subtracting the transported odd score mass from the even source leaves one positive residual packet which is simultaneously

```text
score-exact;
target-subordinate;
coefficientwise row-subordinate in every row 2,...,66;
source-labelled;
causal with displacement at most eight.
```

Thus the exact PR `#456` falsifier is repaired by **joint survival-hazard coalescence before Hall**. No false survival-only prefix inequality is reintroduced.

## 5. Boundary

This theorem is a directed theorem for the hostile leaf, not an all-parameter proof. The universal completion still requires the same joint gain inequalities for every stopped leaf or an equivalent finite-cone certificate.

```text
survival-only stopped-leaf Hall                 FALSE / PR #456
joint hostile-leaf score flow                   EXACT
joint hostile-leaf target gain                  STRICTLY POSITIVE
joint hostile-leaf gains in all 65 rows         STRICTLY POSITIVE
all-parameter joint producer                    OPEN
Riemann Hypothesis                              UNPROVEN
```
