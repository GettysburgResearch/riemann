# X-104510 — Hermite–Biehler last-defect algebra

Run:

```bash
python3 verify.py --output results/verification.json
```

The checker uses exact rational polynomial arithmetic for:

- the factor-two quartic;
- the Laguerre-positive nonreal cubic;
- the phase-velocity identity;
- one antiderivative interval;
- a growing-box scale diagnostic.

It does not evaluate Xi or prove the analytic saddle, strip, PRES, VFLUX, or RH
theorems.
