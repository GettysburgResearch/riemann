# X-91723 — Factor-67 all-column reserve replay

Run:

```bash
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_FACTOR67_ALL_COLUMN_SQRTK_RESERVE
```

The checker uses exact `Fraction` arithmetic and integer-square comparisons. It
authenticates the new constants

```text
57/2, 171/4, 971/4, 2913/16, 129, 130, 4290
```

and the strict thinning algebra. It deliberately does not replay the frozen
factor-67 adjacent mismatch estimate, B-spline collar theorem, terminal
omission, Hall, first-owner, common-port or endpoint-consumer inputs.
