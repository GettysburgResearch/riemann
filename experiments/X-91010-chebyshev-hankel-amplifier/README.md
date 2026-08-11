# X-91010 — Chebyshev–Christoffel Hankel amplifier

This finite replay supports `L-91010`–`L-91012`, `T-91005`, and `R-91004`.

It checks:

- exact shifted-Chebyshev orthogonality for the Catalan beta-`(3/2,3/2)` measure;
- exact congruence between the inverse Catalan Hankel matrix and the Christoffel kernel;
- the exact negative rank-one contribution of one matching off-line pair;
- the closed hyperbolic Christoffel formula;
- synthetic convergence of the first detection degree to
  `log(ell)/(4 atanh(y))`;
- the safe-parabola growth constant `3` and matrix edge `1/(2 log 3)`;
- the one-safe-pole rational Chebyshev accelerator and its boundary exponent
  `2 atanh(2y)`.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_CHEBYSHEV_HANKEL_AMPLIFIER
```

The program establishes finite algebra and synthetic scale laws only. It does not evaluate zeta, prove the parabolic remainder estimate, prove a critical-degree Hankel sign, or prove RH.
