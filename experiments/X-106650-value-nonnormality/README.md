# X-106650 — Value–nonnormality replay

Run:

```bash
python3 experiments/X-106650-value-nonnormality/verify.py \
  --output experiments/X-106650-value-nonnormality/results/verification.json
```

The replay uses exact Gaussian rational arithmetic.  It checks:

```text
canonical defect = nonorthogonal Cauchy-Gram compression energy;
canonical defect = numerator-value sum + nonnormality;
determinant = product of numerator values squared;
a finite frame-ratio value certificate.
```

It does not evaluate Xi or prove `MESOSCHUR106650`,
`MESOTRANS106630`, or the \(90\%\) conclusion.
