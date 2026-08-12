# X-91402 — Prime-inclusive quasi-Lévy Hardy completion replay

This finite replay supports `L-91402`, `L-91403`, `T-91401`, and the
negative-channel firewall `R-91403`.

It checks at

```text
sigma=9/2,
a=4,
t=0.83,
prime-power cutoff=50000:
```

- the one-sign-change formula for Nakamura's continuous quasi-Lévy density;
- the sign boundary `log(varpi)`, where `varpi^3-varpi-1=0`;
- the completed phase-derivative decomposition into:
  - Nakamura drift;
  - the short-jump positive archimedean channel;
  - the long-jump negative archimedean channel;
  - the ordinary-prime atomic channel;
- exact equality of the scored atomic channel with the ordinary-prime Suzuki
  score `beta_a` on the finite prime-power truncation;
- positivity of the score-orthogonal **total-variation** auxiliary Gram on a
  three-carrier packet;
- the exact Jordan-subtraction identity
  ```text
  signed defect = positive-dilation defect - 2 * negative-channel Gram;
  ```
- failure of automatic signed positivity before the structured
  Hardy/model-space/delay compression.

The retained phase-derivative error is

```text
4.185360942331428e-18.
```

The positive-dilation auxiliary eigenvalues are

```text
7.780766610822354e-06
0.003109834069897429
0.47278065706571115.
```

The negative-channel Gram eigenvalues are

```text
4.000179435278566e-06
0.0015882628086723192
0.23225685868866947.
```

After exact signed subtraction, the residual eigenvalues are

```text
-6.736415360827961e-05
-8.388778457951098e-11
 0.008267392786161332.
```

Thus the positive Jordan-dilation reserve is real and useful, but it cannot be
renamed the screw/Weil defect. The missing theorem must control the explicit
long-jump channel after all resident compressions.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_PRIME_INCLUSIVE_QUASI_LEVY_HARDY_COMPLETION
```

This is a finite numerical replay of primary-source and Hilbert-space
identities. It does not establish the all-packet negative-channel domination,
the delayed screw/Weil defect, or RH.
