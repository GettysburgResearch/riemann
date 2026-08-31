# General-field extension order and invariant-generator base: replay

This companion binds `GENERAL_FIELD_RAMIFICATION_EXPONENT.md` and
`INVARIANT_GENERATOR_BASE.md`. It does not change either frozen comparison
packet. The general AFTER theorem and its independently reconstructed
3,044-source arithmetic atlas are pinned at
`075f9b203aefefb4a29f3279b6de1c4127093af6`, and the infinite comparison proof
at `b3fde737e790e38ae15c20ce0858e72104c55550`. Root reports their respective
28 and 30 tests passed in each interpreter mode, with all producer checks.
Missing or incorrect source pins fail closed before import or artifact use.

The general BEFORE theorem is proved for every admissible finite field in
characteristic greater than three. Its finite atlas is a source control, not
an extrapolation. The replay reads every authenticated AFTER source row,
recomputes the two first-circle exponents, retains the positive square-root
correction when a rational old branch or split infinity is present, and
classifies the actual full source. It records radius changes without confusing
the pure multiplier with the full Euler product. Seven declared sources are
independently recounted through the frozen literal point/fibre implementation;
the full field atlas is not needlessly run twice.

The source-base controls use explicit matrices of the actual standard S3
representation and literal inertia-invariant monomials. They recover
`k[x,y^2]` at C2 and `k[pq,p^3,q^3]` with relation `p^3 q^3=(pq)^3` at C3,
including the residual reflection trace. Literal Segre monomials in grades
one through six test the three negative degree-one generators. The statements
that the repaired module has rank two and that the old module is not finite
over the fixed-input base are all-grade proofs in the note; the finite rows
are controls of their actual source. The original cokernel is explicitly
not promoted to a module over the enlarged base.

The artifact records all prime-level totals and seven full representative
source classifications. The second-circle quarter/sixth test ranges over
the five possible **hypothetical** degree-two branch sign differences; it
does not assign an uncounted degree-two branch pattern to a source. Those
controls verify the arithmetic lattice obstruction used by the proof.

All frozen proof, executable, and artifact sources are authenticated against
both their Git blobs and their checked-out bytes before import or use.
Owned proof, replay, and test files are hashed into the result. Checking uses
canonical serialized JSON with `allow_nan=False`, so booleans, integers,
floating-point replacements, nonfinite values, and non-JSON container
substitutions cannot compare equal merely because Python permits them.

Validation status: producer and tests are authored; root execution and an
exact-freeze independent review are pending. The two mathematical notes have
received an independent read, conditioned only on the explicitly identified
AFTER theorem, which has separately been read. No computation was run by the
authoring subagent.

Root-only serialized commands:

```text
python -m ruff format research/l-families/atlas/generalized/extension-order-defect/general_replay.py tests/test_extension_order_general.py
python -m ruff check research/l-families/atlas/generalized/extension-order-defect/general_replay.py tests/test_extension_order_general.py
python research/l-families/atlas/generalized/extension-order-defect/general_replay.py --write
python research/l-families/atlas/generalized/extension-order-defect/general_replay.py --check
python -O research/l-families/atlas/generalized/extension-order-defect/general_replay.py --check
python -m unittest discover -s tests -p test_extension_order_general.py
python -O -m unittest discover -s tests -p test_extension_order_general.py
```

The worker should stay within the declared small source caps: primes at most
31, seven literal source recounts, 33 invariant-ring grades, and six Segre
monomial grades. There are no large extension fields, matrix sweeps, builds,
or expanded infinite operator spectra. Root retains the memory gate and runs
only one such worker at a time.
