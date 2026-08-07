# T-19813 — Affine hybrid exact-periodized resolution theorem

Claim ID: `T-19813`  
Status: **GAPS/BLOCKED — CONDITIONAL COMPOSITION CORRECT, SOURCE-SPECIFIC AFFINE GATE IS RH-BEARING BY `R-19846`**  
Authoring agents: `gpt56-pro-09-r`, status correction `gpt56-pro-09-s`  
Created: 2026-08-07  
Status corrected: 2026-08-07  
Dependencies: affine transfer `L-19861`; hybrid residual hierarchy `L-19862`; endpoint repair `L-19863`; geometric fold `L-19864`; affine profile adapter `L-19865`; exact Xi target `L-19849`; finite real-zero/Hurwitz interface `T-14301`; central obstruction `R-19846`  
Supersedes: the unshifted continuous proposal `T-19811` and the incomplete common-reservoir proposal `T-19812`  
Scope: conditional positive composition; **not a completed proof**

## 1. Strategic architecture

The theorem replaces three earlier invalid interfaces:

```text
unshifted Loewner             -> affine shifted one-sided coercivity;
prolate/common-reservoir gap  -> exact Xi target + exterior cardinal complement;
k>R stationary phase         -> collective Bessel endpoint L2 estimate.
```

The target/complement ordinary residual hierarchy is exact and has a constant
gap. If the source-specific affine gate of Section 6 held, the remaining
spectral and Hurwitz deduction would prove RH.

`R-19846` now proves that, under false RH, the affine gate must fail because an
even off-line Xi-cardinal vector gives a fixed negative finite Rayleigh value,
whereas the Xi target has vanishing Rayleigh value. Thus Section 6 is not a
routine profile theorem left after the high-frequency analysis; it contains the
central RH argument.

## 2. Cofinal finite spaces

Let

\[
 L_j\to\infty,
 \qquad
 I_j=[-L_j/2,L_j/2],
\]

and choose

\[
 N_j=\lceil cL_j^2\rceil
\]

with one fixed `c` large enough for every target Hardy estimate below. Put

\[
 V_j=\operatorname{span}\{e_k:|k|\le N_j\}
 \subset L^2(I_j).
\]

Choose `L_j` where all finite zeta multipliers needed by the exterior cardinal
construction are nonzero.

## 3. Exactly normalized target and complete reservoir

Let `J_Xi=E(p_+)` be the exact arithmetic radical with transform a nonzero real
multiple of `Xi`. Define

\[
 v_j=P_{N_j}\Sigma_{L_j}J_{\Xi},
 \qquad
 \nu_j=\|v_j\|_2,
 \qquad
 p_j={v_j\over\nu_j},
\]

and scale its global lift simultaneously:

\[
 \widetilde J_{\Xi,j}={J_{\Xi}\over\nu_j}.
\]

Then

\[
 P_{N_j}\Sigma_{L_j}\widetilde J_{\Xi,j}=p_j
\]

exactly, and `nu_j` stays bounded above and below away from zero.

For every vector `w` in the ordinary orthogonal complement of `p_j`, use the
exterior-supported smooth arithmetic cardinals of `L-19862` to construct a
linear global radical lift `J_w` satisfying

\[
 \Sigma_{L_j}J_w=w,
 \qquad
 J_w|_{I_j}=0.
\]

For `ap_j+w`, define the exact global residual

\[
 W_j(ap_j+w)
 =a[\widetilde J_{\Xi,j}-\iota_jp_j]
  +[J_w-\iota_jw],
\]

and put

\[
 D_j=W_j^*W_j.
\]

## 4. Exact target/gap hierarchy

For every prescribed `B>0`, increasing the cutoff constant gives

\[
 m_j:=D_j(p_j,p_j)\le C_Be^{-BL_j}.
\]

For `w perpendicular p_j`, physical support separation gives

\[
 D_j(w,w)
 =\|J_w\|^2+\|w\|^2
 \ge\|w\|^2.
\]

Therefore

\[
 \boxed{\theta_2(D_j)\ge1.}
\]

No complete source inverse norm or pure-prolate common-reservoir theorem is
needed.

## 5. Exact finite Weil identity

Every source lift is a global arithmetic radical. Hence

\[
 \boxed{
 A_j(v,z):=Q_W(v,z)=Q_W(W_jv,W_jz)
 \qquad(v,z\in V_j).}
\]

The exact finite projection residual and every periodization fold are retained.

## 6. Conditional affine source-specific gate

The conditional composition assumes a line-centered decomposition

\[
 A_j^0=a_jD_j+C_j+E_j^0
\]

with

\[
 -c_{0,j}(D_j+\tau_jI)
 \preceq C_j\preceq
 c_{0,j}(D_j+\tau_jI),
\]

\[
 -\alpha_j(D_j+\tau_jI)
 \preceq E_j^0\preceq
 \alpha_j(D_j+\tau_jI),
\]

and

\[
 -\delta_j(D_j+\tau_jI)
 \preceq A_j-A_j^0\preceq
 \delta_j(D_j+\tau_jI).
\]

The last estimate must contain every bounded and central ordinate. Set

\[
 \tau_j=m_j,
 \qquad
 c_j=a_j-c_{0,j}-\alpha_j-\delta_j,
\]

and require `c_j>0`. Put

\[
 \sigma_j=-(c_{0,j}+\alpha_j+\delta_j)m_j.
\]

Then `L-19865` gives

\[
 A_j-\sigma_jI\succeq c_jD_j.
\]

The target upper bound is

\[
 A_j(p_j,p_j)-\sigma_j
 \le C_j^{\rm tar}c_jm_j,
\]

with

\[
 C_j^{\rm tar}
 ={a_j+3(c_{0,j}+\alpha_j+\delta_j)\over c_j}.
\]

The conditional closing rate is

\[
 C_j^{\rm tar}m_j\to0.
\]

### Status correction

`R-19846` proves that these inequalities cannot hold cofinally if a nonreal
zero of `Xi` exists. The even cardinal quartet is approximated inside the same
`V_j` and forces `sigma_j<=-kappa`, while the target upper bound forces
`sigma_j->0`.

Therefore the complete Section 6 gate is itself RH-bearing. The Bessel/Airy/
large-sieve machinery only treats its high-ordinate portion; it does not prove
the central sign.

## 7. Conditional spectral conclusion

If Section 6 were independently proved, `L-19861` would give

\[
 \|p_j-\alpha_j^{\rm gr}\xi_j\|_2^2
 \le
 {C_j^{\rm tar}m_j\over1-C_j^{\rm tar}m_j}
 \to0,
\]

where `xi_j` is the simple even finite ground state.

Choosing the target cutoff sufficiently rapidly would upgrade this to the
moving Hardy norm. The finite CCM real-zero theorem and Hurwitz would then imply
RH.

This conditional deduction remains correct.

## 8. Current status boundary

Durable:

```text
exact Xi target and normalization;
exact exterior-cardinal complement;
complete residual gap >=1;
exact finite radical identity;
affine abstract spectral transfer;
corrected endpoint and fold ledgers;
conditional spectral/Hurwitz deduction.
```

Unproved and RH-bearing:

```text
complete bounded/central actual-minus-line affine sign;
source-specific Section 6 gate;
RH.
```

Accordingly:

```text
T-19813 conditional implication: VERIFIED CONDITIONAL
T-19813 as a proof of RH:       GAPS/BLOCKED
accepted proof of RH:           NO
```
