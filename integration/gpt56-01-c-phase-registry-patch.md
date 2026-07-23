# Integrator patch — gpt56-01-c phase-certification continuation

Suggested additions:

| ID | Kind | Title | Status | Owner | File |
|---|---|---|---|---|---|
| L-0902 | Lemma | Phase-perturbation survival for complete carrier Toeplitz witnesses | PROPOSED | `gpt56-01-c` | `claims/lemmas/L-0902-phase-perturbation-survival.md` |
| O-0903 | Observation | Complete binary128 phase comparison remains positive | EMPIRICAL | `gpt56-01-c` | `claims/observations/O-0903-phase-backend-comparison.md` |
| X-0904 | Experiment | Complete phase-backend comparison and frozen-vector budget | EMPIRICAL | `gpt56-01-c` | `experiments/X-0904-phase-backend-comparison/README.md` |

Suggested methodological note:

> For the frozen `c=10^10` carrier vector, the recorded leading margin and
> absolute phase weight require a common phase radius below `1.231e-6` after the
> proposed exact nonprime correction budget. A complete `c=10^8` binary128
> phase rerun remained positive but moved the Toeplitz operator by about
> `8.05e-6`. Future candidate promotion therefore requires directed phase balls
> and fixed-vector accumulation, not a long-double midpoint eigensolve.

No candidate registry change is requested.
