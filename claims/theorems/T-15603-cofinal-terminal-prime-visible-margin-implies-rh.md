# T-15603 — A cofinal terminal-prime visible margin implies RH

Claim ID: `T-15603`  
Title: Directed control of the centered terminal-prime Hankel block completes the three-block cofinal floor  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-e`  
Created: 2026-07-31  
Dependencies: `L-15610`, `L-15611`; `L-15306`--`L-15308`; `T-14302`  
Scope: final conditional composition of the positive localized-Weil route  
Related counterexample candidates: none

## Statement

Let `a_j -> infinity`. At level `j`, decompose the exact localized Weil form as

\[
 \mathcal H_j=
 \begin{pmatrix}
 B_{R,j}&X_j^*&Y_j^*\\
 X_j&B_{V,j}&Z_j^*\\
 Y_j&Z_j&C_j
 \end{pmatrix}
 \tag{1}
\]

on the orthogonal sum of:

1. an exact repaired radical-like packet `R_j` with metric `G_(R,j)`;
2. the plunge-sized endpoint-visible packet `V_j` with metric `G_(V,j)`;
3. the complete ambient complement with metric `M_j`.

Assume the following directed inequalities.

### Radical block

\[
 B_{R,j}\succeq-e_jG_{R,j},
 \qquad e_j\ge0.
 \tag{2}
\]

### Ambient complement

\[
 C_j\succeq h_jM_j,
 \qquad h_j>0.
 \tag{3}
\]

### Endpoint-visible decomposition

The exact identity of `L-15610` holds:

\[
 B_{V,j}=A_j^{loc}+E_j+P_j^{fin},
 \tag{4}
\]

where `P_j^fin` is the explicit finite polar cross term after exact pole
cancellation. Suppose

\[
 A_j^{loc}+P_j^{fin}\succeq\sigma_j^2G_{V,j},
 \tag{5}
\]

\[
 -\theta_jG_{V,j}\preceq E_j\preceq\theta_jG_{V,j},
 \tag{6}
\]

and

\[
 Z_j^*M_j^{-1}Z_j\preceq\zeta_j^2G_{V,j}.
 \tag{7}
\]

Put

\[
 \boxed{
 \beta_j=\sigma_j^2-\theta_j-\frac{\zeta_j^2}{h_j}.}
 \tag{8}
\]

Assume `beta_j>0`.

### Corrected radical cross loss

Define

\[
 \widetilde X_j=X_j-h_j^{-1}Z_j^*M_j^{-1}Y_j
 \tag{9}
\]

and suppose

\[
 h_j^{-1}Y_j^*M_j^{-1}Y_j
 +\beta_j^{-1}\widetilde X_j^*G_{V,j}^{-1}\widetilde X_j
 \preceq\kappa_jG_{R,j}.
 \tag{10}
\]

Finally, let `delta_j>=0` be a complete directed assembly/form radius.

Then

\[
 \boxed{
 \inf\sigma(A_{a_j})
 \ge-(e_j+\kappa_j+\delta_j).}
 \tag{11}
\]

If

\[
 e_j+\kappa_j+\delta_j\longrightarrow0,
 \tag{12}
\]

then the Riemann hypothesis is true.

## Proof

Equations (3) and (7), followed by completion of squares in the ambient metric,
give

\[
 B_{V,j}-h_j^{-1}Z_j^*M_j^{-1}Z_j
 \succeq\beta_jG_{V,j}.
\]

The triangular three-block factorization of `L-15306`, with (2) and (10), gives

\[
 \mathcal H_j\succeq-(e_j+\kappa_j)
 \operatorname{diag}(G_{R,j},0,0).
\]

The directed assembly radius subtracts `delta_j`, proving (11). The cofinal
lower-envelope theorem `T-14302` applies to (12) and gives RH. QED.

## One-radius production form

If a single source-bound residual radius `omega_j` certifies both the visible
diagonal and visible--ambient cross as in `L-15307`, one may use

\[
 \boxed{
 \beta_j
 =\sigma_j^2-\theta_j-\omega_j-\frac{\omega_j^2}{h_j}.}
 \tag{13}
\]

This is the smallest current scalar target for the plunge-sized visible block.

## Alternative terminal-prime certificates

Any of the following may supply (6):

1. exact directed entry balls plus the LMI
   \[
   \theta_j^2G_{V,j}-E_jG_{V,j}^{-1}E_j\succeq0;
   \]
2. a projected weighted-deficit operator upper bound;
3. a phase-complete pole-free terminal-window norm bound;
4. a finite profile basis with exact rational LDL and a separate analytic tail
   moat.

A single favorable scalar phase does not imply (6).

## Gap audit

- The theorem completes the implication once all hypotheses hold; it does not
  prove the zeta-specific bound (6).
- `L-15611` shows that a uniform bound for a packet containing the zero-free
  universal window already implies RH. The terminal-prime gate is therefore the
  substantive arithmetic theorem, not a technical estimate.
- Fixed finite zero frames and phase-blind PNT errors are insufficient.
- No production sequence satisfying (5)--(12) exists.
- RH is not claimed proved.