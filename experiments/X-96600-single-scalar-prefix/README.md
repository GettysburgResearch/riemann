# X-96600 exact regression and diagnostic

Run the exact algebra replay:

```bash
python3 verify.py certificates/control.json --output results/verification.json
```

The deterministic external packet additionally contains a hostile mutation suite, checksum ledgers, and an optional `O(N)` diagnostic scanner. The retained diagnostic checked the scalar prefix through `N=100000000`, but it is explicitly reconnaissance and is never promoted to an all-scale theorem.

The replay verifies only the scalar convolution, odd-core packet, finite-prime source ledger, exact prime recurrence, genealogy and fail-closed status. It does not prove `SCPS`, `ACTQ_2`, eventual scalar positivity, or RH.
