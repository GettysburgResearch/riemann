# X-107200 exact replay

Run:

```bash
python3 experiments/X-107200-xi-cauchy-saddle/verify.py \
  --output experiments/X-107200-xi-cauchy-saddle/results/verification.json
```

The replay checks:

- the local multiplicity/orientation/Cauchy-weight table;
- exact Riccati and curvature transport on symbolic polynomial fixtures;
- the rational \(90\%\) thresholds;
- saddle-root and natural-width inequalities on deterministic numerical
  fixtures;
- the dilation firewall;
- fail-closed conclusion flags.

It does not prove the analytic Xi saddle theorem by computation, evaluate Xi
zeros, or prove `XISCREEN107200`.
