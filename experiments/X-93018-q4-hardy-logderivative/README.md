# X-93018 - Q4 Hardy inversion and logarithmic-derivative dictionary

This lightweight exact replay supports `L-93018`, `L-93019`, and `R-93020`.

It checks:

- the finite prefix/mean Hardy identity;
- exact finite backward inversion with the boundary term;
- boundary-free inversion on exact zero-boundary fixtures;
- the linear-mode boundary firewall;
- the explicit scale-four Mobius coefficients;
- the coefficientwise compact-Q4 logarithmic-derivative convolution;
- hostile mutations removing the boundary or four-adic gauge.

Arithmetic is `fractions.Fraction` plus formal prime-log coefficient maps.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_93018_Q4_HARDY_LOGDERIVATIVE
```

The replay does not prove the square-root Q4 mean bound, endpoint PIG, or RH.
