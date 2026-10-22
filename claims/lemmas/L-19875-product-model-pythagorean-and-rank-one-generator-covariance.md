# L-19875 — Product-model Pythagorean identity and rank-one generator covariance

Claim ID: `L-19875`  
Status: **PROVED EXACT MODEL-SPACE THEOREM WITH QUANTITATIVE FINITE-SECTION ADAPTER — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: standard Hardy model-space algebra; `L-19868`; `L-19873`  
RH status: **no RH input in the abstract theorem**

## 1. Product model spaces

Work first in the unit disk.  Let `F` and `G` be inner functions and put

\[
 I=FG.
\]

Write

\[
 K_F=H^2\ominus FH^2,
 \qquad
 K_G=H^2\ominus GH^2,
 \qquad
 K_I=H^2\ominus IH^2.
\]

The standard product decomposition is

\[
 \boxed{
 K_I=K_F\oplus F K_G
 }
\tag{L-19875.1}
\]

orthogonally.  Indeed,

\[
 H^2=K_F\oplus FH^2
     =K_F\oplus F K_G\oplus FGH^2.
\]

Define

\[
 \boxed{
 \mathcal W_{F,G}:K_I\longrightarrow K_G\oplus K_F,
 \qquad
 \mathcal W_{F,G}(f+Fg)=(g,f).
 }
\tag{L-19875.2}
\]

Then

\[
 \boxed{
 \|h\|_{K_I}^2
 =\|\mathcal W_{F,G}^{\rm crit}h\|_{K_G}^2
  +\|\mathcal W_{F,G}^{\rm st}h\|_{K_F}^2.
 }
\tag{L-19875.3}
\]

Thus `W_(F,G)` is an explicit coefficient-one Pythagorean unitary.  It is not
a square root of an unspecified positive kernel: its two coordinates are the
orthogonal product-model projections

\[
 \mathcal W^{\rm st}h=P_{K_F}h,
 \qquad
 \mathcal W^{\rm crit}h
 =M_F^*P_{F K_G}h.
\tag{L-19875.4}
\]

## 2. Kernel-vector formula

Let

\[
 k_w^J(z)={1-\overline{J(w)}J(z)\over1-\bar wz}
\]

be the model kernel of an inner function `J`.  The product rule gives

\[
 k_w^{FG}=k_w^F+\overline{F(w)}F k_w^G.
\tag{L-19875.5}
\]

Consequently

\[
 \boxed{
 \mathcal W_{F,G}k_w^{FG}
 =\left(\overline{F(w)}k_w^G,k_w^F\right).
 }
\tag{L-19875.6}
\]

Equation (L-19875.6) makes the unitary completely explicit on a dense set and
is the preferred formula for source-feature and one-node applications.

## 3. Exact backward-shift covariance

Let

\[
 (S^*h)(z)={h(z)-h(0)\over z}
\]

be the Hardy backward shift.  Every model space is `S*`-invariant.  For
`f in K_F` and `g in K_G`,

