# 2026-08-01 — Metric-balanced shifted-lattice attack on the square source scalar

## Objective

Attack

\[
 s_M={g_M\over\ell_MA_{M,M^2}^{-1}\ell_M^*}
 \ge-\varepsilon_M,
 \qquad
 \Lambda_M\varepsilon_M+\delta_M\to0,
\]

after the finite frame and Schur algebra have been closed.

## Exact new packet

For `1/2<theta<1` and degree `r`, use

\[
 R_{r,\theta}(x)
 =\prod_{j=1}^r
 {x-(j-\theta)^2\over x-j^2}.
\]

Its partial fractions give a positive source-normalized even vector. The full
D-0001 response has the exact factorial cancellation

\[
 g_{r,\theta,L}(z)
 =L\left[
 {\Gamma(r+1-\theta-\mu)\Gamma(r+1-\theta+\mu)
  \over
  \Gamma(1-\theta-\mu)\Gamma(1-\theta+\mu)
  \Gamma(r+1-\mu)\Gamma(r+1+\mu)}
 \right]^2,
 \qquad \mu={Lz\over2\pi}.
\]

The coefficient metric is

\[
 \|v_{r,\theta}\|^2=O_\theta(r^{2\theta-2}).
\]

Thus, at `(N,c)=(M,M^2)`, the complete affine graph adapter is

\[
 \Lambda_M^{notch}=O_\theta(Mr^{2\theta-2}).
\]

## Feasible exponent wedge

Take `r=M^beta`. After source scaling and the graph adapter, one fixed zero
`z=a+ib`, `|b|<1/2`, contributes at most

\[
 O_{\theta,z}\left(
  (\log M)^{4\theta-1}
  M^{2+2|b|-\beta(2\theta+2)}
 \right).
\]

Therefore every fixed off-line mode is suppressed whenever

\[
 {3\over2(1+\theta)}<\beta<1.
\]

The rational choice

\[
 \theta={3\over4},\qquad\beta={9\over10}
\]

gives

\[
 \Lambda_M^{notch}=O(M^{11/20}),
 \qquad
 \Lambda_M^{notch}\varepsilon_{M,z}
 =O_z((\log M)^2M^{-3/20}).
\]

Its degree also satisfies

\[
 M^{9/10}=o(\sqrt{M^2/\log(M^2)}),
\]

so the fixed-core notch and the sub-square-root support-average envelope are
simultaneously compatible. The half-shift is exactly critical and has no such
sub-full-degree wedge.

## Exact finite replay

`X-20803` checks the rational product, positive residues, source normalization,
and partial-fraction response at `theta=3/4` using only `Fraction`. The retained
levels through `N=6` pass exactly; the mutation suite covers invalid shifts and
dimensions.

## Decisive limitation

For the explicit trial `x_M=g_Mv_M`,

\[
 s_M={1\over g_M}
 \left[
  \langle A_Mx_M,x_M\rangle
  -(P_WA_Mx_M)^*A_{WW,M}^{-1}(P_WA_Mx_M)
 \right].
\]

The new theorem controls the fixed-frequency contribution to the first term,
including every metric and factorial cost. It does not control the residual
dual norm. `R-20802` gives a two-dimensional exact counterexample showing that
raw trial suppression cannot be promoted to a Schur lower bound.

The irreducible remaining producer is now one joint line-centered graph/residual
estimate for this explicit packet. This is narrower than the previous target:
fixed-mode attenuation, coefficient conditioning, and factorial normalization
are no longer open.

No RH proof is claimed.
