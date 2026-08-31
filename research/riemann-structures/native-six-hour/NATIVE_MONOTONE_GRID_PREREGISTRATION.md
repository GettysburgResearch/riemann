# Preregistered complete monotone-grid source campaign

The source is the same original H25 half-source on primes2,3,5,
all63 ordered factors and45 physical ratios, actual2ds and the original
Mellin measure. The exact physical Gram, cross terms and reference
energy are pinned to the affine-source discovery
`46c8453e3976d242479202bf4d58489282a64d2a`.

The first discovery exhausts every monotone axis path on gridsN=2 and3:
90 and1680 paths respectively. Each coordinate makes exactly N steps
of length1/N; all words in the multiset with N copies of2,3,5 are
enumerated lexicographically. The executable and calibration data are
then frozen. The heldout run uses that same executable for N=4,
all34650 words, without changing the metric, path class, scoring,
candidate policy or arithmetic after calibration.

For x=(A,B,C/2,D,E,F) the common integer denominator is2N^3. At a
state(k,l,m), a u-step increments its numerator vector by

    (2Nl, l(2k+1), l^2, 2Nm, m(2k+1), 0);

a v-step increments only F by2Nm; a w-step adds no occupation
coordinate. All source endpoint terms remain in the fixed reference
field. No derivative records or physical labels are thereby deleted.

Original G,g,c intervals are quantized outward to a common2^-512
lattice once. All occupation coordinates and products are nonnegative,
so exact integer lower/upper energy scores can be used without any
floating-point selection. Every leaf contributes its word, coordinates
and two integer scores to a deterministic streaming digest. The path
count must equal(3N)!/(N!)^3.

All coordinate classes whose lower energy score is at most the best
upper score survive. Their complete multiplicities and first words
are retained. Exact original energy expressions distinguish genuine
ties from unresolved interval overlaps; an unresolved overlap is not
called a unique or exact minimizer. Each surviving representative is
replayed through the literal source: all63 coefficients, all45 physical
ratios and original energy must equal the six-moment reconstruction.

Each run is single-worker and streamed, capped at35000 paths and40000
candidate classes, with no artifact above8MiB. No field census, prime
acquisition, randomization, numerical quadrature, floating optimizer,
or source-dependent path pruning is permitted. Empty/degenerate tied
states are retained by the word enumeration.

The controls include the frozen diagonal, joint quadratic, all six
axis orders, and the synchronized-face optimum. All comparison signs
are retained. N=4 refines N=2, but N=3 does not refine N=2; monotonicity
between nonnested grids will not be assumed.

The finite result is a minimum on the stated actual grid-path class.
The separately proved O(1/N) original-source approximation theorem
relates these minima to the all-continuous-monotone-path infimum.
Neither a finite grid winner nor the convex-hull lower bound is
silently identified with that full all-path optimum or a gamma decoder.
