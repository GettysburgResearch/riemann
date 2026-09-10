# Executed checks and exact scope

Environment: Python 3.13.5 on Linux. The checker uses Python standard-library
integers, Fractions and formal prime-log coefficient identities. No zeta,
gamma, Ein, zero ordinate or actual entropy quadrature is evaluated.

## Mathematical controls

The final commands are

```bash
python -B checks.py --output checks.normal.json
python -B -O checks.py --output checks.optimized.json
cmp checks.normal.json checks.optimized.json
python -B validate.py
python -B -O validate.py
python -B rejections.py
```

The exact checker completes **10 named groups / 2,202 bounded fixtures in EACH
Python mode**, with byte-identical reconstructed outputs. Most fixtures are
finite prime-base/prime-power or divisor identities: 1,785 cutoff controls and
132 literal coefficient/rational-factor controls. The remaining groups check
all 64 Laguerre Gram entries through order seven, 72 multiplicity/delay cases,
90 rational Schwarz-kernel controls, four source moments, 30 formal continuum
coefficients, 15 full stepwise Abel sums, six rational constant comparisons,
and four conditional-majorant integrals. These are not 2,202 theorem proofs.

The E_(1/2)(2)<4 result is an analytic bound on the whole frequency integral.
The checker authenticates its elementary constants and signs; it does NOT
numerically integrate that entropy or prove an asymptotic from a sample.
Formal Taylor controls are finite algebra, not truncated numerical estimates
for the entire functions. Infinite remainders are handled in PROOF.md.

## Actual CLI refusals

Both pristine package controls pass. The actual checker CLI rejects five
corrupted retained records in each mode: RH promotion, a float alias, an
integer/Boolean alias, a missing group, and a duplicate JSON key. The actual
package CLI rejects four mutations in each mode: changed proof bytes, missing
manifest coverage, an extra file, and a resealed false parent commit. This is
10 result refusals and 8 package refusals. rejections.json retains the exit
codes. Acceptance uses explicit exceptions, not assertions disabled by -O.

An initial combined validation/refusal shell command reached its 20-second
limit after writing the complete first refusal receipt. Final validation and
refusal commands were then run separately; the interrupted combined command
is not counted as a completed final replay.

The final inventory has 16 files and 15 SHA-256 entries. The packet validator
reconstructs the bounded results and checks eight claim records and eleven
edge records, with the unproved premise kept OPEN. Byte authenticity and finite
logic tests do not decide the validity of the infinite paper proofs.

## Source and publication boundary

The live PR804 source was read at commit
0f6ee91f1a8c8bece1618bde155d62fb0bfb4cad, tree
0c8a32ba10e1e58278bfe2ae20f16281039f6c1c. Its 96 predecessor files are not
claimed newly re-reviewed or replayed. The supplied OE26 manuscript is pinned
by its exact blob, SHA-256 and length in SOURCES.json. It was not observed on
that frozen remote head. This continuation reconstructs all analytic facts it
needs and does not depend on an unpublished upload or another reviewer's work.
The CSM26 and MWR26 supplied bytes match their recorded Git blobs; no old
producer or old mathematical suite was executed.

The research publication is an add-only continuation on a separate branch,
not a main/source/review edit. Exact remote publication and local patch/ZIP
receipts are kept OUTSIDE this packet to avoid a self-referential head hash.
A local patch test, when reported in that receipt, is a temporary Git fixture,
not a full repository checkout or a remote CI run.

## Authoring corrections and limitations

During authoring, a collision between the literal X=2 function and the fixed
lower-endpoint term was removed by naming the latter a_*(s). Redundant
same-expression controls were removed, and the Abel fixtures were changed to
compare a complete step integral against independent atomwise summation.
The final published checks and fixture totals refer only to that corrected
checker. No failed run is counted as a successful theorem or replay.

No unconditional subpower entropy estimate, original-domain completion or RH
proof was found. No improved numerical zero-free region, external novelty,
independent referee acceptance, formal proof, Lean/Comparator build, remote CI
success, new zero census, or actual large-cutoff entropy campaign is claimed.
