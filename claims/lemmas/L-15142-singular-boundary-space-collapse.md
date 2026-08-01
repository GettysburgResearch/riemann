# L-15142 — The declared singular-boundary Hilbert subspace equals the full analytic space

Claim ID: `L-15142`  
Status: **PROVED FROM THE MANUSCRIPT'S DEFINITIONS**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: Shimizu v6 Definitions 2.4, 4.65, 4.88, 4.105 and the displayed equivalent description of `G_R`  
Scope: remove the abstract one-sided projection from the executable chain

## 1. Definitions used

The analytic Hilbert space is a weighted `L^2` space on the half-line,

\[
 H_{\alpha,+}=L^2((0,\infty),\rho_\alpha(x)\,dx),
 \qquad \alpha>\frac12,
 \tag{L-15142.1}
\]

with admissible core

\[
 \mathcal C_R=C_c^\infty([0,\infty)).
 \tag{L-15142.2}
\]

The manuscript gives the equivalent description

\[
 \boxed{
 G_R=\{f\in T_R:\gamma_R^{\rm reg}f=0\}.}
 \tag{L-15142.3}
\]

It then defines

\[
 Q_R^{\rm res}
 =\overline{\operatorname{span}G_R}^{\|\cdot\|_{q_R}}
 \tag{L-15142.4}
\]

and

\[
 H_R^{\rm res}
 =\overline{Q_R^{\rm res}}^{\|\cdot\|_{H_{\alpha,+}}}.
 \tag{L-15142.5}
\]

Finally, `Pi_R^+` is the orthogonal projection of `H_(alpha,+)` onto
`H_R^res`.

## 2. Dense interior core

Every function

\[
 f\in C_c^\infty((0,\infty))
 \tag{L-15142.6}
\]

vanishes on a neighborhood of the endpoint.  Hence its regular boundary trace
is zero.  Such a function lies in the trace graph `T_R`, so (L-15142.3) gives

\[
 C_c^\infty((0,\infty))\subset G_R.
 \tag{L-15142.7}
\]

The left side is dense in the weighted `L^2` space (L-15142.1), because the
weight is positive and locally integrable and ordinary interior compactly
supported smooth approximation applies.

## 3. Collapse theorem

Since

\[
 G_R\subset Q_R^{\rm res}\subset H_R^{\rm res}
 \tag{L-15142.8}
\]

and `G_R` contains the dense class (L-15142.7), the closed subspace
`H_R^res` contains a dense subset of `H_(alpha,+)`. Therefore

\[
 \boxed{H_R^{\rm res}=H_{\alpha,+}.}
 \tag{L-15142.9}
\]

Consequently

\[
 \boxed{K_R^+=H_{\alpha,+},\qquad \Pi_R^+=I.}
 \tag{L-15142.10}
\]

After the analytic embedding into the ambient direct sum, the ambient
projection is simply

\[
 \boxed{\Pi_R=J_{\rm an}J_{\rm an}^*,}
 \tag{L-15142.11}
\]

i.e. the canonical projection onto the analytic summand.

## 4. Consequences for the executable producer

1. No spectral computation is needed to determine the one-sided projector.
2. A finite source package need only bind the coordinate adapter identifying
   the analytic block inside the finite ambient `X` coordinates.
3. The compact-resolvent operator denoted `L_R^res` is a restriction to the
   full analytic Hilbert space at the Hilbert-space level; any additional
   boundary information resides in its form/operator domain, not in a proper
   closed Hilbert subspace.
4. This result does not determine the finite contour probes, `LCI`, seam
   involution, or scalar coefficient, so it does not by itself emit a quartic
   row.

## 5. Proof boundary

The conclusion uses the manuscript's displayed equivalence (L-15142.3). If the
author intended `G_R` to exclude zero singular trace or to impose an additional
non-closed support condition, that condition must be stated; it is not present
in the quoted set equality, and excluding the zero vector would destroy
linearity.
