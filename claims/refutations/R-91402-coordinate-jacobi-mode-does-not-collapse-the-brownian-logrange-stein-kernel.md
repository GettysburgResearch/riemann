# R-91402 — A quadratic Beta-coordinate Stein mode does not collapse the completed Brownian log-range Stein kernel

Claim ID: `R-91402`  
Status: **EXACT SCOPE CORRECTION / METHOD FIREWALL**  
Created: 2026-08-12  
Corrects: the overstrong application paragraph of `L-91406` and the corresponding reading of `T-91402`  
RH status: **unproved**

## 1. What `L-91406` actually proves

For one un-tilted Beta(2,2) coordinate `V`, or its beta-binomial shadow, the canonical Stein-kernel fluctuation is a degree-two Jacobi/Hahn mode. In the continuum,

\[
 \tau_V(v)-\mathbb E\tau_V
 =-\frac14\left(v^2-\frac15\right).
\]

This is exact and useful.

## 2. The completed Brownian variable is nonlinear and coupled

In the BPY two-copy reservoir of PR #401, after conditioning on the Gamma variables,

\[
 A=\sum_n c_nG_n,
 \qquad
 D=\sum_n c_nG_nV_n,
\]

and

\[
 Z_+=\frac12\log(A+D)+C,
 \qquad
 Z_- =\frac12\log(A-D)+C.
\]

The half-size tilt multiplies the product Beta law by

\[
 H_G(V)=(A^2-D^2)^{1/4}.
\]

Thus the coordinates are no longer independent under the completed tilt, and `Z_+`, `Z_-`, `S=Z_++Z_-`, and `Delta=Z_+-Z_-` are nonlinear functions of all coordinates.

Their exact gradients are

\[
 \partial_{V_n}S
 =-\frac{c_nG_nD}{A^2-D^2},
 \qquad
 \partial_{V_n}\Delta
 =\frac{c_nG_nA}{A^2-D^2}.
\]

## 3. Why the low-rank inference is invalid

The one-dimensional Stein kernel of `S` or `Z_+` is not obtained by substituting the coordinate Stein kernel `(1-V_n^2)/4`. It is a conditional carré-du-champ involving the Poisson solution for the nonlinear observable; see `L-91409`.

Even though each coordinate multiplier is quadratic, the Poisson solution and its gradients may contain arbitrarily high multivariate Jacobi modes. The completed tilt also changes the reversible generator's drift.

Therefore the following inference is invalid:

```text
coordinate Beta Stein variability is quadratic
=> completed log-range Stein variability is one quadratic port.
```

No such collapse has been proved.

## 4. Correct surviving use

The beta-binomial/Hahn chain remains a canonical finite positive approximation to the coordinate reservoir, and `L-91405/L-91408` give exact coercivity and edge-current identities for its low modes. They may be used inside a full multivariate Poisson/DtN construction.

The actual Brownian/theta gate remains:

```text
solve the completed tilted product Poisson equation;
identify the conditional carré-du-champ boundary response;
prove its complete polarized sign or factorization.
```

This correction does not refute the Brownian/theta route. It prevents a coordinate-level Jacobi identity from being promoted to the RH-bearing marginal statement.
