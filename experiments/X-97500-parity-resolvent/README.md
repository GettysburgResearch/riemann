# X-97500 — Parity-resolvent and critical-depth exact replay

Run:

```bash
python3 verify.py --output results/verification.json
```

The replay checks exact rational natural/thinned source identities, the missing
cross-depth coefficient, the M-matrix residual identity, and a finite
reciprocal-prime Bonferroni fixture. It imports the directed scalar upper bound
from PR #568 without rerunning MPFR.

It does not prove the analytic small-prime theorem, `LAPBR67`, or RH.
