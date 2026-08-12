# X-91740 — Kernel-lock lurking-isometry replay

This finite replay checks:

1. reconstruction of a positive kernel defect;
2. equality of source and target Gram matrices under the lurking isometry;
3. the exact moving-node kernel-to-entropy threshold;
4. the same-diagonal polarization firewall.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_KERNEL_LOCK_LURKING_ISOMETRY
```

The replay is finite linear algebra. It does not prove the actual zeta kernel
lock, the `o(1/Y^2)` residual rate, or RH.
