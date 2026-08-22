# L-104517 — Uniform high-derivative Xi band and quantitative reverse-Rolle descent

Claim ID: `L-104517`  
Status: **PROVED FROM UNIFORM TILTED-FOURIER SADDLE CONCENTRATION**  
Created: 2026-08-22  
Depends on: `L-104504`, `L-104516`  
RH status: **not assumed**

Fix

\[
0<\eta<1,
\qquad
H>0.
\]

For the tilted probability

\[
d\nu_m(u)=M_m^{-1}u^m\Phi(u)\,du,
\]

let `w_m` be its saddle and let

\[
\sigma_m^2
=
\int (u-w_m)^2\,d\nu_m(u).
\]

The Laplace analysis used in `L-104504` is uniform for

\[
\eta N\le m\le N.
\]

In particular,

\[
w_m={1\over2}\log m+O(\log\log m),
\tag{L-104517.1}
\]

\[
\sigma_m\asymp\sqrt{\frac{\log m}{m}},
\tag{L-104517.2}
\]

and for fixed `H`,

\[
\int
e^{H|u-w_m|}|u-w_m|\,d\nu_m(u)
\ll_{\eta,H}
\sqrt{\frac{\log N}{\eta N}}
\tag{L-104517.3}
\]

uniformly in the entire band.

Let `T_N>=1` satisfy

\[
\boxed{
T_N\sqrt{\frac{\log N}{\eta N}}
\longrightarrow0.
}
\tag{L-104517.4}
\]

## 1. Uniform exponential model

For

\[
A_m(z)=\int e^{izu}\,d\nu_m(u)
\]

and

\[
|\Re z|\le T_N,\qquad |\Im z|\le H,
\]

one has

\[
\begin{aligned}
\left|
e^{-iw_mz}A_m(z)-1
\right|
&\le
|z|
\int e^{H|u-w_m|}|u-w_m|\,d\nu_m(u)\\
&=
o_{\eta,H}(1)
\end{aligned}
\tag{L-104517.5}
\]

uniformly for every integer `m` in `[eta N,N]`.

Consequently all canonical companions

\[
\mathscr E_m(z)=i^mM_mA_m(z)
\]

are zero-free in the complete box

\[
|\Re z|\le T_N,\qquad |\Im z|\le H
\tag{L-104517.6}
\]

for all sufficiently large `N`.

## 2. Simultaneous real-rootedness of an entire derivative band

By `L-104516.3`,

\[
\Xi^{(m)}(z)
=
i^mM_m
\left[
A_m(z)+(-1)^mA_m(-z)
\right].
\]

The model in (L-104517.5) is

\[
i^mM_m
\left[
e^{iw_mz}+(-1)^m e^{-iw_mz}
\right],
\]

which is a nonzero constant times `cos(w_m z)` for even `m` and
`sin(w_m z)` for odd `m`.

Choose disjoint disks of radius `rho/w_m`, with one fixed
`0<rho<pi/4`, around the model zeros.  On each disk boundary the model has a
uniform positive lower bound after division by the dominant exponential.
Equation (L-104517.5) and Rouché's theorem give exactly one Xi-derivative zero
in every disk.  On the complement,

\[
|\cos(x+iy)|^2=\cos^2x+\sinh^2y
\]

and the analogous sine identity exclude all additional zeros.

Because `Xi^(m)` is real entire, the unique zero in each
conjugation-symmetric disk is real.

Therefore

\[
\boxed{
\begin{gathered}
\text{for every }\eta\in(0,1)\text{ and every admissible }T_N,\\
\text{all zeros of }\Xi^{(m)}
\text{ in }|\Re z|\le T_N,\ |\Im z|\le H\\
\text{are real and simple, simultaneously for every }
\eta N\le m\le N,
\end{gathered}
}
\tag{L-104517.7}
\]

for all sufficiently large `N`.

This is a constant-fraction derivative-band theorem, not a fixed-order
statement.

## 3. Quantitative zero counts

Let

\[
N_m(T)
=
\#\{x\in[-T,T]:\Xi^{(m)}(x)=0\}.
\]

The same cellwise Rouché argument gives

\[
\boxed{
N_m(T_N)
=
{2w_mT_N\over\pi}+O(1)
}
\tag{L-104517.8}
\]

uniformly for `eta N<=m<=N`.

The saddle equation also gives

\[
w_m-w_{m-1}=O_\eta(N^{-1}),
\qquad
{w_{m-1}\over w_m}=1+o_\eta(1)
\tag{L-104517.9}
\]

uniformly across the band.  Hence

\[
\boxed{
\inf_{\eta N<m\le N}
{N_{m-1}(T_N)+O(1)\over N_m(T_N)}
\longrightarrow1.
}
\tag{L-104517.10}
\]

In particular, for every fixed `c<1`, all sufficiently large `N` satisfy

\[
\boxed{
N_{m-1}(T_N)
\ge
c\,N_m(T_N)-O(1)
\qquad
(\eta N<m\le N).
}
\tag{L-104517.11}
\]

If `T_N w_(eta N)->infinity`, the `O(1)` may be absorbed and

\[
N_{m-1}(T_N)\ge cN_m(T_N).
\]

This is an unconditional Xi-specific quantitative converse-Rolle theorem of
the kind suggested by Levinson's programme.  Indeed the local critical-line
proportion is exactly `1` for every derivative in the band, and the consecutive
real-zero counts transfer with any prescribed constant `c<1`.

## Scope firewall

The theorem does not descend to a fixed low derivative order as `N` tends to
infinity.  The examples in `R-104512` show that no source-free proportion
argument can bridge that remaining gap.  What has been proved is a uniform
constant-fraction **high-order band**, with a quantitative one-step descent
constant tending to one.
