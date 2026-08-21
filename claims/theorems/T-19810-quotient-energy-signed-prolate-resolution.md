# T-19810 — Quotient-energy signed prolate resolution theorem

Claim ID: `T-19810`  
Status: **PROPOSED FULL COMPOSITION — RH FOLLOWS IF THE NEW ANALYTIC INPUTS SURVIVE INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: `L-19823/L-19824`, `L-19841`, corrected `L-19844/L-19845`, `L-19843`, `L-19846`, `L-19847`; moving-Hardy target theorem `L-16213`; finite Rayleigh-floor theorem `T-15103`; CCM finite-real-zero and transform-limit interfaces  
Supersedes: the source-frame and complete-gap portions of `T-19807/T-19808`  
Scope: corrected positive prolate composition; every new load-bearing lemma remains proposed pending independent review

## 1. What is changed

The rejected proposal required a uniformly controlled congruence

\[
 S_R=P_{N_R}\Sigma_{\mu_R}E|_{U_R}
 \tag{T-19810.1}
\]

between a complete low-prolate source packet and the finite CCM space. That was
used to transport a source tail hierarchy to the natural finite-space metric.
The independent reviewer correctly observed that qualitative surjectivity gives
no controlled right inverse.

The repair does **not** prove such a right inverse. It proves that no complete
right-inverse bound is needed.

The exact replacement is:

```text
generic surjectivity
+ source-map upper bound
+ target-line nondegeneracy
+ quotient-energy min--max
+ complete signed source-tail low-index count.
```

Small singular values make quotient energy larger and are harmless.

## 2. Complete source packet and target

Let

\[
 R=2\pi\lambda^2,
 \qquad
 m_R=O((\log R)^2),
 \tag{T-19810.2}
\]

and let `U_R` be the exact signed low-prolate packet with both source constraints
imposed. It contains both Fourier-sign sectors. Let `u_R` be the exact signed
target from `L-19823`, whose first-alias energy is `O(d_4)`.

The arithmetic map is

\[
 S_R:U_R\longrightarrow V_R,
 \qquad
 S_R=P_{N_R}\Sigma_{\mu_R}E.
 \tag{T-19810.3}
\]

By `L-19847`, outside a countable support set:

\[
 S_R\ \text{is onto and hence bijective},
 \tag{T-19810.4}
\]

\[
 S_R^*H_RS_R\preceq(\log R)^CG_R,
 \tag{T-19810.5}
\]

and

\[
 \|S_Ru_R\|_{H_R}^2\ge c\|u_R\|_{G_R}^2.
 \tag{T-19810.6}
\]

No lower singular-value estimate is assumed. `R-19843` explains why one should
not expect it.

Put

\[
 v_R=S_Ru_R.
 \tag{T-19810.7}
\]

The source-specific prolate-to-Hermite theorem and Mellin factorization give,
in the moving Hardy metric of `L-16213`, nonzero real scalars `c_R` such that

\[
 \|c_Rv_R-k_R^{\Xi}\|_{\lambda,\tau_R}\to0,
 \qquad
 \tau_R\nearrow1/2,
 \tag{T-19810.8}
\]

where the transform of `k_R^Xi` converges locally uniformly to the centered
completed zeta function `Xi`. This is the target-identification step; it is not
inferred merely from surjectivity.

## 3. Complete signed ordinary tail hierarchy

Let `D_R` be the complete ordinary Poisson-tail Gram of the same source packet.
The corrected mode-dependent holomorphic/Airy/endpoint theorem gives one support
in every large block at which

\[
 \|F_R^*H_R+H_R^*F_R\|=o(1)
 \tag{T-19810.9}
\]

and

\[
 \|F_R+H_R\|^2\le(\log R)^C.
 \tag{T-19810.10}
\]

The exact transfer theorem `L-19841`, using the pure signed theorem
`L-19823/L-19824`, yields

\[
 \langle u_R,D_Ru_R\rangle
 \le(\log R)^CC_4d_4(R)\|u_R\|_{G_R}^2,
 \tag{T-19810.11}
\]

and

\[
 \dim\mathbf1_{[0,c_6d_6(R))}
 (G_R^{-1/2}D_RG_R^{-1/2})\le1.
 \tag{T-19810.12}
\]

The complete `-1` Fourier sector is included. The scale is `d_6`, not the
rejected `d_8`.

## 4. Pushforward by quotient energy

Define the finite-space ordinary tail form

\[
 \mathfrak D_R
 =S_R^{-*}D_RS_R^{-1}.
 \tag{T-19810.13}
\]

Because `S_R` is bijective at the selected support, this equals the quotient
form of `L-19846`. Equations (T-19810.5)--(T-19810.6) and
(T-19810.11)--(T-19810.12) give

