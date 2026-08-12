# T-91401 — The prime Poisson output embeds explicitly in the completed two-sided Hardy reserve

Claim ID: `T-91401`  
Status: **PROVED EXACT SOURCE-ORDERED TANGENT EMBEDDING; ZETA-SCREW DEFECT IDENTITY OPEN**  
Created: 2026-08-12  
Depends on: `L-91306`, `L-91307`, `L-91316`, `L-91401`, `L-91402`, `L-91403`  
RH status: **unproved**

## 1. Statement

Fix any safe scale

\[
 a>\frac12,
 \qquad
 \sigma=\frac12+a.
\]

There is an explicit positive Hilbert source

\[
 \boxed{
 \mathcal S_\sigma
 =\mathbb C
  \oplus L^2(\nu_\sigma^+)
  \oplus L^2(\nu_\sigma^-)
 }
\tag{T-91401.1}
\]

and an explicit source-valued boundary symbol `q_a(t)` such that:

1. the norm-one observation by the fixed radial score
   \[
    e_\sigma=N_\sigma^{-1}(1,x,-x)
   \]
   recovers the complete Suzuki tangent multiplier
   \[
    c_\sigma(\mathbf q_a(t))=a\partial_a\Theta_a(t);
   \]
2. the positive atomic direct summand
   \[
    L^2(N_\sigma^{\rm prime})
    \subset L^2(\nu_\sigma^+)
   \]
   is exactly the ordinary-prime Poisson first chaos;
3. after radial scoring, that atomic summand has measure
   \[
    a x\,dN_\sigma^{\rm prime}(x)=d\beta_a(x)
   \]
   and its Hardy block is the exact tail-Hankel operator
   `H_(beta_a)`;
4. the remaining source coordinates are explicit short-jump and long-jump
   archimedean channels plus one deterministic drift channel;
5. the resulting vector-valued Hardy Hankel has a positive orthogonal Julia
   auxiliary;
6. compressed positive delays, both Hardy orientations, and the finite bridge
   have explicit resident/leakage coordinates.

Therefore

\[
 \boxed{
 \text{ordinary-prime Poisson first chaos}
 \hookrightarrow
 \text{completed two-sided delayed Hardy tangent}
 \oplus
 \text{explicit positive reserve}.
 }
\tag{T-91401.2}
\]

This is an embedding of the **source-linear output**, not an assertion that the
completed xi probability law is itself positive-Poisson infinitely divisible.

## 2. Explicit source channels

Nakamura's safe quasi-Lévy measure is

\[
 d\nu_\sigma=d\nu_\sigma^+-d\nu_\sigma^-.
\]

Let `varpi` be the plastic constant and `kappa=log(varpi)`. Then

\[
 d\nu_\sigma^+
 =\sum_{p,r}\frac{p^{-r\sigma}}r
  \delta_{r\log p}
  +q_\sigma(x)\mathbf1_{0<x<\kappa}dx,
\tag{T-91401.3}
\]

\[
 d\nu_\sigma^-
 =-q_\sigma(x)\mathbf1_{x>\kappa}dx,
\tag{T-91401.4}
\]

where

\[
 q_\sigma(x)
 =\frac{e^{-\sigma x}}x
  \left[
   \frac1{1-e^{-2x}}-(1+e^x)
  \right].
\tag{T-91401.5}
\]

All source metrics are positive. The quasi-Lévy sign is encoded only in the
observation vector `(1,x,-x)`.

## 3. Explicit completed tangent feature

Let

\[
 F_t(x)=e^{itx}-1-itx\mathbf1_{x\le1/2},
\]

\[
 G_t(x)=F_t(x)-F_{-t}(x)
 =2i[\sin(tx)-tx\mathbf1_{x\le1/2}].
\]

Nakamura's drift is `lambda_sigma`. Put

\[
 v_{\sigma,t}
 =(-2it\lambda_\sigma',G_t,G_t)
\]

and

\[
 \boxed{
 \mathbf q_a(t)
 =aN_\sigma\Theta_a(t)v_{\sigma,t}.
 }
\tag{T-91401.6}
\]

Then

\[
 \boxed{
 \langle\mathbf q_a(t),e_\sigma\rangle
 =a\partial_a\Theta_a(t).
 }
\tag{T-91401.7}
\]

At a prime atom `x=r log p`, one has `x>1/2`, so

\[
 G_t(x)=e^{itx}-e^{-itx}.
\]

Moreover

\[
 a x\frac{p^{-r\sigma}}r
 =a\Lambda(p^r)(p^r)^{-a-1/2}.
\]

Hence the prime observation is exactly the scattering score

\[
 \chi_a^{\rm p}(t)
 =\int(e^{itx}-e^{-itx})d\beta_a(x).
\tag{T-91401.8}
\]

## 4. Positive Hardy colligation

Define

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
\tag{T-91401.9}
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
\tag{T-91401.10}
\]

Since Suzuki's model-space reserve satisfies

\[
 \mathcal J_a^*\mathcal J_a
 =2H_{m_a}^*H_{m_a},
\]

we obtain

\[
 \boxed{
 2\mathscr Q_a^*\mathscr Q_a
 =\mathcal J_a^*\mathcal J_a
  +2\mathscr R_a^*\mathscr R_a.
 }
\tag{T-91401.11}
\]

This is the completed positive reserve identity.

## 5. Ordinary-prime Julia node

On the atomic direct summand, the positive-frequency Hardy block is

\[
 (\mathsf H_{\beta_a}g)(t)
 =\int_{u>t}g(u-t)d\beta_a(u).
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
\tag{T-91401.12}
\]

Thus the prime direct summand itself has a fully explicit local Julia reserve
inside the completed source colligation.

## 6. Delays and orientations

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
\tag{T-91401.13}
\]

and all mixed-delay cross terms split exactly between the resident and leakage
coordinates. Applying `mathscr Q_a` to `T_tau g` and retaining `R_tau g` gives
the delayed source embedding.

Reflection supplies the opposite orientation. The two Hardy components of the
bridge are projected and retained by the same construction.

## 7. What is not claimed

Nakamura proves that `Xi_sigma` is not infinitely divisible for `sigma>1`.
Accordingly, this theorem does not identify the completed probability law with
one positive Poisson law.

Instead, it uses the positive Jordan decomposition of the signed quasi-Lévy
measure. The prime Poisson first chaos is an orthogonal direct summand of the
positive channel, while the sign of the archimedean completion is stored in a
norm-one observation.

Nor does this theorem assert that its positive auxiliary is the zeta
screw/Weil defect.

## 8. Sole remaining RH-bearing identity

Let

\[
 \mathcal D_a^{\rm QL,del,bridge}
\]

be the sum of:

```text
2 R_a*R_a from the quasi-Levy source-fibre complement;
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
\tag{T-91401.14}
\]

on every finite carrier/delay/orientation/bridge packet in the resident
Guinand--Weil/Suzuki normalization.

If (T-91401.14) holds, the delayed screw Gram is positive and corrected
`T-91008` proves RH. The identity has not been established.

## 9. Exact boundary

```text
completed safe quasi-Levy source split                EXACT
positive two-channel score Hilbert space              EXACT
ordinary-prime Poisson first chaos as direct summand  EXACT
prime tail-Hankel Julia dilation                      EXACT
complete tangent multiplier as score observation     EXACT
completed two-sided delayed Hardy colligation         EXACT
explicit positive reserve                            EXACT
reserve = delayed zeta screw/Weil defect              OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
