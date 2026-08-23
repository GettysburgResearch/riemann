# L-105209 — The natural-order terminal companion is one-sided on the complete Levinson safe ray

Claim ID: `L-105209`  
Status: **PROPOSED COMPLETE UNCONDITIONAL ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: the positive Xi Fourier kernel; `L-105200`; `L-105206`  
RH status: **not assumed**

This theorem addresses the terminal denominator in the **actual** horizontal
Levinson argument.  Unlike `L-105201`, the depth below the real `z`-axis is
not fixed.

## 1. Native terminal companion

For an integer `r>=1`, put

\[
M_r=\int_0^\infty u^r\Phi(u)\,du,
\qquad
\mu_r={M_{r+1}\over M_r},
\qquad
\lambda_r={1\over\mu_r}.
\tag{L-105209.1}
\]

Define

\[
F_r(z)=\Xi^{(r)}(z),
\qquad
E_r(z)=F_r(z)-i\lambda_rF_{r+1}(z).
\tag{L-105209.2}
\]

The one-sided Fourier representation gives exactly

\[
\boxed{
\begin{aligned}
i^{-r}E_r(z)
={}&\int_0^\infty u^r\Phi(u)
 \left(1+{u\over\mu_r}\right)e^{izu}\,du\\
&+(-1)^r\int_0^\infty u^r\Phi(u)
 \left(1-{u\over\mu_r}\right)e^{-izu}\,du.
\end{aligned}}
\tag{L-105209.3}
\]

The second coefficient has zero mean at `z=0`:

\[
\int_0^\infty u^r\Phi(u)
\left(1-{u\over\mu_r}\right)du=0.
\tag{L-105209.4}
\]

Thus `lambda_r` is the exact source parameter which removes the reflected
carrier, not an asymptotic parameter chosen after a hypothetical zero.

## 2. Two tilted saddles

Fix a real ordinate `T` and write the complete lower ray as

\[
z=T-iy,
\qquad y\ge0.
\]

Put

\[
P_{r,y}(T)
=\int_0^\infty u^r\Phi(u)
 \left(1+{u\over\mu_r}\right)e^{yu+iTu}\,du,
\]

\[
N_{r,y}(T)
=\int_0^\infty u^r\Phi(u)
 \left(1-{u\over\mu_r}\right)e^{-yu-iTu}\,du.
\tag{L-105209.5}
\]

Then

\[
i^{-r}E_r(T-iy)=P_{r,y}(T)+(-1)^rN_{r,y}(T).
\tag{L-105209.6}
\]

Let `w_(r,+)(y)` and `w_(r,-)(y)` be the maximizers of

\[
S_{r,\pm y}(u)
=r\log u+\log\Phi(u)\pm yu.
\tag{L-105209.7}
\]

For all sufficiently large `r`, the same differentiated asymptotics used in
`L-105200` give:

\[
w_{r,+}(y)\ge w_r\ge w_{r,-}(y),
\tag{L-105209.8}
\]

and the positive tilted variance satisfies

\[
\boxed{
\sigma_{r,+}(y)^2
\ll {1\over r/w_r+y}
\le C\sigma_r^2
\qquad(y\ge0),
}
\tag{L-105209.9}
\]

where

\[
\sigma_r^2\asymp {w_r\over r}.
\]

The proof is a uniform Laplace argument.  In the central region,

\[
-S_{r,+y}''(u)
={r\over u^2}-(\log\Phi)''(u)
\gg {r\over w_r}+y;
\]

the left tail loses through `u^r`, and the right tail through
`exp(-pi exp(2u))`.  The same estimates apply to the first three tilted
moments and are uniform for all `y>=0`.

## 3. Positive component has no phase cancellation

Assume

\[
\boxed{|T|\sigma_r\longrightarrow0.}
\tag{L-105209.10}
\]

Center the positive tilted probability at its mean `m_(r,+)(y)`.  The elementary
bound

\[
\Re\,\mathbb E e^{iT(U-m)}
\ge1-{T^2\operatorname{Var}(U)\over2}
\]

and (L-105209.9) give, uniformly for `y>=0`,

\[
\boxed{
|P_{r,y}(T)|
\ge(1-o(1))
\int_0^\infty u^r\Phi(u)
\left(1+{u\over\mu_r}\right)e^{yu}du.
}
\tag{L-105209.11}
\]

The logarithmic derivative of the positive component is similarly

