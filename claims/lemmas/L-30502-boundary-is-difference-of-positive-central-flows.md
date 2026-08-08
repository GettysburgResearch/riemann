# L-30502 — Each stopped cutoff boundary is a difference of positive central flows

Claim ID: `L-30502`  
Title: Before source inversion, every individual stopped-power cutoff boundary is exactly the carry image of a finite/infinite positive-flow difference; active-layer truncation must be retained in aggregation  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen context: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Dependencies: PR #280 central residual identity; PR #301 `L-29801`  
Scope: exact per-layer flow identity and aggregation firewall; no quantitative Cycle-Debt estimate

## 1. Central first-difference flow

For a nonnegative decreasing sequence `r`, put

\[
a_r(n)=r(n)-r(n+1)\ge0.
\]

Let `D(r)` assign coefficient `a_r(n)` to the central split

\[
[n,\lfloor n/2\rfloor].
\]

The exact residual operator is

\[
\mathcal Tr(q)=r(q)-L_q(D(r)).
\tag{L-30502.1}
\]

## 2. One stopped layer

Fix a decreasing sequence `p` and an endpoint `Y`, and define

\[
p_Y(n)=p(n)\mathbf1_{n\le Y}.
\]

Both `D(p)` and `D(p_Y)` are coefficientwise nonnegative. For every output
column

\[
q\le\left\lfloor\frac{Y+1}{2}\right\rfloor,
\]

one has `p_Y(q)=p(q)`, and therefore

\[
\boxed{
\mathcal T_\infty p(q)-\mathcal T_Yp_Y(q)
=
L_q\bigl(D(p_Y)-D(p)\bigr).
}
\tag{L-30502.2}
\]

The exact row coefficients are

\[
\begin{aligned}
D(p_Y)-D(p)
={}&p(Y+1)[Y,\lfloor Y/2\rfloor]\\
&-\sum_{n>Y}[p(n)-p(n+1)]
[n,\lfloor n/2\rfloor].
\end{aligned}
\tag{L-30502.3}
\]

Thus each individual cutoff boundary is the carry image of a difference of two
positive central flows.

## 3. Active-layer aggregation

For the critical stopped-power resolution

\[
w_X(q)=
\sum_{Y=1}^{X-1}\ell_Yp_Y(q),
\qquad
\ell_Y=\log\frac{Y+1}{Y}>0,
\qquad
p(q)=q^{-1/2},
\]

column `q` receives a boundary from layer `Y` only when `Y>=2q-1`. Hence

\[
\boxed{
b_X(q)
=
\sum_{Y=2q-1}^{X-1}
\ell_Y
L_q\bigl(D(p_Y)-D(p)\bigr).
}
\tag{L-30502.4}
\]

This is equivalent to the scalar formula in `L-30501`.

The lower limit `2q-1` depends on the output column. Therefore one may **not**
drop the active-layer indicator and replace (L-30502.4) by the carry load of

\[
\sum_{Y=1}^{X-1}\ell_Y[D(p_Y)-D(p)].
\]

That source-independent sum has extra contributions from layers which have no
output coordinate at `q`.

## 4. Correct optimization interface

A repaired flow proof must retain an explicit layer or cutoff-state label until
the active destinations are assembled. Only then may it pass to the finite
Pascal-cycle normal form.

The proof-facing object is therefore the cycle-optimized negative capacity of
the **activated finite manifest**, not the isolated divisor-source norm and not
the unqualified sum of the per-layer flow differences.

This lemma proves the exact positive-flow origin of every layer, but it does not
construct a polylogarithmic activated-flow certificate.

## 5. Proof boundary

Closed exactly:

1. the per-layer finite/infinite boundary as a carry-load difference;
2. positivity of both constituent central flows;
3. the exact row support of their difference;
4. the active-layer condition `Y>=2q-1`;
5. the aggregation firewall preventing an invalid source-independent sum.

Open:

1. a subpower or polylogarithmic activated Pascal-cycle certificate;
2. the resulting sharp prime ramp;
3. RH.
