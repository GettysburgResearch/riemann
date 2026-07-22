# Integrator patch — gpt56-03-b Robin verification and search kernels

This file is intentionally additive and merge-safe. The integrator should reconcile statuses and root registries after PR #19 and this stacked contribution are reviewed.

## Claim rows

| ID | Kind | Title | Status | Owner | File |
|---|---|---|---|---|---|
| L-2001 | Lemma | Atanh-series enclosure for the real logarithm | PROPOSED | `gpt56-03-b` | `claims/lemmas/L-2001-atanh-log-enclosure.md` |
| L-2002 | Lemma | Elementary two-sided enclosure for Euler's constant | PROPOSED | `gpt56-03-b` | `claims/lemmas/L-2002-euler-gamma-harmonic-enclosure.md` |
| L-2003 | Lemma | Positive Taylor enclosure for the exponential | PROPOSED | `gpt56-03-b` | `claims/lemmas/L-2003-exp-taylor-enclosure.md` |
| L-2004 | Lemma | Safe fixed-support Robin branch pruning | PROPOSED | `gpt56-03-b` | `claims/lemmas/L-2004-fixed-support-robin-pruning.md` |
| L-2005 | Lemma | Canonical prime-support and exponent-order dominance | PROPOSED | `gpt56-03-b` | `claims/lemmas/L-2005-canonical-exponent-support-dominance.md` |
| T-2001 | Theorem | Independent certified Robin finite barrier | PROPOSED | `gpt56-03-b` | `claims/theorems/T-2001-independent-robin-finite-barrier.md` |
| T-2002 | Theorem | Hardy--Ramanujan completeness for Robin search | PROPOSED | `gpt56-03-b` | `claims/theorems/T-2002-hardy-ramanujan-completeness.md` |
| O-2001 | Observation | Robin superabundance quantifier warning | PROPOSED | `gpt56-03-b` | `claims/observations/O-2001-robin-superabundant-quantifier-warning.md` |
| X-2001 | Experiment | Independent exact/dyadic Robin finite barrier | PROPOSED | `gpt56-03-b` | `experiments/X-2001-independent-robin-barrier/README.md` |

## Dependency edges

```text
L-2001 -> X-2001
L-2002 -> X-2001
L-2003 -> X-2001
X-2001 -> T-2001
L-0201 -> T-2001
L-2005 -> T-2002
T-2001 -> T-2002
T-2002 -> future complete canonical search
L-2004 -> future complete canonical search
ChoieLichiardopolMoreeSole2007 -> O-2001
Vojak2020 -> O-2001
```

## Status recommendation for existing work

X-2001 independently reproduces the exact maxima and both X-0202 transcendental signs, with no discrepancy. This removes the specific independent-backend blocker recorded in T-0201. The integrator should nevertheless keep T-0201 below `INDEPENDENTLY_VERIFIED` until:

1. X-2001's code and the proof lemmas receive review;
2. Robin's equivalence theorem has the source status required by project policy;
3. PR #19 and this stacked PR are reconciled without losing exact certificate paths.

## New barrier and search facts

- `5583` is certified as the first integer where `e^gamma log log n` exceeds `403/105`.
- A complete counterexample search may be restricted constructively to consecutive-prime, nonincreasing-exponent vectors.
- A fixed-support subtree may be discarded using L-2004's exact rational ceiling.
- No complete restriction to the colossally abundant transition spine is added.
