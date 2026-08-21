# T-23803 — Reflected carry-sandwich proposal for RH

Claim ID: `T-23803`  
Title: A reflected two-contact contraction of the finite nonnegative carry sandwich implies the Riemann hypothesis  
Status: **FULL PROPOSED PROOF — `L-23806` IS THE EXPLICIT SYMBOLIC HINGE**  
Authoring agents: `gpt56-pro`, `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `L-23801`--`L-23803`, `L-23806`; `T-23801`; PRs #158, #202, #226, #229, #233  
Scope: full arithmetic composition; RH is not claimed independently verified

## 1. Exact finite sandwich

For every `X`, let

\[
 \mathfrak L(X)
 =\max\{G^Td:d\ge0,\ B_X^Td\le w_X\}
 \tag{T-23803.1}
\]

and

\[
 \mathfrak U(X)
 =\min\{G^Te:e\ge0,\ B_X^Te\ge w_X\}.
 \tag{T-23803.2}
\]

The exact carry--Legendre identity gives

\[
 \boxed{
 \mathfrak L(X)
 \le\mathcal P(X)
 \le\mathfrak U(X),}
 \tag{T-23803.3}
\]

where

\[
 \mathcal P(X)
 =\sum_{q=p^a\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
 \tag{T-23803.4}
\]

## 2. Reflected two-contact recurrence

Put

\[
 \Delta_X
 =1+igl(4\sqrt X-\mathfrak L(X)\bigr)_+
   +\bigl(\mathfrak U(X)-4\sqrt X\bigr)_+.
 \tag{T-23803.5}
\]

Assume `L-23806`: for one fixed `delta in (0,1/3)` and every sufficiently large
fixed `K`,

\[
 \Delta_X
 \le X^{2/K+o_K(1)}
 \left[
 1+
 \max_{Y\le X^{1-\delta}e^{O_K(1)}}\Delta_Y
 \right].
 \tag{T-23803.6}
\]

This is the scalar carry-envelope replacement for generic balanced Type II.

## 3. Scale contraction

Let

\[
 \vartheta
 =\limsup_{X\to\infty}
 \frac{\log\Delta_X}{\log X}.
 \tag{T-23803.7}
\]

For fixed `K`, (T-23803.6) gives

\[
 \vartheta
 \le\frac2K+(1-\delta)\vartheta.
 \tag{T-23803.8}
\]

Thus

\[
 \vartheta\le\frac{2}{K\delta}.
 \tag{T-23803.9}
\]

Let arbitrarily large fixed `K` run through the exact finite resolvent orders.
Then

\[
 \boxed{\vartheta=0.}
 \tag{T-23803.10}
\]

Consequently

\[
 \boxed{
 4\sqrt X-X^{o(1)}
 \le\mathfrak L(X)
 \le\mathcal P(X)
 \le\mathfrak U(X)
 \le4\sqrt X+X^{o(1)}.}
 \tag{T-23803.11}
\]

## 4. Zero exclusion

Equation (T-23803.11) gives

\[
 \mathcal P(X)=4\sqrt X+X^{o(1)}.
 \tag{T-23803.12}
\]

Put `X=e^x` and

\[
 A(x)=\mathcal P(e^x)-4e^{x/2}.
 \tag{T-23803.13}
\]

Then `A(x)=e^{o(x)}`. For `Re z>1/2`,

\[
 \int_0^\infty A(x)e^{-zx}dx
 =\frac{-\zeta'/\zeta(z+1/2)}{z^2}
  -\frac4{z-1/2}.
 \tag{T-23803.14}
\]

The zeta pole at `z=1/2` is canceled by the second term. Subexponential growth
of `A` makes the left side holomorphic throughout `Re z>0`. A nontrivial zero
`rho` with `Re rho>1/2` would produce a nonremovable pole at
`z=rho-1/2`, contradiction. Functional-equation symmetry gives

\[
 \boxed{\mathrm{RH}.}
 \tag{T-23803.15}
\]

This is the same finite-to-global deduction as `T-23801`; the novelty is the
proposed reflected proof of its carry-sandwich hypothesis.

## 5. One-sided alternative

`L-23804/T-23802` propose that a sharp nonnegative packing alone gives a
sufficient upper envelope for the square screw via Landau's one-sign theorem.
That shorter route remains available as an independent review target.

The two-sided theorem above is preferred for the full proposal because it gives
direct absolute convergence of the centered prime ramp and avoids a separate
one-sided Landau orientation adapter.

## 6. Why the proposal is narrower than BTP

The complete BTP theorem controls a packet-valued balanced energy. The carry
sandwich controls only the scalar functional needed to enclose the prime ramp.
Positive reflected diagonal energy is absorbed into the two convex envelopes;
it need not be small.

The proposal is also weaker than Carry Saturation: the lower and upper
certificates may differ and the exact inverse may contain negative entries.

## 7. Review firewall

The proposal is rejected if:

- a terminal face has three free contacts;
- a balanced row is assumed rather than reflected;
- a transition row is omitted;
- packing and covering errors fail to pair;
- the first-cell Mertens coordinate is lost;
- the recurrence is proved only for finitely many `K`;
- the loss is merely `o(sqrt X)` rather than `X^o(1)`.

A verified symbolic two-contact dictionary closes every remaining arrow.

## 8. Status

```text
finite carry/Legendre identities          proposed exact + exact replay
packing/covering LP and canonical vectors proposed exact
Mobius-curvature coordinates              proposed exact + exact replay
reflected Selberg identity                imported proposed exact
two-contact terminal theorem              new proposed hinge
scale contraction and zero exclusion      complete conditional proof
accepted proof of RH                      no
```
