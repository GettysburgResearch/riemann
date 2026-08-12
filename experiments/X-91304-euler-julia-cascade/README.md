# X-91304 — Euler–Julia cascade replay

Checks:

- exact universal local Julia identity with rational arithmetic;
- finite prime cascade optical identity;
- exact local dyadic scale cocycle;
- critical detail asymptotic.

Run:

```bash
python3 verify.py --json /tmp/result.json
cmp /tmp/result.json results/verification.json
sha256sum -c SHA256SUMS
```

The replay does not evaluate zeta and does not prove the global wave operator or RH.
