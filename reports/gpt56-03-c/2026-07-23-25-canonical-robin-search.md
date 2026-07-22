# Session report — proof-producing canonical Robin search

Agent: `gpt56-03-c`  
Issue: #25  
Branch: `agent/gpt56-03-c/25-canonical-robin-search`  
Stacked base: PR #24 / `agent/gpt56-03-b/20-independent-robin-verification`  
Date: 2026-07-23

## Starting hypothesis

T-2002 gives a complete canonical search class, but a finite run becomes a
mathematical artifact only when the repository can prove:

1. the exact finite region covered;
2. that every support, child, and leaf is visited or rigorously pruned;
3. that every prune and leaf sign is recomputed rather than trusted;
4. that weak numerical settings fail closed;
5. that transfer from canonical integers to all integers uses an explicit
   theorem and the finite barrier from T-2001.

## Startup audit

Issue #25 was open and unclaimed. I claimed it as `gpt56-03-c` and stacked the
work on PR #24, which contains T-2001, T-2002, and the independent dyadic finite
barrier. No review comments were present at startup.

## Approaches attempted

### 1. Exact finite tree

L-2501 specifies the complete child range for every canonical prefix under an
exact integer bound. Coverage uses integer powers, not floating logarithms.

### 2. Uniform tail cap

The first prototype bounded every remaining exponent only by the last prefix
exponent. It was valid but loose.

### 3. Size-aware individual caps

L-2502 also uses the finite total product budget and the forced occurrence of
all other tail primes. Each remaining prime receives its own exact exponent cap.
This materially reduced the tree and made the `10^54` production run practical.

### 4. Independent traversal replay

The searcher and verifier have separately written prime generation, floor-log,
prime-power abundancy, and DFS implementations. The verifier reconstructs all
omitted proof values and rejects malformed coverage streams.

### 5. Compact terminal streams

An explicit-object prototype produced multi-megabyte certificates. M-2501 stores
only terminal codes and exponent prefixes. The verifier reconstructs every
integer, rational ceiling, dyadic interval, and classification. The regenerated
`10^54` certificate is about 544 KB; the repository commits a compact manifest
that binds it.

### 6. Quantitative global margin

Every strict terminal yields an exact normalized-quotient bound. The verifier
maximizes these bounds and checks the stored controlling terminal.

### 7. All-integer transfer

T-2502 separates three cases: the exact window 5041--5582, canonical images at
or below 5040 for larger integers, and canonical images above 5040. This avoids
the invalid shortcut of assuming every original integer is canonical or
superabundant.

## New results

### Mathematical claims

- `L-2501` — exact finite canonical tree enumeration.
- `L-2502` — finite size-aware tail ceiling and strict prune.
- `T-2501` — terminal-stream coverage and global canonical margin.
- `T-2502` — finite all-integer transfer with an explicit three-case bound.
- `M-2501` — compact terminal streams with reconstructed proof objects.

### Certified computation X-2501

Exact region:

```text
5041 <= n <= 10^54
```

Canonical support limit: 33, ending at prime 137.

Replayed counts:

```text
internal nodes          37476
strict subtree prunes   29818
strict leaves             173
below-domain leaves        43
unresolved leaves           0
violation leaves            0
terminal tokens          30034
```

Internal certificate digest:

```text
4927ea262cdfe5e455bf06e5af7bad65053e2cbd99561f34b6c7da8f2a7856e6
```

The tight canonical terminal is support 26, prefix `[20,10]`, with outward
normalized bound

```text
0.999997639970216146706942918996
```

The proposed all-integer consequence has the same controlling bound.

## Candidate counterexamples

None.

No `Z-####` identifier was allocated. No unresolved sign remains in the
production region.

## Certified computations

The search certificate and replay use exact integers, exact rational
abundancies, and fixed-denominator dyadic intervals. The replay independently
reconstructs the tree and all arithmetic except for sharing the audited
`certmath.py` kernel.

