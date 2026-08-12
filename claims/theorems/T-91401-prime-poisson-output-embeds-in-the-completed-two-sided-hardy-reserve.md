# T-91401 — The prime Poisson-Fock output embeds explicitly in the completed two-sided Hardy reserve

Claim ID: `T-91401`  
Status: **PROVED EXACT Fock/TANGENT EMBEDDING AND POSITIVE DILATION; SIGNED SCREW GATE OPEN**  
Created: 2026-08-12  
Corrected: 2026-08-12 by `R-91403`  
Depends on: `L-91036`, `L-91306`, `L-91307`, `L-91316`, `L-91401`--`L-91403`, `R-91403`  
RH status: **unproved**

## 1. Explicit prime one-particle and Fock embeddings

Fix

\[
 a>\frac12,
 \qquad
 \sigma=\frac12+a.
\]

Let

\[
 d\mathsf N_\sigma(x)
 =\sum_{p,r\ge1}\frac{p^{-r\sigma}}r
  \delta_{r\log p}(dx)
\]

be Nakamura's positive prime atomic Lévy measure. The ordinary-prime radial
score measure is

\[
 \boxed{
 d\beta_a(x)=a x\,d\mathsf N_\sigma(x).
 }
\tag{T-91401.1}
\]

Therefore

\[
 \boxed{
 (\mathcal I_a^{\rm p}g)(x)=\sqrt{a x}\,g(x)
 }
\tag{T-91401.2}
\]

defines an isometry

\[
 \boxed{
 \mathcal I_a^{\rm p}:
 L^2(\beta_a)\hookrightarrow L^2(\mathsf N_\sigma).
 }
\tag{T-91401.3}
\]

Its symmetric second quantization is the explicit full-Fock embedding

\[
 \boxed{
 \Gamma_s(\mathcal I_a^{\rm p}):
 \Gamma_s(L^2(\beta_a))
 \hookrightarrow
 \Gamma_s(\mathcal S_\sigma),
 }
\tag{T-91401.4}
\]

where

\[
 \mathcal S_\sigma
 =\mathbb C
  \oplus L^2(\nu_\sigma^+)
  \oplus L^2(\nu_\sigma^-)
\tag{T-91401.5}
\]

is the positive two-channel completed source of `L-91402`.

By `L-91036`, the source-linear Hardy tangent reads only the compensated
first-chaos image. Higher prime chaos sectors are nevertheless embedded
isometrically and remain orthogonal unused environment.

## 2. Completed positive source channels

Let `varpi>1` be the plastic constant and `kappa=log(varpi)`. Nakamura's signed
quasi-Lévy measure has the positive Jordan decomposition

\[
 d\nu_\sigma^+
 =d\mathsf N_\sigma
  +q_\sigma(x)\mathbf1_{0<x<\kappa}dx,
\tag{T-91401.6}
\]

\[
 d\nu_\sigma^-
 =-q_\sigma(x)\mathbf1_{x>\kappa}dx,
\tag{T-91401.7}
\]

where

\[
 q_\sigma(x)
 =\frac{e^{-\sigma x}}x
  \left[
   \frac1{1-e^{-2x}}-(1+e^x)
  \right].
\tag{T-91401.8}
\]

Thus the completed source consists explicitly of

```text
prime atoms;
short positive archimedean jumps;
long archimedean jumps carried in a positive metric with negative sign
stored in the observation;
one deterministic Nakamura drift connection.
```

This does not identify the completed xi probability law with one positive
Poisson law; Nakamura proves that law is not infinitely divisible for
`sigma>1`.

## 3. Source-valued completed tangent

Define

\[
 F_t(x)=e^{itx}-1-itx\mathbf1_{x\le1/2},
\]

\[
 G_t(x)=F_t(x)-F_{-t}(x)
 =2i[\sin(tx)-tx\mathbf1_{x\le1/2}].
\]

Put

\[
 s_\sigma=(1,x,-x),
 \qquad
 \mathfrak n_\sigma=\|s_\sigma\|,
 \qquad
 e_\sigma=s_\sigma/\mathfrak n_\sigma,
\]

