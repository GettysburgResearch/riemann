# X-100140 — Poisson-tail equivalence replay

```bash
python3 verify.py --output results/verification.json
sha256sum -c SHA256SUMS
```

The replay checks exact finite Poisson, tail-square, signed-square,
adjacent-block, and combinatorial identities. It does not prove the
RH-equivalent arithmetic tail estimate.
