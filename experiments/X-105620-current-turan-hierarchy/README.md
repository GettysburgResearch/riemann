# X-105620 — Current–Turán exterior-square hierarchy

This replay authenticates exact finite-source algebra behind `L-105620`,
`L-105621` and `R-105620`.

Run:

```bash
python3 experiments/X-105620-current-turan-hierarchy/verify.py \
  experiments/X-105620-current-turan-hierarchy/results/verification.json
```

Expected:

```text
PASS_X_105620_CURRENT_TURAN_HIERARCHY
62195a8b977b7ddb34607fcd0cbd7d19f9d06161151148104d593a9e7b7e319c
checks=200
RH_UNPROVEN
```

The exact checks cover:

- five Taylor levels of the hyperbolic-current/exterior-square identity on
  three symmetric rational source fixtures;
- coefficientwise positivity of every replayed exterior-square chaos;
- the exact degree-zero shell map `S_r(w)=w(1-rw)/(w-r)`;
- `E_+(S_r)=E_-(S_r)=r^2`;
- the real-rooted nineteen-rung firewall `19/9>2`.

The replay does not evaluate Xi, prove the physical all-pass collision
estimate, establish the balanced shell transfer, or prove RH.
