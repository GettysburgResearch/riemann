# T-19813 — Affine hybrid exact-periodized resolution theorem

Claim ID: `T-19813`  
Status: **PROPOSED FULL RH RESOLUTION — ONE SOURCE-SPECIFIC AFFINE PROFILE THEOREM PENDING REVIEW**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-07  
Dependencies: affine transfer `L-19861`; hybrid residual hierarchy `L-19862`; endpoint repair `L-19863`; geometric fold `L-19864`; affine profile adapter `L-19865`; exact Xi target `L-19849`; finite real-zero/Hurwitz interface `T-14301`  
Supersedes: the unshifted continuous proposal `T-19811` and the incomplete common-reservoir proposal `T-19812`  
Scope: final recovered positive proposal; **not an accepted proof until the source-specific profile LMIs survive independent review**

## 1. Strategic resolution of the three review blockers

The revised deep review identified three failures:

1. a complete unshifted Loewner comparison already implies RH and is therefore
   circular as an intermediate local-Weyl gate;
2. exact finite surjectivity and the low-prolate hierarchy had not been proved
   on one common source reservoir;
3. the `k>R` stationary calculation used an invalid interior stationary-phase
   expansion inside the Bessel endpoint layer.

The present theorem replaces all three.

```text
unshifted Loewner             -> affine shifted one-sided coercivity;
prolate/common-reservoir gap  -> exact Xi target + exterior cardinal complement;
k>R stationary phase         -> collective Bessel endpoint L2 estimate.
```

The target/complement residual hierarchy is exact and has a constant gap. The
remaining analytic theorem is the explicit affine profile estimate of
`L-19865` for this same residual family, including its bounded/central ordinate
block.

## 2. Cofinal finite spaces

Let

\[
 L_j\to\infty,
 \qquad
 I_j=[-L_j/2,L_j/2],
 \tag{T-19813.1}
\]

and choose

\[
 N_j=\lceil cL_j^2\rceil
 \tag{T-19813.2}
\]

with one fixed `c` large enough for every target Hardy estimate below. Put

\[
 V_j=\operatorname{span}\{e_k:|k|\le N_j\}
 \subset L^2(I_j).
 \tag{T-19813.3}
\]

Choose `L_j` in the positive-measure good set where all finite zeta multipliers
needed by the exterior cardinal construction are nonzero and all declared
profile estimates pass.

## 3. Exactly normalized target and complete reservoir

Let `J_Xi=E(p_+)` be the exact arithmetic radical with transform a nonzero real
multiple of `Xi`. Define

\[
 v_j=P_{N_j}\Sigma_{L_j}J_{\Xi},
 \qquad
 \nu_j=\|v_j\|_2,
 \qquad
 p_j={v_j\over\nu_j},
 \tag{T-19813.4}
\]

and scale its global lift simultaneously:

\[
 \widetilde J_{\Xi,j}={J_{\Xi}\over\nu_j}.
 \tag{T-19813.5}
\]

Then

\[
 P_{N_j}\Sigma_{L_j}\widetilde J_{\Xi,j}=p_j
 \tag{T-19813.6}
\]

exactly, and `nu_j` stays bounded above and below away from zero.

For every vector `w` in the ordinary orthogonal complement of `p_j`, use the
exterior-supported smooth arithmetic cardinals of `L-19862` to construct a
linear global radical lift `J_w` satisfying

\[
 \Sigma_{L_j}J_w=w,
 \qquad
 J_w|_{I_j}=0.
 \tag{T-19813.7}
\]

Together with `widetilde J_(Xi,j)`, these lifts form one exact source reservoir
mapping isomorphically onto the complete finite space `V_j`.

For a finite vector `ap_j+w`, define its exact global residual by

\[
 W_j(ap_j+w)
 =a[\widetilde J_{\Xi,j}-\iota_jp_j]
  +[J_w-\iota_jw].
 \tag{T-19813.8}
\]

Let

\[
 D_j=W_j^*W_j
 \tag{T-19813.9}
\]

be the complete ordinary residual Gram.

## 4. Exact target/gap hierarchy

For every prescribed `B>0`, increasing the fixed constant in (T-19813.2) gives

\[
 \boxed{m_j:=D_j(p_j,p_j)\le C_Be^{-BL_j}.}
 \tag{T-19813.10}
\]

For `w perpendicular p_j`, physical support separation gives

