# T-91401 — The prime Poisson-Fock output embeds explicitly in the completed two-sided Hardy reserve

Claim ID: `T-91401`  
Status: **PROVED EXACT SOURCE-ORDERED Fock/TANGENT EMBEDDING; ZETA-SCREW DEFECT IDENTITY OPEN**  
Created: 2026-08-12  
Depends on: `L-91036`, `L-91306`, `L-91307`, `L-91316`, `L-91401`, `L-91402`, `L-91403`  
RH status: **unproved**

## 1. Statement

Fix any safe scale

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

be Nakamura's positive prime atomic Lévy measure, and let

\[
 d\beta_a(x)=a x\,d\mathsf N_\sigma(x)
\tag{T-91401.1}
\]

be the ordinary-prime logarithmic-radius score measure.

Then multiplication by `sqrt(a x)` gives the explicit one-particle isometry

\[
 \boxed{
 \mathcal I_a^{\rm p}:
 L^2(\beta_a)\hookrightarrow L^2(\mathsf N_\sigma),
 \qquad
 (\mathcal I_a^{\rm p}g)(x)=\sqrt{a x}\,g(x).
 }
\tag{T-91401.2}
\]

Its symmetric second quantization gives

\[
 \boxed{
 \Gamma_s(\mathcal I_a^{\rm p}):
 \Gamma_s(L^2(\beta_a))
 \hookrightarrow
 \Gamma_s(\mathcal S_\sigma),
 }
\tag{T-91401.3}
\]

where

\[
 \boxed{
 \mathcal S_\sigma
 =\mathbb C
  \oplus L^2(\nu_\sigma^+)
  \oplus L^2(\nu_\sigma^-)
 }
\tag{T-91401.4}
\]

is the explicit positive two-channel completed source.

The conclusion-producing first-chaos image has an exact vector-valued Hardy
colligation whose norm-one score observation is Suzuki's complete tangent.
After compressed delays and reflection,

\[
 \boxed{
 \text{prime Poisson-Fock source-linear output}
 \hookrightarrow
 \text{completed two-sided delayed Hardy tangent}
 \oplus
 \text{explicit positive reserve}.
 }
\tag{T-91401.5}
\]

This does not assert that the completed xi probability law is infinitely
divisible. The embedding uses the positive Jordan decomposition of its signed
quasi-Lévy tangent source.

## 2. Explicit completed source channels

Nakamura's safe quasi-Lévy measure has the Jordan decomposition

\[
 d\nu_\sigma=d\nu_\sigma^+-d\nu_\sigma^-.
\]

Let `varpi` be the plastic constant and `kappa=log(varpi)`. Then

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

All source metrics are positive. The channels are:

```text
prime atoms                                  positive;
short archimedean jumps  0<x<log(varpi)     positive;
long archimedean jumps   x>log(varpi)        positive metric,
                                              negative observation sign;
deterministic Nakamura drift                  scalar.
```

The sign of the completion is stored in the score vector, not the Hilbert
metric.

## 3. Exact completed tangent feature

Let

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

and

