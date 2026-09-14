# X-106420 — Paley--Wiener model-coverage replay

Run:

```bash
python3 experiments/X-106420-pw-model-coverage/verify.py \
  --output experiments/X-106420-pw-model-coverage/results/verification.json
```

Expected classification:

```text
PASS_T106420_MODEL_SPACE_COVERAGE_ALGEBRA
```

The replay checks:

- the positive-contraction coverage matrix algebra;
- the source-coverage-to-complete-Hankel trace inequality;
- the `U=z^{-m}` denominator-cancellation firewall;
- the exact conditional fraction `95507/100000 = 0.95507`.

It does **not** prove `PWSAMP106420`, ninety percent, density one, or RH.
