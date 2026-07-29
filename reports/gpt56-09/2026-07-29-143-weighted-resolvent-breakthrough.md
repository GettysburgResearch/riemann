# Continuation report — weighted-resolvent breakthrough for Issue #143

Agent: `gpt56-09`  
Date: 2026-07-29  
Branch: `agent/gpt56-09/143-finite-diagonal-prolate`  
Claim added: `L-14302`

## Breakthrough

The first positive criterion `T-14301` reduced RH to proving

\[
 t_j+q_j\kappa_jR_j/g_j\longrightarrow0.
\]

The factor `kappa_j` is a worst-case Hardy-weight amplification over the entire
even complement.  It can grow because of endpoint-heavy modes that the actual
prolate residual never excites.  Therefore it was likely to be the wrong
quantity for an asymptotic proof.

`L-14302` removes it.  In the decomposition

\[
 A=\begin{pmatrix}\mu&b^*\\b&C\end{pmatrix}
\]

around the normalized projected prolate target `v`, let `M` be the exact
Hardy-strip weighted Gram operator on the complement.  If `U` is a certified
upper endpoint for the ground eigenvalue and

\[
 C-UI\succeq hM,
\]

then the exact ground eigenline satisfies

\[
 \inf_c\|c\xi-v\|_M
 \leq \frac{\|b\|_{M^{-1}}}{h}.
\]

For the full prolate target this gives

\[
 \boxed{
 d_j^+=t_j+q_jB_j/h_j,
 \qquad B_j\geq\|b_j\|_{M_j^{-1}}.}
\]

Thus Gate 9 becomes a residual-specific weighted coercivity problem rather than
a worst-case embedding problem.

## Proof kernel

The complement eigen-equation is

\[
 (C-\lambda_0I)w=-\alpha b.
\]

Since `U>=lambda_0`,

\[
 C-\lambda_0I\succeq C-UI\succeq hM.
\]

Conjugating by `M^{-1/2}` and inverting yields

\[
 \|w/\alpha\|_M
 \leq h^{-1}\|b\|_{M^{-1}}.
\]

Projective scaling matches the target component along `v` exactly.

The interval version is also finite and exact.  If `||A-A_0||<=delta`,
`M>=mI`, `C_0-UI>=h_0M`, and `||b_0||_{M^{-1}}<=B_0`, then

\[
 h=h_0-\delta/m,
 \qquad B=B_0+\delta/\sqrt m.
\]

The dual norm bound is certified by the rational Schur-complement matrix

\[
 \begin{pmatrix}B_0^2&b_0^*\\b_0&M\end{pmatrix}\succeq0.
\]

## Important caught error

The first scratch statement used a lower eigenvalue endpoint.  This reverses the
monotonicity of `C-lambda I` and is invalid.  The committed theorem was replaced
immediately and uses only a certified upper endpoint `U>=lambda_0`.

## Why this matters asymptotically

The old term `kappa R/g` can be dominated by a high-weight complement mode even
when the residual is orthogonal to it.  The new ratio sees only the actual
coupling.  In diagonal coordinates it is schematically

\[
 \frac1h
 \left(\sum_r\frac{|b_r|^2}{m_r}\right)^{1/2},
\]

so endpoint-heavy modes with large Hardy weights `m_r` are automatically
downweighted in the dual norm.

This is the favorable direction for the prolate candidate: the obstacle created
by endpoint weights becomes part of the inverse metric rather than a global
penalty.

## New exact analytic target

A complete proof through this route would follow from estimates

\[
 t_j\to0,
 \qquad
 q_j\|b_j\|_{M_j^{-1}}/h_j\to0.
\]

The next attack should expand

\[
 b_j=P_{v_j^\perp}(QW_{\lambda_j}-\mu_j)v_j
\]

using the prolate differential equation before norms are taken.  The hoped-for
identity is cancellation between prime, pole, and archimedean contributions in
the dual Hardy norm, paired with a direct weighted complement coercivity bound.

## Claim boundary

This is a proved finite-dimensional reduction pending independent review.  It
does not establish the required asymptotic estimates and therefore does not yet
prove RH.