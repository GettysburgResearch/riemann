# Hostile self-review of the completed-parity reconstruction

## Findings that force the downgrade

### 1. Parity does not commute away

It is correct to postpone observation until a history is complete.  It is
incorrect to infer that completed histories are canonically oriented.  The
terminal packet is swapped on every odd history, and diagonal grouping or
scalarization preserves that sign.

### 2. The ratio lemma was normalized against the wrong quantity

The monotone-ratio formula is valid under row-2 exactness.  The unique `5:3`
scalar has a different normalizing denominator.  Exact scalar matching creates
row changes in the fixed ratio `Delta_2:Delta_3=-3:5`, so one row is negative.
This is an exact algebraic refutation, not a numerical concern.

### 3. Row monotonicity cannot create target capacity

The PR #561 odd leaf fails before row lifting: the required reverse target edge
has `O_T<E_T` by more than `17`.  Any proof that invokes `rho` before resolving
this target direction is circular.

### 4. Fixed depth remains excluded

Depth two has a certified `5:3` current scalar below `-62.718`.  The asymptotic
sign alternation excludes every other fixed even depth.  No “parity squared”
variant survives grouping or scalarization.

### 5. The finite LP theorem is not the uniform inequality

`L-97302` solves the optimization problem once its atom data are given.  It does
not prove that the odd demand lies below the Lorenz curve for every endpoint.
Calling the LP formula itself a producer would merely rename the open gate.

### 6. Typed scope is explicit

The scalar Lorenz LP uses target and one scalar row.  It does not automatically
satisfy a declared-score inequality or all component rows.  Those stronger
outputs require extra LP coordinates.

## Strongest honest conclusion

The reconstruction yields a sharper and fully explicit frontier, but no
unconditional closure:

```text
CPSL67 / GPHT* / ASHP67 -> 5c_X(2)+3c_X(3)>=0 -> RH.
```

The first arrow is open.  RH remains unproved.
