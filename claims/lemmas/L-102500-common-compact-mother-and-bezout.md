# L-102500 — A compact common mother kernel with exact Smith–Bezout data

Claim ID: `L-102500`  
Status: **PROVED EXACT**  
Created: 2026-08-22  
Programme base: PR #713 at `b6bddacec0e7aeb0ad58c1c2b038c07d66d4467b`  
RH status: **not assumed**

Use the Mellin convention

\[
\widehat f(s)=\int_1^\infty f(y)y^{-s-1}\,dy
\]

and the operators

\[
Df(y)=y f'(y),\qquad S_2f(y)=f(y/2),
\]

with zero extension below `1`.

Define

\[
\Phi_0(y)=\bigl(8\sqrt y-8-4\log y\bigr)\mathbf1_{y\ge1}.
\]

Then

\[
D\Phi_0(y)=4(\sqrt y-1)\mathbf1_{y\ge1}
\]

and

\[
\boxed{\widehat{\Phi_0}(s)=\frac{2}{s^2(s-\frac12)}.}
\tag{L-102500.1}
\]

Put

\[
\mathcal Q_2=(I-\sqrt2S_2)^2(I-S_2)^2
\]

and define

\[
\boxed{\Phi_*=\mathcal Q_2\Phi_0.}
\tag{L-102500.2}
\]

## 1. Compact support and regularity

`(I-sqrt(2)S_2)` annihilates `sqrt(y)`, while `(I-S_2)^2`
annihilates `1` and `log(y)`. Consequently

\[
\boxed{\operatorname{supp}\Phi_*\subset[1,16].}
\tag{L-102500.3}
\]

Moreover `Phi_0(1)=D Phi_0(1)=0`. Every newly activated dyadic
translate enters with zero value and first logarithmic derivative. Hence
`Phi_*` is globally `C^1` in `log(y)`, with

\[
\boxed{\Phi_*(1)=D\Phi_*(1)=\Phi_*(16)=D\Phi_*(16)=0.}
\tag{L-102500.4}
\]

## 2. Common multiplier

Write

\[
q(s)=1-\sqrt2\,2^{-s},\qquad r(s)=1-2^{-s}.
\]

Then

\[
\boxed{m_\Phi(s):=\widehat{\Phi_*}(s)=
\frac{2q(s)^2r(s)^2}{s^2(s-\frac12)}.}
\tag{L-102500.5}
\]

Define

\[
K_{\rm CV}=D\Phi_*,\qquad
K_{\rm XD}=\frac12(D+\tfrac32)\Phi_*.
\tag{L-102500.6}
\]

Their multipliers are

\[
\boxed{m_{\rm CV}(s)=s m_\Phi(s)=
\frac{2q(s)^2r(s)^2}{s(s-\frac12)},}
\tag{L-102500.7}
\]

\[
\boxed{m_{\rm XD}(s)=\frac{s+\frac32}{2}m_\Phi(s)=
\frac{q(s)^2r(s)^2(s+\frac32)}{s^2(s-\frac12)}.}
\tag{L-102500.8}
\]

The second multiplier is exactly the corrected extra-notched `K1` multiplier.
The first is the activation-free critical kernel after the same fixed zero-safe
dyadic filter.

## 3. Smith–Bezout data

Put

\[
A(s)=s,\qquad B(s)=\frac{s+\frac32}{2}.
\]

Then `m_CV=A m_Phi`, `m_XD=B m_Phi`, and

\[
\boxed{-\frac23A(s)+\frac43B(s)=1.}
\tag{L-102500.9}
\]

Thus

\[
\boxed{\Phi_*=-\frac23K_{\rm CV}+\frac43K_{\rm XD}.}
\tag{L-102500.10}
\]

This is a finite common-source reconstruction in both directions. No critical
integration inverse is used.

## 4. Zero safety

A hypothetical zero `rho` with `1/2<Re(rho)<1` corresponds to
`s=rho-1/2`, so `0<Re(s)<1/2`. The zeros of `r` lie on `Re(s)=0`; the
zeros of `q` lie on `Re(s)=1/2`. Therefore

\[
\boxed{m_\Phi(s),m_{\rm CV}(s),m_{\rm XD}(s)\ne0
\quad(0<\Re s<\tfrac12).}
\tag{L-102500.11}
\]

All three fixed channels preserve every hypothetical open-strip pole.
