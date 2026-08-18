# L-95521 — The Q4 kernels intrinsically cancel the continuous prime mode

Claim ID: `L-95521`  
Status: **PROVED EXACT KERNEL THEOREM**  
Created: 2026-08-18  
Depends on: PR #580 `L-95400/L-95402`  
RH status: **not assumed**

PR #580 gives

\[
 \widehat J_0(z)=q(z)\mathcal A_2(t)\widehat W(z),
 \qquad
 \widehat J_1(z)=q(z)\mathcal B_2(t)\widehat W(z),
 \qquad t=2^{-z-1/2},
\]

where

\[
 \mathcal A_2(t)=(1+t)(1-4t^2)^2,
\]

\[
 \mathcal B_2(t)=-t(1-4t^2)(1+8t+4t^2).
\]

At `z=1/2`, one has `t=1/2`. Direct integration of the frozen piecewise
cubic gives

\[
 \widehat W(1/2)=\frac4{315}>0,
\]

and every factor of `q(1/2)` is positive. Therefore

\[
 \boxed{\operatorname{ord}_{z=1/2}\widehat J_0=2,}
 \qquad
 \boxed{\operatorname{ord}_{z=1/2}\widehat J_1=1.}
\tag{L-95521.1}
\]

Equivalently,

\[
 \boxed{
 \int_0^\infty x^{-1/2}J_0(x)\,dx=0,
 \qquad
 \int_0^\infty x^{-1/2}\log x\,J_0(x)\,dx=0,
 }
\tag{L-95521.2}
\]

and

\[
 \boxed{
 \int_0^\infty x^{-1/2}J_1(x)\,dx=0.
 }
\tag{L-95521.3}
\]

## Exact centered prime representation

Let

\[
 \vartheta(y)=\sum_{p\le y}\log p.
\]

For every scale `Y`, compact support and (L-95521.2) give the exact Stieltjes
identity

\[
 \boxed{
 \sum_p\frac{\log p}{\sqrt p}J_0(p/Y)
 =\int_0^\infty t^{-1/2}J_0(t/Y)\,d(\vartheta(t)-t).
 }
\tag{L-95521.4}
\]

The continuous prime-density mode has disappeared before any estimate. The
double zero also annihilates its first logarithmic deformation. Similarly,
`J_1` has one exact continuous-mode cancellation.

This is stronger than merely observing compact support. It identifies the
precise arithmetic object that remains in every Type-I treatment: the centered
prime measure, coupled to the Möbius variable. It does not estimate that
coupling at the polylogarithmic scale.
