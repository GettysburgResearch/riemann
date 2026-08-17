# X-97300 — Completed-parity reconstruction replay

Run:

```bash
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
```

The replay checks:

- accumulated parity and owner invariants;
- exact row coefficient cancellation behind the monotone ratio theorem;
- the difference between row-2 exactness and `5:3` scalar exactness;
- the PR #561 odd-history and depth-two directed inequalities as frozen inputs;
- the finite fractional-knapsack/Lorenz primal-dual theorem on exact rational
  fixtures;
- scalar Mellin numerator factorization;
- theorem-file completeness and hostile mutations.

It does not prove the all-endpoint Lorenz inequality, Landau's theorem, or RH.
