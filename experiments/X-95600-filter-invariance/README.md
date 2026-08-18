# X-95600 — exact subpower/filter/compact-bridge replay

Run:

```bash
python3 verify.py --output /tmp/x95600.json
cmp /tmp/x95600.json results/verification.json
sha256sum -c SHA256SUMS
```

The replay checks exact finite algebra. It does not prove UOSACF, the nonlocal
compact-current estimate, or RH.
