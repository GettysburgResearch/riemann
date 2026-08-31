# Independent review of the Reynolds path obstruction

Reviewed freeze: `5e312c7dc81926e637d2d7343f90eba4708587c0`.

The complete note `NATIVE_REYNOLDS_PATH_OBSTRUCTION.md` has Git blob
`15d7ead32d565eb1c5c42b19368ecbea1fa30f85`; its working file matches.
This is a full proof and source-normalization review, with no scientific
jobs or numerical acquisition. I did not author the note. I contributed
an independent check of the variance inequality during its preparation,
which is disclosed rather than presented as a separate discovery.

No blocker was found. The Stieltjes occupation profile is nondecreasing
almost everywhere and can be expressed as a probability mixture of upper
thresholds, including the endpoint constant functions. Convexity of the
centered squared L2 norm proves `C-A^2 <= 2B-A`; vertical path segments
have zero du mass. The mixture is a proof device for the original
integrals and does not change the primitive `2ds` or physical measure.
The note credits the named earlier Jensen, Chebyshev and lower Gram
bounds without asserting a broader priority claim.

For a uniform permutation average of sequential activations, each pair
has moments `(1/2,1/4,1/2)`, violating that inequality by `1/4`. I checked
the exact distance `(sqrt(10)-3)/2` in the pair-moment maximum norm and
its attaining threshold path. The result does not claim that all
invariant currents are unrealizable: the synchronous path is explicitly
retained as an invariant legal example. Nor can the average, which is
inside the convex hull, be strictly separated from all legal currents by
one linear functional.

The literal half-source coefficients give the three stated `2ds`
readouts, including the endpoint term in `(C-1)/8`. I independently
checked every horizon-25 alias used in the physical argument: ratio
`1/3` retains `(2,6)`, ratio `1/2` retains `(2,4)` and `(3,6)`, and ratio
`2/3` retains `(2,3)` and `(4,6)` (unit-left rows contribute zero).
Their complete weighted coefficients recover A, B and C exactly as
displayed. Finite frequency independence in the original Mellin space
therefore supports the horizon-25 conclusion without treating raw
arithmetic records as separate observed coordinates.

The horizon-450 and infinite-observation consequences use the explicitly
named faithfulness results on the appropriate variation/full tensor
spaces. The positive physical-distance statement is qualitative, with
no evaluated norm-comparison constant. No untested intermediate cutoff,
observed Reynolds-operator descent, metric permutation symmetry,
arithmetic/Walsh identification or retained-gamma decoder is inferred.
