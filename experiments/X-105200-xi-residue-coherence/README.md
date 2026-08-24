# X-105200 exact replay

The replay checks the finite algebra behind the centered monochromatic defect,
the quadratic coherence gain, moment log convexity, the harmonic zero-debt
model, the summable product bound, and the countermodel showing that an
unquantified `o(1)` coherence statement is insufficient.

It does **not** machine-prove the Laplace saddle estimates for Xi. Those are
analytic arguments in `L-105200` and inherited from `L-104504/L-104517`.

```bash
python -B verify.py --output results/verification.json
python -B -m unittest discover -s tests -p 'test_*.py' -v
```
