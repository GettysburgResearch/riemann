# Paired-eta weighted Julia attack

Date: 2026-08-12  
Base: PR #420 at `c978fc2c0f52f67800a0542a962e49c6110a5b8f`  
RH status: **unproved**

## Motivation

The eta/dyadic route had already converted the global zeta-pole cancellation
into one compact finite-interval bridge.  Its declared surviving obstruction
was the unbounded multiplier `exp(omega y)` on the unbounded paired-eta
physical set.

That obstruction depended on insisting that the hard and safe eta states live
in one fixed Hilbert metric.

## Exact advance

For

```text
E=union_m [log(2m-1),log(2m)],
```

one has

```text
I_eta(z)=int_E exp(-z y)dy=eta_D(z)/z.
```

At exponents `sigma-omega` and `sigma+omega`, the correct source spaces have
different exponential weights.  Multiplication by `exp(-omega y)` is an exact
carrier-covariant unitary from the safe weighted space to the hard weighted
space.

Inside the hard space,

```text
m(y)=exp(-omega y),
d(y)=sqrt(1-exp(-2 omega y))
```

form an inner Julia column.  Therefore

```text
hard eta kernel
 = safe returned eta kernel
 + positive eta-detail kernel
```

on the complete carrier family.

The unbounded inverse on one fixed common space remains true but is no longer
load bearing.

## Completed factorization

Writing `I_eta=eta_D/z`, the completed horizontal Xi quotient becomes

```text
I_eta(s-omega)/I_eta(s+omega)
*[(s-omega)/(s+omega)]^2
*compact dyadic/gamma bridge
*positive gamma beta/Laplace factor.
```

The rational factor is inner, the compact bridge is already complete, and the
gamma factor has an explicit positive Laplace source.

Thus all arithmetic source factors are now explicit and positive.

## Hostile firewall

The source identity does not prove that the analytic quotient is Schur, and a
positive arithmetic source does not prove exhaustion by the critical and
stable model outputs.  The remaining theorem is genuinely a canonical
source-to-model colligation.

## New final target

`PEJGOC_omega` asks for that colligation with the exact eta, compact-bridge,
rational and gamma factors retained coefficient one.  Exhaustion by critical
and stable outputs deletes the hyperbolic port.  A sequence `omega_j -> 0`
would prove RH.

## Current judgment

This route has improved materially: neither the free pole nor the paired-eta
tail is now an unbounded source problem.  The remaining difficulty is common
to the other routes—the exact arithmetic source-to-model identification—rather
than a representation-theoretic divergence.
