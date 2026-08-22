# L-102721 — The two-mode centered completion defect is one fixed positive-kernel RH detector

Claim ID: `L-102721`  
Status: **PROVED EXACT REDUCTION; SIGN OPEN**  
Created: 2026-08-22  
Depends on: `L-102720`; specialized negative-mass Landau theorem  
RH status: **unproved**

Let

\[
\beta=(\delta_1-\delta_{67})*\mu,
\]

let \(\beta^\square(m^2)=\beta(m)\), and put

\[
\gamma=\beta^\square-\beta.
\]

Its Dirichlet series is

\[
B_\gamma(z)
=
\frac{1-67^{-2z}}{\zeta(2z)}
-
\frac{1-67^{-z}}{\zeta(z)}.
\tag{L-102721.1}
\]

For

\[
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},
\]

define the positive quadratic completion difference

\[
Q_\gamma(X)
=
\sum_n\frac{\gamma(n)}{\sqrt n}T(X/n)^2.
\]

By `L-102720`,

\[
Q_\gamma(X)\ge0.
\]

The first two exact asymptotic modes are

\[
16B_\gamma(3/2)X,
\qquad
-24B_\gamma(1)\sqrt X.
\]

Define the two-mode centered envelope

\[
\boxed{
\mathscr E_\gamma(X)
=
Q_\gamma(X)
-
16B_\gamma(3/2)X
+
24B_\gamma(1)\sqrt X.
}
\tag{L-102721.2}
\]

A coefficientwise calculation gives

\[
\boxed{
\mathscr E_\gamma(X)
=
\sum_n\frac{\gamma(n)}{\sqrt n}R_2(X/n),
}
\tag{L-102721.3}
\]

where the fixed carrier is

\[
\boxed{
R_2(y)=
\begin{cases}
24\sqrt y-16y,&0<y<1,\\
9,&y\ge1.
\end{cases}
}
\tag{L-102721.4}
\]

Thus \(R_2(y)>0\) for every \(y>0\).  Positivity of the carrier is not
positivity of its signed arithmetic projection.

## Mellin transform

For \(0<\Re s<1/2\),

\[
\boxed{
\widehat R_2(s)
=
\int_0^\infty R_2(y)y^{-s-1}\,dy
=
\frac{2s^2+5s+9}{s(s-1)(2s-1)}.
}
\tag{L-102721.5}
\]

For \(0<X<1\),

\[
\mathscr E_\gamma(X)
=
24B_\gamma(1)\sqrt X
-
16B_\gamma(3/2)X.
\tag{L-102721.6}
\]

Consequently

\[
\boxed{
\begin{aligned}
\int_1^\infty
\mathscr E_\gamma(X)X^{-s-1}\,dX
={}&
\widehat R_2(s)B_\gamma(s+1/2)\\
&-
\frac{24B_\gamma(1)}{1/2-s}
+
\frac{16B_\gamma(3/2)}{1-s}.
\end{aligned}
}
\tag{L-102721.7}
\]

The second line cancels the apparent positive-real poles at \(s=1/2\) and
\(s=1\).  The continuation is holomorphic at every positive real \(s\).

If \(\rho\) is a zeta zero with \(\Re\rho>1/2\), then
\(s_\rho=\rho-1/2\) is a genuine pole of (L-102721.7):

- the \(B_\gamma(2\rho)\) term is holomorphic because \(\Re(2\rho)>1\);
- \(1-67^{-\rho}\ne0\);
- the roots of \(2s^2+5s+9\) have real part \(-5/4\).

Therefore either

\[
\mathscr E_\gamma(X)\ge0
\quad\text{eventually},
\]

or the weaker estimate

\[
\boxed{
\int_1^Y(\mathscr E_\gamma(X))_-\frac{dX}{X}
=
Y^{o(1)}
}
\tag{CCE102721}
\]

implies RH.

## Exact small-scale sign

For \(0<X\le1\), (L-102721.6) is strictly positive.  Indeed
\(\pi<22/7\) gives

\[
B_\gamma(1)=\frac{1-67^{-2}}{\zeta(2)}>3/5,
\]

while the integral bound \(\zeta(3/2)<14/5\) gives

\[
B_\gamma(3/2)
<
1-rac13
=
2/3.
\]

Hence

\[
24B_\gamma(1)
>
16B_\gamma(3/2).
\]

The sign for all \(X\ge1\) remains open and conclusion-bearing.
