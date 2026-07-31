# X-14307 — Exact radical-tail ratio contraction

This standard-library checker verifies two finite layers used by `T-14303`:

1. the polynomial-Gaussian source
   `(z^2-3z/2) exp(-pi x^2)`, `z=pi x^2`, is fixed by the additive Fourier
   transform and satisfies both exact source constraints;
2. proof-gated rational bounds for `T`, `h`, and `||k||^2` imply exact upper
   bounds for `T/h` and `T^2/(h||k||^2)`.

It does not evaluate zeta, a Weil form, or the analytic Gaussian tail. Those
inputs remain separate proof gates.

Run:

```bash
python experiments/X-14307-radical-tail-ratio/verify.py \
  experiments/X-14307-radical-tail-ratio/certificates/synthetic.json \
  --output experiments/X-14307-radical-tail-ratio/results/synthetic-verification.json
python -m unittest discover \
  -s experiments/X-14307-radical-tail-ratio/tests -v
```
