# L-17002 — Explicit three-block cofinal epsilon envelope

Claim ID: `L-17002`  
Title: Radical, visible, and ambient blocks admit one closed cofinal error formula  
Status: `PROPOSED`  
Authoring agent: `gpt56-02-n`  
Created: 2026-07-31  
Dependencies: `L-14308`; `L-17001`; elementary Schur and Young inequalities  
Scope: the corrected low packet `U=R+V` coupled to a positive complement  
Related counterexample candidates: none

## Statement

Let

\[
 A=
 \begin{pmatrix}
 B_R&X^*&Y^*\\
 X&B_V&Z^*\\
 Y&Z&D
 \end{pmatrix}
 \tag{L-17002.1}
\]

be a Hermitian operator or finite form on the orthogonal decomposition

\[
 \mathcal H=R\oplus V\oplus E.
\]

Interpret `R` as the repaired radical-like packet, `V` as the
certified-zero-visible packet, and `E` as the complete ambient complement.
Assume the exact bounds

\[
 D\succeq\gamma I_E,
 \qquad \gamma>0,
 \tag{L-17002.2}
\]

\[
 B_R\succeq-r I_R,
 \qquad
 B_V\succeq v I_V,
 \tag{L-17002.3}
\]

and

\[
 \|X\|\le x,
 \qquad
 \|Y\|\le y,
 \qquad
 \|Z\|\le z,
 \tag{L-17002.4}
\]

with nonnegative rational or directed quantities `r,x,y,z` and real `v`.
Define

\[
 \alpha=r+\frac{y^2}{\gamma},
 \qquad
 \nu=v-\frac{z^2}{\gamma},
 \qquad
 \chi=x+\frac{yz}{\gamma}.
 \tag{L-17002.5}
\]

If

\[
 \boxed{\nu>0,}
 \tag{L-17002.6}
\]

then the fully Schur-corrected low block satisfies

\[
 \boxed{
 \lambda_{\min}
 \left[
 \begin{pmatrix}B_R&X^*\\X&B_V\end{pmatrix}
 -\begin{pmatrix}Y^*\\Z^*\end{pmatrix}
  D^{-1}
  \begin{pmatrix}Y&Z\end{pmatrix}
 \right]
 \ge-\varepsilon,}
 \tag{L-17002.7}
\]

where

\[
 \boxed{
 \varepsilon
 =r+\frac{y^2}{\gamma}
  +\frac{\left(x+yz/\gamma\right)^2}
         {v-z^2/\gamma}.}
 \tag{L-17002.8}
\]

Consequently the complete operator obeys

\[
 \boxed{A\succeq-\varepsilon I.}
 \tag{L-17002.9}
\]

A slightly sharper scalar lower endpoint is

\[
 m_{\rm sharp}
 =\frac{\nu-\alpha-
 \sqrt{(\nu+\alpha)^2+4\chi^2}}2,
 \tag{L-17002.10}
\]

but (L-17002.8) avoids a square root and is better suited to exact rational
certification.

## Proof

Schur-correct the positive ambient complement. The resulting block on `R+V` is

\[
 S=
 \begin{pmatrix}
 B_R-Y^*D^{-1}Y&X^*-Y^*D^{-1}Z\\
 X-Z^*D^{-1}Y&B_V-Z^*D^{-1}Z
 \end{pmatrix}.
 \tag{L-17002.11}
\]

From `D>=gamma I`,

\[
 B_R-Y^*D^{-1}Y\succeq-\alpha I_R,
 \tag{L-17002.12}
\]

\[
 B_V-Z^*D^{-1}Z\succeq\nu I_V,
 \tag{L-17002.13}
\]

and

\[
 \|X-Z^*D^{-1}Y\|\le\chi.
 \tag{L-17002.14}
\]

For `r_0 in R`, `v_0 in V`, Young's inequality gives

\[
 2\chi\|r_0\|\|v_0\|
 \le\frac{\chi^2}{\nu}\|r_0\|^2
    +\nu\|v_0\|^2.
 \tag{L-17002.15}
\]

Therefore

\[
 \langle S(r_0,v_0),(r_0,v_0)\rangle
 \ge-\left(\alpha+\frac{\chi^2}{\nu}\right)\|r_0\|^2
 \ge-\varepsilon(\|r_0\|^2+\|v_0\|^2),
\]

which proves (L-17002.7). Equation (L-17001.10) then proves the complete floor
(L-17002.9). The sharp endpoint (L-17002.10) is the smaller eigenvalue of the
scalar comparison matrix

\[
 \begin{pmatrix}-\alpha&-\chi\\-\chi&\nu\end{pmatrix}.
\]

QED.

## Cofinal consequence

For a support sequence, let the six proof quantities depend on `j`. If

\[
 \gamma_j>0,
 \qquad
 \nu_j=v_j-z_j^2/\gamma_j>0
 \tag{L-17002.16}
\]

cofinally and

\[
 \boxed{
 r_j+\frac{y_j^2}{\gamma_j}
 +\frac{(x_j+y_jz_j/\gamma_j)^2}{\nu_j}
 \longrightarrow0,}
 \tag{L-17002.17}
\]

then

\[
 F_j\ge-\varepsilon_j,
 \qquad
 \varepsilon_j\to0.
 \tag{L-17002.18}
\]

This is the requested symbolic cofinal estimate in its complete three-block
form.

## Interpretation of the terms

- `r_j`: the complete radical-block error;
- `y_j^2/gamma_j`: the squared radical-to-ambient Schur loss;
- `nu_j`: the visible block after its own ambient Schur loss;
- `x_j+y_jz_j/gamma_j`: the corrected radical-visible cross map;
- the last quotient: the only remaining finite low-block penalty.

The Gaussian global-radical tail results on PR #152 address `r_j`, `x_j`, and
`y_j` once a proof-grade near-kernel packet is fixed. PRs #155/#168 address
`gamma_j` and the complement construction. The zeta-specific load-bearing
quantity is the corrected visible floor `nu_j` together with the relative
cross condition in (L-17002.17).

## Useful weak-visible regime

A uniform positive visible floor is not required. It is sufficient that

\[
 \nu_j>0,
 \qquad
 \frac{(x_j+y_jz_j/\gamma_j)^2}{\nu_j}\to0.
 \tag{L-17002.19}
\]

Thus a visible floor may itself tend rapidly to zero, provided the radical
cross map vanishes faster in the squared Schur scale. This is important because
the localized Weil ground and repaired radical levels may be
superexponentially small.

## Gap audit

- The estimate is sufficient, not necessary.
- Every norm must use the same declared packet and complement metrics.
- `v_j` must be a lower bound for the complete visible block before ambient
  correction; a zero-evaluation singular value alone is not a Weil-form floor.
- The denominator `nu_j` must be strictly positive. Touching zero is unresolved.
- Small radical tails do not imply (L-17002.17) unless the visible denominator
  and all cross maps are controlled in compatible norms.
- No production zeta sequence satisfying these rates is supplied here.
