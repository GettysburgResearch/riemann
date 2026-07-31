# X-15111 — Exact finite determinant-moment gate

This standard-library checker validates the finite algebra that every
self-adjoint `det_2` model must satisfy:

- exact rational self-adjoint eigenvalue list;
- exact power traces `Tr(K^m)`;
- exact formal coefficients of `log det_2(I+zK)`;
- vanishing odd moments for a centered-even model;
- ordinary and shifted Stieltjes-Hankel positivity.

The retained spectrum is

```text
+/-1, +/-1/2, +/-1/3.
```

The three-by-three ordinary and shifted Hankel gates are strictly positive.
Seven adversarial tests reject wrong trace moments, wrong determinant
coefficients, broken spectral symmetry, Boolean injection, missing orders, and
an unsupported Hankel request.

This is a synthetic finite regression. It does not evaluate `xi`, the Shimizu
operator, or the arithmetic finite-part ledger, and does not certify RH.

Reproduce with:

```bash
python3 verify.py certificates/symmetric-finite-control.json
python3 -m unittest discover -s tests -v
```
