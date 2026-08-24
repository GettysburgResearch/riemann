# L-105501 — Second-chaos Wick cancellation leaves energy below one thousandth

Claim ID: `L-105501`  
Status: **PROVED FROM THE PRIME NUMBER THEOREM**  
Created: 2026-08-24  
Depends on: the higher-order Wick identity in `L-105320`

## 1. Exact degree-two cancellation

Let

\[
A_X(s)=\sum_{2\le n\le X}\frac{\Lambda(n)}{n^s},
\qquad x=\frac{A_X(s)}L,
\]

and take the source-fixed zero-free entire factor

\[
\boxed{
W_{2,L,X}(s)
=
\exp\!\left(-\frac{x}{2}-\frac{x^2}{4}\right).
}
\tag{L-105501.1}
\]

The `K=2` case of `L-105320.10` gives

\[
\boxed{
\frac{L W_{2,L,X}(s)^2}{L-A_X(s)}
=
\exp\!\left(\sum_{j\ge3}\frac{x^j}{j}\right)
=:\sum_{m\ge0}d_mx^m.
}
\tag{L-105501.2}
\]

Thus

\[
d_0=1,
\qquad d_1=d_2=0,
\tag{L-105501.3}
\]

and both first and second Euler chaos vanish exactly.  Logarithmic
differentiation gives the positive recurrence

\[
\boxed{
md_m=\sum_{j=3}^{m}d_{m-j}
\quad(m\ge1).
}
\tag{L-105501.4}
\]

In particular

\[
d_3=\frac13,
\qquad d_4=\frac14,
\qquad d_5=\frac15,
\]

and induction in (L-105501.4) gives

\[
0\le d_m\le1
\quad(m\ge0).
\tag{L-105501.5}
\]

## 2. Arithmetic coefficient energy

Define the normalized second-chaos-cancelled coefficients

\[
\boxed{
a_{2,L}(n)=
\sum_{m=3}^{\Omega(n)}
 d_mL^{-m}\Lambda^{*m}(n).
}
\tag{L-105501.6}
\]

The squarefree-simplex and repeated-prime argument of `L-105321` applies
verbatim: for each fixed degree `m`, the squarefree contribution tends to
`d_m^2 m!/(2m)!`; mixed degrees and repeated-prime patterns vanish after
normalization; and (L-105501.5) supplies the same uniform factorial
majorant.  Hence

\[
\boxed{
\lim_{L\to\infty}
\sum_{n\le e^L}\frac{a_{2,L}(n)^2}{n}
=
\mathcal D_{W,2}
:=
\sum_{m=3}^{\infty}d_m^2\frac{m!}{(2m)!}.
}
\tag{L-105501.7}
\]

The convergence is uniform for `n<=e^(theta L)` on compact theta intervals,
with the usual factor `theta^(2m)`.

## 3. Exact rational upper bound

The first three terms are

\[
\frac1{1080},
\qquad
\frac1{26880},
\qquad
\frac1{756000}.
\tag{L-105501.8}
\]

Put `t_m=m!/(2m)!`.  For `m>=6`, (L-105501.5) and

\[
\frac{t_{m+1}}{t_m}=rac1{2(2m+1)}\le\frac1{26}
\]

give

\[
\sum_{m\ge6}d_m^2t_m
\le\frac{t_6}{1-1/26}
=\frac{13}{8316000}.
\tag{L-105501.9}
\]

Therefore

\[
\boxed{
\mathcal D_{W,2}
\le
\frac1{1080}+\frac1{26880}+\frac1{756000}
+\frac{13}{8316000}
=
\frac{9181}{9504000}
<\frac1{1000}.
}
\tag{L-105501.10}
\]

The diagnostic value is `0.0009645283...`; only the rational bound is used.

## 4. Scope

The cancellation identity and coefficient recurrence are exact finite
Dirichlet algebra.  The energy limit uses the prime number theorem exactly as
`L-105321` does.  This lemma does not bound the horizontal growth of
`W_(2,L,X)` or identify the frozen model with the actual Xi contour matrix.
Those costs are retained in `W2XFER105500`.
