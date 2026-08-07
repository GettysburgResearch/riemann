# L-24502 — Parabolic seed and exact correction calculus

Claim ID: `L-24502`  
Status: `PROPOSED — exact finite/algebraic identities plus elementary inequalities`  
Scope: elementary carry minorant construction  
Issue: #245

## 1. Explicit parabolic seed

For `2<=m<=X`, define

\[
\boxed{
b_X^{(0)}(m)=2\sqrt m\left[\log\frac Xm-2\left(1-\sqrt{\frac mX}\right)\right].}
\tag{L-24502.1}
\]

With `r=sqrt(m/X)`, the bracket is `-2 log r-2(1-r)>=0`, so

\[
b_X^{(0)}(m)\ge0.
\]

Define

\[
f_X(x)=\frac{b_X^{(0)}(x)}x
=2x^{-1/2}\log\frac Xx-4x^{-1/2}+4X^{-1/2}.
\]

Then

\[
\boxed{f_X'(x)=-x^{-3/2}\log\frac Xx\le0.}
\tag{L-24502.2}
\]

## 2. Sharp objective mass

Since `log(m/(m-1))>=1/m`,

\[
J_X(b_X^{(0)})\ge\sum_{m=2}^X f_X(m).
\]

Using monotonicity from (L-24502.2) and elementary integral comparison gives

\[
\boxed{J_X(b_X^{(0)})\ge4\sqrt X-6\log X+4-8X^{-1/2}.}
\tag{L-24502.3}
\]

In particular the entire critical `4 sqrt(X)` main term is present before any arithmetic repair.

## 3. Adjacent-flow correction

Let `F_1=F_X=0` and define

\[
b_F(m)=b_X^{(0)}(m)+F_{m-1}-F_m.
\tag{L-24502.4}
\]

Then for every integer `q>=2`,

\[
\boxed{
v_q(b_F)-v_q(b_X^{(0)})
=\sum_{j=2}^{X-1}F_j\left(\mathbf1_{q\mid j+1}-2\mathbf1_{q\mid j}+\mathbf1_{q\mid j-1}\right).}
\tag{L-24502.5}
\]

The objective change telescopes exactly:

\[
\boxed{
J_X(b_X^{(0)})-J_X(b_F)
=\sum_{j=2}^{X-1}F_j\log\frac{j^2}{j^2-1}.}
\tag{L-24502.6}
\]

Since

\[
\log\frac{j^2}{j^2-1}=j^{-2}+O(j^{-4}),
\]

transport far to the right is asymptotically cheap in the objective metric.

## 4. Monotone tail-cover correction

Choose `alpha_m>=0`, put

\[
B_m=\sum_{t=m}^X\alpha_t,
\qquad
\widetilde b_m=b_X^{(0)}(m)-B_m.
\tag{L-24502.7}
\]

Then

\[
\boxed{
v_q(\widetilde b)=v_q(b_X^{(0)})-\sum_{kq\le X}\alpha_{kq}.}
\tag{L-24502.8}
\]

and

\[
\boxed{
J_X(b_X^{(0)})-J_X(\widetilde b)=\sum_{m=2}^X\alpha_m\log m.}
\tag{L-24502.9}
\]

Thus it is sufficient to cover the positive constraint excess

\[
e_X(q)=\bigl(v_q(b_X^{(0)})-w_X(q)\bigr)_+
\]

by nonnegative divisibility atoms `alpha_m` while keeping the tail below the seed and the weighted cost polylogarithmic.

## 5. Divisibility Cover Theorem (sufficient closure)

A sufficient theorem is the existence, for every sufficiently large `X`, of `alpha_m>=0` satisfying

\[
\sum_{kq\le X}\alpha_{kq}\ge e_X(q)
\quad(q=p^a\le X),
\tag{D1}
\]

\[
\sum_{t=m}^X\alpha_t\le b_X^{(0)}(m)
\quad(2\le m\le X),
\tag{D2}
\]

and

\[
\sum_{m=2}^X\alpha_m\log m=O(\log^2X).
\tag{D3}
\]

Then `tilde b` is feasible for the prime-power divisor-gradient LP and

\[
J_X(\widetilde b)\ge4\sqrt X-O(\log^2X).
\]

This theorem is not proved here; it is a clean monotone sufficient closure.

## Status boundary

The parabolic seed, its objective lower bound, and both correction identities are proposed complete elementary mathematics. The all-scale cover theorem remains open in this file.
