# X-90704 — Q4 Fourier–Goldbach normal-form replay

This standard-library checker verifies the exact finite identities of `L-90703`
and the sine-mode firewall `R-90703`:

- rational physical/max-kernel/Goldbach expansions;
- cyclic cosine diagonalisation;
- singular discrete-antiderivative formula;
- exact linear operator loss on the first sine mode;
- formal radix-four block-prime identity in independent `log(p)` symbols.

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_90704_Q4_FOURIER_GOLDBACH_NORMAL_FORM
```

The replay proves finite algebra only. It does not prove the arithmetic
Fourier/Goldbach estimate, transfer it to the exact QIDR block measure, prove
PIG, or prove RH.
