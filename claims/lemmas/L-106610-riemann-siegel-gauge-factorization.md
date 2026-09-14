# L-106610 — Exact Riemann–Siegel gauge factorization of every Xi derivative companion

Claim ID: `L-106610`  
Status: **PROVED EXACT ON EVERY SUFFICIENTLY HIGH REGULAR WINDOW**  
Created: 2026-08-26  
Depends on: the standard Hardy \(Z\)-factorization and Stirling's formula  
RH status: **not assumed**

## 1. The analytic Hardy gauge

Put

\[
s=\frac12+it
\]

and choose the standard analytic continuation of the Riemann–Siegel phase

\[
\vartheta(t)
=
\frac{1}{2i}
\left[
\log\Gamma\!\left(\frac14+\frac{it}{2}\right)
-
\log\Gamma\!\left(\frac14-\frac{it}{2}\right)
\right]
-\frac t2\log\pi
\]

on a simply connected neighbourhood of a sufficiently high regular dyadic
window. On the real axis,

\[
Z(t)=e^{i\vartheta(t)}\zeta\!\left(\frac12+it\right)
\]

is real. Write

\[
\Xi(t)=A(t)Z(t)
      =A(t)e^{i\vartheta(t)}h(t),
\qquad
h(t)=\zeta\!\left(\frac12+it\right),
\]

where

\[
A(t)
=
\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)e^{-i\vartheta(t)}
\]

is real and nonzero on the real high window. Define

\[
q=\frac{A'}{A},
\qquad
\omega=\vartheta',
\qquad
D=\frac d{dt},
\qquad
\mathscr L=D+q+i\omega .
\]

Then, for every integer \(k\ge0\),

\[
\boxed{
\Xi^{(k)}(t)
=
A(t)e^{i\vartheta(t)}H_k(t),
\qquad
H_k=\mathscr L^k h .
}
\tag{L-106610.1}
\]

This follows by induction from

\[
D(Ae^{i\vartheta}g)
=
Ae^{i\vartheta}(D+q+i\omega)g.
\]

## 2. A canonical positive analytic scale

Stirling's formula gives, uniformly on every fixed-width high strip,

\[
\omega(t)
=
\frac12\log\frac{t}{2\pi}
+O(t^{-2}),
\]

\[
q(t)
=
-\frac{\pi}{4}
+\frac{7}{4t}
+O(t^{-2}).
\]

Consequently \(\omega\) has no zero near a sufficiently high dyadic window,
and

\[
\boxed{
a_{\rm RS}(t)=\frac1{\omega(t)}
=
\frac{2}{\log(t/2\pi)}
+O\!\left(\frac{1}{t^2\log^2t}\right)
}
\tag{L-106610.2}
\]

is holomorphic nearby, real and strictly positive on the real interval, and
tends uniformly to zero. It is therefore an admissible scale in
`L-106600--L-106603`.

## 3. Exact carrier-cancelled packets

For every \(k\ge0\), define

\[
\boxed{
C_k
=
\frac{i}{\omega}(D+q)H_k,
\qquad
R_k=2H_k-C_k .
}
\tag{L-106610.3}
\]

Because

\[
\mathscr L=(D+q)+i\omega,
\]

one has the exact identities

\[
\boxed{
\Xi^{(k)}
+i a_{\rm RS}\Xi^{(k+1)}
=
Ae^{i\vartheta}C_k,
}
\tag{L-106610.4}
\]

\[
\boxed{
\Xi^{(k)}
-i a_{\rm RS}\Xi^{(k+1)}
=
Ae^{i\vartheta}R_k.
}
\tag{L-106610.5}
\]

Thus the large common gamma/Riemann–Siegel carrier is removed before any norm,
phase, or zero-count estimate. No asymptotic replacement is made in
(L-106610.4)--(L-106610.5).

At the base endpoint,

\[
\boxed{
C_0
=
-\frac1{\omega}
\left(
\zeta'(s)-iq\,\zeta(s)
\right),
}
\tag{L-106610.6}
\]

where \(\zeta'\) denotes the complex derivative. Hence one endpoint companion
is exactly the classical Levinson combination \(\zeta'-iq\zeta\), with an
explicit archimedean coefficient.

## 4. Scope

The theorem is an exact gauge conversion. It does not estimate the zeros,
inner phase measure, or Hankel charge of the resulting arithmetic packets.
It proves that the adaptive scale is explicit and that the remaining
microscopic problem can be stated entirely in finite combinations of zeta
derivatives rather than in opaque Xi companion factors.
