# L-24508 — Signed divisor-gradient certificates suffice

Claim ID: `L-24508`  
Status: `PROPOSED COMPLETE — exact finite algebra`  
Scope: correction of the proof boundary in `T-24501`  
Issue: #245  
Depends on: `L-24501`

The nonnegativity condition

\[
b_m\ge0
\]

is not needed for the prime-ramp lower bound after the second-difference convexification.

## Theorem

Let `b_2,...,b_X` be arbitrary real numbers, put `b_(X+1)=0`, and define

\[
v_q(b)=\sum_{kq\le X}(b_{kq}-b_{kq+1}),
\]

\[
J_X(b)=\sum_{m=2}^Xb_m\log\frac m{m-1}.
\]

If

\[
v_q(b)\le w_X(q)=q^{-1/2}\log(X/q)
\qquad(q=p^a\le X),
\tag{L-24508.1}
\]

then

\[
\boxed{
J_X(b)\le
S_X:=\sum_{q=p^a\le X}\frac{\Lambda(q)}{\sqrt q}\log\frac Xq.}
\tag{L-24508.2}
\]

No sign hypothesis on `b` occurs.

## Proof

The exact von Mangoldt dual identity of `L-24501` is valid for every real vector `b`:

\[
J_X(b)=\sum_{q=p^a\le X}\Lambda(q)v_q(b).
\]

Since `Lambda(q)>=0`, multiplying (L-24508.1) by `Lambda(q)` and summing gives (L-24508.2).

## Adjacent-flow version

Let

\[
b_F(m)=b_X^{(0)}(m)+F_{m-1}-F_m,
\qquad F_1=F_X=0.
\]

If the corrected vector satisfies (L-24508.1) and

\[
\sum_{j=2}^{X-1}F_j\log\frac{j^2}{j^2-1}
\le X^{o(1)},
\tag{L-24508.3}
\]

then, by the exact objective identity,

\[
S_X\ge J_X(b_F)
\ge4\sqrt X-X^{o(1)}.
\]

For the stronger target used in `T-24501`, it is enough to prove an `O(log^2 X)` upper bound in (L-24508.3).

The flow coordinates may therefore be chosen solely to control the prime-power constraints and the weighted cost. They need not preserve `b_F(m)>=0`.

## Meaning for the carry interpretation

If one wants to return from `b` to an explicitly nonnegative combination of average binomial rows, positivity remains relevant. It is **not** relevant to the direct prime-ramp consumer, because the latter uses only the exact identity

\[
J_X(b)=\sum_q\Lambda(q)v_q(b).
\]

The full RH proposal should use the weaker signed certificate unless a positive-row decomposition is desired as an additional result.

## Corrected PNC obligations

The load-bearing correction theorem now needs only:

1. `v_q(b_F)<=w_X(q)` for every prime power;
2. no positive residual on coordinates outside the active correction set;
3. `O(log^2 X)` exact objective cost.

The former requirement that every corrected `b_m` remain nonnegative is withdrawn from the RH deduction.

## Review boundary

This lemma does not construct the correction. It removes one unnecessary hypothesis from the remaining theorem and follows immediately from exact finite algebra.
