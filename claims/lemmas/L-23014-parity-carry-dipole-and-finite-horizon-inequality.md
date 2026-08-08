# L-23014 — Exact parity–carry dipole and finite-horizon two-channel inequality

Claim ID: `L-23014`  
Title: The parity comb is a compact dyadic dipole of the continuum carry kernel, and their finite-horizon output energies differ by only polynomial loss and one lower boundary layer  
Status: **PROPOSED COMPLETE EXACT IDENTITY AND INEQUALITY PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-08  
Frozen parent: PR #236 at `1c9a749a1648c4772509eb3b056598c7044f4393`  
Dependencies: PR #236 `L-23012`; PR #252 `L-24501`; elementary weighted shift and Volterra estimates  
Scope: output-channel comparison; it is not source coercivity

## 1. The two positive kernels

Let `h=log 2`. Retain the parity comb

\[
P(t)=e^{-t/2}\mathbf1_{\lfloor e^t\rfloor\text{ odd}}
\]

and the continuum carry kernel

\[
k(t)=e^{-t/2}
\frac{\lfloor e^t\rfloor(\lfloor e^t\rfloor+1-e^t)}{e^t},
\qquad t\ge0.
\]

Their Laplace transforms are

\[
\widehat P(z)
=
\frac{(1-\sqrt2e^{-hz})\zeta(z+1/2)}{z+1/2},
\tag{L-23014.1}
\]

and

\[
\widehat k(z)
=
\zeta(z+1/2)
\frac{z-1/2}{(z+1/2)(z+3/2)}.
\tag{L-23014.2}
\]

## 2. Exact compact dipole

Division of (L-23014.1) by (L-23014.2) gives

\[
\boxed{
\widehat P(z)
=
(1-\sqrt2e^{-hz})
\frac{z+3/2}{z-1/2}\widehat k(z).
}
\tag{L-23014.3}

Since

\[
\frac{z+3/2}{z-1/2}=1+\frac2{z-1/2},
\]

causal inversion yields the compact signed measure

\[
\boxed{
P=\ell*k,
\qquad
\ell
=
\delta_0-\sqrt2\delta_h
+2e^{t/2}\mathbf1_{[0,h)}(t)\,dt.
}
\tag{L-23014.4}

The potentially growing exponential cancels exactly after one dyadic unitary
difference.

Equivalently, in causal distributions,

\[
\boxed{
\left(\partial-\frac12\right)P
=
\left(\partial+\frac32\right)
\left(I-\sqrt2\tau_h\right)k.
}
\tag{L-23014.5}

## 3. The unitary dyadic shift

On

\[
L^2_{1/2}:=L^2([0,\infty),e^{-t}dt),
\]

define

\[
Uf=\sqrt2\tau_hf.
\]

Then

\[
\boxed{\|Uf\|_{L^2_{1/2}}=\|f\|_{L^2_{1/2}}.}
\tag{L-23014.6}

For `N>=1`, decompose the first `N` dyadic layers by

\[
y_j(u)=2^{-j/2}f(u+jh),
\qquad0\le u<h,
\quad0\le j<N.
\]

The normalized layers of `(I-U)f` are `d_j=y_j-y_(j-1)`, with `y_(-1)=0`.
Since `y_j=sum_(r<=j)d_r`, Cauchy--Schwarz gives

\[
\boxed{
\sum_{j=0}^{N-1}\|y_j\|^2
\le
N^2\sum_{j=0}^{N-1}\|d_j\|^2.
}
\tag{L-23014.7}

Thus

\[
\boxed{
\|f\|_{L^2_{1/2}(0,Nh)}
\le
N\|(I-U)f\|_{L^2_{1/2}(0,Nh)}.
}
\tag{L-23014.8}

For a shifted run of `N` cells starting at layer `a`, the same proof gives

\[
\boxed{
\begin{aligned}
\|f\|^2_{L^2_{1/2}(ah,(a+N)h)}
\le{}&2N\|f\|^2_{L^2_{1/2}((a-1)h,ah)}\\
&+2N^2\|(I-U)f\|^2_{L^2_{1/2}(ah,(a+N)h)}.
\end{aligned}}
\tag{L-23014.9}

The only noncoercive mode on a finite run is the immediately preceding dyadic
boundary layer.

## 4. A genuine two-channel output inequality

Let `gamma` be any causal distribution for which the following convolutions are
well defined after one fixed compact smoothing, and put

\[
c=k*\gamma,
\qquad
p=P*\gamma.
\]

Equation (L-23014.5) gives

\[
\left(\partial+\frac32\right)(I-U)c
=
\left(\partial-\frac12\right)p.
\tag{L-23014.10}

The causal resolvent of `partial+3/2` has multiplier
`1/(z+3/2)`. On the weighted Plancherel line `Re z=1/2`, its norm is at most
`1/2`. Hence, on every cumulative finite horizon,

\[
\boxed{
\|(I-U)c\|_{L^2_{1/2}(0,T)}
\le
\frac12
\left\|\left(\partial-\frac12\right)p
\right\|_{L^2_{1/2}(0,T)}.
}
\tag{L-23014.11}

Combining (L-23014.8) and (L-23014.11),

\[
\boxed{
\|k*\gamma\|_{L^2_{1/2}(0,Nh)}
\le
\frac N2
\left\|\left(\partial-\frac12\right)(P*\gamma)
\right\|_{L^2_{1/2}(0,Nh)}.
}
\tag{L-23014.12}

This is a true two-frequency/digital inequality: the carry output is controlled
by the parity graph output with only polynomial horizon loss.

## 5. Canonical carry inverse control

Let `g` be the causal carry inverse from PR #252, so

\[
k*g=t.
\]

Then

\[
\boxed{
P*g=r,
}
\tag{L-23014.13}

where

\[
r(t)=
\begin{cases}
8e^{t/2}-8-3t,&0\le t<h,\\
8(\sqrt2-1)+3(\sqrt2-1)t-3\sqrt2h,&t\ge h.
\end{cases}
\tag{L-23014.14}

Both branches are nonnegative. On the first branch, `r(0)=0` and
`r'(t)=4e^(t/2)-3>=1`. On the second branch the slope is positive, and

\[
r(h)=8(\sqrt2-1)-3\log2>0
\]

from the elementary bounds `sqrt2>7/5` and `log2<7/10`.

Thus the canonical inverse has two exact positive convolution outputs. This
fact alone does not force `g>=0`, because the kernels have a common zeta factor.

## 6. Proof boundary

Closed exactly:

- the compact parity/carry dipole;
- the distributional differential identity;
- the unitary dyadic layer model;
- finite-horizon Poincare estimates;
- the two-channel output inequality;
- the explicit positive carry-inverse outputs.

Not closed:

- a lower bound on the source from these outputs;
- positivity of the carry inverse;
- RH.