\[
 v_{\sigma,t}=(-2it\lambda_\sigma',G_t,G_t).
\]

The explicit source-valued symbol

\[
 \boxed{
 \mathbf q_a(t)
 =a\mathfrak n_\sigma\Theta_a(t)v_{\sigma,t}
 }
\tag{T-91401.9}
\]

satisfies

\[
 \boxed{
 \langle\mathbf q_a(t),e_\sigma\rangle
 =a\partial_a\Theta_a(t).
 }
\tag{T-91401.10}
\]

At every prime atom `x=r log p>1/2`, the compensation vanishes and

\[
 a x\frac{p^{-r\sigma}}r
 =a\Lambda(p^r)(p^r)^{-a-1/2}.
\]

Hence the observed atomic channel is exactly

\[
 \boxed{
 \chi_a^{\rm p}(t)
 =\int(e^{itx}-e^{-itx})d\beta_a(x).
 }
\tag{T-91401.11}
\]

## 4. Positive Hardy colligation

Define on the common Hardy form core

\[
 \mathscr Q_a
 =(P_-\otimes I_{\mathcal S_\sigma})
  M_{\mathbf q_a}P_+,
\]

\[
 H_{m_a}=P_-M_{a\partial_a\Theta_a}P_+.
\]

The score observation gives

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

Then

\[
 \boxed{
 \mathscr Q_a^*\mathscr Q_a
 =H_{m_a}^*H_{m_a}
  +\mathscr R_a^*\mathscr R_a.
 }
\tag{T-91401.13}
\]

Since Suzuki's model-space reserve satisfies

\[
 \mathcal J_a^*\mathcal J_a
 =2H_{m_a}^*H_{m_a},
\]

we obtain the completed positive reserve identity

\[
 \boxed{
 2\mathscr Q_a^*\mathscr Q_a
 =\mathcal J_a^*\mathcal J_a
  +2\mathscr R_a^*\mathscr R_a.
 }
\tag{T-91401.14}
\]

## 5. Ordinary-prime tail-Hankel Julia node

After the standard Hardy reflection, the prime visible block is exactly

\[
 (\mathsf H_{\beta_a}g)(t)
 =\int_{u>t}g(u-t)d\beta_a(u).
\tag{T-91401.15}
\]

At `a=4`,

\[
 \beta_4((0,\infty))<\frac{85}{196}<1,
\]

and

\[
 \boxed{
 \|g\|^2
 =\|\mathsf H_{\beta_4}g\|^2
 +\|D_0g\|^2+\|D_1g\|^2+\|D_2g\|^2.
 }
\tag{T-91401.16}
\]

Thus the first-chaos prime node has its own completely explicit local Julia
reserve inside the completed source colligation.

By `L-91036`, the linear Hardy output uses this compensated first-chaos node;
the higher sectors of (T-91401.3) remain orthogonal unused environment.

## 6. Delays, orientations, and bridge placement

For a positive delay `S_tau` on `K_(Theta_a)`, put

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
of the finite bridge are projected into the same resident/leakage geometry.
Their exact coefficient-one screw-defect identification remains open.

## 7. What is and is not completed

Closed exactly:

```text
prime Poisson one-particle space -> completed source atomic channel;
full symmetric-Fock second-quantized embedding;
ordinary-prime score as observed direct summand;
archimedean/pole/theta completion in two positive channels plus drift;
completed model-space tangent observation;
positive source-fibre auxiliary;
two Hardy orientations and compressed positive delays;
bridge geometric placement.
```

Not claimed:

```text
the completed xi probability law is one positive Poisson law;
the constructed positive reserve already equals the zeta screw/Weil defect.
```

## 8. Sole remaining RH-bearing identity

Let

\[
 \mathcal D_a^{\rm QL,del,bridge}
\]

be the joint positive reserve formed from:

```text
2 mathscr R_a*mathscr R_a;
compressed-delay leakage Grams;
reflected-orientation leakage;
finite bridge leakage.
```

The exact remaining theorem is

\[
 \boxed{
 \mathcal D_a^{\rm QL,del,bridge}
 =\mathbb K_a^{\rm del}
 }
\tag{T-91401.18}
\]

on every finite carrier/delay/orientation/bridge packet in the resident
Guinand--Weil/Suzuki normalization.

If (T-91401.18) holds, the delayed screw Gram is positive and corrected
`T-91008` proves RH. The identity has not been established.

## 9. Exact boundary

```text
prime one-particle embedding I_a^p                   EXACT
full prime Fock embedding Gamma_s(I_a^p)             EXACT
completed safe quasi-Levy source split               EXACT
ordinary-prime score as direct positive summand      EXACT
prime tail-Hankel Julia dilation                     EXACT
complete tangent multiplier as score observation    EXACT
completed two-sided delayed Hardy colligation        EXACT
explicit positive reserve                           EXACT
reserve = delayed zeta screw/Weil defect             OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```
