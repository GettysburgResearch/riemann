## T105330 addendum — dual Vandermonde contour hierarchy

This continuation converts the two sharp parent last-defect gates into exact
scalar determinant hierarchies while preserving the statement that RH remains
unproved.

### Critical hierarchy

For one regular critical window,

```text
P_rs = -(2pi i)^(-1) integral (F/F')(z) z^(r+s) dz
G_rs =  (2pi i)^(-1) integral (F''/F')(z) z^(r+s) dz
```

satisfy

```text
P = V^T diag(-rho_c) V,
G = V^T V,
det(P+tG)/det(G) = product_c (t-rho_c).
```

Hence all critical points are real and all residues negative exactly when the
complete leading Hankel determinant hierarchy is positive.

### Boundary hierarchy

Every determinant of the parent Cauchy-Loewner remainder has an exact
Cauchy-Vandermonde multiple-contour formula. Nonnegativity for every real packet is exactly the boundary-PSD component of
`BRP105220`; `CRVH105330` supplies the separate nonreal-critical clause.

### Exact conclusion graph

```text
CRVH105330 AND BCVH105330
  -> PRES105220 AND BRP105220
  -> RH.
```

Neither hierarchy is proved for fixed low-order Xi.

### Firewall

For `p=x^4-2x^2-1`, the critical residues are
`(-1/4,+1/4,-1/4)`. The first two leading determinants are positive, while
the full determinant is `-1/16`. Bounded-order determinant tests cannot be
promoted to the pointwise gate.

### Moving-saddle audit

The moving-saddle theorem remains proposed. The correct contour translation
and the missing uniform global relative-dominance inequality are frozen in
`M-105331`.

### Replay

```text
PASS_X_105330_DUAL_VANDERMONDE_CONTOUR_HIERARCHIES
222 exact rational checks
93f59673fad499278a27b6a93f801d96156907759642bf6b8fc9fb0626a66c5e
```

The replay does not prove `CRVH105330`, `BCVH105330`, `PRES105220`,
`BRP105220`, the moving-saddle theorem, or RH.
