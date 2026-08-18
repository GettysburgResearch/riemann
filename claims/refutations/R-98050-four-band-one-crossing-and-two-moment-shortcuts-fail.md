# R-98050 — The four-band critical kernel is neither one-crossing reducible nor two-moment free

Claim ID: `R-98050`  
Status: **PROVED EXACT FINITE-ALGEBRA FIREWALL**  
Created: 2026-08-18  
Depends on: `L-97702`  
RH status: **not assumed**

The exact four-band coefficients in `L-97702` are

\[
\begin{aligned}
c_0&=-3/2,\\
c_1&=(9\sqrt2-3)/2,\\
c_2&=(9\sqrt2-12)/2,\\
c_3&=-6.
\end{aligned}
\]

Their cumulative sums are

\[
-\frac32,
\qquad -3+\frac{9\sqrt2}{2},
\qquad -9+9\sqrt2,
\qquad -15+9\sqrt2.
\]

The signs are respectively

\[
-,+,+,-.
\]

Hence summation by parts does not reduce the four-band functional to a positive measure against a one-crossing monotone profile. At least two shape transitions would be required.

Moreover the zeroth and first dyadic moments are nonzero:

\[
\sum_{j=0}^3 c_j=-15+9\sqrt2\ne0,
\]

\[
\sum_{j=0}^3 j c_j=-\frac{63}{2}+\frac{27\sqrt2}{2}\ne0.
\]

Therefore the kernel does not annihilate either the constant mode or the first dyadic trend. No exact reduction to a pure second discrete curvature is available without adding compensating terms that must themselves be controlled.

This rules out two tempting source-blind shortcuts for C4MBI67:

1. a single-crossing theorem for `B_(1/2)`;
2. a free two-moment/convexity reduction of the four-band kernel.

The exact prime-ownership or future-state structure remains necessary.
