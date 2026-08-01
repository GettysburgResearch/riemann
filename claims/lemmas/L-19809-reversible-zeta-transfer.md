# L-19809 — Reversible completed-zeta transfer

Claim ID: `L-19809`  
Title: The completed-zeta exponential family is reversible, and its self-adjoint dilation has the critical Xi function as exact spectral multiplier  
Status: `PROPOSED — COMPLETE PROOF FROM THE POSITIVE COMPLETED-ZETA DENSITY`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Dependencies: Nakamura's completed-zeta probability density; Fourier/Mellin inversion; detailed balance  
Scope: genuinely self-adjoint starting point for the final strip-sensitive obstruction

## 1. One even positive base density

Use the normalization

\[
\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Put

\[
f(x)=2\pi(2\pi x^4-3x^2)e^{-\pi x^2},\qquad x\ge1,
\]

and define

\[
\boxed{
Q(y)=2e^{|y|/2}\sum_{n\ge1}f(ne^{|y|}),\qquad y\in\mathbb R.}
\tag{L-19809.1}
\]

Every summand is positive. The Gaussian factor gives double-exponential decay,
so all bilateral exponential moments exist. Nakamura's integral representation
is exactly

\[
\boxed{
\xi\!\left(\frac12+z\right)
=\int_{\mathbb R}e^{-zy}Q(y)\,dy,
\qquad z\in\mathbb C.}
\tag{L-19809.2}
\]

In particular,

\[
\Xi(t):=\xi\!\left(\frac12-it\right)
=\int_{\mathbb R}e^{ity}Q(y)\,dy.
\tag{L-19809.3}
\]

Thus the critical Xi function is the Fourier transform of one explicit even
positive density.

## 2. Exponential tilts and exact detailed balance

For `0<omega<1/2`, set

\[
Z_\omega=\xi\!\left(\frac12+\omega\right)
\]

and

\[
\boxed{
P_\omega(y)=Z_\omega^{-1}e^{-\omega y}Q(y).}
\tag{L-19809.4}
\]

Then `P_omega` is a probability density and

\[
\widehat P_\omega(t)
=\frac{\xi(1/2+\omega-it)}{\xi(1/2+\omega)}.
\tag{L-19809.5}
\]

Evenness of `Q`, together with `Z_omega=Z_{-omega}`, gives the exact local
detailed-balance law

\[
\boxed{
P_\omega(-y)=e^{2\omega y}P_\omega(y).}
\tag{L-19809.6}
\]

No zero-location hypothesis enters this identity.

## 3. A reversible Markov convolution

Define

\[
(K_\omega f)(x)=\int_{\mathbb R}P_\omega(u)f(x+u)\,du
\tag{L-19809.7}
\]

and let

\[
dm_\omega(x)=e^{-2\omega x}\,dx.
\tag{L-19809.8}
\]

Equation (L-19809.6) is precisely

\[
e^{-2\omega x}P_\omega(y-x)
=e^{-2\omega y}P_\omega(x-y).
\tag{L-19809.9}
\]

Hence `K_omega` is self-adjoint on `L^2(m_omega)`. The measure is invariant,
because

\[
\int e^{-2\omega x}P_\omega(y-x)\,dx
=e^{-2\omega y}\int e^{2\omega u}P_\omega(u)\,du
=e^{-2\omega y},
\]

where the last exponential moment is `Z_{-omega}/Z_omega=1`. Jensen's
inequality therefore makes `K_omega` a self-adjoint Markov contraction.

Its Dirichlet form is the explicit nonnegative quadratic form

\[
\boxed{
\begin{aligned}
\langle f,(I-K_\omega)f\rangle_{m_\omega}
={1\over2}\iint_{\mathbb R^2}
&|f(y)-f(x)|^2\\
&\times e^{-2\omega x}P_\omega(y-x)\,dx\,dy
\ge0.
\end{aligned}}
\tag{L-19809.10}
\]

## 4. Unitary symmetrization

The map

\[
(U_\omega f)(x)=e^{-\omega x}f(x)
\tag{L-19809.11}
\]

is unitary from `L^2(m_omega)` to ordinary `L^2(dx)`. Direct substitution gives

\[
\boxed{
U_\omega K_\omega U_\omega^{-1}
={1\over Z_\omega}C_Q,}
\tag{L-19809.12}
\]

where `C_Q` is convolution by the same even kernel `Q`, independent of
`omega`. Its Fourier multiplier is therefore

\[
\boxed{
{\Xi(t)\over Z_\omega}.}
\tag{L-19809.13}
\]

Consequently

\[
\boxed{
{1\over2\pi}\int_{\mathbb R}
\left(1-{\Xi(t)\over Z_\omega}\right)
|\widehat g(t)|^2\,dt\ge0
\qquad(g\in L^2).}
\tag{L-19809.14}
\]

This is an unconditional self-adjoint realization of the critical Xi function:
`Xi(t)` is the exact spectral multiplier of a reversible Markov transfer, not an
approximate eigenvalue or determinant.

## 5. Exact boundary of the mechanism

The self-adjoint operator sees the real boundary values `Xi(t)`. A hypothetical
off-line zero is a zero of the analytic continuation of this multiplier, not a
nonreal spectral value of `C_Q`. Thus self-adjointness of (L-19809.12) alone
does not prove RH.

The unresolved information is exactly the minimum-phase/inner factor of the
analytic transfer. The reversible operator fixes its boundary amplitude and
autocorrelation. `T-19805` isolates the remaining all-pass factor and shows that
its defect is an orthogonal projection: one off-line zero cannot be made
arbitrarily small after outer normalization.

## 6. Proof boundary

- The base density, exponential family, detailed balance, and unitary dilation
  are exact.
- The construction is unconditional and contains no verified-zero input.
- It supplies a genuine self-adjoint mechanism, but a self-adjoint convolution
  multiplier does not constrain every zero of its analytic continuation.
- The smallest remaining object is the minimum-phase/inner defect of the same
  transfer, treated in `T-19805`.