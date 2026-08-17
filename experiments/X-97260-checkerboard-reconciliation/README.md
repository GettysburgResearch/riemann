# X-97260 — Checkerboard/Cauchy–Binet reconciliation replay

Run:

```bash
python3 verify.py --output results/verification.json
```

The replay checks the corrected `H^T K` orientation, exact Cauchy–Binet-compatible
TP2 fixture, source-ordering firewall, and a finite model where TP2 holds but
Hall is infeasible. It imports, but does not rerun, PR #561's directed witness.

It does not prove `GPHT*`, `GABPT`, `TFPE`, `ACBI`, or RH.
