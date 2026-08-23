# L-105200 — Natural-window Gaussian saddle for the Xi derivative companions

Claim ID: `L-105200`  
Status: **PROPOSED UNCONDITIONAL ASYMPTOTIC THEOREM; exact analytic proof supplied**  
Created: 2026-08-23  
Depends on: PR #716 `L-104504`; PR #720 `L-104516--L-104517` at `10bba584c01277e880aaa21e1fea09f396ca7246`  
RH status: **not assumed**

## 1. Native one-sided companions

Use the classical positive Fourier representation

\[
\Xi(z)=2\int_0^\infty \Phi(u)\cos(zu)\,du,
\qquad \Phi(u)>0,
\]

and put

\[
M_m=\int_0^\infty u^m\Phi(u)\,du,
\qquad
d\nu_m(u)=M_m^{-1}u^m\Phi(u)\,du,
\]

\[
A_m(z)=\int_0^\infty e^{izu}\,d\nu_m(u).
\tag{L-105200.1}
\]

For large `m`, let `w_m` be the unique maximizer of

\[
S_m(u)=m\log u+\log\Phi(u),
\]

and define the local Gaussian width

\[
\boxed{
 a_m=\bigl(-S_m''(w_m)\bigr)^{-1/2}.
}
\tag{L-105200.2}
\]

The saddle estimates in `L-104504` give, uniformly in every constant-fraction
band `eta N <= m <= N`,

\[
w_m={1\over2}\log m+O(\log\log m),
\tag{L-105200.3}
\]

\[
\boxed{
 a_m^2={w_m\over2m}\left(1+O(1/w_m)\right),
}
\tag{L-105200.4}
\]

and

\[
w_{m+1}-w_m=O_\eta(N^{-1}),
\qquad
{a_{m+1}\over a_m}=1+o_\eta(1).
\tag{L-105200.5}
\]

## 2. Gaussian approximation on the full natural window

Fix

\[
0<\eta<1,
\qquad C>0,
\qquad H>0.
\]

Then

\[
\boxed{
\sup_{\substack{\eta N\le m\le N\\
 |\Re z|\le C/a_m,\ |\Im z|\le H}}
\left|
 e^{-iw_mz+a_m^2z^2/2}A_m(z)-1
\right|
\longrightarrow0.
}
\tag{L-105200.6}
\]

This replaces the condition

\[
T_Na_m\longrightarrow0
\]

from `L-104517` by the sharp fixed natural-window condition

\[
T_Na_m\le C.
\]

The constant `C` is arbitrary but fixed.

## 3. Proof

Set

\[
u=w_m+a_mx.
\]

The large-`u` expansion of `log Phi` used in `L-104504` gives, uniformly for
`eta N <= m <= N`,

\[
S_m'''(w_m)=O_\eta(N/\log N),
\]

and therefore

\[
a_m^3S_m'''(w_m)
=O_\eta\!\left(\sqrt{\log N/N}\right)=o(1).
\tag{L-105200.7}
\]

The same bound holds on every fixed `x`-compact after replacing `w_m` by
`w_m+a_mx`. Taylor's theorem and the definition of `a_m` therefore give

\[
S_m(w_m+a_mx)-S_m(w_m)
=-{x^2\over2}+o_{\eta,R}(1)
\tag{L-105200.8}
\]

uniformly for `|x|<=R`.

The concavity and tail estimates already proved in `L-104504` imply a uniform
integrable majorant. More precisely, after increasing `N_0(eta)`, there are
absolute `c,C_0>0` such that

\[
S_m(w_m+a_mx)-S_m(w_m)\le-cx^2
\]

whenever `|a_mx|<=1`, while the complementary part has exponentially small
mass relative to the central Laplace mass. Consequently the normalized laws
of

\[
X_m={u-w_m\over a_m}
\]

converge in exponentially weighted `L^1` to the standard Gaussian density,
uniformly in the whole band.

Now write

\[
t=a_mz.
\]

On the domain in (L-105200.6), `|Re t|<=C` and
`|Im t|<=a_mH=o(1)`. Uniform dominated convergence gives

\[
\int e^{itx}\,d\mathbb P(X_m\in dx)
=e^{-t^2/2}+o_{\eta,C,H}(1)
\]

uniformly on that compact complex `t`-domain. Since

\[
A_m(z)=e^{iw_mz}\mathbb E(e^{iz(u-w_m)}),
\]

this is exactly (L-105200.6).

Formula (L-105200.4) follows by substituting the saddle equation

\[
2\pi e^{2w_m}={m\over w_m}+O(1)
\]

into

\[
-S_m''(w_m)
={m\over w_m^2}+4\pi e^{2w_m}+O(e^{-2w_m}).
\]

The adjacent relations in (L-105200.5) follow from the implicit-function
formula for the saddle and from (L-105200.4).

## 4. Xi derivative model

The exact reflected companion identity of `L-104516` now gives

\[
\boxed{
\Xi^{(m)}(z)
=2M_m e^{-a_m^2z^2/2}
\left[
\cos\!\left(w_mz+{m\pi\over2}\right)
+\varepsilon_{m,N}(z)
\right],
}
\tag{L-105200.9}
\]

where, after division by the usual dominant exponential in `|Im z|`,

\[
\sup_{\eta N\le m\le N}
\sup_{|\Re z|\le C/a_m,\ |\Im z|\le H}
|\varepsilon_{m,N}(z)|\longrightarrow0.
\tag{L-105200.10}
\]

The Gaussian factor is zero-free. Therefore the complete zero geometry on the
natural window is governed by the trigonometric factor, not merely on a
little-`o` subwindow.

## 5. Scope

The theorem is a fixed-`C` central-limit saddle theorem. It does not claim a
moderate-deviation estimate for `C=C_N -> infinity`, and it does not descend
from high derivative order to a fixed derivative. Those are separate gates.
