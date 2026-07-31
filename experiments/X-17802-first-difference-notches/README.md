# X-17802 — Exact first-difference notch regression

The checker verifies, using only integers and `fractions.Fraction`:

- the `2^m` subset expansion of a five-fold normalized finite difference;
- coefficient absolute sum one;
- half the support cost of the old box-square construction;
- exact line-phase and off-line-displacement planning bounds;
- the rigorous `>10^115` five-notch frontier sensitivity gain.

It does not evaluate zeta zeros, prime powers, exponentials, or a Riemann
counterexample. The frontier and ordinate inequalities are typed external inputs
whose provenance remains an analytic review gate.

Run:

```bash
python verify.py certificates/synthetic.json --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```
