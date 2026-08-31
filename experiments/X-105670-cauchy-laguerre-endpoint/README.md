# X-105670 — Cauchy large-translation Laguerre endpoint

The exact replay checks the finite algebra supporting `L-105670--L-105671`:

- orthonormality of the first eight Laguerre modes;
- the exact integrals `int q_m=(-1)^m` producing the factor `n`;
- the Cauchy trace pair's scale invariance;
- exact rational controls approaching the rank-three large-height limits;
- the positive rank-one all-height identity.

Run:

```bash
python -B experiments/X-105670-cauchy-laguerre-endpoint/verify.py \
  --output experiments/X-105670-cauchy-laguerre-endpoint/results/verification.json
```

Expected:

```text
PASS_T105670_CAUCHY_LAGUERRE_ENDPOINT
checks=97
28e5db953aaccd25a328f7380b9d8162407c54ada77dc640c895531aff54eaaa
```

The replay does not prove Grassmannian convergence, exclude an intermediate
stationary contact, establish cofinal Xi passage, or prove RH.