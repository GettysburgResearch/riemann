# X-106410 — Small-shift endpoint-bank replay

Run:

```bash
python3 experiments/X-106410-small-shift-bank/verify.py \
  --output experiments/X-106410-small-shift-bank/results/verification.json
```

Expected classification:

```text
PASS_T106410_SMALL_SHIFT_ENDPOINT_BANK_ALGEBRA
```

The replay checks:

- 29,282 exact rational-grid instances of the same-sign and reflected channel inequalities;
- the sharpened four-channel constant `2547232/1568239201 < 1/600`;
- the safe conditional fraction `95407/100000 = 0.95407`;
- fail-closed status flags.

It does **not** prove `ENDPOINTBANK106410`, ninety percent, density one, or RH.
