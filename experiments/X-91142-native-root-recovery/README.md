# X-91142 — Native-root normalization, radix-four dual, and rough reservoir

Replay:

```bash
python3 experiments/X-91142-native-root-recovery/verify.py
```

Expected verdict:

```text
PASS_NATIVE_ROOT_NORMALIZATION_AND_DUAL_PACKET
```

The standard-library verifier uses exact `Fraction` arithmetic and formal prime-log vectors to check:

- `mu * log = Lambda`;
- the positive radix-four dual recurrence;
- radix-four summation by parts;
- `mu_(P61) = 1_(rough) * mu`;
- the unique least-rough-prime partition;
- the strict native-capacity overdraw witness;
- the causal target-debt inequality.

The two C++ programs are explicitly discovery-only stress tests for the proposed global one-prime finite-Euler row theorem. They do not certify its infinite parameter range.
