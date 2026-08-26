# L-102737 — The centered Lorentz kernel has one exact prime carrier

Claim ID: `L-102737`  
Status: **PROVED EXACT MELLIN MOMENT AND SOURCE QUOTIENT**  
Created: 2026-08-23  
Depends on: `L-102728`; `L-102732`; PR #694 prime-carrier asymptotics  
RH status: **not assumed**

Let

\[
 R_w(y)=JP_2|S_-(y)+w|^2-cy\mathbf1_{y\ge1},
 \qquad c=2(2-\sqrt2),
\]

be the exact compact centered ray of `L-102732`.

For real `w`, its half-order Mellin moment is affine:

\[
 \widehat R_w(1/2)=M_0+2\kappa_0 w,
 \tag{L-102737.1}
\]

where

\[
 \boxed{
 \kappa_0
 =8\log2(1-2^{-1/2})^2
 =4\log2(3-2\sqrt2)>0.
 }
 \tag{L-102737.2}
\]

Indeed the filtered multiplier has one zero at `s=1/2`; it cancels the
square-root pole of the shifted quadratic and leaves exactly the coefficient
in (L-102737.1).  The affine `cy` subtraction changes only the `s=1` mode.

## Lorentz barycentric moment

The centered Lorentz kernel is

\[
 R_L
 =\frac{17}{2}R_{-1/2}
  +\frac{15}{2}R_{1/2}
  -16R_0.
\]

Its constant moment cancels because the coefficients sum to zero.  Their first
moment is

\[
 \frac{17}{2}\left(-\frac12\right)
 +\frac{15}{2}\left(\frac12\right)
 =-\frac12.
\]

Therefore

\[
 \boxed{
 \widehat R_L(1/2)=-\kappa_0.
 }
 \tag{L-102737.3}
\]

## Exact singleton-prime packet

For the ordinary Möbius source, the literal singleton-prime contribution is

\[
 \boxed{
 \mathcal P_L(X)
 =-
 \sum_p\frac1{\sqrt p}R_L(X/p).
 }
 \tag{L-102737.4}
\]

The quantitative prime number theorem and (L-102737.3) give

\[
 \boxed{
 \mathcal P_L(X)
 =
 +\kappa_0\frac{\sqrt X}{\log X}
 +O\left(\frac{\sqrt X}{\log^2X}\right).
 }
 \tag{L-102737.5}
\]

Thus any absolute value, square or radial cost applied to an unquotiented
regional Lorentz packet is power-sized.

## Source-exact quotient

For any exact source partition

\[
 \mathcal L=\mathcal L_{\rm left}+\mathcal L_{\rm right},
\]

define

\[
 \widetilde{\mathcal L}_{\rm left}
 =\mathcal L_{\rm left}-\mathcal P_L,
\]

\[
 \widetilde{\mathcal L}_{\rm right}
 =\mathcal L_{\rm right}+\mathcal P_L.
\]

Then

\[
 \boxed{
 \mathcal L
 =
 \widetilde{\mathcal L}_{\rm left}
 +
 \widetilde{\mathcal L}_{\rm right}
 }
 \tag{L-102737.6}
\]

coefficient-exactly.  The prime carrier is moved once and recombined before
any nonlinear estimate.

Consequently `OERSC102770` is to be read on the **prime-carrier-quotiented**
one-octave packets.  This quotient is mandatory and does not change the fixed
Mellin detector.