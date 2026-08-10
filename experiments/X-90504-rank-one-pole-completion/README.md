# X-90504 — Minimal rank-one pole completion replay

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The replay checks the pole-plane diagonalisation, uniqueness of the minimal rank-one completion, the exact prime/zero-side square identity, and the off-line index count on synthetic hyperbolic blocks.

It does not prove the prime-side sign theorem or RH.
