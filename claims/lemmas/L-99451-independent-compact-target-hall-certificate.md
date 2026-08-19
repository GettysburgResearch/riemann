# L-99451 — Independent exact reconstruction of the compact target Hall gate

Claim ID: `L-99451`  
Status: **PROVED EXACT FINITE/DIRECTED THEOREM**  
Created: 2026-08-20  
Frozen comparison: `L-99020` in PR #620  
RH status: **not assumed**

For \(1\le t\le66\), define

\[
A_t=\sum_{n\le t}\frac{\mu(n)}n,
\qquad
B_t=\sum_{n\le t}\frac{\mu(n)}{\sqrt n},
\]

and

\[
H_t(x)=4\sqrt x\,A_t-3B_t.
\]

The nested compact Hall graph has a target-feasible flow once

\[
H_t(x)>0
\]

for every active threshold \(t\le x<67\).

## 1. Reduction to finitely many endpoints

For fixed \(t\), \(H_t(x)\) is affine in \(\sqrt x\). Therefore

\[
\inf_{t\le x<67}H_t(x)
=
\begin{cases}
H_t(t),&A_t\ge0,\\
H_t(67),&A_t<0,
\end{cases}
\tag{L-99451.1}
\]

where the second line is a strict lower limit because \(x<67\).

Thus the all-real Hall theorem reduces to 66 finite radical inequalities.

## 2. Directed radical certificate

Use the fixed denominator

\[
Q=2^{48}.
\]

For every integer \(1\le n\le67\), let

\[
\ell_n=\frac{\lfloor Q\sqrt n\rfloor}{Q},
\qquad
u_n=\frac{\lfloor Q\sqrt n\rfloor+1}{Q}.
\]

Then

\[
\ell_n\le\sqrt n\le u_n.
\]

The reciprocal interval is

\[
u_n^{-1}\le n^{-1/2}\le\ell_n^{-1}.
\]

All sums are then evaluated in exact `Fraction` arithmetic with outward
orientation. For a negative Möbius coefficient the reciprocal interval is
reversed before addition; for \(A_t<0\), the upper endpoint \(u_{67}\) is used
to form the lower bound of \(4A_t\sqrt{67}\).

The retained certificate checks every integer \(1\le t\le66\). Its exact
minimum lower enclosure occurs at \(t=13\):

\[
\boxed{
H_{13}(x)
>
0.359317660598493127\ldots
>
\frac7{20}
}
\tag{L-99451.2}
\]

uniformly for \(13\le x<67\).

The exact certificate hash is

```text
c08478d80d73be5b29409bff89e3ae7c6bdb49020912d3f098883b125141c4aa
```

and the complete 66-row rational ledger is stored at

```text
experiments/X-99450-three-interface-hardening/
  certificates/compact_hall_1_66.json
```

## 3. Hall consequence

The compact neighborhoods are nested by source index. The standard
nested-neighborhood Hall theorem therefore gives a nonnegative target flow
\(t_x(o,e)\), supported on \(e\le o\), with

\[
\sum_e t_x(o,e)=T_x(o),
\qquad
\sum_o t_x(o,e)\le T_x(e).
\]

Its residual targets are nonnegative.

This theorem independently reconstructs the finite compact target gate used by
PRs #620, #636, #646, #647, and #648. It does not establish the outer endpoint
registry or the fixed-row analytic consumer.
