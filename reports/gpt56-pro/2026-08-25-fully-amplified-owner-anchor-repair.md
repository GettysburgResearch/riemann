# Fully amplified owner/anchor repair

Date: 2026-08-25  
Execution PR: #751  
Programmes: #743, #736, #737  
Parent: PR #719 at `ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`  
Status: **binding correction and exact normal form; off-diagonal moments open**

## Correction to the first T-106090 checkpoint

The fixed-`Q` local family theorem was valid, but the first proposed global
moment separated opposite owner products and paid them by a scalar Cauchy
weight `Q`.  That weight cancels the fixed-fibre reciprocal `1/Q`; summing the
result counts owner fibres rather than summing their reciprocal source mass.

`R-106095` makes this failure binding.  No scalar power `Q^theta` repairs it:
the dual sum wants `theta>=1`, while the weighted diagonal wants `theta<=0`.

## Correct fully amplified member

For fixed common core `g`, least discrepancy prime `ell` and owner quadratic
class `sigma`, the corrected member sums both coherent dimensions before
squaring:

```text
left:
  every anchor (c,P,...);

right:
  every opposite owner/core atom (Q,d,...).
```

The scalar phase member is

```text
Z_tilde_(g,ell,sigma,h)(t)
 = sum_anchor conjugate(A_anchor(t))
     sum_(Q,d,...) b_(Q,d,...)(t) e_ell(-h Q g^2 d^2).
```

Within one quadratic class, `Qg^2=u_sigma*r_Q^2`, so the multiplicative
family sees the combined variable `r_Q*d`.  This gives an exact even-character
family despite varying `Q`.

## Correct moment

The source-dual weight is now

```text
g^2 * ell,
```

with no separate `Q` weight.  The dual index sum

```text
sum_(g,ell) 1/(g^2*ell)
```

is polylogarithmic.  A subpower bound for the corrected moment therefore
controls the exact least-discrepancy current and `BCI102990`.

## Diagonal progress

`L-106096` pays the literal atomic diagonal.  If

```text
c=ell*m,
ell<P^-(m),
```

then the diagonal factor `ell^2/c^2` is `1/m^2`; summing possible `ell` for
one `m` costs at most `m`, leaving a harmonic sum.  Reciprocal common-core and
owner weights are then summable/polylogarithmic.

Only genuine cross-incidence terms remain:

```text
different left anchor;
different opposite owner/core atom;
or both.
```

## Live two-statement conjunction

```text
FAPCX106100:
  off-atomic-diagonal principal fully amplified moment;

FANEX106100:
  off-atomic-diagonal nonprincipal even-family moment.
```

Their conjunction implies the corrected total moment, `BCI102990`, and the
frozen detector chain.  Neither premise is proved.

## Function-field target

The function-field mirror must also amplify owners and cores before taking the
family square.  A fixed-owner Kummer estimate is only local.  `FFFA106100`
asks for the complete off-diagonal Artin--Schreier/Kummer moment, its constant
and resonant constituents, and an exportable number-field trace theorem.

## Status

```text
least-discrepancy source coordinate       proved exact;
fixed-Q local family                      proved exact/long-core;
first Q-weighted global moment            corrected by R-106095;
fully amplified family                    proved exact;
literal atomic diagonal                   proved subpower;
principal/nonprincipal cross-incidence    open;
BCI102990                                 open;
RH                                        unproved.
```
