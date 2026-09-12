# Independent-review handoff — BPW26

## Requested verdict

Review the all-future **fixed-window** theorem and its executable certificate.
Do not review this as a claimed RH completion. No independent acceptance is
asserted by the author or by successful normal/optimized execution.

The first theorem whose failure would invalidate the application is the
closed-critical-strip error bound (13) in PROOF.md, with the exact normalization
and factor 31/80. Its proof is reconstructed, including the complex Peano
extension and the inverse-moment bound; it is not inferred from real moments.

## Load-bearing mathematical checks

1. Verify the shared-U distributional recursion, fixed law, and the complete
   Mellin identity. Section 3 rederives the BPY scaling using negative moments,
   csch² expansion, gamma duplication and the xi functional equation. The
   analytic continuations at s=0,1 must be genuine pole removals.
2. Check the three density switches in the beta/U^-2 comparison, quadratic
   interpolation signs, moment matching, and passage of third-order order to
   the limit. Check the constant 651/400 in the third-moment recurrence.
3. Check the complex two-child power smoothing, the uniform inverse moments,
   and the changing H_n denominator. The resulting error must cover the CLOSED
   critical strip, not only a scalar point or a compact with an unpriced edge.
4. Verify the theta normalization and full model error: each individual Simpson
   grid has its own endpoint weights; all three time tails and all n>=4 theta
   terms remain; Taylor degree 240 has a complete complex error. An absolute
   source error is not relative error near zeros.
5. Check that the Taylor interval for every full contour segment contains its
   complete image, both polygon endpoints and the entire all-depth error ball.
   Convex zero-free enclosures, not sample nonvanishing, justify the winding.
6. Outer count three plus three disjoint inner counts one must be used to
   exclude the complement. Reflection and multiplicity-one then give exact
   line membership and simplicity. The same argument covers convex interpolation.
7. Check the real derivative lower bounds, Cauchy radius 1/4, and the resulting
   root displacement. The lower bound for the trial model is never used as a
   lower bound for Xi without its full derivative error.

## Implementation checks

`intervals.py` has only outward dyadic arithmetic, exact rational input, Machin
pi and range-reduced exponential series. `certificate.py` reconstructs the
positive sample moments and independent derivative recurrence; it uses an even
scaled polynomial rather than a special-function or zero oracle. `check.py`
authenticates the supplied package before importing these modules. A malicious
replacement of the entire checker AND manifest is not detectable merely by that
same altered checker: compare the externally frozen blobs or archive digest.

Inspect 3,220 complete contour segments, not a plot of the polygon alone.
The receipt's exact margins already subtract all numerical and future-law errors.
The numerical counts concern one backend run in two interpreter modes, not two
independent implementations. No future branching transform was itself numerically
evaluated at depth 32 or later; their inclusion follows from the proved envelope.

## Boundaries that must survive review/publication

- The result covers n>=32, height<=30. It neither covers every finite early
  iterate nor any unbounded-height sequence.
- #860's upper-tail threshold grows with depth; it does not close the interval
  between 30 and T_n. #859 is a different same-path variant, not a second review.
- Three familiar Xi zeros are reconstructed without a zero-table premise.
  This is not a new Xi verification-height claim.
- The multi-zero version permits thin clusters in a FUTURE cofinal certificate;
  it does not prove such a certificate exists or assume RH/simple zeros.
- No source randomness assumption about primes, finite-to-infinite extrapolation,
  independent referee verdict, Lean proof or remote CI success is asserted.
