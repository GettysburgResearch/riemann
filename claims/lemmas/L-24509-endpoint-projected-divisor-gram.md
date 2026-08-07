# L-24509 — Endpoint-projected divisor corrections form an exact Dirichlet Gram

Claim ID: `L-24509`  
Status: `PROPOSED — exact finite algebra`  
Scope: elementary signed correction geometry  
Issue: #245

Let

\[
\mathcal Q_X=\{p^a:p^a\le X\}.
\]

For `q in Q_X` define the finite Dirichlet incidence profile on
`0<=j<=X` by

\[
u_q(0)=0,
\qquad
u_q(j)=\mathbf 1_{q\mid j}\quad(1\le j\le X),
\]

and its endpoint projection

\[
\boxed{
f_q(j)=u_q(j)-\frac jX u_q(X).
}
\tag{L-24509.1}
\]

Then

\[
f_q(0)=f_q(X)=0.
\]

For a real coefficient vector `T=(T_d)_(d in Q_X)`, put

\[
F_T(j)=\sum_{d\in\mathcal Q_X}T_d f_d(j)
\qquad(0\le j\le X).
\tag{L-24509.2}
\]

No sign condition is imposed on `T` or on the resulting corrected `b`.

## 1. Exact correction matrix

Given any real vector `b=(b_m)_(2<=m<=X)`, define

\[
b_T(m)=b_m+F_T(m-1)-F_T(m).
\tag{L-24509.3}
\]

For every prime power `q<=X`, the divisor-gradient coordinate changes by

\[
\begin{aligned}
v_q(b_T)-v_q(b)
&=\sum_{j=1}^{X-1}F_T(j)
 \bigl(u_q(j+1)-2u_q(j)+u_q(j-1)\bigr).
\end{aligned}
\tag{L-24509.4}
\]

The linear endpoint term in `f_q` has zero second difference, so

\[
\Delta f_q(j)=\Delta u_q(j)
\qquad(1\le j\le X-1).
\]

Discrete Green summation, using `f_q(0)=f_q(X)=F_T(0)=F_T(X)=0`, gives

\[
\boxed{
v_q(b_T)-v_q(b)
=-\sum_{d\in\mathcal Q_X}G_X(q,d)T_d,
}
\tag{L-24509.5}
\]

where

\[
\boxed{
G_X(q,d)
=\sum_{j=0}^{X-1}
 \bigl(f_q(j+1)-f_q(j)\bigr)
 \bigl(f_d(j+1)-f_d(j)\bigr).
}
\tag{L-24509.6}
\]

Thus the complete signed correction matrix is exactly `-G_X`.

## 2. Positive definiteness

The matrix `G_X` is a real symmetric Gram matrix. It is in fact positive
definite.

Suppose

\[
F_T(j)=\sum_dT_df_d(j)=0
\qquad(0\le j\le X).
\]

Write

\[
D_T(j)=\sum_{\substack{d\in\mathcal Q_X\\d\mid j}}T_d.
\]

At `j=1`, since no prime power divides `1`, the identity `F_T(1)=0`
gives

\[
D_T(X)=0.
\]

Consequently `F_T(j)=0` gives `D_T(j)=0` for every `1<=j<=X`.
Now order the prime powers increasingly. For a prime power `d`,

\[
0=D_T(d)=T_d+\sum_{\substack{e\in\mathcal Q_X\\e\mid d,\ e<d}}T_e.
\]

Induction on `d` gives `T_d=0` for every prime power. Hence

\[
\boxed{G_X\succ0.}
\tag{L-24509.7}
\]

The endpoint projection removes exactly the boundary obstruction that made the
unprojected finite correction matrix only approximately symmetric.

## 3. Exact objective metric

Let

\[
\lambda_q=\Lambda(q).
\]

The von Mangoldt divisor identity gives, for `1<=j<=X`,

\[
\sum_{q\in\mathcal Q_X}\lambda_q u_q(j)=\log j.
\]

Therefore the physical profile of `lambda` in the projected frame is

\[
\boxed{
h_X(j)=\sum_q\lambda_qf_q(j)
=\log j-\frac jX\log X
\quad(1\le j\le X),
}
\tag{L-24509.8}
\]

with `h_X(0)=0` and `h_X(X)=0`.

Using `J_X(b)=sum_q Lambda(q)v_q(b)`, equation (L-24509.5) gives

\[
\boxed{
J_X(b)-J_X(b_T)
=\lambda^{\!T}G_XT
=\sum_{j=0}^{X-1}\nabla h_X(j)\,\nabla F_T(j).
}
\tag{L-24509.9}
\]

Thus the exact correction cost is the Dirichlet pairing with one explicit
logarithmic arch.

Moreover,

\[
\lambda^{\!T}G_X\lambda
=\sum_{j=0}^{X-1}|h_X(j+1)-h_X(j)|^2
\ll1.
\tag{L-24509.10}
\]

For example, `log(1+1/j)<=1/j` gives the explicit elementary bound

\[
\lambda^{\!T}G_X\lambda
\le \frac{\pi^2}{3}+3
\qquad(X\ge2).
\tag{L-24509.11}
\]

## 4. Consequence for the old primitive-neighbor ledger

The determinant-one and favorable-gcd entries of `L-24503` are coordinate
entries of the same correction operator before endpoint projection. Equation
(L-24509.6) shows that, after the exact linear boundary repair, all of those
entries assemble into one positive Dirichlet energy rather than an arbitrary
nonsymmetric Jacobi matrix.

This does not by itself bound the correction cost: the RH-bearing scalar can
still lie in the low-energy logarithmic direction `lambda`. It does remove the
claimed need to prove convergence of the particular Jacobi iteration in
`T-24501`.

## Review boundary

This lemma is finite algebra. It proves symmetry, positive definiteness, and the
exact objective pairing. It does not prove that the parabolic residual has
polylogarithmic Green energy and does not prove RH.
