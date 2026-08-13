# X-91134 — Uniform `P_61` score-Lorenz cutoff

Companion replay for `L-91357`.

```bash
python3 experiments/X-91134-p61-score-lorenz-cutoff/verify.py
```

Expected verdict:

```text
PASS_P61_SCORE_LORENZ_CUTOFF_10000
```

The checker uses only the Python standard library. It enumerates all `2^18` squarefree divisors of `P_61`, keeps the reciprocal sums exact with `Fraction`, and uses directed rational inverse-square-root bounds. It certifies the fixed reserve

```text
5 sqrt(10000) A_C - 3 B_C - 335/sqrt(10000) > 0.
```

The analytic theorem then implies that the score-Lorenz cutoff is always below `10000`, independently of `p>=67` and `1<=y<=67`.

The replay does not certify the remaining row-prefix determinants or RH.
