# X-24901 — RBC certificate schema

Run:

```bash
python3 verify.py certificates/synthetic.json
python3 -m unittest discover -s tests -v
```

Classification:

```text
EXACT_SYNTHETIC_RBC_SCHEMA_REGRESSION
```

The checker consumes only integers and `fractions.Fraction` after JSON parsing.
It verifies the abstract certificate arithmetic, not any zeta-specific packet.
