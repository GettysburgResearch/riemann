# Actual global Koszul Lie arithmetic source: exact replay

The [global theorem](GLOBAL_KOSZUL_LIE_COHOMOLOGY.md) places the actual
exponentially growing Koszul modules M_n on the frozen S3 cover,
forms finite middle-extension cohomology, and constructs its ordinary
parity-signed Fredholm ratio on the sharp trace-class grading disk.
The [ramification note](S3_LIE_RAMIFICATION_CORRECTION.md) proves the
exact bad-place correction rather than commuting inertia invariants
with the PBW product. These two proofs belong to one replay packet.

The runtime authenticates the actual global source adapter at
`e2b0ef1b35fa46e81a1f1b447a70f42dd3b92c2e` before importing it.
That adapter authenticates both the actual Lie character source and
the genus-three closure geometry. Primitive recounts use only fields
5,25,7,49; the two elliptic polynomials use complete degree-one
counts, the known determinant Q, and independent degree-two heldouts.
No new high-degree polynomial fit or large state-space expansion occurs.

The controls use short exact arrays for source Lie multiplicities,
full local inertia/residual Frobenius, three Mahler identities,
unramified PBW recovery and its three degree-two ramified failures.
They compare the actual finite fibre trace sums to cohomology and
identify M_1 with the regular-source closure zeta function. Finite
signed functional equations, independently bounded logarithm sums,
and the exact point-count exponent certify the global branch gate.
The compact-support controls check the full localization dimensions,
remove the actual bad-fibre traces, and prove the exact split/branch
count identity. They certify that the explicit Segre-source correction
cancels the first fractional branch, leaving the integer zero order
given by rational completely split unramified places. The cubic Lie
obstruction is not promoted to every corrected completion.
The analytic proof establishes the infinite threshold and monodromy;
the finite controls do not fit those claims from numerical values.

From the repository root with the serialized Python runtime:

```text
python -B research/l-families/atlas/generalized/koszul-analytic-parent/global_lie_cohomology_replay.py --check
python -B -O research/l-families/atlas/generalized/koszul-analytic-parent/global_lie_cohomology_replay.py --check
python -B -m unittest discover -s research/l-families/atlas/generalized/koszul-analytic-parent/tests -p test_global_lie_cohomology.py
python -B -O -m unittest discover -s research/l-families/atlas/generalized/koszul-analytic-parent/tests -p test_global_lie_cohomology.py
```

The completed 29-test packet passed the root agent's serialized focused
Ruff checks, producer write/check, optimized producer check and all
29 tests in each Python mode. Both proofs, the uniform-T extension,
the localization/cancellation extension and the full code/test sources
passed independent reading; the exact-freeze review is pending.
The fixture binds the five source files with LF-normalized
SHA-256 digests and requires complete typed-JSON replay.
