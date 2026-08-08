# X-30402 — Zeroth Euler common-tail atomic-mass mutation

This standard-library checker supports `R-30402`.

Run:

```bash
python3 verify.py
```

It verifies with exact integer and `fractions.Fraction` arithmetic that:

1. for
   ```text
   floor((Y+1)/4)+1 <= q <= floor(Y/3),
   ```
   both omitted parity tails start at `k=2`;
2. the zeroth Euler jet has odd source-node atomic contribution
   ```text
   ell_Y/(10 sqrt(q));
   ```
3. the rational enclosure
   ```text
   ell_Y >= 1/(Y+1),
   1/sqrt(q) >= 1/ceil_sqrt(q)
   ```
   already exceeds `floor(sqrt(X))/1000` on the retained endpoints.

Retained digest:

```text
11522fe3473d961667b92fbec785d563bdea16ebd6cc79549492a19858c2298d
```

The all-endpoint `Omega(sqrt X)` lower bound is proved in `R-30402`; the finite replay is a mutation check, not an asymptotic proof.

The package does not refute every possible coupled source repair and does not prove Cycle Debt or RH.
