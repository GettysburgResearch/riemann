# L-32306 — Exact dyadic sign blocks of the five-mode averaged carry image

Claim ID: `L-32306`  
Title: The thirty nonzero averaged carry rows of the five-mode source form four explicit alternating dyadic sign blocks  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Dependencies: `L-32303`; affine Möbius carry contraction  
Scope: finite averaged carry bank; no sign assertion for the triangular inverse

## 1. Polynomial coefficients

Write

\[
P_\Box(x)=\sum_{j=0}^5c_jx^j
\]

with

\[
\boxed{
(c_0,\ldots,c_5)
=
\left(
1,
-{7\over2}-2\sqrt2,
{11\over2}+7\sqrt2,
-8-7\sqrt2,
7+2\sqrt2,
-2
\right).
}
\tag{L-32306.1}
\]

The source is

\[
b_\Box=\sum_{j=0}^5c_j\delta_{2^j}*\mu.
\]

## 2. Closed row formula

For

\[
2^r\le n<2^{r+1},
\qquad0\le r\le5,
\]

only taps `j<=r` are active.  The affine Möbius contraction gives

\[
\begin{aligned}
K_\Box(n)
&:=\sum_{q=2}^nb_\Box(q)\beta_{nq}\\
&=\sum_{j=0}^{r}c_j{2^{j+1}-n-1\over n+1}.
\end{aligned}
\]

Put

\[
C_r=\sum_{j=0}^rc_j,
\qquad
D_r=\sum_{j=0}^r2^{j+1}c_j.
\]

Then

\[
\boxed{
K_\Box(n)={D_r\over n+1}-C_r.
}
\tag{L-32306.2}
\]

The exact partial data are

\[
\boxed{
\begin{array}{c|c|c}
r&C_r&D_r\\ \hline
0&1&2\\
1&-5/2-2\sqrt2&-12-8\sqrt2\\
2&3+5\sqrt2&32+48\sqrt2\\
3&-5-2\sqrt2&-96-64\sqrt2\\
4&2&128\\
5&0&0.
\end{array}}
\tag{L-32306.3}
\]

The final line is exactly the pair of moment cancellations

\[
P_\Box(1)=0,
\qquad
P_\Box(2)=0.
\]

## 3. Four sign blocks

For `2<=n<=3`, substitution of `r=1` in (L-32306.2) gives negative values; explicitly the endpoints are

\[
K_\Box(2)=-{3\over2}-{2\sqrt2\over3}<0,
\qquad
K_\Box(3)=-{1\over2}<0.
\]

For `4<=n<=7`, the expression with `r=2` decreases with `n`; at the right endpoint

\[
K_\Box(7)=1+\sqrt2>0,
\]

so the entire block is positive.

For `8<=n<=15`, the expression with `r=3` increases with `n`; at the right endpoint

\[
K_\Box(15)=-1-2\sqrt2<0,
\]

so the entire block is negative.

For `16<=n<=31`,

\[
K_\Box(n)={128\over n+1}-2.
\]

Since `n+1<=32`,

\[
K_\Box(n)\ge2>0.
\]

Finally, for `n>=32`, all taps are active and `(C_5,D_5)=(0,0)`, so

\[
K_\Box(n)=0.
\]

Therefore

\[
\boxed{
\operatorname{sgn}K_\Box(n)=
\begin{cases}
- & 2\le n<4,\\
+ & 4\le n<8,\\
- & 8\le n<16,\\
+ & 16\le n<32,\\
0 & n\ge32.
\end{cases}}
\tag{L-32306.4}
\]

## 4. Meaning

The finite carry bank is not a generic thirty-dimensional object. Its averaged source lives in four nested dyadic sign blocks whose endpoints are exactly the five source taps.

This does **not** determine the sign of

\[
\sum_{n=2}^{31}c_X(n)K_\Box(n),
\]

because the deep triangular inverse coefficients `c_X(n)` are not known to be nonnegative. Any proof using (L-32306.4) must preserve that firewall.

## 5. Proof boundary

Closed exactly:

- the row formula;
- all partial moments;
- the complete four-block sign pattern;
- vanishing above row 31.

Open:

- a source-specific estimate for the finite-bank pairing with the actual carry inverse;
- RH.
