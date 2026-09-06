# Execution, provenance and limits

## Environment actually used

Python3.13.5; SymPy1.14.0; MPFR4.2.2; GMP; Boost.Multiprecision;
g++14.2.0 and clang17.0.0 on a64-bit Linux platform. The vendor MPFR header
was not installed; the supplied minimal public MPFR4 ABI declarations were
used. `lake` was not installed. Repository network clone was unavailable;
source reads and publication use the GitHub connector instead.

Only independently written review code was executed. No privileged workflow,
repository secret or original branch code was run. The C++ code uses directed
MPFR input/function/conversion operations, checked __int128 arithmetic and
arbitrary-precision integer tail arithmetic. No unsafe fast-math flags.

## Full computation commands executed

    g++ -std=c++17 -O2 p61_replay.cpp -Wl,-l:libmpfr.so.6 -lgmp -o /tmp/p61
    /tmp/p61 /tmp/p61.full.json
    clang++ -std=c++17 -O2 -fsanitize=undefined -fno-sanitize-recover=all \
      p61_replay.cpp -Wl,-l:libmpfr.so.6 -lgmp -o /tmp/p61-clang
    /tmp/p61-clang /tmp/p61.clang.json
    cmp /tmp/p61.full.json /tmp/p61.clang.json

Both full runs completed; the retained outputs are byte-identical. The first
run's process report recorded1,000,000 endpoint input values and no error;
mathematical coverage is encoded in the JSON counts and R25, not wall time.
No UBSan diagnostic was produced. Two compilers share MPFR and do not provide
independent transcendental primitive implementations.

`constant_audit.cpp` was compiled separately with g++ and computes the tight
C0 interval at denominator2^200. Its purpose is to test the OLD serialization
contract. It is independent of the coarse C0 interval used by the full replay.

The public `build_and_replay.sh` reruns the full default-compiler calculation,
constant calculation, exact checks, corruption checks and validator in a
temporary build directory. Vendor mpfr.h is preferred when available. On
systems using a different library linker name, change only the linker flag
and record that environment. No binary is distributed.

## Bounded exact checks actually executed

    python checks.py --output checks.normal.json
    python -O checks.py --output checks.optimized.json
    cmp checks.normal.json checks.optimized.json

Results:14 named checks,6,253 bounded fixtures in each mode, byte-identical.
Most fixtures compare the closed P61 coefficients against an independent
finite convolution through2000. Others reconstruct the complete8x8 Pick box,
complex Haar coefficients, carry inverses, the894 dual pullback, factor64
reward, signed elementary kernel and branchwise derivative identities.

These6,253 fixtures do NOT include the1,999,994 P61 inequalities or the two
256,805-slab C++ tail scans as millions of independent theorem claims. The
P61 result-contract check is one bounded semantic check of the retained full
run. Parsing that output alone would not authenticate the primitive producer.

The supplied Pick table is an explicit transcription of all eight primitive
rectangles and freezes their source SHA/path/blob. The exact conditional
matrix deduction was regenerated; the special functions were not evaluated.
SymPy is used for exact algebra, not floating eigenvalues. The tests do not
machine-prove infinite analytic statements.

## Fail-closed and package checks

The actual JSON parser rejects duplicate keys, non-finite and malformed JSON.
The same whole-result equality used by the checker CLI rejects five altered
bounded-result claims. The P61 semantic parser rejects eight further
coverage/sign/denominator/scope corruptions. `rejections.json` records all16
refusals and is byte-identical in normal and optimized Python.

`package_rejections.py` changes a result, producer, required header, inventory,
and an old predecessor report in separate copied trees. It invokes the actual
validator as a subprocess in normal and optimized Python; all ten cases
return rejection code2. No original local or remote file is changed by these
tests. Retained output is `package_rejections.json`.

`validate.py` checks all new hashes and exact inventory, retained output
agreement, proof-facing P61 counts and signs, ledger counts and139 canonical
coverage total. It recomputes each old16-file Git tree and matches the three
previously published subtree identities. All48 predecessor files remain
byte-identical. Their OLD mathematical checkers and rejection suites were
not rerun in this pass.

The validator is not an authenticity oracle for modified source plus modified
results plus a modified manifest. Publication binds the final Git tree to the
actually tested bytes. A new source version needs new proof review and replay.

## Authoring and assurance record

The publication-stage exception label/exit code was standardized to REJECTED/2;
both full compiler runs were repeated afterward and scientific outputs stayed
byte-identical. An attempted interactive container session failed before writing source; the
ordinary execution path was used. An exploratory high-precision C0 decimal
was used to locate the suspected serialization failure, then replaced by the
retained directed MPFR calculation. That exploratory number is not evidence.
A stale API response handle returned plugin metadata instead of a source;
critical file pins were read again through exact-path GitHub fetches. No
scientific conclusion is based on that unrelated response.

The source reads include explicit limited-read labels for the truncated end
of the one-line Pick68 certificate and the unexpanded PR71 dispatch slice.
The full relevant rectangle table, exact algebra, and final status logic were
read. No claim of complete primitive producer coverage is made.

No fresh high-ordinate special-function backend, zero census, larger Robin
stream, full Lean build, comparator, Nanoda or remote CI run was performed.
Open native allocations and critical inequalities were not proved. No external
human review or machine verification of the analytic arguments is claimed.

The final ZIP is checked after extraction. Exact final commit, tree and blob
comparison are recorded in its publication receipt and PR799, not embedded as
a self-referential hash in these scientific files.
