# X-30402 — PR #304 terminal-source refutations

This standard-library checker supports `R-30402`, `R-30403`, and `R-30404`.

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
2. the literal frozen source interpretation already has square-root layer-cake mass;
3. at
   ```text
   (N,q,k,s)=(18,5,2,1),
   ```
   the actual zeroth boundary value is
   ```text
   49/19000,
   ```
   whereas the declared divisor-source load in column `5` is
   ```text
   -1/250;
   ```
4. after the correct multiples-Möbius inversion, every source node in the transition interval has only the `d=1` term and contributes more than `7/400` to the atomic norm;
5. the resulting exact rational lower bound exceeds `N/2000` on every retained endpoint.

Retained digest:

```text
f1489351731335860a26909ce922ed27025e7bd6de89c97abd06e7e27a5ae4dd
```

The cofinal linear lower bound is proved in `R-30404`. The package does not refute every possible coupled non-atomic source repair and does not prove Cycle Debt or RH.
