# X-91112 — Fractional-column response replay

This small exact replay checks:

- the fractional Pascal Green identity on several rational seeds and columns;
- affine covariance on square dilation factors;
- the conservative response constants used in `L-91324`;
- the enlarged fixed terminal omission margin.

Run:

```bash
python3 verify.py
```

Expected verdict:

```text
PASS_FRACTIONAL_COLUMN_RESPONSE_AND_CONTINUOUS_RESET_CONSTANTS
```
