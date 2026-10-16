# Exact exponent reconstruction and a restricted Cauchy ceiling

Status: exact rational bookkeeping and a PROPOSED elementary implication
about the stated exponent model. Not a lower bound on the arithmetic sum.
Sources: Cureton--Thorner v2 Sections 5.6, 9, 10, 13 and Table 1.

Set alpha=67/100, beta=151/400, h=1-alpha=33/100,
M=alpha+beta=419/400, C=alpha/2+h/6=39/100, b0=1-C=61/100.
The additive factor has square norm O(1/Y+1/X), which is O(1/Y) for
beta<=alpha. The reflected theta square norm on the full support is
O(Z^(2M-1+epsilon)), with M>1. Consequently Cauchy gives

    E_theta=M-1/2-beta/2=287/800,
    b0+E_theta=31/32,  C-E_theta=1/32.                    (1)

For the Poisson side the exterior exponent is

    E(x,y,z)=alpha/2+x-1+h*z+beta*(y-1).                  (2)

The checker reconstructs all seven Table 1 savings from (2), the exact
contours and exact row counts; it does not merely compare two copies of the
printed fractions. The least Poisson saving, less the declared 1/4000
loss budget, is greater than 63/2000, which is greater than 1/32. Hence the
current binding estimate is the theta-side Cauchy bound, not a missing
last decimal in the final Poisson comparison.

## Restricted architecture proposition

Suppose the same two positive mean-square estimates are used, in the regime

    0<beta<=alpha<1,  alpha+beta>1.

Keep h=1-alpha and the same principal-residue reference
C=alpha/2+h/6. The saving obtainable by their Cauchy combination is

    Delta=C-(alpha+beta/2-1/2)=2h/3-beta/2.                (3)

Because alpha+beta>1, beta>h. Because beta<=alpha and alpha+beta>1,
alpha>1/2 and h<1/2. Therefore

    Delta<h/6<1/12.                                      (4)

The ceiling 1/12 is a supremum: take h=1/2-t, alpha=1/2+t,
beta=1/2, t -> 0+. Thus these particular positive estimates cannot by
parameter tuning alone yield a zero-free boundary at or below 11/12.
The OTHER contour constraints may impose a worse ceiling; satisfying (4)
does not prove that a near-11/12 parameter choice is feasible in the paper.

This is not a universal obstruction to theta methods, signed bilinear
estimates, M<=1 regimes, or a different reflected norm bound. It does not
assert the Cauchy bound is attained by the actual arithmetic. It identifies
which inequality must change for a substantial improvement.

## What would change the model

A direct signed estimate for the pairing between the additive and transformed
theta factors could beat their product of L2 norms. It would need to survive
all common-prime terms and be valid for the very same fixed weights that
produce the principal reciprocal. Alternatively a genuine higher native
moment can use FIELD_MOMENT_BRIDGE.md rather than this scalar Cauchy model.
The new source in EULER_STRIPPING.md is a candidate for a reworked transform,
not a bound for that signed pairing.
