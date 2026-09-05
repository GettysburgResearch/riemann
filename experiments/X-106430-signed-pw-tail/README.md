# X-106430 — signed Paley–Wiener tail replay

Run:

```bash
python3 experiments/X-106430-signed-pw-tail/verify.py \
  --output experiments/X-106430-signed-pw-tail/results/verification.json
```

Expected classification:

```text
PASS_T106430_SIGNED_PALEY_WIENER_TAIL_REDUCTION
```

The replay checks:

- Laguerre orthogonality and exact incomplete-gamma tail polynomials through order eight;
- the simple-factor deficit `exp(-2yH)` and its `>99/100` live-scale firewall;
- the finite-rank coverage lower bound;
- the exact visible/complement signed Hankel trace split;
- a fixture where two large absolute complement charges cancel in the index;
- the rational `851/15000` and `101/15000` thresholds.

It does not evaluate Xi, prove `PWSAMP106420`, prove `SIGNEDTAIL106430`, or establish a new critical-line percentage.
