# X-95400 — exact Q4 FOCC annular hardening replay

Run:

```bash
python3 verify.py --scan-limit 100000 --output results/verification.json
sha256sum -c SHA256SUMS
```

The exact portion uses only integers, `fractions.Fraction` and a two-coordinate
`Q(sqrt(2))` implementation. The endpoint scan is explicitly floating
reconnaissance and does not prove SACF, FOCC, OCHD or RH.
