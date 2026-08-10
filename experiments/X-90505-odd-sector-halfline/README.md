# X-90505 — Odd-sector half-line replay

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The replay checks the exact parity index split on synthetic zero/pole blocks and the half-line correlation and jump-square identities on complex test functions.

It does not prove the all-prime half-line sign theorem or RH.
