# X-91127 — `P_61` literal one-prime entropy-surplus certificate

This replay certifies the directed finite gates in `L-91348`.

It checks:

- all `2^18=262144` signed divisor-prefix states of `P_61`;
- the exact nonnegative sieved density `lambda_P` through the finite range;
- the prefix corridors for `a_0`, `a_1`, and `b_0`;
- every derivative-gap cell `67<=X<15000`;
- every terminal score cell `1<=y<67`;
- the exact rational analytic tail and final one-prime margin.

Run:

```bash
python3 verify.py
```

Expected verdict:

```text
PASS_P61_LITERAL_ENTROPY_SURPLUS
```

The replay certifies the directed finite inequalities. The global proof also uses the analytic monotonicity and telescoping arguments written in `L-91348`. It does not prove the remaining complete current-row physical realization or RH.
