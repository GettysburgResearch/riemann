# X-106640 — Phase-majorant correction replay

Run:

```bash
python3 experiments/X-106640-phase-majorant-correction/verify.py \
  --output experiments/X-106640-phase-majorant-correction/results/verification.json
```

The replay uses exact Gaussian rational arithmetic.  It checks the one-pole
counterexample to the former phase-angle equality and several finite
Cauchy-Gram fixtures satisfying

```text
Re Delta <= |Delta| <= canonical overlap
canonical charge <= denominator phase statistic.
```

It does not evaluate Xi or prove `ORIENTEDANGLE106540`,
`MESOTRANS106630`, or the \(90\%\) conclusion.
