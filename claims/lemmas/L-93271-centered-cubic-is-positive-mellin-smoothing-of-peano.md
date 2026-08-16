# L-93271 - The centered cubic potential is a positive Mellin smoothing of the Peano potential

Claim ID: `L-93271`
Status: **PROPOSED COMPLETE EXACT POSITIVE-TRANSFORM THEOREM - INDEPENDENT REVIEW REQUIRED**
Created: 2026-08-16
Depends on: `L-93263` at PR #531 and `L-93270`
Scope: exact kernel dictionary; no transfer of a prime estimate is assumed

## 1. Mellin convolution

For compact functions on `(0,1]`, write

\[
(f*_Mg)(x)
=\int_x^1 f(x/u)g(u)\,\frac{du}{u}.
\tag{L-93271.1}
\]

Then

\[
\widehat{f*_Mg}(s)=\widehat f(s)\widehat g(s).
\tag{L-93271.2}
\]

Let

\[
\Phi_P(x)=x(1-x)^2\mathbf1_{[0,1]}(x)
\tag{L-93271.3}
\]

and define the positive smoothing kernel

\[
\boxed{g(x)=\frac1{24}+\frac{x^4}{8}\ge0.}
\tag{L-93271.4}
\]

Its Mellin transform is

\[
\widehat g(s)
=\frac1{24s}+\frac1{8(s+4)}
=\frac{s+1}{6s(s+4)}.
\tag{L-93271.5}
\]

Since

\[
\widehat\Phi_P(s)=\frac2{(s+1)(s+2)(s+3)},
\tag{L-93271.6}
\]

we obtain

\[
\widehat\Phi_P(s)\widehat g(s)
=\frac1{3s(s+2)(s+3)(s+4)}.
\tag{L-93271.7}
\]

## 2. The unfiltered cubic potential

Put

\[
H(x)=\frac{(1-x)^3(3x+1)}{72}\mathbf1_{[0,1]}(x).
\tag{L-93271.8}
\]

Direct integration gives

\[
\widehat H(s)=\frac1{3s(s+2)(s+3)(s+4)}.
\tag{L-93271.9}
\]

Therefore

\[
\boxed{H=\Phi_P*_Mg.}
\tag{L-93271.10}
\]

This is an equality of compact kernels, not only of formal series. Both factors on the right are nonnegative.

## 3. Recovering the centered cubic potential

The positive potential in `L-93263` is exactly

\[
\boxed{\Phi_C(x)=H(x)-H(4x).}
\tag{L-93271.11}
\]

For `0<=x<=1/4`,

\[
\Phi_C(x)
=\frac{x^2(85x^2-56x+10)}8,
\tag{L-93271.12}
\]

while for `1/4<=x<=1`,

\[
\Phi_C(x)
=\frac{(1-x)^3(3x+1)}{72}.
\tag{L-93271.13}
\]

Thus the centered-cubic route is the scale-four innovation of a positive Mellin smoothing of the canonical Peano route:

\[
\boxed{
\Phi_C=(I-T)(\Phi_P*_Mg).
}
\tag{L-93271.14}
\]

At the curvature level, the sign-changing cubic kernel is not arbitrary. It is the logarithmic second derivative of this positive smoothed scale innovation.

## 4. What transfers and what does not

The identity transfers:

1. compact support;
2. exact Mellin zero locations;
3. positive source realization before the final scale difference;
4. polynomial conditioning between the Peano and cubic transforms.

It does not transfer a pointwise sign of curvature. `R-93270` gives an exact positive-source countermodel to that invalid inference.

## 5. Boundary

The centered cubic and Peano routes are now one positive-transform family. A proof may choose whichever kernel has the more tractable arithmetic producer. No RH-strength prime estimate is imported by this dictionary.
