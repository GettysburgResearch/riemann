# X-91305 — Julia/Wick inverse replay

Checks the local inverse/detail identity and finite tensor coefficient algebra.
It does not prove the Wick renormalization or RH.

```bash
python3 verify.py --json /tmp/result.json
cmp /tmp/result.json results/verification.json
sha256sum -c SHA256SUMS
```
