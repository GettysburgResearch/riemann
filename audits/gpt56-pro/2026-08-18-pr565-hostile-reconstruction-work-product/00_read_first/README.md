# PR #565 hostile-reconstruction work product

This archive preserves the work product from the approximately 200-minute reconstruction pass requested against PR #565 at frozen head

```text
339e3367660f40c74795802a6f8170b15e19b13a
```

It is intentionally an **incomplete research packet**, not a finished manuscript and not an RH proof. It contains:

1. the pre-existing deterministic parity-contractive recovery packet that was inspected;
2. the independent P61 scanner and retained results that falsified the advertised `1/40` lower bias bound;
3. the repaired numerical constants and exact contraction arithmetic;
4. the source-composition/Hall frontier reached after applying the PR #574 and PR #575 firewalls;
5. a reproducible validation harness, checksums, and a precise status ledger.

The original recovery packet is preserved byte-for-byte under `02_original_recovery_packet/`. Its own checker is useful algebraically, but it explicitly records that the universal P61 directed certificate was **not replayed**. The correction dossier in this archive supersedes any suggestion that the old `1/40` contract is valid.

## Headline status

```text
original P61 lower bound 1/40                  FALSE (x = 184)
repaired scalar window 1/42 < F/M < 1/20       strong finite + analytic candidate
repaired formal contraction margin             43/3360 (exact arithmetic)
literal source-subpacket realization            NOT ESTABLISHED
global Hall/Lorenz bypass                        NOT ESTABLISHED
annular Mellin consumer                          conditional on producer
Riemann Hypothesis                               UNPROVED
```

No draft PR, Google Drive publication, TeX manuscript, or compiled PDF was completed during the pass. This ZIP is supplied precisely so the work is not lost despite that incomplete publication state.
