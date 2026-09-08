# Executed validation and its limits

The new reconstruction is standard-library-only and runs in ordinary and
optimized Python. It reconstructs 2,110 bounded exact-rational/directed
controls. It authenticates the parent proof and comparison JSON; it does not
execute parent code. All numerical energy values come from newly assembled
rational source coefficients and the complete finite Green formula.

Executed in the new packet directory:

```sh
python scripts/replay.py --write verification.json
python scripts/replay.py --check
python -O scripts/replay.py --check
python scripts/test_replay.py
python -O scripts/test_replay.py
```

Both reconstruction modes must produce byte-identical verification data.
Nine unit-test methods include twelve distinct actual CLI corruption cases
per mode. Semantic mutations are resealed where needed so rejection is not
merely a checksum mismatch. Cases include mathematical promotion, float
alias, duplicate JSON key, omitted frequency, omitted nonsquarefree source
coefficient, altered energy, empty inventory, unlisted file, symlink, changed
parent bytes, changed source head, and reversed GLOBAL charge orientation.
The last case leaves the quadratic energy unchanged but is rejected by the
literal sine-versus-floor source reconstruction.

The exact proof of the all-scale bounds is in PROOF.md, not inferred from
these finite counts. NUMERICS.md gives every transcendental remainder and
rounding rule. Scope: full energies at M=4,8,16,32; coefficient-bound controls
at M=128,256; primitive divisor identities through 256; 64 paired cells per
full source; physical prefix 512; odd cotangent panel through 63; three fixed
rational meshes for the inverse identity. There is no adaptive or broad scan.

The unchanged balanced-lift predecessor was separately rerun:

```sh
cd ../2026-09-06-astra-balanced-lift
python scripts/replay.py --check
python -O scripts/replay.py --check
```

Each returns PASS_BALANCED_SOURCE_BOUNDED_REPLAY controls=3884. Its numerical
method is independent of the new Green sum, and its three energy intervals
overlap the new results. Its separate unit suite and CLI mutation suite were
not rerun and are not counted as new executions. The checker's
parent_code_executed=false describes the NEW driver, not these separately
recorded command invocations.

No Windows replay, historical portability repair, Lean build, independent
kernel verification, new zeta zero census, unbounded energy estimate, or
referee acceptance is claimed. The fixed energies being below one do not
establish boundedness at arbitrarily large indices. Source hashes establish
byte identity, not theorem truth. A release or publication receipt is
separate from the mathematical status of this packet.

Two aggregate validation invocations hit their execution-tool deadline during
mutation testing. Neither incomplete invocation is counted as an optimized
suite PASS. After the first timeout, caching was moved after exact rational
angle reduction (no numerical formula changed); reconstructed numerical data
remained identical. The second aggregate invocation, after compacting the
retained mesh record, completed the ordinary suite but timed out during the
optimized suite. A separate final `python -O scripts/test_replay.py` invocation
then completed all nine methods and twelve CLI corruption refusals. The final
ordinary suite took 18.432 seconds; the standalone optimized suite took 13.549
seconds. These are execution receipts, not future time estimates.
