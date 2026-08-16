# X-93280 - Phase-locked safe-line and two-row consumer replay

This lightweight standard-library checker verifies:

1. the exact `P_2/P_3` no-common-zero elimination;
2. the phase-lock zero at `i/2` and the critical lattice;
3. the centered-cubic double-zero normalization;
4. the multiplicative factor-64 formula versus the rejected additive mutation;
5. the exact large-prime smooth-reservoir coefficient dictionaries;
6. targeted finite diagnostics for rows two and three;
7. four hostile mutations.

Run:

```bash
python3 verify.py --json /tmp/x93280.json
cmp /tmp/x93280.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_93280_PHASE_LOCKED_TWO_ROW_CONSUMER
```

The row scan is diagnostic only. The replay does not prove `LPTRP_23`,
`SCID_PL`, the safe-line analytic theorem, Landau's theorem, or RH.
