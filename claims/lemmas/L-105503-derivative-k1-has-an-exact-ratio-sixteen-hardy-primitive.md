# L-105503 — The derivative same-\(K_1\) wavelet has an exact ratio-sixteen Hardy primitive

Claim ID: `L-105503`

Status: **PROVED EXACT KERNEL, CELL, ENDPOINT AND JUMP IDENTITIES**

Created: 2026-08-27

Depends on: `L-100310`, `L-105502`

RH status: **not assumed**

Put

\[
K_2=DK_1.
\]

## 1. Explicit four-band kernel

With right-continuous dyadic endpoints,

\[
\boxed{
K_2(y)=
\begin{cases}
4\sqrt y-3,&1\le y<2,\\
-4(1+\sqrt2)\sqrt y+3(1+2\sqrt2),&2\le y<4,\\
2(1+2\sqrt2)\sqrt y-6(1+\sqrt2),&4\le y<8,\\
-2\sqrt y+6,&8\le y<16,\\
0,&\text{otherwise}.
\end{cases}
}
\tag{L-105503.1}
\]

Its Mellin multiplier is

\[
\widehat K_2(s)
=
\frac{(1-\sqrt2\,2^{-s})^2(1-2^{-s})^2(s+\frac32)}
{s(s-\frac12)}.
\tag{L-105503.2}
\]

The zeros of the dyadic factors lie only on
\(\Re s=0\) and \(\Re s=1/2\).

## 2. Integer-cell affine form

For a finite real coefficient sequence \((c_n)\), put

\[
H_2(X)=\sum_n c_nK_2(X/n).
\tag{L-105503.3}
\]

Every breakpoint is one of

\[
n,2n,4n,8n,16n.
\]

Hence

\[
\boxed{
H_2(X)=A_m+B_m\sqrt X,
\qquad
m<X<m+1.
}
\tag{L-105503.4}
\]

For \(j=0,1,2,3\), let

\[
S_j(m)=
\sum_{m/2^{j+1}<n\le m/2^j}c_n,
\qquad
T_j(m)=
\sum_{m/2^{j+1}<n\le m/2^j}\frac{c_n}{\sqrt n}.
\]

Then

\[
A_m
=
-3S_0
+3(1+2\sqrt2)S_1
-6(1+\sqrt2)S_2
+6S_3,
\tag{L-105503.5}
\]

\[
B_m
=
4T_0
-4(1+\sqrt2)T_1
+2(1+2\sqrt2)T_2
-2T_3.
\tag{L-105503.6}
\]

## 3. One exact Hardy primitive

Define the right-continuous cumulative functions

\[
P_c(x)=\sum_{n\le x}c_n,
\qquad
Q_c(x)=\sum_{n\le x}\frac{c_n}{\sqrt n},
\]

and

\[
\boxed{
W_c(x)=3P_c(x)-4\sqrt x\,Q_c(x).
}
\tag{L-105503.7}
\]

Let

\[
(\mathsf Sf)(x)=f(x/2)
\]

and

\[
\boxed{
\Delta_4
=
(I-\mathsf S)^2(I-\sqrt2\,\mathsf S)^2.
}
\tag{L-105503.8}
\]

Explicitly,

\[
\Delta_4
=
I-(2+2\sqrt2)\mathsf S
+(3+4\sqrt2)\mathsf S^2
-(4+2\sqrt2)\mathsf S^3
+2\mathsf S^4.
\tag{L-105503.9}
\]

Direct telescoping of (L-105503.5)--(L-105503.6) gives

\[
\boxed{
H_2(m+)=-\Delta_4W_c(m).
}
\tag{L-105503.10}
\]

The square root in \(W_c(m/2^j)\) is evaluated at the real argument
\(m/2^j\); replacing it by \(\sqrt{\lfloor m/2^j\rfloor}\) is false.

## 4. Atomic jump filter

Let

\[
(\mathsf S_{\rm at}c)(m)
=
\mathbf1_{2\mid m}\,c_{m/2}.
\]

Then

\[
\boxed{
H_2(m+)-H_2(m-)
=
\Delta_{4,\rm at}c(m),
}
\tag{L-105503.11}
\]

where

\[
\Delta_{4,\rm at}
=
(I-\mathsf S_{\rm at})^2
(I-\sqrt2\,\mathsf S_{\rm at})^2.
\]

Equivalently,

\[
\begin{aligned}
H_2(m+)-H_2(m-)
={}&c_m
-(2+2\sqrt2)\mathbf1_{2\mid m}c_{m/2}\\
&+(3+4\sqrt2)\mathbf1_{4\mid m}c_{m/4}\\
&-(4+2\sqrt2)\mathbf1_{8\mid m}c_{m/8}
+2\mathbf1_{16\mid m}c_{m/16}.
\end{aligned}
\tag{L-105503.12}
\]

For the native coefficients \(c_n=\mu(n)/\sqrt n\),

\[
\sum_{M\le m\le2M}
\frac{|\Delta_{4,\rm at}c(m)|}{m}
\ll M^{-1/2}.
\tag{L-105503.13}
\]

Thus the endpoint jump ledger is absolutely closed.
