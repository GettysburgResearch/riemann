# Phase-flow / real-only Gate-0 packet

This exploratory packet makes a first exact pass on:

1. the flower/petal geometry of `zeta(1/2+it)`;
2. a real-only inverse-Poisson representation of zero displacement.

Start with [`MATHEMATICS.md`](MATHEMATICS.md).

## Principal results

- `PFR-T1`: exact Hardy-flower area, speed, curvature, weighted Wirtinger,
  and participation-count identities;
- `PFR-T2`: the centered-Xi flower phase velocity above the zero strip is an
  absolutely convergent real prime cosine signal on `Re(s)>1`;
- `PFR-T3`: for every finite real zero model, inverse Poisson evolution gives
  a real response whose weighted-energy abscissa is exactly the maximal
  off-axis zero height;
- `PFR-T4`: the same de-Poissonization is the critical-weight explicit formula
  for actual Xi, in distributional form;
- `PFR-R1`: an Xi-symmetric off-axis quartet can have only real derivative
  critical points, closing any generic one-quartet/one-Speiser-branch rule.

## Replay

```bash
python3 code/verify_phase_real.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Expected terminal markers:

```text
PASS_PFR_PHASE_REAL_TRANSDUCER
RH_UNPROVEN
```

The replay authenticates finite algebra and high-precision regressions only.
The analytic proofs are in the manuscript and require ordinary mathematical
review.

## Scope

No zero is newly located. No zero proportion is improved. No RH or GRH claim is
made. External novelty and priority are explicitly unreviewed.
