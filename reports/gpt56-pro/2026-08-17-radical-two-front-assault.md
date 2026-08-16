# Radical two-front assault: compact complete-gap annulus and one reciprocal-zeta row

Date: 2026-08-17  
Base: PR #544 at `d4dcd1256dc9c8e110c860cff87b3f89aee842a5`  
Status: exact new reductions and bridges; RH unproved

## Executive result

The normalization firewall of PR #544 remains binding: affine–Volterra packing controls `P_Lambda-H`, while the complete arithmetic gap `F_Lambda=J_Lambda-P_Lambda` remains independent.

This packet attacks both honest fronts with smaller objects.

### Front A: compact annular complete-gap quadrature

For every fixed `h>0`, the scaled second difference of

`Y(t)=-exp(-t/2) F_Lambda(exp t)`

has the exact nonnegative tent kernel

```text
v exp(-v/2)                 0<=v<h,
(2h-v) exp(-v/2)            h<=v<2h,
0                            v>=2h.
```

Thus all arithmetic outside one multiplicative annulus cancels exactly. Its Mellin multiplier is `(1-exp(-hs))^2`, which is nonzero in `Re s>0`. A polylogarithmic bound for this one annular quadrature discrepancy proves RH.

### Front B: one scalar row

The combination

`R_X=5c_X(2)+3c_X(3)`

has positive unsieved base dictionary

`15,6,3,6,6,...`

and exact Mellin numerator

`-3(2^(-z)-1)(2^(-z)-2)`.

It is zero-free throughout the open strip. Eventual positivity of this one scalar proves RH. This strictly improves the two-row producer of PR #546.

### Universal reciprocal state

The combined infinitesimal profile `5p_s(2)+3p_s(3)` is explicitly piecewise affine in `s^(-1/2)` and strictly positive for every `s>2`; the physical profile itself has no remaining sign obstruction.


The scalar row is a positive smoothing of

`V(x)=sum_(d<=x) mu(d)d^(-1/2)log(x/d)`,

whose transform is `1/[s^2 zeta(s+1/2)]`. The same state is connected to the Volterra density by

`(D-1/2)L = D(D+1/2)V`.

The exact affine-cell source target is only a two-moment cone and permits the Volterra density to change sign.

## Exact open producers

```text
ACTQ_h   compact-annulus complete-gap quadrature bound
SPRP     positivity of 5c_X(2)+3c_X(3)
VRP      eventual positivity of the universal reciprocal Riesz potential
AMCP     signed affine-cell moment-cone inequalities
```

Any of the first three closes RH through a frozen exact consumer. None is proved in this packet.

## Exact replay

```text
PASS_T96300_RADICAL_TWO_FRONT_ASSAULT_ALGEBRA
fa2cacdc80a74b9bf8d7a1fe9fe561b2aa898184e590ae9ca0b2fa0f6ca57d18
```

The replay checks exact finite and formal algebra only and fail-closes on every producer or RH promotion.
