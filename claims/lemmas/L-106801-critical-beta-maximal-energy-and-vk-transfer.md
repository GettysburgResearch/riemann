# L-106801 — The maximal compact beta energy has exponent \(2\Theta-1\) and inherits Vinogradov–Korobov decay

Claim ID: `L-106801`  
Status: **PROVED FROM L-106800, THE PINNED CRITICAL-LATTICE THEOREMS, AND THE CLASSICAL MERTENS BOUND**  
Created: 2026-08-27  
Depends on: `L-106800`; `FFPS_CRITICAL_BETA_FOURIER_LATTICE_COMPRESSION`; `FFPS_CRITICAL_BETA_SPECTRAL_WITNESS_PRINCIPLE`  
RH status: **not assumed**

Fix one compact infinite-smoother beta kernel \(B=B_{r,\infty}\). For
\(1\le Y\le X\), put

\[
H_Y(u)
=
\sum_{n\le Y}\frac{\beta(n)}{\sqrt n}B(u-\log n),
\qquad
\mathcal E_B(Y)=\int_{\mathbf R}|H_Y(u)|^2\,du,
\tag{L-106801.1}
\]

and define the maximal energy envelope

\[
\mathfrak E_B(X)=\max_{1\le Y\le X}\mathcal E_B(Y).
\tag{L-106801.2}
\]

## 1. Exact power exponent

Use the one common guarded period \(L_X\) for all \(Y\le X\). The pinned
Fourier-lattice theorem gives

\[
\mathcal E_B(Y)
=
\sum_{k\in\mathbf Z}
w_{k,X}|D_Y(t_{k,X})|^2,
\tag{L-106801.3}
\]

where

\[
w_{k,X}=\frac{|\widehat B(t_{k,X})|^2}{L_X},
\qquad
t_{k,X}=\frac{2\pi k}{L_X}.
\]

At the critical cutoff

\[
|k|\le K_*(X),
\qquad
K_*(X)
=
\exp\!\left(
\sqrt{(\log2)(\log X)}+O(\log\log X)
\right),
\tag{L-106801.4}
\]

the discarded energy is \(X^{o(1)}\), uniformly for \(Y\le X\).

For the retained modes,

\[
|t_{k,X}|
\le
\exp\!\left(\sqrt{(\log2)(\log X)}\right)=X^{o(1)}.
\]

The exact phase inequality of `L-106800.10`, the duplicate-67 inverse, the
bounded kernel transform and the subpower mode count imply

\[
\mathfrak E_B(X)
\le
X^{o(1)}
\left(1+\mathfrak M_0(X)^2\right).
\tag{L-106801.5}
\]

Conversely, for any fixed \(h\ne0\), its coordinate is retained for all
large \(X\), and

\[
\mathfrak E_B(X)
\ge
w_{h,X}\mathfrak D_h(X)^2.
\tag{L-106801.6}
\]

The low-frequency kernel expansion gives

\[
w_{h,X}
\asymp_{r,h}
L_X^{-(2r+1)}=X^{o(1)}
\tag{L-106801.7}
\]

with a subpower inverse. Equations (L-106800.9),
(L-106800.17), and (L-106801.5)--(L-106801.7) prove

\[
\boxed{
\operatorname{pexp}\mathfrak E_B
=
2\Theta-1.
}
\tag{L-106801.8}
\]

The same exponent is carried by the single fixed weighted beta harmonic

\[
\mathfrak W_{h,B}(X)
=
w_{h,X}\mathfrak D_h(X)^2:
\]

\[
\boxed{
\operatorname{pexp}\mathfrak W_{h,B}
=
2\Theta-1.
}
\tag{L-106801.9}
\]

## 2. Every zero-free half-plane is one scalar growth theorem

For every \(1/2\le\sigma\le1\), equations (L-106801.8)--(L-106801.9) give

\[
\boxed{
\zeta(s)\ne0\quad(\Re s>\sigma)
}
\]

if and only if, for every \(\epsilon>0\),

\[
\boxed{
\mathfrak W_{h,B}(X)
\ll_\epsilon X^{2\sigma-1+\epsilon},
}
\tag{L-106801.10}
\]

and equivalently

\[
\boxed{
\mathfrak E_B(X)
\ll_\epsilon X^{2\sigma-1+\epsilon}.
}
\tag{L-106801.11}
\]

At \(\sigma=1/2\) this is RH. More generally, a fixed power saving

\[
\mathfrak E_B(X)\ll X^{1-\delta+o(1)}
\]

would imply the zero-free half-plane

\[
\Re s>1-\frac{\delta}{2}.
\tag{L-106801.12}
\]

This is a graded detector theorem, not merely an RH equivalence.

## 3. Unconditional Vinogradov–Korobov saving

The classical unconditional Mertens estimate supplies a constant \(c_0>0\)
such that

\[
M(x)
\ll
x\exp\!\left(
-c_0\Psi(x)
\right),
\qquad
\Psi(x)
=
(\log x)^{3/5}(\log\log x)^{-1/5}.
\tag{L-106801.13}
\]

Two-way Abel summation, with a split at \(x^{1/2}\), gives a constant
\(c_1>0\) such that

\[
\mathfrak M_0(X)
\ll
\sqrt X\exp(-c_1\Psi(X)).
\tag{L-106801.14}
\]

On the whole critical frequency window, the phase-transport loss is at most

\[
\exp\!\left(O(\sqrt{\log X})\right).
\]

Since

\[
\frac{\Psi(X)}{\sqrt{\log X}}
=
\frac{(\log X)^{1/10}}{(\log\log X)^{1/5}}
\longrightarrow\infty,
\tag{L-106801.15}
\]

this loss, the subpower mode count, the duplicate-67 constants, and every
fixed kernel factor are absorbed into a smaller positive constant.
Consequently there is \(c_B>0\) such that

\[
\boxed{
\mathfrak E_B(X)
\ll_B
X\exp\!\left(-c_B\Psi(X)\right).
}
\tag{L-106801.16}
\]

Likewise, for every fixed \(h\ne0\),

\[
\boxed{
\mathfrak W_{h,B}(X)
\ll_{B,h}
X\exp\!\left(-c_B\Psi(X)\right).
}
\tag{L-106801.17}
\]

The unconditional critical-lattice tail is \(X^{o(1)}\), which is much
smaller than the right side of (L-106801.16) for large \(X\).

Equations (L-106801.16)--(L-106801.17) transfer the strongest classical
zero-free-region shape to the exact source-faithful beta detector. They do
not establish a fixed power saving, RH, or any new zero-free half-plane.
