# L-30502 — The cutoff boundary is the carry image of a difference of positive central flows

Claim ID: `L-30502`  
Title: Before taking any source norm, every stopped-power cutoff boundary is exactly the difference of its finite and infinite nonnegative central first-difference flows  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen context: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Dependencies: PR #280 central residual identity; PR #301 `L-29801`  
Scope: exact finite flow identity; no quantitative Cycle-Debt estimate

## 1. Central first-difference flow

For a nonnegative decreasing sequence

\[
r(2)\ge r(3)\ge\cdots\ge0,
\qquad r(n)=0\text{ eventually},
\]

put

\[
a_r(n)=r(n)-r(n+1)\ge0.
\tag{L-30502.1}
\]

Let `D(r)` be the central split flow assigning coefficient `a_r(n)` to

\[
[n,\lfloor n/2\rfloor].
\]

Write `L_q(D(r))` for its carry load. The exact residual operator of PR #280 is

\[
\mathcal T r(q)=r(q)-L_q(D(r)).
\tag{L-30502.2}
\]

No asymptotic estimate enters this identity.

## 2. Finite and infinite stopped powers

Fix a decreasing sequence `p(n)` and an endpoint `Y`. Define

\[
p_Y(n)=p(n)\mathbf1_{n\le Y}.
\tag{L-30502.3}
\]

Both `p` and `p_Y` are decreasing, and therefore both flows

\[
D(p),\qquad D(p_Y)
\]

are coefficientwise nonnegative.

Let

\[
\mathcal T_\infty p(q)=p(q)-L_q(D(p))
\]

and

\[
\mathcal T_Yp_Y(q)=p_Y(q)-L_q(D(p_Y)).
\]

For every `q<=Y`, one has `p_Y(q)=p(q)`, so subtraction gives

\[
\boxed{
\mathcal T_\infty p(q)-\mathcal T_Yp_Y(q)
=
L_q\bigl(D(p_Y)-D(p)\bigr).
}
\tag{L-30502.4}
\]

Thus the cutoff boundary is already the carry image of one explicit signed
balanced flow obtained as the difference of two nonnegative central flows.

## 3. Exact coefficient support

The coefficients of this difference are

\[
\begin{aligned}
D(p_Y)-D(p)
={}&p(Y+1)[Y,\lfloor Y/2\rfloor]\\
&-\sum_{n>Y}[p(n)-p(n+1)]
[n,\lfloor n/2\rfloor].
\end{aligned}
\tag{L-30502.5}
\]

Indeed, the first differences agree below `Y`; at row `Y`, stopping replaces
`p(Y)-p(Y+1)` by `p(Y)`; and every row above `Y` is deleted.

Equation (L-30502.5) exposes the exact cancellation suppressed by converting the
boundary first into an isolated divisor source.

## 4. Aggregate logarithmic target

For the critical stopped-power resolution of PR #301,

\[
w_X(q)
=
\sum_{Y=1}^{X-1}\ell_Yp_Y(q),
\qquad
\ell_Y=\log\frac{Y+1}{Y}>0,
\qquad
p(q)=q^{-1/2},
\tag{L-30502.6}
\]

sum (L-30502.4) with weights `ell_Y`. On the declared next endpoint,

\[
\boxed{
b_X(q)=L_q(B_X),}
\tag{L-30502.7}
\]

where

\[
\boxed{
B_X=
\sum_{Y=1}^{X-1}\ell_Y
\bigl[D(p_Y)-D(p)\bigr].
}
\tag{L-30502.8}
\]

The scalar `b_X` is exactly the first aggregate boundary of `L-30501`.
Consequently the large divisor-source norm in `L-30501` is the image norm of a
flow difference whose two constituents are positive.

## 5. Correct optimization interface

Let `C_eta` denote the balanced Pascal-cycle matrix of PR #272. Since adding a
cycle does not change any carry load, every flow representing the aggregate
boundary has the form

\[
B_X+C_\eta z.
\]

The proof-facing boundary cost is therefore

\[
\boxed{
\inf_z\mathcal N_\omega(B_X+C_\eta z),
}
\tag{L-30502.9}

not the triangle estimate

\[
\mathcal N_\omega(\Phi(\sigma_X))
\le24\|\sigma_X\|_{\rm at}.
\]

The identity does not prove that (L-30502.9) is polylogarithmic. It proves that
the large source norm does not itself lower-bound the optimized debt, and it
provides the exact flow object that a repaired theorem must estimate.

## 6. Proof boundary

Closed exactly:

1. the finite/infinite cutoff boundary as a carry-load difference;
2. positivity of both constituent central flows;
3. the exact row coefficients of their difference;
4. aggregation over the positive logarithmic endpoint layer cake;
5. the correct Pascal-cycle optimization interface.

Open:

1. a subpower or polylogarithmic bound for the optimized debt in
   (L-30502.9);
2. the resulting sharp prime ramp;
3. RH.
