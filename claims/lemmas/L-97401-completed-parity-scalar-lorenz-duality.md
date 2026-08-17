# L-97401 — Completed-parity scalar Hall is an exact finite Lorenz linear program

Claim ID: `L-97401`  
Status: **PROVED EXACT FINITE-DIMENSIONAL THEOREM**  
Created: 2026-08-18  
Depends on: `L-97400`  
RH status: unproved

Fix one real endpoint `X` and completely expand its finite rough-history source, retaining cumulative parity and activation sides. Let the actual even atoms be indexed by `i=1,...,M`. Atom `i` has available coefficient `a_i>=0`, strictly positive target `t_i`, and scalar coordinate

`r_i=5R_2(i)+3R_3(i)`.

Let the complete odd source have target and scalar demands

`T_O=sum_o b_o t_o`,

`R_O=sum_o b_o r_o`.

The scalar common-source problem is to find `0<=u_i<=a_i` such that

`sum_i t_i u_i=T_O`

and

`sum_i r_i u_i>=R_O`.

Put `T_E=sum_i a_i t_i`, and for `0<=T<=T_E` define

`Phi_X(T)=max {sum_i r_i u_i: 0<=u_i<=a_i, sum_i t_i u_i=T}`.

Then the common-source problem is feasible if and only if

`T_O<=T_E` and `R_O<=Phi_X(T_O)`.

## Explicit Lorenz formula

Order the atoms by decreasing ratio

`theta_i=r_i/t_i`.

Let `A_k=sum_(i<=k)a_i t_i`, `A_0=0`. For the unique `k` with `A_(k-1)<=T<=A_k`,

`Phi_X(T)=sum_(i<k)a_i r_i + theta_k(T-A_(k-1))`.

Thus an optimizer saturates all larger scalar-per-target ratios before using a smaller one and has at most one fractional atom.

## Exact one-parameter dual

The same value equals

`Phi_X(T)=min_(lambda in R) [lambda T + sum_i a_i(r_i-lambda t_i)_+]`.

Proof: weak duality is immediate. Taking `lambda=theta_k` at the Lorenz threshold gives equality.

If the inequality fails, an optimizing `lambda` is an exact finite separating functional for the entire completed-parity scalar cone.

## Zero-strength audit

At `lambda=0`, the dual inequality required for feasibility contains

`R_O <= sum_i a_i(r_i)_+`.

When all completed even scalar coordinates are nonnegative, this reduces to the desired global scalar sign. More generally, the exact Lorenz inequality controls the positive part of the scalar source against the odd scalar demand. It is therefore the conclusion-producing arithmetic theorem, not a bookkeeping lemma.

Uniform validity for every real `X`, including both one-sided activation limits, is denoted `CPSL67`.

## Scope firewall

This theorem is exact at target-plus-scalar scope. If a later construction needs score, rowwise, ordinary-column, radix-four, or boundary coordinates, those are additional resources and require a multi-resource LP. Conversely, the direct scalar Mellin consumer needs only scalar nonnegativity; `R-97300` forbids lifting scalar exactness into two-row feasibility without proof.

```text
finite primal program             PROVED EXACT
Lorenz optimizer                  PROVED EXACT
one-parameter dual                PROVED EXACT
finite separator                  PROVED EXACT
uniform CPSL67                    OPEN / RH-BEARING
```
