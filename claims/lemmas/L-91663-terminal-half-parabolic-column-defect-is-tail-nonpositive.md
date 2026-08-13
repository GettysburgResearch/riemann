# L-91663 — Every terminal-half parabolic column-defect tail is nonpositive

Claim ID: `L-91663`  
Status: **PROVED EXACT FINITE-ARITHMETIC TAIL THEOREM**  
Created: 2026-08-13  
Depends on: the parabolic seed and column response of `L-90015`; compatible with the continuum majorization of `L-26202`  
RH status: **unproved**

## 1. Finite parabolic column defect

For an integer endpoint `X>=3`, retain the nonnegative parabolic seed

\[
b_X(m)
=2\sqrt m\left[
 \log\frac Xm-2\left(1-\sqrt{\frac mX}\right)
\right]\mathbf 1_{m\le X}
\tag{L-91663.1}
\]

and the ordinary column response

\[
v_q(b_X)=\sum_{k\ge1}[b_X(kq)-b_X(kq+1)].
\tag{L-91663.2}
\]

The native target is

\[
w_X(q)=q^{-1/2}\log(X/q)\mathbf 1_{q\le X},
\tag{L-91663.3}
\]

and the signed column defect is

\[
r_X(q)=v_q(b_X)-w_X(q).
\tag{L-91663.4}
\]

## 2. Exact telescoping in the terminal half

Fix an integer `Q` with

\[
\frac X2<Q\le X.
\tag{L-91663.5}
\]

For every `q>=Q`, one has `2q>X`, so only the term `k=1` is active in
(L-91663.2). Therefore

\[
v_q(b_X)=b_X(q)-b_X(q+1).
\tag{L-91663.6}
\]

With the zero extension `b_X(X+1)=0`, summation gives the exact identity

\[
\boxed{
\sum_{q=Q}^{X}v_q(b_X)=b_X(Q).
}
\tag{L-91663.7}
\]

Thus the whole terminal-half tail problem is one scalar comparison between the
endpoint seed and the target tail.

## 3. The target sum dominates its integral

Put

\[
f_X(x)=x^{-1/2}\log(X/x)
\qquad(0<x\le X).
\tag{L-91663.8}
\]

Direct differentiation gives

\[
f_X'(x)
=-x^{-3/2}\left(1+\frac12\log(X/x)\right)<0.
\tag{L-91663.9}
\]

Hence `f_X` is nonnegative and decreasing. For every integer `Q<=X`,

\[
\sum_{q=Q}^{X}w_X(q)
=\sum_{q=Q}^{X}f_X(q)
\ge\int_Q^Xf_X(x)\,dx.
\tag{L-91663.10}
\]

The integral is elementary:

\[
\boxed{
\int_Q^Xx^{-1/2}\log(X/x)\,dx
=4\sqrt X-4\sqrt Q-2\sqrt Q\log(X/Q).
}
\tag{L-91663.11}
\]

## 4. The integral dominates the endpoint seed

Write

\[
t=Q/X\in(0,1].
\]

Subtracting (L-91663.1) from (L-91663.11) gives

\[
\begin{aligned}
&\int_Q^Xf_X(x)\,dx-b_X(Q)\\
&\qquad=4\sqrt X
\left[1-t+\sqrt t\log t\right].
\end{aligned}
\tag{L-91663.12}
\]

For `u=sqrt(t)`, define

\[
F(u)=1-u^2+2u\log u.
\]

Then

\[
F'(u)=2(1-u+\log u)\le0
\tag{L-91663.13}
\]

by `log u<=u-1`, and `F(1)=0`. Consequently

\[
\boxed{
1-t+\sqrt t\log t\ge0
\qquad(0<t\le1).
}
\tag{L-91663.14}
\]

It is strict for `t<1`. Therefore

\[
\boxed{
\int_Q^Xf_X(x)\,dx\ge b_X(Q).
}
\tag{L-91663.15}
\]

## 5. Terminal-half tail theorem

Combining (L-91663.7), (L-91663.10), and (L-91663.15),

\[
\begin{aligned}
\sum_{q=Q}^{X}r_X(q)
&=b_X(Q)-\sum_{q=Q}^{X}w_X(q)\\
&\le b_X(Q)-\int_Q^Xf_X(x)\,dx\\
&\le0.
\end{aligned}
\]

Hence

\[
\boxed{
\sum_{q=Q}^{X}r_X(q)\le0
\qquad\left(\frac X2<Q\le X\right).
}
\tag{L-91663.16}
\]

The inequality is strict for every `Q<X`.

Equivalently, on the complete terminal quotient cell, the positive part of the
parabolic overfill is tail-majorized by native slack. This is the exact finite
analogue of the ordered continuum defect-to-slack transport in `L-26202`.

## 6. Transport consequence

Let

\[
\mu_+(q)=[r_X(q)]_+,
\qquad
\mu_-(q)=[-r_X(q)]_+.
\]

Equation (L-91663.16) says that on the ordered set of terminal-half columns,

\[
\mu_+([Q,X])\le\mu_-([Q,X])
\qquad(Q>X/2).
\tag{L-91663.17}
\]

Therefore every positive terminal-half defect admits a monotone transport to
slack at a larger column index. The theorem does not by itself construct the
corresponding nonnegative row perturbation; that finite incidence lift remains
separate.

```text
terminal-half response telescoping                 EXACT
native target sum >= continuum integral            EXACT
continuum integral >= endpoint seed                 EXACT
all terminal-half defect tails <=0                  EXACT
ordered column transport in terminal half           EXACT
positive row/incidence realization of transport     OPEN
remaining quotient cells X/(N+1)<q<=X/N            OPEN
Riemann Hypothesis                                  UNPROVED
```
