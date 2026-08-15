# X-91726 — PR #476 native-slack repair regression

Run:

```bash
python3 verify.py certificates/control.json --output /tmp/verification.json
python3 verify_root_once.py
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py verify_root_once.py
```

Expected:

```text
PASS_PR476_NATIVE_SLACK_REPAIR_FINITE_ALGEBRA
54d86a9b59b55ac0d7903ae901df9b13851523571230b3518f0d60277f9b332f

PASS_FACTOR67_ROOT_MASS_AND_ONE_SHOT_DESCENDANT_BOUND
21032b872847eb0793fd90eadcddf671aacb8b5994ac46f9c76c3a7b9bebd2b0
```

`results/summary.json` retains the compact main verdict and proof-object digest.
The checkers print the complete canonical JSON.

This is exact finite regression only. It does not reconstruct the frozen Hall,
all-column, terminal/base/port or endpoint-to-RH stack and does not prove RH.
