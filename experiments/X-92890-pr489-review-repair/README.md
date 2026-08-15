# X-92890 — PR #489 review-repair replay

Run:

```bash
python3 verify.py --mutations --output results/verification.json
```

The replay checks constants, required paths, the removal of the full-capacity
promotion, the exact zero-port declaration, endpoint-chain presence and hostile
mutations. It does not certify the analytic Hall, endpoint-realization,
prime-square or Mellin/Landau theorems.
