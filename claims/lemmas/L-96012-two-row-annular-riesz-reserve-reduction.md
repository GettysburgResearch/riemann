# L-96012 — Annular positivity reduces exactly to two scalar four-adic Riesz reserves at integer knots

Claim ID: `L-96012`  
Status: **PROVED EXACT FINITE REDUCTION**  
Created: 2026-08-16  
Depends on: the finite row formula in `L-96010`  
RH status: **not assumed**

Let

\[
H_X(n)=\min\!\left(\log4,\log\frac Xn\right)_+.
\]

Writing the Möbius and component sums by the product \(n=km\) gives

\[
a_X(j)=\sum_{n\le X}\frac{r_j(n)}{\sqrt n}H_X(n),
\qquad r_j=\mu*q_j,
\tag{L-96012.1}
\]

where

\[
q_j(m)=
\begin{cases}
0,&m<j,\\
A_j,&m=j,\\
-B_j,&m=j+1,\\
C_j,&m\ge j+2.
\end{cases}
\tag{L-96012.2}
\]

For the only two rows needed by the consumer, the divisor kernels are explicit:

\[
\boxed{
r_2(n)=\mathbf1_{n=1}-\mu(n)
+2\mathbf1_{2\mid n}\mu(n/2)
-\mathbf1_{3\mid n}\mu(n/3),
}
\tag{L-96012.3}
\]

and

\[
\boxed{
\begin{aligned}
r_3(n)={}&\frac13\mathbf1_{n=1}-\frac13\mu(n)
-\frac13\mathbf1_{2\mid n}\mu(n/2)\\
&+\frac53\mathbf1_{3\mid n}\mu(n/3)
-\mathbf1_{4\mid n}\mu(n/4).
\end{aligned}}
\tag{L-96012.4}
\]

Define prefix sums

\[
S_j(Y)=\sum_{n\le Y}\frac{r_j(n)}{\sqrt n},
\qquad
T_j(Y)=\sum_{n\le Y}\frac{r_j(n)\log n}{\sqrt n}.
\tag{L-96012.5}
\]

For real \(X\ge1\), put \(N=\lfloor X\rfloor\) and
\(M=\lfloor X/4\rfloor\). Splitting the plateau and ramp in (L-96012.1) gives

\[
\boxed{
a_X(j)=
(\log4)S_j(M)
+(\log X)[S_j(N)-S_j(M)]
-[T_j(N)-T_j(M)].
}
\tag{L-96012.6}
\]

On every open unit cell \((N,N+1)\), both \(N\) and \(M\) are fixed, so the
right side is affine in \(\log X\). At an activation knot the entering source
has value zero, hence the function is continuous. Therefore

\[
\boxed{
a_X(j)\ge0\text{ for all real }X
\iff a_N(j)\ge0\text{ for all integers }N.}
\tag{L-96012.7}
\]

The same sum has the Stieltjes moving-window form

\[
a_X(j)=\int_{X/4}^{X}S_j(t)\,\frac{dt}{t},
\tag{L-96012.8}
\]

where \(S_j\) is the right-continuous step function in (L-96012.5).

Thus the entire upstream requirement for the direct consumer is the pair of
explicit scalar inequalities

\[
\boxed{
\int_{X/4}^{X}S_2(t)\frac{dt}{t}\ge0,
\qquad
\int_{X/4}^{X}S_3(t)\frac{dt}{t}\ge0.
}
\tag{L-96012.9}
\]

No undefined Peano edge term, full row, endpoint score, or native benchmark
appears in this reduction.
