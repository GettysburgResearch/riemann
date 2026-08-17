# X-93290 actual LPTRP rows and phase-locked covariance

The experiment has two layers.

1. `certify_rows.cpp` computes the actual `mu_>3` row coefficients through
   `10^8`, encloses every `1/sqrt(n)` by exact unsigned-128-bit inequalities,
   and certifies every prefix derivative.
2. `verify.py` checks the coefficient dictionaries, real-activation interface,
   exact `p=5` cone counterexamples, covariance gauge identity, positive
   spectral quadratic form, and hostile mutations.

Run:

```bash
./replay.sh
```

Expected:

```text
PASS_X_93290_ACTUAL_LPTRP_COVARIANCE
PASS_X_93290_FULL_REPLAY
```

The replay proves the finite row theorem and exact finite algebra. It does not
prove the growing-prime tail, pointwise `SCID_PL`, or RH.