\[
 \frac{\mathfrak D_R(v_R,v_R)}{\|v_R\|_{H_R}^2}
 \le(\log R)^CC_4d_4(R),
 \tag{T-19810.14}
\]

and

\[
 \theta_2(\mathfrak D_R,H_R)
 \ge\frac{c_6d_6(R)}{2(\log R)^C}.
 \tag{T-19810.15}
\]

Hence

\[
 \boxed{
 \frac{
 \mathfrak D_R(v_R,v_R)/\|v_R\|_{H_R}^2
 }{
 \theta_2(\mathfrak D_R,H_R)
 }
 \ll(\log R)^C\frac{d_4(R)}{d_6(R)}
 \longrightarrow0.}
 \tag{T-19810.16}
\]

The complete source-map condition number does not occur.

## 5. Exact localized Weil matrix

Let `A_R^U` be the exact localized Weil matrix in source coordinates. Exact
radical-tail factorization uses the same global source vectors and the same
complete tails as `D_R`. The relative operator local-Weyl theorem gives

\[
 \eta_R=
 \frac{
 \|D_R^{-1/2}(A_R^U-(\log R)D_R)D_R^{-1/2}\|
 }{\log R}
 \longrightarrow0
 \tag{T-19810.17}
\]

at a selected support in every large block.

Push forward by exact congruence:

\[
 A_R^V=S_R^{-*}A_R^US_R^{-1}.
 \tag{T-19810.18}
\]

Relative Loewner error is invariant under simultaneous congruence. Therefore

\[
 (1-\eta_R)(\log R)\mathfrak D_R
 \preceq A_R^V
 \preceq
 (1+\eta_R)(\log R)\mathfrak D_R.
 \tag{T-19810.19}
\]

No factor involving `sigma_min(S_R)` appears.

## 6. Finite target and gap

From (T-19810.14),

\[
 \mu_R
 :=\frac{A_R^V(v_R,v_R)}{\|v_R\|_{H_R}^2}
 \le
 (1+\eta_R)(\log R)(\log R)^CC_4d_4(R).
 \tag{T-19810.20}
\]

From (T-19810.15) and (T-19810.19), the second generalized eigenvalue is at
least

\[
 (1-\eta_R)(\log R)
 \frac{c_6d_6(R)}{2(\log R)^C}.
 \tag{T-19810.21}
\]

The target excess divided by the complete gap is therefore

\[
 O\!\left((\log R)^C\frac{d_4(R)}{d_6(R)}\right)+o(1)
 \longrightarrow0.
 \tag{T-19810.22}
\]

The exact finite ground line is eventually simple, lies in the required even
sector, and converges projectively to `v_R` by the Rayleigh-floor theorem.

## 7. Moving-Hardy and Hurwitz conclusion

Combine the projective ground-state convergence with (T-19810.8). After real
normalization, the finite ground-state transforms converge locally uniformly to
`Xi` on every compact centered strip.

The independently reviewed CCM endpoint gives:

1. every finite simple-even ground-state transform is entire with only real
   zeros;
2. the transforms converge locally uniformly to `Xi`.

Hurwitz excludes a nonreal zero of `Xi`. Therefore every nontrivial zero of
zeta lies on the critical line.

Thus, if the load-bearing proposed lemmas cited at the head of this theorem are
correct,

\[
 \boxed{\mathrm{RH}.}
 \tag{T-19810.23}
\]

## 8. Support selection

In every sufficiently large radial block intersect:

- generic nonsingular supports from `L-19847`;
- target-nondegenerate supports;
- endpoint nonresonance from `L-19845`;
- complete alias cross supports from `L-19844`;
- relative local-Weyl supports from `L-19843`.

The first excluded set is countable and the remaining bad sets have relative
measure `o(1)`. The intersection has positive measure. Choose one support from
each block. The choice is non-effective but mathematical.

## 9. Adversarial status

This theorem corrects all three decisive logical defects in `T-19807`:

1. no quarter-power support-translation argument;
2. complete signed gap `d_6`, not `d_8`;
3. no complete quantitative right inverse.

It does **not** make the proof accepted. The following new statements require
independent line-by-line review:

- `L-19823/L-19824`: complete pure signed `d_4,d_6` hierarchy;
- `L-19844/L-19845`: exact mode-dependent WKB/Airy/endpoint/alias bounds;
- `L-19843`: relative operator local-Weyl theorem;
- `L-19847`: generic low-prolate surjectivity, growing analysis bound, and
  target nondegeneracy;
- (T-19810.8): moving-Hardy identification of the arithmetic target.

A defect in any one leaves RH open. No public claim of an accepted RH proof is
made by this proposed composition.
