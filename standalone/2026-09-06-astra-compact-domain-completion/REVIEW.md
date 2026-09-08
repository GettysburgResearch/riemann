# Targeted review specification

Review this exact packet independently; self-authorship is not acceptance.

1. Check the compact input transform, especially the boundary coefficient
   c_(N+1)=-(N+1)m(N), and reproduction at the endpoint itself. Confirm the
   output really belongs to the original closed domain rather than a changed
   metric or meromorphic boundary substitute.
2. Recheck the shifted Hardy evaluation and the Laguerre jet formula (12).
   Every zero multiplicity is retained. The bound is conditional on a zero,
   not an assertion that such a zero exists.
3. Check the subpower equivalence and its classical RH-to-Mertens input.
   The reverse implication must not assume the desired Mertens estimate.
   Verify the actual critical inverse divergence without assuming RH.
4. Check periodic Bernoulli remainder (17), its integer-knot conventions,
   and both sides of the infinite tail bracket. Verify every dyadic rounding
   operation and the Machin/atanh complete remainders in certificate.py.
5. Recompute the exact divisor coefficients and all 8 cell streams. Counts,
   precision, candidate cutoffs and the infinite-tail coverage must match.
   The normalized denominator is 2, not the predecessor's unit target norm.
6. Do not promote any finite error, safe b>1 result, or conditional rate (10b)
   into the unproved critical subpower bound. Literature comparison remains
   necessary before any claim of novelty; the NB mechanism is classical.

No canonical or formal status is changed. Acceptance, if any, should be at
individual CD26 component scope, with the global output norm marked OPEN.
