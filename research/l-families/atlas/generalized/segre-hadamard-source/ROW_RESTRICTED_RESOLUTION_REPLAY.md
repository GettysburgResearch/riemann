# Replay of complete kernels through certified original-row subsets

Status: new implementation and tests prepared; no new degree-six or
degree-seven success is claimed. The previous continuation stopped on
its898-row preflight. This producer has its own artifact and test identity
and leaves the older26-test contract and every frozen source unchanged.

Each run authenticates and reverifies the complete stage-five cache.
For every new full weight block it selects original rows over65521,
checks their rank independently with the frozen modular column routine,
and runs the unchanged rational kernel on the selected submatrix.
Every resulting primitive relation is checked on all original rows.
If that equality fails, the entire failed attempt and residuals are
retained before the sole permitted fallback1000003.

Complete weight checkpoints bind the algorithm, acquisition contract,
cache source and full ordered matrices. Reuse repeats row selection,
independent modular rank, restricted and full compositions, triangular
kernel independence and every unsuccessful-attempt check. Only rational
elimination is skipped. Operational reuse does not change the final
mathematical payload. Checkpoints do not turn a partial stage into a
complete resolution.

The final payload retains full original-coordinate kernels, the original
old-multiple quotients, all marked polynomial maps, complete dual weights,
selected original rows and every fallback certificate. The maximum-bit
field from rational elimination is retained as an acquisition diagnostic;
actual kernel coefficient bits and all mathematical rank witnesses are
checked independently on reuse.

The separate suite has42 tests: fifteen complete-map checks, eleven
source/typed-acceptance checks, and sixteen bounded original-row controls.
The latter include a600-row matrix, deliberately unlucky first and both
fixed primes, lost/dependent/corrupted kernel witnesses, source/checkpoint
counterfeits and ignored incomplete writes. Before the final artifact
exists, root can run only `OriginalRowCertification` and
`RowRestrictedSourceAcceptance`; the complete-map class requires the
final degree-seven fixture. The older26 tests remain unchanged.

Root first runs the degree-six scout under128MiB/2GiB reserve:

```text
python research/l-families/atlas/generalized/segre-hadamard-source/row_restricted_resolution.py --scout 6
```

Root captures the complete stdout maps. Only after accepting this stage
may root run `--scout 7`, the separate final `--write`, `--check`, optimized
`--check` and the new dedicated test suite. The all-degree exactness
theorem remains conditional on successful actual minimal-generator
acquisitions, as stated in the source proof. No author-run job is claimed.
