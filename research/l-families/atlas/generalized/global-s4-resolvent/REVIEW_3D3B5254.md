# Independent review: S4 closed-place Euler factors

Reviewed scientific commit: `3d3b52541ed33b516c25ec0a27ba3eb568ec513b`.

I independently read the mathematical note, producer and 14 tests, including the final source contract and coverage. I did not execute them. Root reports Ruff, generation, ordinary and optimized producer checks, and 14 tests in each mode passing after final bindings.

The local determinant table is correct for all five S4 classes. I checked it from the four-root permutation action, the three-pair-partition action and the sign twist. The finite branch denominators correctly use the residue-field character of -2: the standard invariant determinant is `(1-t)(1-epsilon*t)` and the twisted one is `1-epsilon*t`. At infinity the character of -1 gives the required nonsplit two-dimensional determinant `1-T^2`. Invariant dimensions alone would not recover these Frobenius factors.

The producer authenticates the frozen geometric packet and the earlier closed-orbit helper before import. It reconstructs complete degree-one through degree-four Frobenius orbits, their irreducible minimal polynomials and source classes in their own residue fields. The extension-field square table therefore evaluates the correct degree-dependent quadratic character. Truncated reciprocal multiplication includes infinity and compares all four nontrivial factors, plus the trivial projective-line zeta factor, with the frozen geometric coefficients.

The tests derive local determinants independently from actual permutation characters and inertia-projector power traces. They also rebuild a degree-two census, check exact closed-point totals, and demonstrate failures from replacing the nonsplit finite or infinite factors by invariant-dimension approximations. Parameter and source-authentication controls reject coercible numeric types and unverified dependencies.

I found no remaining blocking mathematical or implementation defect. The replay verifies the degree-eight twisted factor only through T^4. Its remaining coefficients and held-out extension checks belong to the preceding geometric packet. The all-place equality and continuation rely on the actual finite sheaf and classical cohomological trace formula; finite orbit enumeration is an independent convention and ramification check, not a proof of purity from finitely many coefficients.
