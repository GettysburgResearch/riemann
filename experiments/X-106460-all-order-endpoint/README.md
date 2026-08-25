# X-106460 — All-order endpoint positive-source replay

Run:

```bash
python3 experiments/X-106460-all-order-endpoint/verify.py \
  --output experiments/X-106460-all-order-endpoint/results/verification.json
```

Expected classification:

```text
PASS_T106460_ALL_ORDER_ENDPOINT_POSITIVE_SOURCE
```

The replay checks:

- the endpoint cancellation
  `N_K-D_K=2 i lambda(F F^(K+1)-F'F^K)` on an exact rational grid;
- positivity of `(v-u)(v^K-u^K)` for every odd `K<=31`;
- the exact `xi` times nonnegative factorization for every even `K<=32`;
- the fifth-derivative margin `997/1000-9/10=97/1000`.

It does not evaluate Xi, prove the cofinal height-band passage, prove the
fifth-endpoint signed-tail estimate, establish ninety percent, density one, or
RH.
