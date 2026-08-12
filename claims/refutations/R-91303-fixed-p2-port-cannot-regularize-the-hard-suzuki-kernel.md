# R-91303 — The fixed phase-locked `p=2` port does not regularize Suzuki's hard-range kernel

Claim ID: `R-91303`  
Status: **EXACT ROUTE REFUTATION / REQUIRED CORRECTION TO `L-91308`**  
Created: 2026-08-12  
RH status: **unproved**

## 1. Suzuki's integer singularities

For `omega>0`, Suzuki's arithmetic Hankel kernel has the form

\[
 h_\omega(x)=\frac1x\sum_{n\le x}c_\omega(n)
 g_\omega\!\left(\frac n x\right),
 \qquad
 c_\omega(n)=n^\omega\prod_{p\mid n}(1-p^{-2\omega}),
 \tag{R-91303.1}
\]

with

\[
 g_\omega(t)
 =C_\omega(1-t)^{\omega-1}+O_\omega((1-t)^\omega)
 \qquad(t\uparrow1),
 \tag{R-91303.2}
\]

where `C_omega` is nonzero. Consequently, as `x` decreases to an integer `N`
from above,

\[
 \boxed{
 h_\omega(x)
 =C_\omega A_\omega(N)(x-N)^{\omega-1}
 +O_\omega(1+|x-N|^\omega),
 }
 \tag{R-91303.3}
\]

where

\[
 A_\omega(N)=\prod_{p\mid N}(1-p^{-2\omega})>0.
 \tag{R-91303.4}
\]

Every integer therefore carries a genuine leading singularity. Its square is
locally integrable exactly when

\[
 2(\omega-1)>-1
 \quad\Longleftrightarrow\quad
 \omega>\frac12.
 \tag{R-91303.5}
\]

This is the structural origin of Suzuki's Hilbert--Schmidt threshold.

## 2. Mellin-normalized dyadic dilation

For an integer `m`, define

\[
 (U_mh)(x)=2^m h(2^m x).
 \tag{R-91303.6}
\]

If the Mellin transform is

\[
 \mathcal Mh(s)=\int_0^\infty h(x)x^{-s}\,dx,
 \]

then

\[
 \mathcal M(U_mh)(s)=2^{ms}\mathcal Mh(s).
 \tag{R-91303.7}
\]

The phase-locked local factor used in `L-91308` is

\[
\begin{aligned}
 F_*(s)
 &=2^{2s}Q_*(2^{-s})\\
 &=2\,2^{2s}-15\,2^s+35-30\,2^{-s}+8\,2^{-2s}.
\end{aligned}
 \tag{R-91303.8}
\]

Thus the corresponding physical filter is

\[
 \mathscr R_2
 =2U_2-15U_1+35U_0-30U_{-1}+8U_{-2}.
 \tag{R-91303.9}
\]

## 3. Exact leading singular coefficient at every odd integer

Fix an odd integer `N`. At `x=N`, the terms `U_{-1}h_omega` and
`U_{-2}h_omega` are regular because `N/2` and `N/4` are not integers. The
terms with `m=0,1,2` all have singularities.

For `m>=1`,

\[
 A_\omega(2^mN)
 =A_\omega(N)(1-2^{-2\omega}),
 \tag{R-91303.10}
\]

and (R-91303.3) gives

\[
 U_mh_\omega(x)
 =C_\omega A_\omega(2^mN)2^{m\omega}
 (x-N)^{\omega-1}+\text{less singular terms}.
 \tag{R-91303.11}
\]

Therefore

\[
 \boxed{
 (\mathscr R_2h_\omega)(x)
 =C_\omega A_\omega(N)\kappa_\omega
 (x-N)^{\omega-1}+\text{less singular terms},
 }
 \tag{R-91303.12}
\]

where

\[
 \kappa_\omega
 =35+(1-2^{-2\omega})
 \left(-15\,2^\omega+2\,2^{2\omega}\right).
 \tag{R-91303.13}
\]

Put `t=2^omega`. Then

\[
 \boxed{
 \kappa_\omega
 =2t^2-15t+\frac{15}{t}+33.
 }
 \tag{R-91303.14}
\]

For `0<omega<=1/2`, one has `1<t<=sqrt(2)` and

\[
 \frac d{dt}\left(2t^2-15t+\frac{15}{t}+33\right)
 =4t-15-\frac{15}{t^2}<0.
 \tag{R-91303.15}
\]

Hence the minimum on this interval is attained at `sqrt(2)`, where

\[
 \kappa_{1/2}
 =37-\frac{15}{2}\sqrt2
 >37-\frac{45}{4}
 =\frac{103}{4}>0.
 \tag{R-91303.16}
\]

Thus

\[
 \boxed{
 \kappa_\omega>0
 \qquad(0<\omega\le1/2).
 }
 \tag{R-91303.17}
\]

The phase-locked filter does not cancel even the leading singularity at any
odd integer.

## 4. Consequence

For every `0<omega<=1/2`, `mathscr R_2 h_omega` still has an
`(x-N)^(omega-1)` singularity at every odd integer `N`, with nonzero
coefficient. Therefore

\[
 \boxed{
 \mathscr R_2h_\omega\notin L^2_{\rm loc}
 \quad\text{near every odd integer}.
 }
 \tag{R-91303.18}
\]

In particular, the fixed local port cannot turn Suzuki's hard-range Hankel
kernel into a Hilbert--Schmidt kernel, a trace-class truncation, or an ordinary
Fredholm determinant problem.

## 5. Corrected canonical frontier

The useful local statements survive:

```text
open-strip zero-safety of the p=2 factor;
stable radial Riesz synthesis;
exact finite lossless local port;
four vanishing moments at the global smooth endpoint.
```

The following claim from `L-91308` does not survive:

```text
fixed p=2 filtering regularizes all integer singularities for omega<=1/2.
```

A hard-range canonical construction must instead use one of:

1. a genuinely global all-prime arithmetic regularizer that acts on every
   integer singularity in source order;
2. a singular-integral/Fredholm theory that admits the native
   `(x-N)^(omega-1)` singularities;
3. the completed Lévy--Fock/Hardy optical theorem, from which the canonical
   system is recovered only after global positivity has been established.

The local `p=2` port may remain as a zero-safe boundary port in any of these
three constructions, but it cannot be the regularization mechanism by itself.
