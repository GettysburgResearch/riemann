# X-91008 — Cauchy-square / Clark / Jordan bridge

This experiment packet contains two replays.

## Main bridge replay

`verify.py` checks:

- the soft-count primitive identity;
- its derivative relation to radial curvature;
- the exact line and reflected-pair mass/second-moment projectors;
- the Cauchy-square Fourier transform and hyperbolic depth multiplier;
- Clark boundary-phase orientation;
- generalized-Jordan coefficient positivity and positive shifted cocycle;
- the normalized positive sieve cocycle;
- the \(a=1/2\) Euler-totient specializations;
- the exact two-channel square for the dyadic soft-count increment.

Expected verdict:

```text
PASS_CAUCHY_SQUARE_CLARK_JORDAN_BRIDGE
```

## Three-state scattering replay

`verify_allpass.py` checks:

- the exact `3 x 3` orthogonal transfer matrix;
- determinant one;
- the fixed-generator Cayley representation;
- recovery of the old and two innovation channels from its first row;
- the eigenvalues `1,(a-iu)/(a+iu),(a+iu)/(a-iu)`.

Expected verdict:

```text
PASS_DYADIC_CAUCHY_THREE_STATE_ALLPASS
```

## Run

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json

python3 verify_allpass.py --json /tmp/verification_allpass.json
cmp /tmp/verification_allpass.json results/verification_allpass.json

sha256sum -c SHA256SUMS
```

The main replay performs 1,228 checks, including 540 generalized-Jordan and
540 normalized-sieve cocycle checks. The all-pass replay performs 509 finite
scattering checks. They prove finite algebra and synthetic high-precision
identities only. They do not prove the critical-boundary dyadic gate or RH.
