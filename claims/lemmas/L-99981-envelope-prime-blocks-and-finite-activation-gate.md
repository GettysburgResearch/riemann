# L-99981 — One- and two-prime envelope positivity and the finite activation gate

Claim ID: `L-99981`  
Status: **PROVED EXACT LOCAL/REGIME THEOREM; ALL-PRIME ACTIVATION GATE OPEN**  
Created: 2026-08-20  
Depends on: `L-99980`  
RH status: **unproved**

Normalize the kernel in `L-99980` by

\[
f(y)=\frac{R(y)}y=
\begin{cases}
16,&0<y<1,\\
24y^{-1/2}-9y^{-1},&y\ge1.
\end{cases}
\tag{L-99981.1}
\]

Then

\[
\frac{\mathcal E_2(X)}X
=
\sum_{n\ge1}\frac{\beta(n)}{n^{3/2}}f(X/n).
\tag{L-99981.2}
\]

Represent \(\beta\) by one labelled copy of every prime and a second labelled
copy of \(67\). A label \(q\) has activity \(r_q=q^{-3/2}\).

## 1. Conjugation to ordinary differences

In logarithmic coordinate \(u=\log y\), put

\[
F(u)=e^{3u/2}f(e^u).
\]

Then

\[
F(u)=
\begin{cases}
16e^{3u/2},&u<0,\\
24e^u-9e^{u/2},&u\ge0.
\end{cases}
\tag{L-99981.3}
\]

For \(a=\log q\),

\[
\boxed{
e^{3u/2}(I-q^{-3/2}\tau_a)f(e^u)
=(I-\tau_a)F(u).
}
\tag{L-99981.4}
\]

Thus the entire arithmetic problem is an ordinary finite-difference problem
for one explicit piecewise exponential function. Its sole nonsmooth datum is
the downward unit jump \(F(0^-)-F(0^+)=1\).

## 2. One-prime positivity

For every real \(q\ge2\),

\[
\boxed{
f(y)-q^{-3/2}f(y/q)>0
\qquad(y>0).
}
\tag{L-99981.5}
\]

There are three regimes.

- \(y<1\): the value is \(16(1-q^{-3/2})\).
- \(1\le y<q\): the minimum is at \(y=q^-\), and after multiplying by
  \(q^{3/2}\) it is at least \(24q-9\sqrt q-16>0\).
- \(y\ge q\): the value is
  \[
  24(1-q^{-1})y^{-1/2}
  -9(1-q^{-1/2})y^{-1}>0.
  \]

## 3. Two-prime positivity

For every pair of labels \(2\le p\le q\), including the repeated pair
\(p=q=67\),

\[
\boxed{
(I-p^{-3/2}U_p)(I-q^{-3/2}U_q)f(y)>0
\qquad(y>0).
}
\tag{L-99981.6}
\]

The breakpoints are \(1,p,q,pq\). In the five resulting regimes direct
substitution reduces positivity to:

\[
24p-9\sqrt p>32,
\]

\[
24q(1-p^{-1})-9\sqrt q(1-p^{-1/2})
>16(1-p^{-3/2}),
\]

\[
24(pq-p-q)\sqrt z
-9(\sqrt{pq}-\sqrt p-\sqrt q)+16z>0
\quad(1/p\le z<1),
\]

and, in the fully active region,

\[
24\sqrt y(1-p^{-1})(1-q^{-1})
>
9(1-p^{-1/2})(1-q^{-1/2}).
\]

The smallest cases \(p=2,q=3\) satisfy the displayed strict inequalities;
the left sides increase thereafter. This proves the theorem without a scan.

## 4. Arbitrary fully coactive blocks

For labels \(q_1,\ldots,q_k\), put \(Q=\prod q_i\). If \(y\ge Q\), then

\[
\boxed{
\prod_i(I-q_i^{-3/2}U_{q_i})f(y)
=
24y^{-1/2}\prod_i(1-q_i^{-1})
-
9y^{-1}\prod_i(1-q_i^{-1/2})>0.
}
\tag{L-99981.7}
\]

The ratio of the second term to the first is at most

\[
\frac38y^{-1/2}
\prod_i\frac{\sqrt{q_i}}{\sqrt{q_i}+1}
<
\frac3{8\sqrt Q}<1.
\]

Thus every uniform regime and every active pair is closed exactly.

## 5. Exact finite activation gate

For fixed \(y\), split the labels into

\[
A_y=\{q:q\le y\},
\qquad
I_y=\{q:q>y\},
\]

including the second \(67\) label in the appropriate set, and write

\[
\Delta_A=\prod_{q\in A_y}(1-q^{-3/2}),
\qquad
\Delta_I=\prod_{q\in I_y}(1-q^{-3/2}).
\]

Every nonempty subset of \(I_y\) sends every shifted argument below one, where
\(f=16\). Consequently

\[
\boxed{
\prod_{q\in A_y\cup I_y}(I-q^{-3/2}U_q)f(y)
=
\prod_{q\in A_y}(I-q^{-3/2}U_q)f(y)
-
16(1-\Delta_I)\Delta_A.
}
\tag{L-99981.8}
\]

Therefore the full quadratic-envelope theorem is equivalent to the finite
activation inequality

\[
\boxed{
\prod_{q\in A_y}(I-q^{-3/2}U_q)f(y)
\ge16(1-\Delta_I)\Delta_A
\qquad(y\ge1).
}
\tag{FEAG99980}
\]

All one-prime, two-prime, inactive-tail, and fully coactive pieces of this
inequality are proved above. The remaining mixed-activation composition is
open and conclusion-bearing.
