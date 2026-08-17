## Purpose

Reconcile the unpublished stronger checkerboard/Cauchy–Binet/global-Hall
description with the actual PR #567 artifact.

This is an explicit fail-closed correction, not a silent substitution.

## Freeze

```text
base PR:      #567
base SHA:     50e596560b4f6f423e87fd6718d74913d863df99
head branch:  research/gpt56-pro/97210-checkerboard-cauchy-binet-reconciliation
```

## Exact finding

The earlier prose asserted two sign implications that were not proved:

1. unique one-owner incidence does not imply nonnegative minors;
2. positive terminal coordinates do not imply a terminal checkerboard.

The packet gives exact \(2\times2\) counterexamples to both inferences. It
recovers the correct conditional Cauchy–Binet theorem and the exact
fractional-knapsack form of global Hall.

```text
PR #567                             intentional retraction
terminal checkerboard               not proved
owner-incidence TN                  not proved
Cauchy–Binet                        exact conditional theorem
fixed-endpoint Hall optimizer       exact
GPHT* / TFPE / ACBI                 open / RH-bearing
Riemann Hypothesis                  unproved
```

Expected replay:

```text
PASS_T97210_CHECKERBOARD_RECONCILIATION
```
