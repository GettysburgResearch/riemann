# L-91029 — The zeta screw kernel localizes through the causal Cauchy spectral factor

Claim ID: `L-91029`  
Status: **PROPOSED COMPLETE EXACT SCREW/HARDY LOCALIZATION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91026`; Nakamura--Suzuki, arXiv:2306.08317; Suzuki, JLMS 108 (2023), 1448--1487  
RH status: **unproved**

## 1. The imported screw function

For `t>=0`, let

\[
\begin{aligned}
 g_\zeta(t)={}&-4(e^{t/2}+e^{-t/2}-2)
 +\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n)\\
 &-\frac t2\left(\psi(1/4)-\log\pi\right)\\
 &+\frac14\left[
 e^{-t/2}\Phi(e^{-2t},2,1/4)-\Phi(1,2,1/4)
 \right],
\end{aligned}
 \tag{L-91029.1}
\]

and extend it evenly to the real line.  Here `psi` is the digamma function and
`Phi` is the Hurwitz--Lerch function.

Nakamura and Suzuki prove

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 e^{g_\zeta(t)}\text{ is an infinitely divisible characteristic function}.
 }
 \tag{L-91029.2}

Their exact zero expansion is

\[
 \boxed{
 g_\zeta(t)
 =\sum_\gamma m_\gamma
  \frac{e^{-i\gamma t}-1}{\gamma^2},
 }
 \tag{L-91029.3}

where `gamma` runs over the centred zeros of `xi(1/2-iz)`, generally complex.
Under RH all `gamma` are real and (L-91029.3) is a Levy--Khintchine exponent
with positive Levy measure

\[
 \nu_\zeta
 =\sum_\gamma\frac{m_\gamma}{\gamma^2}\delta_\gamma.
 \tag{L-91029.4}

Equivalently, the screw kernel

\[
 \boxed{
 G_\zeta(t,u)
 =g_\zeta(t-u)-g_\zeta(t)-g_\zeta(-u)+g_\zeta(0)
 }
 \tag{L-91029.5}

is positive semidefinite on the real line exactly under RH.  This is Suzuki's
screw-function form of Weil positivity.

## 2. Exact Laplace bridge to the completed logarithmic derivative

Nakamura--Suzuki's one-sided Fourier identity is

\[
 \int_0^\infty g_\zeta(t)e^{izt}dt
 =\frac1{z^2}\frac{\xi'}{\xi}\left(\frac12-iz\right),
 \qquad \Im z>\frac12.
 \tag{L-91029.6}

Put `z=i lambda`.  Then, for `Re(lambda)>1/2`,

\[
 \boxed{
 \int_0^\infty g_\zeta(t)e^{-\lambda t}dt
 =-\frac1{\lambda^2}
  \frac{\xi'}{\xi}\left(\frac12+\lambda\right).
 }
 \tag{L-91029.7
}

Thus the completed radial log derivative, the Cauchy soft count and the
scattering delay of `L-91023` are differential images of one scalar screw
function.  The heat, resolvent, Pick and Cauchy criteria in the current stack
are localizations of the same conditionally positive kernel.

## 3. The causal residual mother

Retain the algebraic constants

\[
 \alpha=\frac{163-5\sqrt{561}}{28},
 \qquad
 \beta=\frac{163+5\sqrt{561}}{28},
 \qquad \alpha\beta=16.
\]

For `a>0`, define the causal rational spectral factor of `L-91026`:

\[
 \boxed{
 \Psi_a(u)=\sqrt{378}\,a^3
 \frac{u(u+i\sqrt\alpha a)(u+i\sqrt\beta a)}
 {(u+ia)^2(u+2ia)^2(u+4ia)^2}.
 }
 \tag{L-91029.8}

Its poles lie in the lower half-plane, and its inverse Fourier transform is a
one-sided exponential polynomial supported on `t>=0`.  Put on the real axis

\[
 \Psi_a^+(u)=\Psi_a(u),
 \qquad
 \Psi_a^-(u)=\overline{\Psi_a(u)}.
 \tag{L-91029.9}

The second orientation is anti-causal.

The exact scale covariance is

\[
 \boxed{
 \Psi_a(u)=\Psi_1(u/a).
 }
 \tag{L-91029.10}

Moreover,

\[
 \boxed{
 |\Psi_a(u)|^2
 =d_a(u)-\frac1{16}d_{2a}(u),
 }
 \tag{L-91029.11}

where `d_a` is the dyadic Cauchy detail of `L-91022`.

## 4. Exact admissibility constant

The mother has one vanishing moment and satisfies the Calderon integrability
condition.  In fact

\[
 \boxed{
 \int_0^\infty\frac{|\Psi_1(u)|^2}{u}du
 =\frac{15}{16}\log2.
 }
 \tag{L-91029.12}

To see this, put `y=u^2`.  Then twice the left side is

\[
 \int_0^\infty
 \frac{378y^2+4401y+6048}
 {(y+1)^2(y+4)^2(y+16)^2}dy.
\]

The exact partial fraction decomposition is

\[
\begin{aligned}
 {}&\frac1{y+1}+\frac1{(y+1)^2}
 -\frac{17}{16(y+4)}-\frac{17}{4(y+4)^2}\\
 &\qquad+\frac1{16(y+16)}+\frac1{(y+16)^2}.
\end{aligned}
 \tag{L-91029.13}

The double-pole integrals cancel, while the logarithmic terms give
`15 log(2)/8`; division by two proves (L-91029.12).

## 5. Mean-zero Hardy wavelets

Use the Fourier convention

\[
 \widehat f(\lambda)=\int_\mathbb R f(t)e^{-i\lambda t}dt.
\]

For a carrier `x` and orientation `epsilon in {+,-}`, define

\[
 \boxed{
 \widehat f_{a,x}^\epsilon(\lambda)
 =\lambda\Psi_a^\epsilon(\lambda-x).
 }
 \tag{L-91029.14}

Since the right side vanishes at `lambda=0`,

\[
 \int_\mathbb R f_{a,x}^\epsilon(t)dt=0.
 \tag{L-91029.15}

The `+` wavelet is supported on the positive half-line and the `-` wavelet on
the negative half-line.  Both decay exponentially at rate `a`.

## 6. Full cross-Gram localization

For mean-zero test functions, the subtraction terms in (L-91029.5) vanish.
Define

\[
 \mathfrak Q_\zeta(f,h)
 =\iint_{\mathbb R^2}
 g_\zeta(t-u)f(t)\overline{h(u)}dtdu.
 \tag{L-91029.16}

If RH holds, insert (L-91029.3) and use Fourier inversion:

\[
 \mathfrak Q_\zeta(f,h)
 =\sum_\gamma\frac{m_\gamma}{\gamma^2}
  \widehat f(\gamma)\overline{\widehat h(\gamma)}.
 \tag{L-91029.17}

For the wavelets (L-91029.14), the factors `gamma` cancel the Levy weight.
Hence

\[
 \boxed{
\begin{aligned}
 \mathbb K((\epsilon,a,x),(\delta,b,y))
 &:={\mathfrak Q}_\zeta(f_{a,x}^\epsilon,f_{b,y}^\delta)\\
 &=\sum_\gamma m_\gamma
 \Psi_a^\epsilon(\gamma-x)
 \overline{\Psi_b^\delta(\gamma-y)}.
\end{aligned}}
 \tag{L-91029.18}

Thus, under RH, `mathbb K` is one literal Gram kernel across all scales,
carriers and causal orientations.

## 7. The resident recurrence is only the diagonal

Taking equal scales, carriers and the causal orientation gives

\[
 \boxed{
 \mathbb K((+,a,x),(+,a,x))
 =\sum_\gamma m_\gamma|\Psi_a(\gamma-x)|^2
 =a^4\mathcal R_x(a),
 }
 \tag{L-91029.19}

where `R_x(a)` is the three-square recurrence residual of `T-91005`.
Therefore the normalized sixteenfold recurrence sees only the diagonal of a
much stronger cross-scale, cross-carrier, two-Hardy-channel kernel.

This is the central change of proof coordinate:

```text
old target: every scalar dyadic gate is nonnegative;
new target: one fixed Hardy-wavelet Gram kernel is positive semidefinite.
```

## 8. Absolute prime-side availability at a safe scale

The screw function satisfies

\[
 g_\zeta(t)\ll e^{|t|/2-c\sqrt{|t|}}
\]

for some `c>0`.  If `a>1/2`, every wavelet in (L-91029.14) decays rapidly
enough for (L-91029.16) to converge absolutely.

Equivalently, its Guinand--Weil prime term is

\[
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 F(\log n),
\]

where `F` is a finite exponential-polynomial combination with decay
`O(poly(t)e^{-a t})`.  Hence the prime series converges absolutely for every
fixed `a>1/2`.  No growing cutoff, pair-correlation asymptotic or
Hardy--Littlewood input is needed to define any matrix entry.

## 9. Boundary

Closed here, subject to independent review:

```text
Nakamura--Suzuki screw/Levy criterion imported with source lock;
exact Laplace bridge to xi'/xi;
causal and anti-causal residual mothers;
exact residual square and scale covariance;
exact admissibility constant (15/16) log 2;
full cross-scale screw Gram under RH;
resident Cauchy recurrence identified as one diagonal;
absolute Euler availability at every fixed safe scale a>1/2.
```

Still open:

```text
prime-side positivity of the complete two-Hardy-channel Gram;
its realization as a conservative coupling of the Poisson Fock source and
  the completed gamma/scattering channel;
RH.
```
