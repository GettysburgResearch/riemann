# X-91402 — Prime-inclusive quasi-Lévy Hardy completion replay

This finite replay supports `L-91402`, `L-91403`, and `T-91401`.

It checks at

```text
sigma=9/2,
a=4,
t=0.83,
prime-power cutoff=50000:
```

- the one-sign-change formula for Nakamura's continuous quasi-Lévy density;
- the sign boundary `log(varpi)`, where `varpi^3-varpi-1=0`;
- the exact completed phase-derivative decomposition into:
  - Nakamura drift;
  - the short-jump positive archimedean channel;
  - the long-jump negative archimedean channel;
  - the ordinary-prime atomic channel;
- exact equality of the scored atomic channel with the ordinary-prime Suzuki
  score `beta_a` on the finite prime-power truncation;
- positivity of the score-orthogonal auxiliary Gram on a three-carrier packet.

The retained phase-derivative error is

```text
4.185360942331428e-18.
```

The auxiliary eigenvalues are

```text
7.780766610822354e-06
0.003109834069897429
0.47278065706571115.
```

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
identities. It does not prove that the positive auxiliary equals the delayed
zeta screw/Weil defect, and it does not prove RH.
