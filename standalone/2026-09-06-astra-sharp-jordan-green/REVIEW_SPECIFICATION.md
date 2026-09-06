# Review specification

Read PROOF.md Sections 2--4 first. The most consequential fresh inequality is
(2.9), obtained from the prime-power subsource and the factorial lower bound.
Check the Stieltjes signs and endpoint s; neither a PNT approximation nor
prime-only replacement is allowed. Then check the concave polynomial
comparison in all three s ranges, including the connecting interval
[1/2,2/3]. The checker tests algebra, not the analytic inference by sampling.

Check original notation s=2a before accepting the margin 8a/45. Preserve the
unit contact, all arithmetic atoms, and left/right knot conventions in the
Laplace formula. Check the separate sharpness argument at t=0 (and continuity
to small positive t) for kappa<2.

For gamma completion, review the GROUPED identity (6.1). R_s alone is not
positive-Laplace at s>1; an unrestricted claim about its separate inverse is
rejected. Euler beta yields the positive grouped measure for every s>0.

For REAL_AXIS.md, verify the exact B4 remainder and its differentiated bound.
The prime-2 contribution is a lower bound for the COMPLETE positive
prime-power difference, not for a sum in which other signed terms were dropped.

For RH_ATTEMPT.md, the direct exponential map fails and the Schur/exhaustion
premise is OPEN. Do not turn safe Hankel kernel positivity into that premise.
All proposed component results are self-assessed proofs pending independent
review; historical Reviewer D authorship does not confer independent acceptance.

Computational review: checks.py uses exact integers/rationals and SymPy algebra,
not zeta evaluation. Verify the coverage reported, run normal and optimized
modes, and inspect which corruptions rejections.py actually rejects. No test
is a machine proof of RH or of the infinite analytic argument.

Suggested integration destinations after independent review:
- a NEW source-qualified all-scale Green-density object beside the #396 source;
- a NEW corrected all-scale gamma/Stinespring adapter, not a rewrite of L-91031;
- a NEW prime-deletion real-axis margin object beside #440 L-91412;
- retain critical source identification/norm exhaustion as an open dependency.
Do not update the canonical graph to include RH as reached by these components.
