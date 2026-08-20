# X-100710 — lightweight SCME/LRNM disposition replay

Run:

```bash
python3 verify.py --output /tmp/t100710.json
cmp /tmp/t100710.json results/verification.json
```

The replay checks the exact kernel endpoints, the positive constant

```text
kappa_0 = 8 log(2) (1-2^(-1/2))^2,
```

the finite short/long source partition, and representative signs. The
asymptotic refutation of `SCME100704` and proof of `LRNM100704` are analytic
theorems in `L-100710` and `L-100711`; the finite replay is diagnostic only.
