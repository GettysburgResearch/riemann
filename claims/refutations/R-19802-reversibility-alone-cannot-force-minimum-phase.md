# R-19802 — Reversibility alone cannot force minimum phase

Claim ID: `R-19802`  
Title: Even positive kernels can have the complete reversible Markov structure while retaining explicit off-axis zeros  
Status: `PROVED STRUCTURAL REFUTATION`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Dependencies: elementary Gaussian transforms and detailed balance  
Scope: attempted derivation of the gap-one estimate from `L-19809` alone

## 1. The generic reversible construction

Let `Q` be any nonzero even positive integrable function on `R` with all
bilateral exponential moments. Put

\[
 Z_\omega=\int_{\mathbb R}e^{-\omega y}Q(y)\,dy
 \tag{R-19802.1}
\]

and

\[
 P_\omega(y)=Z_\omega^{-1}e^{-\omega y}Q(y).
 \tag{R-19802.2}
\]

Evenness gives

\[
 P_\omega(-y)=e^{2\omega y}P_\omega(y),
 \tag{R-19802.3}
\]

so convolution by `P_omega` is a reversible self-adjoint Markov contraction on

\[
 L^2(e^{-2\omega x}dx).
 \tag{R-19802.4}
\]

Its Dirichlet form is

\[
\boxed{
 {1\over2}\iint
 |f(y)-f(x)|^2e^{-2\omega x}P_\omega(y-x)\,dx\,dy\ge0.}
 \tag{R-19802.5}
\]

This is exactly the abstract positivity mechanism used in `L-19809`; no special
property of the Riemann kernel has been used.

## 2. An explicit smooth positive counterfamily

Let

\[
 g_\tau(y)={1\over\sqrt{2\pi}\tau}
 e^{-y^2/(2\tau^2)},
 \qquad \tau>0,
 \tag{R-19802.6}
\]

and fix `c>2`. Define

\[
\boxed{
 Q_{c,\tau}(y)
 =g_\tau(y-1)+g_\tau(y+1)+c\,g_\tau(y).}
 \tag{R-19802.7}
\]

This kernel is strictly positive, even, smooth, and has every exponential
moment. Its bilateral Laplace transform is

\[
\boxed{
 F_{c,\tau}(z)
 =e^{\tau^2z^2/2}\bigl(2\cosh z+c\bigr).}
 \tag{R-19802.8}
\]

The Gaussian factor is zero-free. Put

\[
 a=\operatorname{arcosh}(c/2)>0.
 \tag{R-19802.9}
\]

Since

\[
 \cosh(a+i(2k+1)\pi)=-\cosh a=-c/2,
 \]

one has the explicit off-axis zero set

\[
\boxed{
 z=\pm a+i(2k+1)\pi,
 \qquad k\in\mathbb Z.}
 \tag{R-19802.10}
\]

Thus the entire transform of a strictly positive even Gaussian mixture has
zeros with nonzero real part.

## 3. Reversible positivity coexists with a full inner defect

For every real `omega`, the exponentially tilted densities built from
`Q_(c,tau)` satisfy the exact detailed-balance identity and the nonnegative
Dirichlet form (R-19802.5). After unitary symmetrization, the multiplier is the
real Fourier transform

\[
 e^{-\tau^2t^2/2}(2\cos t+c)/Z_\omega.
 \tag{R-19802.11}
\]

Nevertheless the analytic transfer has the off-axis zeros (R-19802.10). On any
vertical line immediately to their left, the outer-normalized Hankel defect is
nonzero and the corresponding Hilbert--Poisson energy has the same positive
bubble described in `L-19810`.

Therefore

\[
\boxed{
 \text{reversibility + Markov contraction + a nonnegative Dirichlet form}
 \not\Longrightarrow
 \text{minimum phase}.}
 \tag{R-19802.12}
\]

The failure persists inside the class of strictly positive, even, real-analytic,
superexponentially regular kernels after replacing the Gaussian by any positive
zero-free smoothing with all moments.

## 4. Consequence for the zeta route

No argument that uses only the abstract features

1. `Q>=0` and even;
2. existence of all exponential moments;
3. detailed balance of every exponential tilt;
4. self-adjoint Markov contractivity;
5. positivity of the associated Dirichlet form

can prove the gap-one estimate for the Riemann kernel. Such an argument would
also apply to (R-19802.7), where the conclusion is false.

A successful proof must exploit additional theta/arithmetic structure. The
exact candidates currently visible are:

- positivity of the original Riemann Weyl kernel in `L-19812`;
- a total-positivity property beyond order two for the Riemann kernel;
- a direct arithmetic contraction for the reflection map in `L-19811`.

## 5. Proof boundary

- The counterexample is explicit and elementary.
- It refutes only a generic deduction from reversibility or Dirichlet positivity;
  it does not refute a theta-specific inequality for the Riemann kernel.
- The Riemann positive density contains substantially more structure than an
  arbitrary even kernel, and that structure is exactly what the remaining proof
  must use.
- No statement about RH is inferred from the counterfamily.