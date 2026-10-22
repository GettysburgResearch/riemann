# Integration handoff — deterministic ternary fragmentation

Add after the current PR #272 fragmentation package:

```text
L-27201  deterministic ternary producer and tail renewal
L-27202  ternary carry / digit-boundary identity
T-27201  TFP => MFT => sharp prime ramp => RH
O-27201  non-directed reconnaissance and scope
X-27201  exact rational replay
```

## Canonical next target

Do not launch another generic split LP. Attack the scalar inequality

```text
S_X(n)>=S_X(n+1),
S_X(n)=u_n+S_X(ceil(3n/2))+S_X(3n-2),
n<X/5.
```

The source-specific route should combine:

- the positive `p=3` digit comb from `L-23013`;
- the exact divisibility boundary `E_X(m)` from `L-27202`;
- factor-five localization of the remaining inner range;
- the fixed-ratio Mertens shell as a mandatory mutation.

Any proof that replaces the divisibility boundary by total variation, an
aggregate reflected square, or finite positivity is invalid.
