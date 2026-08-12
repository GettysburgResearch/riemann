# X-91124 — `P_61` one-prime target/score certificate

Companion exact replay for `L-91345`.

```bash
python3 experiments/X-91124-p61-one-prime-target-score/verify.py
```

Expected verdict:

```text
PASS_P61_ONE_PRIME_TARGET_SCORE_SURPLUS
```

The checker uses only exact integer and `Fraction` arithmetic. It verifies all
`262,144` squarefree divisor-prefix states of `P_61`, proving:

- `A_61(z) <= 1` globally;
- the exact minimum of `A_61(z)` for `z >= 67`, attained on the cell beginning
  at `z=70`;
- the uniform positive gap after subtracting the worst child term `1/67`;
- the affine target and score interpolation and the common `9/50` lower
  coefficient imported from `L-91328`.

The replay does not certify the remaining finite Green-boundary row inequality,
ordinary/radix-four physical splice, or RH.
