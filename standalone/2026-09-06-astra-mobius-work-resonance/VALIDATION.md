# Validation and trust boundary

Date: 2026-09-06. This is a self-check of newly proposed research, not an
independent mathematical acceptance or a proof-kernel verification.

## Environment and resources

Python 3.13.5. SymPy 1.14.0 is used only by checks.py for bounded symbolic
rational algebra. certify.py uses Python's standard library alone. The
source producer fixes its arithmetic range at 65536 and its fifteen
checkpoints; it does not accept caller-supplied semantic coverage flags.

## Directed producer contract

All arithmetic endpoints are integers over 2^160. For n>=2,

    log(n/(n-1))=2 sum_(j>=0) 1/[(2j+1)(2n-1)^(2j+1)].

Terms are enclosed by integer floor/ceiling divisions. After J retained
terms the positive remainder is bounded by

    2(2n-1)^2 / [(2J+1)(2n-1)^(2J+1)((2n-1)^2-1)].

The loop stops only when that rational bound is below one dyadic unit.
All retained-term rounding costs are included. The reciprocal square root
uses k=isqrt(floor(2^320/n)); exact integer square tests decide whether
k/2^160 is exact or an upper endpoint one unit larger is required.

Between events, exp(-log(n/(n-1)))=(n-1)/n is used exactly. The state updates,
quadratic storage, and work sum are propagated by outward integer intervals.
The diagonal uses the exact rational mu(n)^2/n, not a rounded square.
No floating-point log, square root, numerical quadrature, zeta/gamma oracle,
or zero list is used. The source Mobius values are freshly sieved.

The event count is 65536. Only fifteen checkpoint norms are retained. Their
entire stopped-input future is the analytically proved quadratic storage.
This is not a reconstruction of future arithmetic beyond the cutoff, nor
an infinite-growth certificate. There is no prime/zero scan.

## Executed mathematical checks

1. `python checks.py --output checks.normal.json`
2. `python -O checks.py --output checks.optimized.json`
3. Byte comparison of those two complete outputs.
4. `python certify.py --output certificate.normal.json`
5. `python -O certify.py --output certificate.optimized.json`
6. Byte comparison of those two complete outputs.

The exact-check suite has 13 named groups / 1217 bounded cases in each
mode. The count includes 1024 independent trial-factorization Mobius
checks, twelve small direct pairwise norm checks, and bounded rational
matrix/resonance controls; it is NOT 1217 independent theorems. The four
positive Q pivots, all sixteen Lyapunov entries, a separate integration of
all sixteen Gram entries, and complex jump conjugation are checked.

The directed producer also verifies the stated N=3 work counterexample,
the previously recorded H(log64) range, and the final rational coarse
bounds. It checks the full data stream, not merely a stored digest.

## Rejection tests

`rejections.py` changes retained records and invokes the ACTUAL recomputing
CLI with `--expect`. In each Python mode it rejects three exact-check
mutations (a negative Q pivot, a missing check group and false case count)
and two directed-source mutations (a missing last checkpoint and altered
N=3 work). These are five subprocess refusals per mode, ten total.
Normal and optimized refusal records are retained. They authenticate
finite outputs; they do not detect arbitrary false analytic manuscripts.

Three separate package mutations (changed proof byte, deleted certificate,
extra file) were rejected by the actual validator in each mode. The six
subprocess results are stored in the outer handoff's PACKAGE_TESTS.json,
to avoid a self-referential manifest. `package_rejections.py` reproduces
them with its output directed outside this hashed directory.

## Discovery and authoring boundary

An initial NON-DIRECTED long-double scout at finitely many cutoffs up to
20000 suggested the N=3 positive work and suggested the range for larger
certificates. It is not included as proof evidence. The actual claims are
recomputed by the integer producer. The coarse final rational bounds were
added as explicit tests and both final-source producer modes were rerun.
No higher-cutoff trend, fitted law or external novelty conclusion is drawn.

The predecessor analytic proofs were read as specified in SOURCES.json;
local copied bytes of the DCP26 and CSM26 construction files matched their
stated Git blob IDs. No parent mathematical suite or parallel CD26
full certificate was rerun. Its compact inverse identity is independently
rederived in RESONANCE.md rather than assumed from a test status.

## Packet validation and publication

SHA256SUMS lists every file in this flat directory except itself. The
validator rejects changed bytes, extra/missing scientific files and
unexpected directories/symlinks. Python __pycache__ is ignored as generated
runtime cache and is not distributed. Final archive extraction and the
add-only patch have separate outer receipts.

No remote write was available through the discovered GitHub actions, and
`git ls-remote` failed DNS resolution. Therefore the handoff is NOT a
published new GitHub checkpoint. Its outer publication receipt gives the
last actually read PR head. The patch preserves all older paths; no main or
research branch was modified in this session.

No Lean, Comparator, remote CI, PDF audit, full literature review, new
critical-line zero computation or independent referee acceptance is claimed.
Finite executions do not machine-prove the all-T resonance argument or the
unbounded criterion. The missing signed work upper bound remains OPEN.
