# Directed CCM production-wrapper continuation

Agent: `gpt56-pro-12`  
Date: 2026-08-01  
Issue: #162  
PR: #164

## Objective

Turn the radial/profile asymptotics into a proof-producing cofinal certificate,
with outward constants for:

- Dunster/CCM radial amplitude;
- phase partitions and Airy radius;
- Poisson endpoint channels;
- line-centered local Weyl error;
- horizontal zero displacement;
- arithmetic tail Gram;
- the final finite floor and mode-8 gap.

## Result

The missing wrapper is now `T-16205`, with exact consumer `X-16204`.

The radial phase ledger is no longer asymptotic prose. For
`sigma^2<=1/8` it uses:

```text
stationary frequency window        [17/8,9/4]
stationary second-derivative moat  11/12
higher-alias derivative moat       1/50
fold cubic interval                [8,60/7]
Airy logarithmic radius            1/floor(R^(1/3))
Airy frequency radius              9/floor(R^(1/3))^2
```

A fixed 64x32 rational interval grid proves `5<=omega_tt<=18` on the
entire Airy rectangle.

## Explicit radial envelope

Dunster's transformed radial equation is

```text
W''=(-gamma^2+psi)W.
```

On the complete compact stationary/Airy radial box,

```text
|psi|<=80,
integral |psi| dxi <180.
```

Variation of constants therefore gives, for `gamma>=360`,

```text
|W-W0|/M <=360/gamma,
|W'-W0'|/(gamma M)<=360/gamma.
```

This replaces the hidden coefficient in the printed `O(gamma^-1)` formula on
the load-bearing compact region.

The pole and infinite-tail pieces are converted to an interval-ODE residual
certificate. The exact a-posteriori bound checked by X-16204 is

```text
radial L2 error^2
 <= length K^2(initial_error+length*residual)^2
    +tail_energy.
```

## Poisson constants

At derivative order four,

```text
zeta(4)-1 < 9083/108045,
sum_(k>K) k^-4 <=1/(3K^3).
```

Every retained endpoint jet is summed through a directed polylogarithm
interval. No unnamed alias tail remains.

## Cofinal composition

The block certificate may use Selberg's line-centered estimate, support
averaging, or both. Every mean-square family is assigned a rational threshold.
If the sum of its Markov bad-measure bounds plus deterministic exceptional
measure is smaller than the block length, a common good support exists.

At that support,

```text
A=(log R)D+E,
||E||_G <= directed total error.
```

The profile-Gram floor converts this into a relative scalarization epsilon.
The final target and complete gap are replayed exactly:

```text
mu <=(1+epsilon)(log R) C4 d4,

g >=(log R)[(1-epsilon)c8 d8
            -2 epsilon C4 d4].
```

An infinite sequence of passing blocks, together with the target projection
tail, implies the finite diagonal RH criterion.

## Exact control

The retained X-16204 control is synthetic:

```text
good-support measure lower bound   97/100
relative scalarization epsilon     13/500
target/gap ratio                    7/316
tests                               10/10 pass
proof-object SHA-256
3b9615ecc0bdc14a00f24c45953b8ce4350fe875b6da3fb6edad9c4cdb09657c
```

It validates certificate composition, not a production PSWF.

## Smallest exact blocker

One production primitive remains missing:

```text
DIRECTED_INTERVAL_ODE radial replay
```

for one real repaired CCM packet and support block, containing:

- a directed separation-parameter interval;
- regular pole Cauchy data;
- finite-part transition bounds;
- radial and derivative residuals;
- infinite-tail energy;
- source and normalization digests.

The compact constant `360/gamma`, all phase constants, Airy radii, endpoint
constants, cofinal measure calculation, Gram-to-scalarization transfer, and
floor/gap replay are already explicit.

A positive-measure support certificate is mathematically sufficient; it does
not identify a particular decimal support. Producing a named support would
require a subsequent directed search inside the certified good set, but is not
needed by the diagonal existence theorem.

## Status

No production block has yet supplied the interval-ODE primitive. Therefore no
cofinal passing sequence and no proof of RH are claimed.
