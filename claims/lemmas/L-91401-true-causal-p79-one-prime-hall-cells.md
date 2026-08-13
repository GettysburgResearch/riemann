# L-91401 — The true causal `P_79` one-prime Hall family is a finite two-variable cell problem

Claim ID: `L-91401`  
Status: **PROPOSED COMPLETE FINITE-REDUCTION THEOREM — DIRECTED REPLAY REQUIRED**  
Created: 2026-08-13  
Depends on: `R-91401`; terminal `P_79` prefix theorem; exact squarefree divisor list  
RH status: **unproved**

## 1. Truncated prefixes

For an odd threshold `t`, a cutoff `z>=0`, and displacement eight, define

\[
A_t(z)=
\sum_{\substack{e\le t+8,\ e\le z,\ \mu(e)=1}}\frac1e
-
\sum_{\substack{o\le t,\ o\le z,\ \mu(o)=-1}}\frac1o,
\]

\[
B_t(z)=
\sum_{\substack{e\le t+8,\ e\le z,\ \mu(e)=1}}\frac1{\sqrt e}
-
\sum_{\substack{o\le t,\ o\le z,\ \mu(o)=-1}}\frac1{\sqrt o},
\]

where only squarefree divisors of `P_79` are present.

The true Hall margin is exactly

\[
\boxed{
\mathcal H_{a,t}^{(8)}(p,y)
=a\sqrt{py}\,A_t(py)-3B_t(py)
-p^{-1/2}\bigl[a\sqrt y\,A_t(y)-3B_t(y)\bigr].
}
\tag{L-91401.1}
\]

This replaces the false untruncated formula fenced by `R-91401`.

## 2. Correct activation geometry

The support can change only on the finite surfaces

\[
y=d,
\qquad
py=d,
\]

where `d` ranges over squarefree `P_79` divisors at most `t+8`. Thus a proof must partition at both child activations and parent activations `y=d/p`.

Write

\[
s=\sqrt y,
\qquad
u=\sqrt p,
\qquad
v=\sqrt{py}=su.
\]

On one cell, with all four prefixes fixed,

\[
\boxed{
H(s,v)=aA_Pv-3B_P-rac{aA_Cs^2-3B_Cs}{v},
}
\tag{L-91401.2}
\]

where `(A_P,B_P)=(A_t(py),B_t(py))` and `(A_C,B_C)=(A_t(y),B_t(y))`.

For fixed `s`,

\[
\partial_vH
=aA_P+rac{aA_Cs^2-3B_Cs}{v^2}.
\tag{L-91401.3}
\]

For fixed `v`, the only nonlinear child term is the quadratic

\[
-aA_Cs^2+3B_Cs.
\tag{L-91401.4}
\]

Therefore the cell minimum occurs among:

1. cell endpoints;
2. the boundary `v=\sqrt{83}\,s`;
3. a derivative root of (L-91401.3), if it lies in the cell;
4. the single quadratic vertex from (L-91401.4), if it lies in the cell.

No sampling or floating optimizer is needed.

## 3. Finite proof set

For `t<4096`, every relevant parent source is at most `4103`; every child source is below `83`. Consequently the complete proof reduces to finitely many rational comparisons involving square roots of integers at most `4103`.

For `py>=t+8`, the parent prefixes are complete. The shifted reciprocal prefix is strictly positive, and the child Hall term is positive. Equation (L-91401.3) then shows that the margin increases with `p`. Thus no unbounded prime scan is required.

For `t>=4096`, retain the separate analytic large-prefix theorem.

## 4. Required replay contract

A valid checker must:

```text
construct the actual P_79 divisor support;
retain d<=py and d<=y separately;
partition at every y=d and y=d/p surface;
evaluate every admissible endpoint and interior critical point;
use outward rational enclosures for every square root;
fail closed if a derivative sign or critical-point location is unresolved;
write a content-bound manifest for source, inputs and result.
```

A positive replay would certify the true target and score Hall inequalities. It would not by itself provide a common row-typing transport; that is a separate packet-cone statement.

## 5. Proof boundary

```text
true causal Hall identity                     EXACT
complete activation geometry                  EXACT
finite candidate reduction                    EXACT
large-prime tail reduction                    EXACT GIVEN PREFIX INPUTS
all finite directed inequalities              REPLAY OBLIGATION
common target/score/every-row packet           SEPARATE
Riemann Hypothesis                             UNPROVED
```