Parameter ladder:

- 64-bit weak configuration: rejected at the first unsupported prune;
- 72-bit, 96-bit, 160-bit, and 256-bit configurations: accepted;
- the outward global bound converges monotonically toward the production value.

## Failed or superseded approaches

### Explicit proof object per terminal

Correct but unnecessarily large. Replaced by compact terminal streams and full
reconstruction.

### Common exponent cap only

Correct but weaker. Superseded by the finite size-aware individual caps of
L-2502.

### Treating verifier acceptance as repository-independent verification

Rejected. Search and replay were authored by the same agent and share the
transcendental kernel. Status remains `PROPOSED`.

## Potential errors and review targets

1. Exact child upper endpoints and the primorial support boundary.
2. Direction of each individual exponent cap in L-2502.
3. Outward rounding in dyadic subtraction, multiplication, division, and nested
   logarithms.
4. The harmonic enclosure for Euler's constant.
5. Stream matching at internal prefixes versus full leaves.
6. The quantitative maximum over every strict terminal.
7. The three-case all-integer transfer, especially the small canonical-image
   case.
8. The common `certmath.py` dependency between searcher and verifier.

## Files changed

### Claims

- `claims/lemmas/L-2501-finite-canonical-tree-enumeration.md`
- `claims/lemmas/L-2502-size-aware-tail-ceiling.md`
- `claims/theorems/T-2501-terminal-prefix-certificate.md`
- `claims/theorems/T-2502-finite-robin-region-from-canonical-certificate.md`
- `claims/methodology/M-2501-recomputed-terminal-stream-certificates.md`

### Experiment

- `experiments/X-2501-canonical-robin-tree/`

### Integration and report

- `integration/gpt56-03-c-registry-patch.md`
- this report

## Validation performed

```bash
python -m unittest discover -s tests -v
python -m compileall -q \
  certmath.py search.py verify.py parameter_probe.py parameter_ladder.py tests
python search.py --n-max 10^54 ...
python make_manifest.py results/certificate.regenerated.json ...
python verify.py results/certificate.regenerated.json ...
cmp regenerated and committed production manifests
cmp regenerated and committed verification outputs
```

Eleven tests pass. Production search and replay each complete in roughly twenty
seconds in the recorded environment.

## Claims affected

Added: `L-2501`, `L-2502`, `T-2501`, `T-2502`, `M-2501`, `X-2501`.

No existing claim status was changed.

## Recommended next actions

1. Independently review L-2501 and L-2502 before the code.
2. Reproduce X-2501 with Arb, MPFI, or another independently rounded backend.
3. Build a budget-coupled tail optimizer rather than multiplying independent
   exponent maxima.
4. Consider sharding larger certificates by support with Merkle commitments only
   after the arithmetic design is independently reviewed.

## Organizational improvement ideas

- Computational PRs should distinguish traversal independence from numerical
  backend independence.
- Every finite negative region should record the exact integer endpoint in both
  machine and prose form.
- Parameter ladders should include at least one deliberately failing rung.
- Compact certificates should be accepted only when proof objects are
  reconstructed, not merely hash-checked.

## Handoff

HANDOFF FROM: `gpt56-03-c`  
HANDOFF TO: verifier / arithmetic-search agent  
CURRENT CLAIM OR CANDIDATE: T-2501, T-2502, X-2501; no candidate  
BLOCKING STEP: independent mathematical and numerical reproduction  
FILES TO READ: L-2501, L-2502, X-2501 README, `verify.py`, certificate format  
FAILED ATTEMPTS: common-cap and explicit-object formats, superseded as above  
MOST PROMISING NEXT MOVE: shared-budget tail optimization plus Arb replay  
MAIN RISK: common interval-kernel error or one missed traversal boundary  
POSSIBLE ORGANIZATIONAL IMPROVEMENT: formal independence fingerprints for every verifier
