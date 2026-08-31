# Proof-focused review of the arithmetic radius dichotomy

Scientific freeze: `075f9b203aefefb4a29f3279b6de1c4127093af6`.
Proof blob: `cf8d794a35c2dc88eb86c1a6f62f6a06cbe3d03f`.

I read the complete frozen mathematical note and confirmed it agrees with the
working file. No proof blocker was found. This is explicitly **not** an
independent whole-packet review: I authored its separate Python producer and
tests. The Segre reviewer supplies the independent proof/code audit. I ran no
computations; root reports all producer modes and 28 tests in each interpreter
mode passed before this freeze.

The proper normalized Galois-fibre count establishes trace divisibility by six,
including the unassigned quadratic sign at u=0 and the paired old branch set.
The even-degree PBW divisor formulas have the correct secondary sign, and
their geometric-series error bounds distinguish the first two exponential
scales. Splitting off a sufficiently large finite source before the tail
expansion keeps initial arithmetic poles inside the finite source rather than
silently assuming H2 is holomorphic on the required disk.

The three logarithms have the coefficients alpha, beta, and gamma displayed
in the proof. Higher Frobenius powers and source-character errors converge
normally beyond the second circle under the explicit finite-cutoff inequality.
The first-circle orders g-minus and g-plus come from actual rational good
places; the odd-characteristic weight argument excludes hidden proper or
boundary cohomological zeros there. Nonnegative integral full-source orders,
rather than multiplier orders alone, are therefore the right removability test.

Finally the real/imaginary second-circle exponents cannot both be integers:
odd aE makes their difference a half-integer, while even aE gives an odd
quarter numerator. Finite holomorphic source zeros can only add integers.
This establishes the two exact radii in the claimed all-field family without
extrapolating the finite atlas. The old trace-class domain and the continued
scalar domain remain distinct.
