# L-19829 — Normalized endpoint and stationary-alias estimates for the complete radial packet

Claim ID: `L-19829`  
Status: **PROPOSED SHARP SCALAR ESTIMATE — PRIMARY-SOURCE NORMALIZATION AUDIT REQUIRED**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Corrected: 2026-08-07 after an internal adversarial notation audit  
Dependencies: exact leakage normalization `L-16217`; integrated Bessel normalization `L-16222`; complex radial Volterra bounds of `L-16229`; fixed mode window `L-16219`  
Scope: closes the two weakest analytic inputs of `L-19827`

## 1. Purpose

The complete branch theorem `L-19827` reduces its most delicate bounds to two
scalar assertions about the canonical unit radial leakage profile:

1. the first endpoint channel and one support derivative are only
   polylogarithmic after exact leakage normalization;
2. the stationary cross term between the first alias and the `k`-th alias is
   summable with total `O(R^-1/2 polylog R)` away from the fold.

This lemma proves those estimates from the normalized Bessel template. It never
uses an absolute compact-source Sobolev norm, which is invalid at the
superexponential prolate scale by `R-16205`.

Throughout,

\[
 R=2\pi\lambda^2,
 \qquad
 n,j\le C(\log R)^2,
 \qquad
 \sigma_n^2,\sigma_j^2
 \le C{(\log R)^2\over R}.
 \tag{L-19829.1}
\]

Let

\[
 \rho_{n,R}(z)
 ={B_{\sigma_n,R}(z)+E_{n,R}(z)
   \over
   \|B_{\sigma_n,R}+E_{n,R}\|_{L^2(1,\infty)}}
 \tag{L-19829.2}
\]

be the canonical unit positive-ray leakage profile of `L-16222`.

## 2. Uniform normalized Bessel bounds

The exact transformed norm comparison of `L-16222` gives

\[
 \|B_{\sigma,R}+E_R\|_2
 =(2R)^{-1/2}
 \left[1+O\left({(\log R)^2\over R}\right)\right]
 \tag{L-19829.3}
\]

uniformly on (L-19829.1). Hence division by the exact leakage norm is equivalent
to multiplication by `sqrt(2R)` up to a relative polylogarithmic `O(R^-1)`
error.

The Bessel template is

\[
 B_{\sigma,R}(z)
 =[(z^2-1)(z^2-\sigma^2)]^{-1/4}
  \xi_\sigma(z)^{1/2}J_0(R\xi_\sigma(z)).
 \tag{L-19829.4}
\]

Use the standard global bound

\[
 |J_0(y)|\le C\min(1,y^{-1/2}),
 \qquad y>0.
 \tag{L-19829.5}
\]

Near `z=1`,

\[
 \xi_\sigma(z)\asymp\sqrt{z^2-1},
 \tag{L-19829.6}
\]

and the algebraic prefactor in (L-19829.4), multiplied by
`xi_sigma^(1/2)`, stays bounded above and below. Therefore

\[
 \boxed{
 |\rho_{n,R}(z)|
 \le C(\log R)^C
 \min\left(R^{1/2},(z^2-1)^{-1/4}\right),
 \qquad 1<z\le2.}
 \tag{L-19829.7}
\]

For `z>=2`, `xi_sigma(z)=z-beta_(sigma)+O(z^-1)` and the large-argument Bessel
bound gives

\[
 \boxed{
 |\rho_{n,R}(z)|
 \le {C(\log R)^C\over z}.}
 \tag{L-19829.8}
\]

The differentiated Volterra equation of `L-16229`, together with
`R partial_R sigma_n^2=O((n+1)/R)`, gives the same estimates for each slowly
varying coefficient after the rapid phases `exp(+-iR xi_sigma)` are extracted:

\[
 \boxed{
 |a_{n,R}^\pm(z)|
 +R|\partial_Ra_{n,R}^\pm(z)|
 +|\partial_za_{n,R}^\pm(z)|
 \le C(\log R)^C.}
 \tag{L-19829.9}
\]

## 3. Exact far-field endpoint expansion

For `z>=2`, the Hankel expansion of `J_0`, inserted into (L-19829.4) and then
normalized by (L-19829.3), gives

\[
 \boxed{
 \rho_{n,R}(z)
 ={a_{n,R}^+(z)e^{iR\xi_n(z)}
   +a_{n,R}^-(z)e^{-iR\xi_n(z)}\over z}
 +q_{n,R}(z),}
 \tag{L-19829.10}
\]

where

\[
 |q_{n,R}(z)|+R|\partial_Rq_{n,R}(z)|
 \le C(\log R)^C
 \left({1\over Rz}+{1\over z^2}\right).
 \tag{L-19829.11}
\]

