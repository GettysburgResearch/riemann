# X-91610 — Logarithmic Clark entropy replay

This finite replay supports `L-91610`, `L-91611`, and the normal-form claims in
`T-91610`.

It checks:

1. the local Euler Julia identity;
2. the exact boundary entropy integral
   ```text
   -log |m|^2 = int_0^1 |d|^2/(|m|^2+t|d|^2) dt;
   ```
3. the identity `-log m = 2 artanh((1-m)/(1+m))` on interior points;
4. positivity of a finite Herglotz kernel for the logarithmic generator;
5. additive logarithms and the Redheffer/tanh law for a finite cascade;
6. the finite-dimensional log-determinant resolvent identity;
7. zero entropy loss and coefficient-one return at the resonance `z=1`.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_LOG_CLARK_ENTROPY
```

The replay verifies finite algebra and numerical positive-kernel controls.  It
does not prove the completed logarithmic interconnection, PDWT, CPPD, or RH.
