# X-99220 — typed cone-budget replay

Run:

```bash
python3 verify.py
```

The replay checks the exact common-kernel score/capacity induction and rejects a
small separate-coordinate coupling mutation. It does not verify PR #620's
local arithmetic inputs and records `rh_established=false`.
