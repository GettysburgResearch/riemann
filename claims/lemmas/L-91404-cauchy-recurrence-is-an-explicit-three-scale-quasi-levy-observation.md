# L-91404 — The coefficient-one Cauchy recurrence is an explicit three-scale quasi-Lévy observation

Claim ID: `L-91404`  
Status: **PROVED EXACT DIFFERENTIAL/SOURCE IDENTITY; POSITIVITY OPEN**  
Created: 2026-08-12  
Depends on: `T-91005`, `L-91022`, Nakamura's safe quasi-Lévy formula, `L-91402`  
RH status: **unproved**

## 1. Completed phase and Cauchy gate

For `c>1/2`, put

\[
 \sigma_c=\frac12+c,
 \qquad
 \Theta_c(x)
 =\frac{\xi(\sigma_c+ix)}{\xi(\sigma_c-ix)}.
\tag{L-91404.1}
\]

Let

\[
 p_x(c)=\Re\frac{\xi'}{\xi}(\sigma_c+ix)
\tag{L-91404.2}
\]

and retain the normalized Cauchy quantity of `T-91005`,

\[
 \mathcal N_x(c)
 =\frac12\left[c p_x(c)-c^2\partial_c p_x(c)\right].
\tag{L-91404.3}
\]

Differentiation in the carrier gives

\[
 \boxed{
 \partial_x\log\Theta_c(x)=2i\,p_x(c).
 }
\tag{L-91404.4}
\]

Consequently, with

\[
 \mathscr D_c
 =\frac{c}{4i}
  (1-c\partial_c)\partial_x,
\]

one has the exact phase-tangent identity

\[
 \boxed{
 \mathcal N_x(c)
 =\mathscr D_c\log\Theta_c(x).
 }
\tag{L-91404.5}
\]

Thus the Cauchy gate is a first radial differential observation of Suzuki's
completed boundary phase.

## 2. Exact three-scale recurrence

Let

\[
 \mathcal G_x(c)=\mathcal N_x(2c)-\mathcal N_x(c),
 \qquad
 \mathcal E_x(c)=c^{-4}\mathcal G_x(c).
\]

Then direct algebra gives

\[
\begin{aligned}
 \mathcal E_x(a)-\mathcal E_x(2a)
 =a^{-4}\Bigg[
 &-\mathcal N_x(a)
 +\frac{17}{16}\mathcal N_x(2a)\\
 &-\frac1{16}\mathcal N_x(4a)
 \Bigg].
\end{aligned}
\tag{L-91404.6}

Equivalently,

\[
 \boxed{
 \mathcal E_x(a)-\mathcal E_x(2a)
 =a^{-4}\sum_{r\in\{1,2,4\}}
  \alpha_r\mathscr D_{ra}
  \log\Theta_{ra}(x),
 }
\tag{L-91404.7}
\]

where

\[
 \boxed{
 \alpha_1=-1,
 \qquad
 \alpha_2=\frac{17}{16},
 \qquad
 \alpha_4=-\frac1{16}.
 }
\tag{L-91404.8}
\]

The coefficient-one recurrence is therefore intrinsically a three-safe-scale
completed-phase observation. It is not the defect of one scale by itself.

## 3. Safe quasi-Lévy formula for one scale

For `sigma_c>1`, Nakamura gives

\[
 \log\Xi_{\sigma_c}(x)
 =ix\lambda_{\sigma_c}
  +\int_0^\infty F_x(u)d\nu_{\sigma_c}(u),
\]

with

\[
 F_x(u)=e^{ixu}-1-ixu\mathbf1_{u\le1/2}.
\]

Since

\[
 \Theta_c(x)
 =\frac{\Xi_{\sigma_c}(-x)}{\Xi_{\sigma_c}(x)},
\]

put

\[
 h_x(u)=\cos(xu)-\mathbf1_{u\le1/2}.
\tag{L-91404.9}
\]

Differentiating the quasi-Lévy representation gives

\[
 \boxed{
 p_x(c)
 =-\lambda_{\sigma_c}
  -\int_0^\infty u h_x(u)d\nu_{\sigma_c}(u).
 }
\tag{L-91404.10}
\]

Because

\[
 \partial_c\nu_{\sigma_c}=-u\nu_{\sigma_c}
\]

in the weak measure sense,

\[
 \boxed{
 \mathcal N_x(c)
 =-\frac c2
  \left(\lambda_{\sigma_c}
        -c\lambda_{\sigma_c}'\right)
  -\frac c2\int_0^\infty
  u(1+cu)h_x(u)d\nu_{\sigma_c}(u).
 }
\tag{L-91404.11}
\]

The compensation in `h_x` makes the integral convergent at zero. Formula
(L-91404.11) is an unconditional safe-line source identity.

## 4. Exact three-scale source coefficients

For `r in {1,2,4}`, put

\[
 \sigma_r=\frac12+ra
\]

and

\[
 \boxed{
 \kappa_r
 =-\frac{\alpha_r r}{2a^3}.
 }
\tag{L-91404.12}
\]

Explicitly,

\[
 \boxed{
 \kappa_1=\frac1{2a^3},
 \qquad
 \kappa_2=-\frac{17}{16a^3},
 \qquad
 \kappa_4=\frac1{8a^3}.
 }
\tag{L-91404.13}
\]

Substituting (L-91404.11) into (L-91404.6) yields

\[
\boxed{
\begin{aligned}
 \mathcal E_x(a)-\mathcal E_x(2a)
 =\sum_{r\in\{1,2,4\}}\kappa_r\Bigg[
 &\lambda_{\sigma_r}-ra\lambda_{\sigma_r}'\\
 &+\int_0^\infty
  u(1+rau)h_x(u)d\nu_{\sigma_r}(u)
 \Bigg].
\end{aligned}}
\tag{L-91404.14}
\]

This is the explicit completed quasi-Lévy source formula for the
coefficient-one recurrence.

## 5. Positive Hilbert realization of the observation

Write

\[
 \nu_{\sigma_r}
 =\nu_{\sigma_r}^+-\nu_{\sigma_r}^-.
\]

Define the positive source space

\[
 \boxed{
 \mathcal H_a^{\rm rec}
 =\mathbb C
 \oplus
 \bigoplus_{r\in\{1,2,4\}}
 \left[
  L^2(\nu_{\sigma_r}^+)
  \oplus L^2(\nu_{\sigma_r}^-)
 \right].
 }
\tag{L-91404.15}
\]

For each carrier `x`, define the source feature

\[
 \boxed{
 V_{a,x}
 =\left(
  1,
  \left(
   \sqrt{|\kappa_r|}(1+rau)h_x(u),
   \sqrt{|\kappa_r|}(1+rau)h_x(u)
  \right)_r
 \right).
 }
\tag{L-91404.16}
\]

Define the score vector

\[
 \boxed{
 S_a
 =\left(
  d_a,
  \left(
   \operatorname{sgn}(\kappa_r)
    \sqrt{|\kappa_r|}\,u,
   -\operatorname{sgn}(\kappa_r)
    \sqrt{|\kappa_r|}\,u
  \right)_r
 \right),
 }
\tag{L-91404.17}
\]

where

\[
 d_a
 =\sum_r\kappa_r
  (\lambda_{\sigma_r}-ra\lambda_{\sigma_r}').
\tag{L-91404.18}
\]

Every score component lies in its positive Hilbert fibre because

\[
 \int u^2d\nu_{\sigma_r}^\pm(u)<\infty.
\]

With the inner product linear in the first entry,

\[
 \boxed{
 \mathcal E_x(a)-\mathcal E_x(2a)
 =\langle V_{a,x},S_a\rangle_{\mathcal H_a^{\rm rec}}.
 }
\tag{L-91404.19}
\]

Thus the entire recurrence is an explicit bounded observation of a positive
multi-scale source space. All signs are stored in the score, not in the metric.
This identity does not imply that the observed scalar is nonnegative.

## 6. Exact prime-side replay of the rational residual

At a prime-power atom `u=log n`, the compensation in `h_x` vanishes and

\[
 u\,d\mathsf N_{\sigma_r}(u)
 =\Lambda(n)n^{-1/2-ra}.
\]

The prime part of (L-91404.14) is therefore

\[
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \cos(x\log n)
 \sum_{r\in\{1,2,4\}}
 \kappa_r
 (1+ra\log n)e^{-ra\log n}.
\tag{L-91404.20}
\]

Using (L-91404.13), the inner sum is exactly

\[
 \boxed{
 -2a^{-4}\mathfrak r_a(\log n),
 }
\tag{L-91404.21}
\]

where

\[
\begin{aligned}
 \mathfrak r_a(t)=a\Bigg[
 &-\frac14(1+a|t|)e^{-a|t|}\\
 &+\frac{17}{32}(1+2a|t|)e^{-2a|t|}\\
 &-\frac1{16}(1+4a|t|)e^{-4a|t|}
 \Bigg]
\end{aligned}
\]

is the physical residual kernel of `L-91022`.

Consequently the quasi-Lévy source formula reproduces exactly the prime term
of `T-91005`:

\[
 \boxed{
 -2a^{-4}\sum_{n\ge2}
 \frac{\Lambda(n)}{\sqrt n}
 \mathfrak r_a(\log n)
 \cos(x\log n).
 }
\tag{L-91404.22}
\]

No source type or coefficient is changed.

## 7. Explicit sign table

The measure-channel sign in (L-91404.14) is the product of the scale sign
`sgn(kappa_r)` and the Jordan sign of `nu_plus-nu_minus`. Therefore:

```text
positive source sectors:
  (r=1, nu_plus),
  (r=2, nu_minus),
  (r=4, nu_plus);

negative source sectors:
  (r=1, nu_minus),
  (r=2, nu_plus),
  (r=4, nu_minus).
```

In particular, the middle-scale ordinary-prime atomic channel belongs to the
negative side of the recurrence observation, while the first- and fourth-scale
prime channels belong to the positive side. Their exact recombination is the
causal rational residual of `L-91026`.

## 8. Correct remaining operator theorem

The scalar source lock is now exact. The remaining conclusion-producing step
is to lift (L-91404.19) from scalar carriers to the full Cauchy-wavelet packet
and prove that, after:

```text
Suzuki model-space compression;
compressed delays and their Julia leakage;
both Hardy orientations;
the finite bridge;
the deterministic drift connection;
```

the positive source sectors dominate the negative sectors with coefficient
one.

Equivalently, one must identify the signed source form with the corrected
screw/Weil Gram and prove its positivity. This remains RH-bearing.

## 9. Exact boundary

```text
Cauchy gate as radial phase differential              EXACT
coefficient-one recurrence as three-scale observation EXACT
safe quasi-Levy source formula for N_x(c)             EXACT
positive multi-scale source Hilbert space             EXACT
bounded score observation                             EXACT
exact prime residual kernel replay                    EXACT
full carrier/delay/orientation/bridge source lock      OPEN
positive sectors >= negative sectors                  OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
