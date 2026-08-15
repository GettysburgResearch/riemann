# X-19887 — CPNR/SIDA/PSSI final audit

Exact `Fraction` regression for:

```text
12012 square-root-thinning constant;
source-owned residual and child slack cocycle;
strict nonzero native defect lower bound;
shrinking SIDA norm bounds;
pure-point versus nonzero diffuse PSSI category conflict.
```

It does not prove the analytic claims, frozen factor-67 dependencies, endpoint consumer, Stieltjes uniqueness theorem, or RH.

Replay:

```bash
python3 verify.py certificates/control.json --output results/verification.json
python3 -m unittest discover -s tests -v
```
