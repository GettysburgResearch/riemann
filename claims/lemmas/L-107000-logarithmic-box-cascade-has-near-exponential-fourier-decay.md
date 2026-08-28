# L-107000 — A logarithmic box cascade has near-exponential Fourier decay

Claim ID: `L-107000`  
Status: **PROVED EXACT ANALYTIC THEOREM**  
Created: 2026-08-27  
Depends on: PR #758's fixed beta band-pass theorem  
RH status: **not assumed**

Fix \(\ell>0\). Put

\[
u_j=\frac1{j\log^2(ej)},
\qquad
Z_0=\sum_{j\ge1}u_j<\infty,
\qquad
a_j=\frac{\ell}{Z_0}u_j.
\tag{L-107000.1}
\]

Then \(\sum_j a_j=\ell\). Let

\[
\eta_j(u)=\frac1{a_j}\mathbf1_{[0,a_j]}(u)
\]

and let \(\eta_{\ell,\log}\) be the infinite convolution of the probability
measures \(\eta_j(u)\,du\).

## 1. Compact smooth probability density

If \(U_j\) are independent and uniform on \([0,a_j]\), then
\(\sum_j U_j\) converges and lies in \([0,\ell]\). Its law is the weak limit
of the finite convolutions and has Fourier--Laplace transform

\[
\boxed{
\Phi_{\ell,\log}(s)
=
\prod_{j\ge1}
\frac{1-e^{-a_js}}{a_js}.
}
\tag{L-107000.2}
\]

The product converges locally uniformly because \(\sum_j a_j<\infty\).
Every factor is entire after removing its value at zero. A zero of one factor
satisfies \(e^{-a_js}=1\), hence lies on \(\Re s=0\). The convergent tail
product is nonzero. Therefore

\[
\boxed{
\Phi_{\ell,\log}(s)\ne0
\qquad(\Re s>0).
}
\tag{L-107000.3}
\]

## 2. Near-exponential Fourier envelope

For real \(t\),

\[
\left|
\frac{1-e^{-ia_jt}}{ia_jt}
\right|
\le
\min\left(1,\frac2{a_j|t|}\right).
\tag{L-107000.4}
\]

Write

\[
c_\ell=\frac{\ell}{Z_0},
\qquad
L(t)=\log(e+|t|),
\qquad
N(t)=
\left\lfloor
\frac{c_\ell |t|}{16L(t)^2}
\right\rfloor.
\]

For sufficiently large \(|t|\), one has \(N(t)\le |t|\). If \(j\le N(t)\),
then \(\log(ej)\le L(t)\) and

\[
a_j|t|
=
\frac{c_\ell|t|}
{j\log^2(ej)}
\ge16.
\]

Each of the first \(N(t)\) factors in (L-107000.2) is therefore at most
\(1/8\) in modulus. Hence there are constants \(c,C,T_0>0\), depending only
on \(\ell\), for which

\[
\boxed{
|\Phi_{\ell,\log}(it)|
\le
C\exp\left\{
-\frac{c|t|}{\log^2(e+|t|)}
\right\}
\qquad(|t|\ge T_0).
}
\tag{L-107000.5}
\]

This dominates every negative power. Fourier inversion may therefore be
differentiated arbitrarily many times. The weak limiting law has a density
and

\[
\boxed{
\eta_{\ell,\log}\in C_c^\infty(\mathbf R),
\quad
\eta_{\ell,\log}\ge0,
\quad
\operatorname{supp}\eta_{\ell,\log}\subset[0,\ell],
\quad
\int\eta_{\ell,\log}=1.
}
\tag{L-107000.6}
\]

## 3. Source-faithful beta band

Let \(K_{\rm bd}\), \(\beta(n)\), \(\Delta_\varepsilon\), and the fixed
finite-difference order \(r\ge1\) be exactly those frozen by PR #758. Define

\[
\boxed{
B_{r,\log}
=
\eta_{\ell,\log}*
\Delta_\varepsilon^rK_{\rm bd}.
}
\tag{L-107000.7}
\]

Then \(B_{r,\log}\) is one fixed nonzero compact \(C^\infty\) beta detector.
Its transform is

\[
\widehat B_{r,\log}(s)
=
\Phi_{\ell,\log}(s)
\left(\frac{1-e^{-\varepsilon s}}{\varepsilon}\right)^r
\widehat K_{\rm bd}(s).
\tag{L-107000.8}
\]

Both newly inserted factors are nonzero in \(\Re s>0\). Hence the new
smoother cancels no hypothetical reciprocal-zeta pole in the open
Mellin--Landau half-plane. The fixed-detector equivalence survives:

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\mathcal E_{r,\log}(X)=X^{o(1)},
}
\tag{L-107000.9}
\]

where

\[
\mathcal E_{r,\log}(X)
=
\int_{\mathbf R}
\left|
\sum_{n\le X}
\frac{\beta(n)}{\sqrt n}
B_{r,\log}(u-\log n)
\right|^2du.
\]

## 4. Almost-logarithmic exterior window

Put

\[
D_X(t)
=
\sum_{n\le X}\frac{\beta(n)}{n^{1/2+it}}.
\]

The complete beta source has the unconditional bound
\(|D_X(t)|\le4\sqrt X\). From (L-107000.5), for every \(A>0\) there is a
constant \(C_A\) such that, with

\[
\boxed{
T_A(X)
=
C_A\log(eX)
\bigl[\log\log(e^eX)\bigr]^2,
}
\tag{L-107000.10}
\]

one has

\[
\boxed{
\frac1{2\pi}
\int_{|t|\ge T_A(X)}
|\widehat B_{r,\log}(it)|^2
|D_X(t)|^2\,dt
=
O_A(X^{-A}).
}
\tag{L-107000.11}
\]

The proof uses only the trivial beta bound and the elementary tail estimate

\[
\int_T^\infty
\exp\left\{-c\,t/\log^2(et)\right\}dt
\ll
\log^2(eT)
\exp\left\{-c' T/\log^2(eT)\right\}.
\]

No Möbius cancellation enters the exterior-frequency theorem.
