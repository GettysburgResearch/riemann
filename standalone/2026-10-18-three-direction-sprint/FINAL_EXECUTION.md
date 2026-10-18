# Execution, byte identity, and review scope

Status: PROPOSED research. No RH proof or new zero-free region is established.
This is a standalone research packet based solely on #983 at
`e9ce2d171fba2bcca4cb4d8c6e78dc97f69613e9`.

The research began at 2026-10-18 19:16:12 UTC. The user's extension sets
the working window through 23:46:12 UTC. The main packet was frozen for
publication during that window; further exploratory reading outside this
packet is not an additional theorem. Three parallel research tracks and
the coordinator read, attempted, and cross-reviewed the stated arguments.

## What the mathematics does and does not establish

The principal analytic contributions are the exact native signed-source
transport; annular, all-height arithmetic debiasing and its complete
comparison price; all-valuation polar energy; an invertible long arithmetic
frame on squarefree rows; and an all-power, simultaneous conductor/core
cleanup. Each note states its native versus imported inputs. Source
readings and reviews are bounded to their recorded scope. In particular,
the original 7/8 argument and all Gauss identities were not independently
reproved in full by this sprint.

The full mixed mean is OPEN. At the synchronized corner, the available
imported consequence is U^(11/8+epsilon), while the sufficient target is
U^(6/5+epsilon). The missing power is U^(7/40). Nonsquarefree physical
rows and the whole witness-length polygon also remain. The exact
conditional 437/500 consumer does not prove that boundary. The native
balanced contraction and all-order theta positivity are likewise OPEN.

The global arithmetic heat-kernel positivity in this packet is an
independent reconstruction of a known result, credited to Polson; it is
not the unscaled Hankel positivity required for RH. The directed covariance
certificate refutes a specified universal finite one-sign assertion; it
does not prove an asymptotic sign or exponent. Finite theta certificates
are secondary results from before the user's instruction to stop climbing
orders. Their finite scope is retained.

The later #1001--#1005 work is source-qualified in SOURCE_UPDATES.md.
The reported #1005 boundary .87488666 depends on the external analytic
hypotheses stated there. It is not a theorem proved by this packet.

## Executed primitive and algebraic checks

The coordinator exported Git-eligible packet files to an isolated replay
directory, preserving raw bytes. The following selected accepting runs
completed there under Python optimization (`python -O`); assert removal
does not bypass their explicit acceptance guards. Track notes contain
additional normal-mode runs, mutation tests and exact source pins.

| Check | Replayed coverage and arithmetic |
| --- | --- |
| rational/check_flux.py --mutations | 80,840 guards, 65,792 native cells, 1,244 signed targets; exact rational and formal prime-log arithmetic; three mutations rejected |
| rational/verify.py --mutations | 46,973 checks over 22 Y values from 2 through 96; eight mutations rejected |
| rational/check_column_adapter.py --mutations | 4,948 guards and 208 shared-prime examples; four mutations rejected |
| eisenstein/verify.py | 65,536 ordinary coefficients, 157 HNF ideals, five CRT checks and six directed Euler--Maclaurin checks |
| eisenstein/gauss_gram_check.py | 37 squarefree rows, seven labels, 33 zero entries and seven positive exact Q(omega) minors |
| eisenstein/growing_residue_check.py | 465 HNF ideals, 272 unit entries, 20 responses, 138 Cholesky checks, 5,936 polar checks, 24 cusp units; six mutations rejected |
| eisenstein/residue_valuation_check.py | 152 density, 152 periodicity and 1,728 Boolean checks; eight mutations rejected |
| eisenstein/tail_mollifier_check.py | 117 HNF ideals, 67 unit entries, 238 Euler checks; three mutations rejected |
| eisenstein/mixed_consumer_check.py | 20,301 exact tuples and 151 polygon checks |
| eisenstein/relaxed_mixed_consumer_check.py | 6,281 exact rational closed cells cover the complete consumer domain, including both frequency endpoints |
| eisenstein/profile_inverse_check.py | 27 labels, 729 exact inverse entries, 27 responses; four mutations rejected |
| critical/covariance_sign_check.py --check | Complete original finite source, 619 ideals, 312 physical rows, all 2,646 input pairs and 13,818 selected upper row pairs; outward Arb intervals establish the two opposite signs |
| theta/check_heat_positive.py --check | 892 complete directed contour segments establish the low-zero census; explicit arithmetic bounds and a complete zero-count tail cover the entire positive half-line |
| reviews/check_xi_source.py | Actual xi source recomputed through degree 32 at 896-bit precision, with its stated directed tail bounds |
| theta/certify_merge.py | Preserved finite merger certificate recomputed |
| reviews/certify_cyclic.py | Preserved degree-26 certificate recomputed |
| theta/certify_harmonic_observed_obstruction.py | Preserved directed harmonic-hub obstruction recomputed |
| critical/certify_tent_energy.py | 524,288 source values and 524,287 finite energy cells reconstructed |

Check the track READMEs for command spelling and required input arguments;
the table identifies the accepting executions and their scope, rather
than prescribing every command as an argument-free entry point. Analytic
infinite estimates in the proof notes are not certified by these finite
runs. No formal Lean proof of RH, repository-wide CI pass, or external
human review is claimed.

## Runtime and byte contract

The exact rational scripts use Python's standard library. Directed runs
use `python-flint==0.9.0`; the covariance script additionally uses NumPy
for bounded integer arrays, not floating-point BLAS for its proof. The
declared dependency path is explicit in the track instructions. Optional
floating scouts and their local dependency directories are ignored and
not required for the published accepting paths. Ordinary floating-point
exploration is not evidence for a directed assertion.

The old isolated replay inventory was compared against the final packet
before publication. Accepting code and its load-bearing data were kept
byte-identical; later additions are analytic notes and review receipts.
All Python sources were syntax-parsed, local Markdown targets were
checked, and accepting input paths were checked for Git eligibility.

MANIFEST.json records raw file length, SHA256 and Git blob SHA1 for every
published payload file, excluding itself. The packet's `.gitattributes`
disables text conversion. Raw CRLF bytes in inherited certificates are
deliberately preserved. Some older certifiers print a canonical-JSON hash;
that hash is not described as a raw file digest. In particular, the raw
actual-xi degree-32 source file has SHA256
`89903a63d27cd7fac0e023edfc685ef409f8172379e57f4b75082490c93850d3`.
Track input and certificate records state their corresponding canonical
contracts.

For a fresh exported packet, run:

```sh
python verify_manifest.py --strict-inventory
python -O verify_manifest.py --strict-inventory
```

The strict inventory check authenticates bytes and membership. It does
not establish any theorem or validate the imported papers. Mutation
controls for damaged bytes, an incorrect blob identity, duplicate JSON
keys and an extra unlisted file are also executed during publication.

## Review boundary and smallest invalidating gaps

Internal cross-reviews name the exact raw source hashes they inspect.
A repair has a new hash and an updated review receipt. This is team
cross-review, not an external referee verdict or integration approval.
The standalone packet does not change the integrated mathematical status.

For the .874 conditional target, the smallest outstanding load-bearing
statement is a complete original-source U^(6/5+epsilon) mixed-mean estimate
uniform over the specified robust witness polygon and its masks/heights.
For the native 5/6 target it is the complete balanced contraction with
a=1/3 and p=3/2. For the weighted-canonical RH route it is positive
weighted feasibility at unbounded orders. None was proved here.
