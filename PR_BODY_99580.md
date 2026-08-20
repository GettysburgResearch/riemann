## Purpose

Directly attack IHR67 on frozen PR #649 at
`433fd3662f7b2e4ba384ce64f196380e88624090`.

**RH remains unproved.** The attempted proof produced an exact stop-loss
reduction and sharp no-go results, not a valid global sign proof.

## Results

```text
IHR67 relative-persistence identity       proved exact
critical finite-difference identity       proved exact
off-line zero -> two-sided oscillation    proved exact
generic duplicate-label positivity       refuted exactly
positive-symbol shortcut                  rejected
positive-renewal shortcut                 rejected
prime-log stop-loss coupling              open / RH-bearing
IHR67                                     open / RH-bearing
RH                                        unproved
```

## Replay

```text
PASS_T99580_IHR67_STOP_LOSS_AND_OSCILLATION_ATTACK
```

The replay is standard-library, exact at the finite algebraic scope, and
records `ihr67_proved=false` and `rh_established=false`.
