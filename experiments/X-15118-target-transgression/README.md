# X-15118 — Exact target-transgression checker

This experiment verifies the finite rational identities in `L-15138` and the
finite matrix inputs to `T-15116`.

It checks:

- raw and renormalized trace moments;
- the target defect
  `e_ell = a_ell^lin - Tr(K^ell)`;
- the exact logarithmic target-ratio coefficient
  `(-i)^(ell-2) e_ell / ell` at every retained even order;
- the quartic sign and factor `-e_4/4`;
- declared Hilbert--Schmidt radius and difference bounds;
- the quartic power-trace stability inequality.

The synthetic control deliberately has

```text
e_2 = 0,
e_4 = 5/7,
e_6 = -2/9,
e_8 = 0,
```

so

```text
log(F_lin/F_Ward)
 = -5/28 w^4 -1/27 w^6 + ...
```

It demonstrates that a quartic Ward discrepancy changes the entire target and
cannot be absorbed into constant/linear exponential factors.

The checker uses only Python integers, `fractions.Fraction`, JSON, and SHA-256.
It does not evaluate `xi`, a Guinand--Weil contour, or a Riemann seam map.

## Reproduction

```bash
python3 verify.py certificates/synthetic-quartic-transgression.json
python3 -m unittest discover -s tests -v
```
