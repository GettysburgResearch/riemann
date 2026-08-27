# R-105300 — Gaussian-only moderate deviations and high-tail descent are invalid shortcuts

Claim ID: `R-105300`  
Status: **BINDING SCOPE FIREWALL**  
Created: 2026-08-23  
RH status: **unproved**

## 1. The cubic phase cannot be dropped at two-thirds height

Let

\[
b_m=\sqrt{w_m/m},
\qquad
\lambda=i s_mz,
\qquad
\gamma_m=S_m^{(3)}(w_m)s_m^3.
\]

`L-105301` proves

\[
\gamma_m=-\sqrt2\,b_m(1+o(1)).
\]

At a real height

\[
z=c(m/w_m)^{2/3},
\]

one has `lambda asy i c b_m^(-1/3)` and therefore

\[
{\gamma_m\lambda^3\over6}=\Theta_c(1),
\]

a nonvanishing imaginary phase correction. Hence

\[
A_m(z)e^{-iw_mz+s_m^2z^2/2}
\not\to1
\]

in general on this boundary. A proof which reuses the purely Gaussian model at
two-thirds height is false even though the corrected cubic exponential remains
nonzero.

## 2. Additive central-limit error is insufficient

For real `z` on a growing scale, the Gaussian characteristic factor
`exp(-s_m^2z^2/2)` can be exponentially small. An additive estimate

\[
A_m(z)=e^{iw_mz-s_m^2z^2/2}+o(1)
\]

has no zero-control content there. The contour shift in `L-105301` is
load-bearing because it produces a **relative** asymptotic after factoring the
small Gaussian and cubic saddle action.

## 3. Local quotient algebra is not a localization theorem

`L-105300` computes finite-polynomial residue moments by one quotient operator.
It does not justify replacing a height-window Xi residue sum by a polynomial
truncation. Exterior critical points, canonical-product convergence and
boundary flux remain explicit obligations.

## 4. High-tail coherence still does not imply RH

The improved entry order

\[
r(T)=O(T^{3/2}\log T)
\]

only removes the terminal off-real count from the reverse-Rolle ledger. It does
not control

\[
2\sum_{j<r(T)}R_j(1-\mathfrak C_j)
+
\sum_{j<r(T)}(B_j+W_j-1).
\]

The quantifiers `m>=M` and `M->infinity` cannot be exchanged with a fixed low
derivative order. `CRDB105200` and RH remain unproved.
