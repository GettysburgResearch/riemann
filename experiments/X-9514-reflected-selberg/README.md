# X-9514 — Exact reflected Selberg regression

This standard-library experiment verifies the finite Laurent-polynomial algebra
in `L-9516`.

## Run

```bash
python verify.py
```

## What is checked

For all coefficients through `n=30`, the verifier represents the twist
`n^(-it)` by a Laurent monomial in one formal variable per prime. A completely
additive integer derivation replaces `log(n)`; the proof uses only additivity.
It checks exactly:

1. `b*(a ell^2)=Lambda_A ell+Lambda_A*Lambda_A` for each twist;
2. the logarithmic derivative of the product is the sum of the two twisted
   logarithmic derivatives;
3. subtraction of the two individual Selberg identities from the product
   identity gives

   ```text
   C_cross-C_plus-C_minus=2 Lambda_plus*Lambda_minus.
   ```

The retained proof-object SHA-256 is

```text
807779c2d1debb67eeb2d971dd244930e5296f3fc014f8197dee43645cc9d94f
```

## Proof boundary

The checker verifies finite coefficient algebra only. It does not prove the
analytic continuation, the windowed forcing estimate, `L-9517`, or RH.
