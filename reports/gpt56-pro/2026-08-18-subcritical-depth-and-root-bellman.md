# Factor-67: subcritical-depth no-go and the minimal root Bellman target

## Executive result

This successor continues the newly published LAPBR correction rather than
repeating it.  The negative-layer argument extends to every even stopping depth
satisfying

```text
L(X) log(2L(X)) = o(sum_(67<=p<=X) 1/p).
```

Thus no shallow count-depth rule can close the natural rough recursion.  The
published `O(log log log X)` depth is only one instance of a broad no-go.

The pass also reconciles the scalar and Lorenz formulations.  PR #590's exact
largest-prime identity shows that eventual root positivity is equivalent to one
root-only Type-II budget `RBLPTE67`.  In PR #591's Lorenz language this is
precisely the zero hinge `D^+(0)`.  All-hinge `CPSL67` and state-wise Bellman
feasibility are sufficient but formally stronger; a two-atom target-capacity
countermodel separates them.

## Scientific boundary

```text
subcritical count-depth closure       FALSE
root scalar / zero-hinge map          EXACT
minimal root Type-II budget           IDENTIFIED
RBLPTE67                              OPEN / RH-BEARING
RH                                    UNPROVEN
```
