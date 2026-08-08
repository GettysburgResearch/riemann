# Integration correction — prime-tail drift and squarefree collectors

## Superseded claim

Do not promote `T-27302` as a live full proposal. Its conditional implication
is correct, but `R-27302` proposes the asymptotic lower bound

```text
C_X^up >= (4(1-gamma)+o(1)) sqrt(X)/log^2(X),
```

so the asserted subpower prime-only tail charge is false.

## Retained files

- `L-27301`: ordinary-prime dual collapse;
- `L-27302`: exact proper-power-neutral Farkas dual;
- `L-27303`: exact prime-incidence greedy algebra;
- `R-27301`: annular ADF scope correction;
- all exact finite experiments.

## New canonical proposal

Use `L-27304/T-27303`:

```text
parabolic ordinary-prime benchmark
-> squarefree composite incidence collectors
-> exact proper-power neutrality
-> nonnegative objective increment
-> all ordinary-prime constraints feasible
-> sharp prime ramp
-> square-screw/Landau
-> RH.
```

The only new hinge is the all-scale Squarefree Collector Lift `SCL`.

## Mandatory provenance

A future integration must keep:

1. `R-27302`'s prime-density correction;
2. the squarefree endpoint manifest;
3. every proper-power zero response;
4. the logarithmic dual ray;
5. the distinction between finite block algebra and all-scale SCL existence.

## Current status

```text
prime-only PTC                     proposed refuted
squarefree collector algebra       proposed complete exact
SCL                                open / RH-bearing
RH                                 unproved
```
