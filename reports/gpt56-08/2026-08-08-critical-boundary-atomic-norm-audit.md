# Critical-boundary atomic-norm audit

Date: 2026-08-08  
Agent: `gpt56-08`  
Frozen target: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`

## Executive verdict

The proposed terminal adjacent-commutator proof does **not** survive the critical stopped-power boundary.

For the exact `x^(-1/2)` channel, the cutoff boundary on every integer

```text
N/3 < q <= N/2
```

is negative with magnitude at least

```text
1/(12 sqrt(q)).
```

On the declared next-half divisor state these are top coordinates, so their source coefficients are forced. The square-root atomic norm is therefore at least `N/84` for `N>=42`.

This contradicts the polylogarithmic boundary atomic-norm claim used to derive polylogarithmic Cycle Debt.

## Load-bearing theorem

See

```text
claims/refutations/
  R-30402-critical-quotient-two-boundary-has-linear-atomic-norm.md
```

The proof is elementary and does not use zeta zeros, prime estimates, or numerical reconnaissance.

## What is retained

The audit does not affect:

```text
shifted analytic 6/7 contraction;
adjacent central-tree divisor-source identity;
24 sqrt(m) capacity bound for one source atom;
local logarithmic cost of an actual paired shifted fiber;
Cycle-Debt duality and the conditional Cycle-Debt-to-RH consumer.
```

It refutes the composition which asserts that the **complete** cutoff boundary can be terminated on the strict next-half state at polylogarithmic total atomic cost.

## Why finite Euler transformation does not repair it

The finite jets and the exact Euler remainder sum to the same boundary function. On a fixed next-half divisor state the source representation is unique in its upper half. Therefore the sum of the atomic norms of all emitted components is at least the atomic norm of the complete boundary, which is linear in `N`.

A proof cannot obtain a polylogarithmic bound by decomposing the same unique top coordinates more finely.

## Corrected research frontier

The critical quotient-two boundary must remain coherent. This agrees with the independent live routes:

```text
factor-five quotient cells 2/3/4;
Selberg--Kummer endpoint null channel;
pole-preserving prime-annulus commutator;
full atomized carry-position normal Gram.
```

The correct full-problem architecture is now:

```text
strictly contracting analytic/transverse bank
+
coherent pole-preserving boundary bank
-> coupled lower-scale energy recurrence
-> RH.
```

The first bank may be controlled by atomic variation. The second may not.

## Exact status

```text
PR #304 full proof proposal                  rejected by R-30402
Riemann Hypothesis                          unproved
best exact boundary representation          atomized carry-position Gram
remaining theorem                           coupled interior/boundary recurrence
```

No reviewer is being asked to repair the rejected proof. Any replacement must contain the complete coherent boundary matrix and its lower-scale recurrence as part of the proof itself.
