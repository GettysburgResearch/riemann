# Third checkpoint: one fixed window, one signed scale integral

**PROPOSED COMPONENT PROOFS. The decisive arithmetic covariance estimate remains OPEN. No new fourth/sixth moment, 17/24 half-plane, or RH proof is claimed.**

This continues PR #916 at `8d49acb264577f63374358c33636ebe8e05ccf70`. Earlier packets and sibling branches are preserved. Start with [the complete proof](INTEGRATED_CRITERION.md); the [new-sieve audit](OPTIMAL_SIEVE_AUDIT.md) records the separate arithmetic attack and why it does not close the remaining gap.

## What is new in this checkpoint

The pointwise smaller-scale hypothesis is no longer needed. On the product measure of the complete fixed row set and logarithmic scale, the exact inverse kernel gives

\[
(1-q)^2\mathcal I_M(D;H)\le\mathcal I_B(D;H)
\le(1+q)^2\mathcal I_M(D;H),\qquad q\le1/3.
\]

Here the two quantities are weighted scale integrals of the higher moment and the balanced coprime mean square. Holder is applied jointly in row and scale, and shorter dilations stay inside the same finite horizon. No separately assumed unequal-length estimate or scale supremum occurs.

The classical dyadic uniform-convolution window, used in logarithmic coordinates, has

\[
\widehat W_*(s)=\prod_{j\ge1}\frac{\sinh(2^{-j}s)}{2^{-j}s}\ne0
\quad(\Re s>0).
\]

Thus ONE fixed, nonnegative, compact C-infinity window suffices for every prospective zero. Its classical origin is credited and its needed properties are proved explicitly.

For that window the full integrated diagonal is proved to be O(H). A one-sided upper bound for the exact signed off-diagonal, of size D^(h+lambda+epsilon) with H=D^h, implies the conditional boundary

\[
\Re s>\frac12+\delta+\frac{\lambda+5h/6}{2k}.
\]

The prime-extraction step has an exact weighted-norm proof with no one-shot omitted-prime error or moving-prime constant. Letting fixed delta tend to zero recovers 17/24, 23/36 and the all-order frontier CONDITIONALLY. For zeta alone the logical criterion needs only the principal Hecke target over Q(sqrt(-3)); it does not presume that proving the criterion avoids auxiliary families.

## A newer sieve was tried, not silently assumed to solve the problem

De Faveri's October 2, 2026 Theorem 1.1 gives a stronger sixth-power-free large sieve. The supplied all-row adapter improves the generic balanced row/column envelope from T^(4/3) to T^(7/6). However, at the high-moment product length its sixth-power-replica term still returns boundary 1. A genuine prime-supported arithmetic example proves that this term cannot simply be deleted from an arbitrary-coefficient theorem. The required cancellation must use the actual Mobius/divisor coefficients.

## Scope and evidence

The main reduction is independent of the new external sieve and of the imported quasi-RH theorem. The external sieve is a cited input, not independently rebuilt here. Normal and optimized execution both reconstruct **32,082 exact finite predicates**, reject **three** false identities, and agree byte for byte. A separately tampered result file is rejected. These are rational/cyclotomic free-monoid fixtures, NOT actual Hecke moment samples and NOT an infinite analytic certificate.

See [validation and source scope](VALIDATION_AND_SOURCES.md), [checker](check_integrated_window.py), [recorded output](result.json), and [manifest](MANIFEST.json).

**Exact remaining gap:** `INTEGRATED_CRITERION.md` (7.6), the one-sided signed integrated covariance bound, with useful excess lambda. The row range is the same H=D^h at every scale within the integral; replacing it by X^h is not justified.
