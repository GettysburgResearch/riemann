# L-19862 — Exterior arithmetic cardinals give an exact complete residual gap

Claim ID: `L-19862`  
Status: **PROPOSED COMPLETE ALGEBRAIC/TAIL THEOREM — AFFINE WEIL LOWER BOUND SEPARATE**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-07  
Dependencies: exact Mellin factorization; exact finite Fourier containment `L-19858`; Xi source identity `L-19849`; Xi Fourier cutoff `L-16213`  
Scope: closes the common-reservoir spectral gap left open in the revised review

## 1. Finite space and exactly normalized Xi target

Let

\[
 I_L=[-L/2,L/2],
 \qquad
 V_{L,N}=\operatorname{span}\{e_k:|k|\le N\},
 \qquad
 e_k(t)=L^{-1/2}e^{2\pi ikt/L}.
 \tag{L-19862.1}
\]

Let `J_Xi=E(p_+)` be the exact global arithmetic radical of `L-19849`, normalized
so that its logarithmic Fourier transform is a nonzero real multiple of `Xi`.
Let `Sigma_L` denote logarithmic periodization and put

\[
 v_{L,N}=P_N\Sigma_LJ_{\Xi}\in V_{L,N},
 \qquad
 \nu_{L,N}=\|v_{L,N}\|_2.
 \tag{L-19862.2}
\]

The target projections converge to the nonzero vector `J_Xi`, so

\[
 0<c\le\nu_{L,N}\le C
 \tag{L-19862.3}
\]

for all sufficiently large levels. Define the unit target and its simultaneously
normalized global lift by

\[
 p_{L,N}={v_{L,N}\over\nu_{L,N}},
 \qquad
 \widetilde J_{\Xi,L,N}={J_{\Xi}\over\nu_{L,N}}.
 \tag{L-19862.4}
\]

Then

\[
 P_N\Sigma_L\widetilde J_{\Xi,L,N}=p_{L,N}
 \tag{L-19862.5}
\]

exactly. Its exact global residual is

\[
 W_*=\widetilde J_{\Xi,L,N}-\iota_Lp_{L,N}
 ={J_{\Xi}-\iota_Lv_{L,N}\over\nu_{L,N}},
 \tag{L-19862.6}
\]

where `iota_L` is zero extension from `I_L`.

## 2. Target residual tends to zero at any prescribed exponential rate

Before division by `nu_(L,N)`, decompose

\[
 J_{\Xi}-\iota_Lv_{L,N}
 =\bigl[J_{\Xi}-\iota_L\Sigma_LJ_{\Xi}\bigr]
  +\iota_L(I-P_N)\Sigma_LJ_{\Xi}.
 \tag{L-19862.7}
\]

The first bracket consists of the exterior support tail and its complete folded
copies. The logarithmic Xi source is Schwartz and in fact has faster-than-
exponential tails in every fixed Hardy strip. For every `B>0`,

\[
 \left\|J_{\Xi}-\iota_L\Sigma_LJ_{\Xi}\right\|_2
 \le C_Be^{-BL}.
 \tag{L-19862.8}
\]

The coefficient theorem `L-16213` gives

\[
 \left\|(I-P_N)\Sigma_LJ_{\Xi}\right\|_2^2
 \le C L^C\exp\!\left(-{\pi^2N\over L}\right)+C_Be^{-BL},
 \tag{L-19862.9}
\]

up to the fixed convention factor between full and half interval length.
Consequently, for every prescribed `B>0`, choosing

\[
 N_L=\lceil c_BL^2\rceil
 \tag{L-19862.10}
\]

with sufficiently large fixed `c_B`, and using (L-19862.3), gives

\[
 \boxed{
 m_L:=\|W_*\|_2^2\le C_Be^{-BL}.}
 \tag{L-19862.11}
\]

The same choice gives convergence in every moving Hardy norm with
`tau_L->1/2` after increasing `c_B` once more.

## 3. Exterior-supported exact character sources

Fix a small constant `a>0`. Translate the smooth differential cardinals of
`L-19819` so that their logarithmic source profiles are supported inside

\[
 [-3L/2-3a,-L/2-a].
 \tag{L-19862.12}
\]

Translation multiplies every Mellin sample by a known unimodular phase; absorb
that phase into the cardinal normalization. The differential factor still gives
exactly

\[
 \widehat q_k(2\pi j/L)=\delta_{kj},
 \qquad
 \widehat q_k(i/2)=0.
 \tag{L-19862.13}
\]

Let

\[
 f_k(e^t)=e^{-t/2}q_k(t)
 \tag{L-19862.14}
\]

on the positive half-line and extend evenly. These sources are smooth, compactly
supported away from zero, and satisfy

\[
 f_k(0)=0,
 \qquad
 \int_{\mathbb R}f_k=0.
 \tag{L-19862.15}
\]

At a support for which

\[
 \zeta\!\left(\frac12-{2\pi ik\over L}\right)\ne0
 \qquad(|k|\le N),
 \tag{L-19862.16}
\]

