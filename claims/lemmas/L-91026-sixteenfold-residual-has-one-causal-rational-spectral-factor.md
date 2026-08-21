# L-91026 — The sixteenfold Cauchy residual has one causal rational spectral factor

Claim ID: `L-91026`  
Status: **PROPOSED COMPLETE EXACT HARDY/SPECTRAL-FACTOR THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91022`  
RH status: **unproved**

## 1. Factorisation constants

Let

\[
 \boxed{
 \alpha={163-5\sqrt{561}\over28},
 \qquad
 \beta ={163+5\sqrt{561}\over28}.
 }
 \tag{L-91026.1}
\]

Then

\[
 \alpha>0,
 \qquad \beta>0,
 \qquad
 \alpha+\beta={163\over14},
 \qquad
 \alpha\beta=16.
 \tag{L-91026.2}
\]

The residual numerator in `L-91022` satisfies

\[
 \boxed{
 378y^2+4401y+6048
 =378(y+\alpha)(y+\beta).
 }
 \tag{L-91026.3}
\]

## 2. One scalar spectral factor

For `a>0`, define

\[
 \boxed{
 \Psi_a(u)
 =\sqrt{378}\,a^3
 {u(u+i\sqrt\alpha\,a)(u+i\sqrt\beta\,a)
  \over
  (u+ia)^2(u+2ia)^2(u+4ia)^2}.
 }
 \tag{L-91026.4}
\]

For real `u`,

\[
\begin{aligned}
 |\Psi_a(u)|^2
 ={}&378a^6
 {u^2(u^2+\alpha a^2)(u^2+\beta a^2)
  \over
  (u^2+a^2)^2(u^2+4a^2)^2(u^2+16a^2)^2}\\
 ={}&\boxed{
 d_a(u)-{1\over16}d_{2a}(u).
 }
\end{aligned}
 \tag{L-91026.5}
\]

Thus the three real square ports of `L-91022` are the realification of one
complex scalar Hardy port.

## 3. Causality and decay

With the Fourier convention of `L-91022`, all poles of `Psi_a` lie at

\[
 -ia,-2ia,-4ia
\]

and have order two.  Therefore the inverse Fourier transform `psi_a` is
supported on one half-line and has the explicit form

\[
 \boxed{
 \psi_a(t)=\mathbf1_{t\ge0}
 \sum_{c\in\{1,2,4\}}(A_c+B_ct)e^{-cat},
 }
 \tag{L-91026.6}
\]

for algebraic constants `A_c,B_c` determined by residues.  In particular

\[
 \psi_a\in L^1\cap L^2,
 \qquad
 \int\psi_a(t)dt=\Psi_a(0)=0.
 \tag{L-91026.7}
\]

The spectral factor has

\[
 \Psi_a(u)=O_a(u^{-3}),
 \tag{L-91026.8}
\]

which explains the `u^(-6)` residual energy.

## 4. Exact autocorrelation

Let

\[
 \widetilde\psi_a(t)=\overline{\psi_a(-t)}.
\]

Then

\[
 \boxed{
 \mathfrak r_a
 =\psi_a*\widetilde\psi_a,
 }
 \tag{L-91026.9}
\]

where `mathfrak r_a` is the explicit three-exponential physical residual of
`L-91022.13`.

Hence for arbitrary carriers `x_j`,

\[
 \left(
 \widehat{\mathfrak r_a}(x_j-x_k)
 \right)_{j,k}
\]

is positive semidefinite, with a scalar Hardy-space Gram representation.  No
matrix polarization choice remains.

## 5. One-Weil-square form of the recurrence residual

Shift the spectral factor by a carrier `x`:

\[
 \Psi_{a,x}(u)=\Psi_a(u-x).
\]

The zero-side residual in `T-91005` is exactly the sum of the squared
magnitudes

\[
 \boxed{
 \mathcal R_x(a)
 =a^{-4}\sum_\rho m_\rho
  |\Psi_a(\gamma_\rho-x)|^2
 }
 \tag{L-91026.10
}
\]

when all centred zero coordinates are real.  Thus the coefficient-one
recurrence is the positivity of one explicit causal rational Weil square.

Under false RH, the same meromorphic test develops the negative hyperbolic
pair contribution described by the Cauchy gate.

## 6. Source-side opportunity

The factor `Psi_a` has only the three double pole scales

\[
 a,2a,4a
\]

and one vanishing moment.  Its physical source is therefore a finite linear
combination of one-sided exponential-polynomial atoms.  This is precisely the
class on which finite Selberg/Jordan deformations and positive Hankel
convolutions are algebraically closed.

The final source theorem may now be sought in the scalar form

```text
construct one positive source-convolved Selberg square for psi_a
with no same-scale remainder.
```

This is strictly narrower than a generic three-port independent-frequency
matrix theorem.

## 7. Boundary

Closed:

```text
exact algebraic factorisation of the residual polynomial;
one scalar causal spectral factor;
three real ports = one complex Hardy port;
finite exponential-polynomial physical source;
exact scalar autocorrelation and carrier Gram;
one-Weil-square normal form of the delayed recurrence.
```

Open:

```text
positive arithmetic/Selberg realization of this one Hardy square;
prime-side recurrence residual sign;
RH.
```
