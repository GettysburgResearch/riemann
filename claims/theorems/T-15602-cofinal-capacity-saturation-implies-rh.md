# T-15602 — Cofinal capacity saturation implies RH

Claim ID: `T-15602`  
Title: Exact low-index saturation and vanishing packet forms produce a cofinal localized-Weil lower envelope  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-d`  
Created: 2026-07-31  
Dependencies: `T-14302`; `L-15602`; `L-15603/L-15604`; localized-Weil support monotonicity  
Scope: completed logical form of the scalar capacity program

## Statement

Let `A_j` be exact localized Weil operators on an unbounded support sequence

\[
 a_j\longrightarrow\infty.
 \tag{T-15602.1}
\]

For each `j`, let `L_j` be a finite-dimensional exact repaired radical packet,
with coordinate map `J_j` and Gram matrix

\[
 G_j=J_j^*J_j\succ0.
 \tag{T-15602.2}
\]

Put

\[
 B_j=J_j^*A_jJ_j
 \tag{T-15602.3}
\]

and let the complete residual outside `L_j` have Gram

\[
 \mathcal R_j
 =J_j^*A_j(I-P_{L_j})A_jJ_j.
 \tag{T-15602.4}
\]

Suppose there are numbers

\[
 0\le\alpha_j<t_j<\Gamma_j,
 \qquad
 \beta_j\ge0,
 \qquad
 \delta_j\ge0
 \tag{T-15602.5}
\]

such that:

### A. Vanishing near-radical packet

\[
 -\alpha_jG_j\preceq B_j\preceq\alpha_jG_j,
 \tag{T-15602.6}
\]

\[
 0\preceq\mathcal R_j\preceq\beta_j^2G_j.
 \tag{T-15602.7}
\]

### B. Exact capacity saturation

The complete orthogonal complement satisfies

\[
 \boxed{A_j|_{L_j^\perp}\succeq\Gamma_jI.}
 \tag{T-15602.8}
\]

It is sufficient to certify this by the finite symbol/visible Schur packet of
`L-15604`.

### C. Directed assembly radius

All represented form data differ from the exact operator by a rigorously
accounted lower-floor loss at most `delta_j`.

### D. Cofinal rates

\[
 \alpha_j\longrightarrow0,
 \qquad
 \frac{\alpha_j}{t_j}\longrightarrow0,
 \qquad
 \frac{\beta_j^2}{t_j}\longrightarrow0,
 \qquad
 \delta_j\longrightarrow0.
 \tag{T-15602.9}
\]

Then the Riemann hypothesis is true.

## Capacity inequality

Let

\[
 d_j=\dim L_j.
\]

By (T-15602.6), every direction in `L_j` lies below `t_j`.  By
(T-15602.8), no direction in `L_j^perp` lies below `Gamma_j`.  Therefore

\[
 \boxed{
 N_{A_j}(t_j)=N_{A_j}(\Gamma_j)=d_j.}
 \tag{T-15602.10}
\]

Thus the requested scalar inequality is realized by the exact saturated
certificates

\[
 \boxed{
 D(a_j,t_j,\Gamma_j)
 =C(a_j,\alpha_j,\beta_j)
 =d_j.}
 \tag{T-15602.11}
\]

A previously available loose symbol cap may be larger; T-15602 replaces it by
the sharp certified count `d_j` rather than attempting to prove that the loose
integer is intrinsically small.

## Lower floor

Apply `L-15602` at level `j`.  Before the assembly radius, it gives

\[
 \inf\sigma(A_j)
 \ge
 -\frac{3t_j\alpha_j+\alpha_j^2+\beta_j^2}
        {t_j-\alpha_j}.
 \tag{T-15602.12}
\]

Hence the rigorous lower floor is

\[
 \boxed{
 F_j=
 -\frac{3t_j\alpha_j+\alpha_j^2+\beta_j^2}
        {t_j-\alpha_j}
 -\delta_j.}
 \tag{T-15602.13}
\]

The rate assumptions imply

\[
 F_j\longrightarrow0^-.
 \tag{T-15602.14}
\]

Indeed,

\[
 \frac{3t_j\alpha_j}{t_j-\alpha_j}
 =\frac{3\alpha_j}{1-\alpha_j/t_j}\to0,
\]

\[
 \frac{\alpha_j^2}{t_j-\alpha_j}
 =\frac{\alpha_j(\alpha_j/t_j)}{1-\alpha_j/t_j}\to0,
\]

and

\[
 \frac{\beta_j^2}{t_j-\alpha_j}
 =\frac{\beta_j^2/t_j}{1-\alpha_j/t_j}\to0.
\]

The cofinal lower-envelope theorem `T-14302` now gives RH.  QED.

## Important weakening

The positive complement threshold `t_j` need not be bounded away from zero.  It
may tend to zero provided

\[
 \alpha_j=o(t_j),
 \qquad
 \beta_j=o(\sqrt{t_j}).
 \tag{T-15602.15}
\]

This is useful when the whole localized low cluster collapses toward zero.

Likewise, packet ranks may grow arbitrarily and low eigenvalues may be multiple.
No ground-state vector, simple eigenvalue, parity, determinant convergence, or
principal angle is required.

## Sufficient finite implementation of B

At each level choose a complete symbol-selected packet `U_j` and form

\[
 W_j=L_j+U_j,
 \qquad
 V_j=W_j\cap L_j^\perp,
 \qquad
 E_j=W_j^\perp.
\]

It is enough to prove

\[
 A_j|_{E_j}\succeq\Gamma_jI+h_jM_j
\]

and the finite robust Schur inequality

\[
 Y_j-\Gamma_jI
 -h_j^{-1}R_j^*M_j^{-1}R_j\succeq0
\]

on `V_j`.  This is exactly `L-15604`.  Certified-zero evaluation splitting may
first move the radical-like near-kernel of `V_j` into `L_j`, leaving only a
finite evaluation-visible block.

## What remains unproved in the zeta application

T-15602 is a complete implication theorem.  The unresolved analytic statement
is the existence of a cofinal sequence satisfying B and the uniform growing-rank
rates in A and D.

In particular, neither of the following is sufficient:

- fixed-rank radical packets with support chosen after the rank;
- a symbol rank cap having the same order of growth as a source-packet count.

The first lacks uniform growing-rank control.  The second does not exclude an
additional low direction.  A production proof must supply the exact finite
saturation certificate at every cofinal level and one symbolic rate envelope.

## Proof boundary

- The theorem is conditional and does not assert that its hypotheses have been
  established for the Riemann zeta Weil operator.
- Source normalization, symbol normalization, form domains, and directed
  assembly remain external gates.
- No proof of RH is claimed without the cofinal saturation/rate theorem.