define the normalized source by dividing by this finite nonzero multiplier.
Its arithmetic image `J_k=E(f_k)` satisfies

\[
 \boxed{\Sigma_LJ_k=e_k.}
 \tag{L-19862.17}
\]

Because every positive-half source is supported below `exp(-L/2-a)`,

\[
 \boxed{J_k(t)=0\quad(t\ge-L/2).}
 \tag{L-19862.18}
\]

In particular, `J_k` vanishes identically on the central cell `I_L`.

The good-support construction of `L-19840` supplies a relative-`1-o(1)` set in
every large unit `L`-block on which (L-19862.16) holds simultaneously and the
source synthesis has subexponential graph norm. Exact containment `L-19858`
provides the same algebra without a quantitative norm.

## 4. One common onto reservoir

Let

\[
 C_{L,N}=p_{L,N}^{\perp}\subset V_{L,N}
 \tag{L-19862.19}
\]

and choose an ordinary orthonormal basis `w_1,...,w_(d-1)` of this complement.
Using (L-19862.17) linearly, choose exterior arithmetic images `J_(w_j)` with

\[
 \Sigma_LJ_{w_j}=w_j,
 \qquad
 J_{w_j}|_{I_L}=0.
 \tag{L-19862.20}
\]

Define the finite source reservoir

\[
 \mathcal U_{L,N}
 =\operatorname{span}\{\widetilde J_{\Xi,L,N},
 J_{w_1},\ldots,J_{w_{d-1}}\}
 \tag{L-19862.21}
\]

and the exact finite output map

\[
 S_{L,N}\widetilde J_{\Xi,L,N}=p_{L,N},
 \qquad
 S_{L,N}J_{w_j}=w_j.
 \tag{L-19862.22}
\]

This map is an isomorphism onto the complete finite CCM space. Thus exact finite
surjectivity and the target source occur in one reservoir with no scalar
mismatch.

## 5. Exact complete residual form

For `w in C_(L,N)`, let `J_w` be the corresponding exterior arithmetic image.
The exact residual of its finite vector is

\[
 W_w=J_w-\iota_Lw.
 \tag{L-19862.23}
\]

The two terms have disjoint physical supports, so

\[
 \boxed{
 \|W_w\|_2^2
 =\|J_w\|_2^2+\|w\|_2^2
 \ge\|w\|_2^2.}
 \tag{L-19862.24}
\]

Let `D_(L,N)` be the residual Gram on the output coordinates, defined by the
linear synthesis

\[
 W(ap+w)=aW_*+W_w.
 \tag{L-19862.25}
\]

The compression of `D_(L,N)` to the codimension-one target complement obeys

\[
 \boxed{D_{L,N}|_{C_{L,N}}\succeq I.}
 \tag{L-19862.26}
\]

Cauchy interlacing therefore gives

\[
 \boxed{\theta_2(D_{L,N})\ge1.}
 \tag{L-19862.27}
\]

No control of the cross block with `W_*` is required. It may be arbitrarily
large subject only to positivity of the Gram; a codimension-one compression
floor already forces the second full eigenvalue above one.

On the exactly normalized target line,

\[
 \boxed{D_{L,N}(p_{L,N})=m_L\le C_Be^{-BL}.}
 \tag{L-19862.28}
\]

Thus the common-reservoir target/gap ratio satisfies

\[
 \boxed{
 {D_{L,N}(p_{L,N})\over\theta_2(D_{L,N})}
 \le C_Be^{-BL}.}
 \tag{L-19862.29}
\]

This resolves the common-reservoir spectral objection raised in the revised
review. The gap is constant rather than `d_6`.

## 6. Exact finite radical identity

Each reservoir vector is the finite image of a global arithmetic radical. Let
`W` denote its complete global-minus-finite residual. Polarization of radicality
gives

\[
 \boxed{
 Q_W(v,z)=Q_W(W_v,W_z)
 \qquad(v,z\in V_{L,N}).}
 \tag{L-19862.30}
\]

Thus `D_(L,N)` is the ordinary positive metric naturally paired with the exact
finite Weil matrix. No omitted finite-projection term is being ignored.

## 7. What this theorem changes

The finite route no longer needs to prove that the exact character sources
inherit the pure low-prolate `d_4,d_6` hierarchy. Instead:

```text
one exactly normalized Xi lift gives exponentially small residual energy;
all complement character lifts are exterior supported;
their residuals contain an exact orthonormal interior copy;
therefore the complete complement floor is at least one.
```

This is stronger and algebraically simpler than the previously proposed hybrid.

## 8. Proof boundary

- The target residual estimate, exterior cardinal construction, exact onto map,
  disjoint-support identity, and interlacing argument are proved.
- The theorem does **not** prove a lower bound for the indefinite Weil form.
- The remaining RH-bearing input is precisely an affine one-sided estimate
  comparing the exact finite Weil matrix to this explicit residual Gram, plus a
  target-line upper bound. That analytic adapter is isolated in `L-19865`.
- No accepted proof of RH is claimed here.