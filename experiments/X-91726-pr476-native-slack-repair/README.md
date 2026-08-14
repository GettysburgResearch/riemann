# X-91726 — PR #476 native-slack repair regression

Run:

```bash
python3 verify.py certificates/control.json --output /tmp/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py
```

Expected:

```text
PASS_PR476_NATIVE_SLACK_REPAIR_FINITE_ALGEBRA
54d86a9b59b55ac0d7903ae901df9b13851523571230b3518f0d60277f9b332f
```

`results/summary.json` retains the compact verdict and proof-object digest.  The
checker prints the complete canonical JSON.

This is exact finite regression only. It does not reconstruct the frozen Hall,
all-column, terminal/base/port or endpoint-to-RH stack and does not prove RH.
