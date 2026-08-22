# X-102780 — Outer-ray radial-duality replay

This standard-library replay checks:

- the change of variables from the original radial SDP to the one-dimensional
  primal;
- weak duality on exact rational fixtures;
- feasibility of the distinguished rank-one dual point;
- the `w=-8` outer-ray identity;
- the exact three-ray Lagrange coefficients `136,120,-255`;
- sharpness of the source-blind countermodel.

It does not prove `OER102780` or RH.