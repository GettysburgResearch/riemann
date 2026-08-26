# X-106030 — Mollified owner-conductor moment replay

Standard-library exact replay for `L-106025--L-106027` and the finite algebra
behind `T-106030`.

It checks:

```text
owner-excluded twisted Moebius is the Dirichlet-convolution inverse of the
owner-excluded twisted constant source;

the balanced fixed-cutoff Vaughan row equals
  mu - 2 mu_U + mu_U * mu_U * 1
and therefore the coefficient expansion of
  (1-M_U Z)^2 / Z;

P a^2 remains in the quadratic owner class kappa_rho(P);

the quadratic root field equals sigma times the principal root field inside
one owner class;

exact cyclic Mellin/Plancherel algebra for Gaussian-integer fixtures.
```

The replay uses exact integer and Gaussian-integer arithmetic. It does not
evaluate an `L`-function, remove the physical shell projection, prove either
`PCM106030` or `NEM106030`, prove `SOCM106020`, or prove RH.

Run:

```bash
python3 verify.py --output /tmp/x106030.json
cmp /tmp/x106030.json results/verification.json
```

Expected verdict:

```text
PASS_X_106030_MOLLIFIED_OWNER_CONDUCTOR_NORMAL_FORM
```
