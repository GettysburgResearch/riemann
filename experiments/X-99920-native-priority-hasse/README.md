# X-99920 — Native priority-Hasse surface replay

The verifier uses exact `fractions.Fraction` arithmetic.  It checks:

- nodewise conservation of the priority-Hasse flow;
- the two-labelled-67 native fibres;
- activation-truncated flow feasibility;
- equality of unmatched odd mass and upward surface flux;
- the Stieltjes/coarea identity on an exact clipped-linear potential;
- the Cauchy-Poisson coefficient-tail identity;
- the exact negative prefix `sum_(n<=13) mu(n)/n=-2323/30030`;
- hostile mutations of the owner weights, 67 multiplicity, and monotonicity.

Run:

```bash
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v
```

This finite replay authenticates the algebraic reductions.  It does not prove the all-scale `UPBF67` estimate or RH.
