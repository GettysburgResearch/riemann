# X-105200 — Exact Poisson–Bézout residue localization replay

This standard-library replay checks the finite algebra behind `L-105200` and
`L-105201`.

It uses rational polynomial fixtures

\[
p'(x)=(x^2-a^2)(x^2-b^2)
\]

with `a^2+b^2=2c^2`, so both the critical points of `p` and the zeros of
`p''` are rational. Boundary evaluation at `iT` is performed in exact
Gaussian rational arithmetic.

Checked:

- one common cubic Cauchy/Poisson localizer for critical-point count;
- the same localizer for the first residue moment;
- the uncorrected second moment plus the complete `p''` debt;
- the polynomial extended-Euclidean construction of the Bézout interpolant;
- exact cancellation of the debt;
- the debt-free second-moment boundary functional;
- smooth coherence `0<C<=1`;
- the epsilon-monochromatic coherence lower bound.

Not checked:

- entire Xi interpolation;
- canonical-product exhaustion;
- nonreal Xi critical-point estimates;
- RH.

Run:

```bash
python -B experiments/X-105200-poisson-bezout/verify.py \
  --output experiments/X-105200-poisson-bezout/results/verification.json

python -B -m unittest discover \
  -s experiments/X-105200-poisson-bezout/tests \
  -p "test_*.py" -v
```