Equations (L-19829.9)--(L-19829.11) prove that the normalized first endpoint
coefficient and one support derivative are polylogarithmic. In particular, no
factor `d_n^-1/2` remains after the exact radial normalization.

## 4. Collective first endpoint channel

The leading outgoing endpoint contribution from every alias `k>=2` has the form

\[
 {a_{n,R}^+(kz)\over kz}
 e^{iR\xi_n(kz)}.
 \tag{L-19829.12}
\]

After extracting the common asymptotic phase and freezing the slowly varying
coefficient, the scalar alias sum is

\[
 \sum_{k=2}^\infty{e^{ik\theta}\over k}
 =-\log(1-e^{i\theta})-e^{i\theta}
 \tag{L-19829.13}
\]

in `L2` of one period. Parseval gives

\[
 \int_0^{2\pi}
 \left|\sum_{k=2}^\infty{e^{ik\theta}\over k}\right|^2d\theta
 =2\pi\sum_{k=2}^\infty{k^{-2}}.
 \tag{L-19829.14}
\]

Partitioning the radial half-line into phase periods and using the external
`z^-2` weight therefore proves

\[
 \boxed{
 \left\|
 \sum_{k=2}^\infty {a_{n,R}^+(k\cdot)
 e^{iR\xi_n(k\cdot)}\over k(\cdot)}
 \right\|_{L^2(2,\infty)}
 \le C(\log R)^C.}
 \tag{L-19829.15}
\]

The incoming channel is identical. Every remainder in (L-19829.11) is
absolutely summable. Thus the complete endpoint aggregate has a
polylogarithmic `L2` norm in the unit first-alias metric.

For support differentiation one must not differentiate the logarithm in
(L-19829.13). Keep the series termwise. The `k`-th coefficient is `O(k^-1)`, and
one support integration by parts in its `k`-dependent phase contributes another
`k^-1`. Equation (L-19829.9) controls the differentiated slow coefficient.
Hence the complete differentiated endpoint ledger is bounded by

\[
 \sum_{k=2}^\infty k^{-2}<\infty.
 \tag{L-19829.16}
\]

## 5. Exact stationary point for alias `k`

For signs `epsilon,epsilon' in {+1,-1}`, write the branch phase

