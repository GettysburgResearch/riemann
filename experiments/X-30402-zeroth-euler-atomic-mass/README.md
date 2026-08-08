# X-30402 — PR #304 terminal-source refutations

This standard-library checker supports `R-30402` and `R-30403`.

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
   already exceeds `floor(sqrt(X))/1000` on the retained endpoints;
4. at
   ```text
   (N,q,k,s)=(18,5,2,1),
   ```
   the actual zeroth boundary value is
   ```text
   49/19000,
   ```
   whereas the declared divisor-source load in column `5` is
   ```text
   -1/250.
   ```

Retained digest:

```text
cee6b423067889dcaaf718569e7082946d5cb61f943e288d97a96856b3940925
```

The all-endpoint `Omega(sqrt X)` lower bound is proved in `R-30402`. The source-type mismatch in `R-30403` is an exact finite contradiction.

The package does not refute every possible coupled source repair and does not prove Cycle Debt or RH.
