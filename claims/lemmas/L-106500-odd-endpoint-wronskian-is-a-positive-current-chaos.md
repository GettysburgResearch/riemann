# L-106500 — Odd endpoint Wronskians are first chaoses of positive cross currents

Claim ID: `L-106500`  
Status: **PROVED EXACT UNCONDITIONALLY FROM A POSITIVE EVEN FOURIER SOURCE**  
Created: 2026-08-25  
Depends on: `L-105620`, `L-106401`; the positive even Xi Fourier kernel  
RH status: **not assumed**

Let

\[
F(t)=\int_{\mathbb R}\Phi(u)e^{itu}\,du,
\qquad \Phi(-u)=\Phi(u)\ge0,
\]

with enough decay for all operations below.  Fix an odd integer

\[
K=2m+1.
\]

Define the signed endpoint Wronskian

\[
\boxed{
\mathcal L_K(t)
=(-1)^m\bigl(F'(t)F^{(K)}(t)-F(t)F^{(K+1)}(t)\bigr).
}
\tag{L-106500.1}

## 1. Positive exterior-square density

Writing `v=xi-u`, product convolution followed by the interchange
`u <-> v` gives

\[
\boxed{
\widehat{\mathcal L_K}(\xi)
={1\over2}\int_{\mathbb R}
 (v-u)(v^K-u^K)\Phi(u)\Phi(v)\,du
\ge0.
}
\tag{L-106500.2}

The sign is pointwise because the odd power map is increasing on the complete
real line.

Using the exterior-square chaoses

\[
\Lambda_{2j}(\xi)
={1\over2}\int(2u-\xi)^{2j}\Phi(u)\Phi(\xi-u)\,du,
\]

and the coordinates `u+v=xi`, `v-u=d`, the binomial identity yields

\[
\boxed{
\widehat{\mathcal L_K}(\xi)
=2^{1-K}\sum_{\ell=0}^{m}
 {K\choose 2\ell+1}
 \xi^{K-2\ell-1}\Lambda_{2\ell+2}(\xi).
}
\tag{L-106500.3}

Every power of `xi` in (L-106500.3) is even.  Thus the positivity is also a
finite positive combination of the existing current chaoses.

For the conclusion-facing fifth derivative,

\[
\boxed{
\widehat{\mathcal L_5}(\xi)
={1\over16}
\left(
 5\xi^4\Lambda_2(\xi)
 +10\xi^2\Lambda_4(\xi)
 +\Lambda_6(\xi)
\right)\ge0.
}
\tag{L-106500.4}

## 2. All-order positive cross current

For `h>0`, put `F_h(t)=F(t+ih)` and define

\[
\boxed{
J_{K,h}(t)
=(-1)^m\operatorname{Im}
\left(F_h(t)\overline{F_h^{(K)}(t)}\right).
}
\tag{L-106500.5}

A direct upper/lower-boundary Fourier calculation gives

\[
\boxed{
\widehat J_{K,h}(\xi)
={1\over2}\int_{
\mathbb R}
 (v^K-u^K)\sinh\!\bigl(h(v-u)\bigr)
 \Phi(u)\Phi(v)\,du
\ge0,
\qquad v=\xi-u.
}
\tag{L-106500.6}

Again the two factors have the same sign.  Expanding the hyperbolic sine by
monotone convergence gives

\[
\boxed{
\widehat J_{K,h}
=\sum_{r=0}^{\infty}
 {h^{2r+1}\over(2r+1)!}\Gamma_{K,2r+2},
}
\tag{L-106500.7}

where

\[
\boxed{
\Gamma_{K,2r+2}(\xi)
={1\over2}\int
 (v^K-u^K)(v-u)^{2r+1}
 \Phi(u)\Phi(v)\,du
\ge0.
}
\tag{L-106500.8}

The first chaos is exactly

\[
\boxed{
\Gamma_{K,2}=\widehat{\mathcal L_K},
\qquad
\widehat J_{K,h}\ge h\widehat{\mathcal L_K}.
}
\tag{L-106500.9}

At `K=1`, equations (L-106500.5)--(L-106500.9) are precisely the
current–Turan hierarchy of `L-105620`.

## 3. Causal source contraction

Analytic translation gives

\[
\widehat{\mathcal L_K(\cdot+ih)}(\xi)
=e^{-h\xi}\widehat{\mathcal L_K}(\xi).
\]

Consequently, on the decaying positive-frequency channel,

\[
\boxed{
0\le
h e^{-h\xi}\widehat{\mathcal L_K}(\xi)
\le \widehat J_{K,h}(\xi),
\qquad \xi\ge0.
}
\tag{L-106500.10}

The reflected channel obeys the mirror inequality.  Therefore every
nonnegative diagonal weight `w` satisfies

\[
\boxed{
h^2\int_0^\infty
 w(\xi)e^{-2h\xi}
 |\widehat{\mathcal L_K}(\xi)|^2d\xi
\le
\int_0^\infty w(\xi)|\widehat J_{K,h}(\xi)|^2d\xi.
}
\tag{L-106500.11}

In particular `w(xi)=xi` gives the topology-sensitive Hankel/
`H^(1/2)` source contraction.

## 4. Scope

The theorem is a diagonal source theorem.  It does not identify the cross
current metric with the finite derivative-companion quotient, transport the
contraction through its variable all-pass phase, control finite-window
endpoints, or prove a new critical-line percentage.  Those noncommuting rows
remain explicit in `T-106500`.
