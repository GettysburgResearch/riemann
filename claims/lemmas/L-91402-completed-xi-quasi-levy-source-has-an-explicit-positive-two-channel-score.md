# L-91402 — The completed xi quasi-Lévy source has an explicit positive two-channel score

Claim ID: `L-91402`  
Status: **PROVED EXACT PRIME-INCLUSIVE COMPLETED FIRST-CHAOS/Fock-SOURCE THEOREM**  
Created: 2026-08-12  
Depends on: Nakamura 2015 source lock; `L-91036`, `L-91307`, `R-91402`  
RH status: **unproved**

## 1. Safe completed characteristic law

Fix

\[
 a>\frac12,
 \qquad
 \sigma=\frac12+a>1.
\]

Put

\[
 \Xi_\sigma(t)=\frac{\xi(\sigma-it)}{\xi(\sigma)}
\]

and

\[
 \Theta_a(t)
 =\frac{\xi(\sigma+it)}{\xi(\sigma-it)}
 =\frac{\Xi_\sigma(-t)}{\Xi_\sigma(t)}.
\tag{L-91402.1}
\]

Nakamura's Theorem 1.4 gives

\[
 \log\Xi_\sigma(t)
 =it\lambda_\sigma
  +\int_0^\infty F_t(x)d\nu_\sigma(x),
\tag{L-91402.2}
\]

where

\[
 F_t(x)=e^{itx}-1-itx\mathbf1_{x\le1/2},
\tag{L-91402.3}
\]

and

\[
 d\nu_\sigma=d\nu_\sigma^+-d\nu_\sigma^-
\tag{L-91402.4}
\]

is the explicit Jordan split in the Nakamura source lock.

## 2. The two positive channels

Let `varpi>1` solve

\[
 \varpi^3-\varpi-1=0,
 \qquad
 \kappa=\log\varpi.
\]

With

\[
 q_\sigma(x)
 =\frac{e^{-\sigma x}}x
  \left[
   \frac1{1-e^{-2x}}-(1+e^x)
  \right],
\]

one has

\[
 d\nu_\sigma^+
 =d\mathsf N_\sigma
  +q_\sigma(x)\mathbf1_{0<x<\kappa}dx,
\tag{L-91402.5}
\]

\[
 d\nu_\sigma^-
 =-q_\sigma(x)\mathbf1_{x>\kappa}dx,
\tag{L-91402.6}
\]

where

\[
 d\mathsf N_\sigma(x)
 =\sum_p\sum_{r\ge1}
  \frac{p^{-r\sigma}}r\delta_{r\log p}(dx).
\tag{L-91402.7}
\]

Both `nu_sigma^+` and `nu_sigma^-` are positive Lévy measures, and their
support split is independent of `sigma`.

Every coefficient in (L-91402.5)--(L-91402.7) contains the factor
`e^(-sigma x)`. Therefore, in the weak measure sense,

\[
 \boxed{
 \partial_\sigma\nu_\sigma^\pm
 =-x\nu_\sigma^\pm.
 }
\tag{L-91402.8}
\]

## 3. Positive score Hilbert space

Define

\[
 \boxed{
 \mathcal S_\sigma
 =\mathbb C
  \oplus L^2(\nu_\sigma^+)
  \oplus L^2(\nu_\sigma^-).
 }
\tag{L-91402.9}
\]

The scalar coordinate is the deterministic drift channel. Since

\[
 \int x^2d\nu_\sigma^\pm(x)<\infty,
\tag{L-91402.10}
\]

the score vector

\[
 s_\sigma=(1,x,-x)
\tag{L-91402.11}
\]

belongs to `S_sigma`. Put

\[
 \mathfrak n_\sigma
 =\|s_\sigma\|_{\mathcal S_\sigma},
 \qquad
 e_\sigma=s_\sigma/\mathfrak n_\sigma,
\tag{L-91402.12}
\]

and define the norm-one observation

\[
 c_\sigma(v)=\langle v,e_\sigma\rangle.
\tag{L-91402.13}
\]

The inner product is linear in its first entry.

## 4. Exact radial phase feature

Put

\[
 \boxed{
 G_t(x)=F_t(x)-F_{-t}(x)
 =2i\left[
  \sin(tx)-tx\mathbf1_{x\le1/2}
 \right].
 }
\tag{L-91402.14}
\]

For fixed `t`, `G_t` belongs to both positive source fibres: near zero the
linear term cancels and `G_t(x)=O_t(x^3)`, while at infinity both measures have
exponential tails.

Define

