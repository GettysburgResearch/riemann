# L-96100 — Exact annular component rows and reduction from real endpoints to integers

Claim ID: `L-96100`  
Status: **PROVED EXACT FINITE ALGEBRA**  
Created: 2026-08-16  
RH status: **not assumed**

For an integer row index `j>=2`, put

\[
 A_j=\frac{j+1}{j-1},\qquad
 B_j=\frac{(j+1)(j-2)}{j(j-1)},\qquad
 C_j=\frac2{j(j-1)}.
\]

The canonical component spline is

\[
\begin{aligned}
 Q_X(j)={}&
 \frac{A_j}{\sqrt j}\log\frac Xj\,\mathbf1_{X\ge j}
 -\frac{B_j}{\sqrt{j+1}}\log\frac X{j+1}\,
     \mathbf1_{X\ge j+1}\\
 &+C_j\sum_{m\ge j+2}
 \frac1{\sqrt m}\log\frac Xm\,\mathbf1_{X\ge m}.
\end{aligned}
\tag{L-96100.1}
\]

Define the full native component row directly by the finite Möbius sum

\[
 c_X(j)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j).
\tag{L-96100.2}
\]

The scale-four annular component is

\[
 \boxed{a_j(X)=c_X(j)-c_{X/4}(j).}
\tag{L-96100.3}
\]

No endpoint benchmark occurs in these definitions.

## 1. A one-dimensional coefficient formula

Define a finite sequence `p_j` by

\[
 p_j(m)=
 \begin{cases}
 -C_j,&1\le m<j,\\
 1+2/j,&m=j,\\
 -1,&m=j+1,\\
 0,&m>j+1.
 \end{cases}
\tag{L-96100.4}
\]

and its Möbius convolution

\[
 h_j=C_j\delta_1+\mu*p_j.
\tag{L-96100.5}
\]

Completing the tail in (L-96100.1) and using `mu*1=delta_1` gives

\[
 \boxed{
 c_X(j)=\sum_{n\le X}\frac{h_j(n)}{\sqrt n}\log\frac Xn.
 }
\tag{L-96100.6}
\]

Subtracting the quarter-scale copy gives

\[
 \boxed{
 a_j(X)=
 \sum_{n\le X}\frac{h_j(n)}{\sqrt n}
 \min\!\left(\log4,\log\frac Xn\right)_+.
 }
\tag{L-96100.7}
\]

For the two rows used by the direct consumer,

\[
 h_2(n)=\delta_{n1}-\mu(n)
 +2\mathbf1_{2\mid n}\mu(n/2)
 -\mathbf1_{3\mid n}\mu(n/3),
\tag{L-96100.8}
\]

and

\[
\begin{aligned}
 h_3(n)={}&\frac13\delta_{n1}-\frac13\mu(n)
 -\frac13\mathbf1_{2\mid n}\mu(n/2)\\
 &+\frac53\mathbf1_{3\mid n}\mu(n/3)
 -\mathbf1_{4\mid n}\mu(n/4).
\end{aligned}
\tag{L-96100.9}
\]

These formulas are the controlling computational and analytic definitions.

## 2. Exact real-cell reduction

Every breakpoint in (L-96100.7) is of the form `X=n` or `X=4n`, hence is an integer. On each open unit cell `(N,N+1)`, every summand is either zero, constant, or affine in `log X`. Therefore

\[
 a_j(X)=\alpha_{N,j}\log X+\beta_{N,j}
 \qquad(N<X<N+1).
\tag{L-96100.10}
\]

The function is continuous at the endpoints: an entering logarithmic term has value zero, and the tapered-to-flat transition agrees at `log 4`. Thus, if

\[
 X=N^{1-t}(N+1)^t,\qquad 0\le t\le1,
\]

then

\[
 \boxed{
 a_j(X)=(1-t)a_j(N)+t a_j(N+1).
 }
\tag{L-96100.11}
\]

Consequently

\[
 \boxed{
 a_j(X)\ge0\text{ for all real }X
 \iff
 a_j(N)\ge0\text{ for all integers }N.
 }
\tag{L-96100.12}
\]

This eliminates all noninteger activation-cell ambiguity from the remaining producer theorem.
