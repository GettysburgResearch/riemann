# X-90202 — Completely additive Liouville extremality cone

Run:

```bash
python3 verify.py
```

The checker uses `Fraction` only. For deterministic positive prime costs it
verifies the direct squarefree divisor convolution against `L-90202.5` on every
integer through 180, exhaustively over all vertex signs and on a five-point
interior grid whenever at most three distinct primes occur.

A successful run prints:

```text
PASS_X_90202_ADDITIVE_LIOUVILLE_CONE
```

The package authenticates finite algebra only. It proves no asymptotic estimate,
Form A, GFEP, or RH.
