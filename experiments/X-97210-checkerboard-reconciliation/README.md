# X-97210 — checkerboard reconciliation replay

Run:

```bash
python3 verify.py --output results/verification.json
```

The replay authenticates the two minimal counterexamples, a positive
Cauchy–Binet fixture, and one fractional-knapsack fixture. It does not test the
actual terminal arithmetic, prove `GPHT*`, or establish RH.
