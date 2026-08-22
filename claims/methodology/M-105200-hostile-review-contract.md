# M-105200 — Hostile review contract for the summable Xi residue tail

Review in this order:

1. verify the exact centered coefficient cancellation in `L-105200.4`;
2. check that the saddle estimates really provide fixed centered moments of
   every order used in `L-105200.7`;
3. check the normalization `kappa_m^2=M_(m+1)/M_(m-1)` and the identity
   `M_(m-1) kappa_m^2=M_(m+1)`;
4. reconstruct the uniform lower bound for the adjacent derivative at every
   model-cell zero;
5. verify that the coherence loss is quadratic in the residue error;
6. check the log-convex moment ratio used in `L-105202`;
7. keep fixed-height and growing-height statements separate;
8. confirm that `L-105201.7` concerns only multiplicative coherence and does not sum the one-step endpoint `-1`;
9. confirm that no claim is made for the finite derivative prefix or RH.

Immediate falsifiers:

- an omitted uncentered carrier in `Delta_m`;
- only `O(m^-1/2)` relative residue control;
- a denominator lower bound that fails near a cell endpoint;
- replacing a local fixed-window debt by the global polynomial debt;
- claiming that summable high-tail loss controls the finite prefix.
