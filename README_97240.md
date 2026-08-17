# T-97240 - Adaptive parity-Hall scalar/Julia reduction

This add-only successor continues PR #561 at exact head
`db9bdc63c855c6ddf664b763d748f8155a6a2c67`.

It does **not** claim a proof of the Riemann Hypothesis. It closes the following interfaces unconditionally:

- the unique `5:3` scalar reduction;
- an adaptive-depth Bonferroni theorem for the homogeneous rough product;
- positivity of every smooth-interior rough finite difference;
- an exact parity-covariant positive Julia lift;
- localization of the remaining sign problem to activation-boundary histories;
- a source-blind Julia-to-Landau no-go theorem.

The remaining arithmetic producer is `GABPT`, the Global Activation-Boundary Parity Transport theorem. `GABPT -> RH` is proved conditionally.

## Replay

```bash
python3 experiments/X-97240-global-parity-hall/verify.py \
  --output experiments/X-97240-global-parity-hall/results/verification.json
```

Expected:

```text
PASS_T97240_GLOBAL_PARITY_HALL_SCALAR_JULIA_REDUCTION
```
