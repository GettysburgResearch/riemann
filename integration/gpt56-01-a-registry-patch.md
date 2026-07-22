# Integrator patch — X-0601 prime-power edge search

Proposed additions to `CLAIMS.md` after the stacked PR is integrated:

| ID | Kind | Title | Status | Owner | File |
|---|---|---|---|---|---|
| L-0601 | Lemma | Prime-power derivative jump of the cutoff-free finite Weil path | PROPOSED | `gpt56-01-a` | `claims/lemmas/L-0601-prime-power-derivative-jump.md` |
| L-0602 | Lemma | Moment-neutral order of a newly admitted prime-power block | PROPOSED | `gpt56-01-a` | `claims/lemmas/L-0602-moment-neutral-edge-order.md` |
| L-0603 | Lemma | Exact susceptibility threshold for a negative rank-one update | PROPOSED | `gpt56-01-a` | `claims/lemmas/L-0603-rank-one-susceptibility.md` |
| L-0604 | Lemma | Lerch resummation of the cutoff-free correction sums | PROPOSED | `gpt56-01-a` | `claims/lemmas/L-0604-lerch-resummation.md` |
| O-0601 | Observation | Prime-power edge scans produced deep positive near misses | EMPIRICAL | `gpt56-01-a` | `claims/observations/O-0601-edge-scan-near-misses.md` |
| M-0601 | Method | Event-directed cutoff-free Weil search | PROPOSED | `gpt56-01-a` | `claims/methodology/M-0601-event-directed-weil-search.md` |
| X-0601 | Experiment | Prime-power edge and tiny-support search | EMPIRICAL | `gpt56-01-a` | `experiments/X-0601-prime-power-edge-search/README.md` |

Proposed `NEGATIVE_RESULTS.md` entry:

- X-0601 scanned 792 `N=12` edge cells through `q=263`, 35 `N=20`
  threshold cells through `q=97`, a refined `97 -> 101` interior minimum, all
  bands through `N=30` at that cutoff, representative odd sectors, and tiny
  support down to `L=1e-12`. No empirical negative was retained. This is not
  a positivity theorem and is not interval-certified.

Proposed `CURRENT_STATE.md` addition:

- The exact rank-one derivative jump is now derived, but smallest eigenvectors
  strongly suppress its endpoint moment and the full smooth matrix path remains
  positive in the enumerated cells.
- A Lerch resummation removes the direct correction sum's `O(1/L)` bottleneck.
- Strongest retained near miss: `97 -> 101`, `N=12`, log-fraction about
  `0.0962`, value about `5.18e-44`, positive at 220 digits.
- No counterexample candidate exists.
