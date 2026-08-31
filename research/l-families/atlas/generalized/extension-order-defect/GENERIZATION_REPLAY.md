# Generization counterfeit: bounded replay

This packet tests the actual source distinction in
`GENERIZATION_AND_EULER_INVISIBILITY.md`. It leaves all frozen packets
unchanged. The old C2 boundary basis is reconstructed from literal Segre
and generator monomials in grades zero through six. Its inclusion into
nearby invariants and the augmentation map have different ranks, while
acting on the same Frobenius representation. Source multiplication is
checked on all products of boundary basis vectors of grades at most three.

The frozen literal C3-infinity and new-point constructions retain their
residual Frobenius actions. Exact ordinary determinant prefixes through
degree eight are compared with Newton reconstruction from eight power
traces; the eigenfactor formulas define the full determinants. Twists and
constant-field splitting keep both the new closed-point degree and the
correct power of the original Frobenius and twist. The replay does not
replace these operations by an unexplained single-variable substitution.

All-degree stalk equivalence, existence of the alternative algebra sheaf,
and failure of the prescribed `j_*A` map are proofs in the note. No finite
trace sample is used to infer them. In particular a zero old boundary
cokernel at u=0 does not erase the separate generization modification.

Validation status: proof and bounded producer/tests are authored. Root
execution and independent proof/code review are pending. The authoring
subagent has run no computation. Root alone should execute the following
under the standing memory gate:

```text
python -m ruff format research/l-families/atlas/generalized/extension-order-defect/generization_replay.py tests/test_extension_order_generization.py
python -m ruff check research/l-families/atlas/generalized/extension-order-defect/generization_replay.py tests/test_extension_order_generization.py
python research/l-families/atlas/generalized/extension-order-defect/generization_replay.py --write
python research/l-families/atlas/generalized/extension-order-defect/generization_replay.py --check
python -O research/l-families/atlas/generalized/extension-order-defect/generization_replay.py --check
python -m unittest discover -s tests -p test_extension_order_generization.py
python -O -m unittest discover -s tests -p test_extension_order_generization.py
```

The finite producer and both source proofs are authenticated before any
import; their own dependency authentication is then invoked. Owned files
are hashed into the artifact. Canonical serialized JSON checking rejects
boolean/integer/floating-point substitutions, nonfinite numbers, and
non-JSON containers. No field enumeration, large matrix, build, or expanded
infinite spectrum is needed.
