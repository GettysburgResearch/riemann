# Signed Mertens control of the SHARP activation defect

Status: **Root-reviewed quantitative component lemmas M-A1--M-A9.** The bounds below are derived from an
explicit Mertens hypothesis. Imported zero-free regions are separate
inputs through the proved classical adapter in `ZERO_FREE_MERTENS.md`.
Literal beta, the positive jump T(1)=1, and the extra labelled 67 are
preserved. There is no critical positivity or RH conclusion.

Prior credit: [PR #915](https://github.com/GettysburgResearch/riemann/pull/915),
`standalone/2026-10-10-sextic-critical-core/POLYNOMIAL_CRITICAL_HORIZON.md`
(content SHA-256 `664cffb7738fc9cce5d5bd81916e10e5760dff0072fefeb55a2d96317cf0c4a6`),
already proves the qualitative uniform Mertens expansion and polynomial
horizon (Theorem 1 and Corollary 1.1), its converse zero-free consequence,
and the exact horizon infimum 1/(1-Theta_zeta) (Theorems 2--3). Those
qualitative conclusions are inherited. This file supplies an explicit
inclusive-endpoint identity, a piecewise error bound for every m>=1, and
source-dependent constants 461/24, 49, 45, and 120. It does not supply a
new horizon-index theorem or new zero-free region.

## 1. Exact signed-source hypothesis and activation identity

Assume that for some eta in (1/2,1) and constant C_M,

\[
 |M(y)|\le C_M y^\eta\qquad(y\ge1),\qquad
 M(y)=\sum_{n\le y}\mu(n).
 \tag{M-A1}
\]

The native beta prefix is exactly

\[
 A_\beta(y)=M(y)-M(y/67),\qquad
 |A_\beta(y)|\le C_\beta y^\eta,
 \quad C_\beta=C_M(1+67^{-\eta}),
 \tag{M-A2}
\]

where M(t)=0 for t<1. Its constant therefore covers every endpoint,
including the extra source label and its projection multiplicities.

For m>=1 put a=(m+1)/2 and

\[
 h_m(u)=(1-3\sqrt u/4)^m\mathbf1_{u\le1},\qquad
 B(a)=(1-67^{-a})/\zeta(a).
\]

The scaled native sum is

\[
 Q_m(x)=H_m(x)/(4^m x^{m/2})
       =\sum_{n\le x}\beta(n)n^{-a}h_m(n/x).
\]

For a>=1>eta, signed partial summation converges and gives
B(a)=a integral_1^infinity A_beta(t)t^-a-1 dt, with B(1)=0. For a>1
this is the usual absolutely convergent Euler identity. The integral
converges continuously down to a=1, so its endpoint value is the limit
(1-67^-a)/zeta(a)=0; no absolute convergence at a=1 is asserted.

Partial summation of the active finite sum, retaining its inclusive
endpoint jump h_m(1)=4^-m, yields the exact identity

\[
 Q_m(x)-B(a)=4^{-m}A_\beta(x)x^{-a}
 +\int_1^x A_\beta(t)\left[
 a t^{-a-1}(h_m(t/x)-1)-t^{-a}\frac{d}{dt}h_m(t/x)\right]dt
 -a\int_x^\infty A_\beta(t)t^{-a-1}dt.
 \tag{M-A3}
\]

This follows by integrating the smooth active expression only on [1,x]
and then subtracting the full Dirichlet integral. It remains valid when
x is an integer: the boundary uses A_beta(x), including beta(x), while
the integrals are unchanged by individual endpoint values. Omitting the
first boundary term would erase the native positive activation jump.

## 2. Explicit error for every power m>=1

On 0<u<=1, Bernoulli and direct differentiation give

\[
 0\le1-h_m(u)\le3m\sqrt u/4,\qquad
 \left|\frac{d}{dt}h_m(t/x)\right|
 \le\frac{3m}{8\sqrt{x t}}.
\]

The second inequality uses m>=1 and
(1-3sqrt(t/x)/4)^(m-1)<=1. Inserting (M-A2) into (M-A3), and integrating
the positive tail, proves

\[
 |Q_m(x)-B(a)|\le C_\beta\left[
 \left(4^{-m}+\frac a{a-\eta}\right)x^{\eta-a}
 +\frac{3m(2a+1)}8x^{-1/2}L_{\eta-m/2}(x)\right],
 \tag{M-A4}
\]

where L_d(x)=(x^d-1)/d if d!=0 and L_0(x)=log x. Indeed the finite
integrand is bounded by
C_beta * (3m/8)(2a+1)x^-1/2 t^(eta-a-1/2), whose integral is exactly
x^-1/2 L_(eta-m/2)(x). No sign of the Mertens prefix is assumed.

When 1<=m<2eta, L_d(x)<=x^d/d, giving the simpler bound

\[
 |Q_m(x)-B(a)|\le C_\beta K_\eta(m)x^{\eta-a},\quad
 K_\eta(m)=4^{-m}+\frac a{a-\eta}
                    +\frac{3m(m+2)}{8(\eta-m/2)}.
 \tag{M-A5}
\]

The logarithmic transition at m=2eta and the x^-1/2 bound when m>2eta
are already covered by (M-A4). All hypotheses and denominators are
explicit.

## 3. A uniform near-critical horizon under eta=7/8

Take eta=7/8 and 1<=m<=3/2. The three parts of K_eta(m) are bounded
respectively by 1/4, 8, and 63/4, so K_eta(m)<=24 exactly. A sharper
uniform constant follows from convexity: 4^-m is convex,
a/(a-eta)=1+eta/(a-eta) is convex, and writing d=eta-m/2 gives
m(m+2)/d=4eta(eta+1)/d-(8eta+4)+4d, also convex. Hence K_eta is convex
on this closed interval and is at most its larger endpoint value:
K_eta(1)=45/4, K_eta(3/2)=461/24. Consequently

\[
 \left|\frac{H_m(x)}{4^m x^{m/2}}-B((m+1)/2)\right|
 \le(461/24)C_\beta x^{7/8-(m+1)/2}.
 \tag{M-A6}
\]

For m>1 the main coefficient is positive. Hence a sufficient strict
positivity horizon is

\[
 x>\left[\frac{(461/24)C_\beta}{B((m+1)/2)}\right]^{1/((m+1)/2-7/8)}.
 \tag{M-A7}
\]

Writing epsilon=(m-1)/2 in (0,1/4], the elementary integral test gives
zeta(1+epsilon)<=1+1/epsilon, and 1-67^-(1+epsilon)>=66/67. Therefore

\[
 B(1+\epsilon)\ge\frac{66}{67}\frac{\epsilon}{1+\epsilon}.
\]

Since a-7/8>=1/8 and C_beta>=1, a further fully explicit sufficient
horizon, uniform for 1<m<=3/2, is

\[
 x>\left[\frac{49C_\beta}{m-1}\right]^8
       \quad\Longrightarrow\quad H_m(x)>0.
 \tag{M-A8}
\]

To check the constants, (461/24)*(67/66)*(5/2)=154435/3168<49 and
(1+epsilon)/epsilon=(m+1)/(m-1)<=5/[2(m-1)]. The base is >1, so replacing
the reciprocal exponent by eight enlarges it. This is an explicit eighth-
power sufficient horizon in the native Mertens constant.

At m=1, the sharper specific K_eta(1)=45/4 in (M-A5) gives

\[
 |F(x)|=|H_1(x)|\le45C_\beta x^{3/8},\qquad
 N(Y)\le120C_\beta(Y^{3/8}-1).
 \tag{M-A9}
\]

The first identity uses the literal critical F in `NEGATIVE_MASS.md`;
the second integrates F_-<=|F| against dx/x. No sign or nonnegativity
at the critical power follows.

## 4. Exact import boundary and the remaining source gap

An imported zero-free region Re rho>theta, with theta<7/8, implies
(M-A1) at eta=7/8 by the fully derived classical adapter in
`ZERO_FREE_MERTENS.md`. The adapter supplies existence of C_M, rather
than a computed numerical value. All conclusions above retain that
constant explicitly.

For example, the separately imported refined external scalar

\[
 \theta_{\rm ext}=(1507-2\sqrt{921})/1653<7/8
\]

satisfies the required strict inequality. It is an external zero-free
input, not a theorem established by this packet. Given that input, the
native eighth-power horizon (M-A8) and critical negative-mass bound
(M-A9) follow as component deductions. The sharper eta>theta choice
also gives the previously reviewed exponent bound theta-1/2+epsilon.

More generally, for fixed eta in (1/2,1) and any fixed
0<delta<2eta-1, the constant K_eta(m) is bounded on [1,1+delta]. Since
B(1+epsilon)~(66/67)epsilon, the sufficient horizon from (M-A5) is
O((m-1)^(-1/(1-eta))) as m decreases to one, with a constant depending
on the Mertens hypothesis. From zero-free theta, every power
p>1/(1-theta) is consequently available by choosing eta>theta sufficiently
close to theta and keeping its C_M fixed. No uniform endpoint constant
as eta decreases to theta is assumed.

This signed-source estimate is much stronger near critical power than
the absolute-product activation norm (K8), whose optimized logarithmic
horizon grows at least as log(1/(m-1))/(m-1). Nevertheless (M-A8) still
escapes to infinity as m decreases to one. It leaves an expanding finite
endpoint range unpaid, and (M-A9) controls negative mass without forcing
it to vanish. Thus the imported quasi-RH information does not settle the
native critical positivity/negative-mass source gap.
