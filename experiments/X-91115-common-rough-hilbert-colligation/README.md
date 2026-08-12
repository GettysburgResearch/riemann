# X-91115 — Common rough Hilbert colligation

Companion exact replay for `L-91326`.

```bash
python3 experiments/X-91115-common-rough-hilbert-colligation/verify.py
```

Expected verdict:

```text
PASS_COMMON_ROUGH_HILBERT_COLLIGATION
```

The checker uses exact `Fraction` matrix arithmetic. It verifies the common
metric, one-packet defect, determinant factorization, three-factor conservative
telescope, diagonal product law, and the SHARP/score energy constants.
