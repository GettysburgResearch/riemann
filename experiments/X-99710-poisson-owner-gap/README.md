# X-99710 — Adaptive Poisson-owner gap replay

Run

```bash
python3 experiments/X-99710-poisson-owner-gap/verify.py
```

Expected first line:

```text
PASS_T99710_ADAPTIVE_POISSON_OWNER_GAP
```

The replay checks:

- exact normalization of the duplicated-67 owner law;
- the Cauchy-averaged lower gap on all three owner-edge types;
- the sharp continuous-order threshold `u*=log(2)/log(67)`;
- the critical local coefficients `1,0,1,2,4,...`;
- the adaptive strip/gap exponent tradeoff;
- fail-closed status flags for `APOC99710` and RH.

It does not prove the source-Carleson embedding, reconstruct the full `10^8`
SHARP scan, or establish RH.