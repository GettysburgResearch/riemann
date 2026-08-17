# X-95310 — finite odd-core Q4 replay

Run:

```bash
python3 verify.py --output results/verification.json
sha256sum -c SHA256SUMS
```

The replay uses exact integer/rational arithmetic, formal prime-log maps and
\(\mathbb Q(\sqrt2)\). It does not prove the distinct-core correlation theorem
or RH.
