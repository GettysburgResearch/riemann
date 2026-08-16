# L-20214 — Exact archimedean curvature and dyadic bounds

Claim ID: `L-20214`  
Title: The prime-free zeta screw curvature is strictly increasing and the dyadic renormalized barrier has explicit exponential coercivity  
Status: `PROPOSED — COMPLETE ELEMENTARY DIFFERENTIATION AND BOUNDS`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: the exact prime-free function `F` in `L-19801/T-20205`  
Scope: `t>0`; dyadic tiles `T in [r log2,(r+1)log2]`

## 1. Prime-free function

For `0<t<log2`, the screw function has no prime ramp and equals

\[
\begin{aligned}
 F(t)={}&4(e^{t/2}+e^{-t/2}-2)
 +{C_\Gamma t\over2}\\
 &-{1\over4}\left[
 e^{-t/2}\Phi(e^{-2t},2,1/4)
 -\Phi(1,2,1/4)
 \right],
\end{aligned}
 \tag{1}

where

\[
 C_\Gamma=\psi(1/4)-\log\pi.
\]

The same explicit formula defines the smooth archimedean function `F` for every `t>0`.

## 2. Exact second derivative

Use

\[
 e^{-t/2}\Phi(e^{-2t},2,1/4)
 =4\sum_{k\ge0}{e^{-(2k+1/2)t}\over(2k+1/2)^2}.
 \tag{2}

Two differentiations give

\[
\boxed{
 F''(t)
 =e^{t/2}+e^{-t/2}
  -{e^{-t/2}\over1-e^{-2t}}
 =e^{t/2}-{e^{-5t/2}\over1-e^{-2t}}.}
 \tag{3}

In particular, `F''(t)` tends to `-infinity` as `t downarrow0`; no global positivity claim is made.

## 3. Strictly increasing curvature

Differentiating (3),

\[
\boxed{
\begin{aligned}
 F'''(t)={}&{1\over2}e^{t/2}
 +{5\over2}{e^{-5t/2}\over1-e^{-2t}}\\
 &+2{e^{-9t/2}\over(1-e^{-2t})^2}>0.
\end{aligned}}
 \tag{4}

Therefore

\[
\boxed{F''\text{ is strictly increasing on }(0,infinity).}
 \tag{5}

For every integer `r>=2`,

\[
 H_r(T)=F(T)-r^2F(T/r)
\]

has

\[
\boxed{
 H_r''(T)=F''(T)-F''(T/r)>0
 \qquad(T>0),}
 \tag{6}

so the renormalized barrier is globally strictly convex.

This is the exact fact used by the Legendre/Bregman construction.

## 4. Explicit large-scale bounds

For `T>=log4`, equation (3) gives

\[
 {e^{-5T/2}\over1-e^{-2T}}
 =e^{T/2}{e^{-3T}\over1-e^{-2T}}
 \le {1\over60}e^{T/2}.
\]

Hence

\[
\boxed{
 {59\over60}e^{T/2}
 \le F''(T)<e^{T/2}.}
 \tag{7}

Put `a=log2` and define the finite base constant

\[
 C_a=\max_{a\le t\le3a/2}|F''(t)|.
 \tag{8}

For `T in [ra,(r+1)a]` and `r>=2`, one has `T/r in [a,3a/2]`. Therefore

\[
\boxed{
 {59\over60}e^{T/2}-C_a
 \le H_r''(T)
 \le e^{T/2}+C_a.}
 \tag{9}

Choose any explicit integer `r_0` satisfying

\[
 C_a\le {29\over60}2^{r_0/2}.
 \tag{10}

Then for every `r>=r_0` and `T in [ra,(r+1)a]`,

\[
\boxed{
 {1\over2}e^{T/2}
 \le H_r''(T)
 \le C_a' e^{T/2},}
 \tag{11}

where, for example,

\[
 C_a'=1+C_a2^{-r_0/2}.
\]

All constants are finite evaluations of the explicit function (3).

## 5. Uniform dyadic condition number

Let

\[
 m_r=\inf_{T\in[ra,(r+1)a]}H_r''(T),
 \qquad
 L_r=\sup_{T\in[ra,(r+1)a]}H_r''(T).
\]

Equation (11) yields

\[
\boxed{
 {L_r\over m_r}
 \le2C_a'e^{a/2}
 =2\sqrt2\,C_a',}
 \tag{12}

independently of `r>=r_0`.

Thus the primal Bregman divergence and the centered mass square in `L-20209` are uniformly equivalent on every sufficiently large dyadic tile.

## 6. Proof boundary

- Equations (3)--(6) are exact.
- The finite constants in (8)--(11) must be enclosed directedly in a production artifact.
- Curvature coercivity does not establish the prime transport reserve or centered discrepancy bound.
