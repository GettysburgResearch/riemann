# Root review of the conditional continuation gate

Status: **CONDITIONAL REDUCTION CHECKED; target-family hypotheses unproved**. Date: 2026-10-30.  
Reviewed source: `normality_gate.md`.  
Reviewed SHA256: `b71cd0894e5aa8d635b41d34e6da609c197f8b722c0d3421a434f15d7b737262`.

The rescaling f_Q(z)=R R_Q*(c+Rz) preserves residues. The detector has only simple poles with positive residues in the stated domain, even when an underlying zero has multiplicity. There are finitely many distinct poles for each Q in the disk, whose closure lies in the meromorphic domain.

The three stated assumptions suffice. The unweighted budget gives B_Q(z0)>=exp(−B), ensuring a nonzero holomorphic subsequential denominator. On |z|<=r, cancelling one Blaschke factor yields |B_Q(z)/(z−a)|<=1/(1−r). Bounded positive residue mass and local bounds on the regular part then give a locally bounded holomorphic numerator. Its limit vanishes on the right-side open set and hence throughout the disk.

A small contour whose boundary avoids the limiting denominator's discrete zero set has a uniform nonzero denominator for large Q. The normalized contour integral consequently tends to zero. A persistent zeta pole contributes an integer multiplicity; a fixed primitive conductor-d pole contributes a limiting positive weight at least its multiplicity divided by d. Positivity prevents cancellation. Both give the claimed contradiction.

The two examples are valid: exp(−N(s−a))/(s−a) has an unbounded regular part despite one fixed positive pole, and z^(N−1)/(z^N−r^N) has unit total positive pole mass and zero regular part but fails meromorphic normality across |z|=r. The note correctly distinguishes bounded holomorphic numerator/denominator extraction from normality of the original meromorphic family.

The package is stronger than the original zeta-only contour threshold below one: continuation to zero excludes all fixed conductors. Neither weighted density nor the newly derived arithmetic main term supplies the unweighted budget or regular-part bound. The note states this limitation explicitly. No unconditional target-strip continuation follows from this reduction.
