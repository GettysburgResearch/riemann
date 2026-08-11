# X-90422 — Exact PIG factor-16 ordinary-prime normal form

This standard-library checker supports `L-90422`.

Run:

```bash
cd experiments/X-90422-pig-factor16
python3 -m py_compile verify.py
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
```

Expected classification:

```text
PASS_X_90422_PIG_FACTOR16_NORMAL_FORM
```

The exact packet verifies:

```text
63     compact/ordinary mean and annular relations
127    lower-sixteenth support cancellations
18,288 piecewise-linear kernel coefficients
9      exact polynomial-factorization controls
```

It proves finite algebra only. It does not prove the Mellin continuation, a critical-growth estimate for the factor-16 scalar, or RH.
