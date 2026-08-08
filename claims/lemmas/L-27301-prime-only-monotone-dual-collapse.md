# L-27301 — Ordinary-prime monotone duals collapse to the endpoint

Claim ID: `L-27301`  
Title: Every nonnegative strongly additive potential that is nondecreasing through \(X\ge8\) vanishes below the endpoint  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #273  
Depends on: PR #248 `L-24517/L-24520`; PR #271 finite boundary-charge duality  
Scope: finite ordinary-prime carry cone; no RH conclusion

## 1. Ordinary-prime carry matrix

Let \(\mathcal P_X\) be the primes through \(X\), and define

\[
 V_X^{\mathbb P}(p,m)
 =
 \mathbf1_{p\mid m}
 -
 \mathbf1_{p\mid m-1},
 \qquad
 p\in\mathcal P_X,\quad2\le m\le X.
\tag{L-27301.1}
\]

For \(y_p\ge0\), put

\[
\boxed{
 Y_y(n)=\sum_{\substack{p\le X\\p\mid n}}y_p,
 \qquad Y_y(1)=0.
}
\tag{L-27301.2}
\]

Then exactly

\[
\boxed{
 ((V_X^{\mathbb P})^*y)_m
 =
 Y_y(m)-Y_y(m-1).
}
\tag{L-27301.3}
\]

Thus the dual condition

\[
 (V_X^{\mathbb P})^*y\ge0
\]

is precisely monotonicity of the strongly additive function \(Y_y\) on
\(\{1,\ldots,X\}\).

## 2. Collapse theorem

Assume \(X\ge8\), \(y_p\ge0\), and

\[
0=Y_y(1)\le Y_y(2)\le\cdots\le Y_y(X).
\tag{L-27301.4}
\]

Then

\[
Y_y(2)=y_2,\qquad
Y_y(3)=y_3,\qquad
Y_y(4)=y_2.
\]

Monotonicity gives

\[
y_2\le y_3\le y_2,
\]

so

\[
y_2=y_3.
\tag{L-27301.5}
\]

Next,

\[
Y_y(6)=y_2+y_3=2y_2,
\qquad
Y_y(8)=y_2.
\]

Since \(6<8\),

\[
2y_2\le y_2.
\]

Nonnegativity yields

\[
\boxed{y_2=y_3=0.}
\tag{L-27301.6}
\]

Let

\[
 L=2^{\lfloor\log_2X\rfloor}.
\]

Then

\[
\frac X2<L\le X.
\tag{L-27301.7}
\]

Because \(y_2=0\),

\[
Y_y(L)=0.
\]

The function is nonnegative and nondecreasing from \(Y_y(1)=0\), so

\[
\boxed{Y_y(n)=0\qquad(1\le n\le L).}
\tag{L-27301.8}
\]

In particular,

\[
y_p=0
\qquad(p\le L).
\tag{L-27301.9}
\]

Now let \(p\) be prime with \(L<p<X\).  The integer \(p+1\le X\) is even
and composite.  Every prime divisor \(r\mid p+1\) satisfies

\[
r\le\frac{p+1}{2}\le\frac X2<L,
\]

so (L-27301.9) gives \(Y_y(p+1)=0\).  Monotonicity then gives

\[
0\le y_p=Y_y(p)\le Y_y(p+1)=0.
\]

Therefore

\[
\boxed{
y_p=0\qquad\text{for every prime }p<X.
}
\tag{L-27301.10}
\]

If \(X\) is composite, all its prime factors are below \(X\), and
\(Y_y(X)=0\). If \(X\) is prime, only \(y_X\) may be nonzero.

The threshold \(X\ge8\) is sharp for this proof statement: through \(X=7\),

\[
(y_2,y_3,y_5,y_7)=(1,1,1,2)
\]

gives the nonzero monotone sequence

\[
0,1,1,1,1,2,2.
\]

## 3. Prime-only boundary charge

Let \(a=(a_2,\ldots,a_X)\) be any nonnegative benchmark and let
\(r_p=v_p(a)-w_X(p)\). Define the least ordinary-prime affine charge

\[
C_X^{\mathbb P}(a)
=
\inf\left\{
 C\ge0:
 \begin{array}{l}
 \text{there exists }b_m\ge a_m-C,\\
 v_p(b)\le w_X(p)\quad(p\le X)
 \end{array}
\right\}.
\tag{L-27301.11}
\]

Finite LP duality gives

\[
\boxed{
C_X^{\mathbb P}(a)
=
\max_y\sum_{p\le X}y_pr_p,
}
\tag{L-27301.12}
\]

where

\[
y_p\ge0,\qquad
Y_y(1)\le\cdots\le Y_y(X),\qquad
Y_y(X)\le1.
\tag{L-27301.13}
\]

For the parabolic benchmark \(a=b_X^{(0)}\), the endpoint row satisfies

\[
v_X(b_X^{(0)})=b_X^{(0)}(X)=0,
\qquad
w_X(X)=0.
\tag{L-27301.14}
\]

By the collapse theorem, every dual objective is zero. Hence

\[
\boxed{
C_X^{\mathbb P}(b_X^{(0)})=0
\qquad(X\ge8).
}
\tag{L-27301.15}
\]

Equivalently, for every \(X\ge8\) there exists \(h_m\ge0\) such that

\[
\boxed{
v_p(b_X^{(0)}+h)
\le
\frac1{\sqrt p}\log\frac Xp
\qquad(p\le X).
}
\tag{L-27301.16}
\]

This is an exact existence theorem. It uses no prime asymptotic, no RH input,
and no floating optimization.

## 4. Why this does not yet prove RH

The ordinary-prime objective is

\[
J_{\mathbb P,X}(b)
=
\sum_{p\le X}(\log p)v_p(b).
\]

Unlike the complete prime-power objective,

\[
J_X(b)
=
\sum_{m=2}^Xb_m\log\frac m{m-1},
\]

its physical coordinate weights are not all nonnegative. Therefore

\[
h_m\ge0
\]

does not imply

\[
J_{\mathbb P,X}(b_X^{(0)}+h)
\ge
J_{\mathbb P,X}(b_X^{(0)}).
\]

The missing requirement is control of the proper-prime-power response of the
repair. It is isolated in `L-27302`.

## 5. Proof boundary

```text
ordinary-prime dual cone collapse        PROPOSED COMPLETE
ordinary-prime positive feasibility      PROPOSED COMPLETE
sharp ordinary-prime objective           NOT IMPLIED
proper-power-neutral lift                OPEN
RH                                       UNPROVED
```
