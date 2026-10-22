# X-95040 — Interior carry span and two-leaf cone

```bash
python3 verify.py --json /tmp/x95040.json
cmp /tmp/x95040.json results/verification.json
sha256sum -c SHA256SUMS
```

The replay uses `fractions.Fraction` only. It authenticates finite algebra and the exact separator, not a cofinal CRCTP theorem or RH.
