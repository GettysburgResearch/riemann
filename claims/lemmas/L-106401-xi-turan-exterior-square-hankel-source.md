# L-106401 — The actual Xi Turán numerator is an exterior-square Hankel source

Claim ID: `L-106401`  
Status: **PROVED UNCONDITIONALLY FROM THE POSITIVE XI FOURIER KERNEL**  
Created: 2026-08-24  
Depends on: the classical positive even Fourier representation of Xi  
RH status: **not assumed**

Use the Fourier convention

\[
\Xi(t)=\int_{\mathbb R}\Phi(u)e^{itu}\,du,
\qquad
\widehat f(\xi)=\frac1{2\pi}\int_{\mathbb R}f(t)e^{-it\xi}\,dt,
\]

so that \(\widehat\Xi=\Phi\).  The classical Xi kernel satisfies

\[
\Phi(u)=\Phi(-u)\ge0
\]

and has moments of every order.

Define the Laguerre--Turán function

\[
\mathcal L_\Xi(t)=\Xi'(t)^2-\Xi(t)\Xi''(t).
\]

## 1. Exact exterior-square density

Product convolution and symmetrization under \(u\leftrightarrow\xi-u\) give

\[
\boxed{
\widehat{\mathcal L_\Xi}(\xi)
 =\frac12\int_{\mathbb R}
   (2u-\xi)^2\Phi(u)\Phi(\xi-u)\,du
 =:\Lambda_\Xi(\xi)\ge0.
}
\tag{L-106401.1}
\]

Thus the complete actual-Xi Laguerre determinant has a nonnegative Fourier
density.  This is a literal exterior-square identity: the factor
\((2u-\xi)^2\) is the squared frequency separation of the two Xi source
particles.

Because \(\Phi\) is even, \(\Lambda_\Xi\) is even.  It is rapidly decreasing and
nonnegative.

## 2. Endpoint Turán numerator

Differentiation gives

\[
\frac d{dt}\bigl(\Xi'^2-\Xi\Xi''\bigr)
 =\Xi'\Xi''-\Xi\Xi'''.
\]

Therefore the endpoint numerator from `L-106400` is

\[
\boxed{
\mathcal T_\Xi(t)
 :=\Xi(t)\Xi'''(t)-\Xi'(t)\Xi''(t)
 =-\mathcal L_\Xi'(t),
}
\tag{L-106401.2}
\]

and

\[
\boxed{
\widehat{\mathcal T_\Xi}(\xi)
 =-i\xi\Lambda_\Xi(\xi).
}
\tag{L-106401.3}
\]

No frozen Euler product, mollifier, or hypothetical zero enters this identity.

## 3. Negative Hardy compression

Identify the Hardy space of the upper half-plane with \(L^2(0,\infty)\) by
Fourier transform.  For \(h\in L^2(0,\infty)\) and \(x>0\), the negative
frequency of \(\mathcal T_\Xi h\) at \(-x\) is

\[
\widehat{\mathcal T_\Xi h}(-x)
 =i\int_0^\infty
   (x+s)\Lambda_\Xi(x+s)h(s)\,ds.
\]

Hence the Hankel operator \(H_{\mathcal T_\Xi}=P_-M_{\mathcal T_\Xi}|_{H^2}\)
is unitarily equivalent, up to the harmless phase \(i\), to

\[
\boxed{
(\mathcal H_\Xi h)(x)
 =\int_0^\infty
   (x+s)\Lambda_\Xi(x+s)h(s)\,ds.
}
\tag{L-106401.4}
\]

Its integral kernel is real, symmetric and pointwise nonnegative.  The theorem
does not assert that pointwise kernel positivity alone makes the operator
positive semidefinite; the conclusion-facing Gram is instead
\(\mathcal H_\Xi^*\mathcal H_\Xi\succeq0\).

For any finite analytic frame \((g_j)\), with positive-frequency transforms
\(h_j\), the matrix \(Q\) of `L-106400` is exactly

\[
\boxed{
Q_{ij}=\langle\mathcal H_\Xi h_i,\mathcal H_\Xi h_j\rangle.
}
\tag{L-106401.5}
\]

Thus the numerator side of the two-rung Xi descent is already an explicit
actual-Xi positive Gram.  The remaining difficulty is normalization by the
endpoint denominator frame and cofinal frame coverage, not identification or
sign of the numerator source.

## 4. Scope

Equations (L-106401.1)--(L-106401.5) are unconditional.  They do not bound
\(\operatorname{tr}(G^{-1}Q)\), control zeros of the endpoint companions, or
prove any new critical-line percentage by themselves.
