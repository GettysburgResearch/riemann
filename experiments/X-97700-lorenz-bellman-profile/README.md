# X-97700 — Lorenz-Bellman profile maps and separators

Run the exact remote replay:

```bash
python3 verify.py
```

Expected:

```text
PASS_T97700_EXACT_LORENZ_BELLMAN_CORE
c604f54409e9c65641f6f31e065a815b18b41d557e96f81ea8d19e6e73977385
```

It verifies the source-faithful dual identities, swap/prime recurrence, exact NCBI/CPSL countermodels, minimal-state separators, and the directed 239-atom odd-history witness.

The deterministic companion packet also contains a larger horizon-256 binary64 diagnostic and the complete `X=61841` Lorenz solve. Those computations are explicitly discovery/falsification evidence, not an all-scale proof of `LBP67`.