# L-96101 — The fixed annular row has an explicit reciprocal-zeta Mellin transform

Claim ID: `L-96101`  
Status: **PROVED EXACT ANALYTIC LEMMA**  
Created: 2026-08-16  
Depends on: `L-96100`  
RH status: **not assumed**

Define

\[
 P_j(z)=A_jj^{-z}-B_j(j+1)^{-z}
 -C_j\sum_{m=1}^{j+1}m^{-z}.
\tag{L-96101.1}
\]

For `Re(s)>1/2`, absolute convergence and

\[
 \int_m^\infty\log(X/m)X^{-s-1}\,dX=\frac{m^{-s}}{s^2}
\]

give

\[
 \int_1^\infty c_X(j)X^{-s-1}\,dX
 =\frac{C_j}{s^2}
 +\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}.
\tag{L-96101.2}
\]

Since `c_Y(j)=0` for `Y<j`, the substitution `X=4Y` is exact at the lower limit and yields

\[
 \int_1^\infty c_{X/4}(j)X^{-s-1}\,dX
 =4^{-s}\int_1^\infty c_X(j)X^{-s-1}\,dX.
\]

Therefore the annular transform is

\[
 \boxed{
 \mathcal A_j(s)
 :=\int_1^\infty a_j(X)X^{-s-1}\,dX
 =(1-4^{-s})
 \left[
  \frac{C_j}{s^2}
  +\frac{P_j(s+1/2)}{s^2\zeta(s+1/2)}
 \right].
 }
\tag{L-96101.3}
\]

This formula is independent of `J_Lambda`, `P_Lambda`, `F_Lambda`, the sparse `Y_4` dual, the prime-square moat, and the endpoint-sign theorem.

For every positive real `s`, `z=s+1/2` is a positive real number greater than `1/2`. The zeta function has no zero there: it is positive for `z>1`, and for `0<z<1` the alternating eta representation has positive numerator and nonzero denominator. At `z=1`, `1/zeta(z)` has a zero. Thus

\[
 \boxed{\mathcal A_j(s)\text{ is holomorphic at every real }s>0.}
\tag{L-96101.4}
\]

At a nontrivial zero `rho` with `Re(rho)>1/2`, the only possible cancellation of the reciprocal-zeta pole is by `P_j(rho)`; the annular factor cannot vanish because

\[
 |4^{-(\rho-1/2)}|=4^{-(\Re\rho-1/2)}<1.
\tag{L-96101.5}
\]
