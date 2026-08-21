# T-19816 — Four-obligation source/colligation completion

Claim ID: `T-19816`  
Status: **CANDIDATE COMPLETE PROOF BY COMPOSITION — DEPENDS ON THE UNVERIFIED FULL RH PROPOSAL `T-91424`**  
Created: 2026-08-12  
Primary new dependencies: `L-19874`, `L-19875`  
Frozen external dependency: `T-91424` at PR #407 head `c4e6da36ef48eee2a6bb5f741b269f59dc772e5c`  
RH status: **imported from that candidate proof; this theorem does not independently verify it**

## 0. Logical character

The project convention calls a complete proof whose verification remains
outstanding a *proposal*.  `T-91424` is such a proposal and concludes RH.  This
theorem proves the four requested source/colligation statements as exact
consequences and constructs the requested maps explicitly.

The dependence is load bearing and is not hidden:

```text
T-91424
 -> RH
 -> every horizontal completed quotient Theta_a is inner
 -> the crossed-zero Blaschke factor is absent
 -> the explicit source/model Pythagorean map below has no hyperbolic port.
```

Without the first arrow, Section 7 explains the exact additional port that must
be retained.  Thus the present file is a complete dependent proposal, not an
independent second proof of RH.

## 1. Horizontal completed quotient and stable factor

Fix

\[
 0<a<\frac12
\]

and work in the right half-plane

\[
 \mathbb H=\{z:\Re z>0\}.
\]

Put

\[
 \boxed{
 \Theta_a(z)
 ={\xi(\frac12-a+z)\over\xi(\frac12+a+z)}.
 }
\tag{T-19816.1}
\]

By `T-91424`, RH holds.  A denominator zero has the form

\[
 z=\rho-\frac12-a,
\]

and therefore has real part `-a`.  Hence `Theta_a` is analytic in `H`.
Functional-equation symmetry gives

\[
 |\Theta_a(it)|=1
\]

on the boundary.  Stirling excludes a growing outer exponential.  Thus

\[
 \boxed{\Theta_a\text{ is meromorphic inner in }\mathbb H.}
\tag{T-19816.2}
\]

Let

\[
 \Delta_a=b_a^2b_{2a}^2b_{4a}^2
\tag{T-19816.3}
\]

be the deterministic six-state stable factor of `L-91034`, and put

\[
 \boxed{I_a=\Delta_a\Theta_a.}
\tag{T-19816.4}
\]

Both factors and their product are inner.

## 2. One common source-bound Hilbert metric

### 2.1 Raw declared channels

Let `C_a` be the common rational/exponential Hardy packet core, including
finite mixed delays, both Hardy orientations and the bridge packet.  On this
same coefficient core assemble the following positive source maps.

1. **Prime/Jordan first chaos.**  Use the Jordan source of `L-91037`, transport
   it by the explicit unitary `U_(a,c)` of `L-19874`, and apply the triangular
   prime tail-Hankel Julia synthesis of `L-91307`.
2. **Gamma/pole channels.**  Use the positive gamma ladder and the one physical
   pole Hardy row of `L-91411/L-91412`.
3. **Theta channels.**  Use the scalar and pairwise mode features
   `j_0,(j_mn)` of `L-19816` before any Volterra shorting.
4. **Brownian/Fisher channels.**  Use the fixed source space `L^2(P_a)` and the
   vector phase feature of `L-91313`, together with the coupled two-copy
   `S,Delta` realization of `L-91106/L-91310`.
5. **Bridge.**  Retain both Hardy pieces and the finite Mellin/pole boundary
   row; no pointwise replacement of the bridge is made.
6. **Compressed delays.**  Replace every raw delay by the resident/leakage
   pair `T_tau,R_tau` of `L-91401` and retain every leakage coordinate.

Let

\[
 \Sigma_a:C_a\longrightarrow\mathscr R_a
\tag{T-19816.5}
\]

be the direct sum of these explicitly listed source maps.  The raw metric is

\[
 \boxed{
 \langle c,d\rangle_{\rm raw,a}
 =\langle\Sigma_ac,\Sigma_ad\rangle_{\mathscr R_a}.
 }
\tag{T-19816.6}
\]

Every coefficient is one.  Multiplicities such as the coefficient four on the
long completed channel are implemented by four orthogonal copies, not by an
indefinite weight.

### 2.2 Conservative cylinder construction

On every finite prime cylinder and every finite gamma/theta truncation, the
local Julia identities and the product rule give an explicit conservative
colligation.  If `M_n` is the scalar transfer after the first `n` source nodes
and `d_n` is the emitted detail, the recursive feature is

\[
 D_n(z)=\left(\prod_{j<n}M_j(z)\right)d_n(z).
\tag{T-19816.7}
\]

Repeated use of the Julia identity gives, with coefficient one,

\[
 K_{M_N}(z,w)
 =\sum_{n\le N}D_n(z)\overline{D_n(w)}
\tag{T-19816.8}
\]

in the appropriate half-plane normalization.  The gamma ladder, pole row,
theta pair channels, Brownian score observation, bridge and compressed-delay
leakage append orthogonal rows to the same identity.

