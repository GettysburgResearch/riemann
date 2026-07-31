# L-15610 — Exact terminal-prime Hankel matrix for the endpoint-visible block

Claim ID: `L-15610`  
Title: Endpoint-visible Suzuki packets reduce exactly to a centered terminal-prime Hankel matrix after pole cancellation  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-e`  
Created: 2026-07-31  
Dependencies: Suzuki equation (4.5); repository `L-15401`, `L-15404`; elementary matrix polarization  
Scope: the plunge-sized endpoint-visible block in `L-15306/L-15307`  
Related counterexample candidates: none

## 1. Profile packet

Fix `R>0` and profiles

\[
 \phi_1,\ldots,\phi_m\in C_c^\infty(0,R).
\]

For `a>2R`, let `w_(a,j)` be the odd endpoint packet whose positive half is

\[
 f_{a,j}(x)=\sqrt a\,\phi_j(a(1-x))
 \quad (1-R/a<x<1).
\]

For `c in C^m`, write

\[
 \phi_c=\sum_jc_j\phi_j,
 \qquad
 w_{a,c}=\sum_jc_jw_{a,j}.
\]

Define the Laplace vectors

\[
 v^-_j=\int_0^R e^{-r/2}\phi_j(r)\,dr,
 \qquad
 v^+_j=\int_0^R e^{r/2}\phi_j(r)\,dr.
 \tag{1}
\]

Extend every profile by zero outside `(0,R)` and define the Hermitian Hankel
matrix

\[
 C(u)_{ij}
 =\int_{\mathbb R}\phi_i(u-r)\overline{\phi_j(r)}\,dr,
 \qquad 0\le u\le2R.
 \tag{2}
\]

Indeed, the substitution `r -> u-r` gives `C(u)^*=C(u)`.

## 2. Exact terminal and polar matrices

Put

\[
 u_n=2a-\log n,
 \qquad c_n=\frac{\Lambda(n)}{\sqrt n}.
\]

Polarization of the endpoint-overlap calculation in `L-15404` gives the exact
terminal-prime matrix

\[
 P_a^{\rm term}
 =2\sum_{0\le u_n\le2R}c_nC(u_n).
 \tag{3}
\]

The odd polar channel is exactly

\[
 P_a^{\rm pol}
 =-2\bigl(e^{a/2}v^- -e^{-a/2}v^+\bigr)
       \bigl(e^{a/2}v^- -e^{-a/2}v^+\bigr)^*.
 \tag{4}
\]

The convolution identity is matrix-valued:

\[
 \boxed{
 \int_0^{2R}e^{-u/2}C(u)\,du=v^-(v^-)^*.}
 \tag{5}
\]

Define the centered terminal-prime Hankel matrix

\[
 \boxed{
 E_a
 =2\sum_{0\le u_n\le2R}c_nC(u_n)
  -2e^a\int_0^{2R}e^{-u/2}C(u)\,du.}
 \tag{6}
\]

Then the exponentially large pole terms cancel **exactly**:

\[
 \boxed{
 P_a^{\rm term}+P_a^{\rm pol}
 =E_a
  +2\bigl(v^-(v^+)^*+v^+(v^-)^*\bigr)
  -2e^{-a}v^+(v^+)^*.}
 \tag{7}
\]

No asymptotic prime number theorem is used in (7).

### Proof

Equations (3) and (4) are the polarized forms of `L-15404.8` and
`L-15404.11`. Fubini gives

\[
\begin{aligned}
 \int e^{-u/2}C(u)_{ij}\,du
 &=\iint e^{-(r+s)/2}\phi_i(s)\overline{\phi_j(r)}\,drds\\
 &=v_i^-\overline{v_j^-},
\end{aligned}
\]

which proves (5). Expanding (4), inserting (5), and collecting terms proves
(7). QED.

## 3. The complete visible block

Let `A_a^loc` denote every remaining exact contribution on the declared profile
packet:

- the continuous jump and local potential;
- the fixed prime-power prefix `log n<=R`;
- same-end endpoint correlations;
- directed assembly corrections already charged inside the finite block.

Then the exact endpoint-visible matrix is

\[
 \boxed{
 B_{V,a}=A_a^{loc}+E_a
 +2(v^-(v^+)^*+v^+(v^-)^*)
 -2e^{-a}v^+(v^+)^*.}
 \tag{8}
\]

Thus all cofinal arithmetic not already finite/local is concentrated in `E_a`.
The apparent `e^a` polar instability is absent from the true matrix.

## 4. Exact scalar norm gate

Let `G_V>0` be the profile metric. If directed arithmetic certifies

\[
 -\theta_aG_V\preceq E_a\preceq\theta_aG_V,
 \tag{9}
\]

and

\[
 A_a^{loc}
 +2(v^-(v^+)^*+v^+(v^-)^*)
 -2e^{-a}v^+(v^+)^*
 \succeq \sigma_a^2G_V,
 \tag{10}
\]

then

\[
 \boxed{B_{V,a}\succeq(\sigma_a^2-\theta_a)G_V.}
 \tag{11}
\]

A proof-facing sufficient certificate for (9) is

\[
 \boxed{
 \theta_a^2G_V-E_aG_V^{-1}E_a\succeq0.}
 \tag{12}
\]

After the ambient complement `C>=hM` and visible--ambient cross bound

\[
 Z^*M^{-1}Z\preceq\zeta_a^2G_V,
\]

`L-15307` gives the corrected visible margin

\[
 \boxed{
 \beta_a
 =\sigma_a^2-\theta_a-\frac{\zeta_a^2}{h_a}.}
 \tag{13}
\]

The one-radius version is

\[
 \beta_a=\sigma_a^2-\theta_a-\omega_a-\omega_a^2/h_a.
 \tag{14}
\]

## 5. Laplace-transform meaning

For a scalar profile `phi`, let `C_phi=phi*phi^sharp` denote the corresponding
Hankel convolution. The scalar contraction of (6) is

\[
 c^*E_ac
 =2\left[
 \sum_{0\le2a-\log n\le2R}
 \frac{\Lambda(n)}{\sqrt n}C_{\phi_c}(2a-\log n)
 -e^a\int_0^{2R}e^{-u/2}C_{\phi_c}(u)\,du
 \right].
 \tag{15}
\]

Its translated Laplace transform is the pole-subtracted logarithmic derivative
of zeta multiplied by the profile transform. The zeta pole is removed by the
second term; the remaining nontrivial poles are shifted zeta zeros. This is the
matrix-valued terminal-prime statistic isolated independently in PR #165.

## 6. Gap audit

- Equation (7) is exact finite algebra, subject to Suzuki normalization review.
- The prime number theorem proves only `e^{-a}E_a -> 0` for each fixed packet;
  it does **not** prove `||E_a||=o(1)`.
- A phase-blind absolute prime bound destroys the cancellation in (7).
- A fixed finite certified-real-zero frame cannot bound `E_a` cofinally if an
  off-line zero exists; see `R-16901`.
- No cofinal bound for `theta_a` is asserted here.
- RH is not claimed.