# X-90601 — Brownian Bohr-instability regression

This standard-library regression accompanies `L-90601`, `L-90602`, and `R-90601`.

It checks:

- the exact coefficient ratio
  `C_(N,k+1)/C_(N,k)=((N-k)/(N+k+1))^2` in 3,160 rational cases;
- the explicit exponentially small multiple-tail constant used in the selected-prime block;
- a right-half-plane root of `H_63` near
  `0.2508380937103903 + 55.82354339041126 i`;
- an independent higher root of `H_60` near
  `0.25268645868759 + 270.2566119804343 i`;
- the Liouville vertical-limit probe changing sign between `N=79` and `N=80`;
- the exact leading continuum cancellation of `L-90602`.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_90601_BROWNIAN_BOHR_INSTABILITY
```

The computation is not the proof of the cofinal refutation.  The theorem is the coefficient-estimate, Steinhaus-orthogonality, polygon, Kronecker, and Hurwitz argument in `L-90601`.
