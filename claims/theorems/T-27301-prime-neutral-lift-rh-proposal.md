# T-27301 — Prime-neutral positive-lift proposal for RH

Claim ID: `T-27301`  
Title: Ordinary-prime dual collapse plus a proper-power-neutral positive lift implies the Riemann Hypothesis  
Status: **FULL ELEMENTARY PROPOSAL — `PNL` OPEN; RH UNPROVED**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #273  
Parent: draft PR #267  
Depends on: `R-27301`, `L-27301`, `L-27302`; PR #248 `L-24517/T-24504`

## 1. Exact finite front door

The parabolic carry benchmark satisfies

\[
b_X^{(0)}(m)\ge0
\]

and

\[
J_{\mathbb P,X}(b_X^{(0)})
\ge4\sqrt X-O(\log^2X).
\tag{T-27301.1}
\]

For ordinary primes, `L-27301` proves unconditionally that there is a
coordinatewise nonnegative correction \(h\) making every prime constraint
feasible. The finite dual cone collapses to the endpoint row, whose parabolic
residual is zero.

Thus the graph/feasibility part of the ordinary-prime problem is closed.

## 2. Exact remaining finite theorem

Construct \(h_m\ge0\) satisfying

\[
v_p(b_X^{(0)}+h)
\le
\frac1{\sqrt p}\log\frac Xp
\qquad(p\le X)
\tag{T-27301.2}
\]

while preserving the proper-prime-power responses,

\[
v_{p^a}(h)=0
\qquad(a\ge2,\ p^a\le X),
\tag{T-27301.3}
\]

or, more generally,

\[
\sum_{\substack{p^a\le X\\a\ge2}}
(\log p)v_{p^a}(h)
\le X^{o(1)}.
\tag{T-27301.4}
\]

Call this the Proper-Power-Neutral Lift theorem `PNL`.

The exact Farkas dual is the monotone additive-potential inequality in
`L-27302`. It contains the complete logarithmic/von-Mangoldt ray and is
therefore an honest RH-bearing theorem.

## 3. Sharp ordinary-prime ramp

Under PNL,

\[
J_{\mathbb P,X}(h)
=
J_X(h)+O(X^{o(1)})
\ge -X^{o(1)}.
\]

Consequently,

\[
\begin{aligned}
P_X
&\ge J_{\mathbb P,X}(b_X^{(0)}+h)\\
&\ge4\sqrt X-X^{o(1)}.
\end{aligned}
\tag{T-27301.5}
\]

The proper-prime-power tail of the complete ramp is only \(O(\log^2X)\), so

\[
\sum_{p^a\le X}
\frac{\log p}{p^{a/2}}\log\frac X{p^a}
\ge4\sqrt X-X^{o(1)}.
\tag{T-27301.6}
\]

## 4. RH transfer

At \(X=N^2\), the source-pinned square-screw identity gives a
subpolynomial upper envelope for the zeta screw function. The reviewed
interpolation and Landau one-sign theorem exclude every zeta zero with
real part greater than \(1/2\). Functional-equation symmetry gives RH.

Thus

\[
\boxed{\mathrm{PNL}\Longrightarrow\mathrm{RH}.}
\tag{T-27301.7}
\]

## 5. Why this proposal is sharper than the annular frame proposal

The previous `ADF` route asks for an \(L^2\)-small annular flow. In the exact
logarithmic direction it would force an \(X^{-3/2+o(1)}\) prime-ramp error.

The present route asks only for:

```text
ordinary-prime feasibility          already exact;
proper-power weighted neutrality    X^o(1).
```

No global flow norm, generated frame floor, or stepwise leakage contraction is
required.

## 6. Reviewer-first acceptance and rejection

The proposal is accepted only after a source-level proof of PNL or its weighted
form. It is rejected as a completion by any one of:

1. an omitted proper-prime-power row;
2. a correction \(h\) with a hidden negative coordinate;
3. a prime constraint repaired only after taking absolute values;
4. a proper-power leakage larger than the declared \(X^{o(1)}\) budget;
5. removal of the logarithmic dual ray;
6. an incorrect square-screw sign or endpoint normalization.

## 7. Status

```text
ADF as sole canonical hinge               WITHDRAWN
ordinary-prime positive feasibility       PROPOSED COMPLETE
proper-power-neutral finite dual          PROPOSED COMPLETE
PNL existence                             OPEN / RH-BEARING
PNL -> prime ramp -> RH                   PROPOSED COMPLETE
Riemann Hypothesis                        UNPROVED
```
