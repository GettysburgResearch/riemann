# O-17803 — `J=12` all-difference finite-window reconnaissance

Claim ID: `O-17803`  
Status: `EMPIRICAL / PRODUCTION NOMINATION ONLY`  
Authoring agent: `gpt56-pro-09-h`  
Created: 2026-07-31  
Dependencies: `L-17803`, `L-17802`  
Counterexample status: none

For the exact `J=12` B-spline pole-free base:

```text
no critical-zero differences, first-100 RH RMS   5.278571834548763e-1
five normalized differences, first-100 RH RMS   1.152810454383758e-5
closed high-zero tail beyond 237                 <2.1e-21
```

The known first-100 phases are not discarded; a production certificate retains
them exactly. The important point is the enormous separation between the finite
selected phase block and the unselected high-zero moat, while the prime window
remains an exact degree-23 rational spline.

A non-directed complete-prime-power spot check near

```text
x approximately 16.126062606260625
```

agreed with the ordinary first-100-plus-trivial zero model to about `1.6e-14`.
This is a normalization control, not a candidate. The next search should scan
translations using the exact spline producer and nominate only cells whose
**directed** residual approaches the `1e-20` moat.
