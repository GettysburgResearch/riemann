# L-21707 — Positive Brownian tail-occupation defect for every cutoff mixture

Claim ID: `L-21707`  
Title: Every positive finite Brownian cutoff mixture differs from the completed zeta factor by the Mellin transform of one explicit nonnegative tail-occupation kernel  
Status: **PROPOSED COMPLETE EXACT THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-21705`; Euler's sine product; the zeta functional equation  
Scope: exact finite/infinite Brownian comparison; no zero-location or RH conclusion

## 1. Positive cutoff mixtures

Let

\[
\lambda_1,\ldots,\lambda_N\ge0,
\qquad
\sum_{K=1}^N\lambda_K=1,
\tag{L-21707.1}
\]

and retain the Brownian gamma truncations

\[
S_K=\sum_{j=1}^K\frac{\Gamma_{2,j}}{j^2},
\qquad
Y_K=\sqrt{S_K/\pi},
\qquad
m_K(s)=\mathbb E[Y_K^s].
\]

Define

\[
m_\lambda(s)=\sum_{K=1}^N\lambda_Km_K(s)
=\pi^{-s/2}\Gamma\!\left(1+\frac s2\right)D_\lambda(s).
\tag{L-21707.2}
\]

This includes the raw cutoff, the logarithmic Nörlund mixture of `L-21706`, and every other positive finite cutoff average.

Put

\[
\omega_K=\left(\frac{\binom{2K}{K}}{4^K}\right)^2
\tag{L-21707.3}
\]

and introduce the entire cardinal functions

\[
\boxed{
 p_K(z)=
 \frac{\Gamma(2K+1)}
 {4^K\Gamma(K+1-z)\Gamma(K+1+z)}.}
\tag{L-21707.4}
\]

They satisfy

\[
p_K(0)^2=\omega_K,
\qquad
p_K(n)=\frac{\binom{2K}{K-n}}{4^K}
\quad(0\le n\le K),
\tag{L-21707.5}
\]

and `p_K(n)=0` for integers `n>K`.

Define the positive cardinal Green profile

\[
\boxed{
G_\lambda(z)=
\sum_{K=1}^N\frac{\lambda_K}{\omega_K}p_K(z)^2.}
\tag{L-21707.6}
\]

Then `G_lambda(0)=1`.

## 2. Exact coefficient collapse

At an integer `1<=n<=K`, logarithmic differentiation gives

\[
\frac{p_K'(n)}{p_K(n)}
=\psi(K-n+1)-\psi(K+n+1)
=-(H_{K+n}-H_{K-n}).
\tag{L-21707.7}
\]

The coefficient of `n^(-s)` in `D_K(s)` from `L-21705` is

\[
4\frac{p_K(n)^2}{\omega_K}
\left[n(H_{K+n}-H_{K-n})+\frac{s-1}{2}\right].
\]

Summing with the weights `lambda_K` therefore gives

\[
\boxed{
D_\lambda(s)
=2\sum_{n=1}^N
\left[(s-1)G_\lambda(n)-nG_\lambda'(n)\right]n^{-s}.}
\tag{L-21707.8}
\]

Equivalently,

\[
\boxed{
D_\lambda(s)
=-2\sum_{n=1}^{\infty}
\left.
\frac{d}{dx}\left(x^{1-s}G_\lambda(x)\right)
\right|_{x=n}.}
\tag{L-21707.9}
\]

The infinite notation is harmless: every summand vanishes for `n>N`.

This is the first exact reduction of every positive Brownian cutoff mixture to one sampled positive Green profile.

## 3. Cardinal product and the positive defect

Euler's product gives

\[
\boxed{
 p_K(z)
 =\sqrt{\omega_K}
 \frac{\sin\pi z}{\pi z}
 \prod_{j=1}^K
 \left(1-\frac{z^2}{j^2}\right)^{-1}.}
\tag{L-21707.10}
\]

Hence, for `y>0`,

\[
\frac{G_\lambda(iy)}{\sinh^2\pi y}
=
\frac1{\pi^2y^2}
\sum_{K=1}^N\lambda_K
\prod_{j=1}^K
\left(1+\frac{y^2}{j^2}\right)^{-2}.
\tag{L-21707.11}
\]

The infinite Euler product is

\[
\frac1{\sinh^2\pi y}
=
\frac1{\pi^2y^2}
\prod_{j=1}^{\infty}
\left(1+\frac{y^2}{j^2}\right)^{-2}.
\tag{L-21707.12}
\]

Every finite product in (L-21707.11) is at least the infinite product. Therefore

\[
\boxed{
A_\lambda(y)
:=
\frac{G_\lambda(iy)-1}{\sinh^2\pi y}
\ge0
\qquad(y>0).}
\tag{L-21707.13}
\]

More explicitly,

\[
\boxed{
A_\lambda(y)
=
\frac1{\pi^2y^2}
\sum_{K=1}^N\lambda_K
\left[
 \prod_{j=1}^K\left(1+\frac{y^2}{j^2}\right)^{-2}
 -
 \prod_{j=1}^{\infty}\left(1+\frac{y^2}{j^2}\right)^{-2}
\right].}
\tag{L-21707.14}
\]

The singular terms cancel at zero, so `A_lambda(y)=O(1)` as `y downarrow0`. The first finite cutoff gives `A_lambda(y)=O(y^-6)` at infinity. Thus

\[
\int_0^\infty A_\lambda(y)y^{1-s}dy
\]

is holomorphic throughout

\[
-4<\operatorname{Re}s<2.
\tag{L-21707.15}
\]

## 4. Exact contour identity

Put

\[
f_s(z)=z^{1-s}G_\lambda(z).
\]

At every positive integer,

\[
\operatorname*{Res}_{z=n}
\frac{f_s(z)}{\sin^2\pi z}
=
\frac{f_s'(n)}{\pi^2}.
\tag{L-21707.16}
\]

Furthermore,

\[
\frac{\pi^2G_\lambda(z)}{\sin^2\pi z}
=
\frac1{z^2}
\sum_{K=1}^N\lambda_K
\prod_{j=1}^K
\left(1-\frac{z^2}{j^2}\right)^{-2},
\tag{L-21707.17}
\]

so the right-half-plane semicircle contributes zero when `-4<Re(s)<0`. Integrating along the imaginary axis and using (L-21707.9) gives

\[
D_\lambda(s)
=-2\pi\sin\frac{\pi s}{2}
\int_0^\infty
\frac{G_\lambda(iy)}{\sinh^2\pi y}
y^{1-s}dy.
\tag{L-21707.18}
\]

Initially this holds for `-4<Re(s)<0`.

The reference integral is

\[
\int_0^\infty
\frac{y^{1-s}}{\sinh^2\pi y}dy
=
4\Gamma(2-s)(2\pi)^{s-2}\zeta(1-s).
\tag{L-21707.19}
\]

The zeta functional equation reduces its contribution exactly to

\[
-2\pi\sin\frac{\pi s}{2}
\int_0^\infty
\frac{y^{1-s}}{\sinh^2\pi y}dy
=2(s-1)\zeta(s).
\tag{L-21707.20}
\]

Subtracting the reference kernel and using analytic continuation inside the common strip yields the central identity

\[
\boxed{
D_\lambda(s)
=2(s-1)\zeta(s)
-2\pi\sin\frac{\pi s}{2}
\int_0^\infty A_\lambda(y)y^{1-s}dy,}
\tag{L-21707.21}
\]

valid throughout

\[
\boxed{-4<\operatorname{Re}s<2.}
\tag{L-21707.22}
\]

No zeta zero, limiting argument, or sign estimate enters this identity.

## 5. Complete monotonicity and Brownian occupation

For `q>0`, write

\[
P_K(q)=\mathbb E[e^{-qS_K}]
=\prod_{j=1}^K\left(1+\frac q{j^2}\right)^{-2}
\]

and

\[
P_\infty(q)=\mathbb E[e^{-qS_\infty}].
\]

Couple every truncation to the same infinite gamma sequence, so `S_K<=S_infinity` almost surely. Equation (L-21707.14) becomes

\[
\pi^2A_\lambda(\sqrt q)
=
\sum_K\lambda_K\frac{P_K(q)-P_\infty(q)}q.
\tag{L-21707.23}
\]

But

\[
\frac{e^{-qS_K}-e^{-qS_\infty}}q
=
\int_{S_K}^{S_\infty}e^{-qx}dx.
\]

Therefore

\[
\boxed{
\pi^2A_\lambda(\sqrt q)
=
\int_0^\infty e^{-qx}b_\lambda(x)dx,}
\tag{L-21707.24}
\]

where the explicit nonnegative occupation density is

\[
\boxed{
b_\lambda(x)
=
\sum_{K=1}^N\lambda_K
\mathbb P(S_K\le x<S_\infty)
\ge0.}
\tag{L-21707.25}
\]

Thus `q mapsto A_lambda(sqrt(q))` is completely monotone. It is not merely pointwise positive.

Taking Mellin transforms in (L-21707.24), and using

\[
\Gamma(1+s/2)\Gamma(1-s/2)
\sin(\pi s/2)=\pi s/2,
\]

gives the exact physical-space remainder

\[
\boxed{
2\xi(s)-m_\lambda(s)
=
\frac{s}{2}\pi^{-s/2}
\int_0^\infty b_\lambda(x)x^{s/2-1}dx,}
\tag{L-21707.26}
\]

again for `-4<Re(s)<2`.

This identifies the finite-to-infinite error as the Mellin transform of the actual Brownian tail occupation between the truncated and complete gamma sums.

## 6. Central-binomial-square Green producer

A particularly rigid choice is

\[
\lambda_K^{\rm cb}
=
\frac{\omega_K}{Z_N},
\qquad
Z_N=\sum_{K=1}^N\omega_K.
\tag{L-21707.27}
\]

Then

\[
\boxed{
G_N^{\rm cb}(z)
=
\frac1{Z_N}\sum_{K=1}^Np_K(z)^2.}
\tag{L-21707.28}
\]

At an integer `n`, `p_K(n)` is the probability that a simple symmetric walk of length `2K` is at displacement `2n`. Hence `G_N^cb` is a normalized truncated diagonal Green profile for two independent walks.

The coefficient formula becomes

\[
\boxed{
D_N^{\rm cb}(s)
=
\frac2{Z_N}
\sum_{n=1}^N
\left[(s-1)G_N(n)-nG_N'(n)\right]n^{-s},}
\tag{L-21707.29}
\]

where `G_N=sum_(K<=N)p_K^2` is unnormalized.

The weights have the elementary lower bound

\[
\omega_K\ge\frac1{4K}.
\tag{L-21707.30}
\]

Indeed `omega_1=1/4`, and

\[
\frac{\omega_{K+1}}{\omega_K}
=\left(\frac{2K+1}{2K+2}\right)^2
\ge\frac K{K+1}.
\]

Therefore `Z_N>=H_N/4`, while `omega_K<=1`. Averaging the bound of `L-21705` gives

\[
\boxed{
|m_N^{\rm cb}(s)-2\xi(s)|
\le
\frac{4\zeta(2)}{H_N}|s|
\qquad(0\le\operatorname{Re}s\le1).}
\tag{L-21707.31}
\]

Thus the central-binomial Green producer converges locally uniformly to `2 xi` and has the same direct Hurwitz endpoint as the logarithmic Nörlund producer.

## 7. What this theorem changes

The finite Brownian route no longer presents the cutoff error as an opaque analytic remainder. It is now one explicit positive object in three equivalent forms:

```text
finite-product deficit on the imaginary axis;
completely monotone Laplace kernel;
Brownian tail-occupation measure between S_K and S_infinity.
```

The central-binomial weights additionally collapse the complete coefficient array to a normalized random-walk Green square.

This does not prove real zeros. Raw cutoffs also have a positive tail-occupation defect and nevertheless develop off-line finite zeros. A successful finite Hermite--Biehler proof must use the detailed cutoff-mixing geometry, not positivity of `A_lambda` alone.

## 8. Proof boundary

Closed here, subject to review:

- cardinal Green coefficient collapse;
- exact right-half-plane contour identity;
- nonnegative and completely monotone defect kernel;
- Brownian occupation representation;
- central-binomial random-walk Green producer;
- elementary critical-strip convergence rate.

Open:

- a zero-free/Hermite--Biehler theorem for the one-sided producer;
- BLNRZ or an analogous real-zero theorem for the central-binomial symmetrization;
- RH.