\[
 D_j(w,w)
 =\|J_w\|^2+\|w\|^2
 \ge\|w\|^2.
 \tag{T-19813.11}
\]

Therefore Cauchy interlacing yields the exact complete gap

\[
 \boxed{\theta_2(D_j)\ge1.}
 \tag{T-19813.12}
\]

No source inverse norm, pure-prolate `d_6` transfer, or common-reservoir
assumption remains. Equations (T-19813.10)--(T-19813.12) give

\[
 {m_j\over\theta_2(D_j)}\le C_Be^{-BL_j}.
 \tag{T-19813.13}
\]

## 5. Exact finite Weil identity

Every source lift is a global arithmetic radical. Hence for finite vectors
`v,z in V_j`,

\[
 \boxed{
 A_j(v,z)
 :=Q_W(v,z)
 =Q_W(W_jv,W_jz).}
 \tag{T-19813.14}
\]

This is the exact finite CCM/Weil matrix. It includes the support tail, every
periodization fold, and the complete finite residual; no `q` term or alias is
silently omitted.

## 6. Affine source-specific profile theorem

Assume the complete residual family (T-19813.8) satisfies the source-specific
profile LMIs of `L-19865` on a positive-measure set in every sufficiently large
support block. Concretely:

\[
 A_j^0=a_jD_j+C_j+E_j^0,
 \tag{T-19813.15}
\]

with `a_j>0`,

\[
 -c_{0,j}(D_j+\tau_jI)
 \preceq C_j\preceq
 c_{0,j}(D_j+\tau_jI),
 \tag{T-19813.16}
\]

\[
 -\alpha_j(D_j+\tau_jI)
 \preceq E_j^0\preceq
 \alpha_j(D_j+\tau_jI),
 \tag{T-19813.17}
\]

and the **complete** actual-minus-line estimate

\[
 -\delta_j(D_j+\tau_jI)
 \preceq A_j-A_j^0\preceq
 \delta_j(D_j+\tau_jI).
 \tag{T-19813.18}
\]

The last estimate includes a directly certified bounded/central ordinate block;
only the dyadic high-ordinate part is delegated to support averaging.

Set

\[
 \tau_j=m_j,
 \tag{T-19813.19}
\]

\[
 c_j=a_j-c_{0,j}-\alpha_j-\delta_j,
 \tag{T-19813.20}
\]

and require

\[
 \boxed{c_j>0.}
 \tag{T-19813.21}
\]

Put

\[
 \sigma_j=-(c_{0,j}+\alpha_j+\delta_j)m_j.
 \tag{T-19813.22}
\]

Then `L-19865` gives

\[
 \boxed{A_j-\sigma_jI\succeq c_jD_j.}
 \tag{T-19813.23}
\]

On the target line,

\[
 \boxed{
 A_j(p_j,p_j)-\sigma_j
 \le C_j^{\rm tar}c_jm_j,}
 \tag{T-19813.24}
\]

where

\[
 C_j^{\rm tar}
 ={a_j+3(c_{0,j}+\alpha_j+\delta_j)\over c_j}.
 \tag{T-19813.25}
\]

Require the exact target/gap rate

\[
 \boxed{C_j^{\rm tar}m_j\longrightarrow0.}
 \tag{T-19813.26}
\]

Because `m_j` may be made `e^(-B L_j)` for arbitrary fixed `B`, this permits
large but sub-prescribed-exponential profile losses. No universal assertion
`a_j=log R_j` is made for the multi-scale hybrid family.

The lower estimate is shifted; it does not assert `A_j>=0` and therefore does
not assume cofinal Weil positivity.

## 7. Source-specific analytic ledger

The proof target (T-19813.15)--(T-19813.18) is fully typed:

1. `L-19821` supplies the line-centered positive operator Riemann--von Mangoldt
   decomposition on each declared frequency branch.
2. Bounded and central zero ordinates are retained as exact finite Hermitian
   blocks. A hypothetical low off-line zero is not placed in a high-frequency
   large-sieve error.
3. `L-19818` supplies the rank-one actual-minus-line support large sieve on
   eligible dyadic high-ordinate blocks, paying one source envelope rather than
   its square.
4. Radial endpoints use the Bessel/simple-pole model.
5. Every arithmetic alias `2<=k<=R` uses its unique nondegenerate stationary
   point.
6. Every `k>R` contribution is treated collectively in the endpoint layer by
   `L-19863`, not by nonuniform stationary phase.
