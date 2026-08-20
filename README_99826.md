# T99826 — Fixed-shell Hardy–Carleson continuation

This collision-free continuation belongs to draft PR #665.

It proves that the correctly normalized zero-free box admits a fixed
ratio-536 compactification with uniformly bounded coefficient diagonal. It
also proves a support-shifted Poisson point-evaluation identity that removes
the absolute-scale cost exactly.

Replay:

```bash
python3 experiments/X-99820-native-box-audit/verify_fixed_shell.py \
  --output experiments/X-99820-native-box-audit/results/fixed_shell_verification.json
sha256sum -c T99826_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T99826_FIXED_SHELL_HARDY_CARLESON_REDUCTION
6ca887e8cc02f23d48b0101e07e4702f71f1a0f11b8a60a7a985da24b2ba6b8b
```

The signed shell Hardy–Carleson estimate and RH remain unproved.
