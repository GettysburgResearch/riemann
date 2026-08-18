# R-98071 — No finite dyadic target filter cancels both tail modes and stays nonnegative

Claim ID: `R-98071`  
Status: **PROVED EXACT NO-GO THEOREM**  
RH status: **not assumed**

Let
\[
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},\qquad
K(y)=\sum_{j=0}^m a_jT(y/4^j).
\]
Cancelling the square-root and constant tail modes forces
\[
\sum_j a_j=0,\qquad \sum_j2^{-j}a_j=0.
\]

On the final activation band `4^(m-1)<=y<4^m`, all earlier scales are already
active and the two cancellation equations reduce the kernel to
\[
K(y)=a_m\left(3-\frac{4\sqrt y}{2^m}\right).
\]
The bracket moves from `+1` to `-1` across the band. Hence every nonzero finite
two-mode-cancelling dyadic filter changes sign.

Therefore a finite positive Haar/Q4-style target filter cannot close the route.
