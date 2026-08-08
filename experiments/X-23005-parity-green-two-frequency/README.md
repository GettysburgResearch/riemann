# X-23005 — Exact parity–Green two-frequency regression

This standard-library checker verifies finite algebra used by `L-23013`--`L-23016`:

- positive digit-comb jump coefficients for bases 2, 3, and 5;
- exact contractions with the Möbius and Euler-aligned sources;
- the power-of-two Green matrix and cumulative-square factorization;
- exact PSD of the finite-horizon dyadic Poincare moat;
- the binary-digit recurrence through a finite endpoint;
- the parity/carry rational identity and rank-one bulk determinant.

It does **not** verify `PGC(R)`, an asymptotic shell-energy estimate, or RH.
