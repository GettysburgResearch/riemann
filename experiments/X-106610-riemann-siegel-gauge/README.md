# X-106610 — Exact Riemann–Siegel gauge replay

Run:

```bash
python -B experiments/X-106610-riemann-siegel-gauge/verify.py
```

The replay uses formal power series over the Gaussian rationals. Across 120
deterministic fixtures it checks:

- all \(+\) and \(-\) carrier-cancelled companion identities through order
  five;
- the amplitude-connection cancellation in the endpoint Wronskian for odd
  orders \(1,3,5\);
- the complete Bell-polynomial expansion of \(H_5\);
- the exact \(3/40+11/500=97/1000\) conclusion ledger.

It does not evaluate zeta, estimate the oriented phase measure, prove
`RSGAUGE106610`, establish ninety percent, or prove RH.
