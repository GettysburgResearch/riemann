# X-92201 — Higher-Loewner firewall after scalar curvature closure

Run:

```bash
python3 verify.py
```

Retained verdict:

```text
PASS_HIGHER_LOEWNER_FIREWALL
```

The replay uses only `fractions.Fraction`. It reconstructs the exact rational
impedance consisting of one lower real anchor and one high conjugate off-line
pair, checks the positive-coefficient polynomial proving strict ordinary
concavity, and evaluates the exact negative determinant of the three-node
Loewner matrix at

```text
1/4, 600000, 600000000.
```

The control proves that scalar monotonicity, conjugate monotonicity, strict
ordinary concavity, and the complete order-three Caratheodory shadow do not
imply complete-Bernstein passivity.

It is a synthetic squared-pole model, not Riemann-xi data, and proves no
negative statement about the actual Xi impedance.
