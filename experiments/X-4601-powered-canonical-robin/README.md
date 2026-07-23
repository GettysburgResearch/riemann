# X-4601 — Powered proof-producing canonical Robin certificate through `10^100`

Experiment ID: X-4601  
Agent: `gpt56-03-d`  
Issue: #46  
Stacked dependencies: PR #34, PR #40  
Status: PROPOSED certified computation pending independent reproduction  
Date: 2026-07-23

## Research question

Can the exact powered shared-budget envelope of L-3502 be integrated into the
complete X-2501 canonical traversal, independently replayed, and used to extend
the finite all-integer Robin certificate substantially beyond `10^54`?

## Result

The production stream covers every canonical exponent vector

\[
 n=\prod_{i=1}^{K}p_i^{a_i},
 \qquad
 a_1\ge\cdots\ge a_K\ge1,
 \qquad
 n\le10^{100}.
\]

The exact support maximum is `K=53`. Search and independently written replay
agree on:

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

The powered dual usage is:

```text
(1,128)  437
(1, 96)    5
(1, 64)    2
```

The complete certificate has internal digest

```text
cf2274e2ebce5e6243a4d7e7df5699406c0e4ffcbfbe8b25d99780e64a88e30d
```

and is committed as a deterministic gzip artifact. Its uncompressed and
compressed hashes are recorded in `results/production-manifest.json`.

No violation and no unresolved sign was found. No `Z-####` candidate is created.

## Conditional all-integer consequence

The canonical stream is combined with the exact finite barriers and canonical
dominance from stacked PR #24. The three all-integer cases are:

1. `5041<=n<=5582`;
2. `n>=5583` with canonical image at most `5040`;
3. canonical image between `5041` and `10^100`.

The third case controls. The outward normalized quotient bound is

```text
0.999999970290790912669514849764
```

Therefore, conditional on the explicitly named proposed structural claims,
Robin's strict inequality holds for every integer

```text
5041 <= n <= 10^100.
```

This is an exact finite negative-search region. It is not RH and makes no claim
for larger integers.

## Mixed terminal format

The deterministic terminal stream uses:

```text
P:e1,e2,...       separate-cap subtree prune
J:a,d:e1,e2,...   exact powered shared-budget subtree prune
S:e1,e2,...       rigorously satisfied leaf
B:e1,e2,...       leaf at or below 5040
U:e1,e2,...       unresolved leaf
V:e1,e2,...       certified violation leaf
```

A `J` token stores no dynamic-program table. The verifier reconstructs:

- the exact prefix integer and abundancy;
- the remaining consecutive primes;
- the exact residual product budget;
- every finite exponent cap;
- every level gain and prefix product;
- every exact rational dynamic-program maximum;
- the separate and powered ceilings;
- the outward Robin lower interval;
- and the final strict comparison in integer `d`-th powers.

The dyadic `d`-th-root ceiling is used only to summarize the global normalized
margin. The prune itself is checked without taking a numerical root.

## Search and verifier independence

The searcher and verifier do not share traversal code.

| Component | Searcher | Verifier |
|---|---|---|
| Prime generation | division by previously found primes | trial division by all candidate divisors |
| Integer floor logarithm | repeated multiplication | repeated exact exponentiation |
| Prime-power abundancy | geometric closed form | explicit finite sum |
| Powered recurrence | prefix-max implementation | direct constrained maximization |
| Tree traversal | author DFS | independently written replay DFS |
| Transcendentals | `certmath.py` | `certmath.py` |

The common final row is an explicit common-mode dependency. This is independent
traversal replay, not an independently implemented numerical backend.

## Production parameters

```text
integer upper endpoint  10^100
bits                    160
log terms               56
exp terms               56
harmonic cutoff         30000
powered dual ladder     (1,128), (1,96), (1,64)
root upper bits         192
```

Ordinary binary64 arithmetic ranks candidate duals and screens obvious failures.
It never authorizes a terminal. Every emitted terminal is exact rational plus
outward dyadic arithmetic.

