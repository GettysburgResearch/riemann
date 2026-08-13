# L-91402 — Paired least-prime sources may be regrouped at a stopping line before physical observation

Claim ID: `L-91402`  
Status: **PROVED EXACT SOURCE-TREE REGROUPING THEOREM**  
Created: 2026-08-13  
Depends on: exact paired recursion `L-91333`; finite Boolean expansion; Tonelli for positive measures  
RH status: **unproved**

## 1. Paired source recursion

For a fixed parameter `a>=1`, retain the positive paired parity source

\[
\mathbf P_j^{(a)}(x)=(E_j^{(a)}(x),O_j^{(a)}(x))
\]

and its exact least-prime recursion

\[
\boxed{
\mathbf P_j^{(a)}(x)
=\binom{a\sqrt x-1}{0}
+\sum_{k\ge j,\ p_k\le x}
 p_k^{-1/2}S\mathbf P_{k+1}^{(a)}(x/p_k).
}
\tag{L-91402.1}
\]

Every summand is a positive measure, the parameter `a` is preserved, and every squarefree source atom occurs exactly once.

## 2. Positive stopping lines

Let `\mathcal S` be any stopping line in the least-prime tree: no root-to-leaf path meets it twice, and every infinite active path meets it or terminates in the finite forcing.

Iterating (L-91402.1) and applying monotone convergence gives the exact positive measure identity

\[
\boxed{
\mathbf P_j^{(a)}(x)
=\mathbf O_{\mathcal S}^{(a)}(x)
 +\sum_{v\in\mathcal S}c_vS^{|v|}
   \mathbf P_{j(v)}^{(a)}(x_v),
}
\tag{L-91402.2}
\]

where

\[
c_v=\prod_{p\in v}p^{-1/2},
\qquad
x_v=x\prod_{p\in v}p^{-1},
\]

and `\mathbf O_\mathcal S` is the positive forcing/frontier accumulated before stopping.

The leaf packets are source-disjoint. In particular, their positive source masses form a submeasure of the parent source.

## 3. Finite-block regrouping

Fix the finite block `P_79` and stop immediately after the first unabsorbed rough prime has moved the local endpoint into `1<=y<83`.

Before applying any signed physical observation, sum all finite small-prime Boolean states attached to one stopped leaf. Unique factorization gives exactly the complete finite packet

\[
\boxed{
\sum_{d\mid P_{79}}d^{-1/2}S^{\omega(d)}
\mathbf P_{>79}^{(a)}(py/d),
}
\tag{L-91402.3}
\]

and its terminal child with the exact least-prime coefficient

\[
\boxed{
p^{-1/2}S
\sum_{d\mid P_{79}}d^{-1/2}S^{\omega(d)}
\mathbf P_{>79}^{(a)}(y/d).
}
\tag{L-91402.4}
\]

Thus the complete finite-block Euler identity is applied to a complete paired packet, not to one coordinatewise hazard slice.

## 4. Hidden-hazard firewall

The diagonal hidden decomposition has different hazard coefficients in its `X` and `Y` coordinates. A pure reserve hazard therefore need not be an `r`-scaled canonical child; the exact PR #431 counterexample remains valid for that literal statement.

The present theorem does not use that decomposition. It uses the paired squarefree source tree, in which the coefficient `p^{-1/2}` multiplies the complete parity pair and its parameter label before physical observation.

Consequently the hidden calculation

```text
hazard target = 2r,
hazard score  = r^2
```

is not a contradiction to the regrouped paired packet. It is a warning not to observe or normalize the hidden coordinates before regrouping.

## 5. Compatibility with packet-valued branching

The stopped packets in (L-91402.2) need not be scalar copies of one preferred native packet. They are actual positive subpackets, and their masses sum to at most the parent mass.

They therefore satisfy the source-side hypothesis of the packet-envelope consumer `T-91401`, provided the local row/capacity producer proves (T-91401.7).

## 6. Proof boundary

```text
paired least-prime recursion                       EXACT
arbitrary positive stopping-line identity          EXACT
finite small-prime regrouping before observation   EXACT
source-disjoint stopped packet ledger               EXACT
hidden-hazard literal child identification          NOT USED / REMAINS FALSE
local stopped-packet row/capacity producer           OPEN
packet-envelope recurrence                          AVAILABLE
Riemann Hypothesis                                  UNPROVED
```
