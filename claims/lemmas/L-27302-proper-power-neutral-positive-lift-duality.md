# L-27302 — Proper-power-neutral positive lift and its exact Farkas dual

Claim ID: `L-27302`  
Title: A positive ordinary-prime repair that is neutral on proper prime powers would close the elementary RH route  
Status: **PROPOSED COMPLETE FINITE DUALITY; PNL EXISTENCE OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #273  
Depends on: `L-27301`; PR #248 `L-24517`; PR #271 affine boundary lift  
Scope: exact finite cone and conditional RH interface

## 1. Prime and proper-power rows

Let

\[
\mathcal P_X=\{p:p\le X\},
\qquad
\mathcal H_X=\{p^a\le X:a\ge2\}.
\]

Write \(V_{\mathbb P}\) and \(V_{\mathbb H}\) for the corresponding
divisor-gradient matrices

\[
V(q,m)=\mathbf1_{q\mid m}-\mathbf1_{q\mid m-1}.
\tag{L-27302.1}
\]

Let

\[
r_p
=
v_p(b_X^{(0)})
-
\frac1{\sqrt p}\log\frac Xp.
\tag{L-27302.2}
\]

## 2. Proper-Power-Neutral Lift (`PNL`)

The finite theorem sought is the existence of \(h=(h_2,\ldots,h_X)\) such that

\[
\boxed{h_m\ge0,}
\tag{PNL1}
\]

\[
\boxed{
V_{\mathbb P}h\le-r_{\mathbb P},
}
\tag{PNL2}
\]

and

\[
\boxed{
V_{\mathbb H}h=0.
}
\tag{PNL3}
\]

`L-27301` proves (PNL1)--(PNL2) without (PNL3).  The neutrality condition is
the entire remaining finite obstruction in this coordinate.

## 3. PNL gives the sharp prime ramp

Put

\[
b=b_X^{(0)}+h.
\]

By (PNL1),

\[
b_m\ge b_X^{(0)}(m)\ge0.
\tag{L-27302.3}
\]

By (PNL2), every ordinary-prime constraint is feasible:

\[
v_p(b)\le p^{-1/2}\log(X/p).
\tag{L-27302.4}
\]

The complete physical objective increment is

\[
J_X(h)
=
\sum_{q=p^a\le X}\Lambda(q)v_q(h).
\tag{L-27302.5}
\]

By (PNL3), all proper-power terms vanish, so

\[
\boxed{
J_{\mathbb P,X}(h)=J_X(h).
}
\tag{L-27302.6}
\]

Since the physical weights of \(J_X\) are positive and \(h_m\ge0\),

\[
J_X(h)
=
\sum_{m=2}^Xh_m\log\frac m{m-1}
\ge0.
\tag{L-27302.7}
\]

Therefore

\[
\begin{aligned}
P_X
&=
\sum_{p\le X}\frac{\log p}{\sqrt p}\log\frac Xp\\
&\ge J_{\mathbb P,X}(b)\\
&=J_{\mathbb P,X}(b_X^{(0)})+J_X(h)\\
&\ge J_{\mathbb P,X}(b_X^{(0)}).
\end{aligned}
\tag{L-27302.8}
\]

PR #248 `L-24517` proves

\[
J_{\mathbb P,X}(b_X^{(0)})
\ge4\sqrt X-O(\log^2X).
\]

Hence PNL implies

\[
\boxed{
P_X\ge4\sqrt X-O(\log^2X),
}
\tag{L-27302.9}
\]

and the existing square-screw/Landau transfer gives RH.

A weaker quantitative form suffices: replace (PNL3) by

\[
\sum_{q\in\mathcal H_X}\Lambda(q)v_q(h)
\le X^{o(1)}.
\tag{L-27302.10}
\]

## 4. Exact Farkas dual

The system (PNL1)--(PNL3) is infeasible exactly when there exist

\[
y_p\ge0\quad(p\in\mathcal P_X),
\qquad
z_q\in\mathbb R\quad(q\in\mathcal H_X)
\]

such that

\[
\boxed{
V_{\mathbb P}^*y+V_{\mathbb H}^*z\ge0
}
\tag{L-27302.11}
\]

and

\[
\boxed{
\langle y,r_{\mathbb P}\rangle>0.
}
\tag{L-27302.12}
\]

Define the additive prime-power potential

\[
\boxed{
L_{y,z}(n)
=
\sum_{\substack{p\mid n}}y_p
+
\sum_{\substack{p^a\mid n\\a\ge2}}z_{p^a}.
}
\tag{L-27302.13}
\]

Then

\[
\boxed{
(V_{\mathbb P}^*y+V_{\mathbb H}^*z)_m
=
L_{y,z}(m)-L_{y,z}(m-1).
}
\tag{L-27302.14}
\]

Thus PNL is equivalent to the statement:

> Every nondecreasing additive potential whose first prime increments are
> nonnegative has nonpositive pairing with the parabolic ordinary-prime
> residual.

This is a finite elementary inequality.  It has no hidden functional-analytic
existence step.

## 5. The logarithmic firewall

Take

\[
y_p=\log p,
\qquad
z_{p^a}=\log p
\quad(a\ge2).
\tag{L-27302.15}
\]

Then

\[
L_{y,z}(n)=\log n
\]

and

\[
V_{\mathbb P}^*y+V_{\mathbb H}^*z
=
\left(\log\frac m{m-1}\right)_{m=2}^X
>0.
\tag{L-27302.16}
\]

The Farkas objective is

\[
\boxed{
\langle y,r_{\mathbb P}\rangle
=
J_{\mathbb P,X}(b_X^{(0)})-P_X.
}
\tag{L-27302.17}
\]

This is the sharp ordinary-prime ramp deficit itself. Therefore PNL is
genuinely RH-bearing: a proof may not delete, damp, or orthogonally project out
the logarithmic ray.

The role of proper prime powers is now precise. They carry only
\(O(\log^2X)\) in the final ramp, but their free dual coefficients are what
allow the monotone additive cone to contain the logarithmic direction.

## 6. Proposed proof mechanism

The most promising source-specific route is:

1. use the exact ordinary-prime collapse of `L-27301`;
2. solve the proper-power neutrality constraints by dyadic and higher
   prime-power correction chains;
3. recombine all powers of one prime before taking a positive part;
4. use the factor-two child descent and bounded consecutive-power clusters of
   PR #254;
5. retain the logarithmic ray as one scalar recurrence rather than paying it by
   a generic norm;
6. allow \(O(\log^A X)\) weighted proper-power leakage, which is already within
   the final error budget.

## 7. Exact boundary

```text
PNL finite cone and Farkas dual          PROPOSED COMPLETE
PNL -> sharp ordinary-prime ramp         PROPOSED COMPLETE
ordinary-prime feasibility alone         PROVED IN L-27301
proper-power-neutral positive lift       OPEN / RH-BEARING
logarithmic dual ray                      RETAINED EXACT
Riemann Hypothesis                        UNPROVED
```
