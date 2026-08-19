# T99100 handoff — phase-locked Hermite annular frontier

Base:

```text
PR #618
2dfa73325a6402418fc64b9e554c1b13dd2b9bf1
```

Conclusion-producing chain:

```text
hypothetical rho=1/2+delta+i gamma
 -> exact high-order notch preserving rho
 -> optimal order M~2(1/2-delta)^2 T
 -> one-sided annulus log n=2delta T+O(sqrt T)
 -> phase-twisted fractional owner martingale
 -> PLHAC99100 arithmetic Carleson estimate   OPEN
 -> contradiction with pole lower rate
 -> RH.
```

Immediate hostile tests:

1. verify the differential/contour multiplier and its factor two;
2. verify the two stationary points and the optimization in `alpha`;
3. verify that the one-sided cutoff does not alter the local Hankel term;
4. verify the fractional owner probabilities and complex martingale;
5. reject any proof which replaces the fixed phase by an absolute value or a center supremum;
6. require an exponential saving strictly larger than `delta(1-2delta)T` relative to the optimal magnitude envelope.

RH remains unproved.
