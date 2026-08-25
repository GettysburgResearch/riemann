# L-105471 — The cell endpoints are one dyadic Hardy primitive and one finite jump filter

Claim ID: `L-105471`

Status: **PROVED EXACT DYADIC FACTORIZATION**

Retain the finite real coefficient sequence \((a_n)\) and current \(H\) of
`L-105470`.  Define right-continuous cumulative functions

\[
P(x)=\sum_{n\le x}a_n,
\qquad
Q(x)=\sum_{n\le x}{a_n\over\sqrt n},
\tag{L-105471.1}
\]

and the Hardy primitive

\[
\boxed{W(x)=2P(x)-\sqrt x\,Q(x).}
\tag{L-105471.2}
\]

Let the dyadic pullback be

\[
(Sf)(x)=f(x/2),
\]

and set

\[
\boxed{
\Delta_2=(I-S)^2(I-\sqrt2S)
=I-(2+\sqrt2)S+(1+2\sqrt2)S^2-\sqrt2S^3.
}
\tag{L-105471.3}
\]

## 1. Exact right-endpoint identity

Expanding the three ranges in `L-105470.3` gives

\[
A_m=8\Delta_2P(m).
\tag{L-105471.4}
\]

If \(R(x)=\sqrt xQ(x)\), the square-root part satisfies

\[
B_m\sqrt m=-4\Delta_2R(m).
\tag{L-105471.5}
\]

Consequently

\[
\boxed{
H(m+)=4\Delta_2W(m).
}
\tag{L-105471.6}
\]

Equivalently, for the one-sided Hardy atom

\[
\phi(y)=(2-\sqrt y)\mathbf1_{y\ge1},
\]

one has the coefficientwise identity

\[
K_L(y)=4(I-S_y)^2(I-\sqrt2S_y)\phi(y),
\tag{L-105471.7}
\]

where \((S_yf)(y)=f(y/2)\).  The apparently unbounded tails of the four
\(\phi\)-terms cancel exactly.

## 2. Exact endpoint jump

Extend the arithmetic sequence by zero off the positive integers and define

\[
\boxed{
E(m)=a_m-(2+\sqrt2)\mathbf1_{2\mid m}a_{m/2}
 +(1+2\sqrt2)\mathbf1_{4\mid m}a_{m/4}
 -\sqrt2\mathbf1_{8\mid m}a_{m/8}.
}
\tag{L-105471.8}
\]

The jumps of `K_L` at \(1,2,4,8\) are respectively

\[
4,
\quad-4(2+\sqrt2),
\quad4(1+2\sqrt2),
\quad-4\sqrt2.
\]

Therefore

\[
\boxed{H(m+)-H(m-)=4E(m).}
\tag{L-105471.9}
\]

Combining (L-105471.6) and (L-105471.9),

\[
\boxed{
H((m+1)-)
=4\bigl(\Delta_2W(m+1)-E(m+1)\bigr).
}
\tag{L-105471.10}
\]

## 3. Continuous variation versus one discrete sequence

For an integer \(M\ge1\), put

\[
\begin{aligned}
V_M(H)
 &=\int_M^{2M}|H(X)|{dX\over X},\\
G_M(W)
 &=\sum_{m=M}^{2M-1}w_m
 \bigl(|\Delta_2W(m)|+|\Delta_2W(m+1)|\bigr),\\
J_M(a)
 &=\sum_{m=M}^{2M-1}w_m|E(m+1)|,
\end{aligned}
\tag{L-105471.11}
\]

where \(w_m=\sqrt{1+1/m}-1\).  Substitution of
(L-105471.6) and (L-105471.10) into `L-105470.10` yields

\[
\boxed{
\sqrt2\bigl(G_M(W)-J_M(a)\bigr)
\le V_M(H)
\le4\bigl(G_M(W)+J_M(a)\bigr).
}
\tag{L-105471.12}
\]

The lower bound is understood literally; it remains valid when its displayed
right side is negative.

By `L-105470.11`,

\[
G_M(W)\asymp
\sum_{m=M}^{2M}{|\Delta_2W(m)|\over m},
\tag{L-105471.13}
\]

with absolute constants, including both boundary terms.

Thus all continuous kernel geometry has been removed.  Apart from the finite
jump ledger \(J_M(a)\), the derivative-outer logarithmic L1 norm is one
weighted `l1` norm of the scalar sequence \(\Delta_2W(m)\).
