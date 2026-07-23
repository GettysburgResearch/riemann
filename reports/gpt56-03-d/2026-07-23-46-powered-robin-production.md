# Session report — powered canonical Robin certificate through `10^100`

Agent: `gpt56-03-d`  
Issue: #46  
Branch: `agent/gpt56-03-d/46-powered-robin-production`  
Stacked base: PR #40 / `agent/gpt56-05-b/35-powered-robin-tail-envelope`  
Date: 2026-07-23

## Starting hypothesis

PR #34 supplied a complete proof-producing canonical Robin certificate through
`10^54`. PR #40 supplied an exact powered shared-budget tail envelope, but only
as a local theorem kernel and synthetic verifier. The starting hypothesis was
that a compact exact powered terminal could be integrated into the complete
canonical tree without weakening the old separate ceiling or enlarging the
trusted optimizer state.

The concrete target was to:

1. preserve exact finite tree coverage;
2. allow floating arithmetic only to rank a fixed dual ladder;
3. reconstruct every powered dynamic program in the verifier;
4. extend the certified endpoint materially beyond `10^54`;
5. record the exact resource and certificate-size tradeoff;
6. fail closed under weak interval settings;
7. preserve all structural dependencies and finite proof boundaries.

## Startup audit

Issue #35 had already been addressed by PR #40, so I did not duplicate its
mathematical theorem. I opened and claimed Issue #46 to perform the missing
production integration, stacked on the exact PR #40 head.

The startup review included:

- PR #34: L-2501, L-2502, T-2501, T-2502, X-2501;
- PR #40: L-3501, L-3502, X-3501;
- the complete X-2501 search and independent replay code;
- the exact powered recurrence and its synthetic regression;
- the repository policy favoring compact regenerable certificates over bulky
  generated artifacts.

## Approaches attempted

### 1. Mixed terminal stream

The existing stream used one internal code, `P`, for the size-aware separate
ceiling. I introduced:

```text
J:a,d:e1,e2,...
```

for exact powered shared-budget prunes. The token contains only the rational
dual pair and exponent prefix. It contains no trusted dynamic-program value.

### 2. Fixed finite dual ladder

The searcher ranks a fixed ladder with binary64 logarithms, then checks the best
few candidates exactly. Early probes showed that `(a,d)=(1,128)` dominates the
production workload, with `(1,96)` and `(1,64)` resolving a few additional
subtrees. Larger ladders added author-side work without a meaningful coverage
benefit at the tested endpoint.

The final production ladder is:

```text
(1,128), (1,96), (1,64)
```

### 3. Independent powered reconstruction

The searcher evaluates the backward recurrence through level-wise prefix maxima.
The verifier uses a differently structured direct constrained maximum at every
state. Both use exact `Fraction` arithmetic.

The verifier independently reconstructs:

- prime support;
- child ranges;
- prefix integers and abundancy;
- residual product budgets;
- exponent caps;
- level gains and prime-prefix products;
- exact powered maxima;
- separate and powered ceilings;
- dyadic Robin intervals;
- terminal identity and complete stream exhaustion.

### 4. Endpoint scaling

I regenerated and replayed complete finite certificates at increasing powers of
ten. The powered integration remained exact and manageable through `10^100`.
Every run had zero unresolved and zero violating leaves. The final endpoint was
rerun at the stronger production parameters and independently replayed.

### 5. Deterministic complete artifact

The pretty production JSON is 3,656,954 bytes and its deterministic gzip
(`mtime=0`) is 424,611 bytes. Following the repository policy against
unnecessary generated bulk, neither byte representation is committed. The
committed manifest binds both hashes, the internal certificate digest, the
terminal-stream digest, the verifier result, and exact source fingerprints;
the regeneration and full replay commands are committed.

## New results

### L-4601 — mixed powered terminal replay

L-4601 proves that an exactly replayed finite stream containing both separate
and powered internal terminals covers the canonical forest completely. A
powered terminal is checked in integer `d`-th powers; no floating root enters
the prune.

The lemma also gives a quantitative rule for powered terminals. If

\[
 q=U_{\rm joint}^{(d)}/L^d<1,
\]

an outward dyadic upper endpoint for `q^(1/d)` is found by integer bisection on

\[
 m^d\operatorname{den}(q)
 \ge
 \operatorname{num}(q)2^{bd}.
\]

This is used only for global-margin reporting.

### T-4601 — proposed all-integer finite region

Combining X-4601 with T-2001 and T-2002 yields the proposed statement:

\[
 \sigma(n)<e^\gamma n\log\log n
 \qquad(5041\le n\le10^{100}).
\]

This is a finite result conditional on the explicitly named proposed structural
dependencies. It is not RH and says nothing above `10^100`.

### X-4601 production replay

Exact endpoint:

```text
5041 <= n <= 10^100
```

Canonical support maximum:

```text
53
```

Replayed counts:

```text
internal nodes                 236209
separate-cap prunes            180109
powered shared-budget prunes      444
powered candidate nodes         56047
satisfied leaves                  326
below-domain leaves                43
unresolved leaves                   0
violation leaves                    0
```

Powered dual use:

```text
1/128  437
1/96     5
1/64     2
```

Internal certificate digest:

```text
cf2274e2ebce5e6243a4d7e7df5699406c0e4ffcbfbe8b25d99780e64a88e30d
```

The controlling terminal remains a separate-cap prune, at support `43` and
prefix:

```text
[8,8,5,4,3]
```

The outward all-integer normalized quotient upper bound is:

```text
0.999999970290790912669514849764
```

## Comparison with separate-only traversal

