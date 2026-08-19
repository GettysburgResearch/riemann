# L-99550 — The arithmetic Volterra atom is uniquely double clamped

Claim ID: `L-99550`  
Status: **PROVED EXACT**  
Created: 2026-08-19  
Depends on: `L-99230`  
RH status: **unproved**

For \(y>0\), let

\[
V_y f
=
\frac{2y^2f''-yf'+f}{2\sqrt y}.
\tag{L-99550.1}
\]

Define, for \(y\ge1\),

\[
\boxed{
\Phi(y)
=
4y\log y
+
2\sqrt y\log y
-
12y
+
12\sqrt y,
}
\tag{L-99550.2}
\]

and set \(\Phi(y)=0\) for \(0<y<1\).

## 1. Exact inverse density

For an exponent \(a\),

\[
\begin{aligned}
&(2y^2\partial_y^2-y\partial_y+1)(y^a\log y)\\
&\qquad=
(2a^2-3a+1)y^a\log y+(4a-3)y^a,
\end{aligned}
\tag{L-99550.3}
\]

while

\[
(2y^2\partial_y^2-y\partial_y+1)y^a
=
(2a^2-3a+1)y^a.
\tag{L-99550.4}
\]

At \(a=1\) and \(a=1/2\), the logarithmic coefficient vanishes. Therefore

\[
V_y(y\log y)=\frac{\sqrt y}{2},
\qquad
V_y(\sqrt y\log y)=-\frac12,
\tag{L-99550.5}
\]

and

\[
V_y(y)=V_y(\sqrt y)=0.
\tag{L-99550.6}
\]

Substitution in (L-99550.2) gives

\[
\boxed{
V_y\Phi(y)=2\sqrt y-1
\qquad(y>1).
}
\tag{L-99550.7}
\]

## 2. Unique activation clamps

Start from the general open-cell primitive

\[
\Phi_{a,b}(y)
=
4y\log y+2\sqrt y\log y+ay+b\sqrt y.
\tag{L-99550.8}
\]

At activation,

\[
\Phi_{a,b}(1)=a+b,
\tag{L-99550.9}
\]

and

\[
\Phi'_{a,b}(1+)=6+a+\frac b2.
\tag{L-99550.10}
\]

The two conditions

\[
\Phi_{a,b}(1)=0,
\qquad
\Phi'_{a,b}(1+)=0
\tag{L-99550.11}
\]

have the unique solution

\[
\boxed{a=-12,\qquad b=12.}
\tag{L-99550.12}
\]

Thus the homogeneous coefficients in (L-99550.2) are forced by continuity of
both the packet and its first derivative at the activation threshold.

## 3. Exact Green reconstruction

For \(x\ge1\), PR #638's Green kernel at lower endpoint \(1\) is

\[
K(x,t)
=
\mathbf1_{x\ge t}
\frac{2(x-\sqrt{xt})}{t^{3/2}}.
\tag{L-99550.13}
\]

Direct integration gives

\[
\begin{aligned}
\int_1^x K(x,t)(2\sqrt t-1)\,dt
&=
4x\log x+2\sqrt x\log x\\
&\quad-12x+12\sqrt x\\
&=\Phi(x).
\end{aligned}
\tag{L-99550.14}
\]

Since \(\Phi(1)=\Phi'(1+)=0\), both homogeneous coefficients of the Green
formula are zero.

```text
open-cell inverse density       2 sqrt(y)-1
value clamp                     exact zero
first-derivative clamp          exact zero
sqrt(y) homogeneous mode        zero
y homogeneous mode              zero
```
