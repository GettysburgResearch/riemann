# X-99320 — Target-aligned rank-one row-frame replay

```bash
python3 verify.py --output results/verification.json
sha256sum -c SHA256SUMS
```

The replay checks exact finite algebra and positivity certificates. It does not
rerun the frozen compact Hall campaign, reconstruct the actual root registry,
or establish RH.
