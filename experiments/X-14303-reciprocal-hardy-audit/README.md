# X-14303 — reciprocal-Hardy diagnostic audit

This experiment independently stress-tests the finite-dimensional inequality and
Fourier constants in `L-14303`. It is not a proof dependency.

Run:

```bash
python3 experiments/X-14303-reciprocal-hardy-audit/check.py
```

The deterministic script performs:

- 5,000 random SPD compression tests for the ordinary and constraint-corrected
  inverse-compression inequalities;
- 153 direct Hardy-Gram formula comparisons at 80 decimal digits;
- 153 reciprocal-Gram finite/full-line tail checks;
- finite direct-Gram spectral-floor checks through dimension 41.

The retained output is in `results/check.txt`.
