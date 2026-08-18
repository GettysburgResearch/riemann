# L-95501 — The Q4 annular kernel has no counterexample-strip zero and its ratio completion is positive spectral mass

Claim ID: `L-95501`  
Status: **PROPOSED COMPLETE EXACT KERNEL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: PR #580 `L-95400/L-95402`  
Scope: exact finite-band/Mellin geometry; no Möbius estimate

## 1. Exact Mellin factors

Retain

\[
\widehat J_0(z)
=q(z)\mathcal A_2(t)\widehat W(z),
\qquad
 t=2^{-z-1/2},
\]

where

\[
q(z)=\prod_{k=1}^{3}(1-2^{-z-k}),
\]

\[
\mathcal A_2(t)=(1+t)(1-4t^2)^2,
\]

and

\[
\widehat W(z)
=(1-4^{1-z})\frac{z-1}{3(z+1)(z+2)(z+3)}.
\tag{L-95501.1}
\]

## 2. Zero-free counterexample strip

Suppose

\[
0<\Re z<\frac12.
\]

Then:

- a zero of `q` has real part `-1`, `-2`, or `-3`;
- `1+t=0` requires \(|t|=1\), hence \(\Re z=-1/2\);
- `1-4t^2=0` requires \(|t|=1/2\), hence \(\Re z=1/2\);
- `1-4^{1-z}=0` requires \(\Re z=1\);
- `z-1=0` requires \(z=1\).

The denominator in (L-95501.1) is also nonzero. Therefore

\[
\boxed{
\widehat J_0(z)\ne0
\qquad(0<\Re z<\tfrac12).
}
\tag{L-95501.2}
\]

At a hypothetical zeta zero \(\rho\) with \(1/2<\Re\rho<1\), the relevant
point is

\[
z_\rho=\rho-\frac12,
\]

which lies exactly in this strip.

## 3. Pole order cannot cancel

Put

\[
M_o(s)=\frac1{(1-2^{-s})\zeta(s)}.
\]

The exact one-variable Mellin transform of the annular packet is

\[
\mathfrak F(z)
=
-\widehat J_0(z)M_o'(z+\tfrac12)
+(\log2)\widehat J_1(z)M_o(z+\tfrac12).
\tag{L-95501.3}
\]

If \(\rho\) is a zeta zero of multiplicity \(m\), then `M_o'` has a pole of
order \(m+1\), while the `J1` term has pole order at most \(m\). By
(L-95501.2), the leading pole has nonzero coefficient. Hence

\[
\boxed{
\mathfrak F(z)
\text{ has a pole of order }m+1
\text{ at }z=\rho-\tfrac12.
}
\tag{L-95501.4}
\]

The ten-band Q4 kernel creates no spectral cancellation of an off-line zero.

## 4. Exact nonzero low-frequency mass

At `z=0`, exact substitution gives

\[
\boxed{
\widehat J_0(0)
=\frac7{128}\left(1+\frac1{\sqrt2}\right)>0.
}
\tag{L-95501.5}
\]

Thus the logarithmic channel has nonzero Mellin mass at frequency zero.

## 5. Positive multiplicative autocorrelation

For \(L=\log X\), extend by zero and put

\[
\gamma_L(u)
=
(L-u)J_0(e^{-u})+(\log2)J_1(e^{-u}),
\qquad 0\le u\le10\log2.
\]

Define the ratio autocorrelation

\[
R_L(v)=\int_{\mathbb R}\gamma_L(u)\gamma_L(u+v)\,du.
\tag{L-95501.6}
\]

Its Fourier transform is exactly

\[
\boxed{
\widehat R_L(t)=|\widehat\gamma_L(t)|^2\ge0.
}
\tag{L-95501.7}
\]

For all sufficiently large `X`, (L-95501.5) makes
\(\widehat\gamma_L(0)\ne0\). Hence the exact finite-band ratio completion has
strict positive spectral mass near zero. A positive-kernel completion
reinforces the resonant reciprocal-zeta square; it does not provide an
oscillatory cancellation mechanism.

## 6. Boundary

```text
J0 zero-free in 0<Re z<1/2              EXACT
higher-order pole survives J1 channel    EXACT
nonzero zero-frequency Mellin mass        EXACT
multiplicative autocorrelation PSD        EXACT
kernel-generated SACF cancellation        ABSENT
arithmetic Möbius cancellation            OPEN / RH-BEARING
```
