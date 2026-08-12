# X-91404 — Three-scale Cauchy quasi-Lévy source replay

This replay supports `L-91404`.

At

```text
a=4,
carrier=0.83,
prime-power cutoff=50000,
```

it checks:

- the exact phase differential
  ```text
  partial_x log Theta_c(x)=2 i Re[xi'/xi(1/2+c+ix)];
  ```
- the identity
  ```text
  N_x(c)=c/(4i) (1-c partial_c) partial_x log Theta_c(x);
  ```
- the three-scale recurrence
  ```text
  E_x(a)-E_x(2a)
   =a^-4[-N_x(a)+17/16 N_x(2a)-1/16 N_x(4a)];
  ```
- Nakamura's quasi-Lévy source reconstruction of each `N_x(c)`;
- the exact source coefficients
  ```text
  kappa_1=1/(2a^3),
  kappa_2=-17/(16a^3),
  kappa_4=1/(8a^3);
  ```
- the termwise equality of the three-scale prime source with the physical
  rational residual kernel `r_a(log n)`.

Retained errors:

```text
phase differential error       1.89e-81
three-scale source error        3.45e-18
prime residual identity error   8.84e-75
```

The sign table is

```text
positive source sectors:
  r=1, nu_plus
  r=2, nu_minus
  r=4, nu_plus

negative source sectors:
  r=1, nu_minus
  r=2, nu_plus
  r=4, nu_minus.
```

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_THREE_SCALE_CAUCHY_QUASI_LEVY_SOURCE
```

The replay verifies finite source and differential identities. It does not
prove the all-packet positive-sector domination, the delayed screw/Weil Gram,
or RH.
