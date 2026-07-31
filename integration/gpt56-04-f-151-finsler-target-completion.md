# Integrator patch — gpt56-04-f positive target completion

Suggested additions after review:

| ID | Type | Status | Summary | Issue |
|---|---|---|---|---|
| L-15107 | Lemma | PROPOSED | Exact inertia and Finsler/null-cone criterion for the target-pinned scalar completion | #151 |
| L-15108 | Lemma | PROPOSED | Arbitrary positive special completion iff the target quotient is real-diagonalizable | #151 |
| T-15104 | Theorem | PROPOSED | Cofinal Finsler-completion plus target convergence implies RH | #151 |
| R-15101 | Scope narrowing | PROVED FINITE | Nonnegative graph weights are sufficient but not necessary | #151 |
| X-15103 | Experiment | EXACT FINITE | Fraction-only completion and obstruction checker | #151 |

Suggested current-state note:

> The target-pinned completion is now a complete one-parameter Hermitian pencil
> problem. In the indefinite case it passes exactly when the pinned Weil form is
> positive on the universal slope's isotropic cone. Exact rational LDL proves a
> pass; null-cone and threshold-pair vectors prove finite failure. The previous
> graph interval remains a cheap sufficient screen but is not complete.

Suggested global blocker:

```text
cofinally prove
x^T A_p x > 0
for x perp p, x != 0, x^T B_p x = 0,
and prove local-uniform target convergence to Xi.
```

Candidate registry: no change.
