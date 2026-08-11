# X-91008 — Cauchy-square / Clark / Jordan bridge

This finite replay checks:

- the soft-count primitive identity;
- its derivative relation to radial curvature;
- the exact line and reflected-pair mass/second-moment projectors;
- the Cauchy-square Fourier transform and hyperbolic depth multiplier;
- Clark boundary-phase orientation;
- generalized-Jordan coefficient positivity;
- the positive shifted cocycle;
- the \(a=1/2\) Euler-totient specialization.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_CAUCHY_SQUARE_CLARK_JORDAN_BRIDGE
```

The replay proves finite algebra and synthetic high-precision identities only.
It does not prove prime-side soft-count monotonicity or RH.
