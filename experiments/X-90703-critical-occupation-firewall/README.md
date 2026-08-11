# X-90703 — critical Pascal occupation firewall

This directed standard-library replay constructs the exact uniform-Pascal Green
occupation for the critical target at `X=14`. It certifies that the occupation is
not monotone, identifies its sole upward step, and verifies that the
upward-variation payment criterion from `L-90701` still has large slack.

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_90703_CRITICAL_OCCUPATION_FIREWALL
```

This is one exact finite firewall, not a cofinal variation theorem or RH proof.
