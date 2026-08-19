# L-99241 — Child-mass contraction makes the complete fixed-row calibration defect Mellin-holomorphic

Claim ID: `L-99241`  
Status: **PROVED EXACT TREE/ANALYTIC THEOREM**  
Created: 2026-08-19  
Depends on: `L-99240`; factor-67 source typing  
RH status: **not assumed**

Fix a root endpoint \(X\) and one component row \(j\). Let \(\mathcal T_X\)
be the finite labelled source tree produced by compact Hall, common-parent
partition and residual-only causal splitting.

For a node \(v\), let \(m_v\ge0\) be its positive source mass. Only the
normalized \(\alpha\)-children recurse, and the exact causal coefficients give

\[
\sum_{w\succ v}m_w\le\kappa m_v,
\qquad
\kappa<\frac18.
\tag{L-99241.1}
\]

The compact root source has uniformly bounded mass. One may use the exact
directed bound \(M_{67}<16\), but only finiteness is required:

\[
m_{\rm root}\le M_0<\infty.
\tag{L-99241.2}
\]

Let \(C_v(j)\) be the signed local calibration coordinate per unit node source,
including retained-cell quadrature, activation-knot atoms and the two
Volterra boundary modes. By `L-99240`,

\[
|C_v(j)|\le B_j.
\tag{L-99241.3}
\]

The fully resolved defect is

\[
\mathfrak E_X(j)=\sum_{v\in\mathcal T_X}m_v C_v(j).
\tag{L-99241.4}
\]

Since the tree is finite and positive,

\[
\sum_{v\in\mathcal T_X}m_v
\le M_0\sum_{\ell\ge0}\kappa^\ell
\le\frac{M_0}{1-\kappa}.
\]

Therefore

\[
\boxed{
|\mathfrak E_X(j)|
\le
\frac{M_0B_j}{1-\kappa}
\le
\frac87M_0B_j.
}
\tag{L-99241.5}
\]

In particular, the resolved defect is uniformly bounded as \(X\to\infty\).

For any \(X_0>1\), define

\[
\mathcal E_j(s)
=
\int_{X_0}^{\infty}
\mathfrak E_X(j)X^{-s-1}\,dX.
\tag{L-99241.6}
\]

The bound (L-99241.5) gives absolute locally uniform convergence on every
closed half-plane \(\Re s\ge\delta>0\). Hence

\[
\boxed{
\mathcal E_j(s)\text{ is holomorphic on }\Re s>0.
}
\tag{L-99241.7}
\]

The theorem uses no sign of the calibration defect and no equality-score
normalization.
