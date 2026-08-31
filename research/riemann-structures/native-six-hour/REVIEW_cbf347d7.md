# Independent review of the all-arity Specht law

Reviewed freeze: `cbf347d79971535dc37df2874e884482b44bbee3`.

Reviewed file: `NATIVE_ALL_ARITY_SPECHT_LAW.md`, Git blob
`bf9ff11528371299140cebfbb3991bbe75057ead`. The working file has the
same blob. This is a full mathematical and scope review of a proof-only
note. I did not author the note and ran no scientific computation or tests.

No mathematical blocker was found. The source input is the exact
sequence from `NATIVE_S3_CURVATURE_ISOTYPES.md` at
`cb9278bec3844cc3fd8072987a6890f1df32a368`, which I also independently
read. The binary tensor realization of the source and the induced
ternary tensor realization of the one-form carrier give the stated
Specht multiplicities by Schur--Weyl duality and one-box branching.
The single differential index contributes no sign twist. Distinct
removable predecessor partitions occur once, including equal-row edge
cases; subtraction of the binary source and restoration of its constant
line agree with the exact sequence.

I checked the two- and three-row Weyl dimension formulas, the four-row
support bound and its positive hook example, and the closed trivial,
sign and standard multiplicities with their stated arity ranges. In
particular, the arity-two standard/sign coincidence and the arity-one
zero carrier are treated correctly. Every entry in both complete
arity-four and arity-five tables was checked from the predecessor
partitions; their weighted dimensions are respectively 93 and 374.
These are deductions from the source sequence, not held-out experiments.

The scope is accurate: canonical isotypic summands do not provide
canonical multiplicity-space splittings, legal projected monotone paths,
or permutation invariance of the fixed-prime physical metric. The note
preserves the earlier horizon-25 observation-kernel obstruction and does
not identify coordinate permutations with arithmetic, Wick or Walsh
actions. This review checks the stated classical formulas and their
application; it is not a separate bibliographic audit of the cited
textbooks' theorem numbering.
