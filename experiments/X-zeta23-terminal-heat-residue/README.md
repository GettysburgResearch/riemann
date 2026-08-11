# X-zeta23-terminal-heat-residue

Finite regression for the proposed terminal Gaussian heat-residue theorem.

The checker verifies:

- the parabolic two-point finite-difference kernel;
- exact `-2` target-residue normalization;
- the closed real-part formula for a nuisance residue;
- equality of the residue saddle with the PR #364 terminal threat exponent;
- the three-Gaussian factorization;
- equality between the finite prime/continuum scalar and the three-point
  Gaussian Mellin transform;
- a finite all-integer tail-envelope control.

It does **not** verify the zeta contour shift, the terminal-pair theorem, a
complete infinite tail, the corrected-kernel floor, or RH.

## Replay

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_TERMINAL_GAUSSIAN_HEAT_RESIDUE
```
