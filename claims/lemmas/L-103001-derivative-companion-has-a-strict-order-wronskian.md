# L-103001 — The derivative companion has a strict order-Wronskian sign

Claim ID: `L-103001`  
Status: **PROVED EXACT SIGN-REGULARITY THEOREM**  
Created: 2026-08-25  
Depends on: `L-103000`; `L-102701`  
RH status: **not assumed**

Use the logarithmic spline

\[
a(u)=A(e^u)
\]

from `L-103000`, and put

\[
b(u)=A_-(e^u)=a'(u)-\frac12a(u).
\]

The exact two-box formula gives

\[
b(u)=
\begin{cases}
1,&0<u<\log2,\\
-\sqrt2,&\log2<u<2\log2,\\
0,&\text{otherwise}.
\end{cases}
\tag{L-103001.1}
\]

On the interior support define

\[
\psi(u)=\frac{b(u)}{a(u)}.
\]

Then

\[
\boxed{
\psi(u)=
\begin{cases}
\displaystyle {1\over2(e^{u/2}-1)},&0<u<\log2,\\[3mm]
\displaystyle -{1\over2(1-e^{(u-2\log2)/2})},&\log2<u<2\log2.
\end{cases}
}
\tag{L-103001.2}
\]

Both branches are strictly decreasing, and the jump at `u=log 2` is strictly downward. Thus `psi` is strictly decreasing throughout the support.

## Exact Wronskian sign

For source shifts `x<y`, define

\[
\mathcal W_{x,y}(u)
=b(u-x)a(u-y)-a(u-x)b(u-y).
\]

On the overlap of the two translated supports,

\[
\mathcal W_{x,y}(u)
=a(u-x)a(u-y)
[\psi(u-x)-\psi(u-y)].
\]

Since `u-x>u-y` and `psi` is decreasing,

\[
\psi(u-x)-\psi(u-y)\le0.
\]

Outside the overlap, both terms in one translated factor vanish simultaneously. Therefore

\[
\boxed{
 x<y
 \quad\Longrightarrow\quad
 \mathcal W_{x,y}(u)\le0
 \quad\text{for every }u.
}
\tag{L-103001.3}
\]

The inequality is strict on every nonempty region where both translates are positive and avoid the central knot.

Equivalently,

\[
\boxed{
(y-x)\mathcal W_{x,y}(u)\le0.
}
\tag{L-103001.4}
\]

## Multiplicative physical form

For positive integers or real source locations `n<m`, put

\[
\mathcal W_{n,m}(X)
=A_-(X/n)A(X/m)-A(X/n)A_-(X/m).
\]

Then

\[
\boxed{
 n<m
 \quad\Longrightarrow\quad
 \mathcal W_{n,m}(X)\le0
 \quad(X>0).
}
\tag{L-103001.5}
\]

Consequently every nonnegative physical weighting preserves the sign:

\[
\int_0^\infty w(X)\mathcal W_{n,m}(X)\frac{dX}{X}\le0
\qquad(w\ge0).
\tag{L-103001.6}
\]

This is the exact kernel-side orientation missing from the endpoint/Pluecker coordinates. Arithmetic can oppose it only by assigning the opposite sign to an ordered pair.