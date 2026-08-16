# L-96010 — Every fixed annular component row has an exact reciprocal-zeta Mellin transform

Claim ID: `L-96010`  
Status: **PROVED EXACT ANALYTIC ALGEBRA**  
Created: 2026-08-16  
RH status: **not assumed**

For \(j\ge2\), define

\[
A_j=\frac{j+1}{j-1},\qquad
B_j=\frac{(j+1)(j-2)}{j(j-1)},\qquad
C_j=\frac2{j(j-1)}.
\]

The canonical unsieved component is

\[
Q_X(j)=
 \frac{A_j}{\sqrt j}\log\frac Xj\mathbf1_{X\ge j}
-\frac{B_j}{\sqrt{j+1}}\log\frac X{j+1}\mathbf1_{X\ge j+1}
+C_j\sum_{m\ge j+2}
 \frac1{\sqrt m}\log\frac Xm\mathbf1_{X\ge m}.
\tag{L-96010.1}
\]

The native component row is the finite Möbius transform

\[
c_X(j)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j).
\tag{L-96010.2}
\]

Put

\[
P_j(z)=A_jj^{-z}-B_j(j+1)^{-z}
-C_j\sum_{m=1}^{j+1}m^{-z}.
\tag{L-96010.3}
\]

For \(\Re s>1/2\), absolute convergence and

\[
\int_m^\infty \log(X/m)X^{-s-1}\,dX=\frac{m^{-s}}{s^2}
\]

give

\[
\boxed{
\mathcal C_j(s):=
\int_1^\infty c_X(j)X^{-s-1}\,dX
=\frac{C_j}{s^2}
+\frac{P_j(s+\tfrac12)}{s^2\zeta(s+\tfrac12)}.
}
\tag{L-96010.4}
\]

Now define the actual scale-four annular component

\[
a_X(j)=c_X(j)-c_{X/4}(j),
\tag{L-96010.5}
\]

with zero extension below support. Substituting \(X=4Y\) in the second Mellin
integral gives

\[
\boxed{
\mathcal A_j(s):=
\int_1^\infty a_X(j)X^{-s-1}\,dX
=(1-4^{-s})
\left[
 \frac{C_j}{s^2}
 +\frac{P_j(s+\tfrac12)}{s^2\zeta(s+\tfrac12)}
\right].
}
\tag{L-96010.6}
\]

For \(\Re s>0\), the annular factor cannot vanish because
\(|4^{-s}|<1\). This direct transform never mentions
\(J_\Lambda,P_\Lambda,F_\Lambda\), a physical score, or a prime-square moat.
