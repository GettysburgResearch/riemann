# X-91008 — Cauchy-square / Clark / Jordan bridge

This finite replay checks:

- the soft-count primitive identity;
- its derivative relation to radial curvature;
- the exact line and reflected-pair mass/second-moment projectors;
- the Cauchy-square Fourier transform and hyperbolic depth multiplier;
- Clark boundary-phase orientation;
- generalized-Jordan coefficient positivity and positive shifted cocycle;
- the normalized positive sieve cocycle;
- the \(a=1/2\) Euler-totient specializations;
- the exact two-channel square for the dyadic soft-count increment.

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

The retained replay performs 1,228 checks, including 540 generalized-Jordan
and 540 normalized-sieve cocycle checks. It proves finite algebra and synthetic
high-precision identities only. It does not prove the Dyadic Cauchy-Square
Gate, prime-side soft-count monotonicity, or RH.
