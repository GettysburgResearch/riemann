# L-91658 — Same-index multiplicative child placement is a complete endpoint-datum functor

Claim ID: `L-91658`  
Status: **PROVED EXACT LINEAR FUNCTOR THEOREM — NORMALIZATION EXPLICIT**  
Created: 2026-08-13  
Depends on: `L-91361`, `L-91653`, `L-91406`  
RH status: **unproved**

## 1. Typed datum at the child endpoint

Let `Y=X/m`, with `m>=1`, and put `r_m=m^(-1/2)`. A recursively transportable normalized datum at endpoint `Y` is

\[
P_Y=(\ell,J,T,S,E,q,\Gamma,\Xi,b),
\]

where all coordinates are additive and positively homogeneous, `q` is the nonnegative component row, `Gamma` and `Xi` are its exact ordinary and radix-four responses, `E` is literal row score, and `b` consists only of boundary capacities owned by this child packet. Root-global collars, omissions and common ports remain current-generation data.

## 2. Three distinct objects

The notation must distinguish:

1. `U_mP_Y`: the **normalized same-index embedding** into the parent coordinate. It changes endpoint/provenance labels but not numerical packet coordinates.
2. `r_mU_mP_Y`: the arithmetic placement of one unit child source under node multiplication `n -> mn`.
3. `cU_mP_Y`: a child whose actual arithmetic source coefficient in the parent is already the scalar `c`.

Thus

\[
(q,\Gamma,\Xi,J,T,S,E,b)_X(U_mP_Y)
=(q,\Gamma,\Xi,J,T,S,E,b)_Y(P_Y),
\tag{L-91658.1}
\]

while

\[
(q,\Gamma,\Xi,J,T,S,E,b)_X(r_mU_mP_Y)
=r_m(q,\Gamma,\Xi,J,T,S,E,b)_Y(P_Y).
\tag{L-91658.2}
\]

`L-91361` is exactly the statement that multiplication of source nodes supplies the coefficient `r_m` while retaining the same row indices. No affine row-index dilation and no fractional physical column occurs.

## 3. Compatibility with the causal identity

The causal generator is

\[
\boxed{
C_{m;X}=P_X-r_mU_mP_{X/m}.
}
\tag{L-91658.3}
\]

For the provenance coefficients

\[
\alpha_i=r_i\lambda_i,
\]

one has

\[
\lambda_iC_{p_i;X}+\alpha_iU_{p_i}P_{X/p_i}
=\lambda_iP_X.
\tag{L-91658.4}
\]

There is no double scaling: the final scalar `alpha_i` is already the actual child coefficient in the parent coordinate. Equivalently,

\[
\alpha_iU_{p_i}P_{X/p_i}
=\lambda_i(r_iU_{p_i}P_{X/p_i}).
\]

## 4. Feasible-set covariance

For normalized embedding,

\[
\boxed{
\mathcal F_X(U_mP_Y)=U_m\mathcal F_Y(P_Y),
}
\tag{L-91658.5}
\]

where `U_m` keeps the numerical row vector and changes only endpoint/provenance labels. Every ordinary, radix-four, score and child-owned boundary coordinate is identical.

For arithmetic placement,

\[
\boxed{
\mathcal F_X(r_mU_mP_Y)=r_mU_m\mathcal F_Y(P_Y).
}
\tag{L-91658.6}
\]

The literal score obeys the same two rules.

## 5. Deficit covariance

Consequently

\[
\boxed{
\Delta_X(U_mP_Y)=\Delta_Y(P_Y),
}
\tag{L-91658.7}
\]

and, by positive homogeneity,

\[
\boxed{
\Delta_X(cU_mP_Y)=c\Delta_Y(P_Y)
\qquad(c\ge0).
}
\tag{L-91658.8}
\]

In particular, the final child in (L-91658.4) contributes exactly

\[
\alpha_i\Delta_{X/p_i}(P_{X/p_i}).
\]

This is the coefficient used by the packet envelope.

## 6. Source-disjoint sums

If

\[
P_X=P_{\rm cur}+\sum_bc_bU_{m_b}P_{X/m_b}^{(b)}
\]

is an exact source-disjoint datum identity, arbitrary feasible child rows may be inserted by

\[
d_X=d_{\rm cur}+\sum_bc_bU_{m_b}d_b.
\]

All ordinary, radix-four, benchmark, score and child-owned boundary ledgers add once. Therefore

\[
\boxed{
\Delta_X(P_X)
\le\Delta_X(P_{\rm cur})+
\sum_bc_b\Delta_{X/m_b}(P_b).
}
\tag{L-91658.9}
\]

This is the omitted cross-endpoint theorem identified by PR #443.

```text
normalized embedding U_m                         EXACT
arithmetic unit placement r_m U_m                EXACT
actual child coefficient c                       EXTERNAL SCALAR
same-index capacity and score covariance         EXACT
child deficit coefficient alpha_i                EXACT
root-global collars and common ports             CURRENT, NOT RECURSIVE
Riemann Hypothesis                               UNPROVED
```
