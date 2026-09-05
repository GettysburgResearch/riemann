# X-105250 replay

Run:

```bash
python3 experiments/X-105250-polynomial-wick-hierarchy/verify.py
```

The standard-library replay checks exact rational coefficient identities,
positivity through `K=12`, the eventual coefficient constant, the Banach
coefficient and Lipschitz sums, the general energy bound, and the exact
degree-one/degree-two `99/101` proportion comparisons.

It does not evaluate Xi, replay the external PNT prime-simplex theorem, prove
the actual contour transfer, establish 90%, establish density one, or prove RH.
