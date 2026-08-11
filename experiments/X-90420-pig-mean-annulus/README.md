# X-90420 — Exact PIG mean and factor-four annulus replay

This standard-library checker supports:

- `L-90418-mean-mode-is-an-inclusive-uniform-carry-transform.md`;
- `R-90411-haar-pig-normalization-correction.md`;
- the finite algebra in `T-90420`;
- `L-90421-factor4-annularization-of-the-pig-mean.md`.

Run:

```bash
cd experiments/X-90420-pig-mean-annulus
python3 -m py_compile verify.py
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
```

Expected classification:

```text
PASS_X_90420_PIG_MEAN_ANNULUS
```

The exact packet verifies:

```text
72    prefix/source mean identities
9,180 inclusive-carry kernel identities
72    corrected Haar/PIG normalization identities
72    factor-four annular identities
```

It also rejects every lower-quarter basis vector in the annular scalar and checks

```text
2-3y+y^2=(1-y)(2-y)
```

at exact rational controls.

The checker proves finite algebra only. It does not prove the Mellin continuation, the critical mean estimate, deterministic PIG, the repaired global adapter, or RH.
