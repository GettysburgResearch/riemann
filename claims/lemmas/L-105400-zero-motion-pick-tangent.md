# L-105400 — Zero-motion representation of the Pick current

Let `F_delta=F'+delta F`. If `c` is a simple zero of `F'`, implicit
differentiation gives

\[
\boxed{c'(0)=-F(c)/F''(c).}
\]

For analytic primitives `Psi_ij' = phi_i phi_j`, differentiation of the
ordinary zero statistic gives

\[
\boxed{
\left.\frac d{d\delta}\sum_{F_\delta(c)=0}\Psi_{ij}(c)\right|_0
=-\sum_{F'(c)=0}\frac{F(c)}{F''(c)}\phi_i(c)\phi_j(c).}
\]

The right side is the low-order Hermite--Pick matrix. T-105340 supplies the
confluent contour version without simplicity.
