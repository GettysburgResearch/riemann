# X-99030 — survival-resolvent Bellman hardening replay

Run:

```bash
python3 verify.py --output results/verification.json
```

The checker uses only the Python standard library and exact rational interval
arithmetic. It verifies:

- the sixty-six exact root-mass cell formulas and `15<M_67<16`;
- exact causal coefficients on rational fixtures;
- the survival-resolvent Bellman identity;
- current-debt and missing-resolvent mutations;
- the resulting `<32` arithmetic debt constant;
- status firewalls, including `rh_established_by_replay=false`.

It does not rerun the heavy compact Hall/profile or endpoint campaigns and does
not prove RH.