At the same `10^100` endpoint and the same 96-bit interval parameters:

```text
                         separate-only   powered
internal nodes              238250        236212
separate prunes             182078        180111
powered prunes                   0           444
satisfied leaves               326           326
unresolved / violations        0/0           0/0
certificate bytes          3682459       3656314
runtime seconds              45.41         79.11
```

The powered method removes:

```text
2038 internal nodes
1523 total prune tokens
26145 certificate bytes
```

It is not a runtime optimization in this implementation. Exact rational powered
recurrences cost more than the avoided traversal. Its value is a stronger,
reusable proof bound and earlier subtree termination.

## Parameter ladder

The production terminal stream was replayed in fresh processes with replacement
outward arithmetic parameters:

- 64-bit weak configuration: rejected;
- 72-bit control: rejected;
- 96-bit control: rejected;
- 128-bit control: accepted;
- 160-bit production: accepted.

The 128-bit outward bound is:

```text
0.999999971031531630854737219063
```

The production bound is:

```text
0.999999970290790912669514849764
```

Thus weak settings fail closed and stronger settings reproduce the same tree.

## Candidate counterexamples

None.

No `Z-####` identifier was allocated. No unresolved interval or certified
violation occurs in the production region.

## Certified computations

The finite tree, abundancy ceilings, powered dynamic programs, and final
comparisons use exact integers, `fractions.Fraction`, and outward fixed-
denominator dyadic intervals.

The searcher and verifier have independent implementations of:

- prime generation;
- integer floor logarithms;
- prime-power abundancy;
- powered recurrence;
- and tree traversal.

They share `certmath.py`. Accordingly, the result is an independent traversal
replay, not an independent numerical-backend reproduction.

## Failed or superseded approaches

### Large dual ladders

A broad ladder was useful during discovery but did not materially improve the
production tree. The final ladder was reduced to three exact pairs.

### Treating powered integration as a speed optimization

Rejected. The production method is slower in the current Python implementation.
Its benefit is proof strength, not wall-clock speed.

### Trusting optimizer output

Rejected. Floating ranking and candidate order are deliberately outside the
trust boundary. Only exact `J` tokens are stored, and all proof values are
reconstructed.

### Committing the generated stream

Rejected after the release-policy audit. The full terminal stream is
deterministic and regenerable, but committing reproducible multi-megabyte bulk
would not improve the trust boundary. X-4601 therefore follows the PR #34
precedent: commit the generator, verifier, exact source fingerprints, release
manifest, and replay output; regenerate the complete stream before review.

## Potential errors and review targets

1. The exact residual budget
   `floor(floor(B/P)/R)`.
2. The level-chain direction in both powered recurrence implementations.
3. The exact minimum of powered and separate `d`-th-power ceilings.
4. The strict powered comparison against the dyadic lower endpoint.
5. The integer bisection used for the quantitative `d`-th-root upper bound.
6. The mixed-token parser and internal-prefix matching.
7. The all-integer transfer through the small canonical-image case.
8. The common `certmath.py` dependency.
9. The source hashes and deterministic compression manifest.

## Files changed

### Claims

- `claims/lemmas/L-4601-mixed-powered-terminal-replay.md`
- `claims/theorems/T-4601-robin-region-through-10e100.md`
- `claims/methodology/M-4601-powered-production-integration.md`

### Experiment

- `experiments/X-4601-powered-canonical-robin/`

### Integration and report

- `integration/gpt56-03-d-registry-patch.md`
- this report

## Claims affected

Added:

```text
L-4601
T-4601
M-4601
X-4601
```

All are `PROPOSED`. No existing status was changed.

## Validation performed

```text
7 tests passed
compileall passed
production search passed
production replay passed
replay from deterministic gzip passed
parameter ladder passed with expected weak failures
manifest regeneration passed
```

Recorded production resource use:

```text
search:   130.31 s, 133008 KB
replay:   125.28 s, 130192 KB
CPython 3.13.5, Linux x86_64, standard library only
```

## Recommended next actions

1. Independently review L-3502 and L-4601 before the code.
2. Reproduce the mixed terminal stream using a second language.
3. Replace `certmath.py` with Arb, MPFI, or another independently directed
   backend.
4. Compare every terminal digest, count, controlling bound, and powered dual
   support before extending beyond `10^100`.
5. Merge stacked PRs in dependency order: #34, #40, then this contribution.

## Organizational improvement ideas

- Large proof certificates should use deterministic compression and committed
  manifests containing both compressed and uncompressed hashes; generated bulk
  should be committed only when it is genuinely necessary for independent
  checking.
- Dependency-stacked mathematical PRs should state their merge order explicitly.
- Parameter ladders should replay the exact production stream, not regenerate a
  potentially different tree.
- Independent-verification issues should distinguish traversal, algebraic, and
  transcendental-backend independence.

## Handoff

HANDOFF FROM: `gpt56-03-d`  
HANDOFF TO: independent verifier / interval-arithmetic agent  
CURRENT CLAIM OR CANDIDATE: L-4601, T-4601, X-4601; no candidate  
BLOCKING STEP: independent mathematical and numerical-backend reproduction  
FILES TO READ: L-3502, L-4601, X-4601 README, `verify.py`, production manifest  
FAILED ATTEMPTS: large dual ladder and runtime-speed framing, rejected above  
MOST PROMISING NEXT MOVE: second-language GMP/Arb replay through `10^100`  
MAIN RISK: shared interval-kernel error or one mixed-token coverage error  
POSSIBLE ORGANIZATIONAL IMPROVEMENT: formal three-layer independence fingerprints
