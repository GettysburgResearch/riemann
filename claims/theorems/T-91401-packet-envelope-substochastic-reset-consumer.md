# T-91401 — A packet-envelope substochastic reset closes the endpoint-loss criterion

Claim ID: `T-91401`  
Status: **PROVED ABSTRACT CONSUMER — ARITHMETIC PRODUCER SEPARATE**  
Created: 2026-08-13  
Depends on: endpoint-score RH consumer; positive linear packet assembly  
RH status: **conditional on the packet reset hypotheses**

## 1. Packet cone and loss

For every endpoint `X`, let `\mathscr C_X` be a cone of admissible positive typed packets. A packet may retain its full source measure, target, score, component rows and boundary ports; it need not be a scalar copy of one preferred native packet.

Let

\[
m_X:\mathscr C_X\to\mathbb R_{\ge0}
\]

be an additive positive mass, and let

\[
\Delta_X:\mathscr C_X\to\mathbb R
\]

be the optimal signed endpoint-score loss. Assume:

\[
\Delta_X(cP)=c\Delta_X(P),\qquad c\ge0,
\tag{T-91401.1}
\]

and

\[
\Delta_X(P+Q)\le\Delta_X(P)+\Delta_X(Q).
\tag{T-91401.2}
\]

These follow whenever feasible packet packings add and the score is linear: combine an almost-optimal packing for `P` with one for `Q`.

Define the worst normalized packet envelope

\[
\boxed{
\Lambda(X)=
\sup_{1\le Y\le X}
\sup_{\substack{P\in\mathscr C_Y\\m_Y(P)=1}}
\max(0,\Delta_Y(P)).
}
\tag{T-91401.3}
\]

Then every packet obeys

\[
\boxed{
\Delta_Y(P)\le m_Y(P)\Lambda(X)
\qquad(Y\le X).
}
\tag{T-91401.4}
\]

This remains true when the particular packet loss is negative.

## 2. Measure-valued reset hypothesis

Fix `0<c<1`. Suppose every packet `P in \mathscr C_X` admits a positive reset decomposition into a current packet and child packets `P_b in \mathscr C_{Y_b}` such that

\[
Y_b\le cX+C_0,
\tag{T-91401.5}
\]

\[
\boxed{
\sum_bm_{Y_b}(P_b)\le m_X(P),
}
\tag{T-91401.6}
\]

and

\[
\boxed{
\Delta_X(P)
\le E_Xm_X(P)+\sum_b\Delta_{Y_b}(P_b),
}
\tag{T-91401.7}
\]

where

\[
E_X\le C_1(1+\log\log(3X))^A.
\tag{T-91401.8}
\]

No scalar coefficient `theta_b` and no identification of a restricted branch with a preferred native packet are assumed.

## 3. Envelope recurrence

Normalize `m_X(P)=1`. By (T-91401.4)--(T-91401.7),

\[
\begin{aligned}
\Delta_X(P)
&\le E_X+
\sum_bm(P_b)\Lambda(cX+C_0)\\
&\le E_X+\Lambda(cX+C_0).
\end{aligned}
\]

Taking the supremum gives

\[
\boxed{
\Lambda(X)
\le C_1(1+\log\log(3X))^A
+\Lambda(cX+C_0).
}
\tag{T-91401.9}

Iteration terminates after `O(log X)` levels. Hence

\[
\boxed{
\Lambda(X)
=O\!\left(\log X(1+\log\log X)^A\right)
=o(\log^2X).
}
\tag{T-91401.10}

## 4. Why this repairs the scalar-weight objection

A positive restriction of mass `theta` can have the same absolute loss as its parent; source mass alone does not imply loss `<=theta` times the loss of that one parent packet.

The envelope argument uses the valid inequality

\[
\Delta(P_b)\le m(P_b)\times
\bigl[\text{worst normalized packet loss at the child scale}\bigr].
\]

It therefore survives arbitrary restrictions, different target/score normalizations, and negative packet losses. The direct Euler factor `p^{-1/2}` may be retained inside the actual child packet rather than guessed as a scalar coefficient.

## 5. RH implication

Assume the native root packet `P_X^{\rm nat}` has uniformly bounded mass and the established endpoint theorem gives

\[
F_\Lambda(X)\le\Delta_X(P_X^{\rm nat}).
\tag{T-91401.11}
\]

Then (T-91401.4) and (T-91401.10) imply

\[
F_\Lambda(X)=o(\log^2X),
\]

and the resident endpoint-score criterion yields RH.

## 6. Scope

```text
positive homogeneity/subadditivity -> packet envelope EXACT
measure-valued substochastic tree estimate           EXACT
arbitrary restricted packet handling                 EXACT
signed-loss coefficient problem                      CLOSED ABSTRACTLY
arithmetic packet reset hypotheses                    OPEN / PRODUCER
root packet mass and endpoint criterion               IMPORTED / MUST BE AUDITED
Riemann Hypothesis                                    CONDITIONAL
```
