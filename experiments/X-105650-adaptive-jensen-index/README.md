# X-105650 — Adaptive Jensen index exact ledger

Run:

```bash
python experiments/X-105650-adaptive-jensen-index/verify.py
```

Expected output:

```text
PASS_X_105650_ADAPTIVE_JENSEN_INDEX
checks=3836
bc40c413a854087e28fe82e7a73e0f5022d7b31d7f9acb8f7f7da80630cce486
RH_UNPROVEN
```

The replay checks with exact rational arithmetic:

- the probability and closed-transform ledger for
  `mu(ds)=2s/(1+s)^3 ds`;
- the clipped-index/coarea identity `y min(1,delta/y)=min(y,delta)`;
- the soft-depth transform `x/(1+x)`;
- additive finite-quotient signed index and random-scale mixtures;
- exact visible-band plus endpoint-complement conservation for finite step
  profiles;
- the degree-zero one-pair phase-energy separator
  `1-4ab/(a+b)^2=(a-b)^2/(a+b)^2`.

It does **not** replay:

- the analytic logarithmic integral over the real line;
- Paley--Wiener or model-space functional analysis;
- the infinite theta-series or Maxwell arguments;
- cofinal Xi canonical-product passage;
- `D0PHASE105650`;
- the pointwise differential microscope;
- RH.

The retained result is `results/verification.json`.
