# L-105470 — The derivative-outer current is affine in `sqrt(X)` on every integer cell

Claim ID: `L-105470`

Status: **PROVED EXACT CELL LOCALIZATION AND CLOSED CELL INTEGRAL**

Let

\[
K_L(y)=
\begin{cases}
8-4\sqrt y,&1\le y<2,\\
-8(1+\sqrt2)+4\sqrt2\sqrt y,&2\le y<4,\\
8\sqrt2-2\sqrt y,&4\le y<8,\\
0,&\text{otherwise},
\end{cases}
\tag{L-105470.1}
\]

be the fixed derivative-outer kernel of `L-102880`.  For a finite real
coefficient sequence \((a_n)\), put

\[
H(X)=\sum_{n\ge1}a_nK_L(X/n).
\tag{L-105470.2}
\]

The canonical arithmetic application has \(a_n=\sigma_U(n)/\sqrt n\), after
all literal source representations with physical product \(n\) have been
recombined.

## 1. Exact cell normal form

Fix an integer \(m\ge1\) and let \(m<X<m+1\).  Because every breakpoint of
\(K_L(X/n)\) is one of

\[
X=n,\quad X=2n,\quad X=4n,\quad X=8n,
\]

all breakpoints are integers.  The active index sets are therefore constant on
the open unit cell.  Define

\[
\begin{aligned}
S_0(m)&=\sum_{m/2<n\le m}a_n,
&T_0(m)&=\sum_{m/2<n\le m}{a_n\over\sqrt n},\\
S_1(m)&=\sum_{m/4<n\le m/2}a_n,
&T_1(m)&=\sum_{m/4<n\le m/2}{a_n\over\sqrt n},\\
S_2(m)&=\sum_{m/8<n\le m/4}a_n,
&T_2(m)&=\sum_{m/8<n\le m/4}{a_n\over\sqrt n}.
\end{aligned}
\tag{L-105470.3}
\]

Direct substitution in (L-105470.1) gives

\[
\boxed{H(X)=A_m+B_m\sqrt X\qquad(m<X<m+1),}
\tag{L-105470.4}
\]

where

\[
\boxed{
\begin{aligned}
A_m
 &=8S_0(m)-8(1+\sqrt2)S_1(m)+8\sqrt2S_2(m),\\
B_m
 &=-4T_0(m)+4\sqrt2T_1(m)-2T_2(m).
\end{aligned}}
\tag{L-105470.5}
\]

No asymptotic approximation or smoothing occurs.

## 2. Exact logarithmic cell mass

Put

\[
a=\sqrt m,
\qquad
b=\sqrt{m+1},
\qquad
F_m(t)=A_m\log t+B_mt.
\]

Then

\[
\Psi_m
 :=\int_m^{m+1}|H(X)|{dX\over X}
 =2\int_a^b{|A_m+B_mt|\over t}\,dt.
\tag{L-105470.6}
\]

If \(B_m\ne0\) and the real root

\[
r_m=-A_m/B_m
\]

lies strictly between \(a\) and \(b\), then

\[
\boxed{
\Psi_m
 =2\left(
 |F_m(r_m)-F_m(a)|
 +|F_m(b)-F_m(r_m)|
 \right).
}
\tag{L-105470.7}
\]

Otherwise

\[
\boxed{
\Psi_m=2|F_m(b)-F_m(a)|.
}
\tag{L-105470.8}
\]

These formulae include the constant case \(B_m=0\).

## 3. Uniform two-endpoint equivalence

Let

\[
u_m=H(m+),
\qquad
v_m=H((m+1)-),
\qquad
w_m={\sqrt{m+1}-\sqrt m\over\sqrt m}
     =\sqrt{1+{1\over m}}-1.
\]

For an affine function on \([a,b]\),

\[
{b-a\over4}(|u|+|v|)
\le
\int_a^b|q(t)|dt
\le
{b-a\over2}(|u|+|v|).
\tag{L-105470.9}
\]

The lower constant is sharp when \(u=-v\).  Since
\(1/b\le1/t\le1/a\) and \(b/a\le\sqrt2\), (L-105470.6) gives

\[
\boxed{
{w_m\over2\sqrt2}(|u_m|+|v_m|)
\le
\Psi_m
\le
w_m(|u_m|+|v_m|).
}
\tag{L-105470.10}
\]

Also

\[
\boxed{
{1\over(1+\sqrt2)m}
\le w_m\le {1\over2m}.
}
\tag{L-105470.11}
\]

Thus the continuous logarithmic absolute mass is already a uniformly
discrete two-endpoint norm.  The values assigned to `K_L` at its finitely many
breakpoints do not affect (L-105470.6).
