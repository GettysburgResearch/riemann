# X-95300 — PICR separator and root-port replay

Run:

```bash
python3 verify.py --output results/verification.json
sha256sum -c SHA256SUMS
```

The replay checks exact finite algebra, rational linear rank, multiples Möbius
inversion and multiradical noncancellation. It does not prove an eventual root
sign or RH.
