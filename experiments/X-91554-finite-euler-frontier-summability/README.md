# X-91554 — finite Euler frontier summability

This standard-library directed replay certifies the explicit constants in
`L-91554`.

For a fixed small-prime Euler support `P`, the sourcewise terminal estimate is

```text
E_source(P)
 < 2(4 sqrt(67)-3) product_(q|P)(1+q^(-1/2)).
```

The replay proves

```text
P_79 bound < 5600;
P_61 bound < 3600.
```

All square roots use exact `Fraction` arithmetic and directed rational
intervals. The product identity itself is elementary expansion over squarefree
divisors.

This certificate does **not** certify the parent-index source normalization,
Hall residual coefficient bound, all-depth score telescope, physical
ordinary/radix-four assembly, or any RH conclusion. Those interfaces remain
mathematical review obligations.

```bash
python3 verify.py
```
