# 2026-08-08 — Green–dipole Skorokhod carry sharpness

Agent: `gpt56-pro`  
Issue: #260  
Branch: `agent/gpt56-pro/260-green-dipole-skorokhod`  
Status: **FULL PROPOSAL; GREEN–DIPOLE SHARPNESS OPEN; RH NOT CLAIMED**

## Frozen inputs

This pass began from the exact parabolic carry branch

```text
PR #248
5f2b25f89afbb90a3bc4ca6d40148f530303eb54
```

and inspected the live carry proposal, signed dipole, and cross-route review
stacks.

During the pass PR #240 advanced to

```text
fbc1dc1c75cdc8df01145c28a605f45415b5f5a6
```

with exact Green orthogonal neutralization and zero-cost two-moment signed
balayage. Those results were incorporated as dependencies, not restated.

## Main exact advance

Let `b^star` be the canonical endpoint-projected Green correction of the
parabolic seed, satisfying every prime-power carry constraint with equality.

The negative excursion

```text
a=(-b^star)_+
```

has a canonical interval layer cake. Each interval `(A,B]` is exactly the
signed constraint dipole

```text
+t at B
-t at A
```

and costs `t log(B/A)` in the carry objective.

Clipping only after the exact signed solve gives

```text
b^circle=(b^star)_+.
```

If

```text
epsilon_q=v_q(b^circle)-w_X(q),
D_plus =sum Lambda(q)(epsilon_q)_+,
D_minus=sum Lambda(q)(-epsilon_q)_+,
```

then exactly

```text
L_GS=J(b^circle)-D_plus <= prime ramp <= J(b^circle)+D_minus=U_GS,
prime ramp-L_GS=D_minus,
U_GS-prime ramp=D_plus.
```

The positive and negative interval endpoints are therefore recombined in
`epsilon` before either part is taken.

A second exact form uses the one-sided Skorokhod contacts. If

```text
sigma_m=max_(k<=m)(-b_k^star)_+,
lambda_j=sigma_j-sigma_(j-1),
```

then the `j`th contact is the endpoint incidence dipole from `j-1` to `X`, and

```text
prime ramp-L_down
 =sum_j lambda_j log((j-1)/gcd(j-1,X)).
```

The suffix reflection is an exact nonnegative cover with gap

```text
sum_j nu_j log j.
```

These are new exact contact-debt formulas.

## Möbius–Poisson bridge

For any correction `s=b-b0`, put

```text
gamma_m=s_m-s_(m+1),
h(q)=v_q(b)-v_q(b0).
```

Then

```text
h(q)=sum_(kq<=X) gamma_(kq),
gamma_m=sum_(k<=X/m) mu(k) h(mk),
s_m=sum_(n>=m) gamma_n.
```

For the canonical Green state, this defines the complete all-integer extension
of the prime-power residual before quotient-cell analysis. It is the exact
bridge between the carry Möbius decoder and the adjacent-flow/Green geometry.

## New full proposal

Define

```text
C_X=J(seed)-L_GS.
```

The Green–Dipole Sharpness theorem is

```text
(C_X)_+ = X^o(1),
```

or the stronger finite inequality suggested by reconnaissance,

```text
L_GS>=J(seed).
```

Since

```text
J(seed)>=4 sqrt(X)-O(log X),
L_GS<=prime ramp,
```

the theorem gives the critical prime-ramp lower bound and RH through the
reviewed square-screw/Landau transfer.

The proposed construction of `GDS` is the Contact-Cell Descent certificate:

```text
exact Green orthogonal purge
-> exact two-moment cell balayage
-> physical negative-excursion layer cake
-> signed endpoint dipoles
-> complete quotient-cell Möbius recombination
-> bounded same-scale prime-power cluster solve
-> factor-two child descent
-> nonexpansive contact recurrence
-> polylogarithmic debt.
```

This is intended as a physical positive-cone realization of PR #240's open
`SGQB(K)` barrier.

## Exact regression

`X-26201` uses only integers and `fractions.Fraction` for its proof layer. On
a rational `X=12` control it verifies:

```text
endpoint-projected Green solve
exact equality on 8 prime-power rows
11 Möbius–Poisson decoder rows
negative-excursion layer cake
signed incidence dipoles
clipped lower/upper formal-log identities
prefix and suffix contact-debt identities
9/9 mutation/interface tests
proof SHA-256
5941277ae1d4435a1e57ab72c7cde8edadd0aed3fef5061b0618e07f898672ea
```

The checker certifies finite algebra only.

## Reconnaissance

Ordinary NumPy binary64 reconnaissance was run at

```text
X=50,100,200,500,1000,2000,5000,10000,20000.
```

At every retained level:

```text
L_GS-J(seed) > 0.
```

At `X=20000`:

```text
Green rank                    2328
negative coordinates           117
negative support       19869..20000
minimum b^star          -0.00287547
clipped total gap         0.502045
L_GS-J(seed)              4.922483
prefix contact debt       0.026225
```

The Green equality replay radius was about `1.8e-10`. These are discovery
values, not certificates.

## Exact remaining theorem

The branch is ready for review of its exact algebra, but the conclusion-producing
statement is still:

```text
GDS / CCD.
```

A proof must show that the aggregate contact-cell debt is polylogarithmic or
subpower. It may use the PR #240 `SGQB` identity, but it must also prove
physical positive-cone closure and include every endpoint, floor transition,
and fixed-ratio Mertens mutation.

## Status

```text
Möbius–Poisson factorization             PROPOSED EXACT
Green clipping / signed dipole ledger    PROPOSED EXACT
Skorokhod contact debts                  PROPOSED EXACT
exact finite checker                     PASS
GDS / CCD                                OPEN, RH-BEARING
RH                                       NOT PROVED
```
