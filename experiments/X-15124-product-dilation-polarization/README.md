# X-15124 — Product-dilation polarization

This exact standard-library regression verifies the corrected arithmetic ledger in `L-15152`.

It checks:

- the complete synthetic `Lambda_2` channel sum;
- equality of the grouped product-dilation form and the channel expansion;
- the exact polarization into positive squares minus mass terms;
- a finite control where product and factor-ratio orientations are different.

The arithmetic logarithms are replaced by exact rational symbolic values. The experiment is an algebraic regression, not Riemann data.

Run:

```bash
python experiments/X-15124-product-dilation-polarization/verify.py
python -m pytest -q experiments/X-15124-product-dilation-polarization/tests
```

Retained proof digest:

```text
2eb1ec14ec4f351c0546646dbe6fd6ec134b6cf8176b7f735f0be58fa9546b43
```
