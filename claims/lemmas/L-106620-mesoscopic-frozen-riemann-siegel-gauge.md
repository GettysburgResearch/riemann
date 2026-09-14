# L-106620 — Mesoscopic frozen Riemann--Siegel gauge

Claim ID: `L-106620`  
Status: **PROVED EXACT ALGEBRA + UNIFORM CARRIER-MISMATCH BOUND**  
Created: 2026-08-26  
Depends on: `L-106610--L-106612`  
RH status: **not assumed**

Let

\[
\Xi=Ae^{i\vartheta}h,\qquad
h(t)=\zeta(1/2+it),
\]

and put

\[
q=A'/A,\qquad \omega=\vartheta',\qquad
\mathscr L=D+q+i\omega,\qquad H_k=\mathscr L^k h.
\]

Fix \(B>0\). Partition a regular dyadic interval \([T,2T]\) into

\[
J_T=\lceil(\log T)^B\rceil
\]

regular subintervals \(I_j\) of length \(O(T/J_T)\). Choose
\(t_j\in I_j\) and the positive constant companion scale

\[
\boxed{\lambda_j=\omega(t_j)^{-1}.}
\tag{L-106620.1}
\]

## 1. Exact constant-scale packets

On \(I_j\), define

\[
\boxed{
C_{k,j}
=(1-\lambda_j\omega)H_k
+i\lambda_j(D+q)H_k,
}
\tag{L-106620.2}
\]

\[
\boxed{
R_{k,j}
=(1+\lambda_j\omega)H_k
-i\lambda_j(D+q)H_k.
}
\tag{L-106620.3}
\]

Since \(H_{k+1}=(D+q+i\omega)H_k\),

\[
\boxed{
\Xi^{(k)}+i\lambda_j\Xi^{(k+1)}
=Ae^{i\vartheta}C_{k,j},
}
\tag{L-106620.4}
\]

\[
\boxed{
\Xi^{(k)}-i\lambda_j\Xi^{(k+1)}
=Ae^{i\vartheta}R_{k,j}.
}
\tag{L-106620.5}
\]

Therefore the fifth-endpoint quotient on \(I_j\) is exactly

\[
\boxed{
U_{5,j}
=\frac{R_{0,j}C_{5,j}}{C_{0,j}R_{5,j}}.
}
\tag{L-106620.6}
\]

No variable companion coefficient and no diagonal Rouché argument is used.

## 2. Exact amplitude cancellation

Direct expansion gives

\[
\boxed{
R_{0,j}C_{5,j}-C_{0,j}R_{5,j}
=
2i\lambda_j
\left(h\,DH_5-(Dh)H_5\right).
}
\tag{L-106620.7}
\]

The \(q\)-connection cancels exactly, just as in `L-106611`. The only
difference from the fully adaptive packet is that the carrier residual remains
inside the four denominator/numerator packets, where it is explicit.

## 3. Arbitrarily accurate carrier matching

Stirling gives

\[
\omega'(t)=\frac1{2t}+O(t^{-3}),
\qquad
\omega(t)\asymp\log T
\]

uniformly on \([T,2T]\). Hence

\[
\sup_{t\in I_j}
|1-\lambda_j\omega(t)|
\ll\frac1{J_T\log T}
\ll(\log T)^{-B-1}.
\tag{L-106620.8}
\]

Thus the frozen packets approach the exact carrier-cancelled packets at an
arbitrarily high fixed logarithmic rate by increasing \(B\), while preserving
a constant companion coefficient on every subwindow.

This coefficient-level estimate is not promoted to a Hankel-charge estimate:
phase measure can concentrate. The conclusion-facing microscopic mean remains
explicit in `T-106620`.
