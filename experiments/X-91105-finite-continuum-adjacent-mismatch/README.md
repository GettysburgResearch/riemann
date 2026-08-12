# X-91105 — Finite/continuum adjacent mismatch certificate

Companion replay for `R-91102` and `L-91114`.

```bash
python3 experiments/X-91105-finite-continuum-adjacent-mismatch/verify.py
```

Expected verdict:

```text
PASS_FINITE_CONTINUUM_ADJACENT_MISMATCH
```

The checker uses only the Python standard library, exact `Fraction` arithmetic,
and directed rational square-root and atanh-log enclosures. It proves:

- the reset-window derivative constant `C_55<17`;
- `log 4>4/3`;
- the interior mismatch-plus-collar relative constant is below `174/K`;
- the coarse terminal coefficient `800/sqrt(c_0)` is below `6000`.

The analytic adjacent-difference identity, `zeta(3/2)<3`, ordinary carry
summation and radix-four telescope are proved in `L-91114`. The replay does not
prove the terminal quotient certificate, the rough-prime allocation, or RH.
