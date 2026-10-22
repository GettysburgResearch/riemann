# M-27202 — Fail-closed Cycle Debt certificate

Claim ID: `M-27202`  
Status: **PRODUCTION METHODOLOGY / NO RH CLAIM**

## Purpose

`L-27205` and `T-27202` reduce the finite arithmetic theorem to one explicit
weighted negative-mass optimization. A proof object must expose the actual
source and every cycle correction; an objective value without reconstruction is
not accepted.

## Primal certificate

At endpoint `X`, emit:

```text
eta
complete balanced edge manifest E_eta(X)
carry columns chi_e(q)
capacity weights omega_e=sum_q chi_e(q)/sqrt(q)
exact target w_X(q)
exact Mobius divergence r_X
canonical tree flow d_tree(r_X)
fundamental-cycle matrix C_eta
cycle coordinates z_X
final signed flow d_X=d_tree+C_eta z_X
negative debt N_X=sum_e omega_e(-d_X(e))_+
```

Mandatory exact checks:

1. every edge is eta-balanced;
2. every fundamental cycle has zero divergence;
3. `partial d_X=r_X`;
4. every carry load equals `w_X(q)`;
5. the identity
   ```text
   sum_e d_X(e)omega_e
    =sum_q w_X(q)/sqrt(q)
   ```
   holds;
6. total capacity variation equals baseline plus twice the negative debt;
7. prime-power and all-integer entropy ledgers are replayed independently;
8. dyadic and `2/3` fixed-ratio shell projections are unchanged.

## Dual certificate

A lower obstruction emits a real potential `F(1),...,F(X)` satisfying

```text
0 <= F(n)-F(j)-F(n-j) <= omega_(n,j)
```

on every allowed split. Exact pairing then gives

```text
mathfrak N_eta(X)
 >= -sum_m r_X(m)F(m).
```

A claimed upper theorem is rejected if a retained dual certificate exceeds its
announced bound.

## Cofinal theorem

The asymptotic producer must prove, rather than infer from finite data,

```text
for every epsilon>0,
N_X <= C_epsilon X^epsilon
```

for all sufficiently large `X` or along a square-endpoint sequence sufficient
for the reviewed Landau transfer.

## Automatic rejection

Reject any artifact which:

- takes a positive part before exact cycle recombination;
- uses unweighted negative edge count instead of `omega_e`;
- changes one target carry column;
- omits an edge, collar, quotient layer, or fixed-ratio mutation;
- substitutes a generic kernel positivity or bounded-rank assertion;
- suppresses the directed ternary counterexample;
- reports a floating LP objective as a cofinal theorem;
- claims RH from finite feasibility alone.
