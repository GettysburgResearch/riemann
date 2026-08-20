# X-99900 — Exact weighted cube flow and parity barrier replay

Run:

```bash
python3 verify.py --output results/verification.json
```

The checker uses exact rational arithmetic. It verifies recursive Hasse flows,
all vertex capacities, the exact parity residual, reversed-parity optimality,
the two-labelled-67 specialization, a finite positive layer-cake fixture, and
the path-capacity firewall.

It does not prove EPXGC99900, PXGC99700, or RH.
