# L-98041 — The continuous full-base Dickman profile is uniformly positive

Claim ID: `L-98041`<br>
Status: **PROVED UNCONDITIONAL ANALYTIC THEOREM**<br>
Created: 2026-08-18<br>
Depends on: `L-98040`; classical Dickman ratio estimates<br>
RH status: **not assumed**

Extend the Dickman function by `rho(v)=0` for `v<0`. For

\[
L=\log z,
\qquad
u={\log Y\over L},
\]

define the continuous full-base profile

\[
\boxed{
\mathcal C_L(u)=
\int_{[1,\infty)}
\rho\!\left(u-{\log x\over L}\right)dh(x).
}
\tag{L-98041.1}
\]

The extension to infinity is harmless because the kernel vanishes for `x>Y`.
There is an absolute constant `C_D` such that

\[
{\rho(u-v)\over\rho(u)}
\le \exp\!\bigl(C_Dv\log(u+2)\bigr)
\qquad(0\le v\le u),
\tag{L-98041.2}
\]

which follows from the standard de Bruijn estimate
`-rho'(t)/rho(t)=O(log(t+2))`.

Choose any `eta<1/2`. Combining (L-98041.2) with the exponentially weighted
variation `V_eta` of `L-98040` gives, uniformly when

\[
L\ge 2C_D\eta^{-1}\log(u+2),
\tag{L-98041.3}
\]

the relative approximation

\[
\boxed{
\mathcal C_L(u)
=a_*\rho(u)
\left(1+O_{P_{61}}\!\left({\log(u+2)\over L}\right)\right).
}
\tag{L-98041.4}
\]

In particular, there is a constant `C_0` such that

\[
\boxed{
L\ge C_0\log(u+2)
\quad\Longrightarrow\quad
\mathcal C_L(u)\ge {a_*\over2}\rho(u)>0.
}
\tag{L-98041.5}
\]

## Proof

Write `w=log x` and `H(w)=h(e^w)`. The signed measure `dH` has total mass
`a_*` and

\[
\int e^{\eta w}|dH(w)|<\infty.
\]

For `0<=w<=uL`, (L-98041.2) and the mean-value bound give

\[
|\rho(u-w/L)-\rho(u)|
\ll \rho(u)
 {w\log(u+2)\over L}
 \exp\!\left({C_Dw\log(u+2)\over L}\right).
\]

Under (L-98041.3), the exponential is bounded by `e^(eta w/2)`, and integration
against `|dH|` gives the error in (L-98041.4). The tail `w>uL` contributes at
most `O(e^{-eta uL})`; the de Bruijn lower bound
`rho(u)>=exp[-C u log(u+2)]` absorbs it under the same hypothesis. Since
`int dH=a_*`, the main term is `a_*rho(u)`.

## Explicit first logarithmic moment

Let `B_61(s)` be the Mellin transform of `b`. With `w=s+1/2`,

\[
B_{61}(s)=
{1-4^{-s}\over s^2}
\left[6\zeta(w)-3(1-2^{-w})(2-2^{-w})\right]
\prod_{p\le61}(1-p^{-w}).
\tag{L-98041.6}
\]

At `s=1/2`,

\[
B_{61}(s)={a_*\over s-1/2}+J_*+O(s-1/2),
\tag{L-98041.7}
\]

where, putting `P=product_(p<=61)(1-1/p)`,

\[
\begin{aligned}
J_*={}&2\left[
6P\sum_{p\le61}{\log p\over p-1}
+(6\gamma-9/4)P
\right]\\
&+6(2\log4-8)P.
\end{aligned}
\tag{L-98041.8}
\]

Directed evaluation gives

\[
\boxed{2.0695<J_*<2.0697.}
\tag{L-98041.9}
\]

Mellin--Stieltjes integration by parts identifies

\[
\boxed{
-\int_{[1,\infty)}\log x\,dh(x)=J_*.
}
\tag{L-98041.10}
\]

Thus the first correction to the continuous profile is
`(J_*/L)rho'(u)`, which is negative because `J_*>0`; this is diagnostic only.
The uniform positivity theorem uses the full variation estimate rather than a
truncated asymptotic series.
