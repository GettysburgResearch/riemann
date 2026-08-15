# O-93880 — PR #508 and PR #509 become compatible only after sector separation

PR #508 supplies a strong directed Target-Lorenz producer. PR #509 supplies an
exact native hybrid source marginal. Their shared ancestry is not independent
confirmation.

The compatible synthesis is:

```text
continuum bulk:
  use the rank-one Volterra/Möbius source;
  do not use Target-Lorenz or a normalized row profile;

anchored finite/rough sector:
  use the complete directed Target-Lorenz coefficients;
  retain current-only row bonuses and frontier rows explicitly;

finite realization:
  identity on anchored rows;
  martingale B-spline only on bulk;

native correction:
  retain one signed observation defect;
  pay it by all-column scalar thinning and top omission;

endpoint:
  use the direct Y4 slack and reconstruct only the one-way Mellin/Landau
  implication needed for RH.
```

This sector split removes a hidden quantifier mismatch: a theorem about
normalized root fibres need not be extrapolated to stopped rough leaves, and a
stopped-leaf determinant need not be imposed on the rank-one continuum bulk.
