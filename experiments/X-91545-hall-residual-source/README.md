# X-91545 — Hall residual source disintegration

This exact replay checks the algebra of `L-91545` on deterministic and random
finite Hall networks:

- every odd target demand is matched;
- residual source coefficients are nonnegative;
- residual target equals the signed target exactly;
- residual score superordinates the signed score;
- signed rows equal residual-source rows plus a nonnegative target-null bonus.

The replay treats target, score and normalized row values as exact rational data.
It does not certify the imported number-theoretic Hall margins, their live-branch
normalization, the full reset, or RH.

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```
