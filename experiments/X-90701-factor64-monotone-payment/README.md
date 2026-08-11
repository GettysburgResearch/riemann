# X-90701 — factor-64 signed-variation replay

This standard-library checker reconstructs the exact factor-64 reward in
\(\mathbb Q(\sqrt2)\), verifies the sign blocks and prefix bounds of `L-90701`,
and exercises both the monotone Abel payment and the arbitrary signed
upward-variation inequality on exact rational sequences.

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_90701_FACTOR64_MONOTONE_PAYMENT
```

The checker proves finite reward algebra only. It does not prove the critical
base sign or cofinal occupation-variation theorem, the factor-64 sign, or RH.