\[
 v_{\sigma,t}=(-2it\lambda_\sigma',G_t,G_t)
\]

and

\[
 \boxed{
 \mathbf q_a(t)
 =a\mathfrak n_\sigma\Theta_a(t)v_{\sigma,t}.
 }
\tag{T-91401.9}
\]

The norm-one score observation satisfies

\[
 \boxed{
 \langle\mathbf q_a(t),e_\sigma\rangle
 =a\partial_a\Theta_a(t).
 }
\tag{T-91401.10}
\]

At every prime atom `x=r log p>1/2`, the compensation vanishes and the observed
atomic channel is exactly

\[
 \boxed{
 \chi_a^{\rm p}(t)
 =\int(e^{itx}-e^{-itx})d\beta_a(x).
 }
\tag{T-91401.11}
\]

## 4. Completed Hardy colligation

On the common Hardy form core, define

\[
 \mathscr Q_a
 =(P_-\otimes I_{\mathcal S_\sigma})
  M_{\mathbf q_a}P_+,
\]

\[
 H_{m_a}=P_-M_{a\partial_a\Theta_a}P_+.
\]

Then

\[
 H_{m_a}=(I\otimes c_\sigma)\mathscr Q_a.
\tag{T-91401.12}
\]

Let

\[
 \mathscr R_a
 =(I\otimes(I-|e_\sigma\rangle\langle e_\sigma|))
  \mathscr Q_a.
\]

Orthogonal source-fibre decomposition gives

\[
 \boxed{
 \mathscr Q_a^*\mathscr Q_a
 =H_{m_a}^*H_{m_a}
  +\mathscr R_a^*\mathscr R_a.
 }
\tag{T-91401.13}
\]

Since Suzuki's canonical model-space reserve satisfies

\[
 \mathcal J_a^*\mathcal J_a
 =2H_{m_a}^*H_{m_a},
\]

we have the exact positive-dilation identity

\[
 \boxed{
 \mathcal C_a^{\rm abs}
 :=2\mathscr Q_a^*\mathscr Q_a
 =\mathcal J_a^*\mathcal J_a
  +\mathcal D_a^{\rm abs},
 \qquad
 \mathcal D_a^{\rm abs}=2\mathscr R_a^*\mathscr R_a\succeq0.
 }
\tag{T-91401.14}
\]

## 5. Prime tail-Hankel Julia node

After the standard Hardy reflection, the prime visible block is

\[
 (\mathsf H_{\beta_a}g)(t)
 =\int_{u>t}g(u-t)d\beta_a(u).
\tag{T-91401.15}
\]

At `a=4`,

\[
 \beta_4((0,\infty))<\frac{85}{196}<1,
\]

and `L-91307` gives

\[
 \boxed{
 \|g\|^2
 =\|\mathsf H_{\beta_4}g\|^2
 +\|D_0g\|^2+\|D_1g\|^2+\|D_2g\|^2.
 }
\tag{T-91401.16}
\]

Thus the prime first-chaos node has its own completely explicit Julia reserve
inside the completed colligation.

## 6. Delays, orientations, and bridge placement

For a positive delay `S_tau` on `K_(Theta_a)`, define

\[
 T_\tau=P_aS_\tau|_{K_{\Theta_a}},
 \qquad
 R_\tau=M_{\Theta_a}^*S_\tau|_{K_{\Theta_a}}.
\]

Then

\[
 \boxed{
 S_\tau g=T_\tau g+M_{\Theta_a}R_\tau g,
 }
\tag{T-91401.17}
\]

and every mixed-delay cross term splits exactly between resident and leakage
coordinates. The delayed source feature is

\[
 g\longmapsto(\mathscr Q_aT_\tau g,R_\tau g).
\]

Reflection supplies the opposite Hardy orientation. The two Hardy components
of the finite bridge have the same explicit resident/leakage placement.

Consequently the requested embedding component is closed:

\[
 \boxed{
 \Gamma_s(L^2(\beta_a))
 \hookrightarrow
 \Gamma_s(\mathcal S_\sigma)
 \longrightarrow
 \text{completed two-sided delayed Hardy tangent}
 \oplus\text{positive dilation reserve}.
 }
\tag{T-91401.18}
\]

## 7. The positive reserve is not the signed screw defect

Let `mathscr Q_(a,-)` be the long-jump component of `mathscr Q_a`. The natural
source form linear in Nakamura's signed measure is

\[
 \mathcal C_a^{\rm sgn}
 =\mathcal C_a^{\rm abs}
  -4\mathscr Q_{a,-}^*\mathscr Q_{a,-}.
\tag{T-91401.19}
\]

Hence its source-minus-shape form is

\[
 \boxed{
 \mathcal D_a^{\rm sgn}
 =\mathcal D_a^{\rm abs}
  -4\mathscr Q_{a,-}^*\mathscr Q_{a,-}.
 }
\tag{T-91401.20}
\]

This is `R-91403`. The earlier shortcut

```text
positive dilation reserve = delayed zeta screw/Weil defect
```

is therefore withdrawn. It would replace the signed source by its total
variation.

## 8. Correct remaining RH-bearing theorem

Two obligations remain.

### A. Signed source lock

Prove on the full delayed two-sided-plus-bridge core that

\[
 \boxed{
 \mathbb K_a^{\rm del}
 =\mathcal D_a^{\rm sgn,del,bridge}.
 }
\tag{T-91401.21}
\]

This fixes the rational Cauchy mother, deterministic connection, all delay and
orientation cross terms, and the bridge in one Guinand--Weil/Suzuki
normalization.

### B. Long-jump domination

After (T-91401.21), positivity is equivalent to

\[
 \boxed{
 \mathcal D_a^{\rm abs,del,bridge}
 \succeq
 4\mathscr Q_{a,-}^*\mathscr Q_{a,-}.
 }
\tag{T-91401.22}
\]

This is the explicit remaining operator inequality: the positive Julia reserve
must absorb the long-jump archimedean channel after the exact structured
compression.

A finite hostile packet in `X-91402` shows that this domination is not automatic
before the Hardy/model-space/delay/bridge source lock.

If (T-91401.21)--(T-91401.22) hold, the delayed screw Gram is positive and
corrected `T-91008` gives RH. Neither statement has been established.

## 9. Exact boundary

```text
prime one-particle embedding I_a^p                   EXACT
full prime Fock embedding Gamma_s(I_a^p)             EXACT
prime-inclusive completed positive source            EXACT
ordinary-prime tail-Hankel visible block             EXACT
completed tangent score observation                 EXACT
positive two-sided delayed Hardy dilation            EXACT
positive total-variation reserve                     EXACT
positive reserve = signed screw defect               REFUTED
signed quasi-Levy source lock to screw Gram           OPEN
positive reserve >= long-jump channel                OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```
