# L-91031 — The zeta screw kernel localizes through the causal Cauchy wavelet

Claim ID: `L-91031`  
Status: **PROPOSED COMPLETE EXACT SCREW/HARDY LOCALIZATION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91026`; Nakamura–Suzuki; Suzuki's zeta screw criterion  
RH status: **unproved**

## 1. Imported screw function

Let `g_zeta` be the explicit even function of Nakamura and Suzuki.  Their
published theorem gives

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 e^{g_\zeta(t)}\text{ is an infinitely divisible characteristic function}.
 }
 \tag{L-91031.1}
\]

Under RH,

\[
 \boxed{
 g_\zeta(t)=
 \sum_\gamma m_\gamma
 \frac{e^{-i\gamma t}-1}{\gamma^2},
 }
 \tag{L-91031.2}
\]

so the Lévy measure is

\[
 \nu_\zeta=
 \sum_\gamma\frac{m_\gamma}{\gamma^2}\delta_\gamma.
 \tag{L-91031.3}
\]

Suzuki's associated screw kernel is

\[
 \boxed{
 G_\zeta(t,u)=
 g_\zeta(t-u)-g_\zeta(t)-g_\zeta(-u)+g_\zeta(0).
 }
 \tag{L-91031.4}
\]

Its positivity on all compact smooth mean-zero tests is equivalent to RH.

The exact one-sided Laplace bridge is

\[
 \boxed{
 \int_0^\infty g_\zeta(t)e^{-\lambda t}dt
 =-\frac1{\lambda^2}
 \frac{\xi'}{\xi}\left(\frac12+\lambda\right),
 \qquad \Re\lambda>\frac12.
 }
 \tag{L-91031.5}
\]

Thus the heat, resolvent, radial-Pick, Cauchy and scattering-delay criteria in
the current stack are local transforms of one screw function.

## 2. Causal rational mother

Retain

\[
 \alpha=\frac{163-5\sqrt{561}}{28},
 \qquad
 \beta=\frac{163+5\sqrt{561}}{28}
\]

and define

\[
 \boxed{
 \Psi_a(u)=\sqrt{378}\,a^3
 \frac{u(u+i\sqrt\alpha a)(u+i\sqrt\beta a)}
 {(u+ia)^2(u+2ia)^2(u+4ia)^2}.
 }
 \tag{L-91031.6}
\]

Its inverse Fourier transform is causal; the conjugate boundary function is
anti-causal.  The exact identities are

\[
 \boxed{
 |\Psi_a(u)|^2=d_a(u)-\frac1{16}d_{2a}(u),
 \qquad
 \Psi_a(u)=\Psi_1(u/a).
 }
 \tag{L-91031.7}
\]

The first identity is the one-complex-port form of the three-square Cauchy
residual in `L-91022`.

## 3. Exact admissibility constant

The mother has one vanishing moment and

\[
 \boxed{
 \int_0^\infty\frac{|\Psi_1(u)|^2}{u}du
 =\frac{15}{16}\log2.
 }
 \tag{L-91031.8}
\]

With `y=u^2`, twice the integral is the integral over `[0,infinity)` of

\[
 \frac{378y^2+4401y+6048}
 {(y+1)^2(y+4)^2(y+16)^2}.
\]

The partial fraction decomposition is

\[
\begin{aligned}
 &\frac1{y+1}+\frac1{(y+1)^2}
 -\frac{17}{16(y+4)}-\frac{17}{4(y+4)^2}\\
 &\qquad+\frac1{16(y+16)}+\frac1{(y+16)^2}.
\end{aligned}
\]

The double-pole integrals cancel and the logarithmic terms give (L-91031.8).

## 4. Mean-zero Hardy wavelets

For an orientation `epsilon in {+,-}`, let

\[
 \Psi_a^+(u)=\Psi_a(u),
 \qquad
 \Psi_a^-(u)=\overline{\Psi_a(u)}
\]

on the real line.  For a carrier `x`, define

\[
 \boxed{
 \widehat f_{a,x}^\epsilon(\lambda)
 =\lambda\Psi_a^\epsilon(\lambda-x).
 }
 \tag{L-91031.9}
\]

The factor `lambda` gives

\[
 \int_\mathbb R f_{a,x}^\epsilon(t)dt=0.
\]

The `+` family is supported on the positive half-line and the `-` family on the
negative half-line, with exponential decay governed by `a`.

## 5. Full cross-Gram localization

For mean-zero tests define

\[
 \mathfrak Q_\zeta(f,h)=
 \iint g_\zeta(t-u)f(t)\overline{h(u)}dtdu.
 \tag{L-91031.10}
\]

Under RH, (L-91031.2) gives

\[
 \mathfrak Q_\zeta(f,h)=
 \sum_\gamma\frac{m_\gamma}{\gamma^2}
 \widehat f(\gamma)\overline{\widehat h(\gamma)}.
\]

For the wavelets in (L-91031.9), the factors `gamma` cancel the Lévy weight.
Thus

\[
 \boxed{
\begin{aligned}
 \mathbb K((\epsilon,a,x),(\delta,b,y))
 &=\mathfrak Q_\zeta(f_{a,x}^\epsilon,f_{b,y}^\delta)\\
 &=\sum_\gamma m_\gamma
 \Psi_a^\epsilon(\gamma-x)
 \overline{\Psi_b^\delta(\gamma-y)}.
\end{aligned}}
 \tag{L-91031.11}
\]

Under RH this is one literal Gram kernel across scales, carriers and Hardy
orientations.

## 6. Resident Cauchy recurrence is one diagonal

At equal scales and carriers,

\[
 \boxed{
 \mathbb K((+,a,x),(+,a,x))
 =\sum_\gamma m_\gamma|\Psi_a(\gamma-x)|^2
 =a^4\mathcal R_x(a),
 }
 \tag{L-91031.12}
\]

where `R_x(a)` is the recurrence residual of `T-91005`.

The scalar route therefore tests only the diagonal of the stronger cross-Gram.

## 7. Fixed safe-scale arithmetic availability

If `a>1/2`, each physical source is a finite exponential-polynomial
combination with rates `a,2a,4a`.  Its Guinand–Weil prime series is absolutely
convergent, and each matrix entry is a finite combination of safe
`-zeta'/zeta` derivatives in `Re(s)>1`, plus explicit gamma/pole terms.

No moving prime cutoff, pair-correlation asymptotic or Hardy–Littlewood input
is needed to define the kernel.

## 8. Boundary

Closed here, subject to independent review:

```text
published screw/Lévy criterion imported with source lock;
exact Laplace bridge to xi'/xi;
causal and anti-causal rational mothers;
exact residual modulus and scale covariance;
exact admissibility constant (15/16)log2;
full cross-scale screw Gram under RH;
Cauchy recurrence identified as one diagonal;
absolute Euler availability at every fixed a>1/2.
```

Open:

```text
prime-side positivity of the complete two-Hardy-channel Gram;
completed Poisson-Fock/Hardy conservative realization;
RH.
```
