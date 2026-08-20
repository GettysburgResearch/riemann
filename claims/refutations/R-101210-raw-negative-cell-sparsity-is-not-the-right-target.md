# R-101210 — Raw negative-cell sparsity is not the stable incidence target

Claim ID: `R-101210`  
Status: **FINITE DIAGNOSTIC FIREWALL; NO ASYMPTOTIC REFUTATION**  
Created: 2026-08-21

A direct evaluation of the exact `L-101210` cell state through `N<10^6` finds large dyadic populations of shallowly negative cells. Representative complete blocks include

```text
L=15: 19780 of 32768 cells contain a negative point;
L=16: 37526 of 65536;
L=17: 72247 of 131072;
L=18: 103803 of 262144.
```

This is diagnostic evidence only. It neither proves nor refutes asymptotic subpower sparsity. Its binding methodological consequence is narrower:

> a proof should not assume that negativity itself is rare merely because several auxiliary producers are positive.

`L-101211` repairs the target by permitting dense shallow negativity and asking only for sparsity of cells below a subpower negative threshold.
