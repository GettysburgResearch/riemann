# L-99020 — Compact factor-67 Hall has a positive residual-source sort and a score-free positive row sort

Claim ID: `L-99020`  
Status: **PROPOSED COMPLETE EXACT/DIRECTED THEOREM**  
Created: 2026-08-18  
RH status: **not assumed**

## 1. Compact fibre

Fix `1<=x<67`. For a squarefree `k` supported on primes at most `61`, put

\[
T_x(k)=\frac{4\sqrt{x/k}-3}{\sqrt k},
\qquad
S_x(k)=\frac{5\sqrt{x/k}-3}{\sqrt k},
\]

and, for `j>=2`,

\[
A_{x,j}(k)=\frac1{\sqrt k}Q_{x/k}(j),
\]

with all atoms zero outside causal support. Let `E_x` and `O_x` be the
positive and negative Möbius occurrences.

For every active odd threshold `t`, define

\[
H_t(x)=\sum_{e\le t,\,\mu(e)=1}T_x(e)
       -\sum_{o\le t,\,\mu(o)=-1}T_x(o).
\]

Writing

\[
A_t=\sum_{n\le t}\frac{\mu(n)}n,
\qquad
B_t=\sum_{n\le t}\frac{\mu(n)}{\sqrt n},
\]

one has `H_t(x)=4sqrt(x)A_t-3B_t`. On `t<=x<67` this is affine in
`sqrt(x)`, so its minimum is at `x=t` if `A_t>=0` and at `x=67` if
`A_t<0`. The exact directed certificate in `X-99020` evaluates all active
thresholds and proves

\[
\boxed{H_t(x)>7/20.}
\tag{L-99020.1}

The nested-neighbourhood Hall theorem therefore gives a deterministic flow
`t_x(o,e)>=0`, supported on `e<=o`, satisfying

\[
\sum_e t_x(o,e)=T_x(o),
\qquad
\sum_o t_x(o,e)\le T_x(e).
\tag{L-99020.2}

Put

\[
u_x(e)=T_x(e)-\sum_o t_x(o,e)\ge0.
\tag{L-99020.3}

## 2. The exact two-sort identity

For any profile `rho`, finite algebra gives

\[
\sum_eT_e\rho(e)-\sum_oT_o\rho(o)
=
\sum_eu_e\rho(e)
+
\sum_{o,e}t(o,e)[\rho(e)-\rho(o)].
\tag{L-99020.4}

For the component-row profile

\[
\rho_j(k)=\frac{Q_{x/k}(j)}{4\sqrt{x/k}-3},
\]

the directed/analytic profile theorem reproduced in the standalone proof gives

\[
e\le o\Longrightarrow\rho_j(e)\ge\rho_j(o).
\tag{L-99020.5}

Hence the edge term is a coefficientwise nonnegative row

\[
B_{x,j}=\sum_{o,e}t_x(o,e)[\rho_j(e)-\rho_j(o)]\ge0.
\tag{L-99020.6}

For the declared score per target

\[
g(z)=\frac{5z-3}{4z-3},
\qquad g'(z)=-\frac3{(4z-3)^2}<0,
\]

the edge term has the opposite sign. Therefore

\[
\sum_eu_x(e)\frac{S_x(e)}{T_x(e)}
\ge
\sum_eS_x(e)-\sum_oS_x(o).
\tag{L-99020.7}

The correct output has two sorts:

```text
source sort:
    positive residual occurrences u_x(e),
    carrying target, declared score and component rows;

row sort:
    the coefficientwise nonnegative vector B_x,
    carrying no target, no declared score and no recursive child coordinate.
```

In every component row,

\[
\boxed{
\text{signed compact row}
=
\text{residual-source row}+B_x.
}
\tag{L-99020.8}

The row sort remains current-owned. It is never interpreted as a complete
positive score packet and is never recursively copied. At `x=2`, its omitted
declared-score coordinate would be strictly negative; `R-99020` and the replay
retain that mutation as a mandatory firewall.
