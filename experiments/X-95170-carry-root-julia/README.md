# X-95170 — Carry root-Julia exact replay

Run:

```bash
python3 verify.py --output /tmp/x95170.json
cmp /tmp/x95170.json results/verification.json
sha256sum -c SHA256SUMS
```

Arithmetic class:

```text
EXACT_INTEGER_AND_RATIONAL_WITH_FORMAL_PRIME_LOGS
```

The replay checks finite coefficient identities, PSD carry currents, exact energy constants, and the polynomial no-common-zero reduction. It does not prove the analytic Landau step, TFSE, Cycle Debt, or RH.
