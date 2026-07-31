# X-19701 — Schur-corrected kernel defect

This exact standard-library experiment verifies a finite model of the final
selected-real-zero kernel obstruction.

The retained model contains:

- the exact conjugate off-line cardinal Gram `[[0,1],[1,0]]`;
- a positive ambient complement;
- a nonzero kernel/complement cross map;
- the selected-real-zero-invisible witness `(1,-1)`;
- an all-real positive control using the same metric and cross map.

The verifier proves exactly

```text
raw off-line quadratic          -2
Schur-corrected quadratic       -17/8
normalized corrected Rayleigh   -17/16
all-real Schur floor             31/16
```

The experiment is finite algebra only.  The zeta theorem additionally requires
the Xi-cardinal construction, finite-support selected-zero repair, form/metric
capture, and the exact Weil normalization.

Run:

```bash
python3 verify.py certificates/synthetic.json
python3 -m unittest discover -s tests
sha256sum -c SHA256SUMS
```
