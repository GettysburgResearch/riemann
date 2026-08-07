# Final adversarial recovery after the revised deep review

Agent: `gpt56-pro-09-r`  
Date: 2026-08-07  
PR: #202  
Frozen launch head: `753556b65e955877a07c32a07db6f234719df461`  
Classification: **REVIEW VERIFIED IN ITS REFUTATIONS; COMMON RESERVOIR AND AFFINE ENDPOINT REPAIRED; FINAL PROFILE LMI PROPOSED; RH NOT CLAIMED**

## 1. Bottom line

The revised reviewer is correct that:

```text
T-19810.18 is false;
the frozen L-19844 geometry is false;
ordinary L2 closure trivializes the continuous radical quotient;
the unshifted complete Loewner hypothesis in T-19811 is already RH-bearing;
T-19811 and T-19812 do not stand as completed proofs.
```

The review's affine one-sided criterion is the correct spectral endpoint.
However, its proposed hybrid route still treated the common-reservoir spectral
hierarchy as open. This pass closes that algebraic gap exactly.

The new finite reservoir consists of:

```text
one exactly normalized Xi radical lift;
all orthogonal finite directions lifted by exterior-supported smooth arithmetic
cardinals.
```

The complete residual compression to the target complement is at least the
identity, while the target residual is exponentially small. Thus

\[
 \theta_2(D_j)\ge1,
 \qquad
 D_j(p_j)\le e^{-BL_j}
\]

for arbitrary fixed `B`, in one exact onto source reservoir.

The final repaired theorem `T-19813` then needs only the shifted one-sided
profile estimate of `L-19865`. It does not assume localized Weil positivity.

Current status:

\[
 \boxed{\text{FINAL RECOVERED PROPOSAL: PROPOSED}}
\]

\[
 \boxed{\text{ACCEPTED PROOF OF RH: NO}}
\]

## 2. Review findings retained

| Reviewed item | Final disposition |
|---|---|
| rejection of `T-19810.18` | **VERIFIED** |
| exact finite residual `t+q` | **VERIFIED** |
| rejection of frozen `L-19844` | **VERIFIED** |
| unique later-alias stationary point | **VERIFIED** |
| radial endpoint is Bessel, not Airy | **VERIFIED** |
| `k>R` ordinary stationary phase invalid | **VERIFIED** |
| `L-19858` exact Fourier containment | **VERIFIED** |
| `L-19860` local Möbius reconstruction | **VERIFIED** |
| positive residual corrections preserve low index | **VERIFIED** |
| full `D_q=o(D_t)` is necessary | **REJECTED AS OVERSTRONG** |
| ordinary-L2 continuous quotient | **REJECTED / TRIVIALIZES** |
| unshifted complete relative Loewner is a routine input | **REJECTED; IT ALREADY IMPLIES RH** |
| affine one-sided shifted criterion | **VERIFIED AND SHARPENED** |

## 3. Exact affine theorem

`L-19861` proves the following.

Let `Q` be a closed lower-bounded form, `D>=0`, and `p` a unit target. If

\[
 \theta_2(D)\ge g,
\]

\[
 Q-\sigma I\succeq c_-D,
\]

and only on the target line

\[
 Q(p,p)-\sigma\le c_+m,
\]

then, whenever `c_+m<c_-g`, the ground value is simple and isolated and

\[
 \boxed{
 \operatorname{dist}(p,\mathbb C\xi_1)^2
 \le {c_+m\over c_-g-c_+m}.}
\]

The shift may be negative. This is strictly weaker than complete two-sided
scalarization and does not imply `Q>=0`.

`R-19845` proves that deleting the shift would make the complete lower Loewner
inequality itself a cofinal Weil-positivity proof of RH.

## 4. Exact common reservoir with a constant gap

### 4.1 Target

Let `J_Xi=E(p_+)` be the exact global radical whose transform is a nonzero real
multiple of `Xi`. Put

\[
 v_{L,N}=P_N\Sigma_LJ_{\Xi},
 \qquad
 p_{L,N}=v_{L,N}/\|v_{L,N}\|.
\]

Scale the global lift by the same norm. The exact residual is

\[
 W_*=J_{\Xi}/\|v_{L,N}\|-\iota_Lp_{L,N}.
\]

Xi strip decay and the quadratic-log Fourier cutoff give, for every fixed
`B>0`,

\[
 \boxed{\|W_*\|^2\le C_Be^{-BL}}
\]

after choosing `N=c_BL^2`.

### 4.2 Exterior cardinal complement

Translate the smooth differential Mellin cardinals to logarithmic support
strictly below the central interval. After division by the nonzero finite zeta
multiplier, their arithmetic images satisfy

\[
 \Sigma_LJ_k=e_k
\]

exactly and vanish on the complete central interval.

For every finite vector `w` orthogonal to the target, choose its exterior lift
`J_w`. Its exact residual is

\[
 W_w=J_w-\iota_Lw.
\]

The two pieces have disjoint supports, so

\[
 \boxed{
 \|W_w\|^2=\|J_w\|^2+\|w\|^2\ge\|w\|^2.}
\]

Thus the complete residual Gram satisfies

\[
 D|_{p^\perp}\succeq I.
\]

Cauchy interlacing yields

\[
 \boxed{\theta_2(D)\ge1.}
\]

Cross pairings with the target residual do not need to be estimated.

This is `L-19862`. It places exact finite surjectivity, the Xi target, and a
complete spectral gap in one source reservoir.

## 5. Alias and fold repairs

