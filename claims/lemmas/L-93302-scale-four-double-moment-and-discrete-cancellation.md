# L-93302 — The scale-four cubic wavelet has two Mellin moments and an exact discrete cancellation law

Claim ID: `L-93302`  
Status: **UNCONDITIONAL EXACT STRUCTURAL THEOREM**  
Created: 2026-08-16  
Depends on: `L-93301`  
RH status: **unproved**

## 1. Mellin transform

For

\[
 F(x)=K(x)-4K(4x)\mathbf1_{x\le1/4},
\]

a change of variables gives

\[
 \boxed{
 \widehat F(s)
 :=\int_0^1F(x)x^{s-1}\,dx
 =(1-4^{1-s})
 \frac{s-1}{3(s+1)(s+2)(s+3)}.
 }
 \tag{L-93302.1}
\]

The factor \(1-4^{1-s}\) and the cubic factor \(s-1\) give a double zero at
\(s=1\).  Hence

\[
 \boxed{
 \int_0^1F(x)\,dx=0,
 \qquad
 \int_0^1F(x)\log x\,dx=0.
 }
 \tag{L-93302.2}
\]

The first nonzero logarithmic moment is

\[
 \boxed{
 \int_0^1F(x)(\log x)^2\,dx
 =\widehat F''(1)
 =\frac{\log4}{36}>0.
 }
 \tag{L-93302.3}
\]

Thus \(F\) is a genuine two-moment multiplicative wavelet, not merely a
mean-zero cutoff.

## 2. Exact integer-grid cancellation

For an integer \(M\ge1\), put

\[
 \mathcal G(M)=\sum_{n=1}^{M}F(n/M).
\]

Write \(M=4h+r\), \(0\le r<4\).  Direct Faulhaber summation of the two cubic
pieces gives

\[
 \boxed{
 \mathcal G(4h)=0,
 }
 \tag{L-93302.4}
\]

\[
 \boxed{
 \mathcal G(4h+1)
 =-\frac{8h(h+1)}{(4h+1)^3},
 }
 \tag{L-93302.5}
\]

\[
 \boxed{
 \mathcal G(4h+2)
 =-\frac{4h(h+1)}{3(2h+1)^3},
 }
 \tag{L-93302.6}
\]

and

\[
 \boxed{
 \mathcal G(4h+3)
 =-\frac{8h(h+1)}{(4h+3)^3}.
 }
 \tag{L-93302.7}
\]

In particular,

\[
 |\mathcal G(M)|\ll M^{-1}.
 \tag{L-93302.8}
\]

The exact zero on every grid divisible by four is a finite arithmetic shadow
of the scale-four construction.

## 3. Real-mesh quadrature

The function \(F\) is continuous on \([0,1]\), vanishes at both endpoints,
and has piecewise \(C^2\) derivative of bounded variation.  Composite
Euler--Maclaurin, with the one derivative jump at \(1/4\) retained, gives for
every real \(y\ge2\)

\[
 \boxed{
 \sum_{n\le y}F(n/y)=O(y^{-1}).
 }
 \tag{L-93302.9}
\]

For \(F(x)\log x\), split off the first mesh interval and apply the same
argument on \([1/y,1]\).  Since (L-93302.2) kills the integral and both endpoint
values vanish,

\[
 \boxed{
 \sum_{n\le y}\log(n/y)F(n/y)
 =O\!\left(\frac{\log(2y)}y\right).
 }
 \tag{L-93302.10}
\]

Consequently,

\[
 \boxed{
 \sum_{n\le y}\log n\,F(n/y)
 =O\!\left(\frac{\log(2y)}y\right).
 }
 \tag{L-93302.11}
\]

All constants are absolute and depend only on the displayed piecewise cubic.

## 4. Additive Fourier dispersion

Extend \(F\) periodically from \([0,1]\).  Since \(F(0)=F(1)=0\) and its
periodic derivative has bounded variation, its Fourier coefficients satisfy

\[
 \widehat F_{\mathbb T}(0)=0,
 \qquad
 |\widehat F_{\mathbb T}(h)|\ll(1+|h|)^{-2}.
 \tag{L-93302.12}
\]

The Fourier series is absolutely convergent at every mesh point.  Therefore,
for every finite coefficient sequence \(a_n\),

\[
 \boxed{
 \sum_{n\le N}a_nF(n/N)
 =
 \sum_{h\ne0}\widehat F_{\mathbb T}(h)
 \sum_{n\le N}a_ne(hn/N).
 }
 \tag{L-93302.13}
\]

This is the exact additive-dispersion coordinate requested by the Q4
major-arc programme.  The zero additive frequency is absent identically.

If

\[
 \Phi(\xi)=\int_0^1K(x)e^{-2\pi i\xi x}\,dx,
\]

then the scale-four relation is

\[
 \boxed{
 \widehat F_{\mathbb T}(h)
 =\Phi(h)-\Phi(h/4).
 }
 \tag{L-93302.14}
\]

## 5. What the two moments do and do not prove

The two moments eliminate the continuous main density and its first
logarithmic perturbation.  The exact grid formulas make the same cancellation
visible before any prime input.

They do not control

\[
 \int F(t/N)\,d[\vartheta(t)-t].
\]

That term contains the complete open-strip zero information by `L-93300`.
Any use of (L-93302.2) as though it were a prime-distribution estimate violates
`R-93300`.

## 6. Boundary

```text
Mellin transform                                 exact
two vanishing Mellin moments                     exact
first nonzero log moment                         exact
integer-grid residue-class formulas              exact
real-mesh quadrature                             unconditional
additive Fourier expansion                       exact
prime discrepancy cancellation                   open / RH-bearing
Riemann Hypothesis                               unproved
```