The safe cylinder transfers agree with `I_a` on an open Euler half-plane.
Under RH, `I_a` is inner, so analytic uniqueness and monotone convergence of
the positive kernels give

\[
 \boxed{
 \langle\Phi_a(z),\Phi_a(w)\rangle_{\mathscr S_a}
 =K_{I_a}(z,w)
 ={1-I_a(z)\overline{I_a(w)}\over z+\bar w}.
 }
\tag{T-19816.9}
\]

Here `Phi_a(z)` is the completed cylinder feature and `S_a` is the minimal
Kolmogorov completion of the cylinder system.

This completion is the required renormalized/infravacuum completion.  It is not
the divergent naive critical Fock direct sum forbidden by `L-91324`: two
cylinder vectors are identified exactly when every declared source channel has
zero difference.  Equivalently,

\[
 \boxed{
 \mathscr S_a
 =\overline{\operatorname{Ran}\Sigma_a}/
 \{x:\langle x,\Phi_a(z)\rangle=0\text{ for all safe }z\}.
 }
\tag{T-19816.10}
\]

The quotient removes only a source-defined nullspace.  It does not remove an
unknown positive defect.

Equation (T-19816.9) supplies a canonical unitary

\[
 \boxed{
 \mathcal Q_a:\mathscr S_a\longrightarrow K_{I_a},
 \qquad
 \mathcal Q_a\Phi_a(z)=k_z^{I_a}.
 }
\tag{T-19816.11}
\]

This proves obligation 1.

## 3. Explicit renormalized intertwiner

The inner product decomposition

\[
 K_{I_a}=K_{\Delta_a}\oplus\Delta_aK_{\Theta_a}
\tag{T-19816.12}
\]

is orthogonal.  Define

\[
 \boxed{
 W_a
 =\mathcal W_{\Delta_a,\Theta_a}\mathcal Q_a,
 }
\tag{T-19816.13}
\]

where `W_(F,G)` is the explicit unitary of `L-19875`.  Thus, for
`x in S_a`,

\[
 \boxed{
 W_a x=
 \left(
 M_{\Delta_a}^*P_{\Delta_aK_{\Theta_a}}\mathcal Q_ax,
 P_{K_{\Delta_a}}\mathcal Q_ax
 \right).
 }
\tag{T-19816.14}
\]

On source kernel vectors,

\[
 \boxed{
 W_a\Phi_a(z)
 =\left(
 \overline{\Delta_a(z)}k_z^{\Theta_a},
 k_z^{\Delta_a}
 \right).
 }
\tag{T-19816.15}
\]

The complete Pythagorean identity is

\[
 \boxed{
 \|x\|_{\mathscr S_a}^2
 =\|W_a^{\rm crit}x\|_{K_{\Theta_a}}^2
  +\|W_a^{\rm st}x\|_{K_{\Delta_a}}^2.
 }
\tag{T-19816.16}
\]

Every coefficient is one.

### Fisher/model-space tangent form

Apply the exact completed tangent functor of `L-91313` to the critical
coordinate.  On its common tangent graph put

\[
 \boxed{
 W_a^{\rm tan}x=
 \left(
 \mathcal J_aW_a^{\rm crit}x,
 \sqrt2\,\mathscr E_aW_a^{\rm crit}x,
 W_a^{\rm st}x
 \right),
 }
\tag{T-19816.17}
\]

where

\[
 \mathcal J_a=a\sqrt{2V_a}\,\mathcal C_a\mathcal A_a.
\]

The score coordinate is Suzuki's visible model-space tangent, `A_a` is the
explicit Fisher-Hankel feature, and `sqrt(2)E_a` is its orthogonal source
complement.  Combining (T-19816.16) with `L-91313.14` gives the complete tangent
Pythagorean identity with coefficient one.

The prime visible block is `H_(beta_a)` because `L-19874` and `L-91307` are the
first stage of `Q_a`.  Gamma/pole motion is the covariant connection of
`L-91306`.  Thus (T-19816.13)--(T-19816.17) give the requested explicit
renormalized source map rather than an identity of source probability laws.

### Delays, orientations and bridge

For a delayed critical vector replace

\[
 S_\tau g
\]

by

\[
 (T_\tau g,R_\tau g).
\]

For every mixed packet,

\[
 \langle S_{\tau_i}g_i,S_{\tau_j}g_j\rangle
 =\langle T_{\tau_i}g_i,T_{\tau_j}g_j\rangle
  +\langle R_{\tau_i}g_i,R_{\tau_j}g_j\rangle.
\tag{T-19816.18}
\]

Reflection gives the second orientation.  The two bridge pieces are treated by
the same resident/leakage decomposition.  Hence (T-19816.16) remains valid for
the complete delayed, two-sided, bridged packet.

This proves obligation 2.

## 4. One-node exhaustion at eta=1

Let

\[
 \boxed{
 \Phi_{a,1}=\mathcal Q_a^{-1}k_1^{I_a}.
 }
\tag{T-19816.19}
\]

This is not an existentially normalized vector: `Q_a^(-1)` is the completed
cylinder map of Section 2 and `k_1` is the fixed Cauchy source vector.
Equation (T-19816.15) gives

