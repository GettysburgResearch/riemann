# L-19701 — Off-line Xi-cardinal negativity survives the complete Schur correction

Claim ID: `L-19701`  
Title: A conjugate off-line zero pair gives a fixed negative selected-real-zero-kernel direction after every positive-complement elimination  
Status: `PROPOSED — COMPLETE ABSTRACT PROOF; XI-CARDINAL DOMAIN/CAPTURE INHERITED`  
Authoring agent: `gpt56-03-o`  
Created: 2026-07-31  
Dependencies: the centered Weil zero-sum formula; the Xi-cardinal construction of `L-14321/T-14307`; finite-section selected-zero repair of `T-14306`; elementary Schur-complement algebra  
Scope: the final kernel block in Issue #197  
Related counterexample candidates: none

## 1. Finite Schur monotonicity

Let a finite Hermitian form be written on `K direct-sum E` as

\[
 \mathcal H=
 \begin{pmatrix}
 B_K&Z^*\\
 Z&C
 \end{pmatrix},
 \qquad C\succ0.
 \tag{L-19701.1}
\]

Its exact Schur-corrected kernel form is

\[
 \boxed{S_K=B_K-Z^*C^{-1}Z.}
 \tag{L-19701.2}
\]

For every `x in K`,

\[
 \boxed{
 \langle S_Kx,x\rangle
 =\langle B_Kx,x\rangle
 -\|C^{-1/2}Zx\|^2
 \le\langle B_Kx,x\rangle.}
 \tag{L-19701.3}
\]

Equivalently,

\[
 \langle S_Kx,x\rangle
 =\inf_{e\in E}
 \langle\mathcal H(x,e),(x,e)\rangle.
 \tag{L-19701.4}
\]

Thus eliminating a positive complement can never repair a negative kernel
quadratic. It either leaves the value unchanged or lowers it further.

## 2. Exact off-line cardinal direction

Write

\[
 \Xi(z)=\xi\!\left(\frac12+iz\right)
\]

and use the centered polarized Weil normalization

\[
 Q_W(f,g)=
 \sum_{\omega:\Xi(\omega)=0}
 m_\omega\widehat f(\omega)
 \overline{\widehat g(\overline\omega)}.
 \tag{L-19701.5}
\]

Assume RH is false and let `rho` be a nonreal centered zero of multiplicity
`m>=1`. Put

\[
 A_\rho=
 \lim_{z\to\rho}\frac{\Xi(z)}{(z-\rho)^m}\ne0
 \tag{L-19701.6}
\]

and define the entire cardinal transform

\[
 L_\rho(z)=
 \frac{\Xi(z)}{A_\rho(z-\rho)^m}.
 \tag{L-19701.7}
\]

Let `ell_rho` be its inverse Fourier representative in the declared Hardy/form
domain. Then

\[
 \widehat\ell_\rho(\rho)=1,
 \qquad
 \widehat\ell_\rho(\omega)=0
 \quad(\omega\ne\rho,\ \Xi(\omega)=0).
 \tag{L-19701.8}
\]

Define

\[
 \boxed{h_\rho=\ell_\rho-\ell_{\overline\rho}.}
 \tag{L-19701.9}
\]

It vanishes at every real centered zeta zero and at every zero except the
conjugate pair:

\[
 \widehat h_\rho(\rho)=1,
 \qquad
 \widehat h_\rho(\overline\rho)=-1.
 \tag{L-19701.10}
\]

Therefore

\[
 \boxed{Q_W(h_\rho,h_\rho)=-2m.}
 \tag{L-19701.11}
\]

This value is independent of how many critical-line zeros have already been
selected.

## 3. Exact finite-support selected-zero repair

Let `Z_j` be any finite set of certified real centered zeros, let `V_j` denote
evaluation on `Z_j`, and let `P_j` be localization to the retained support.
Suppose the exact supported cardinal synthesis of `T-14306` is available:

\[
 \widetilde C_j
 =P_jC_{Z_j}(V_jP_jC_{Z_j})^{-1},
 \qquad
 V_j\widetilde C_j=I.
 \tag{L-19701.12}
\]

Define

\[
 \boxed{
 k_{\rho,j}
 =P_jh_\rho-\widetilde C_jV_jP_jh_\rho.}
 \tag{L-19701.13}
\]

Then

\[
 \boxed{V_jk_{\rho,j}=0}
 \tag{L-19701.14}
\]

exactly. Since `V_jh_rho=0`,

\[
 V_jP_jh_\rho=-V_j(I-P_j)h_\rho.
 \tag{L-19701.15}
\]

For each fixed finite `Z_j`, the Xi-cardinal tail estimate and the Neumann bound
for (L-19701.12) imply

\[
 k_{\rho,j}\longrightarrow h_\rho
 \tag{L-19701.16}
\]

as support tends to infinity, in every declared topology that controls both the
Weil form and the denominator metric.

A growing hierarchy needs the following explicit capture condition.

### Off-line-cardinal capture

A finite selected-real-zero kernel `K_j subset ker V_j` captures the off-line
cardinal sequence if there exist `u_{rho,j} in K_j` such that

