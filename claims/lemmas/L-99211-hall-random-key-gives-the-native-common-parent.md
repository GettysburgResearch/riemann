# L-99211 — Fractional Hall plus one random key gives the literal native common parent

Claim ID: `L-99211`  
Status: **PROPOSED COMPLETE EXACT SOURCE-DISINTEGRATION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-19  
Depends on: `L-99020`, `L-99021`, `L-99210`; abstract random-key theorem of PR #632  
RH status: **not assumed**

## 1. Hall is already a literal divisible-source partition

Fix one compact Hall fibre. For every positive/even source `e`, represent its
target mass `T_e` by the interval `I_e=[0,T_e)`. Let `t(o,e)>=0` be the
nested-neighbourhood Hall flow, with

\[
 \sum_e t(o,e)=T_o,
 \qquad \sum_o t(o,e)\le T_e.
\]

Partition `I_e` into intervals `I_(o,e)` of lengths `t(o,e)` and one residual
interval of length

\[
 u_e=T_e-\sum_ot(o,e).
\]

If `rho_e` and `rho_o` are the normalized physical component-row profiles,
each matched micro-source contributes

\[
 t(o,e)(\rho_e-\rho_o)\ge0,
\]

because `e<=o` and `L-99020` proves `rho_e>=rho_o` in every component row. The
residual interval carries `u_e rho_e` and is the only Hall output allowed to
recurse. Writing `Y_e=x/e` and `T_e=T(Y_e)`,

\[
 u_e\rho_e=\frac{u_e}{T_e}\mathbf P_{Y_e}.
\]

Thus its coefficient is the literal source fraction `c=u_e/T_e in [0,1]`, not
a separately normalized child mass. The Hall row bonus is the nonnegative row
observation of matched source and is never recursively copied.

## 2. Causal children are restrictions of the same residual packet

Consider one residual packet with coefficient `c>=0` and endpoint `Y`. Let its
active rough children have endpoints `Y_i<=Y` and exact coefficients

\[
 \alpha_i=r_i\lambda_i,
 \qquad r_i=p_i^{-1/2},
 \qquad \sum_i\alpha_i<67^{-1/2}<1/8.
\tag{L-99211.1}
\]

Use a scalar control measure `nu=sum_a M_a` for the finite positive vector
measure of `L-99210`, write `d\mathbf M=v(t)d\nu(t)`, and cross the source
`c v(t)d\nu(t)` with `[0,1]`. Put

\[
 f_i(t)=\alpha_i\mathbf1_{t\le Y_i},
 \qquad F_i(t)=\sum_{h\le i}f_h(t).
\]

The sets

\[
 E_i=\{(t,u):F_{i-1}(t)\le u<F_i(t)\}
\tag{L-99211.2}
\]

are disjoint because `sum_i f_i(t)<1/8`. Restriction to `E_i`, followed by the
same-index child label map, gives exactly

\[
 \alpha_i c\mathbf P_{Y_i}.
\tag{L-99211.3}
\]

The complementary set gives

\[
 c\mathbf P_Y-\sum_i\alpha_i c\mathbf P_{Y_i}.
\tag{L-99211.4}
\]

By the exact causal algebra,

\[
\begin{aligned}
 c\mathbf P_Y-\sum_i\alpha_i c\mathbf P_{Y_i}
={}&cs_k\mathbf P_Y\\
&+c\sum_i\lambda_i(\mathbf P_Y-r_i\mathbf P_{Y_i}),
\end{aligned}
\tag{L-99211.5}
\]

which is precisely the positive current packet. Hence the causal decomposition
is one literal partition of one unnormalized residual source, not merely a
compatible list of marginals.

## 3. The complete finite source tree

At every child node repeat Sections 1--2 with a fresh key coordinate. Since

\[
 Y'\le Y/67+1,
\]

the tree has finite depth at every fixed root. Every micro-source has exactly
one fate:

```text
matched Hall current;
causal current;
one labelled child;
one terminal leaf;
one declared positive omission.
```

No micro-source enters two children, and the Hall bonus never enters the child
operator. Summing all cylinder observations gives the finite-tree physical-row
identity consumed by the nilpotent resolvent.

## 4. Positive direct integration

Take the disjoint union over the positive equality endpoint measure. Hall
intervals, endpoint Stieltjes coordinates and random keys become source
coordinates. Finite Tonelli preserves the exact current/child identity and
every provenance label. Common positive restrictions or omissions cannot
create a duplicate owner.

## 5. Consequence

The local identity

\[
 \mathsf E_X=\mathsf J_X+\mathsf E_X\mathsf T_X
\]

is therefore realized on one literal labelled source, provided the frozen
compact Hall/profile and endpoint-frame statements hold at their stated
scopes.
