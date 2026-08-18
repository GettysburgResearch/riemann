# T98010/T98012 integration handoff

## Freeze

```text
repository: gfreund123/riemann
base PR:    #596
base SHA:   40bfd7e70521f4205e95d3960812a6cef6073c05
branch:     research/gpt56-pro/98000-zero-marginal-lorenz-collapse
date:       2026-08-18
```

## Controlling reading order

```text
L-98010  ordered scalar-to-target marginal
L-98011  zero-marginal convex collapse
L-98012  one-switch layer-cake representation
R-98010  pointwise target-prefix positivity is false
T-98011  corrected cumulative frontier; controls T-98010 on OSTP67
L-98013  upper target sandwich is unconditional asymptotically
T-98012  target-root positivity implies RH
L-98014  target-root Volterra identity
C-98010  finite-cell notation clarification for L-98014
M-98010  area-plus-slope future-prime search protocol
```

`T-98010` remains useful for its structural statements, but its listing of pointwise `OSTP67` as an open closure option is superseded by `R-98010` and `T-98011`.

## New proved results

```text
vartheta(Y)=Q_*(Y)/T(Y) is strictly increasing from 0 to 6;
every Lorenz active set is a single source-index cutoff;
lambda=0 is the global Lorenz minimum iff T_E^+<=T_O<=T_E;
all hinges have an exact one-switch target-prefix layer cake;
pointwise one-switch target-prefix positivity is false;
the upper zero-marginal target inequality holds eventually;
the target root has an exact reciprocal-zeta Mellin transform;
TRP67 -> RH is a complete conditional Landau theorem;
the target root is one Volterra storage derivative of sum mu(n)/n.
```

## Exact refutation

At `P=P_61`, `X=600`, `Y=100`, cutoff `d<6`,

\[
\mathcal T_{P_{61}}(600;100)<-14/15.
\]

Therefore no proof may require every instantaneous target prefix to be nonnegative. The cumulative hinge area is the correct object.

## Replays

```bash
python3 experiments/X-98010-zero-marginal-lorenz/verify.py
python3 experiments/X-98010-zero-marginal-lorenz/scan_target_root.py --limit 1000000
```

The first script has exact Fraction fixtures plus finite Decimal diagnostics. The second is reconnaissance and explicitly records `rh_established=false`.

## Integration status

```text
ordered marginal theorem                         candidate for canonical extraction
zero-marginal convex theorem                     candidate for canonical extraction
pointwise target-prefix refutation               candidate for canonical extraction
upper zero-band domination                       candidate for analytic review
TRP67 Mellin-Landau consumer                     candidate for hostile reconstruction
TRP67 arithmetic sign                            OPEN / RH-BEARING
cumulative one-switch profile                    OPEN
GPC67 / RBLPTE67                                 OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVEN
```

## Next integrator warning

Do not merge `OSTP67` as an open theorem target without its refutation. Do not describe the two-moment instantaneous state `(U,V)` as sufficient: `R-98010` proves that the derivative may be negative. A viable Bellman state must retain cumulative area or an exact equivalent.