\[
 \|u_{\rho,j}-k_{\rho,j}\|_{\mathfrak q,G}\longrightarrow0.
 \tag{L-19701.17}
\]

It is enough that the packet contain `k_(rho,j)` exactly. Ordinary `L2` density
without form and metric control is insufficient.

## 4. Fixed negative gap after Schur elimination

Let the exact finite block on `K_j direct-sum E_j` be

\[
 \mathcal H_j=
 \begin{pmatrix}
 B_{K,j}&Z_j^*\\
 Z_j&C_j
 \end{pmatrix},
 \qquad C_j\succ0,
 \tag{L-19701.18}
\]

and define

\[
 S_{K,j}=B_{K,j}-Z_j^*C_j^{-1}Z_j.
 \tag{L-19701.19}
\]

Assume the capture condition (L-19701.17), and write

\[
 N_\rho^2=\|h_\rho\|_{G_\infty}^2>0.
 \tag{L-19701.20}
\]

Form/metric convergence gives

\[
 Q_W(u_{\rho,j},u_{\rho,j})\longrightarrow-2m,
 \qquad
 \|u_{\rho,j}\|_{G_j}^2\longrightarrow N_\rho^2.
 \tag{L-19701.21}
\]

By (L-19701.3),

\[
 \langle S_{K,j}u_{\rho,j},u_{\rho,j}\rangle
 \le Q_W(u_{\rho,j},u_{\rho,j}).
 \tag{L-19701.22}
\]

Consequently

\[
 \boxed{
 \limsup_{j\to\infty}
 \lambda_{\min}(S_{K,j},G_{K,j})
 \le-\frac{2m}{N_\rho^2}<0.}
 \tag{L-19701.23}
\]

More conservatively, every

\[
 0<\delta_\rho<\frac{2m}{N_\rho^2}
 \tag{L-19701.24}
\]

satisfies

\[
 \boxed{
 \lambda_{\min}(S_{K,j},G_{K,j})
 \le-\delta_\rho}
 \tag{L-19701.25}
\]

for all sufficiently large `j`.

False RH therefore produces a fixed negative gap. It does not merely prevent a
particular rate estimate.

## 5. Converse under RH

Assume RH. Every centered zero is real, and every summand in (L-19701.5) is
nonnegative:

\[
 Q_W(f,f)=
 \sum_{\gamma\in\mathbb R}m_\gamma
 |\widehat f(\gamma)|^2\ge0.
 \tag{L-19701.26}
\]

Hence every finite compression of the complete Weil form is positive
semidefinite. If `C_j` is positive definite, its Schur complement is positive
semidefinite:

\[
 \boxed{S_{K,j}\succeq0.}
 \tag{L-19701.27}
\]

Thus RH gives the requested lower floor with `epsilon_j=0`.

## 6. Complete radical-synthesis sufficient condition

The exact dichotomy above does not prevent a noncircular proof, but it shows
what such a proof must establish.

Let

\[
 J_j:\mathbb C^{d_j}\to K_j
 \tag{L-19701.28}
\]

be a basis map for the **complete** selected-real-zero kernel, including the old
repaired radicals and every new zero-invisible augmentation direction. Suppose
there is a map

\[
 R_j:\mathbb C^{d_j}\to\mathcal R_W
 \tag{L-19701.29}
\]

into the exact global Weil radical, and put

\[
 E_j=J_j-R_j.
 \tag{L-19701.30}
\]

Global radicality gives

\[
 Q_W(J_ja,J_ja)=Q_W(E_ja,E_ja).
 \tag{L-19701.31}
\]

If one proves uniformly that

\[
 \boxed{
 |Q_W(E_ja,E_ja)|
 +\|C_j^{-1/2}Z_jJ_ja\|^2
 \le
 \eta_j\|J_ja\|_{G_j}^2
 \quad\text{for every }a,}
 \tag{L-19701.32}
\]

with

\[
 \eta_j\longrightarrow0,
 \tag{L-19701.33}
\]

then

\[
 \boxed{S_{K,j}\succeq-\eta_jG_{K,j}.}
 \tag{L-19701.34}
\]

This is the exact complete-kernel synthesis target. It cannot be checked only
on the old radical rows; it must include every direction added by ambient
deficit capture.

Under false RH, (L-19701.32) is impossible on a capturing hierarchy because of
(L-19701.23).

## 7. What does not prove the target

None of the following is sufficient:

1. `V_jx=0` at finitely many selected real zeros;
2. equality between packet dimension and a low-index upper bound;
3. positivity of the ambient complement after moving dangerous directions into
   the finite packet;
4. `L2` density of global radicals without form/metric convergence;
5. small tails for the old radical subpacket only;
6. a Schur correction estimate with the wrong sign.

The Schur term is negative semidefinite and strengthens any hidden negative
kernel defect.

## 8. Proof boundary

- The finite Schur inequality is elementary and exact.
- The off-line cardinal signature `-2m` follows from the centered zero-sum
  normalization.
- The finite-support repair and cardinal tail/domain estimates are inherited
  from `L-14321/T-14306/T-14307` and require their independent normalization
  audit.
- The fixed-gap conclusion requires complete form/metric capture of the
  off-line-cardinal sequence.
- The lemma classifies the final obstruction; it does not establish RH.
