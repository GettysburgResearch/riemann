# X-106670 — regularized Pick free-energy replay

Run

```bash
python experiments/X-106670-regularized-pick-free-energy/verify.py
```

The replay checks exact source-Pick determinants, Jacobi derivatives,
conditional pivots, positive cycle coefficients, the lossless free-energy
sandwich, the full/cutoff allowance arithmetic, the equal-rank Cauchy/Frullani
identity, and the height/raw-volume firewalls.

It is a finite-dimensional identity replay. It does not estimate the Xi
partition function and does not prove more than 90%, density one, or RH.
