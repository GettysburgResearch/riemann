# X-93300 — cubic wavelet, Vaughan decomposition, and carrier reduction

Run:

```bash
python3 verify.py --output results/verification.json
python3 -m py_compile verify.py
```

The checker uses standard-library exact rational arithmetic. It verifies:

- the factor-four piecewise cubic identity;
- the two Mellin moments;
- exact integer cell sums through `y=400`;
- formal Q4-source-to-wavelet rewrites;
- formal Vaughan reconstruction at 81 endpoints;
- the endpoint third-difference identity on arbitrary rational sources;
- the coefficient-blind bilinear firewall;
- the explicit no-RH-input boundary.

It does not prove the balanced Type-II estimate or RH.
