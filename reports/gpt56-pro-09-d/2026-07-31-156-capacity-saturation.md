# Capacity inequality audit and exact saturation replacement

Agent: `gpt56-pro-09-d`  
Date: 2026-07-31  
Issue: #156  
Base: counted inverse-Ritz branch / PR #161

## Executive result

The requested inequality

```text
D(a,t,Gamma) <= C(a,epsilon)
```

cannot be obtained as an ordinary comparison between an upper symbol count and a
near-radical capacity.  For every `epsilon<t<Gamma`, min--max already forces

```text
C <= N_A(t) <= N_A(Gamma) <= D.
```

Thus the desired reverse inequality means exact equality throughout.  It is a
low-index saturation theorem.

## New proof layers

### L-15603 — index sandwich

A `C`-dimensional packet whose compression lies below `t` creates at least `C`
eigenvalues below `t`.  Any certified upper count below `Gamma` lies above the
actual count.  Therefore `D<=C` is possible only when the packet captures the
entire low spectral index and `[t,Gamma)` is empty.

### L-15604 — finite saturation

Let `U` be the complete symbol-selected packet and `L` the exact radical packet.
Set

```text
W=L+U
V=W intersect L^perp
E=W^perp.
```

A symbol theorem supplies an outer floor on `E`.  One finite robust Schur
complement on `V` then proves

```text
A|L^perp >= Gamma.
```

This returns the sharp count `D_sat=dim L`.  No principal angle between `L` and
`U` is needed.

### L-15605 / L-15606 — capacity and plunge deficit

Imposing `r` exact source constraints costs at most `r` dimensions in any
uniformly concentrated source packet.  The Connes--Consani source loses at most
two dimensions, and only one in a self-dual sector.

When the count and capacity are built from the same concentration operator, the
possible surplus `D-C` is at most the plunge count plus this finite codimension.
The newest one-dimensional localization results make that mismatch
logarithmic or near-logarithmic rather than bulk-sized. They do not prove its
arithmetic sign.

### L-15607 / L-15608 — scalar leverage and trace-tail saturation

For the exact lower symbol `s` and packet `L`, define

```text
c_L(xi)=||(I-P_L)e_xi||^2/(2*pi)
D_L(G)=integral c_L(xi)(G-s(xi))_+ dxi.
```

Then

```text
A|L^perp >= [G-D_L(G)] I.
```

The scalar inequality `D_L(G)<=G-Gamma` proves exact saturation. Moreover,
with `T_G=P_I F^-1(G-s)_+ F P_I`,

```text
D_L(G)=Tr((I-P_L)T_G).
```

Thus the optimal unconstrained rank-d packet has deficit equal to the eigenvalue
tail `sum_(n>d) theta_n(T_G)`, while exact source constraints can be imposed and
replayed by a finite rational nullspace/Gram trace calculation.

### T-15602 — cofinal theorem

If the packet compression and complete residual obey

```text
-alpha G <= B <= alpha G
R <= beta^2 G,
```

and exact saturation holds, then

```text
F = -(3 t alpha + alpha^2 + beta^2)/(t-alpha)-delta.
```

The rates

```text
alpha -> 0
alpha/t -> 0
beta^2/t -> 0
delta -> 0
```

imply `F->0-`, even when `t->0`.  The cofinal lower-envelope theorem then gives
RH.

## Exact regression

The retained synthetic operator is

```text
A = [[0,0,1/100],
     [0,0,0],
     [1/100,0,1]].
```

For `L=span(e1,e2)`, `t=1/4`, and `Gamma=1/2`, the packet is strictly below `t`
and its exact complement is above `Gamma`; hence both spectral counts equal two.
With `q=-1249/313`, the inverse-Ritz moat has exact pivots

```text
1/5000, 3/5008
```

and certifies

```text
inf spectrum(A) >= -3/4996.
```

Nine adversarial tests pass.

## Remaining theorem

The remaining zeta-specific statement is not a rank asymptotic.  It can be
expressed either as:

1. cofinal positivity of the finite evaluation-visible Schur block after every
   repairable radical-like direction has been moved into `L`; or
2. the scalar weighted trace-tail bound
   `Tr((I-P_L)T_G)<=G-Gamma` for exact repaired packets.

Recent localization results improve the source-packet and symbol-packet size
estimates, but do not prove either arithmetic cofinal bound.

## Status

- New claims are `PROPOSED`.
- Exact checker results are synthetic finite algebra.
- No production localized-Weil saturation packet exists.
- RH is not claimed proved.
