# L-107010 — One fixed box cascade realizes every finite Bertrand Fourier envelope

Claim ID: `L-107010`  
Status: **PROVED EXACT ANALYTIC THEOREM**  
Created: 2026-08-27  
Depends on: `L-107000`; the fixed source-faithful beta band of PR #758  
RH status: **not assumed**

For \(x\ge1\), define softened iterated logarithms

\[
 L_1(x)=\log(e+x),
 \qquad
 L_{j+1}(x)=\log(e+L_j(x)).
\]

For an integer \(m\ge0\), put

\[
 \boxed{
 W_m(x)
 =
 \left(\prod_{j=1}^{m}L_j(x)\right)L_{m+1}(x)^2,
 }
 \tag{L-107010.1}
\]

with the empty product equal to one. The corresponding Bertrand series

\[
 Z_m
 =
 \sum_{n\ge1}\frac1{nW_m(n)}
 \tag{L-107010.2}
\]

converges. This is the usual iterated-log integral test: after \(m+1\)
successive logarithmic substitutions, the last integral is
\(\int du/u^2\).

Fix \(\ell>0\) and allocate support lengths

\[
 \ell_m=\frac{\ell}{2^{m+1}}.
\]

For every \(m,n\), define

\[
 a_{m,n}
 =
 \frac{\ell_m}{Z_m}\frac1{nW_m(n)}
\]

and let \(\eta_{m,n}\) be the uniform probability density on
\([0,a_{m,n}]\).

## 1. One fixed causal probability law

The complete width sum is

\[
 \sum_{m,n}a_{m,n}
 =
 \sum_m\ell_m
 =
 \ell.
\]

Hence the infinite convolution

\[
 \boxed{
 \eta_{\ell,\mathrm{Ber}}
 =
 *_{m\ge0}\ *_{n\ge1}\eta_{m,n}
 }
 \tag{L-107010.3}
\]

exists as the law of a sum of independent nonnegative bounded random
variables and is supported in \([0,\ell]\).

Its Fourier--Laplace transform is the locally uniformly convergent entire
product

\[
 \boxed{
 \Phi_{\ell,\mathrm{Ber}}(s)
 =
 \prod_{m\ge0}\prod_{n\ge1}
 \frac{1-e^{-a_{m,n}s}}{a_{m,n}s}.
 }
 \tag{L-107010.4}
\]

Every factor has all zeros on \(\Re s=0\). Absolute convergence of the tail
product on compact sets therefore gives

\[
 \boxed{
 \Phi_{\ell,\mathrm{Ber}}(s)\ne0
 \qquad(\Re s>0).
 }
 \tag{L-107010.5}
\]

## 2. Simultaneous all-depth decay

Fix one depth \(m\). Ignore every factor in (L-107010.4) except the row with
that \(m\). Write

\[
 c_m=\ell_m/Z_m
\]

and, for sufficiently large \(|t|\), put

\[
 N_m(t)
 =
 \left\lfloor
 \frac{c_m|t|}{32W_m(|t|)}
 \right\rfloor.
\]

The functions \(W_m\) are increasing. Thus, for \(n\le N_m(t)\),

\[
 a_{m,n}|t|
 =
 \frac{c_m|t|}{nW_m(n)}
 \ge32.
\]

The corresponding box factor is at most \(1/16\) in modulus. Consequently

\[
 \boxed{
 |\Phi_{\ell,\mathrm{Ber}}(it)|
 \le
 C_m
 \exp\left\{
 -c'_m\frac{|t|}{W_m(|t|)}
 \right\}
 }
 \tag{L-107010.6}
\]

for every fixed \(m\), with constants depending only on \(m,\ell\).

Already the \(m=0\) row gives superpolynomial decay, so Fourier inversion can
be differentiated arbitrarily many times:

\[
 \boxed{
 \eta_{\ell,\mathrm{Ber}}
 \in C_c^\infty(\mathbf R),
 \quad
 \eta_{\ell,\mathrm{Ber}}\ge0,
 \quad
 \operatorname{supp}\eta_{\ell,\mathrm{Ber}}\subset[0,\ell],
 \quad
 \int\eta_{\ell,\mathrm{Ber}}=1.
 }
 \tag{L-107010.7}
\]

## 3. One native beta detector

With the source-locked compact boundary kernel \(K_{\rm bd}\), fixed
difference order \(r\ge1\), and fixed \(\varepsilon>0\), define

\[
 B_{r,\mathrm{Ber}}
 =
 \eta_{\ell,\mathrm{Ber}}
 *
 \Delta_\varepsilon^rK_{\rm bd}.
 \tag{L-107010.8}
\]

It is one fixed nonzero compact causal \(C^\infty\) detector. Its multiplier is

\[
 \widehat B_{r,\mathrm{Ber}}(s)
 =
 \Phi_{\ell,\mathrm{Ber}}(s)
 \left(\frac{1-e^{-\varepsilon s}}{\varepsilon}\right)^r
 \widehat K_{\rm bd}(s).
\]

The new factor is nonzero in the complete open Mellin--Landau half-plane.
Therefore

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal E_{r,\mathrm{Ber}}(X)=X^{o(1)}
 }
 \tag{L-107010.9}
\]

for the literal native beta source
\(\beta=(\delta_1-\delta_{67})*\mu\).

## 4. Strict improvement down the ladder

For every fixed \(m\),

\[
 \frac{W_{m+1}(x)}{W_m(x)}
 =
 \frac{L_{m+2}(x)^2}{L_{m+1}(x)}
 \longrightarrow0.
 \tag{L-107010.10}
\]

Thus one and the same detector has Fourier envelopes asymptotically stronger
than every prescribed finite depth in the Bertrand hierarchy.
