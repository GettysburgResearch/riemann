# Bounded S4 source replay contract

The source is b=c=1 over F5 and F7, and (b,c)=(3,4) over F7 to expose
nonsplit finite branch stalks. The producer constructs the first
encoded monic irreducible field polynomial for each extension and counts
every point of E,D,R,C,G,H. It covers F_(5^n), n=1,...,6, and F_(7^n),
n=1,...,4. The largest field has 15,625 elements. There are no precomputed
field tables, numerical eigenvalues, coefficient searches or fitted
polynomial roots. The field helper is authenticated against commit
dc4db621017ddaa8aeca1acfb211374dc0f04501 before importing it; its own
predecessor authentication remains active. Its small resource contracts
are unchanged.

The square-root tables are reconstructed by enumerating field elements.
For every finite u, root counts plus the discriminant determine the
unramified class or the normalized ramified Frobenius coset. The producer
compares its invariant traces with three independently counted fibres:
the quartic E, cubic resolvent R, and A3 quotient C. It checks every
affine R point away from (0,0) in the displayed rational map to u, while
counting (0,0) exactly once among R's affine points over base infinity.
All projective corrections are included explicitly.

The six curves are counted directly from their equations. The genus-19
cover Z is **not** enumerated from an affine splitting-variety model.
Its point count is obtained from the normalized regular character of the
proved S4 cover. This distinction is recorded in the artifact key.

For E and R, one trace plus proved elliptic reciprocity constructs the
degree-two polynomial, and all other counts are independent checks.
For D and G, two traces and reciprocity construct the degree-four
polynomial. For H and tw, four traces and proved symplectic reciprocity
construct the degree-eight polynomial. The p5 extension-five and
extension-six traces are then held out checks. The independent G and H
polynomials are compared to D times tw. The larger C and Z polynomials
are constructed using the proved source decomposition, then compared
to all available counts; they are not claimed to be independently
reconstructed from fourteen or thirty-eight power traces.

The unit tests derive S4 characters from actual root and pair-partition
permutation actions, enumerate A3 cosets, check inertia averages with
actual commuting permutations, and enumerate all affine point tuples
over both prime fields. Actual extension fields exercise both finite
branch Frobenius signs. Other controls reject the smooth cyclic stratum,
singular source, impossible fibre classes, coercible scalar inputs and
forged resource/source identities before allocation.

`source.json` has a hard-coded canonical typed JSON hash. The artifact is
recomputed before acceptance, and the provenance binds source, producer,
tests, both notes and artifact with normalized-LF hashes. Booleans and
floats are not accepted as integers in identity comparisons. Proof-
critical checks do not depend on Python assert statements.

Execution: Ruff format/check, complete primitive write/check, optimized
primitive check, and all 15 focused tests in ordinary and optimized
Python passed. The test suites took about 0.005 seconds each; the full
primitive reconstruction took about nine seconds per invocation. Root
serialized all computation behind the shared free-memory gate. The
all-field geometry,
purity and duality claims are supplied by the proof and its stated
classical inputs, not by these finite fixtures.
