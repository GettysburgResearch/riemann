# X-102010 — Ratio-four half-divisor factorization replay

This exact standard-library replay checks the finite algebra used by
`L-102009--L-102010`:

- the local and global identities `eta*eta=1`;
- the half-completed source identity `h_U*h_U=a_U*a_U*mu`;
- vanishing of `h_U(n)` for `n<=U`;
- the piecewise differential formulas for `A_-` and `A_+`;
- the sharp `L2` Hardy multiplier bound `3`.

Run:

```bash
python3 experiments/X-102010-ratiofour-half-divisor/verify.py \
  --output experiments/X-102010-ratiofour-half-divisor/results/verification.json
```

Expected verdict:

```text
PASS_X_102010_RATIOFOUR_HALF_DIVISOR_FACTORIZATION
```

The replay does not prove `HHFE102010`, a subpower asymptotic, or RH.
