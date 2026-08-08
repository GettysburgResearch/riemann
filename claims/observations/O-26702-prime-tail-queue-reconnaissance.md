# O-26702 — Prime-tail queue reconnaissance

Observation ID: `O-26702`  
Title: The explicit parabolic prime-tail queue is small through two million and its positive-tail support moves rapidly toward zero scale  
Status: **FLOATING RECONNAISSANCE — NOT A CERTIFICATE OR ASYMPTOTIC THEOREM**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-26704`, `L-26705`; `X-26702`

## Retained data

Ordinary binary64 evaluation gives:

```text
X          Q_X                 last positive tail start
100        0                   none
1,000      1.57054462085459    3
10,000     5.82573532275636    11
100,000   13.7366868733482     53
1,000,000 28.7253203795668    347
2,000,000 35.6246037205209    601
```

At every retained level from `X=1,000` onward, the maximizing tail begins at the prime `2`; however, all tails beginning beyond the displayed final positive start are nonpositive.

The ratios

```text
last_positive_start / X
```

decrease from `3e-3` at `X=1,000` to approximately `3e-4` at `X=2,000,000`, in qualitative agreement with the proved fixed-ratio localization `L-26705`.

## Interpretation

The queue is neither the maximum point residual nor the unsigned residual mass. It is the minimal boundary charge of the exact upward prime-dipole transport. The data suggest that the continuum tail cancellation survives prime sampling much farther into the shrinking-ratio regime than the current theorem proves.

A plausible quantitative target is

```text
Q_X = O(log^A X)
```

or a half-scale recurrence with polylogarithmic forcing. Either would imply RH through `T-26703`.

## Scope boundary

The computation uses ordinary floating arithmetic and a finite endpoint range. It does not establish a rate, a sign beyond the tested levels, PTQ, the prime-ramp inequality, or RH.