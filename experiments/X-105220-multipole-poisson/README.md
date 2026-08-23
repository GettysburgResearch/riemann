# X-105220 — Multipole Poisson safe-line algebra

Run:

```bash
python -B experiments/X-105220-multipole-poisson/verify.py \
  --output experiments/X-105220-multipole-poisson/results/verification.json
```

The standard-library exact replay checks:

- the three-height partial-fraction identity;
- the boundary mass `3/5`;
- cancellation of the first two formal orders in the coherence defect;
- the leading formal defect `4(D Q2-Q^2)`;
- the rational quartic debt firewall;
- the unit-core localizer floor `9/25`;
- the theta-growth exponent `-3/2`.

It does **not** authenticate the analytic Stirling/Bell estimates, the
entire-function passage, the nonreal correction, `MCRC105220`, or RH.
