# L-91658 — Same-index multiplicative child placement is a complete endpoint-datum functor

Claim ID: `L-91658`  
Status: **PROVED EXACT LINEAR FUNCTOR THEOREM**  
Created: 2026-08-13  
Depends on: `L-91361`, `L-91653`, `L-91406`  
RH status: **unproved**

## 1. Typed datum at the child endpoint

Let `Y=X/m`, with `m>=1`. A recursively transportable typed datum at endpoint `Y` is

\[
P_Y=(\ell,J,T,S,E,q,\Gamma,\Xi,b),
\]

where all coordinates are additive and positively homogeneous, `q` is the nonnegative component row, `Gamma` and `Xi` are its exact ordinary and radix-four response vectors, `E` is literal row score, and `b` consists only of boundary capacities owned by this child packet. Root-global collars, omissions and common ports are not child-owned and remain current-generation data.

## 2. The physical placement functor

Define `U_mP_Y` in the parent physical row space by:

```text
source node n                 -> mn;
source coefficient            -> m^(-1/2) times the child coefficient;
row index j                   -> j;
J,T,S,E,q,Gamma,Xi,b          -> m^(-1/2) times the child coordinate;
tail-prime index              -> advanced past every prime dividing m.
```

The equality of row coordinates is exactly `L-91361`:

\[
q_X(U_mP_Y)=m^{-1/2}q_Y(P_Y)
\tag{L-91658.1}
\]

in the same row index. Consequently

\[
\Gamma_X(U_mP_Y)=m^{-1/2}\Gamma_Y(P_Y),
\qquad
\Xi_X(U_mP_Y)=m^{-1/2}\Xi_Y(P_Y),
\tag{L-91658.2}
\]

and

\[
J_X(U_mP_Y)=m^{-1/2}J_Y(P_Y),
\quad
T_X(U_mP_Y)=m^{-1/2}T_Y(P_Y),
\tag{L-91658.3}
\]

\[
S_X(U_mP_Y)=m^{-1/2}S_Y(P_Y),
\quad
E_X(U_mP_Y)=m^{-1/2}E_Y(P_Y),
\quad
b_X(U_mP_Y)=m^{-1/2}b_Y(P_Y).
\tag{L-91658.4}
\]

No affine row-index dilation and no fractional physical column occurs.

## 3. Feasible packings transport exactly

Let `F_Y(P_Y)` be the feasible nonnegative row-packing cone determined by all ordinary, radix-four and child-owned boundary capacities of `P_Y`. Define

\[
\iota_m d=m^{-1/2}d
\]

in the same row index. Equations (L-91658.1)--(L-91658.4) give

\[
\boxed{
F_X(U_mP_Y)=\iota_mF_Y(P_Y).
}
\tag{L-91658.5}
\]

Indeed, every defining capacity inequality and every row coefficient is scaled by the same positive number. The inverse inclusion follows by multiplying a parent-feasible row by `m^(1/2)`.

The literal score scales exactly:

\[
\operatorname{Score}_X(\iota_md)
=m^{-1/2}\operatorname{Score}_Y(d).
\tag{L-91658.6}
\]

## 4. Deficit covariance

For the physical packet deficit of `L-91653`, equations (L-91658.3), (L-91658.5), and (L-91658.6) imply

\[
\boxed{
\Delta_X(U_mP_Y)=m^{-1/2}\Delta_Y(P_Y).
}
\tag{L-91658.7}
\]

Thus the child coefficient appearing in the provenance reset is the literal coefficient of the child deficit. It is not inferred from hidden target or score fractions.

## 5. Source-disjoint sums

If

\[
P_X=P_{\rm cur}+\sum_bU_{m_b}P_{X/m_b}^{(b)}
\]

is an exact source-disjoint datum identity, arbitrary feasible child packings may be inserted by

\[
d_X=d_{\rm cur}+\sum_b\iota_{m_b}d_b.
\]

All ordinary, radix-four, benchmark, score and child-owned boundary ledgers add once. Consequently

\[
\Delta_X(P_X)
\le\Delta_X(P_{\rm cur})+
\sum_bm_b^{-1/2}\Delta_{X/m_b}(P_b).
\tag{L-91658.8}
\]

This is the omitted cross-endpoint theorem identified by PR #443.

```text
same-index row placement                       EXACT
ordinary/detail capacity scaling               EXACT
literal-score scaling                          EXACT
feasible-set covariance                        EXACT
deficit covariance                             EXACT
root-global collars and common ports           CURRENT, NOT RECURSIVE
Riemann Hypothesis                             UNPROVED
```
