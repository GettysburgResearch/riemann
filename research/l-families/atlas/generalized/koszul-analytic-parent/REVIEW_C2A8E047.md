# Independent review: source cohomology duality and grading boundary

Reviewed scientific commit: `c2a8e0477e7aaa9774692b51a7466dfed3e01589`.

I independently read `GLOBAL_DUALITY_AND_GRADING_BOUNDARY.md`, its producer, tests and replay note. I checked the final acceptance-bound correction at the frozen commit. I did not run computational jobs. Root reports Ruff, producer generation and both ordinary/optimized checks, plus 20 ordinary and 20 optimized tests passing.

## Mathematical review

The finite-cutoff functional equation retains grade zero and its rational factor; the explicit sums of multiplicities yield the stated cutoff powers. The obstruction to a compact same-space operator with bounded perfect duality follows from the bounded left inverse forced by the pairing equation. The Hilbert-scale construction supplies the stated two-space duality while retaining the unbounded inverse after compact inclusion. These are different operator settings and the note distinguishes them.

For real `0<T<1/Q`, the grading-boundary proof is source-bound: the leading identity-character coefficient is the actual normalized S3 Galois-closure count `#Z(F_(Q^m))/6`. At a root of unity of order h, the radial fourth-order logarithmic coefficient is `1/2 sum_(h|m) #Z(F_(Q^m)) T^m/m^5`. The two points at infinity over the quadratic extension give a positive term at m=2h. Uniform degree-six point-count bounds justify dominated convergence and the stated geometric tails. The lower-order transposition and three-cycle terms vanish after fourth-order scaling. Positive radial exponential growth excludes a meromorphic extension at each root of unity, giving a grading natural boundary by density.

The conclusion is correctly restricted to the declared real T interval and the grading variable. It does not assert a T-plane natural boundary, an all-complex-T result, or a new proof of the finite-field weight theorem.

## Code review and repaired finding

The exact replay authenticates the preceding cohomological source before import, uses rational and Q(omega) arithmetic, checks finite-cutoff reciprocity and primitive source counts, and compares positive limiting-constant enclosures with radial scaled-log enclosures. Output rounding occurs only after the exact internal calculation.

I identified an acceptance precision issue in the draft: comparing the observed lower bound with half the target lower bound did not prove the stated comparison with half the actual limiting constant. The frozen code compares `observed[0] > target[1]/2`, which proves that stronger statement. This repair affects the certificate criterion, not the analytic theorem.

The tests cover source authentication, typed/capped inputs, finite functional equations, actual closure counts, roots-of-unity arithmetic and certified tails. I found no remaining blocking defect in the frozen five-file packet. The finite enclosures verify declared small cases; the universal natural-boundary assertion rests on the proof above, not on those samples.