\[
 \phi_{jnk}^{\epsilon,\epsilon'}(z)
 =\epsilon\xi_{\sigma_j}(z)
  -\epsilon'\xi_{\sigma_n}(kz).
 \tag{L-19829.17}
\]

Opposite signs have no stationary point. For equal signs, put

\[
 a_j=1-\sigma_j^2,
 \qquad a_n=1-\sigma_n^2,
 \qquad u=z^2-1.
\]

Since

\[
 \xi_\sigma'(z)^2
 =1+{1-\sigma^2\over z^2-1},
 \tag{L-19829.18}
\]

the stationary equation, after squaring positive quantities, is

\[
 {a_j\over u}
 =(k^2-1)+{k^2a_n\over k^2u+k^2-1}.
 \tag{L-19829.19}
\]

The left side is strictly decreasing from infinity to zero. The right side is
positive and bounded between `k^2-1` and `k^2+1`. Thus the stationary point is
unique and satisfies

\[
 \boxed{
 {a_j\over k^2+1}
 \le z_{jnk}^2-1
 \le {a_j\over k^2-1}.}
 \tag{L-19829.20}
\]

In particular, `z_jnk-1=Theta(k^-2)` uniformly on the packet.

## 6. Stationary curvature

Differentiation gives

\[
 \xi_\sigma''(z)
 =-{(1-\sigma^2)z
 \over
 (z^2-1)^{3/2}(z^2-\sigma^2)^{1/2}}.
 \tag{L-19829.21}
\]

At (L-19829.20), the first term has magnitude `Theta(k^3)`. Since
`kz_jnk>=2`,

\[
 k^2|\xi_{\sigma_n}''(kz_{jnk})|=O(k^{-1}).
\]

Therefore, for all sufficiently large `R` and every `k>=2`,

\[
 \boxed{
 |(\phi_{jnk}^{\epsilon,\epsilon})''(z_{jnk})|
 \ge c k^3.}
 \tag{L-19829.22}
\]

After the natural rescaling `z-z_jnk=k^-2y`, the derivative ratios entering the
stationary-phase lemma are uniformly polynomial in the mode window.

## 7. Correct branch amplitude estimate for `k<=R`

When `2<=k<=R`, the stationary point satisfies

\[
 R\xi_j(z_{jnk})\asymp R/k\gtrsim1,
\]

so the Bessel function may be resolved into its incoming/outgoing Hankel
branches. The first branch coefficient, including its endpoint algebraic
factor, obeys

\[
 |b_{j,R}^\epsilon(z_{jnk})|
 \le C(\log R)^C k^{1/2},
 \tag{L-19829.23}
\]

while the dilated far-field branch obeys

\[
 |b_{n,R}^{\epsilon}(kz_{jnk})|
 \le {C(\log R)^C\over k}.
 \tag{L-19829.24}
\]

Thus the product of the **slow branch amplitudes**, not the already oscillatory
full profiles, is bounded by

\[
 C(\log R)^C k^{-1/2}.
 \tag{L-19829.25}
\]

The equal-sign branch integral is therefore

\[
 I_{jnk}^{\epsilon}(R)
 =\int
 b_{j,R}^{\epsilon}(z)
 \overline{b_{n,R}^{\epsilon}(kz)}
 e^{iR\phi_{jnk}^{\epsilon,\epsilon}(z)}\chi_k(z)\,dz,
 \tag{L-19829.26}
\]

where `chi_k` is a fixed rescaled cutoff around the unique stationary point.
There is no additional phase inside either `b`.

Equations (L-19829.22)--(L-19829.25) give

\[
 \boxed{
 |I_{jnk}^{\epsilon}(R)|
 \le C R^{-1/2}k^{-2}(\log R)^C,
 \qquad 2\le k\le R.}
 \tag{L-19829.27}
\]

On the nonstationary complement, one integration by parts gives

\[
 \boxed{
 |I_{jnk}^{\rm nonstat}(R)|
 \le C R^{-1}k^{-2}(\log R)^C.}
 \tag{L-19829.28}
\]

## 8. Collective endpoint regime `k>R`

For `k>R`, the formal stationary point lies inside the Bessel endpoint layer
`R xi_j=O(1)`, where splitting `J_0` into two Hankel branches is not uniform.
It must not be treated by (L-19829.26).

Split the first profile into the endpoint layer

\[
 1<z<1+C R^{-2}
\]

and its complement. By (L-19829.7), its `L2` mass in the endpoint layer is
`O(R^-1)`; hence its `L2` norm there is `O(R^-1/2)`. The complete higher-alias
endpoint aggregate has polylogarithmic `L2` norm by (L-19829.15). Cauchy--Schwarz
therefore gives the collective bound

\[
 \boxed{
 |C_{k>R}^{\rm endpoint}|
 \le C R^{-1/2}(\log R)^C.}
 \tag{L-19829.29}
\]

Outside the endpoint layer, the first profile is oscillatory and every
`k>R` phase has derivative bounded below by `c k`. Retaining the aliases
termwise, one integration by parts supplies an additional `k^-1`; the original
endpoint coefficient already contributes `k^-1`. Thus

\[
 \sum_{k>R}|C_k^{\rm outside}|
 \le C R^{-1}\sum_{k>R}k^{-2}(\log R)^C
 \le C R^{-2}(\log R)^C.
 \tag{L-19829.30}
\]

Combining (L-19829.27)--(L-19829.30),

\[
 \boxed{
 \sum_{k=2}^\infty|C_{1,k}(R)|
 \le C R^{-1/2}(\log R)^C.}
 \tag{L-19829.31}
\]

This is the corrected first-versus-rest scalar cross estimate.

## 9. Consequences

Uniformity over `O(log^2 R)` modes and the finite exact-radical frame only
increases the logarithmic power. The complete compact first-versus-rest cross
operator therefore satisfies

\[
 \left\|
 \Delta_R^{-1/2}C_R\Delta_R^{-1/2}
 \right\|
 \le C R^{-1/3}(\log R)^C,
\]

where the weaker `R^-1/3` exponent accommodates the fold. Away from the fold,
(L-19829.31) gives the stronger `R^-1/2` rate.

The endpoint aggregate and square-summable compact aliases give

\[
 H_R^*H_R\preceq(\log R)^C\Delta_R.
\]

These are precisely the two analytic hypotheses of `L-19826` and the two
previously audit-sensitive inputs of `L-19827`.

## 10. Proof boundary

- The stationary location and curvature bounds are exact algebra.
- The corrected proof separates slow branch amplitudes from the full
  oscillatory profile and treats `k>R` collectively in the Bessel endpoint
  layer.
- The powers of `R` and `k`, the collective endpoint summation, and the
  normalized coefficient cancellation follow from the Bessel template.
- The transfer from the exact PSWF to the normalized template inherits the
  uniform complex radial error and support-derivative bounds of
  `L-16222/L-16229/L-19827`.
- Independent review should verify the precise Fourier and radial scale
  conventions before promotion. No RH conclusion is claimed here alone.
