# L-26203 — Polynomial-filtered centered Selberg equation

Claim ID: `L-26203`  
Status: `PROPOSED COMPLETE — exact distributional and Laplace algebra pending independent review`  
Scope: every fixed translation polynomial; no RH input  
Date: 2026-08-08  
Depends on: PR #219 `L-21906`; elementary translation-convolution algebra

Let `h>0`, let `tau` be right translation by `h`, and let

\[
p(z)=\sum_{j=0}^d c_j z^j
\]

be a fixed real polynomial. Put

\[
P(s)=p(e^{-hs}),
\qquad
\mathfrak Dp(z)=z p'(z).
\tag{L-26203.1}
\]

Let the centered prime measure `nu` satisfy

\[
\boxed{
\mathscr L\nu+\nu*\nu=R,
}
\tag{L-26203.2}
\]

where

\[
\mathscr L\nu=y\,d\nu+2dP_0*d\nu,
\qquad
dP_0(y)=e^{y/2}{\bf1}_{y\ge0}dy.
\tag{L-26203.3}
\]

Define the filtered measure

\[
\boxed{
\mu=p(\tau)\nu.
}
\tag{L-26203.4}
\]

## 1. Translation commutator

For every integer `j>=0`,

\[
\mathscr L\tau^j
=\tau^j\mathscr L+jh\tau^j.
\tag{L-26203.5}
\]

Consequently

\[
\boxed{
\mathscr L p(\tau)
=p(\tau)\mathscr L+h(\mathfrak Dp)(\tau).
}
\tag{L-26203.6}
\]

Since translations commute with convolution,

\[
[p(\tau)\nu]*[p(\tau)\nu]
=p(\tau)^2(\nu*\nu).
\tag{L-26203.7}
\]

## 2. Closed filtered equation

Apply `p(tau)^2` to (L-26203.2). From (L-26203.6),

\[
\begin{aligned}
p(\tau)^2\mathscr L\nu
&=\mathscr L p(\tau)^2\nu
 -h\mathfrak D(p^2)(\tau)\nu\\
&=\mathscr L p(\tau)\mu
 -2h(\mathfrak Dp)(\tau)\mu.
\end{aligned}
\]

Therefore `mu` satisfies the exact closed equation

\[
\boxed{
\Bigl[
 \mathscr L p(\tau)-2h(\mathfrak Dp)(\tau)
\Bigr]\mu
+\mu*\mu
=p(\tau)^2R.
}
\tag{L-26203.8}
\]

The quadratic term is the literal self-convolution of the same filtered source. No undifferenced copy of `nu` remains.

For `p(z)=1-z`, equation (L-26203.8) specializes to the first-difference equation of PR #219 `L-21906`.

## 3. Laplace form

Write

\[
H(s)=\langle\nu,e^{-s\cdot}\rangle,
\qquad
M(s)=P(s)H(s),
\qquad
\mathcal R(s)=\langle R,e^{-s\cdot}\rangle.
\tag{L-26203.9}
\]

The original Riccati equation is

\[
-H'(s)+\frac{2}{s-1/2}H(s)+H(s)^2=\mathcal R(s).
\tag{L-26203.10}
\]

Substituting `M=PH` gives

\[
\boxed{
-P(s)M'(s)
+\left[P'(s)+\frac{2P(s)}{s-1/2}\right]M(s)
+M(s)^2
=P(s)^2\mathcal R(s).
}
\tag{L-26203.11}
\]

This is the Laplace transform of (L-26203.8).

## 4. Positive real-exponential adjoint

Assume

\[
P(u)>0
\qquad(u\ge s_0>1).
\tag{L-26203.12}
\]

Define

\[
\boxed{
 m_{P,s_0}(u)
 =\frac{P(s_0)(s_0-1/2)^2}
 {P(u)^2(u-1/2)^2},
 \qquad u\ge s_0.
}
\tag{L-26203.13}
\]

Then

\[
\frac{m_{P,s_0}'(u)}{m_{P,s_0}(u)}
=-2\frac{P'(u)}{P(u)}-\frac{2}{u-1/2}.
\tag{L-26203.14}
\]

Multiplying (L-26203.11) by `m_(P,s_0)`, integrating on `[s_0,infinity)`, and integrating the derivative term by parts cancels the complete interior linear density. The boundary is normalized by

\[
P(s_0)m_{P,s_0}(s_0)=1.
\]

Hence

\[
\boxed{
 M(s_0)
 +\int_{s_0}^{\infty}m_{P,s_0}(u)M(u)^2du
 =\int_{s_0}^{\infty}m_{P,s_0}(u)P(u)^2\mathcal R(u)du.
}
\tag{L-26203.15}
\]

The kernel

\[
f_{P,s_0}(x+y)
=\int_{s_0}^{\infty}m_{P,s_0}(u)e^{-u(x+y)}du
\]

is positive Hankel.

## 5. Exact gauge cancellation

Substituting `M=PH` into (L-26203.15) gives

\[
\begin{aligned}
&P(s_0)H(s_0)\\
&\quad+P(s_0)(s_0-1/2)^2
 \int_{s_0}^{\infty}\frac{H(u)^2}{(u-1/2)^2}du\\
&=P(s_0)(s_0-1/2)^2
 \int_{s_0}^{\infty}\frac{\mathcal R(u)}{(u-1/2)^2}du.
\end{aligned}
\tag{L-26203.16}
\]

After division by `P(s_0)`, this is exactly the unfiltered positive-exponential identity. Thus fixed polynomial filtering preserves the closed square but does not strengthen the real-axis positive-adjoint estimate.

## 6. Application to the critical Euler fiber

For

\[
P(s)=(1-2^{1-s})(1-2^{1/2-s})^2,
\]

one has `P(u)>0` for every real `u>1`, so the preceding construction applies. It validates the exact closed Euler-filtered equation, but also proves that a proof using only this real positive-exponential adjoint cannot supply the missing local reflected reserve.

## 7. Proof boundary

Closed exactly:

- the commutator for every fixed translation polynomial;
- the closed filtered Selberg equation;
- its Riccati/Laplace form;
- the positive exponential adjoint;
- the exact gauge cancellation.

Not closed:

- a two-frequency physical-block inequality;
- a signed balanced contraction;
- `EFRC`;
- RH.