7. The Mellin frequency fold alone uses the Airy/cubic model.
8. Leading `1/k` and `(log k)/k` endpoint channels are summed by Parseval before
   norms are taken.
9. Logarithmic periodization folds are treated separately by `L-19864`.
10. Every phase-neutral horizontal term remains in the main, central, or scalar
    correction; only eligible oscillatory crosses enter the support sieve.
11. The final interval/operator ledger must prove both `c_j>0` and
    `C_j^tar m_j->0`.

The abstract estimates in items 1 and 3--9 are proved in the cited files. The
remaining production task is to bind their constants to the exact hybrid
residual (T-19813.8), certify the central blocks, and verify the LMIs in one
normalization.

## 8. Simple even finite ground state

Apply `L-19861` with

\[
 Q=A_j,
 \quad
 D=D_j,
 \quad
 g=1,
 \quad
 c_-=c_j,
 \quad
 c_+=C_j^{\rm tar}c_j,
 \quad
 m=m_j.
\]

Equations (T-19813.10), (T-19813.12), and
(T-19813.23)--(T-19813.26) give

\[
 \boxed{
 \|p_j-\alpha_j^{\rm gr}\xi_j\|_2^2
 \le
 {C_j^{\rm tar}m_j
  \over1-C_j^{\rm tar}m_j}
 \longrightarrow0.}
 \tag{T-19813.27}
\]

The cutoff constant may be chosen so that the right side is
`e^(-B L_j+o(L_j))`. Here `xi_j` is the normalized finite ground state after a
phase choice. The finite form commutes with inversion and `p_j` is even, so
`xi_j` is eventually even. Its lowest eigenvalue is simple and isolated.

## 9. Moving-Hardy convergence

Choose the target cutoff rate so that

\[
 e^{2\tau_j^{\rm H}L_j}
 {C_j^{\rm tar}m_j
  \over1-C_j^{\rm tar}m_j}
 \longrightarrow0
 \tag{T-19813.28}
\]

for a sequence

\[
 \tau_j^{\rm H}\nearrow1/2.
\]

The Xi source tail and quadratic-log Fourier theorem give nonzero real
normalizations `b_j` for which

\[
 \|b_jp_j-k_j^{\Xi}\|_{\tau_j^{\rm H}}
 \longrightarrow0,
 \tag{T-19813.29}
\]

where the transforms of `k_j^Xi` converge locally uniformly to `Xi`.
Combining (T-19813.28)--(T-19813.29),

\[
 \boxed{
 \|c_j'\xi_j-k_j^{\Xi}\|_{\tau_j^{\rm H}}
 \longrightarrow0}
 \tag{T-19813.30}
\]

for nonzero real `c_j'`.

## 10. Real zeros and RH

The independently reviewed finite CCM theorem applies to every simple even
finite ground state: `widehat xi_j` is entire and all its zeros are real. The
Hardy-strip estimate turns (T-19813.30) into local-uniform convergence

\[
 \widehat{c_j'\xi_j}\longrightarrow\Xi
\]

on compact subsets of the centered critical strip. Hurwitz excludes every
nonreal zero of `Xi`. Therefore the hypotheses of Section 6 imply

\[
 \boxed{\mathrm{RH}.}
 \tag{T-19813.31}

## 11. Exact status boundary

The former assembly gaps are closed:

```text
finite projection residual          retained exactly;
exact finite surjectivity           explicit;
common source reservoir             explicit;
complete ordinary residual gap      >=1 exactly;
target residual                     exponentially small;
periodization fold index            separated from Poisson alias index;
k>R endpoint range                  repaired;
unshifted positivity assumption     removed by scalar shift.
```

The remaining review target is singular and concrete:

\[
 \boxed{
 \begin{gathered}
 \text{verify (T-19813.15)--(T-19813.18) for the exact hybrid residual
 family (T-19813.8), including the central zero block,}\\
 c_j>0,\qquad
 C_j^{\rm tar}m_j\to0.
 \end{gathered}}
 \tag{T-19813.32}

This is an affine operator-valued Riemann--von Mangoldt/support theorem with
explicit regularization. It is weaker than cofinal positivity and weaker than a
complete two-sided relative local-Weyl law.

Until (T-19813.32) passes independent reconstruction:

```text
final recovered proposal: PROPOSED
accepted proof of RH:      NO
```