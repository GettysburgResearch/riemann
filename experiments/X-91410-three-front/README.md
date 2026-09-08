# X-91410 — Three-front exact algebra replay

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
```

Retained verdict:

```text
PASS_X_91410_THREE_FRONT_EXACT_ALGEBRA
```

The replay checks only:

- the factor-54 first-entrance scale inequality for primes through 2000;
- the exact two-channel Stieltjes feature identity;
- the exact two-point Xi-impedance determinant factorization;
- the two-Green boundary-jet algebra on a finite synthetic source;
- a rational series certificate that `log(2)<3/4`.

It does **not** identify the arithmetic matrix port on Route I, construct the
theta Stieltjes measure on Route II, construct the completed Cauchy–Jordan
colligation on Route III, evaluate zeta, or prove RH.
