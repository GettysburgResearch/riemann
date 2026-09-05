# X-106550 — 280-point spectral-pressure replay

Run:

```bash
python3 experiments/X-106550-280-pressure/verify.py \
  --output experiments/X-106550-280-pressure/results/verification.json
```

The replay verifies:

- the exact pressure \(2603/2500\);
- the transition \(280/279\);
- the algebraic defect \(c_{280}\);
- the global span coefficient \(279/140000\);
- the new bound interval from the pinned \(H_0\) interval;
- strict improvement over `T-105210`;
- hostile mutations of the block size, unit-cap replacement, and span count.

It does not rerun the external Arb certificate or establish 90% or RH.