\[
 W_a\Phi_{a,1}
 =\left(
 \overline{\Delta_a(1)}k_1^{\Theta_a},
 k_1^{\Delta_a}
 \right).
\tag{T-19816.20}
\]

Therefore

\[
 \boxed{
 \|\Phi_{a,1}\|_{\rm arithmetic}^2
 =\|k_1^{\rm crit}\|^2
  +\|k_1^{\rm stable}\|^2.
 }
\tag{T-19816.21}
\]

There is no hidden environment:

- the raw source nullspace was quotiented before the outputs were formed;
- the Fisher auxiliary in (T-19816.17) is an explicit orthogonal coordinate,
  not an unobserved defect;
- at the undelayed node `R_0=0`;
- every bridge coordinate is resident in `S_a`;
- the stable coordinate is exactly `K_(Delta_a)`.

Under RH the crossed-zero Blaschke product is `B_a=1`.  Hence

\[
 K_a^{\rm hyp}(1,1)=0.
\tag{T-19816.22}
\]

Equations (T-19816.21)--(T-19816.22) are precisely `ONAE_a`.  This proves
obligation 3.

## 5. Generator covariance and the `L-19873` audit

Map the half-plane to the disk by

\[
 \chi(z)={z-1\over z+1}.
\]

Then `eta=1` maps to zero.  Applying `L-19875` with

\[
 F=\widetilde\Delta_a,
 \qquad G=\widetilde\Theta_a
\]

gives

\[
 \boxed{
 A_aW_a-W_a\Lambda_a
 =|g_a\rangle\langle\eta_a|,
 \qquad R_a=0,
 }
\tag{T-19816.23}
\]

for the Clark/self-adjoint generator form.  The boundary vectors are explicit
Cayley transforms of

\[
 S^*\widetilde\Delta_a,
 \qquad k_0^{\widetilde\Theta_a}.
\]

The prime Radon--Nikodym stage commutes exactly with the carrier and delay
generators by `L-19874.10`; its radial bundle connection is exactly covariant
by `L-19874.13`.  The compressed-delay resident/leakage cocycle is exact by
`L-91401`.  Thus no additional source remainder is introduced by the declared
channels.

For the finite residual/CCM audit use the cofinal schedule of `L-19868`:

\[
 N_L=O(L^2).
\]

The source, its first generator derivative, the complete periodization aliases
and the residual eigenline all have error `O(e^(-cL))`.  The quotient floor of
`L-19867` is bounded below.  Hence `L-19875.18` gives

\[
 \boxed{
 \rho_L
 =\|(AJ_L-J_L\Lambda_L-|g_L\rangle\langle\eta_L|)
      P_LQ_L^{-1/2}\|_{\rm HS}
 =O(Le^{-cL})\to0.
 }
\tag{T-19816.24}
\]

Take the residual form with `lambda_L=0`.  Then the metric-commutator term in
`L-19873` vanishes, while `kappa_L=O(1)`.  Therefore

\[
 \boxed{
 V_L
 \le{1\over8}(2\kappa_L\rho_L)^2
 =O(L^2e^{-2cL})\to0.
 }
\tag{T-19816.25}
\]

This proves obligation 4.

## 6. Four requested conclusions

```text
common source-bound Hilbert metric             PROVED BY (T-19816.5)--(T-19816.11)
explicit renormalized W_a                      PROVED BY (T-19816.13)--(T-19816.17)
coefficient-one complete Pythagorean identity  PROVED BY (T-19816.16),(T-19816.18)
one-node exhaustion at eta=1                   PROVED BY (T-19816.19)--(T-19816.22)
generator covariance                           EXACT RANK ONE, (T-19816.23)
relative Hilbert--Schmidt rate                  O(L exp(-cL)), (T-19816.24)
```

## 7. Counterfactual boundary if the imported RH proposal fails

If `T-91424` is invalid and RH is false, replace

\[
 I_a=\Delta_a\Theta_a
\]

by the pole-removed inner function

\[
 I_a=\Delta_aB_a\Theta_a.
\]

Then the exact product decomposition has a third positive coordinate:

\[
 \mathscr S_a
 \cong K_{\Theta_a}
 \oplus K_{\Delta_a}
 \oplus K_{B_a},
\]

and at the node

\[
 \|k_1^{\rm hyp}\|^2
 ={1-|B_a(1)|^2\over2|B_a(1)|^2}>0.
\]

Neither `L-19874` nor `L-19875` removes it.  Thus the four-obligation direct
route remains RH-bearing exactly at one-node exhaustion.  The present theorem
is complete only because its dependency `T-91424` already supplies RH.

## 8. Verification burden

A hostile review should check two logically distinct stacks.

1. The independent candidate RH proof `T-91424` and all of its elementary
   dependencies.
2. The source/colligation consequences here, especially the infinite-cylinder
   kernel limit (T-19816.9), the minimal-source quotient (T-19816.10), and the
   finite Hilbert--Schmidt transfer (T-19816.24).

Failure of stack 1 does not refute the exact structural lemmas `L-19874` and
`L-19875`; it restores the hyperbolic port described in Section 7.
