# Independent review: the marked Kummer orbit obstruction

Reviewed scientific commit: `6551c743d4a86e2664d4b5a62da3c303fa805c7e`.

The four reviewed files are `MARKED_KUMMER_ORBIT_OBSTRUCTION.md`, `marked_kummer_orbit_obstruction.py`, its result JSON, and `tests/test_marked_kummer_orbit_obstruction.py`. The frozen source is the repaired complete marked-owner packet at `faf74a47dac33927d081a890f2b5a7ead48b869b`. The main agent reports proof-object hash `d9a61c79638355542ef38ea346bba42eef722d5b2208be92a7d2f307507514fd`, focused Ruff, producer write and both check modes, and all nine tests passing in normal and optimized Python.

The reviewer independently read the full proof, producer and nine test definitions, checked the exact frozen inventory, and verified the cited primary theorem on topological invariance. No test or producer execution was performed by the reviewer.

## Mathematical assessment

No blocking issue found in the stated generic and finite-category scope. The proof works over `F_5(lambda,rho)` and explicitly allows changing punctured opens under partial Frobenius. It does not wrongly treat the original punctured configuration space as preserved by each marked map.

The bi-infinite graph polynomials are irreducible and have distinct prime divisors. Their divisor valuations give independent square classes. The multiquadratic degree is therefore `2^N` for any selected N graph classes. The proof of the degree statement via sign eigenspaces is valid. If a finite field extension containing the first square root admitted a lift of the left partial Frobenius embedding, iteration would place all nonnegative graph square roots in it, contradicting those degree bounds. This does not exclude an infinite cover.

The positive and negative index pullback formulas check, including the fifth-power corrections across zero. Total Frobenius fixes every square class while the marked maps shift the orbit in opposite directions. This distinction is essential to the conclusion.

The finite-rank constituent argument is also sound. The pullback equivalence comes from the purely inseparable extension of the image field and topological invariance of the small etale site. I independently opened [Stacks, Theorem 59.45.2](https://stacks.math.columbia.edu/tag/04DY), whose universal-homeomorphism hypothesis applies here. Exact pullback preserves composition factors. A finite-length representation invariant under this pullback cannot contain a line with an infinite orbit of pairwise nonisomorphic constituents. The theorem correctly requires an actual constituent and does not infer one from a virtual difference.

For the complete owner observable, the declared Kummer--Tate polynomial has trace `4J`, by the all-field moment identity of the frozen source. The integral ordered-source parent has trace `16J`, so its integral trace model is `4Q`. This preserves the repaired ordered-source normalization. The statement is equality of the specified trace functions, not an unproved equality of derived pushforward objects.

I checked the decomposition `Q=Q0+a Q1` and the specialization to the actual fixed external sign rows. At `R=0,S=-2,W=1`, the coefficient is exactly `648(n-3)^2[(n-2)^2(n-5)+(n-9)]`. It is nonzero and positive in the declared range, and changing the crossed sign changes J by `-Q1/2`, reproducing the source defect.

The finite Kummer--Tate ring argument is faithful in this setting. Coordinate-divisor classes and graph-divisor classes remain independent even geometrically. Their rank-one characters are distinct; different Tate powers are distinct arithmetic characters and cannot introduce a relation between the finite quadratic characters. Translation of a nonempty finite set of graph indices has an infinite orbit. A finite invariant group-ring sum therefore has no crossed component. This proves the no-go for the declared finite orbit repairs, including products of crossed lines, without claiming an obstruction for every possible geometric or derived parent.

## Executable assessment

The producer authenticates the three frozen owner-source blobs, including the repaired proof object, before accepting its source data. It expands the full group-ring polynomial using exact integer coefficients and finite character masks. All 512 sign assignments at two declared n values are compared with a separate scalar formula. The actual source witness is separately checked against the frozen owner artifact.

Finite graph controls check polynomial pullbacks and distinct divisor incidence without expanding enormous monomial spaces. The report explicitly distinguishes these controls from the infinite divisor argument. The tests cover source specialization, crossed parity, graph intersections versus common divisors, finite-support translation, exact types and caps, false source blobs and strict JSON numeric types. No imported runtime or hidden large-field enumeration is needed.

## Limits

This is an obstruction for a specified generic Kummer orbit, its genuine finite-rank constituents, and a finite Kummer--Tate trace model of the complete polynomial owner observable. Cancellation by the remaining integer carrier source, a changed observable, coupled correspondences, infinite orbits and categories outside the declared ring remain possible. Full integer-source transport is still unproved. The report records an independent mathematical/code read and primary-source check, not an independent execution or formal verification.
