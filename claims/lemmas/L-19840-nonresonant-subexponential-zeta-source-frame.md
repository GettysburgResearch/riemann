# L-19840 — A nonresonant subexponential signed source frame

Claim ID: `L-19840`  
Status: **PROPOSED COMPLETE SOURCE-FRAME THEOREM IN THE LOG-SOURCE METRIC; PROLATE-TAIL COMPATIBILITY IS SEPARATE**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: Mellin factorization for the arithmetic map; the Fourier-coefficient identity for multiplicative periodization; the standard local factorization of `zeta` by the zeros in a unit ordinate window  
Scope: replaces the unnecessarily strong polylogarithmic version of the quantitative source-frame gate by a `lambda^{o(1)}` theorem, which is sufficient against the fixed-mode `d_4/d_6` separation

## 1. Statement

Write

\[
 \ell=\log\mu=2\log\lambda,
 \qquad
 t_k(\ell)=\frac{2\pi k}{\ell},
 \qquad
 |k|\le N_\ell,
 \qquad
 N_\ell\le C_0\ell^2.
 \tag{L-19840.1}
\]

Let

\[
 \mathcal E_{N_\ell}(\ell)
 =\operatorname{span}\{e^{2\pi iky/\ell}:|k|\le N_\ell\}
 \tag{L-19840.2}
\]

with its ordinary Fourier coefficient metric. There are constants `C,c>0`
and, for every sufficiently large `X`, a measurable set

\[
 \mathcal G_X\subset[X,X+1],
 \qquad
 |\mathcal G_X|\ge1-e^{-cX^{1/3}},
 \tag{L-19840.3}
\]

such that for every `ell in mathcal G_X` there is a finite-dimensional real
signed source space

\[
 \mathcal U_{\ell,+}\oplus\mathcal U_{\ell,-}
 \tag{L-19840.4}
\]

of compact-BV even sources satisfying exactly

\[
 f(0)=0,
 \qquad
 \int_{\mathbb R}f=0,
 \tag{L-19840.5}
\]

for which multiplicative periodization of the arithmetic map is an isomorphism
onto the complete finite Fourier space and

\[
 \boxed{
 \sigma_{\min}\!\left(
 P_{N_\ell}\Sigma_{e^\ell}E
 \bigm|
 \mathcal U_{\ell,+}\oplus\mathcal U_{\ell,-}
 \right)
 \ge
 \exp\{-C X^{1/3}\log X\}.}
 \tag{L-19840.6}
\]

The source norm in (L-19840.6) is the `L2` norm of the logarithmic source
profile, equivalently the pullback norm in (L-19840.31) below. The same theorem
holds with any fixed finite number of logarithmic derivatives, at the cost of a
polynomial factor in `X`.

In particular,

\[
 \left\|
 \left(P_{N_\ell}\Sigma_{e^\ell}E\right)^{-1}
 \right\|
 =\exp(o(\ell))
 =\lambda^{o(1)}.
 \tag{L-19840.7}
\]

This is weaker than a fixed polylogarithmic bound but is sufficient in every
composition in which it is multiplied by a fixed power of `d_4/d_6`, because

\[
 d_4/d_6=\lambda^{-4+o(1)}
 \tag{L-19840.8}
\]

in the signed fixed-mode hierarchy.

## 2. A local lower bound for zeta away from its zeros

We use the following standard local-factorization consequence of
`zeta'/zeta`.

**Lemma.** There is `C>0` such that, for `T>=3`, `|t|<=C_1T`, and

\[
 \operatorname{dist}
 \left(\frac12+it,\mathcal Z\right)\ge\delta,
 \qquad
 0<\delta\le\frac14,
 \tag{L-19840.9}
\]

one has

\[
 \boxed{
 \log\left|\zeta\!\left(\frac12+it\right)\right|
 \ge
 -C\log(2+T)\,[1+|\log\delta|].}
 \tag{L-19840.10}
\]

Here `mathcal Z` is the multiset of nontrivial zeros; multiplicity is retained.

### Proof

On a unit rectangle about ordinate `t`, the standard partial-fraction formula is

