# X-28004 — Two-contact endpoint reserve

This exact standard-library checker supports the finite boundary portion of
`L-28015`.

For every integer row `4<=n<=15`, it evaluates all logarithms by the rational
identity

```text
log y = 2 atanh((y-1)/(y+1))
```

with an explicit positive geometric remainder. It then proves, by outward
interval arithmetic,

```text
32 R_2(n,2)-L_2(n)^2 > 0.
```

For the coincident interior position at `n=4`, it additionally proves

```text
16 R_2(4,2)-L_2(4)^2 > 0.
```

The range `n>=16` is handled analytically in `L-28015`.

Run:

```bash
python experiments/X-28004-two-contact-endpoint-reserve/verify.py
```

Expected verdict:

```text
PASS_EXACT_TWO_CONTACT_ENDPOINT_RESERVE
```

The checker proves only the finite logarithmic inequalities. It does not
construct the full source-coupled physical congruence or prove RH.
