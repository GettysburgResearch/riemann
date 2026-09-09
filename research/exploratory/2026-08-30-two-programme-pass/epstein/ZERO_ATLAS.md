# E2 — Zero atlas at the arithmetic points (t in (0,30))

NON_DIRECTED_HIGH_PRECISION numerics, dps=40; zeros to 12 digits; window t in
[0.05, 30.0] (see SCOPE.md for the bottom margin), box delta = 0.2.

At z = i (square lattice) Lambda_i(s) = 4 pi^{-s} Gamma(s) zeta(s) beta(s), so its
on-line zeros are the union of zeta zeros and Dirichlet-beta zeros; at
z = 1/2 + i sqrt(3)/2 (hexagonal) the factor is 6 (2/sqrt3)^{-s} zeta(s) L(s,chi_-3)
(zeros: zeta union L(s,chi_-3)). Each zero below is labeled by which factor vanishes.

## square_z_i  (z = 0.0 + 1.000000000000 i)

on-line zeros found: 13; argument-principle box count: 13; discrepancy: **0**

| # | t (12 digits) | factor |
|---|---|---|
| 1 | 6.020948904698 | beta_chi_-4 |
| 2 | 10.243770304167 | beta_chi_-4 |
| 3 | 12.988098012312 | beta_chi_-4 |
| 4 | 14.134725141735 | zeta |
| 5 | 16.342607104587 | beta_chi_-4 |
| 6 | 18.291993196124 | beta_chi_-4 |
| 7 | 21.022039638772 | zeta |
| 8 | 21.450611343983 | beta_chi_-4 |
| 9 | 23.278376520460 | beta_chi_-4 |
| 10 | 25.010857580146 | zeta |
| 11 | 25.728756425089 | beta_chi_-4 |
| 12 | 28.359634343025 | beta_chi_-4 |
| 13 | 29.656384014593 | beta_chi_-4 |

## hexagonal  (z = 0.5 + 0.866025403784 i)

on-line zeros found: 11; argument-principle box count: 11; discrepancy: **0**

| # | t (12 digits) | factor |
|---|---|---|
| 1 | 8.039737155681 | L_chi_-3 |
| 2 | 11.249206207773 | L_chi_-3 |
| 3 | 14.134725141735 | zeta |
| 4 | 15.704619176722 | L_chi_-3 |
| 5 | 18.261997495693 | L_chi_-3 |
| 6 | 20.455770807742 | L_chi_-3 |
| 7 | 21.022039638772 | zeta |
| 8 | 24.059414856493 | L_chi_-3 |
| 9 | 25.010857580146 | zeta |
| 10 | 26.577868735775 | L_chi_-3 |
| 11 | 28.218164506233 | L_chi_-3 |

Both boxes match the on-line counts exactly: **no off-line zeros were detected in
[1/2-0.2, 1/2+0.2] x (0,30) at either arithmetic point — consistent with GRH numerically**
(for the factor L-functions; this is a finite numerical check to the stated precision,
not a theorem, and RH/GRH remain unproved).

This is the arithmetic baseline for E3/E4: at these two CM points the survival ladder is
maximal (Euler product + FE), and every low-height zero sits on the line to 12 digits.
