# L-106602 — Carrier-matched companions annihilate a monochromatic endpoint block

Claim ID: `L-106602`  
Status: **PROVED EXACT CALIBRATION**  
Created: 2026-08-26  
Depends on: `L-106600`  
RH status: **not assumed**

Let

\[
F(t)=A\cos(\omega t+\phi),
\qquad
A\ne0,\quad \omega>0,
\]

and let \(K=2m+1\) be odd. Choose the positive companion scale

\[
a=\frac1\omega .
\]

Then

\[
F-iaF'=Ae^{i(\omega t+\phi)},
\qquad
F+iaF'=Ae^{-i(\omega t+\phi)}.
\]

Moreover

\[
F^{(K)}
=(-1)^{m+1}A\omega^K\sin(\omega t+\phi),
\]

so

\[
F^{(K)}+iaF^{(K+1)}
=i(-1)^{m+1}A\omega^Ke^{-i(\omega t+\phi)}
\]

and

\[
F^{(K)}-iaF^{(K+1)}
=-i(-1)^{m+1}A\omega^Ke^{i(\omega t+\phi)}.
\]

Consequently

\[
\boxed{U_{K,1/\omega}\equiv-1.}
\tag{L-106602.1}
\]

After common-factor reduction, both inner divisors are empty and therefore

\[
\boxed{\|H_{U_{K,1/\omega}}\|_{\mathcal S_2}^2=0.}
\tag{L-106602.2}
\]

This is the exact carrier calibration for the adaptive-scale programme.

## Slowly modulated first companion

If

\[
F(t)=A(t)\cos\phi(t),
\qquad
a(t)\phi'(t)=1,
\qquad
\varepsilon_A(t)=a(t)\frac{A'(t)}{A(t)},
\]

then the first companion has the exact residual form

\[
\boxed{
\begin{aligned}
F-iaF'&=A\left(e^{i\phi}-i\varepsilon_A\cos\phi\right),\\
F+iaF'&=A\left(e^{-i\phi}+i\varepsilon_A\cos\phi\right).
\end{aligned}
}
\tag{L-106602.3}
\]

Thus a phase-speed scale converts the first endpoint error into pure amplitude
modulation. No analogous statement for the fifth endpoint is asserted
without a common phase representation for \(F^{(5)}\).

For Xi, the eventual positive analytic Riemann--Siegel phase-speed reciprocal
is therefore a concrete candidate scale, not a proved estimate.
