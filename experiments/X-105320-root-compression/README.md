# X-105320 — Exact root-compression replay

This standard-library replay authenticates the rational matrix identities in
the first half of `L-105320`.

Run:

```bash
python -B experiments/X-105320-root-compression/verify.py \
  --output experiments/X-105320-root-compression/results/verification.json
```

Expected:

```text
PASS_X_105320_ROOT_COMPRESSION_SCHUR
e3a54b6fa894ecaf87e860510ff9aa0f7c2858220327892328dd89b2d45b2d13
RH_UNPROVEN
```

The replay performs 97 exact rational checks across four independent root
fixtures:

- `det(zI-C)=p'(z)/n` for the zero-sum root compression;
- the complete Schur identity for `p/p'` at rational test points;
- the exact coupling norm `||b||^2=V_2/n`.

It does **not** replay the spectral projector/angle perturbation argument,
the proposed Xi complex-saddle theorem, `CRDB105200`, or RH.
