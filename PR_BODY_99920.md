## Purpose

Republish the previously missing priority-Hasse surface packet on the corrected native normalized-box base, using a collision-free T-99920 namespace.

```text
base PR:      #667
base SHA:     7c044d232198265974dd8f4a530b98c6653dba55
head branch:  research/gpt56-pro/99920-native-priority-hasse-surface-retry
```

**RH remains unproved.**

## Binding correction

The normalized zero-free box has coefficient `beta(n)/n`, so every prime label has activity `1/p`, not `1/sqrt(p)`.  The prime 67 is represented by two independent labels of activity `1/67`, yielding the exact local fibres `1,-2/67,1/67^2`.

## Exact new results

1. coefficient-exact odd-to-even priority-Hasse flow on every finite weighted Euler cube;
2. exact activation truncation by the physical box potential;
3. arbitrary constrained min-cut bounded by one explicit upward first-owner flux;
4. exact Stieltjes product-boundary coarea for that flux;
5. exact Cauchy-Poisson Gram = coefficient-tail-square identity;
6. normalization and automatic-sign firewalls.

## Remaining theorem

```text
UPBF67:
  integral_2^Y sqrt(X) U_X dX/X = Y^o(1).
```

`UPBF67` implies subpower negative mass for the zero-free box and hence RH through PR #667's Mellin-Landau consumer.  It is not proved here.

## Replay

```text
PASS_T99920_NATIVE_PRIORITY_HASSE_SURFACE_REDUCTION
e112c829971ba9f25cdddab7d71edce17aa75a1a87071a7289ef0bf7b83ee208
```

```text
native priority-Hasse flow          PROVED
activation surface reduction        PROVED
Poisson-tail coarea                 PROVED
UPBF67                              OPEN / RH-BEARING
Riemann Hypothesis                  UNPROVED
```
