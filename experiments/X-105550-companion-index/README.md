# X-105550 replay

The checker authenticates exact polynomial reduction, Cauchy-phase algebra,
Blaschke dipole energy, model-space Gram inequalities, and hostile mutations.
Complex root counts are diagnostic fixtures with large separation margins; the
proof of the half-plane theorem is the argument-principle proof in L-105550.

```bash
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

It does not prove the Xi partial-index estimate, ninety percent, the public
record, or RH.
