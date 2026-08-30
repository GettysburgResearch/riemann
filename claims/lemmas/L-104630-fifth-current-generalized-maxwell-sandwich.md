# L-104630 — The fifth odd current obeys a generalized-Maxwell source sandwich

Claim ID: `L-104630`  
Status: **PROVED EXACT FROM THE POSITIVE XI SOURCE AND ITS STRONG LOG-CONCAVITY**  
Created: 2026-08-27  
Depends on: `L-106500`, `L-106501` at PR #731 head
`433490c133b26bce4163f4edf7ad04aeda9d33e3`; `L-105640` at PR #729 head
`e399156475cac82199275ea1470eaa83ec6ebbc3`  
RH status: **not assumed**

Let

\[
F(t)=\int_{\mathbb R}\Phi(u)e^{itu}\,du,
\qquad \Phi=e^{-\psi}>0,
\qquad \psi''\ge\kappa_0,
\]

where for the standard Xi kernel

\[
\boxed{\kappa_0={20476\over2345}>8.}
\tag{L-104630.1}
\]

For the fifth odd endpoint use the positive first chaos and cross current of
`L-106500`,

\[
\widehat{\mathcal L_5}(s)
={1\over2}\int(v-u)(v^5-u^5)\Phi(u)\Phi(v)\,du,
\qquad v=s-u,
\]

\[
\widehat J_{5,H}(s)
={1\over2}\int(v^5-u^5)\sinh(H(v-u))\Phi(u)\Phi(v)\,du .
\]

On the positive-frequency channel define

\[
r_{5,H}(s)
={H e^{-Hs}\widehat{\mathcal L_5}(s)\over\widehat J_{5,H}(s)}
\tag{L-104630.2}
\]

with value zero when the denominator vanishes.

## 1. Exact conditional source

Write

\[
u={s\over2}-x,\qquad v={s\over2}+x.
\]

Then

\[
(v-u)(v^5-u^5)
={5\over4}s^4x^2+10s^2x^4+4x^6.
\tag{L-104630.3}
\]

Consequently

\[
{\widehat J_{5,H}(s)\over H\widehat{\mathcal L_5}(s)}
=
\mathbb E_{q_{s,5}}
{\sinh(2HX)\over2HX},
\tag{L-104630.4}
\]

where the probability density on `x>0` is proportional to

\[
\left({5\over4}s^4x^2+10s^2x^4+4x^6\right)
\Phi(s/2+x)\Phi(s/2-x).
\tag{L-104630.5}
\]

All three coefficients are nonnegative. The full fifth-current source is
retained; no individual chaos is estimated and then recombined.

## 2. Generalized-Maxwell domination

Let the reference density be obtained from (L-104630.5) by replacing the
product of Xi kernels by `exp(-kappa_0 x^2)`. The polynomial factor cancels
from the likelihood ratio, and

\[
{d\over dx}\log {q_{s,5}(x)\over g_{s,5}(x)}
=
-\psi'(s/2+x)+\psi'(s/2-x)+2\kappa_0x
\le0.
\tag{L-104630.6}
\]

Thus `q_(s,5)` is stochastically dominated by `g_(s,5)`. The reference law is
a positive mixture of the three densities proportional to

\[
x^2e^{-\kappa_0x^2},\qquad
x^4e^{-\kappa_0x^2},\qquad
x^6e^{-\kappa_0x^2}.
\]

Put `z=H^2/kappa_0`. Their exact hyperbolic moments are

\[
M_1(z)=e^z,
\]

\[
M_2(z)=e^z\left(1+{2z\over3}\right),
\]

\[
M_3(z)=e^z\left(1+{4z\over3}+{4z^2\over15}\right).
\tag{L-104630.7}
\]

They follow either from the moment series or from
`_1F_1(r+1/2;3/2;z)`. For `z>=0`,

\[
M_1(z)\le M_2(z)\le M_3(z).
\]

Moreover, coefficientwise,

\[
1+{4z\over3}+{4z^2\over15}\le e^{4z/3},
\]

so

\[
\boxed{M_3(z)\le e^{7z/3}.}
\tag{L-104630.8}
\]

Since `x -> sinh(2Hx)/(2Hx)` is increasing, (L-104630.4)--(L-104630.8)
give the exact two-sided current-profile estimate

\[
\boxed{
e^{-Hs-\frac{7H^2}{3\kappa_0}}
\le r_{5,H}(s)\le e^{-Hs}
\qquad(H,s\ge0).
}
\tag{L-104630.9}
\]

The reflected frequency channel obeys the mirrored statement.

## 3. Meaning

The earlier base-current theorem used a Maxwell `x^2` law and the factor
`exp(H^2/kappa_0)`. The fifth endpoint is not the same law: its complete
source is a positive mixture of the `x^2,x^4,x^6` generalized-Maxwell
channels. Equation (L-104630.9) reconstructs that distinction and supplies a
uniform quantitative metric for the actual fifth-endpoint current.

No phase transport or critical-line percentage is proved here.
