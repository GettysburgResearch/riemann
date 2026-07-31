# X-15606 — Exact strict symbol-capacity regression

This standard-library-only checker verifies the finite algebra behind
`R-15603`:

```text
A >= Gamma I-D,
A|L <= alpha I,
D > 0,
alpha < Gamma
```

forces

```text
Tr D > dim(L)(Gamma-alpha).
```

The retained exact control is

```text
Gamma = 2,
alpha = 0,
D = diag(2,1/3),
A = Gamma I-D = diag(0,5/3),
L = span(e1).
```

It certifies

```text
packet requirement       2,
total deficit trace      7/3,
strict positive slack    1/3,
complement floor         5/3.
```

The analytic step that upgrades the finite positive-definite model to a genuine
time-frequency localization operator is proved in `R-15603`: Paley–Wiener
uniqueness makes every nonzero localization strictly positive and infinite
rank.

Run:

```bash
python3 verify.py certificates/synthetic.json
python3 -m unittest discover -s tests -v
```

The checker uses only Python integers, JSON, `hashlib`, and
`fractions.Fraction`.
