# L-93600 — The square-root logarithmic ramp has a uniform `5 Y^(-3/2)` remainder

Claim ID: `L-93600`  
Status: **PROVED ANALYTIC ESTIMATE**  
Created: 2026-08-15  
RH status: **unproved**

For real `Y>=1`, put

\[
 S(Y)=\sum_{n\le Y}\frac1{\sqrt n}\log\frac Yn.
\]

Then

\[
\boxed{
 S(Y)=4\sqrt Y+\zeta(1/2)\log Y+\zeta'(1/2)+R(Y),
 \qquad |R(Y)|<5Y^{-3/2}.
}
\tag{L-93600.1}
\]

## Proof

Let `N=floor(Y)`, `a=N+1`, and `h=log(a/Y)`. Thus `a>=2` and

\[
 0\le h\le\log\frac a{a-1}\le\frac1{a-1}.
\tag{L-93600.2}
\]

Write the finite sum as

\[
S(Y)=\log Y\,[\zeta(1/2)-\zeta(1/2,a)]
     +[\zeta'(1/2)-\partial_s\zeta(s,a)|_{s=1/2}].
\]

Euler--Maclaurin for the Hurwitz tail, stopped after `B_2`, gives

\[
\zeta(s,a)=\frac{a^{1-s}}{s-1}+\frac12a^{-s}
 +\frac{s}{12}a^{-s-1}+\mathcal R(s,a),
\]

\[
\mathcal R(s,a)
=-\frac{s(s+1)}2\int_a^\infty \bar B_2(t)t^{-s-2}\,dt,
\qquad |\bar B_2(t)|\le\frac16.
\]

Substitution at `s=1/2` yields

\[
\begin{aligned}
R(Y)={}&\sqrt a(4-2h-4e^{-h/2})
 +\frac h{2\sqrt a}
 -\frac{1/12-h/24}{a^{3/2}}+\mathcal E(Y).
\end{aligned}
\tag{L-93600.3}
\]

The elementary inequalities

\[
0\ge4-2h-4e^{-h/2}\ge-\frac{h^2}{2}
\]

and (L-93600.2) show that the first three terms in (L-93600.3), after
multiplication by `a^(3/2)`, have absolute sum below `25/8`.

For the differentiated Euler remainder, with
`C(s)=s(s+1)/2`, one obtains exactly

\[
\mathcal E(Y)=C'(1/2)I+C(1/2)
 \int_a^\infty \bar B_2(t)(\log Y-\log t)t^{-5/2}\,dt,
\]

where $I=\int_a^\infty \bar B_2(t)t^{-5/2}\,dt$. Hence

\[
|\mathcal E(Y)|
\le a^{-3/2}\left(\frac19+\frac h{24}+\frac1{36}\right)
<\frac15a^{-3/2}.
\]

Since `a>Y`, these estimates give the deliberately rounded bound `5Y^(-3/2)`.

## Component-row corollary

For `Y>=j+1`, the exact Green normal form gives

\[
Q_Y(j)=a_j\sqrt Y+b_j\log Y+c_j+\varepsilon_j(Y),
\]

where

\[
a_j=\frac8{j(j-1)},
\]

\[
 b_j=\frac2{j(j-1)}\zeta(1/2)
 -\frac2{j(j-1)}\sum_{m<j}m^{-1/2}
 +\frac{j+2}{j\sqrt j}-\frac1{\sqrt{j+1}},
\]

\[
 c_j=\frac2{j(j-1)}\zeta'(1/2)
 +\frac2{j(j-1)}\sum_{m<j}\frac{\log m}{\sqrt m}
 -\frac{j+2}{j\sqrt j}\log j
 +\frac{\log(j+1)}{\sqrt{j+1}},
\]

and

\[
\boxed{|\varepsilon_j(Y)|<\frac{10}{j(j-1)}Y^{-3/2}.}
\tag{L-93600.4}
\]

The first activation strip `j<=Y<j+1` remains exact:

\[
Q_Y(j)=\frac{j+1}{(j-1)\sqrt j}\log\frac Yj.
\]
