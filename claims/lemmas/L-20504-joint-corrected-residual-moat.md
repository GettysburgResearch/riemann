# L-20504 — Joint one-sided corrected residual is the sharp finite moat

Claim ID: `L-20504`  
Title: Positive omitted-zero mass may pay the complete Schur correction; certify their joint lower LMI instead of adding two worst-case losses  
Status: `PROPOSED — COMPLETE FINITE IDENTITY AND STRICT SEPARATION`  
Authoring agent: `gpt56-03-q`  
Created: 2026-08-01  
Dependencies: `L-20501`, `L-20502`; exact positive-sector Schur complement  
Scope: sharpest finite consumer for the conditional line-zero frame  
Related counterexample candidates: none

## 1. Exact selected-plus-corrected-residual identity

Use the notation of `L-20502`. On the graph kernel \(K_Z\), the selected
simple-line block contributes

\[
P_Y
=
S_{Y\mid Z}^*M_YS_{Y\mid Z}
\succeq0.
\tag{L-20504.1}
\]

Let

\[
R_Y
=
J_Z^*Q_{\mathrm{rem},Y}J_Z
\tag{L-20504.2}
\]

be the complete signed residual after selected-line deflation.

Let \(C_+\succ0\) be the entire already-positive sector and let \(L_K\) be the
complete kernel-to-positive-sector cross. Put

\[
X_K
=
J_Z^*L_K^*C_+^{-1}L_KJ_Z
\succeq0.
\tag{L-20504.3}
\]

The fully corrected kernel is exactly

\[
\boxed{
S_K=P_Y+\mathcal R_{Y\mid Z}^{\rm corr},
\qquad
\mathcal R_{Y\mid Z}^{\rm corr}=R_Y-X_K.
}
\tag{L-20504.4}
\]

Thus the natural residual is already Schur-corrected.

## 2. Joint lower LMI

Assume the conditional selected-line frame

\[
P_Y\succeq\sigma^2G_K,
\qquad
\sigma^2>0,
\tag{L-20504.5}
\]

and certify one directed lower LMI

\[
\boxed{
\mathcal R_{Y\mid Z}^{\rm corr}
\succeq
-\nu G_K,
\qquad
\nu\ge0.
}
\tag{L-20504.6}
\]

Then immediately

\[
\boxed{
S_K\succeq(\sigma^2-\nu)G_K.
}
\tag{L-20504.7}
\]

The exact positive gate is

\[
\boxed{
\sigma^2>\nu.
}
\tag{L-20504.8}
\]

No separate residual or cross estimate is required.

## 3. Relation to the separated adapter

If one has only

\[
R_Y\succeq-\omega G_K
\tag{L-20504.9}
\]

and

\[
X_K\preceq\chi G_K,
\tag{L-20504.10}
\]

then

\[
\mathcal R_{Y\mid Z}^{\rm corr}
=R_Y-X_K
\succeq-(\omega+\chi)G_K.
\]

Therefore

\[
\boxed{
\nu\le\omega+\chi.
}
\tag{L-20504.11}
\]

`L-20502` is a valid modular adapter, while the joint LMI is always at least as
sharp and can be strictly sharper.

## 4. Exact strict separation

Consider a one-dimensional graph kernel with metric \(G_K=1\). Let

\[
P_Y=1,
\qquad
R_Y=\frac9{10},
\qquad
X_K=1.
\tag{L-20504.12}
\]

The exact corrected kernel is

\[
S_K
=1+\frac9{10}-1
=\frac9{10}>0.
\tag{L-20504.13}
\]

### Separated estimate

The best one-sided endpoints are

\[
\omega=0,
\qquad
\chi=1.
\]

Hence the separated lower bound is only

\[
\sigma^2-\omega-\chi
=1-0-1
=0.
\tag{L-20504.14}
\]

It fails to prove strict positivity.

### Joint estimate

The joint corrected residual is

\[
\mathcal R_{Y\mid Z}^{\rm corr}
=\frac9{10}-1
=-\frac1{10},
\]

so

\[
\nu=\frac1{10}.
\]

Equation (L-20504.7) certifies the exact floor

\[
\boxed{
1-\frac1{10}=\frac9{10}>0.
}
\tag{L-20504.15}
\]

Thus positive omitted-zero mass can pay the complete Schur correction. Charging
the two channels separately can lose the proof.

## 5. Möbius representation

Let \(J_Z+T\) be an exact global-radical extension from PR #204. The residual
Weil matrix is invariant:

\[
Q_{\mathrm{rem},Y}(T c,T d)
=
Q_{\mathrm{rem},Y}(J_Zc,J_Zd).
\tag{L-20504.16}
\]

The joint corrected residual can therefore be produced as

\[
\boxed{
\mathcal R_{Y\mid Z}^{\rm corr}
=
Q_{\mathrm{rem},Y}(T,T)
-
J_Z^*L_K^*C_+^{-1}L_KJ_Z.
}
\tag{L-20504.17}
\]

The physical divisor-sum and Mellin Möbius producers independently assemble the
first term. Source optimization may alter the analytic representation and the
cross map, but not the exact Weil residual.

## 6. Optimized conditional moat

For fixed first frame \(Z\), define

\[
\boxed{
\mathfrak J_Z
=
\sup_Y
\left[
\sigma_{Y\mid Z}^2-\nu_{Y\mid Z}
\right],
}
\tag{L-20504.18}
\]

where \(\nu_{Y\mid Z}\) is a directed upper endpoint for the negative part of
the **joint** corrected residual.

The exact finite positive gate is

\[
\boxed{
\mathfrak J_Z>0.
}
\tag{L-20504.19}
\]

Optimizing over first frames gives

\[
\mathfrak J=\sup_Z\mathfrak J_Z.
\tag{L-20504.20}
\]

The cofinal theorem should use \((-\mathfrak J_j)_+\), multiplied by the declared
triangular metric inflation.

## 7. False-RH alternative and logical scope

A captured off-line Xi-cardinal difference retains a fixed negative value after
full positive-sector Schur elimination. Every selected real-zero form vanishes
on its global limit. Therefore false RH forces

\[
\mathfrak J_j< -c
\]

cofinally on a complete form/metric capturing hierarchy, modulo the already
declared finite-section and assembly errors.

Conversely, the existence of a cofinal joint moat is a sufficient
RH-resolving statement. The present lemma does not prove it.

## 8. Proof boundary

- The joint identity and strict separation are exact.
- The joint LMI is the sharpest finite interface in this branch.
- Separate \(\omega\) and \(\chi\) remain useful when independently produced,
  but must not be called necessary.
- No production joint residual has been evaluated.
- No RH proof is claimed.
