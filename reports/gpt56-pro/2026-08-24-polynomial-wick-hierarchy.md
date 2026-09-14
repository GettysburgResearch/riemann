# Report — square-root polynomial Wick hierarchy

## Why this route was selected

PR #742 proves that the deposited pointwise converse-Rolle pricing loop cannot
beat its own two-thirds baseline: the rung-zero self coefficient is at least
`8/5`. Its named exit is distributional pricing.

PR #726 supplies exactly such a distributional route: full confluent
Cauchy-index descent plus a degree-two triangular source congruence giving a
conditional `92.10%` theorem. The apparent limitation was that the
degree-two construction looked isolated and depended on a finite nilpotent
projection.

## New synthesis

The degree-two polynomial `1-x/2-x^2/8` is the second truncation of
`sqrt(1-x)`. Every truncation `P_K` has:

1. exact cancellation of source degrees `1,...,K`;
2. a coefficientwise nonnegative residual quotient `P_K^2/(1-x)`;
3. source-algebra inverse norm at most `4^K/binom(2K,K)=O(sqrt K)`;
4. superfactorially decaying frozen residual energy;
5. a contractive half-line Dirichlet-shift realization on every right safe line;
6. power-saving omitted-prime stability for growing degree.

The resulting implication lattice is:

```text
PWXFER(K=2) with 99/101 transfer
        -> 92.102816...% on the line

PWXFER(K) for every fixed K
        -> model reserve tends to one
        -> density one for zeta zeros on the line

density one + an independent zero-free exceptional-set theorem
        -> possible later RH route
```

The last arrow is not supplied here. Density one itself is not RH.

## What remains

The actual Xi compression must realize the source congruence with asymptotically
lossless trace and Hilbert-Schmidt comparison. The remaining terms are now
only:

- archimedean freezing;
- horizontal contour caps;
- smooth-taper/physical frame transfer;
- companion/pole and endpoint ledgers.

Polynomial invertibility, finite projection nilpotence, and the arithmetic
safe-line tail are no longer open.
