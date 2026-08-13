# L-91658 — Same-index multiplicative child placement is a complete endpoint-datum functor

Claim ID: `L-91658`  
Status: **PROVED EXACT LINEAR FUNCTOR THEOREM — NOTATION REPAIRED**  
Created: 2026-08-13  
Depends on: `L-91361`, `L-91653`, `L-91406`  
RH status: **unproved**

## 1. Typed datum at the child endpoint

Let `Y=X/m`, with `m>=1`, and put `r_m=m^(-1/2)`. A recursively transportable typed datum at endpoint `Y` is

\[
P_Y=(\ell,J,T,S,E,q,\Gamma,\Xi,b),
\]

where all coordinates are additive and positively homogeneous, `q` is the nonnegative component row, `Gamma` and `Xi` are its exact ordinary and radix-four response vectors, `E` is literal row score, and `b` consists only of boundary capacities owned by this child packet. Root-global collars, omissions and common ports remain current-generation data.

## 2. Relabelling and physical placement are distinct

Define `U_m` to be the **unscaled provenance relabelling**:

```text
source node n       -> mn;
row index j         -> j;
tail-prime index    -> advanced past every prime dividing m.
```

The physical placement is

\[
\boxed{\iota_mP_Y=r_mU_mP_Y.}
\tag{L-91658.1}
\]

This convention agrees with the causal generator used throughout the proposal:

\[
C_{m;X}=P_X-r_mU_mP_{X/m}=P_X-\iota_mP_{X/m}.
\tag{L-91658.2}
\]

There is no second factor of `r_m`.

By `L-91361`, the complete coordinates of the physical placement are

\[
q_X(\iota_mP_Y)=r_mq_Y(P_Y),
\tag{L-91658.3}
\]

\[
\Gamma_X(\iota_mP_Y)=r_m\Gamma_Y(P_Y),
\qquad
\Xi_X(\iota_mP_Y)=r_m\Xi_Y(P_Y),
\tag{L-91658.4}
\]

and

\[
(J,T,S,E,b)_X(\iota_mP_Y)
=r_m(J,T,S,E,b)_Y(P_Y).
\tag{L-91658.5}
\]

No affine row-index dilation and no fractional physical column occurs.

## 3. Feasible packings transport exactly

Let `F_Y(P_Y)` be the feasible nonnegative row-packing cone determined by all ordinary, radix-four and child-owned boundary capacities of `P_Y`. For a row define

\[
\iota_md=r_md
\]

in the same row index. Equations (L-91658.3)--(L-91658.5) give

\[
\boxed{
F_X(\iota_mP_Y)=\iota_mF_Y(P_Y).
}
\tag{L-91658.6}
\]

The inverse inclusion follows by multiplying a parent-feasible row by `r_m^(-1)`.

The literal score scales exactly:

\[
\operatorname{Score}_X(\iota_md)
=r_m\operatorname{Score}_Y(d).
\tag{L-91658.7}
\]

## 4. Deficit covariance

For the packet deficit of `L-91653`,

\[
\boxed{
\Delta_X(\iota_mP_Y)=r_m\Delta_Y(P_Y).
}
\tag{L-91658.8}
\]

Thus the coefficient of a placed child deficit is its literal physical coefficient. It is not inferred from hidden target or score fractions.

## 5. Source-disjoint sums

If

\[
P_X=P_{\rm cur}+\sum_b\iota_{m_b}P_{X/m_b}^{(b)}
\]

is an exact source-disjoint datum identity, arbitrary feasible child rows may be inserted by

\[
d_X=d_{\rm cur}+\sum_b\iota_{m_b}d_b.
\]

All ordinary, radix-four, benchmark, score and child-owned boundary ledgers add once. Consequently

\[
\Delta_X(P_X)
\le\Delta_X(P_{\rm cur})+
\sum_bm_b^{-1/2}\Delta_{X/m_b}(P_b).
\tag{L-91658.9}
\]

This is the omitted cross-endpoint theorem identified by PR #443.

```text
unscaled relabelling U_m                         EXACT
physical placement iota_m=m^(-1/2)U_m           EXACT
same-index row/capacity/score scaling            EXACT
feasible-set and deficit covariance              EXACT
root-global collars and common ports             CURRENT, NOT RECURSIVE
Riemann Hypothesis                               UNPROVED
```
