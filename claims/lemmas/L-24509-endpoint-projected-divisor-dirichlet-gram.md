# L-24509 — Endpoint-projected divisor coordinates form an exact Dirichlet Gram

Claim ID: `L-24509`  
Status: `PROPOSED COMPLETE — exact finite algebra`  
Scope: symmetric elementary correction geometry  
Issue: #245  
Depends on: `L-24501`, `L-24508`

Let

\[
\mathcal Q_X=\{p^a:p^a\le X\}.
\]

For `q in Q_X` and `0<=j<=X`, define

\[
u_q(j)=\mathbf 1_{q\mid j}
\quad(1\le j\le X),
\qquad u_q(0)=0,
\]

and its endpoint-projected version

\[
\boxed{
f_q(j)=u_q(j)-\frac jX u_q(X).}
\tag{L-24509.1}
\]

Then

\[
f_q(0)=f_q(X)=0.
\]

Define the matrix

\[
\boxed{
G_X(q,d)=
\sum_{j=0}^{X-1}
\bigl(f_q(j+1)-f_q(j)\bigr)
\bigl(f_d(j+1)-f_d(j)\bigr).}
\tag{L-24509.2}
\]

## 1. Positive definiteness

For a real coefficient vector `T=(T_d)`, put

\[
F_T(j)=\sum_{d\in\mathcal Q_X}T_d f_d(j).
\]

Then exactly

\[
\boxed{
T^T G_XT
=
\sum_{j=0}^{X-1}\bigl(F_T(j+1)-F_T(j)\bigr)^2.}
\tag{L-24509.3}
\]

If the right side is zero, `F_T` is constant and its zero endpoints force `F_T=0`. Put

\[
D_T(j)=\sum_{d\mid j,\ d\in\mathcal Q_X}T_d.
\]

The equation `F_T(j)=0` gives

\[
D_T(j)=\frac jX D_T(X).
\]

At `j=1`, this forces `D_T(X)=0`, hence `D_T(j)=0` for every `j`. Induction over the prime powers gives `T_d=0`: at `j=d`, all proper prime-power divisors have already been eliminated and the remaining term is `T_d`.

Therefore

\[
\boxed{G_X>0.}
\tag{L-24509.4}
\]

## 2. Exact signed correction

Let `F_T` be as above and define

\[
b_T(m)=b(m)+F_T(m-1)-F_T(m),
\qquad 2\le m\le X.
\tag{L-24509.5}
\]

Since the linear endpoint term in (L-24509.1) has zero second difference, finite summation by parts gives

\[
\boxed{
v_q(b_T)-v_q(b)=-(G_XT)_q.}
\tag{L-24509.6}
\]

Equivalently, the formerly nonsymmetric endpoint ledger becomes exactly the negative Dirichlet Gram after subtracting the linear endpoint trace.

No sign assumption on `T`, `F_T`, or `b_T` is used.

## 3. Exact objective coordinate

Let

\[
\lambda_q=\Lambda(q)
\qquad(q\in\mathcal Q_X).
\]

The associated physical profile is

\[
\begin{aligned}
h_X(j)
&=\sum_{q\in\mathcal Q_X}\Lambda(q)f_q(j)\\
&=\log j-\frac jX\log X
\qquad(1\le j\le X),
\end{aligned}
\tag{L-24509.7}
\]

with `h_X(0)=h_X(X)=0`. Hence

\[
\boxed{
\lambda^TG_X\lambda
=
\sum_{j=0}^{X-1}
\left(
 h_X(j+1)-h_X(j)
\right)^2.}
\tag{L-24509.8}
\]

The elementary estimates `log(1+1/j)<=1/j` and `(a-b)^2<=2a^2+2b^2` give, for every `X>=2`,

\[
\boxed{
\lambda^TG_X\lambda\le6.}
\tag{L-24509.9}
\]

Finally, the exact von Mangoldt identity implies

\[
\boxed{
J_X(b_T)-J_X(b)
=-\lambda^TG_XT.}
\tag{L-24509.10}
\]

Thus the objective cost is the Dirichlet inner product of the explicit logarithmic chord `h_X` with the correction potential `F_T`.

## 4. Residual Green norm

For the parabolic seed define

\[
r_X(q)=v_q(b_X^{(0)})-w_X(q),
\]

and

\[
\boxed{
\mathcal G_X=r_X^TG_X^{-1}r_X.}
\tag{L-24509.11}
\]

Cauchy–Schwarz in the `G_X` metric yields

\[
\boxed{
\left|
\sum_{q\in\mathcal Q_X}\Lambda(q)r_X(q)
\right|
\le\sqrt{6\mathcal G_X}.}
\tag{L-24509.12}
\]

But

\[
\sum_q\Lambda(q)r_X(q)
=J_X(b_X^{(0)})-S_X.
\tag{L-24509.13}
\]

Therefore

\[
\boxed{
S_X
\ge
J_X(b_X^{(0)})-\sqrt{6\mathcal G_X}.}
\tag{L-24509.14}
\]

This identity bypasses Jacobi convergence, preservation of coefficient signs, and the monotone cover.

## 5. Exact proof boundary

The matrix factorization and inequality (L-24509.14) are complete finite algebra. The arithmetic burden has moved to an explicit scalar Green energy `G_X`. A polylogarithmic or subpower upper bound for that energy is not proved in this file.
