# L-93280 - The centered cubic scale field has an exact safe-line Plancherel formula

Claim ID: `L-93280`  
Status: **PROPOSED COMPLETE UNCONDITIONAL ANALYTIC THEOREM - INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: the centered-cubic kernel on PR #531; the classical zero-free line `Re s=1` and the standard bound for `zeta'/zeta` there  
RH status: **not assumed**

## 1. The normalized field

Let

\[
W=W_C,
\qquad
\ell(v)=e^{-v}W(e^{-v})\mathbf1_{v\ge0}.
\tag{L-93280.1}
\]

For a real carrier `t`, define the tempered signed measure on `[0,infinity)`

\[
d\nu_t(u)
=e^{itu}\left[
\sum_{n\ge2}\frac{\Lambda(n)}n\delta_{\log n}(du)-du
\right].
\tag{L-93280.2}
\]

The centered normalized cubic field is

\[
\boxed{
\mathcal G_C(r,t)=(\ell*d\nu_t)(r),
\qquad r\ge0.
}
\tag{L-93280.3}
\]

Equivalently, with `X=e^r`,

\[
\boxed{
\begin{aligned}
\mathcal G_C(r,t)
={}&X^{-1}
\sum_{n\le X}\Lambda(n)n^{it}W(n/X)\\
&-X^{-1}\int_1^Xx^{it}W(x/X)\,dx.
\end{aligned}
}
\tag{L-93280.4}
\]

This is exactly `e^{-r/2}(F_C-F_C^cont)` in the notation of `R-93280`.

## 2. Safe-line Fourier transform

Use

\[
\widehat f(\xi)=\int_{\mathbb R}f(r)e^{-i\xi r}\,dr.
\]

Changing variables `x=e^{-v}` gives

\[
\boxed{
\widehat\ell(\xi)=\widehat W(1+i\xi).
}
\tag{L-93280.5}
\]

For `epsilon>0`, introduce the regularized safe-line logarithmic derivative

\[
Z_\epsilon(\tau)
=-\frac{\zeta'}{\zeta}(1+\epsilon+i\tau)
-\frac1{\epsilon+i\tau}.
\tag{L-93280.6}
\]

The second term removes the continuous density and the pole of zeta at one.
Abel convergence gives the exact regularized identity

\[
\widehat{\mathcal G}_{C,\epsilon}(\xi,t)
=\widehat W(1+i\xi)
Z_\epsilon(\xi-t).
\tag{L-93280.7}
\]

Letting `epsilon` decrease to zero in the weighted `L2` space yields

\[
\boxed{
\widehat{\mathcal G}_C(\xi,t)
=\widehat W(1+i\xi)Z(\xi-t),
}
\tag{L-93280.8}
\]

where

\[
Z(\tau)=\operatorname*{fp}_{\epsilon\downarrow0}Z_\epsilon(\tau)
\tag{L-93280.9}
\]

is continuous at zero and is the boundary value on the zero-free line.

## 3. Unconditional finite scale energy

The centered-cubic multiplier satisfies

\[
|\widehat W(1+i\xi)|\ll(1+|\xi|)^{-2}.
\tag{L-93280.10}
\]

The classical de la Vallee Poussin zero-free line and the standard logarithmic
derivative estimate give

\[
|Z(\tau)|\ll\log^2(2+|\tau|)
\qquad(\tau\in\mathbb R).
\tag{L-93280.11}
\]

Plancherel therefore gives

\[
\boxed{
\begin{aligned}
\|\mathcal G_C(\cdot,t)\|_2^2
&=\frac1{2\pi}
\int_{\mathbb R}
|\widehat W(1+i\xi)|^2|Z(\xi-t)|^2\,d\xi\\
&\ll \log^4(2+|t|).
\end{aligned}
}
\tag{L-93280.12}
\]

In particular,

\[
\boxed{
\|\mathcal G_C(\cdot,t)\|_2
\ll\log^2(2+|t|)
}
\tag{L-93280.13}
\]

unconditionally.

## 4. Interpretation

The raw field lives on the critical line `Re s=1/2` and contains the growing
continuous-prime mode. The centered normalized field lives on the safe line
`Re s=1`, where its complete scale energy is finite and controlled by classical
zero-free-line mathematics.

This does not prove the First-Hermite sign. The remaining issue is a signed
pairing with the phase-locked synthesis vector, not the existence of scale
energy.
