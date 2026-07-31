# X-14315 — exact cardinal/radical finite-section repair

This standard-library-only checker verifies the finite algebra used by
`T-14306`:

- exact global cardinal identity `C^T Q = V` and `VC=I`;
- exact global radical identity `QR=0` and `VR=0`;
- finite evaluation correction `C_tilde=PC(VPC)^-1`;
- exact zero-kernel repair `K=PR-C_tilde VPR`;
- direct-sum and kernel identities;
- quadratic cardinal, radical, and cross-error identities;
- a positive complement block;
- the exact Schur-corrected lower floor in the packet metric.

The retained model is deliberately globally indefinite. It has a positive
cardinal coordinate, an exact radical coordinate, a negative localization-error
direction, and a nonzero cross map into a positive complement. The checker
certifies the corrected floor

```text
Schur low block >= -(1/62) packet Gram.
```

This is a synthetic finite regression. It is not a Xi evaluator, a zeta-zero
certificate, or a proof that the constructed packet captures the complete
localized low spectrum.

## Replay

```bash
python3 -m py_compile verify.py tests/test_verify.py
python3 -m unittest discover -s tests -v
python3 verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
sha256sum -c SHA256SUMS
```
