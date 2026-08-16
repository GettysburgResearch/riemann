# X-20204 — Symbolic transcendental-pin replay

This standard-library checker verifies the finite algebra used by `T-20206`.
It treats `exp(-N)` as a **typed transcendental symbol**, not a floating number.

The retained synthetic example uses the rational base filter

```text
lambda=(30,-12,2),
N=3,
pin=exp(-3) at tap 1.
```

For parent multiplicity `2` and descendant multiplicities `(1,3)`, the pole
residue has the formal form

```text
66 + 2 exp(-3).
```

Its transcendental coefficient is nonzero, so it cannot vanish against the
algebraic base part. The checker also verifies:

- the exact pinned ramp value at `s=1/2`;
- full prime support exponent `2` at the critical mesh;
- pin-only prime support exponent `2/N=2/3`;
- strict schema, tap, multiplicity, and transcendence gates.

Eight central/mutation tests are included.

```bash
python3 verify.py certificates/synthetic.json
python3 -m unittest discover -s tests -v
```

This is synthetic symbolic algebra only. Lindemann--Weierstrass, the imported
screw/Laplace normalization, Landau continuation, and every zeta sign remain
analytic proof dependencies.
