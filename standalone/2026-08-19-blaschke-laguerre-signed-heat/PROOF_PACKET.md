# T99100 — Blaschke–Laguerre signed heat packet

**Scientific status: the Riemann Hypothesis remains unproved.**

Frozen parent: PR #623 at `712412e286cc309bbe9960ee839df158316df9e5`.

## 1. Lossless critical-line pole centering

Put

\[
z=s-\frac12,\qquad a=\frac12,
\qquad J(z)=\frac{z-a}{z+a}=\frac{s-1}{s}.
\]

On the critical boundary `z=it`, `|J(it)|=1`, while `J(a)=0`. Thus `J` is
the one-zero inner factor for the half-plane `Re z>0`.

For `f in C_c^infty(0,infinity)`, define

\[
(V_af)(u)=\int_0^u e^{-a(u-v)}f(v)\,dv,
\qquad U_af=f-2aV_af.
\]

If `Lf(z)=integral_0^infinity e^{-zu}f(u)du`, then

\[
\boxed{L(U_af)(z)=J(z)Lf(z).}
\tag{1}
\]

Writing `y=V_af` gives

\[
f=y'+ay,\qquad U_af=y'-ay,
\]

and hence

\[
|f|^2-|U_af|^2=2a\frac d{du}|y|^2.
\tag{2}
\]

Because `y(0)=y(infinity)=0`,

\[
\boxed{\|U_af\|_2=\|f\|_2.}
\tag{3}
\]

The direction is important. If `B` vanishes at `s=1`, its centered quotient
`C=B/J` is obtained by the inverse of `U_a` on its range, and `U_af_C=f_B`.
Thus multiplication by `J` puts the real zero back; division by `J` removes it.

For

\[
B_\diamond(s)=\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)},
\]

the quotient

\[
C_\diamond(s)=\frac{s}{s-1}B_\diamond(s)=\frac{B_\diamond(s)}{J(s)}
\tag{4}
\]

is holomorphic and nonzero at `s=1`, with value `3/8`. At every nontrivial
zeta zero `rho`, the factor `rho/(rho-1)` is finite and nonzero, so (4) removes
only the deterministic real carrier.

## 2. Exact monotone-heat square function

Let `g>=0` be absolutely continuous, nonincreasing, and tend to zero. Integrating
(2) by parts gives

\[
\boxed{
\int_0^\infty g(u)(|f(u)|^2-|U_af(u)|^2)\,du
=-2a\int_0^\infty g'(u)|V_af(u)|^2\,du\ge0.
}
\tag{5}
\]

Thus undoing the real zero has a precise positive heat-energy cost. Iterating,

\[
\boxed{
E_g(f)-E_g(U_a^Mf)
=-2a\sum_{j=0}^{M-1}\int_0^\infty
 g'(u)|V_aU_a^jf(u)|^2\,du.
}
\tag{6}
\]

For `g_T(u)=exp(-u^2/(2T))`,

\[
\boxed{
E_T(f)-E_T(U_a^Mf)
=\frac{2a}{T}\sum_{j=0}^{M-1}\int_0^\infty
u e^{-u^2/(2T)}|V_aU_a^jf(u)|^2\,du.
}
\tag{7}
\]

In (7), the first factor in the integrand is the ordinary real variable `u`.
Every summand is positive and source owned.

If a packet has a pole at

\[
z_\rho=\rho-\frac12=\delta+i\gamma,\qquad\delta>0,
\]

then `U_a^M` multiplies its principal coefficient by `J(z_rho)^M`, where

\[
|J(z_\rho)|^2=
\frac{(\delta-a)^2+\gamma^2}{(\delta+a)^2+\gamma^2}<1.
\tag{8}
\]

For every `M(T)=o(T)`, this changes the pole contribution only by `e^{o(T)}`;
its heat type `e^{2 delta^2 T}` survives.

## 3. Sharp filter-only barrier

One might take `M=kappa T+o(T)` and try to suppress a right
absolute-convergence contour while retaining the pole. This cannot work without
a critical-side arithmetic estimate.

For `x>0`, define

\[
h_\gamma(x)=-\log\left|
\frac{x-1/2+i\gamma}{x+1/2+i\gamma}\right|
=\frac12\log\frac{(x+1/2)^2+\gamma^2}{(x-1/2)^2+\gamma^2}.
\]

Direct differentiation gives

\[
h_\gamma'(x)=
\frac{\gamma^2+1/4-x^2}
{((x+1/2)^2+\gamma^2)((x-1/2)^2+\gamma^2)},
\tag{9}
\]

so `h_gamma` is increasing on `0<x<=1` at every nontrivial zeta ordinate.
The Gaussian/inner-factor rate on `Re z=x` is

\[
\Phi_\kappa(x)=x^2-\kappa h_\gamma(x).
\]

Pole dominance over the critical boundary requires

\[
\kappa<\frac{\delta^2}{h_\gamma(\delta)}.
\tag{10}
\]

Pole dominance over the absolute-convergence line `Re s=3/2`, i.e. `x=1`,
requires

\[
\kappa>\frac{1-\delta^2}{h_\gamma(1)-h_\gamma(\delta)}.
\tag{11}
\]

But

\[
h_\gamma(1)\le\frac1{\gamma^2},
\qquad
h_\gamma(\delta)\ge
\frac{\delta}{\gamma^2+(\delta+1/2)^2}
\ge\frac{\delta}{\gamma^2+1}.
\tag{12}
\]

For `0<delta<1/2` and `gamma^2>1`, (12) implies

\[
h_\gamma(\delta)>\delta^2h_\gamma(1).
\tag{13}
\]

Equation (13) is equivalent to the lower threshold in (11) being at least the
upper threshold in (10). No admissible `kappa` exists.

## 4. Correct conclusion-producing target

Let `f_pc` be the exact pole-centered signed source of T99000 after one fixed
Cauchy regularization nonzero at every open-strip zeta zero. For any
`M(T)->infinity` with `M(T)=o(T)`, define

\[
\mathfrak T_T=E_T(U_a^{M(T)}f_{pc})
\]

and

\[
\mathfrak Q_T=\frac{2a}{T}\sum_{j<M(T)}\int_0^\infty
u e^{-u^2/(2T)}|V_aU_a^jf_{pc}(u)|^2\,du.
\]

The first factor in this integrand is again the real variable `u`. Equation
(7) gives

\[
E_T(f_{pc})=\mathfrak T_T+\mathfrak Q_T.
\tag{14}
\]

Define **BLSH** by

\[
\boxed{\mathfrak T_T+\mathfrak Q_T=e^{o(T)}.}
\tag{15}
\]

An off-line zero of displacement `delta>0` would instead force

\[
E_T(f_{pc})\ge e^{2\delta^2T+o(T)},
\]

contradicting (15). Hence `BLSH -> RH`.

The exact boundary is

```text
real-carrier quotient / Hardy range inverse   PROVED EXACT
false Weyl/parity mechanism                   NOT USED
monotone heat contraction                     PROVED EXACT
positive Laguerre square-function telescope   PROVED EXACT
filter-only contour closure                   REFUTED
BLSH source-specific estimate                 OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVEN
```
