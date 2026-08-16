# X-95100 — Carry terminal-control bank

Run:

```bash
python3 verify.py --json /tmp/x95100.json
cmp /tmp/x95100.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected classification:

```text
PASS_X_95100_CARRY_TERMINAL_CONTROL_BANK
```

The checker uses exact `Fraction` algebra for the terminal ratio, convex
interpolation, cutoff-switch formula, and mod-12 schedule. It uses directed
`Decimal` primitives as finite diagnostics for the actual square roots and
logarithms at 96 endpoints. It proves no cofinal sign theorem and no RH result.
