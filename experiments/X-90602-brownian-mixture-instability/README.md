# X-90602 — Positive Brownian-mixture instability regression

Finite exact-rational checks accompanying `L-90603`, `L-90604`, and `R-90602`.

The script verifies:

- normalization and positivity of logarithmic Nörlund and central-binomial Green weights;
- quantitative top-half mass at representative levels;
- positivity and the universal upper bound `b_(N,n)<=2` for the one-sided leading Dirichlet coefficients;
- exact finite coefficient-ratio controls for multiples.

Run:

```bash
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_X_90602_BROWNIAN_MIXTURE_INSTABILITY
```

The replay proves no Kronecker/Hurwitz or symmetrized Rouché theorem. Those are the analytic arguments in the claim files.
