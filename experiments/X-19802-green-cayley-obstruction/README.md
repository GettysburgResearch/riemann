# X-19802 — Exact Green–Cayley obstruction

This standard-library-only experiment verifies the two-node rational control in
`R-19803`.

It checks exactly that:

- the lifted multiplier is a strict contraction;
- both multiplier entries are values of `(1-r)/(1+r)` at nonnegative raw
  Volterra coordinates;
- the trace-zero fiber is strictly positive;
- the declared Green vector satisfies the Euler equation;
- the Green lift is a right inverse in the observed plus coordinate;
- the induced observed map is `CKE=5I`.

Run:

```bash
python verify.py > results/synthetic-verification.json
python -m unittest discover -s tests -v > results/tests.txt 2>&1
```
