# DMC31 validation and reading guide

**Proposed component mathematics, not independent acceptance or RH.**
Start with [MELLIN_DENSE.md](MELLIN_DENSE.md). ACC29 and SFC30 remain unchanged.

## Executed exact checks

From this packet directory, the following completed successfully in the
current Linux container:

```sh
python -I -S -B verify_mellin_dense.py > mellin_dense_results.json
python -I -S -B -O verify_mellin_dense.py > optimized.json
cmp mellin_dense_results.json optimized.json
```

Each run made **85,308 exact comparisons**: 86 balanced sources, exact
multiplicative collision formulas for L=2,...,40, rational Schur row
majorants through size 64, exact cutoff ceilings (including L=10^20),
constant inequalities, 81 finite Hardy fixtures with their below-support
boundary, and complete native Newton reconstruction for Y=3,7,15,31,63,95,255.
The last native prefix ends at 65,535. This is not an extension of SFC30's
native computation range, and is not a full-repository test campaign.

The actual altered-coefficient CLI was executed:

```sh
python -I -S -B verify_mellin_dense.py --mutate
```

It exited **1**, rejecting the complete Jordan numerator on the first
prime/prime-square fixture. The accepting script uses explicit exceptions,
not assertions erased by optimized Python. Finite algebraic checks cannot
prove the infinite zeta bound, mean-value inequalities, Mellin Plancherel,
or the proposed all-scale theorems.

Both predecessor checkers were also rerun, unmodified, in ordinary and
optimized Python, with matching outputs between modes:

```sh
python -B verify.py
python -B -O verify.py
python -B verify_continuation.py
python -B -O verify_continuation.py
```

These replayed ACC29's 96,190 comparisons and SFC30's 179,941 comparisons,
respectively. They are same-author regression replays, not independent
review of either predecessor. No whole-checkout validator, CI run, Lean
build, independent mathematical acceptance, or other platform run was done.

## Optional finite-band floating diagnostics

This command completed:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B mellin_diagnostics.py
```

The saved output is `mellin_diagnostics.json`. It uses NumPy and mpmath,
not the exact acceptance backend. Composite Simpson meshes 1/64 and 1/32
were compared. Nine mpmath double-precision zeta values were compared with
60-digit evaluations; the largest displayed absolute difference was below
4.4e-13. This is a spot check, NOT an error enclosure for every evaluation.

Four native completed sources (Y=15,31,63,127) cover [0,T_L] and [T_L,4T_L]
in positive Mellin frequency, with conjugate symmetry including both signs.
The complete D, O and twice-covariance ledger is retained, not only |P|^2.
The largest absolute mesh difference across all reported quantities was
below 3.1e-9. The script does not bound quadrature error and evaluates
nothing beyond 4T_L. The infinite-tail theorem is analytic, not inferred
from those panels.

For Y=127, L=129, T_L=337, the descriptive total P energies are
1.5695103168210267 on |t|<=337 and 0.0074648837515563825 on
337<=|t|<=1348. Most of this FINITE observed spectral energy is in the
uncontrolled low band. This does not indicate a completion of the native
estimate; it makes the remaining difficulty visible. Constants in the
uniform theorem are conservative and are not fitted to these examples.

## Frozen reading and trust boundaries

- #905: `dfd20b6a778941a3d0c5f671ba840a6b35e4d36e`.
- Concurrent #904: `d0d7ad05f9d4504e9d752518b34a9fd0609a06f7`.
- #903 metadata also inspected; no mathematical dependency on its newest
  continuation is introduced.
- Patel--Yang's explicit theorem is imported from the primary arXiv record,
  not re-proved. Newton/Mertens and transform ancestors are credited in the
  proof. External priority/novelty is not certified.
- Mellin and angular projections differ; native interval restriction does
  not preserve global orthogonality. The continuous Hardy bridge explicitly
  avoids unjustified sampling of filtered functions.

## Payload SHA-256

These authenticate the local payloads; publication verification must
separately compare the actual remote Git blobs.

```
216dc7dd70116533beee28e4fd8148a2b77b5e661d3f9ee9765c092f4ea11696  MELLIN_DENSE.md
b502be7172a5ff52386c346d4df50d1e3275cc1d2f6c68f80a96c7c81e3952f3  verify_mellin_dense.py
b03cbaa7bfe0218de921ee324092e29a9ab7cf6c7085d5e9915bd645ef439714  mellin_dense_results.json
820e00b77ee18dbdfb96894f5eff6f7a29a73a1db1dbaa1916c4035646f4a99a  mellin_diagnostics.py
cc4791ab6af8a40bdcce367dc77ecde41d91f252eacf43b55c923121e37b9022  mellin_diagnostics.json
```
