# X-27301 — Prime-neutral lift and annular-scope control

This standard-library checker authenticates the finite algebra used by the
Issue #273 continuation.

Run:

```bash
python verify.py --self-test --output results/exact-verification.json
```

It verifies:

1. the ordinary-prime monotone-dual collapse for every `8<=X<=512`;
2. the exact prime-gradient transpose identity;
3. the complete formal prime-power logarithmic ray through `n=256`;
4. the exact annular norm ledger
   `||A_X^*Lambda||_2 <= 50 X^(-3/2)`;
5. the zero parabolic residual in the endpoint prime row;
6. eight central and mutation tests.

Retained verdict:

```text
EXACT_PRIME_DUAL_COLLAPSE_AND_SCOPE_CONTROL
```

Proof-object SHA-256:

```text
528355a5e8d9e2eb9f418d8368bc61d8e4d01dfe07d43254def32863e242a9bc
```

The checker proves no proper-power-neutral lift and no statement about RH.
