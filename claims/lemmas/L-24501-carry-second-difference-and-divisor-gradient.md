# L-24501 — Carry second differences and the divisor-gradient LP

Claim ID: `L-24501`  
Status: `PROPOSED — exact finite algebra`  
Scope: elementary finite reduction  
Issue: #245

## 1. Discrete convexity of the average binomial row

Let

\[
G_n=\frac1{n+1}\sum_{j=0}^n\log\binom nj,
\qquad
F_n=(n+1)G_n.
\]

Then

\[
F_n-F_{n-1}=(n-1)\log n-\log((n-1)!),
\]

and therefore

\[
\boxed{F_n-2F_{n-1}+F_{n-2}=(n-1)\log\frac n{n-1}>0.}
\tag{L-24501.1}
\]

This identity is exact for every integer `n>=2`.

## 2. Second difference of the carry kernel

For integers `2<=q<=n`, define

\[
\beta_{nq}=\frac{\lfloor n/q\rfloor\bigl(q-1-(n\bmod q)\bigr)}{n+1},
\]

and put

\[
g_q(n)=(n+1)\beta_{nq}.
\]

Then for every `m>=2`,

\[
\boxed{
g_q(m)-2g_q(m-1)+g_q(m-2)
=(m-1)(\mathbf 1_{q\mid m}-\mathbf 1_{q\mid m-1}).}
\tag{L-24501.2}
\]

Thus two discrete differences turn the floor-valued carry matrix into a signed divisibility gradient.

## 3. Double summation by parts

Let `c_n` be any finite coefficient vector supported on `2<=n<=X`. Put

\[
a_n=\frac{c_n}{n+1},
\qquad
A_m=\sum_{n=m}^X(n-m+1)a_n,
\qquad
b_m=(m-1)A_m.
\]

Then exact finite summation by parts using (L-24501.1) and (L-24501.2) gives

\[
\boxed{\sum_{n=2}^X c_n\beta_{nq}
=\sum_{m=2}^X b_m(\mathbf 1_{q\mid m}-\mathbf 1_{q\mid m-1}).}
\tag{L-24501.3}
\]

and

\[
\boxed{\sum_{n=2}^X c_nG_n
=\sum_{m=2}^X b_m\log\frac m{m-1}.}
\tag{L-24501.4}
\]

Equivalently, with `b_{X+1}=0`,

\[
\boxed{v_q(b):=\sum_{m=2}^Xb_m(\mathbf 1_{q\mid m}-\mathbf 1_{q\mid m-1})
=\sum_{kq\le X}(b_{kq}-b_{kq+1}).}
\tag{L-24501.5}
\]

## 4. Prime-power LP and exact von Mangoldt dual

Let

\[
\mathcal Q_X=\{p^a:p^a\le X\},
\qquad
w_X(q)=q^{-1/2}\log(X/q),
\]

and

\[
J_X(b)=\sum_{m=2}^Xb_m\log\frac m{m-1}.
\]

Consider

\[
\begin{aligned}
\text{maximize }&J_X(b),\\
\text{subject to }&b_m\ge0,\\
&v_q(b)\le w_X(q)\quad(q\in\mathcal Q_X).
\end{aligned}
\tag{P_X}
\]

Only prime powers are constrained because Legendre's formula for the binomial row contains only prime powers.

For every `b`,

\[
\begin{aligned}
\sum_{q\in\mathcal Q_X}\Lambda(q)v_q(b)
&=\sum_{m=2}^X b_m\left(\sum_{q\mid m}\Lambda(q)-\sum_{q\mid m-1}\Lambda(q)\right)\\
&=\sum_{m=2}^Xb_m\log\frac m{m-1}\\
&=J_X(b),
\end{aligned}
\]

since `sum_{q|n,q=p^a} Lambda(q)=log n`. Hence

\[
\boxed{J_X(b)=\sum_{q\in\mathcal Q_X}\Lambda(q)v_q(b).}
\tag{L-24501.6}
\]

Therefore every feasible `b` satisfies

\[
\boxed{
\sum_{q\in\mathcal Q_X}\frac{\Lambda(q)}{\sqrt q}\log\frac Xq\ge J_X(b).
}
\tag{L-24501.7}
\]

The dual choice `y_q=Lambda(q)` saturates every dual constraint exactly.

## 5. Exact primal optimum

For each prime power `p^a<=X`, put

\[
\delta_{p^a}=w_X(p^a)-w_X(p^{a+1}),
\]

with the convention `w_X(p^{a+1})=0` after the last power below `X`, and put `delta_n=0` otherwise. Define

\[
b_m=\sum_{n=m}^X\delta_n.
\]

Then `b_m>=0` and the prime-power chains telescope to

\[
v_{p^a}(b)=w_X(p^a).
\]

Thus

\[
\boxed{\max(P_X)=\sum_{q\in\mathcal Q_X}\frac{\Lambda(q)}{\sqrt q}\log\frac Xq.}
\tag{L-24501.8}
\]

The optimizer is arithmetic/tautological, but it proves that the convexified carry LP is exactly the prime ramp rather than merely a relaxation.

## Review boundary

This file contains only finite identities and LP duality. It does not prove a non-arithmetic near-optimal feasible vector and does not prove RH.
