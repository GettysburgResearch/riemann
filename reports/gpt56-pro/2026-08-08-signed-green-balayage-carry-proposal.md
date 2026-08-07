# Signed Green–balayage recovery of the Carry Sandwich route

Date: 2026-08-08  
Agent: `gpt56-pro`  
Issue: #238  
Branch: `agent/gpt56-pro/238-carry-packing-minorant`  
Status: full proposed architecture; `SGQB(K)` open; RH not claimed proved

## 1. Why the former two-contact proposal is no longer load bearing

The later fourth-pass review correctly identified the defect in the former
closing theorem:

```text
one scalar affine interval has two endpoints
```

does not imply

```text
the complete arithmetic source has only two free coordinates.
```

The PR #239 same-sign Möbius cube supplies arbitrarily high arithmetic rank in
one fixed-ratio shell. No complete `K=6`, `K=8`, or symbolic source dictionary
proved the old `2/K` exponent. The branch therefore retains the old files as
history but removes them from the proof spine.

The replacement begins from two later exact observations:

1. the canonical Green correction already solves every carry constraint in
   signed coordinates;
2. constant carry blocks transport ordinary-prime residual mass exactly, with
   objective equal to its logarithmic moment.

The remaining problem is scalar debt transport, not contact enumeration.

## 2. Exact breakthrough: high-rank residuals are free off the logarithmic mode

Let `G` be the endpoint-projected divisor Dirichlet Gram, `lambda` the
von-Mangoldt/logarithmic vector, and `r` the complete signed residual. Put

```text
E       = lambda^T G lambda,
delta   = lambda^T r,
r_perp  = r-(delta/E)G lambda,
T_perp  = G^-1 r_perp.
```

Then exactly

```text
new residual       = (delta/E)G lambda,
objective change   = 0,
Green energy       = delta^2/E + <r_perp,G^-1 r_perp>.
```

Thus every high-rank direction orthogonal to the one logarithmic scalar can be
removed exactly, regardless of its Green energy or arithmetic dimension.

This directly survives:

- the rank-`K` same-sign Möbius cube;
- a zero reflected Schur reserve;
- the failure of nonnegative monotone covering.

It does not solve the scalar `delta`; it isolates it honestly.

## 3. Exact breakthrough: zero-cost signed cell balayage

For a complete signed residual in one ordinary-prime logarithmic cell, retain
its total mass `M` and logarithmic moment `L`. There is a unique measure on the
two cell endpoints with those two moments.

Using exact constant carry blocks, every interior residual can be transported
to those endpoint charges with zero total objective cost. The construction is
signed and works for arbitrary source rank.

The two endpoints are therefore **aggregate moment coordinates**. They are not
a claim that the source face has two arithmetic variables. This is precisely
what the previous proposal lacked.

## 4. New load-bearing theorem: `SGQB(K)`

After complete signed recombination, Green neutralization, and cell balayage,
let `Gamma_(K,X)` be the aggregate boundary residual. The proposed Signed Green
Quotient Barrier is an exact source identity

```text
Gamma_(K,X)
 = sum_nu c_(nu,X) Lift_(nu,X) Gamma_(K,Y_nu)
   + G_X z_X
   + e_X,
```

with

```text
Y_nu <= X^(1-eta) exp(O_K(1)),
c_(nu,X) >= 0,
sum_nu c_(nu,X) <= polylog_K(X),
lambda_X^T G_X z_X = 0,
lambda_X^T e_X <= polylog_K(X).
```

The source maps must be explicit and preserve the scalar normalization. Pairing
with the logarithmic coordinate yields

```text
(delta_X)_+
 <= polylog_K(X)
    [1+max_(Y<=X^(1-eta)exp(O_K(1))) (delta_Y)_+].
```

One fixed order and one fixed reserve imply zero polynomial exponent by strict
scale contraction.

This is materially stronger than the old contact theorem:

- no `X^(C/K)` loss;
- no limit `K->infinity`;
- no rank or face count;
- no positive Schur reserve;
- no full Green-energy estimate;
- no generic BTP norm;
- no nonnegative cover.

## 5. Proposed production proof

1. Form complete quotient layers before any positive part.
2. Choose Euler variables only by frozen-complement conditions.
3. Remove every logarithmically orthogonal source direction by the exact Green
   correction.
4. Balayage each complete cell to its two aggregate moments.
5. Join adjacent cells before estimating endpoint charges; common endpoints
   cancel exactly.
6. Route a cell with one complete macroscopic lattice through high-order Euler.
7. Route every other exposed product to a strict lower endpoint.
8. Retain only genuine outer boundaries, floor transitions, and the fixed-ratio
   Mertens shell in the polylogarithmic boundary ledger.

The high-rank cube is a mandatory mutation throughout this process.

## 6. Full RH composition

The parabolic seed has ordinary-prime objective

```text
J_seed(X) >= 4 sqrt(X)-O(log^2 X).
```

Its scalar debt is

```text
delta_X = J_seed(X)-P_X.
```

`SGQB(K)` gives `(delta_X)_+=X^o(1)`, so

```text
P_X >= 4 sqrt(X)-X^o(1).
```

Proper prime powers cost only `O(log^2 X)`. The complete prime-power ramp
therefore has the same lower bound. At square endpoints the zeta screw has a
subpolynomial upper envelope, and the reviewed square-sampling/Landau transfer
excludes every zero to the right of the critical line. Functional-equation
symmetry gives RH.

## 7. Exact replay

`X-23820-green-balayage` uses only standard-library rational arithmetic. It
verifies:

```text
Green metric E                    26
scalar delta                       3
scalar Green energy              9/26
orthogonal Green energy        850/117
total Green energy             137/18
Green objective cost               0
cell total mass                     9
cell logarithmic moment            60
endpoint charges                  4,5
cell transport objective cost       0
mutations rejected                  4
```

Proof-object SHA-256:

```text
ef7ac6b1828f4215667a1c0549820ea454bb66337941497cff825d08bd5d79e0
```

The replay proves finite algebra only.

## 8. Review order

1. `L-23820-canonical-green-orthogonal-neutralization.md`
2. `L-23821-zero-cost-two-moment-signed-balayage.md`
3. `X-23820-green-balayage/verify.py`
4. `L-23822-signed-green-quotient-layer-barrier.md`
5. `T-23810-signed-green-balayage-rh-proposal.md`
6. `M-23810-signed-green-barrier-review.md`
7. PR #239 same-sign cube refutation
8. PR #254 signed constraint dipole
9. PR #248 Green/divisor-gradient interfaces
10. fixed-ratio shell and square-screw consumers

## 9. Exact status

```text
old two-contact source-count closure        withdrawn as load-bearing
Green orthogonal neutralization              proposed exact
signed two-moment cell balayage              proposed exact
exact rational replay                        passed locally before push
SGQB(K)                                       open / RH-bearing
SGQB(K) -> prime ramp -> RH                  complete conditional chain
Riemann Hypothesis                           not proved
```
