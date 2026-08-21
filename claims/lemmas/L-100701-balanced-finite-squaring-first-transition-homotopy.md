# L-100701 — Finite Euler squaring admits an exact inverse-free first-transition homotopy

Claim ID: `L-100701`  
Status: **PROVED EXACT FINITE OPERATOR THEOREM**  
Created: 2026-08-20  
Depends on: PR #677 finite Euler squaring; `L-100700`  
RH status: **not assumed**

Let

\[
E_h=I-r_hU_h,
\qquad
Q_h=I-r_h^2U_h^2,
\qquad
R_h=r_hU_h(I-r_hU_h).
\]

Then

\[
\boxed{E_h=Q_h-R_h.}
\tag{L-100701.1}
\]

The factor `Q_h` is the exact squared-prime factor produced by multiplying
`E_h` by `I+r_hU_h`. The term `R_h` is the first unsquared transition which
must be retained when returning to the original Euler source.

For an interval put

\[
E_{a:b}=\prod_{h=a}^{b}E_h,
\qquad
Q_{a:b}=\prod_{h=a}^{b}Q_h,
\]

with empty products equal to `I`.

## 1. First-transition expansion

For every `a<=b`,

\[
\boxed{
E_{a:b}
=Q_{a:b}
-
\sum_{t=a}^{b}
Q_{a:t-1}R_tE_{t+1:b}.
}
\tag{L-100701.2}
\]

### Proof

Induct on `b-a`. For one factor this is (L-100701.1). If the identity holds
through `b-1`, multiply it by `E_b=Q_b-R_b` and group the term whose first
transition is `b`. Equivalently, expand `prod(Q_h-R_h)` and assign every
nonempty transition subset to its least member. Every monomial appears exactly
once.

No inverse of `I+r_hU_h` is used.

## 2. Double-owner insertion

For `i<j`, PR #691 gives

\[
\mathcal D_{i,j}
=r_ir_jU_iU_jE_{i+1:j-1}.
\]

Substitution of (L-100701.2) yields

\[
\boxed{
\begin{aligned}
\mathcal D_{i,j}
={}&r_ir_jU_iU_jQ_{i+1:j-1}\\
&-
\sum_{i<t<j}
 r_ir_jU_iU_jQ_{i+1:t-1}R_tE_{t+1:j-1}.
\end{aligned}
}
\tag{L-100701.3}
\]

Thus every long double-owner interval splits into:

1. a fully squared interior core;
2. one explicit first-transition label `t`;
3. the exact unsquared future interval after `t`.

This is a coefficient-exact **triple-owner localization** `(i,t,j)`. It is
strictly finer than applying a completed scalar and then attempting the
alternating inverse.

## 3. Higher transitions are already included

The future factor `E_(t+1:j-1)` contains all later transitions with their
native parity. Iterating (L-100701.2) gives the full ordered transition simplex,
but (L-100701.3) is often the useful stopping point: the first transition is
explicit and the prefix before it has summable squared-prime owner mass.

## 4. Statement-to-use boundary

Finite squaring may be used inside a double-owner interval only through the
balanced identity (L-100701.3), or an algebraically equivalent transition
expansion. Keeping the positive completed core and discarding the transition
packet changes the native Euler source.

The exact verifier checks (L-100701.2)--(L-100701.3) coefficientwise on every
subinterval of a five-label rational fixture.