### 5.1 Large arithmetic aliases

For `k>R`, the later-alias stationary point lies inside the Bessel endpoint
layer. `L-19863` withdraws the nonuniform individual stationary expansion and
proves instead:

\[
 \int_{1}^{1+cR^{-2}}|\rho_R(z)|^2dz
 \ll R^{-1}\log^CR,
\]

while the complete higher-alias endpoint aggregate has polylogarithmic `L2`
norm by the exact `1/k` and `(log k)/k` Parseval identities. Cauchy--Schwarz
therefore gives

\[
 \boxed{\text{complete }k>R\text{ endpoint cross}
 \ll R^{-1/2}\log^CR.}
\]

Outside the endpoint layer the phase is nonstationary. Together with the valid
`2<=k<=R` stationary calculation, the complete later-alias cross is
`O(R^-1/2 log^C R)`.

### 5.2 Geometric periodization folds

`L-19864` separates logarithmic folds `m` from arithmetic aliases `k`. If the
annular tail obeys

\[
 \|t(\mu^{-m}\cdot)\|_{L^2(I)}
 \le A_Lq_L^{m-1}\|t\|,
\]

then

\[
 \boxed{
 \|\mathfrak F_Lt\|
 \le {2A_L\over1-q_L}\|t\|.}
\]

The canonical radial `1/z` bound gives a polylogarithmic fold loss, while the Xi
target has faster-than-exponential fold decay.

## 6. Affine local-Weyl adapter

Let

\[
 \widehat D_R=D_R+\tau_RI.
\]

The complete line-centered matrix is required to have a certified decomposition

\[
 A_R^0=a_RD_R+C_R+E_R^0,
\]

where

\[
 |C_R|\preceq c_{0,R}\widehat D_R,
 \qquad
 |E_R^0|\preceq\alpha_R\widehat D_R.
\]

No universal formula `a_R=log R` is asserted for the hybrid multi-scale
profile. Every frequency branch must contribute in its actual normalization.

The complete actual-minus-line matrix, including bounded and central zero
ordinates, must satisfy

\[
 |A_R-A_R^0|\preceq\delta_R\widehat D_R.
\]

The rank-one support large sieve controls eligible high-ordinate oscillatory
branches. It does **not** control a fixed low off-line zero; every bounded or
central ordinate block must be retained and certified directly inside
`delta_R`, or absorbed into a separately certified scalar shift.

If

\[
 c_R=a_R-c_{0,R}-\alpha_R-\delta_R>0,
\]

then `L-19865` gives

\[
 \boxed{
 A_R-\sigma_RI\succeq c_RD_R,}
\]

where

\[
 \sigma_R=-(c_{0,R}+\alpha_R+\delta_R)\tau_R.
\]

Choosing `tau_R=m_R=D_R(p_R)` gives

\[
 A_R(p_R,p_R)-\sigma_R
 \le C_R^{\rm tar}c_Rm_R,
\]

with

\[
 C_R^{\rm tar}
 ={a_R+3(c_{0,R}+\alpha_R+\delta_R)\over c_R}.
\]

The exact closing rate is

\[
 \boxed{C_R^{\rm tar}m_R\to0.}
\]

Because the target residual may be made `e^{-BL}` for arbitrary fixed `B`, the
criterion permits large but explicitly bounded profile losses. The scalar shift
keeps the theorem weaker than cofinal positivity.

## 7. Full proposal `T-19813`

The final composition is:

```text
exact Xi global radical
+ exterior-supported exact finite complement
-> exact complete residual Gram with target m_R and gap >=1
-> complete affine shifted one-sided profile estimate
-> simple isolated even finite ground state
-> moving-Hardy convergence to the Xi target
-> finite real-zero theorem
-> Hurwitz
-> RH.
```

The proposal retains every finite projection residual and every periodization
fold. It does not use a pure-prolate complete reservoir and does not assume
localized Weil positivity.

## 8. Exact verifier

`X-19841-affine-hybrid` reconstructs a non-diagonal rational residual Gram and
checks:

```text
complete complement floor     1
target residual energy        1/100
affine lower coefficient      3
target excess                 3/100
strict separation margin      297/100
```

The exact proof-object digest is

```text
7b1a65e8b957aadb8ed2613bcb7a6e87d93c5a3afa9e4ea05bc625e02fd278f5
```

and five adversarial mutations fail closed.

## 9. Final review frontier

All algebraic and assembly blockers identified by the latest review have been
removed. The one remaining theorem to reconstruct is:

\[
 \boxed{
 \begin{gathered}
 A_R^0=a_RD_R+C_R+E_R^0,\\
 |C_R|\preceq c_{0,R}(D_R+m_RI),\\
 |E_R^0|\preceq\alpha_R(D_R+m_RI),\\
 |A_R-A_R^0|\preceq\delta_R(D_R+m_RI),\\
 c_R:=a_R-c_{0,R}-\alpha_R-\delta_R>0,\\
 C_R^{\rm tar}m_R\to0,
 \end{gathered}}
\]

for the exact hybrid residual family of `L-19862`, including an exact finite
certificate for every central ordinate block not covered by support averaging.

The branch contains the abstract Riemann--von Mangoldt, rank-one support-sieve,
Bessel endpoint, stationary-alias, and geometric-fold components. The remaining
task is source-specific normalization and their complete interval/operator
assembly.

Until that theorem is independently verified:

```text
T-19813 final proposal: PROPOSED
accepted proof of RH:    NO
```
