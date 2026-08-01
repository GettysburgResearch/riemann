# X-16201 — Exact affine-sector and radical-tail audit

This standard-library-only experiment checks the finite algebra used by
`L-16201`--`L-16204`.

It verifies:

- exact lower bounds against a full affine prolate fit from off-diagonal and
  three-mode curvature obstructions;
- a source/background Schur lower-gap certificate;
- the radical-tail factorization `PJP` / omitted-tail identity;
- the exact two-dimensional generalized spectral-diameter invariant;
- fail-closed logical gates and malformed-certificate rejection.

Run:

```bash
python verify.py certificate.json --output results/verification.json
python -m unittest discover -s tests -v
sha256sum -c SHA256SUMS
```

Retained result:

```text
9/9 adversarial tests pass
proof-object SHA-256
841bb98b828601ebb6257d0709c91e91ce6d8aad8e304721eed7b9369a3735e0
```

This is exact synthetic rational algebra. It does not evaluate a production
CCM matrix, a prolate asymptotic, the Weil form, or Riemann `Xi`.