\[
 \begin{aligned}
 S^*(Fg)
 &=F S^*g+g(0)S^*F.
 \end{aligned}
\tag{L-19875.7}

Therefore

\[
 \boxed{
 \mathcal W_{F,G}S_I^*\mathcal W_{F,G}^{-1}
 =
 \begin{pmatrix}
 S_G^*&0\\
 |S^*F\rangle\langle k_0^G|&S_F^*
 \end{pmatrix}.
 }
\tag{L-19875.8}
\]

Here `g(0)=<g,k_0^G>`.  If

\[
 \mathcal A_{F,G}=S_G^*\oplus S_F^*,
\]

then

\[
 \boxed{
 \mathcal A_{F,G}\mathcal W_{F,G}
 -\mathcal W_{F,G}S_I^*
 =-
 \left|0\oplus S^*F\right\rangle
 \left\langle k_0^G\oplus0\right|
 \mathcal W_{F,G}.
 }
\tag{L-19875.9}
\]

The complete generator failure is exactly one Green boundary row.  There is no
uncontrolled remainder.

## 4. Resolvent and self-adjoint generator form

Let `T` denote the lower-triangular operator in (L-19875.8), and let

\[
 T_0=S_G^*\oplus S_F^*.
\]

For every `zeta` in the common resolvent set,

\[
 \boxed{
 (T-\zeta)^{-1}-(T_0-\zeta)^{-1}
 =
 \begin{pmatrix}
 0&0\\
 -(S_F^*-\zeta)^{-1}|S^*F\rangle
 \langle k_0^G|(S_G^*-\zeta)^{-1}&0
 \end{pmatrix}.
 }
\tag{L-19875.10}
\]

Thus every Möbius/Cayley transform of the model generator differs from the
block-diagonal output generator by one rank-one boundary operator.  In
particular, whenever the inner functions are meromorphic and the corresponding
Clark generators are self-adjoint, their source/output intertwining has the
form required by `L-19873`:

\[
 \boxed{
 A\mathcal W_{F,G}-\mathcal W_{F,G}\Lambda
 =|g\rangle\langle\eta|,
 \qquad R=0.
 }
\tag{L-19875.11}
\]

The vectors `g,eta` are obtained explicitly from the resolvent factors in
(L-19875.10).  The statement remains valid for repeated finite Blaschke factors;
all their internal states belong to `K_F`, while the cross-boundary rank stays
one.

## 5. Half-plane normalization and the node eta=1

Let

\[
 \chi(z)={z-1\over z+1}
\tag{L-19875.12}
\]

be the Cayley map from the right half-plane to the disk.  The interior Cauchy
node `eta=1` maps to the disk origin.  Transporting (L-19875.1)--(L-19875.11)
through the standard Hardy unitary gives the identical statements for
half-plane inner functions.

For the Riemann model, take

\[
 F=\widetilde\Delta_a,
 \qquad
 G=\widetilde\Theta_a,
 \qquad
 I=\widetilde\Delta_a\widetilde\Theta_a,
\tag{L-19875.13}
\]

whenever `Theta_a` is inner.  The two Pythagorean coordinates are precisely the
critical Xi model port and the six-state deterministic stable port.  On the
kernel vector at `eta=1`,

\[
 \boxed{
 \|k_1^{\Delta_a\Theta_a}\|^2
 =\|k_1^{\Theta_a}\|^2
  +\|k_1^{\Delta_a}\|_{\rm congr}^2.
 }
\tag{L-19875.14}
\]

The congruence in the stable term is the explicit diagonal factor already
recorded in `L-91034`.  No hyperbolic coordinate is present in (L-19875.14)
when `Theta_a` itself is inner.

## 6. Compressed delays

Let `T_tau,R_tau` be the resident/leakage compressed-delay pair of `L-91401`:

\[
 S_\tau g=T_\tau g+M_\Theta R_\tau g,
 \qquad
 T_\tau^*T_\tau+R_\tau^*R_\tau=I.
\]

Apply `T_tau` to the critical coordinate of (L-19875.2) and retain `R_tau` as
an orthogonal leakage coordinate.  For every mixed packet,

\[
 \boxed{
 \langle S_{\tau_i}g_i,S_{\tau_j}g_j\rangle
 =\langle T_{\tau_i}g_i,T_{\tau_j}g_j\rangle
  +\langle R_{\tau_i}g_i,R_{\tau_j}g_j\rangle.
 }
\tag{L-19875.15}
\]

Hence the product-model Pythagorean identity is stable under all mixed delays,
reflection to the opposite Hardy orientation, and the two Hardy components of
the finite bridge.

## 7. Quantitative finite-section adapter

Assume an exact global source/model intertwiner has been fixed, and use the
periodized Fourier schedule of `L-19868`:

\[
 N_L=O(L^2).
\]

The global Xi source and every fixed derivative satisfy the same
super-exponential strip bound.  Periodization has exact matching of every
endpoint derivative, and the centered Fourier projector commutes with
logarithmic differentiation.  Therefore each projected source column and its
first generator derivative have error

\[
 O(e^{-cL}).
\tag{L-19875.16}
\]

Let `J_L` be the resulting finite source lift, let `P_L` remove its target
line, and assume the positive quotient form satisfies

\[
 Q_L\succeq q_0 I
\quad\text{on }\operatorname{Ran}P_L
\tag{L-19875.17}
\]

with fixed `q_0>0`; `L-19867` supplies such a floor for the residual pencil.
After extracting the exact rank-one boundary term in (L-19875.11), put

\[
 R_L=AJ_L-J_L\Lambda_L-|g_L\rangle\langle\eta_L|.
\]

Columnwise use of (L-19875.16) gives

\[
 \boxed{
 \|R_LP_LQ_L^{-1/2}\|_{\rm HS}
 \le {C\sqrt{N_L}\over\sqrt{q_0}}e^{-cL}
 =O(Le^{-cL})
 \longrightarrow0.
 }
\tag{L-19875.18}
\]

Outward matrix enclosures add the term
`O(sqrt(N_L)delta_L)`; the schedule `delta_L<=e^(-4L)` of `L-19868` leaves
(L-19875.18) unchanged.

Thus the relative Hilbert--Schmidt source-intertwining estimate requested by
`L-19873` follows automatically from an exact global product-model
intertwiner.  It is not a second RH-sized sign theorem.

## 8. Application to the vertical-defect inequality

In the notation of `L-19873`, the exact model theorem gives

\[
 \rho_L=O(Le^{-cL}).
\]

If the residual form is used with `lambda_L=0`, then the metric-commutator term
`|lambda_L|chi_L` vanishes.  The quotient floor gives `kappa_L=O(1)`.  Hence

\[
 \boxed{
 V_L
 \le {1\over8}(2\kappa_L\rho_L)^2
 =O(L^2e^{-2cL})
 \longrightarrow0.
 }
\tag{L-19875.19}
\]

This is the desired independent finite-Galerkin audit once the global inner
source identification has been proved.

## 9. Proof boundary

The product-model unitary, coefficient-one Pythagorean identity, rank-one
generator covariance and finite-section rate are proved above.

For the Riemann application, the remaining logical input is exactly that the
completed arithmetic source identifies `Theta_a` itself as an inner factor.
Without that input, the crossed-zero Blaschke factor belongs in `F`, and the
Pythagorean output acquires the positive hyperbolic port.  The abstract theorem
does not delete that port by notation.
