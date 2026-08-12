# L-91402 — The completed xi quasi-Lévy source has an explicit positive two-channel score

Claim ID: `L-91402`  
Status: **PROVED EXACT PRIME-INCLUSIVE COMPLETED FIRST-CHAOS SOURCE THEOREM**  
Created: 2026-08-12  
Depends on: Nakamura 2015 source lock; `L-91307`, `R-91402`  
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
 =dN_\sigma+q_\sigma(x)\mathbf1_{0<x<\kappa}dx,
\tag{L-91402.5}
\]

\[
 d\nu_\sigma^-
 =-q_\sigma(x)\mathbf1_{x>\kappa}dx.
\tag{L-91402.6}
\]

Both are positive Lévy measures and their support split is independent of
`sigma`.

Every coefficient in (L-91402.5)--(L-91402.6) contains the factor
`e^(-sigma x)`. Therefore, in the weak measure sense,

\[
 \boxed{
 \partial_\sigma\nu_\sigma^\pm
 =-x\nu_\sigma^\pm.
 }
\tag{L-91402.7}
\]

For the prime atom `x=r log p`, this is the derivative of `p^(-r sigma)/r`.

## 3. Positive score Hilbert space

Define

\[
 \boxed{
 \mathcal S_\sigma
 =\mathbb C
  \oplus L^2(\nu_\sigma^+)
  \oplus L^2(\nu_\sigma^-).
 }
\tag{L-91402.8}
\]

The first coordinate is the deterministic drift channel.  Since

\[
 \int x^2d\nu_\sigma^\pm(x)<\infty,
\tag{L-91402.9}
\]

the vector

\[
 s_\sigma=(1,x,-x)
\tag{L-91402.10}
\]

belongs to `S_sigma`. Put

\[
 N_\sigma=\|s_\sigma\|_{\mathcal S_\sigma},
 \qquad
 e_\sigma=s_\sigma/N_\sigma,
\tag{L-91402.11}
\]

and let

\[
 c_\sigma(v)=\langle v,e_\sigma\rangle
\tag{L-91402.12}
\]

with the inner product linear in its first entry. Then `c_sigma` is a
contraction of norm one.

## 4. Exact radial phase feature

Put

\[
 \boxed{
 G_t(x)=F_t(x)-F_{-t}(x)
 =2i\left[
  \sin(tx)-tx\mathbf1_{x\le1/2}
 \right].
 }
\tag{L-91402.13}
\]

For fixed `t`, `G_t` belongs to both `L2(nu_sigma^+)` and
`L2(nu_sigma^-)`: near zero the linear term cancels and `G_t(x)=O_t(x^3)`,
while for large `x` it is bounded and both measures have exponential tails.

Define

\[
 v_{\sigma,t}
 =\left(-2it\lambda_\sigma',G_t,G_t\right)
 \in\mathcal S_\sigma.
\tag{L-91402.14}
\]

Differentiating (L-91402.2), using (L-91402.7), gives

\[
\begin{aligned}
 \partial_\sigma\log\Theta_a(t)
 &=-2it\lambda_\sigma'
   +\int xG_t(x)d\nu_\sigma^+(x)\\
 &\qquad
   -\int xG_t(x)d\nu_\sigma^-(x).
\end{aligned}
\tag{L-91402.15}
\]

Hence

\[
 \boxed{
 \partial_\sigma\log\Theta_a(t)
 =\langle v_{\sigma,t},s_\sigma\rangle_{\mathcal S_\sigma}.
 }
\tag{L-91402.16}
\]

No zero sum or analytic continuation of an Euler first chaos appears in this
identity; all ingredients are explicit in the safe half-plane.

## 5. Completed source-valued tangent symbol

Define

\[
 \boxed{
 \mathbf q_a(t)
 =aN_\sigma\Theta_a(t)v_{\sigma,t}
 \in\mathcal S_\sigma.
 }
\tag{L-91402.17}
\]

Since `partial_a=partial_sigma`, (L-91402.16) yields

\[
 \boxed{
 c_\sigma(\mathbf q_a(t))
 =a\partial_a\Theta_a(t).
 }
\tag{L-91402.18}
\]

Thus the complete Suzuki tangent multiplier is one norm-one observation of an
explicit positive-metric source feature.

The sign of the quasi-Lévy completion is stored in the score vector
`(1,x,-x)`, not in the Hilbert metric.

## 6. The ordinary-prime score is an orthogonal direct summand

The positive channel decomposes orthogonally as

\[
 L^2(\nu_\sigma^+)
 =L^2(N_\sigma^{\rm prime})
  \oplus
  L^2(q_\sigma\mathbf1_{(0,\kappa)}dx),
\tag{L-91402.19}
\]

because its atomic and continuous parts are mutually singular.

At `x=r log p`, one has `x>log 2>1/2`, so the truncation term in `G_t` vanishes
on every prime atom. Moreover

\[
 a x\frac{p^{-r\sigma}}r
 =a\Lambda(p^r)(p^r)^{-a-1/2}.
\tag{L-91402.20}
\]

Therefore the prime atomic component of (L-91402.15) is exactly

\[
 \boxed{
 a\int G_t(x)x\,dN_\sigma^{\rm prime}(x)
 =\int(e^{itx}-e^{-itx})d\beta_a(x)
 =\chi_a^{\rm p}(t).
 }
\tag{L-91402.21}
\]

This is the ordinary-prime scattering score of `L-91307`.

Consequently

\[
 \boxed{
 \text{ordinary-prime Poisson first chaos}
 \text{ is a direct positive summand of }
 \mathcal S_\sigma.
 }
\tag{L-91402.22}
\]

The remaining source coordinates are explicit:

```text
short-jump archimedean positive channel  0<x<log(varpi);
long-jump archimedean negative channel   x>log(varpi),
                                         stored with positive metric;
deterministic drift channel              C.
```

## 7. Relation to the Fisher source

The positive probability/Fisher realization of `L-91309/L-91316` and the
quasi-Lévy realization here are two different positive source factorizations
of the same completed tangent multiplier.

The present source has one strategic advantage: the actual ordinary-prime
Poisson first chaos is visibly an orthogonal direct summand.  Therefore no
unproved Poisson-to-Fisher probability-law identification is required to embed
the prime output into a completed source feature.

No isometry between the full quasi-Lévy and Fisher fibres is asserted.

## 8. Exact boundary

```text
Nakamura quasi-Levy measure                         IMPORTED EXACT
one plastic-constant sign boundary                 EXACT
positive Jordan channels nu_plus, nu_minus         EXACT
fixed radial score vector (1,x,-x)                 EXACT
completed phase derivative as positive-Hilbert
score observation                                  EXACT
ordinary-prime score as direct positive summand    EXACT
full source-valued tangent symbol q_a              EXACT
Hardy/model-space colligation of q_a               L-91403
source auxiliary = delayed screw/Weil defect       OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVED
```