\[
 \frac{\zeta'}{\zeta}(s)
 =\sum_{|\Im\rho-t|\le2}\frac1{s-\rho}+O(\log(2+T)),
 \tag{L-19840.11}
\]

uniformly after the pole and the two fixed trivial-zero terms are separated.
The Riemann--von Mangoldt formula gives

\[
 \#\{\rho:|\Im\rho-t|\le2\}=O(\log(2+T))
 \tag{L-19840.12}
\]

with multiplicity. Subtract the displayed principal parts and integrate from a
point on `Re s=2`, where `zeta` and `1/zeta` are bounded, to `1/2+it` inside a
fixed enlarged rectangle. The resulting zero-free analytic factor has
logarithm `O(log(2+T))`. Consequently

\[
 \log|\zeta(1/2+it)|
 =
 \sum_{|\Im\rho-t|\le2}
 \log|1/2+it-\rho|
 +O(\log(2+T)),
 \tag{L-19840.13}
\]

where changing every factor by a fixed bounded normalization is absorbed in
the error. Equations (L-19840.9), (L-19840.12), and
`log |1/2+it-rho|>=log delta` prove (L-19840.10). QED.

This proof deliberately uses only the complete local zero count. It assumes no
simplicity and no uniform multiplicity bound.

## 3. Good support lengths

Fix `X` and put

\[
 \delta_X=e^{-X^{1/3}}.
 \tag{L-19840.14}
\]

Delete from `[X,X+1]` every `ell` for which

\[
 \left|rac{2\pi k}{\ell}-\gamma\right|<\delta_X
 \tag{L-19840.15}
\]

for some `|k|<=C_2X^2` and some nontrivial-zero ordinate
`|gamma|<=C_3X+2`.

For fixed `gamma`, the resonant integers whose crossing lies in `[X,X+1]`
form an interval of length `O(|gamma|+1)`. At one such crossing,

\[
 \left|\frac{d}{d\ell}\frac{2\pi k}{\ell}\right|
 =\frac{|\gamma|}{\ell}+O(\delta_X/X),
 \tag{L-19840.16}
\]

so its deleted support interval has length

\[
 O\!\left(\frac{X\delta_X}{|\gamma|+1}\right).
 \tag{L-19840.17}
\]

Summing first over the `O(|gamma|+1)` crossings for one ordinate and then over
the `O(X\log X)` zeros up to height `C_3X+2` gives

\[
 |[X,X+1]\setminus\mathcal G_X|
 \ll X^2\log X\,e^{-X^{1/3}}
 \le e^{-cX^{1/3}}.
 \tag{L-19840.18}
\]

For `ell in mathcal G_X`, every sample in (L-19840.1) is at distance at least
`delta_X` from every zero in its relevant unit window. The local lemma gives

\[
 \boxed{
 \min_{|k|\le N_\ell}
 \left|\zeta\!\left(\frac12-it_k(\ell)\right)\right|
 \ge
 \exp\{-C X^{1/3}\log X\}.}
 \tag{L-19840.19}
\]

The fixed sample `k=0` is harmless because `zeta(1/2)!=0`.

## 4. Exact finite Mellin interpolation

Use the logarithmic Fourier convention

\[
 \widehat g(z)=\int_{\mathbb R}g(y)e^{-izy}\,dy.
 \tag{L-19840.20}
\]

For `|k|<=N_ell`, put

\[
 g_k^0(y)
 =\frac1\ell
  e^{it_k(\ell)y}\,\mathbf1_{[0,\ell]}(y).
 \tag{L-19840.21}
\]

Then, for every integer `j`,

\[
 \widehat g_k^0(t_j)=\delta_{jk}.
 \tag{L-19840.22}
\]

It remains to impose the source integral without changing any periodized
Fourier coefficient. Choose a fixed real
`q in C_c^infty((0,1))` with `widehat q(i/2)!=0` and define

\[
 h_\ell(y)=q(y)-q(y-\ell).
 \tag{L-19840.23}
\]

Its transform is

\[
 \widehat h_\ell(z)
 =(1-e^{-iz\ell})\widehat q(z),
 \tag{L-19840.24}
\]

so

\[
 \widehat h_\ell(t_j)=0
 \quad(j\in\mathbb Z),
 \qquad
 \widehat h_\ell(i/2)
e0.
 \tag{L-19840.25}
\]

Put

\[
 c_\ell=h_\ell/\widehat h_\ell(i/2),
 \qquad
 g_k=g_k^0-\widehat g_k^0(i/2)c_\ell.
 \tag{L-19840.26}
\]

Then exactly

\[
 \widehat g_k(t_j)=\delta_{jk},
 \qquad
 \widehat g_k(i/2)=0.
 \tag{L-19840.27}
\]

The apparently large correction is benign. Indeed

\[
 |\widehat h_\ell(i/2)|\asymp e^{\ell/2},
 \qquad
 \|c_\ell\|_2\ll e^{-\ell/2},
 \tag{L-19840.28}
\]

while

\[
 |\widehat g_k^0(i/2)|
 \ll\frac{e^{\ell/2}}{\ell(1+|t_k|)}.
 \tag{L-19840.29}
\]

Thus the correction has `L2` norm
`O(ell^{-1}(1+|t_k|)^{-1})`. The family
`{sqrt(ell) g_k}` is a rank-one `O(ell^{-1/2})` perturbation of an orthonormal
family. In particular its finite synthesis and analysis bounds are bounded by
fixed constants for large `ell`.

Define on the positive half-line

\[
 f_k(x)=x^{-1/2}g_k(\log x),
 \tag{L-19840.30}
\]

and extend evenly. These sources are compactly supported, BV, zero near the
origin, and (L-19840.27) gives

\[
 f_k(0)=0,
 \qquad
 \int_0^\infty f_k(x)\,dx=0.
 \tag{L-19840.31}
\]

The natural log-source norm is

\[
 \|f\|_{X_\ell}:=
 \|e^{y/2}f(e^y)\|_{L^2(dy)}.
 \tag{L-19840.32}
\]

## 5. Arithmetic map and periodization

The Mellin factorization gives

\[
 \widehat{E(f_k)}(z)
 =\zeta\!\left(\frac12-iz\right)\widehat g_k(z).
 \tag{L-19840.33}
\]

The `j`th Fourier coefficient of multiplicative periodization to the circle of
length `ell` is the value at `t_j`. Hence

\[
 P_{N_\ell}\Sigma_{e^\ell}E(f_k)
 =
 \zeta\!\left(\frac12-it_k\right)e_k.
 \tag{L-19840.34}
\]

For `ell in mathcal G_X`, define

\[
 u_k=
 \frac{f_k}{\zeta(1/2-it_k)}.
 \tag{L-19840.35}
\]

Then

\[
 P_{N_\ell}\Sigma_{e^\ell}E(u_k)=e_k
 \tag{L-19840.36}
\]

exactly. Equations (L-19840.19), (L-19840.28)--(L-19840.32) give

\[
 \left\|\sum a_ku_k\right\|_{X_\ell}
 \le
 \exp\{CX^{1/3}\log X\}
 \left(\sum|a_k|^2\right)^{1/2},
 \tag{L-19840.37}
\]

which is equivalent to (L-19840.6), after an inessential polynomial
normalization of the Fourier basis.

Because `u_-k=conjugate(u_k)`, the real combinations

\[
 u_k^+=u_k+u_{-k},
 \qquad
 u_k^-=i(u_k-u_{-k})
 \tag{L-19840.38}
\]

map respectively to the `+1` and `-1` inversion/Fourier-sign sectors. This
proves the complete signed statement.

## 6. Why a fixed polylogarithmic theorem is not the right gate

Suppose instead that a fixed `C_0` gave the lower bound

\[
 \min_{|k|\le C\ell^2}
 |\zeta(1/2+it_k)|\ge\ell^{-C_0}
 \tag{L-19840.39}
\]

on a nonempty set in every large unit support block. Let
`rho=1/2+i gamma` be a critical-line zero of multiplicity `m` with
`gamma asymp ell`. For every support in the corresponding block some grid point
satisfies

\[
 |t_k-\gamma|\le\pi/\ell.
 \tag{L-19840.40}
\]

Cauchy's estimate for zeta on a fixed small disk, together with the ordinary
polynomial vertical-strip upper bound, gives

\[
 |\zeta(1/2+it_k)|
 \le \ell^{C_1}\left(\frac{C_2}{\ell}\right)^m.
 \tag{L-19840.41}
\]

Combining (L-19840.39)--(L-19840.41) bounds `m` by a constant depending only on
`C_0`. Therefore a fixed polylogarithmic complete multiplier floor contains, as
a consequence, a uniform bound for critical-line zero multiplicities. Such a
bound is not supplied by generic zeta-cycle avoidance.

This does not prove that a polylogarithmic frame is false. It proves that it is
a substantially stronger zero theorem than the reviewed proposal acknowledged.
The subexponential bound above avoids this hidden simplicity/multiplicity gate.

## 7. Exact proof boundary

1. The good-support measure estimate, exact source interpolation, two source
   constraints, signed splitting, and `exp(o(ell))` inverse bound are proved
   here.
2. The theorem is in the explicit logarithmic source norm (L-19840.32). A claim
   in another metric must state and prove the metric adapter.
3. These sources give a complete quantitative arithmetic frame, but their
   omitted tails are not automatically the low prolate radial tails. Thus this
   theorem closes the algebraic/conditioning part of the source-frame gate; it
   does **not** by itself transfer the `d_4,d_6` hierarchy to the same tails.
4. The final positive route needs only `lambda^{o(1)}` conditioning, not the
   rejected stronger polylogarithmic formulation, provided the source/tail
   compatibility and local-Weyl theorems are proved in the same frame.
5. No RH conclusion is claimed by this lemma alone.
