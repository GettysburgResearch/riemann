# X-107110 — stationary q-adic coarea replay

This bounded exact replay checks only the finite algebra used by
`L-107110--L-107112`:

- shifted-band coarea equals the triangular pair kernel;
- the prefix-versus-band Cauchy inequality on rational fixtures;
- squarefree common-core reindexing with a completely multiplicative rational
  proxy weight;
- the inclusion of every terminal core in the shallow-primitive region.

Run:

```bash
python -B experiments/X-107110-stationary-qadic-coarea/verify.py \
  --output experiments/X-107110-stationary-qadic-coarea/results/verification.json
```

Expected:

```text
PASS_T107110_STATIONARY_QADIC_COAREA
checks=4026
f5e71155375fc5bbb78993e1e5f3b4995c666accd9935c3401df0bc4d55324d9
```

The replay does not prove the zero-abscissa input, Vinogradov--Korobov bound,
high-primitive cancellation, or RH.