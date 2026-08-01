# R-18502 — The two-sided evaluation threshold is not necessary

Claim ID: `R-18502`  
Title: The inequality `epsilon < B+beta < Sigma` can fail on a strictly positive full packet  
Status: `PROVED SCOPE REFUTATION`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependencies: `L-18508`  
Scope: the requested scalar threshold after the full-complement theorem  
Related candidates: none

## 1. Purpose

After `L-18507`, the actual complement

\[
 W=R^{\perp_G}\cap U
\]

is framed directly by selected critical-line evaluations. The earlier counted
transfer asked for a threshold

\[
 \epsilon<B+\beta<\Sigma.                                \tag{R-18502.1}
\]

This condition is sufficient for count saturation, but it is not necessary for
a positive visible Schur floor or for a positive complete finite form.

## 2. Exact positive family

For every integer `j>=2`, let

\[
 U=\mathbb R^2,
 \qquad G=I_2,
 \qquad R=\operatorname{span}\{e_1\},
 \qquad W=\operatorname{span}\{e_2\}.                    \tag{R-18502.2}
\]

Put

\[
 K_j=
 \begin{pmatrix}
  j^{-1}&0\\
  0&j^{-2}
 \end{pmatrix},
 \qquad B_j=0,
 \qquad S_j=K_j.                                         \tag{R-18502.3}
\]

Then

\[
 K_j|_R\preceq\epsilon_jG|_R,
 \qquad \epsilon_j=\frac1j,                              \tag{R-18502.4}
\]

and the exact full-complement frame floor is

\[
 \Sigma_j=\frac1{j^2}>0.                                 \tag{R-18502.5}
\]

Thus

\[
 \epsilon_j>\Sigma_j.                                    \tag{R-18502.6}
\]

There is no `beta_j>0` satisfying

\[
 \epsilon_j<B_j+\beta_j<\Sigma_j.                        \tag{R-18502.7}
\]

Nevertheless the complete form is strictly positive:

\[
 S_j\succ0,                                               \tag{R-18502.8}
\]

and its visible restriction has the exact positive floor

\[
 \boxed{
 S_j|_W\succeq\frac1{j^2}G|_W.}                          \tag{R-18502.9}
\]

The finite ground value is `j^-2>0`.

## 3. Consequence

The failure of (R-18502.1) in this family is benign. It says only that the
radical evaluation endpoint lies above the visible endpoint, so no single
threshold separates the two restrictions of `K_j`. It does **not** say that the
visible block or the full form is negative.

Once `W` is known explicitly, `L-18508` gives the direct restriction

\[
 S|_W\succeq(\Sigma-B)G|_W.                              \tag{R-18502.10}
\]

Therefore the necessary proof-facing visible condition is

\[
 \boxed{B<\Sigma,}                                       \tag{R-18502.11}
\]

not the stronger two-sided count threshold. Radical compression and cross maps
must be controlled by their own Schur/tail estimates.

## 4. What remains load bearing

The scope correction does not prove `B<Sigma` cofinally. Under a hypothetical
off-line zero, the complete signed residual can overwhelm every selected-real-
zero frame on a complete low hierarchy. Thus

\[
 \Sigma-B>0                                               \tag{R-18502.12}
\]

is still an RH-bearing arithmetic statement.

The correction is that `epsilon` should not be inserted into that visible-block
statement merely to manufacture a generalized-eigenvalue count which is no
longer needed.

## 5. Proof boundary

- The counterexample and all matrix inequalities are exact.
- It refutes only the **necessity** of the requested threshold.
- If a later argument specifically needs count saturation or an automatic
  principal angle, (R-18502.1) remains a valid sufficient gate.
- The direct three-block route should instead use `L-18508.4` and the separate
  radical-row bounds of `L-15306/T-15302`.