## Separate-only comparison

At the same endpoint and the same 96-bit outward arithmetic, a separate-only
control and the powered search give:

| Quantity | Separate only | Powered |
|---|---:|---:|
| Internal nodes | 238250 | 236212 |
| Separate prunes | 182078 | 180111 |
| Powered prunes | 0 | 444 |
| Satisfied leaves | 326 | 326 |
| Unresolved / violations | 0 / 0 | 0 / 0 |

Thus the powered ceiling removes 2,038 internal nodes and 1,523 total terminal
prune records. It costs more author-side exact rational arithmetic; recorded
runtime rises from 45.41 seconds to 79.11 seconds in the local environment. The
proof value is earlier, stronger subtree termination and a reusable exact
shared-budget token—not a claim of runtime speedup.

See `results/mode-comparison.json` for exact counts, sizes, and the proof
boundary.

## Reproduction

From this experiment directory:

```bash
python -m unittest discover -s tests -v
python -m compileall -q \
  certmath.py search.py verify.py pack_release.py \
  parameter_probe.py parameter_ladder.py tests

python search.py \
  --n-max 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 \
  --bits 160 \
  --log-terms 56 \
  --exp-terms 56 \
  --harmonic-cutoff 30000 \
  --duals 1/128,1/96,1/64 \
  --root-upper-bits 192 \
  --output results/certificate.production.regenerated.json

python verify.py \
  results/certificate.production.regenerated.json \
  --output results/verification.regenerated.json

python pack_release.py \
  results/certificate.production.regenerated.json \
  --compressed results/certificate.production.regenerated.json.gz \
  --manifest results/production-manifest.regenerated.json \
  --verification results/verification.pack.regenerated.json \
  --verification-input results/verification.regenerated.json
```

The committed compressed certificate can be checked directly:

```bash
python verify.py \
  results/certificate.production.json.gz \
  --output results/verification.from-gzip.json
```

Compare hashes and summaries against `results/production-manifest.json` rather
than trusting filenames.

## Parameter ladder

`parameter_ladder.py` replays the same terminal stream in fresh processes with
replacement interval parameters. It does not regenerate optimizer decisions.
A deliberately weak rung is expected to reject; stronger accepted rungs must
reconstruct every terminal.

```bash
python parameter_ladder.py \
  results/certificate.production.json.gz \
  --output results/parameter-ladder.regenerated.json
```

## Adversarial tests

The committed suite checks:

- exact shared-budget domination by exhaustive enumeration on a synthetic tail;
- strict improvement over the separate ceiling;
- agreement between differently structured powered recurrences;
- complete replay of a small production-format certificate;
- rejection after changing a powered dual pair;
- rejection after deleting a terminal;
- rejection of a forged quantitative summary even after refreshing the digest;
- and fail-closed replay under deliberately weak arithmetic parameters.

## Resource record

Production search:

```text
130.31 seconds
133008 KB maximum resident set
```

Production replay:

```text
125.28 seconds
130192 KB maximum resident set
```

Environment:

```text
CPython 3.13.5
Linux x86_64
Python standard library only
```

Runtime is environment-specific and is not part of the mathematical result.

## Proof boundary

- Every finite tree and powered comparison is submitted as a proposed certified
  computation pending independent review.
- T-2001, T-2002, and L-3502 retain their repository statuses.
- Search and replay were authored by the same agent.
- Both share `certmath.py`.
- No counterexample was found.
- Nothing here proves or disproves RH.
- No inference is made above `10^100`.

## Files

```text
certmath.py
search.py
verify.py
pack_release.py
parameter_probe.py
parameter_ladder.py
CERTIFICATE_FORMAT.md
tests/test_engine.py
results/certificate.production.json.gz
results/production-manifest.json
results/verification.json
results/parameter-ladder.json
results/mode-comparison.json
results/runtime.txt
results/tests.txt
results/SHA256SUMS
```
