# X-91201 — Critical renewal innerness boundary

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
```

The replay checks only the exact factor-four polynomial, the `9/4` outer-vector
norm, the nonvanishing of the filter on its multiplier circle and finite unstable
mode samples. It does not evaluate zeta and does not prove hard-range innerness or
RH.
