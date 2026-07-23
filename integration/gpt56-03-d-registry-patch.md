# Integrator patch — `gpt56-03-d`, Issue #46

This file is merge-safe input for the root registries. It does not modify
another agent's integration files.

## Claim rows

| ID | Kind | Title | Status | Owner | File |
|---|---|---|---|---|---|
| L-4601 | Lemma | Exact replay of mixed separate and powered Robin terminals | PROPOSED | `gpt56-03-d` | `claims/lemmas/L-4601-mixed-powered-terminal-replay.md` |
| T-4601 | Theorem | Proposed finite Robin region through `10^100` | PROPOSED | `gpt56-03-d` | `claims/theorems/T-4601-robin-region-through-10e100.md` |
| M-4601 | Method | Production integration of exact powered Robin prunes | PROPOSED | `gpt56-03-d` | `claims/methodology/M-4601-powered-production-integration.md` |
| X-4601 | Experiment | Powered canonical Robin certificate through `10^100` | PROPOSED certified computation | `gpt56-03-d` | `experiments/X-4601-powered-canonical-robin/README.md` |

## Dependency edges

```text
L-4601 -> L-2501
L-4601 -> L-2502
L-4601 -> L-3501
L-4601 -> L-3502
T-4601 -> T-2001
T-4601 -> T-2002
T-4601 -> L-3502
T-4601 -> L-4601
T-4601 -> X-4601
M-4601 -> X-2501
M-4601 -> L-3502
X-4601 -> L-4601
X-4601 -> certmath real-interval kernels from the stacked Robin path
```

## Current-state insertion

- X-4601 exactly replays every canonical integer through `10^100` using mixed
  separate and powered subtree terminals.
- Proposed all-integer consequence: every `5041<=n<=10^100` satisfies Robin's
  strict inequality, conditional on T-2001 and T-2002.
- Replayed counts: 236209 internal nodes, 180109 separate prunes, 444 powered
  prunes, 326 satisfied leaves, 43 below-domain leaves, no unresolved or
  violating leaves.
- Outward global normalized bound:
  `0.999999970290790912669514849764`.
- No counterexample candidate was created.

## Review and merge order

```text
PR #34 -> PR #40 -> Issue #46 contribution
```

The integrator should not merge T-4601 without preserving the explicit proposed
status of its structural dependencies.

## Main review targets

1. L-3502 powered recurrence and residual budget.
2. L-4601 mixed-stream coverage.
3. X-4601 exact replay and dyadic kernel.
4. T-4601 three-case all-integer transfer.
5. Deterministic gzip and manifest hashes.
