# L-19832 — Exact finite-projection radical residual identity and assembly gate

Claim ID: `L-19832`  
Status: **PROVED EXACT IDENTITY; RELATIVE PROJECTION GATE OPEN**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: exact radical-tail factorization `L-16206`; finite CCM Fourier space; absolute zero-side convergence  
Scope: exposes a fifth gate omitted by both `T-19807` and its independent review

## 1. Purpose

The exact source-tail theorem and the finite CCM theorem apply to different
vectors.

For a global arithmetic radical

\[
 J=E(f),
\]

let

\[
 g=P_\lambda J,
 \qquad
 t=(I-P_\lambda)J.
 \tag{L-19832.1}
\]

`L-16206` proves that the localized source form of `g` is exactly the zero-side
form of `t`.

The finite CCM matrix, however, acts on the Fourier truncation

\[
 v=P_Ng\in E_N(\lambda),
 \qquad
 q=(I-P_N)g.
 \tag{L-19832.2}
\]

The equality `QW(g)=QW(t)` does not imply `QW(v)=QW(t)`. The missing correction
is the full residual

\[
 e=J-v=t+q.
 \tag{L-19832.3}
\]

This lemma gives the exact identity and the precise relative gate required to
transfer a source-tail hierarchy to the finite CCM matrix.

## 2. Exact zero-side identity

Let `s` range over centered nontrivial-zero parameters, with multiplicity. Since
`J` is in the weak global Weil radical,

\[
 \widehat J(s)=0.
 \tag{L-19832.4}
\]

Equations (L-19832.1)--(L-19832.3) give

\[
 \widehat t(s)=-\widehat g(s),
 \qquad
 \widehat e(s)=-\widehat v(s),
 \qquad
 \widehat e(s)=\widehat t(s)+\widehat q(s).
 \tag{L-19832.5}
\]

For a finite family of sources, let `A_fin` be the exact finite CCM zero-side
matrix of the vectors `v_j`. Absolute convergence gives, term by term,

\[
 \boxed{
 A_{\rm fin}
 =Z(e,e)
 =Z(t+q,t+q),}
 \tag{L-19832.6}
\]

where

\[
 Z(a,b)_{jk}
 :=\sum_s
 \overline{\widehat a_j(\bar s)}\widehat b_k(s).
 \tag{L-19832.7}
\]

Consequently,

\[
 \boxed{
 A_{\rm fin}
 =A_{\rm tail}+C_{tq}+A_q,}
 \tag{L-19832.8}
\]

with

\[
 A_{\rm tail}=Z(t,t),
 \qquad
 C_{tq}=Z(t,q)+Z(q,t),
 \qquad
 A_q=Z(q,q).
 \tag{L-19832.9}
\]

No sign is available for `C_tq` or `A_q` without RH. The residual is not a
positive ordinary projection error; it is a complete zero-side matrix.

## 3. Ordinary residual Gram

The two pieces `t` and `q` have disjoint physical support:

```text
t lies outside [lambda^-1,lambda],
q lies inside [lambda^-1,lambda].
```

Therefore their ordinary `L2` Gram is exactly

\[
 \boxed{
 D_e=D_t+D_q,}
 \tag{L-19832.10}
\]

where

\[
 D_t=(\langle t_j,t_k\rangle),
 \qquad
 D_q=(\langle q_j,q_k\rangle).
 \tag{L-19832.11}
\]

Thus even at the continuous-density level the finite residual scalarizes against
`D_e`, not automatically against the prolate omitted-tail Gram `D_t`.

## 4. Exact sufficient assembly gate

Assume `D_t` is positive definite. Put

\[
 \theta_R
 :=\|D_t^{-1/2}D_qD_t^{-1/2}\|.
 \tag{L-19832.12}
\]

Then ordinary Cauchy--Schwarz gives

\[
 \left\|
 D_t^{-1/2}
 (\langle t,q\rangle+\langle q,t\rangle)
 D_t^{-1/2}
 \right\|
 \le2\sqrt{\theta_R}.
 \tag{L-19832.13}
\]

Since physical supports are disjoint, the ordinary cross term actually vanishes,
but (L-19832.13) is the form needed for any smooth localization variant.
Equation (L-19832.10) yields

