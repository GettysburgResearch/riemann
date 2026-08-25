# L-103070 — The critical-weighted common half-kernel has a strictly positive Fourier factor

Claim ID: `L-103070`  
Status: **PROVED EXACT KERNEL/SPECTRAL THEOREM**  
Created: 2026-08-26  
Depends on: `L-102701`, `L-103000`  
RH status: **not assumed**

Let `A` be the positive ratio-four half-kernel in

\[
 \Phi_*=2A_-*_M A,
 \qquad A_-=(D-\tfrac12)A,
\]

and put

\[
 L=\log2,
 \qquad a(u)=A(e^u).
\]

By `L-103000`,

\[
 a(u)=
 \begin{cases}
 2(e^{u/2}-1),&0<u<L,\\[1mm]
 2\sqrt2\bigl(1-e^{(u-2L)/2}\bigr),&L<u<2L,\\[1mm]
 0,&\text{otherwise}.
 \end{cases}
\tag{L-103070.1}
\]

Define the critical conjugate

\[
 b(u)=e^{-u/4}a(u).
\tag{L-103070.2}
\]

## 1. Exact weighted reflection symmetry

For `0<u<L`, direct substitution in the second branch of
(L-103070.1) gives

\[
 a(2L-u)=\sqrt2\,e^{-u/2}a(u).
\]

Consequently

\[
\boxed{
 b(2L-u)=b(u).
}
\tag{L-103070.3}
\]

Thus `b(L+v)` is a positive even function of `v`, supported on
`[-L,L]`.

## 2. Exact positive Fourier factor

Use the convention

\[
 \widehat f(t)=\int_{\mathbb R}f(u)e^{-itu}\,du.
\]

The Mellin multiplier of `A` is

\[
 \widehat A(s)
 =
 { (1-2^{-s})(1-\sqrt2\,2^{-s})
  \over s(s-1/2)}.
\]

Since `b(u)=e^{-u/4}a(u)`,

\[
 \widehat b(t)=\widehat A(1/4+it).
\]

Multiplying by the centering phase and simplifying the two numerator factors,

\[
\boxed{
 e^{itL}\widehat A(1/4+it)
 =r_A(t)
 :={2\bigl(\cosh(L/4)-\cos(Lt)\bigr)
    \over t^2+1/16}.
}
\tag{L-103070.4}
\]

For every real `t`,

\[
\boxed{r_A(t)>0.}
\tag{L-103070.5}
\]

Indeed `cosh(L/4)>1>=cos(Lt)`. Therefore

\[
\boxed{
 \widehat b(t)=e^{-itL}r_A(t),
 \qquad r_A(t)\text{ real, even and strictly positive}.
}
\tag{L-103070.6}
\]

The common half-kernel contributes no nontrivial spectral phase after the
critical conjugation.

## 3. Finite-source transform

Let `(c_n)` be any finite complex source and put

\[
 f(u)=\sum_n c_n a(u-\log n),
 \qquad
 g(u)=e^{-u/4}f(u).
\]

Define

\[
 S_c(t)=\sum_n c_n n^{-1/4-it}.
\]

Then (L-103070.6) gives exactly

\[
\boxed{
 \widehat g(t)=e^{-itL}r_A(t)S_c(t).
}
\tag{L-103070.7}
\]

Thus every spectral phase of a physical half-field comes from the literal
arithmetic source polynomial `S_c`; the kernel contributes only the fixed
linear translation phase `e^{-itL}`.

## 4. Scope

Strict positivity of `r_A` is not a positivity theorem for an analytic
self-convolution. The latter contains `S_c(t)^2`, not `|S_c(t)|^2`.
The exact BCI application and the binding phase firewall are
`L-103071` and `R-103010`.
