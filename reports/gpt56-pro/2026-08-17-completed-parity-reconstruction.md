# Completed-parity T-96500 reconstruction report

## Executive verdict

The missing mathematical packet was reconstructed from the exact heads of PRs
#559, #561, #567, and #568, together with the earlier T-96400 proposal and the
annular PR #556 input.  The candidate-complete claim does not survive.

The decisive new reconstruction result is the distinction between two edge
normalizations:

```text
row-2 exactness  -> row 3 gains by monotone rho;
5:3 scalar exactness -> row 2 loses and row 3 gains in ratio -3:5.
```

The former response used the first coefficient while naming the second
coupling.  Independently, the PR #561 odd-history target witness blocks the
leafwise edge before row lifting.

## New exact advance

After complete parity expansion, the scalar common-source problem at each fixed
endpoint is a finite fractional-knapsack/Lorenz LP.  Its optimum and dual are
explicit.  This replaces the vague “all-depth scalar Hall” phrase by one exact
finite inequality and one exact separating threshold.

## Status

```text
complete claim                         withdrawn
new exact algebra and LP reduction     proved
uniform Lorenz inequality              open / RH-bearing
RH                                     unproved
```
