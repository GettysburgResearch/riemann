# Bounded exact checks and source binding

The inherited checker and output in `../evidence/` are preserved unchanged. The new `check_identities.py` authenticates both with fixed SHA-256 digests before importing the inherited checker. It checks additional finite identities with `fractions.Fraction` and explicit exceptions, including under optimized Python.

## Executed publication-session checks

Both normal and optimized runs reproduced `results.json` byte-for-byte:

```sh
python checks/check_identities.py --output /tmp/rhg26-identities.json
python -O checks/check_identities.py --output /tmp/rhg26-identities-opt.json
cmp checks/results.json /tmp/rhg26-identities.json
cmp /tmp/rhg26-identities.json /tmp/rhg26-identities-opt.json
```

The output reports 740 finite Newton-prefix cases, 35 independently evaluated derivative constants, 36 exact formal-series coefficients for the Pólya–Gamma mixture, 42 energy-dilation cases, an exact positive native covariance control, and six expected rejection controls. These are not counts of infinite theorems or a full mutation-testing campaign.

The Gaussian prefactor control checks its algebraic H-scaling; it is not an independently enclosed numerical Fourier integral. The formal Pólya–Gamma checks compare finitely many Taylor coefficients, not the infinite probability law. The written arguments supply the infinite identities and remain subject to mathematical review.

## SHA-256 receipts

| File | SHA-256 |
|---|---|
| `../evidence/mobius_packet_check.py` | `d8b87123900d07c9db074f8d6c030e251b5f24eb5aab56cbc55b3850cfff81fa` |
| `../evidence/mobius_packet_check_results.json` | `cadabefd169b0f3e61739d7d647cc647bf93f765c1adfe2dfa00b7471e79c061` |
| `check_identities.py` | `9415fe171dc3b3f7d6205b938b9f01e849be9b6779fedabe9bc22358bab996a9` |
| `results.json` | `0abb014bafc09631b86d1a4fccbdcbfbdadad60043cdbb580e0e54d7abd2bc1f` |

Only the code and results named in the receipt have these SHA-256 bindings. The Git commit/tree binds the accompanying Markdown files. A passing check does not establish the native subpolynomial bound, nested Golomb density, a prime-zeta continuation theorem, or RH.
