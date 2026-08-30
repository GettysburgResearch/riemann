# Independent review: finite-group source boundary and S4 completion

Reviewed scientific commit: `da203ad2d170835499a0f4f7484f04ff787ee408`.

I independently read the general theorem, S4 specialization, producer and 24 tests. I did not execute jobs. Root reports Ruff, generation, ordinary/optimized producer checks, and 24 tests in each mode passing.

The finite-cover inertia average is the correct whole-representation trace, including finite wild inertia with characteristic-zero coefficients. Its nonnegative averaging weights have identity coefficient `#Z(F_(Q^m))/|G|`. The maximal pole criterion follows from symmetric-power eigenvalue multiplicities: full order occurs precisely when an element is scalar on both inputs. Extra scalar resonances therefore contribute nonnegative leading terms and cannot be silently omitted. A closed point of the actual source guarantees a positive resonant identity term at every root of unity. The uniform character bound supplies dominated convergence and the grading natural boundary for the declared positive real T interval.

I requested two precision changes in the draft: distinguish rho from its dual in the general associated-sheaf/cohomology construction, and avoid using the same symbol for the identity and a closed-point degree. These were corrected. The S4 specialization uses real representations, so its numerical formulas were unaffected.

I independently reconstructed all five S4 character series from permutation cycle lengths. The finite and infinite ramified averages, conductor dimensions, degree-38 regular-source decomposition, sixth-order coefficient `5/12`, and finite-duality exponents agree. The negative grade-zero functional exponent is retained. The C2 genus-zero scalar-kernel example correctly shows that the identity-only shortcut omits every odd power term at the root -1.

The producer authenticates the S4 source and preceding boundary packet before import. It rebuilds symmetric-power coefficients, integral multiplicities and conductor/cohomology identities, and independently recounts only extension degrees one and two (fields at most 49). Larger-degree source polynomial reconstruction is transparently reused from the frozen geometry. Exact rational controls verify finite functional equations, the required `z^degree` local weight, positive limiting-constant enclosures and radial comparisons using the upper target endpoint. The conservative tail constants are valid.

The tests cover the source character construction, all five constituents, nonsplit ramification, source counts and caps, finite duality, scalar resonances and authenticated fixture refusal. I found no remaining blocking defect. The universal theorem is proved analytically from the actual finite cover; it is not inferred from the finite root-order or grade lists. It supplies a cohomological completion and a grading boundary, not a new purity theorem, number-field Euler product, or RH mechanism.
