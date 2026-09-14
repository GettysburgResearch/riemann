# X-106600 — Adaptive-scale endpoint replay

Run:

```bash
python -B experiments/X-106600-adaptive-scale/verify.py
```

The replay checks:

- exact weighted endpoint-difference and modulus identities on rational data;
- exact monochromatic cancellation using rational points on the unit circle;
- the one-factor phase-concentration firewall;
- the \(97/1000\) fifth-endpoint allowance.

It authenticates finite algebra only. It does not evaluate Xi, prove
`ADAPTIVEANGLE106600`, establish ninety percent, or prove RH.