\[
 D_e=D_t^{1/2}(I+Q_R)D_t^{1/2},
 \qquad
 0\preceq Q_R\preceq\theta_RI.
 \tag{L-19832.14}
\]

Hence

\[
 \boxed{
 \theta_R\to0
 \quad\Longrightarrow\quad
 D_e=D_t^{1/2}(I+o_{op}(1))D_t^{1/2}.}
 \tag{L-19832.15}
\]

If a relative local-Weyl theorem is proved for the **full residual** `e`,

\[
 \left\|
 D_e^{-1/2}
 [A_{\rm fin}-(\log R)D_e]
 D_e^{-1/2}
 \right\|=o(\log R),
 \tag{L-19832.16}
\]

then (L-19832.15) transfers it to the prolate tail metric `D_t`.

Therefore the exact finite assembly gate is

\[
 \boxed{
 \|D_t^{-1/2}D_qD_t^{-1/2}\|\longrightarrow0,}
 \tag{L-19832.17}
\]

plus the branch/local-Weyl theorem for `e=t+q` rather than for `t` alone.

## 5. Quantitative form of the gate

Let the pure signed hierarchy have target scale `d_4` and complete next scale
`d_6`. A weaker sufficient condition for ground-state transfer is

\[
 \boxed{
 \|D_t^{-1/2}D_qD_t^{-1/2}\|
 ={o(d_6)\over O(d_4)+d_6}=o(1),}
 \tag{L-19832.18}
\]

on the target-plus-low-complement sector, together with a positive lower floor
on the remaining source directions. Entrywise absolute smallness relative to
ordinary source norm is irrelevant; the comparison must be in the prolate tail
metric.

For one source vector the condition reads simply

\[
 \boxed{
 \|(I-P_N)P_\lambda E(f)\|_2^2
 =o(\|(I-P_\lambda)E(f)\|_2^2).}
 \tag{L-19832.19}
\]

This ratio is not controlled by surjectivity of `P_N\Sigma_\mu E`, nor by the
smallest singular value of that map.

## 6. Why a source-frame bound does not imply the assembly gate

A lower singular-value estimate gives

\[
 \|P_Ng\|\ge c\|f\|_{\rm src}.
\]

It says nothing about

\[
 \|(I-P_N)g\|
\]

and therefore nothing about (L-19832.17). A vector may have a well-conditioned
finite image and still retain a Fourier residual much larger than its
superexponentially small prolate tail. Conversely, a near-kernel in ordinary
source norm may be harmless if its Fourier residual is also small in the
`D_t` metric.

Thus the two gates are logically independent.

## 7. Endpoint scale warning

The unit normalized radial profile has endpoint size as large as `O(R^1/2)`.
At the additive endpoint this corresponds to a localized arithmetic source
boundary layer at frequency scale `R`. A Fourier cutoff of only
`N=O((log R)^2)` cannot be declared relatively complete from ordinary smoothness
or Hermite approximation alone. One needs an exact normalized endpoint/Fourier
coefficient theorem proving (L-19832.17), or a different finite realization.

The target approximation theorem `L-16213` proves only an **absolute** moving
Hardy error tending to zero. It does not prove the superexponentially relative
estimate (L-19832.17).

## 8. Consequence for the review frontier

The four theorems listed in the independent review are not sufficient as stated.
A corrected finite CCM route also needs:

```text
finite-projection assembly:
the high Fourier residual of the localized exact-radical source packet is
negligible in the complete prolate tail metric, and its zero-side branches are
included in the local-Weyl theorem.
```

Equivalently, theorem 4 must be formulated directly for the full residual
`e=E(f)-P_NE(f)`, not merely for the omitted support tail.

## 9. Proof boundary

- Equations (L-19832.6)--(L-19832.17) are exact finite identities and elementary
  operator estimates.
- No estimate of `theta_R` is claimed here.
- The branch analysis in `L-19827/L-19829` controls the omitted Poisson tail; it
  does not yet contain the finite Fourier residual `q`.
- Accordingly, `L-19828` is a source-localized local-Weyl theorem until this
  projection gate is closed. It must not be cited as a complete finite CCM
  theorem without `L-19832.17`.
