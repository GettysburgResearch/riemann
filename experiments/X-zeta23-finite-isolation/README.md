# X-zeta23-finite-isolation

Finite numerical regression for `FINITE_OFFLINE_ISOLATION.md`.

Run:

```bash
python3 experiments/X-zeta23-finite-isolation/verify.py
sha256sum -c experiments/X-zeta23-finite-isolation/SHA256SUMS
```

The control uses the rectangular aggregate-power profile on an interval of length eight. It verifies:

- positive definiteness of the complex exponential evaluation Gram;
- the exact two-point capture cost
  ```text
  2/[L^2(sinh(yL)/(yL)-1)];
  ```
- exact minimum-norm interpolation of values `1,-1,0,...,0`;
- equality between the full inverse-Gram and target Schur-complement formulas;
- monotone increase of capture cost as nuisance-zero constraints are added;
- exact local Weil contribution `-2` for a multiplicity-one reflected pair;
- the corresponding far-tail operator threshold.

The dramatic growth of the retained capture costs illustrates the genuine remaining issue: exact finite interpolation is automatic, but uniform conditioning under clustered zero constraints is not.

The experiment proves no zero separation, tail estimate, corrected-kernel floor, or RH conclusion.
