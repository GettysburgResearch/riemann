# L-91406 — The endpoint packet deficit is positively homogeneous and subadditive

Claim ID: `L-91406`  
Status: **PROVED EXACT CONVEX-CONE THEOREM**  
Created: 2026-08-13  
Depends on: linear endpoint capacity map; linear score; positive row-packing cone  
RH status: **unproved**

## 1. Typed packets

At endpoint `X`, let a typed packet `P` determine linearly:

1. a benchmark `J_X(P)`;
2. an ordinary/radix-four capacity vector `\Omega_X(P)`;
3. any required boundary-port capacities.

Let `\mathcal F_X(P)` be the set of nonnegative finite row/endpoint packings satisfying all capacities of `P`. Let `\mathcal S_X(d)` be the linear endpoint score.

Define the optimal packet deficit

\[
\boxed{
\Delta_X(P)
=J_X(P)-\sup_{d\in\mathcal F_X(P)}\mathcal S_X(d).
}
\tag{L-91406.1}
\]

The supremum may be replaced by an infimum of signed loss; the proof is unchanged.

## 2. Positive homogeneity

Linearity of all packet capacities gives

\[
\mathcal F_X(cP)=c\mathcal F_X(P),
\qquad c\ge0.
\]

Therefore

\[
\boxed{
\Delta_X(cP)=c\Delta_X(P).
}
\tag{L-91406.2}

## 3. Minkowski superadditivity of feasibility

If `d_P` is feasible for `P` and `d_Q` is feasible for `Q`, then

\[
d_P+d_Q\ge0
\]

and every linear capacity inequality for `P+Q` is the sum of the corresponding inequalities. Hence

\[
\boxed{
\mathcal F_X(P)+\mathcal F_X(Q)
\subseteq\mathcal F_X(P+Q).
}
\tag{L-91406.3}

Consequently

\[
\sup_{d\in\mathcal F_X(P+Q)}\mathcal S_X(d)
\ge
\sup_{d\in\mathcal F_X(P)}\mathcal S_X(d)
+
\sup_{d\in\mathcal F_X(Q)}\mathcal S_X(d).
\]

Since `J_X` is linear,

\[
\boxed{
\Delta_X(P+Q)
\le\Delta_X(P)+\Delta_X(Q).
}
\tag{L-91406.4}

## 4. Restrictions are not scalar copies

For a positive restriction `P_B<=P`, no assertion of the form

\[
\Delta(P_B)\le\frac{m(P_B)}{m(P)}\Delta(P)
\]

is made. Such an inequality is false in general, exactly as PR #431 observes.

Instead, homogeneity gives

\[
\Delta(P_B)\le m(P_B)\Lambda_X
\]

for the worst normalized packet envelope of `T-91401`. This is the valid replacement.

## 5. Signed losses

The deficit may be negative. Equations (L-91406.2)--(L-91406.4) remain valid. In the envelope consumer one takes the positive part only after the supremum, so increasing a scalar coefficient never reverses an inequality involving a negative native loss.

## 6. Scope

```text
packet deficit positive homogeneity       EXACT
packet deficit subadditivity               EXACT
arbitrary packet restriction handling      VIA T-91401
native scalar branch coefficient           NOT REQUIRED
linear packet/capacity typing               REQUIRED INPUT
root endpoint-to-RH criterion               SEPARATE
Riemann Hypothesis                          UNPROVED
```
