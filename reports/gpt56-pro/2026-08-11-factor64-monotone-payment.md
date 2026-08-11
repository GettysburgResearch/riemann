# Factor-64 continuation: the 51-state debt collapses to upward occupation variation

**Date:** 2026-08-11  
**Status:** exact finite theorem proposed for independent review  
**RH:** unproved

## Result

The factor-64 uniform-Pascal reward `d_64` is negative exactly on states `13,...,63`, but all cumulative sums

\[
D(M)=\sum_{m=2}^M d_{64}(m)
\]

satisfy

\[
\frac9{10}<D(M)<\frac{21}{10}.
\]

Therefore every finitely supported nonnegative nonincreasing occupation pays the entire signed reward:

\[
\sum_m d_{64}(m)M(m)\ge\frac9{10}M(2).
\]

For a general nonnegative occupation,

\[
\sum_m d_{64}(m)M(m)
\ge\frac9{10}M(2)-\frac65
\sum_m[M(m+1)-M(m)]_+.
\]

Thus the previous 51-coordinate payment target is reduced to one scalar upward-variation bound. The sufficient condition is

\[
\sum_m[M(m+1)-M(m)]_+\le\frac34M(2).
\]

## Significance

This does not prove the critical occupation bound. It identifies exactly what the factor-64/Pascal bridge still consumes: not arbitrary signed Cycle Debt, but control of upward variation in the explicit uniform-Pascal Green occupation.

## Verification

```text
PASS_X_90701_FACTOR64_MONOTONE_PAYMENT
```

The replay rebuilds the polynomial coordinates, finite block sums and all prefix bounds in `Q(sqrt(2))`, with the directed enclosure

\[
707/500<\sqrt2<283/200.
\]
