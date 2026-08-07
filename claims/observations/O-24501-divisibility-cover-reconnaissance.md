# O-24501 — Divisibility-cover reconnaissance

Claim ID: `O-24501`  
Status: `FLOATING_RECONNAISSANCE — not proof`  
Scope: numerical scheduling for the stronger monotone cover route  
Issue: #245

The stronger sufficient theorem in `L-24502` asks for nonnegative atoms `alpha_m` such that

\[
\sum_{kq\le X}\alpha_{kq}\ge e_X(q),
\qquad
\sum_{t=m}^X\alpha_t\le b_X^{(0)}(m),
\]

while minimizing the exact objective loss

\[
\sum_m\alpha_m\log m.
\]

I solved this finite LP in ordinary floating point for several small/moderate scales. This is reconnaissance only.

Representative minimum costs were approximately

```text
X=100      0.2621
X=200      0.9062
X=500      2.5954
X=800      3.9606
X=1000     4.7683
X=1500     6.5142
```

For comparison, `(log X)^2` over the same range is roughly `21` through `53`, while `sqrt(X)` is roughly `10` through `39`.

At every tested scale the LP was feasible with the tail-capacity constraints included. The optimizer was sparse and typically used roughly one atom per initially violated prime-power constraint, often placing atoms on integers with several useful divisors.

This suggests a possible stronger closure:

```text
explicit divisibility packing
-> cover all low-ratio prime-power excess
-> exact tail capacity
-> O(log^2 X) weighted cost
-> no Jacobi convergence theorem needed.
```

The present data do not prove any asymptotic rate. They should be used only to search for a constructive packing lemma, perhaps by assigning each violated prime power to a controlled multiple in a disjoint or bounded-overlap interval family.

## Proposed combinatorial target

A particularly attractive target is a Hall-type packing theorem: construct a map from prime-power deficit masses to multiples in dyadic/rightward bins so that

1. each prime power `q` receives total assigned mass at least `e_X(q)`;
2. the total mass assigned at an integer `m` is at most a local capacity derived from `b_X^(0)(m)-b_X^(0)(m+1)` or a tail-capacity decomposition;
3. each unit of assigned mass pays `O(log X)` and the total assigned mass is `O(log X)`.

Together these would imply the `O(log^2 X)` cover cost.

## Status boundary

All numbers in this file are ordinary floating-point LP output. No certificate, asymptotic theorem, or RH claim is made.
