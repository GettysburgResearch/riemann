# X-91108 — Euler remainder Schur port and positive rough Euler cubes

Companion replay for `L-91316` and `L-91317`.

```bash
python3 experiments/X-91108-euler-remainder-schur-port/verify.py
sha256sum -c experiments/X-91108-euler-remainder-schur-port/SHA256SUMS
```

Expected verdict:

```text
PASS_EULER_REMAINDER_SCHUR_PORT_AND_POSITIVE_CUBES
```

The standard-library checker uses exact `Fraction` arithmetic and directed rational
square-root enclosures. It certifies:

- the sharp `N=1` gate needed for
  `|rho(x)| < (8/9) varrho(x)`;
- a rigorous Euler-transformed lower bound for `-zeta(1/2)`;
- the exact critical mass
  `prod_(p<=53)(1+1/p) < 9/2`;
- the off-diagonal endpoint-port mass bound below `4`;
- representative finite Boolean-cube product identities.

The replay certifies finite gates and algebra only. It does not prove the remaining
projective `(L,R)` cone conversion or RH.