\[
 v_{\sigma,t}
 =\left(-2it\lambda_\sigma',G_t,G_t\right)
 \in\mathcal S_\sigma.
\tag{L-91402.15}
\]

Differentiating (L-91402.2), using (L-91402.8), gives

\[
\begin{aligned}
 \partial_\sigma\log\Theta_a(t)
 &=-2it\lambda_\sigma'
   +\int xG_t(x)d\nu_\sigma^+(x)\\
 &\qquad
   -\int xG_t(x)d\nu_\sigma^-(x).
\end{aligned}
\tag{L-91402.16}
\]

Hence

\[
 \boxed{
 \partial_\sigma\log\Theta_a(t)
 =\langle v_{\sigma,t},s_\sigma\rangle_{\mathcal S_\sigma}.
 }
\tag{L-91402.17}
\]

All ingredients are explicit in the safe half-plane; no zero sum or
continuation of a critical Euler vector occurs.

## 5. Completed source-valued tangent symbol

Define

\[
 \boxed{
 \mathbf q_a(t)
 =a\mathfrak n_\sigma\Theta_a(t)v_{\sigma,t}
 \in\mathcal S_\sigma.
 }
\tag{L-91402.18}
\]

Since `partial_a=partial_sigma`,

\[
 \boxed{
 c_\sigma(\mathbf q_a(t))
 =a\partial_a\Theta_a(t).
 }
\tag{L-91402.19}
\]

Thus the complete Suzuki tangent multiplier is one norm-one observation of an
explicit positive-metric source feature. The sign of the quasi-Lévy completion
is stored in the score `(1,x,-x)`, not in the metric.

## 6. Literal one-particle embedding of the prime Poisson source

The positive channel splits orthogonally because its atomic and continuous
parts are mutually singular:

\[
 L^2(\nu_\sigma^+)
 =L^2(\mathsf N_\sigma)
  \oplus
  L^2(q_\sigma\mathbf1_{(0,\kappa)}dx).
\tag{L-91402.20}
\]

For a prime-power atom `x=r log p`,

\[
 a x\frac{p^{-r\sigma}}r
 =a\Lambda(p^r)(p^r)^{-a-1/2}.
\tag{L-91402.21}
\]

Therefore

\[
 \boxed{
 d\beta_a(x)=a x\,d\mathsf N_\sigma(x),
 }
\tag{L-91402.22}
\]

where `beta_a` is the exact ordinary-prime scattering-score measure of
`L-91307`.

Let

\[
 \mathfrak h_a^{\rm p}=L^2(\beta_a),
 \qquad
 \mathfrak h_\sigma^{\rm at}=L^2(\mathsf N_\sigma).
\]

Define

\[
 \boxed{
 (\mathcal I_a^{\rm p}g)(x)=\sqrt{a x}\,g(x).
 }
\tag{L-91402.23}
\]

Then

\[
 \boxed{
 \|\mathcal I_a^{\rm p}g\|_{L^2(\mathsf N_\sigma)}^2
 =\|g\|_{L^2(\beta_a)}^2.
 }
\tag{L-91402.24}
\]

Thus `I_a^p` is an explicit isometric embedding of the prime Poisson
one-particle space into the atomic direct summand of the completed positive
source.

## 7. Symmetric-Fock lift

Let

\[
 \Gamma_s(\mathfrak h)
 =\bigoplus_{m\ge0}\mathfrak h^{\otimes_s m}
\]

be bosonic symmetric Fock space. The second quantization

\[
 \boxed{
 \Gamma_s(\mathcal I_a^{\rm p})
 =\bigoplus_{m\ge0}
  (\mathcal I_a^{\rm p})^{\otimes_s m}
 }
\tag{L-91402.25}
\]

is an isometry

\[
 \boxed{
 \Gamma_s(L^2(\beta_a))
 \hookrightarrow
 \Gamma_s(L^2(\mathsf N_\sigma))
 \hookrightarrow
 \Gamma_s(\mathcal S_\sigma).
 }
\tag{L-91402.26}
\]

It preserves the vacuum and every chaos sector. By `L-91036`, an exactly
source-linear Hardy tangent reads only the compensated first-chaos sector; the
higher sectors remain orthogonal unused environment, but their embedding is
now explicit rather than implicit.

## 8. Prime score as the observed atomic summand

Every prime atom satisfies `x>=log 2>1/2`, so the compensation in `G_t`
vanishes there. The atomic contribution to (L-91402.16), after logarithmic
radial scoring, is

\[
 \boxed{
 a\int G_t(x)x\,d\mathsf N_\sigma(x)
 =\int(e^{itx}-e^{-itx})d\beta_a(x)
 =\chi_a^{\rm p}(t).
 }
\tag{L-91402.27}
\]

This is exactly the ordinary-prime Suzuki scattering score. The remaining
source coordinates are explicit:

```text
short-jump archimedean positive channel  0<x<log(varpi);
long-jump archimedean negative channel   x>log(varpi),
                                         stored with positive metric;
deterministic drift channel              C.
```

## 9. Relation to the Fisher source

The completed probability/Fisher realization of `L-91309/L-91316` and the
quasi-Lévy realization here are different positive factorizations of the same
completed tangent multiplier.

The present source has the decisive structural advantage that the actual prime
Poisson Fock system embeds explicitly through (L-91402.23)--(L-91402.26). No
false identification of the completed probability law with a positive Poisson
law is required.

No isometry between the full quasi-Lévy and Fisher fibres is asserted.

## 10. Exact boundary

```text
Nakamura quasi-Levy measure                           IMPORTED EXACT
one plastic-constant sign boundary                   EXACT
positive Jordan channels nu_plus, nu_minus           EXACT
completed phase derivative as score observation      EXACT
prime score measure d beta=a x d N                    EXACT
prime one-particle embedding I_a^p                    EXACT
full symmetric-Fock lift Gamma_s(I_a^p)               EXACT
prime score as observed atomic summand                EXACT
completed source-valued tangent symbol q_a            EXACT
Hardy/model-space colligation of q_a                  L-91403
source auxiliary = delayed screw/Weil defect          OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
