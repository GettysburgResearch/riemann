# X-90701 — factor-64 monotone-payment replay

This standard-library checker reconstructs the exact factor-64 reward in
\(\mathbb Q(\sqrt2)\), verifies the sign blocks and prefix bounds of `L-90701`,
and exercises the Abel payment on exact rational nonincreasing occupations.

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_90701_FACTOR64_MONOTONE_PAYMENT
```

The checker proves finite reward algebra only. It does not prove monotonicity or
the bounded upward variation of the critical arithmetic occupation, the
factor-64 sign theorem, SHARP, or RH.
