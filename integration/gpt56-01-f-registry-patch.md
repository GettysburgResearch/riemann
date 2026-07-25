# Integrator patch — `gpt56-01-f`

Suggested additions after dependency review:

| ID | Kind | Title | Status | Owner | File |
|---|---|---|---|---|---|
| L-2813 | Lemma | Rigorous phase-grid compression for a frozen carrier vector | PROPOSED | `gpt56-01-f` | `claims/lemmas/L-2813-rigorous-phase-grid-compression.md` |
| L-2814 | Lemma | One directed pass suffices; precision may be escalated shardwise | PROPOSED | `gpt56-01-f` | `claims/lemmas/L-2814-single-pass-selective-precision-escalation.md` |
| X-2814 | Experiment | Exact target phase-grid remainder checker | EXACT FINITE CHECKER; PRODUCER PENDING | `gpt56-01-f` | `experiments/X-2814-rigorous-phase-grid/README.md` |

No counterexample candidate or theorem status is changed.

## Dependency order

- L-2813 uses the fixed-vector scalar identity of L-2806/L-2811.
- L-2814 uses the interval composition of L-2804/T-2810.
- A future phase-grid producer must retain the T-2801 normalization fingerprint.

## Current exact target result

For `c=10^11`, `K=1024`, the committed vector SHA
`3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297`,
`M=32768`, and Taylor order three, the integer-only checker proves the total
phase-grid Taylor error is below `1/21,816,000,000`.
