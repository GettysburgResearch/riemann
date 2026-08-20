## Purpose

Hostilely continue PR #669 at exact head
`898f5baa42ed3bdfe9de2794eb1d4aea5a5c26b0` and decide its final positive
surface estimate rather than renaming it as a proof.

**RH remains unproved.**

## Binding correction

The proposed positive priority flux is not subpower.  For every ordering,
prime pairs in

```text
2 sqrt(X) < p,q <= 3 sqrt(X)
```

force

```text
U_X >> 1/(log X)^3,
```

and therefore

```text
integral_2^Y sqrt(X) U_X dX/X
 >> sqrt(Y)/(log Y)^3.
```

Thus `UPBF67` is false.

## Exact repair

The first-owner identity retains a discarded even surface:

```text
native scalar = empty survival + even surface - odd surface.
```

The signed coarea is exactly the native reciprocal prefix
`sum_(n<=t) beta(n)/n`.  The pair shell above is cancelled there; changing the
priority ordering cannot remove the final signed arithmetic.

## New positive theorem

For every `-1<=c<=3`, the complete native shifted quadratic transform

```text
sum beta(n)/sqrt(n) [4 sqrt(X/n)-3+c]^2
```

is globally nonnegative.  The member `c=-1` vanishes at every activation and
gives a quadratic-to-linear descent with no signed activation atoms.
Its remaining critically weighted downward variation is exactly
RH-equivalent.

## Replay

```text
PASS_T99970_UPBF_FIREWALL_AND_BALANCED_SURFACE
46a77ea83a85b007bd964d0f2912ddf094506854034e55ca0fbaf374e1420408
```

## Boundary

```text
native priority flow                       retained exact
UPBF67 positive-flux estimate              refuted
balanced signed surface                    proved exact
shifted quadratic family                   proved all-scale
activation-free critical descent           proved exact
AFCD99970 negative-mass estimate           open / RH-equivalent
Riemann Hypothesis                         unproved
```