\[
\boxed{
{P_{r,y}'(T)\over P_{r,y}(T)}
=i m_{r,+}(y)
+O\!\left(|T|\sigma_{r,+}(y)^2\right).
}
\tag{L-105209.12}
\]

## 4. The reflected component is uniformly negligible

At `y=0`, the exact cancellation (L-105209.4) gives

\[
\begin{aligned}
|N_{r,0}(T)|
&\le {1\over\mu_r}
 \int u^r\Phi(u)|u-\mu_r|
 |e^{-iTu}-e^{-iT\mu_r}|du\\
&\le {|T|\over\mu_r}
 M_r\operatorname{Var}_{\nu_r}(U).
\end{aligned}
\tag{L-105209.13}
\]

Hence

\[
{ |N_{r,0}(T)|\over |P_{r,0}(T)|}
\ll |T|{\sigma_r^2\over\mu_r}=o(1).
\tag{L-105209.14}
\]

For `y>0`, compare the two real tilted partition functions.  Uniform saddle
expansion for `0<=y<=c/sigma_r`, followed by the monotone saddle bounds for
larger `y`, gives

\[
\boxed{
\sup_{y\ge0}
{ |N_{r,y}(T)|\over |P_{r,y}(T)|}
=o(1).
}
\tag{L-105209.15}

One convenient quantitative split is:

```text
0 <= y <= 1/mu_r:
  use the zero at y=0 and the tilted variance;

1/mu_r <= y <= c/sigma_r:
  use Z(-y)/Z(y) <= exp(-c mu_r y) and Gaussian tilting;

y >= c/sigma_r:
  use the separated saddle values in S_(r,+y) and S_(r,-y).
```

In every region the polynomial factors `1+-u/mu_r` are absorbed by the first
two tilted moments.  The double-exponential right tail makes the last estimate
uniform to `y=infinity`.

The same proof with one additional factor `u` gives

\[
\sup_{y\ge0}
{ |N_{r,y}'(T)|
 \over
 m_{r,+}(y)|P_{r,y}(T)|}
=o(1).
\tag{L-105209.16}

## 5. Complete safe-ray sector theorem

Equations (L-105209.11)--(L-105209.16) imply

\[
\boxed{
E_r(T-iy)\ne0
\qquad(y\ge0),
}
\tag{L-105209.17}

and

\[
{E_r'(T-iy)\over E_r(T-iy)}
=i m_{r,+}(y)
+O\!\left(|T|\sigma_{r,+}(y)^2\right)
+o(m_{r,+}(y)).
\tag{L-105209.18}

Since `E_r'=E_(r+1)`, and since

\[
{G_{r,\lambda_r}\over G_{r+1,\lambda_r}}
=i{E_r\over E_{r+1}},
\]

one obtains the narrow-sector estimate

\[
\boxed{
\sup_{y\ge0}
\left|
\arg {G_{r,\lambda_r}(1/2+y+iT)
      \over
      G_{r+1,\lambda_r}(1/2+y+iT)}
\right|
=o(1).
}
\tag{L-105209.19}

The argument is the branch continued from `y=infinity`; the quotient remains
inside one fixed acute sector and therefore cannot accumulate a hidden winding.
Consequently

\[
\boxed{
\Theta_{r,\lambda_r}(T)=o(1)
}
\tag{L-105209.20}

on every sequence satisfying (L-105209.10).

## 6. Natural derivative order

Since

\[
\sigma_r^2\asymp{\log r\over r},
\]

condition (L-105209.10) holds whenever

\[
{T^2\log r\over r}\longrightarrow0.
\tag{L-105209.21}

Thus it is enough to take

\[
\boxed{
r=T^2\log T\,L(T),
\qquad L(T)\to\infty.
}
\tag{L-105209.22}

The slowly growing reserve is used only to make the complete safe-ray phase
sector shrink to zero.  A fixed sufficiently large multiple of
`T^2 log T` still yields a fixed acute sector, which is enough for
nonvanishing but not the `o(1)` conclusion.

## 7. Scope

This theorem removes the terminal **high-derivative denominator** from the
actual Levinson horizontal argument.  It does not estimate the numerator

\[
\xi+\lambda_r\xi'.
\]

That numerator is the classical low-order Levinson auxiliary and retains the
zeta-zero difficulty.  The theorem is proposed complete analytic mathematics,
but its uniform all-`y` saddle estimates require independent hostile review.
