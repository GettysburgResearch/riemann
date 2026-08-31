# Fixed-minor diagnostic replay

This separate, bounded reader verifies the exact coarse inequalities in
Section 5 of the frozen `NATIVE_FIXED_MINOR_INFINITY_DEFECT.md`,
commit `78918a6f3297d4c88b3b3c42140eba4c0f11778e`.
It consumes the already verified \(2^{48}\) extension artifact frozen at
`987ccb82d0bf097942389027c6e785925847e6a7`, exact blob
`98e4df4711a418f8ef3c084e5596ba0be7aaa69e`, internal proof digest
`aa3f9ad57373bb321996f9e5615652ec5322ef8e0147af5fd18c51cf93f0f2a1`.

The source artifact, frozen decoder, local source formula, and theorem
are all authenticated before compiling the decoder or parsing JSON.
The frozen decoder rejects duplicate keys, floats, nonfinite numbers,
and a changed complete canonical body digest. All diagnostic comparisons
then use canonical rational strings and literal bounded integer types.

The reader checks the exact twenty ratios and coordinates, all four
twenty-by-twenty matrix shapes, all inverse entry bounds, every local
partial/upper/remainder identity, all forty-four distinct local tables
with the unchanged 65-term cutoff, all actual alias integer bounds and
smooth support, the stored same-majorant subtraction, and every recorded
comparison row sum. It does not reconstruct an inverse, replay source
vectors, enumerate a new alias campaign, or multiply the full inverse
and tail matrices. Those identities are explicit inputs from the
independently accepted frozen artifact.

The exact extrema and proof provenance are retained in the new
`native_fixed_minor_diagnostic.json`. A successful diagnostic reports
`PASS` for the new inequalities while preserving
`UNKNOWN_TAIL_NOT_CONTRACTIVE` for the old experiment. In particular,
the local degree-64 remainder contributes less than \(4\cdot10^{-7}\)
to the recorded comparison norm, while every positive diagonal
weighting of that recorded comparison matrix has infinity norm greater
than three. This is a diagnosis, not a new tail method or an effective
all-future rank certificate.

Eight tests cover actual source extrema, authentication-before-parse,
typed JSON/body-digest counterfeits, inverse bounds and dimensions,
local-cutoff/identity/duplicate corruptions, selection and alias
corruptions, the row-sum obstruction and false outcome upgrades, and the
literal curvature scalar bound.

Validation status: the implementation and eight controls are written.
Root execution of write/check/optimized-check, formatting/lint, and the
ordinary/optimized tests is pending. No scientific job was run by the
author. The frozen source campaign's prior successful executions do not
count as execution of this new reader.

The first root write attempt failed honestly before producing an artifact:
the new reader incorrectly identified a row's stored integer alias cutoff
with its last smooth alias. The source field is actually
`isqrt(H // b)`, which need not itself be supported on 2, 3, and 5. The
reader now checks that exact cutoff and separately bounds the last smooth
alias by it. The existing alias test also rejects a changed cutoff, and
the positive source control retains the distinction. The failed run is
not reported as a successful diagnostic; root retry remains pending.

Root commands:

```text
python research/riemann-structures/native-six-hour/native_fixed_minor_diagnostic.py --write
python research/riemann-structures/native-six-hour/native_fixed_minor_diagnostic.py --check
python -O research/riemann-structures/native-six-hour/native_fixed_minor_diagnostic.py --check
python -m unittest discover -s tests -p test_native_six_hour_fixed_minor_diagnostic.py
python -O -m unittest discover -s tests -p test_native_six_hour_fixed_minor_diagnostic.py
```
