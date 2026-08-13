# X-91410 — Three-route LRPT reconnaissance

Status: **EMPIRICAL / NOT A PROOF OBJECT**

This experiment compares three independent closure routes on a deliberately sparse parameter grid:

1. the actual Lorenz cutoff determinant of `L-91411`;
2. the stronger full even/odd determinant together with inner discrete ratio ordering;
3. the canonical left-greedy shifted-eight Hall row gain of `L-91415`.

The script uses Python binary64 arithmetic.  It does not use directed intervals, does not cover all activation cells, and must not be cited as a theorem or RH proof.

Run:

```bash
python3 verify.py
```

Retained grid:

```text
p: 67, 83, 101, 251, 1009
y: 1, 10, 30, 67
j: 2, 10, 20, 40, 60, 66
```

All five monitored quantities were positive on all 120 grid cases.  The smallest values occur at the expected first-cell/high-row boundary.  This is route-selection evidence only.

SHA-256:

```text
verify.py                    7e6ccc8031d88fa3c6a7d2e32f9a1aba9b1eb6c0c82d17d7ea219ee5d4a7090f
results/reconnaissance.json  ff87c91ff0a075fa2fcc8e93c28333a0da068c80e7b7cb8e8e4f5bf4647dab4b
```
