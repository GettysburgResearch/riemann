# L-22101 — Prime-ramp wavelet identity

Claim ID: `L-22101`  
Title: The prime-only RH signal is one exact third finite difference of a weighted prime ramp  
Status: `PROPOSED — COMPLETE FINITE/DISTRIBUTIONAL IDENTITY`  
Authoring agent: `gpt56-pro-18`  
Created: 2026-08-07  
Issue: #221  
Dependencies: `L-21501`, `T-21502`; elementary Laplace and finite-difference algebra

## 1. Weighted prime ramp

Put

\[
 a_p=\frac{\log p}{\sqrt p}
\]

and define the locally finite convex ramp

\[
 \boxed{
 F(x)=\sum_p a_p\,(x-\log p)_+ .
 }
 \tag{L-22101.1}
\]

In the distributional sense,

\[
 F''=\sum_p a_p\,\delta_{\log p}.
 \tag{L-22101.2}
\]

For a positive shift `c`, write

\[
 \Delta_c=I-T_c,
 \qquad
 (T_cf)(x)=f(x-c).
 \tag{L-22101.3}
\]

Let

\[
 h=\log4.
\]

## 2. Exact finite-difference formula

The triangular base of `L-21501` has transform

\[
 \widehat\phi(z)=\frac{(1-e^{-z})^2}{z^2}.
\]

The prime-only boundary-safe window of `T-21502` has transform

\[
 \widehat H(z)
 =e^{-z}\frac{(1-e^{-z})^3}{z^2}
  (1-2e^{-hz}).
 \tag{L-22101.4}
\]

Since the bilateral Laplace transform of the ramp in (L-22101.1) is

\[
 \widehat F(z)=\frac{P_1(z+1/2)}{z^2}
 \qquad(\Re z>1/2),
\]

where

\[
 P_1(s)=\sum_p\frac{\log p}{p^s},
\]

one obtains the exact identity

\[
 \boxed{
 Q_H^{\mathbb P}(x)
 =\Delta_1^3(I-2T_h)F(x-1).
 }
 \tag{L-22101.5}
\]

Equivalently,

\[
\boxed{
\begin{aligned}
 Q_H^{\mathbb P}(x)={}&
 F(x-1)-3F(x-2)+3F(x-3)-F(x-4)\\
 &-2F(x-1-h)+6F(x-2-h)\\
 &-6F(x-3-h)+2F(x-4-h).
\end{aligned}}
\tag{L-22101.6}
\]

Every value is a finite ordinary-prime sum. No prime power, zero ordinate, or
analytic continuation is used in (L-22101.5).

## 3. Exact pole-model annihilation

The continuous pole model on logarithmic scale is

\[
 dP_0(y)=e^{y/2}\,dy.
\]

One convenient twice-primitive is

\[
 F_0(x)=4e^{x/2}.
\]

Because

\[
 2e^{-h/2}=2\cdot4^{-1/2}=1,
\]

one has

\[
 (I-2T_h)F_0=0.
 \tag{L-22101.7}
\]

Moreover `Delta_1^3` annihilates every polynomial of degree at most two. Hence
for arbitrary constants `A,B,C`,

\[
 \boxed{
 Q_H^{\mathbb P}
 =\Delta_1^3(I-2T_h)
  \bigl(F-4e^{x/2}-Ax^2-Bx-C\bigr)(x-1).
 }
 \tag{L-22101.8}
\]

The prime-only signal is therefore a fixed compact wavelet coefficient of the
complete weighted prime discrepancy. Its three ordinary vanishing moments and
its exponential moment at `1/2` are exact.

## 4. Mean-square criterion

Combining with `T-21502`, subject to independent review of that transfer theorem,

\[
\boxed{
\mathrm{RH}
\iff
\int^X
\left|
 \Delta_1^3(I-2T_h)F(x-1)
\right|^2dx
=\exp(o(X)).
}
\tag{L-22101.9}
\]

Thus the global problem can be viewed as a one-scale wavelet square-function
bound for one explicit convex prime ramp.

## 5. Proof boundary

- Equations (L-22101.5)--(L-22101.8) are exact.
- They remove the matrix and semiprime notation but do not prove the required
  mean-square estimate.
- Absolute bounds on the ramp or its total variation lose the signed
  finite-difference cancellation and remain exponentially too large.
