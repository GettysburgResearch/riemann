# L-102891 — Every strict positive completion is unconditionally eventually positive

Claim ID: `L-102891`  
Status: **PROVED UNCONDITIONAL SELBERG–DELANGE ASYMPTOTIC**  
Created: 2026-08-24  
Depends on: corrected `L-102866`; the labelled duplicate-67 source convention  
RH status: **not assumed**

Let \(\mathcal P^\#\) consist of all ordinary prime labels together with one
additional label whose physical prime is \(67\).  For a fixed parameter

\[
0<c<1
\]

define the partially completed Euler source \(\gamma_c\) by

\[
\boxed{
B_c(z):=
\sum_{n\ge1}\frac{\gamma_c(n)}{n^z}
=
\prod_{\ell\in\mathcal P^\#}
(1-p_\ell^{-z})(1+c\,p_\ell^{-z}).
}
\tag{L-102891.1}
\]

Thus \(c=0\) is the native source and \(c=1\) is the squared completion; the
present theorem concerns only strict interior parameters.

Let \(R_L\) be the fixed carrier-centered outer/Lorentz kernel of
`L-102866`, supported on \([1,8]\), and put

\[
H_c(X)=
\sum_{n\ge1}\frac{\gamma_c(n)}{\sqrt n}
R_L(X/n).
\tag{L-102891.2}
\]

The sum is finite at every \(X\).

## 1. Exact singular factorization

Write

\[
f_c(x)=(1-x)(1+cx).
\]

Separating the ordinary prime product from the extra labelled \(67\) gives

\[
\boxed{
B_c(z)=\zeta(z)^{c-1}G_c(z),
}
\tag{L-102891.3}
\]

where

\[
\boxed{
G_c(z)
=
f_c(67^{-z})
\prod_p(1-p^{-z})^c(1+c\,p^{-z}).
}
\tag{L-102891.4}
\]

The logarithm of one ordinary local factor is

\[
c\log(1-x)+\log(1+cx)
=-\frac{c+c^2}{2}x^2+O_c(x^3).
\]

Hence the product in (L-102891.4) converges locally uniformly and is nonzero
for \(\Re z>1/2\).  In particular,

\[
\boxed{
G_c(1)
=
(1-67^{-1})(1+c/67)
\prod_p(1-p^{-1})^c(1+c/p)>0.
}
\tag{L-102891.5}
\]

## 2. Critical Mellin value of the outer kernel

Direct integration of the corrected piecewise formula in `L-102866` gives

\[
\boxed{
\widehat R_L(1/2)
:=
\int_1^8R_L(y)y^{-3/2}\,dy
=
(8\sqrt2-12)\log2
=-4(\sqrt2-1)^2\log2<0.
}
\tag{L-102891.6}

This is distinct from the nonzero square-lattice moment
\(\widehat R_L(0)=8(1-\sqrt2)(\log2)^2\).

## 3. Kernelized Selberg–Delange formula

The standard Selberg–Delange/Hankel-contour expansion, applied to

\[
B_c(z)=\zeta(z)^\alpha G_c(z),
\qquad \alpha=c-1\in(-1,0),
\]

and to the fixed compact piecewise-\(C^1\) kernel \(R_L\), gives

\[
\boxed{
H_c(X)
=
\frac{\widehat R_L(1/2)G_c(1)}{\Gamma(c-1)}
X^{1/2}(\log X)^{c-2}
\left(1+O_c\!\left(\frac1{\log X}\right)\right).
}
\tag{L-102891.7}
\]

For completeness, the contour proof is the usual one: write the Mellin
integral for (L-102891.2), move it to a Hankel contour about
\(s=1/2\), use

\[
B_c(s+1/2)
=G_c(1)(s-1/2)^{1-c}
\bigl(1+O_c(s-1/2)\bigr),
\]

replace \(\widehat R_L(s)\) by \(\widehat R_L(1/2)\), and apply

\[
\frac1{2\pi i}
\int_{\mathcal H}e^w w^{1-c}\,dw
=\frac1{\Gamma(c-1)}.
\]

The error is uniform when \(c\) ranges over a compact subinterval of
\((0,1)\).

Since

\[
\Gamma(c-1)<0
\qquad(0<c<1),
\]

both the numerator and denominator in the leading constant are negative.
Therefore

\[
\boxed{
H_c(X)>0
\quad\text{for every sufficiently large }X,
}
\tag{L-102891.8}
\]

for every fixed strict completion parameter \(c\in(0,1)\).

## 4. Arithmetic midpoint

At \(c=1/2\),

\[
H_{1/2}(X)
\sim
\boxed{
\frac{2(3-2\sqrt2)\log2}{\sqrt\pi}
G_{1/2}(1)
\frac{\sqrt X}{(\log X)^{3/2}}
}>0.
\tag{L-102891.9}
\]

The positivity is unconditional and does not use RH, a zero-free strip beyond
the classical neighborhood of \(1\), or a finite scan.

## Endpoint firewall

The asymptotic is not uniform at \(c=0\) or \(c=1\).  At \(c=0\),
\(1/\Gamma(-1)=0\): the real branch term disappears and the native
reciprocal-zeta source becomes conclusion-bearing.  This sharp endpoint
transition is analyzed in `R-102870` and `T-102900`.
