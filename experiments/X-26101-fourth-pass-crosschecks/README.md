# X-26101 — Fourth-pass exact cross-checks

This standard-library proof object accompanies the fourth-pass review of the live RH proposal graph.

Run:

```bash
python verify.py
```

It writes `results/verification.json` and exits nonzero on the first mismatch.

## Exact checks

- affine Möbius contraction of the carry row;
- divisor-gradient second difference;
- one-sided continuum/discrete carry comparison;
- the exact `-233/64` derivative-kernel determinant;
- dyadic digit convolution and binary digit partial sums;
- identification of the PR #243/#247/#252 carry profiles;
- exceptional `{2,3,4,5}` prime-power cluster inverse;
- finite full rank of endpoint-projected Dirichlet Grams;
- exact correction map `delta v=-G T`;
- finite regression for consecutive prime-power runs.

## What it does not prove

It does not prove any asymptotic estimate, positivity of the global carry state, Greedy Slack/DCRS, FGCM, GET, Constraint-Dipole Transport, BTP, a Schur reserve, a bounded charge map, or RH.
