# X-104550 — fixed-order Laguerre-kernel algebra

Run:

```bash
python3 verify.py --output /tmp/t104550.json
```

The replay checks the exact finite Fourier/correlation identity, nonnegative
source coefficients, orientation-to-proportion arithmetic, and the
positive-definite/pointwise-sign firewall.  It does not evaluate Xi, prove
`LAG2XI104550`, reproduce Conrey's mollifier theorem, or prove RH.
