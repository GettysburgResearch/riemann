# L-97600 — The canonical rows, the 5:3 scalar and every real-endpoint knot are explicit

Claim ID: `L-97600`  
Status: **PROVED EXACT ANALYTIC ALGEBRA**  
Created: 2026-08-17  
RH status: **not assumed**

For `j>=2`, define

\[
A_j={j+1\over j-1},\qquad
B_j={(j+1)(j-2)\over j(j-1)},\qquad
C_j={2\over j(j-1)}
\]

and

\[
Q_Y(j)=A_jh_j(Y)-B_jh_{j+1}(Y)+C_j\sum_{m\ge j+2}h_m(Y),
\]

where

\[
h_m(Y)=m^{-1/2}\log(Y/m)\,\mathbf1_{Y\ge m}.
\]

Every hinge vanishes at its activation point.  Hence `Q_Y(j)` is continuous for
all real `Y>0`, affine in `log Y` on every open activation cell, and has both
one-sided knot limits equal to its knot value.

Put

\[
c_X(j)=\sum_{k\ge1}{\mu(k)\over\sqrt k}Q_{X/k}(j)
\]

(the sum is finite), and

\[
R_X=5c_X(2)+3c_X(3).
\]

The unsieved coefficient dictionary is

\[
q_*(1)=0,\quad q_*(2)=15,\quad q_*(3)=6,\quad q_*(4)=3,
\quad q_*(m)=6\ (m\ge5).
\]

Thus

\[
R_X=\sum_{n\le X}{a_*(n)\over\sqrt n}\log(X/n)
\]

with

\[
a_*(n)=6\mathbf1_{n=1}-6\mu(n)
 +9\mathbf1_{2\mid n}\mu(n/2)
 -3\mathbf1_{4\mid n}\mu(n/4).
\]

The same continuity statement holds for every real `X`: a newly entering term
has zero logarithmic hinge, so no integer-only interpolation theorem is needed.
