# X-2501 — Proof-producing canonical Robin tree through `10^54`

Experiment ID: X-2501  
Status: PROPOSED certified computation; independent repository review pending  
Agent: `gpt56-03-c`  
Issue: #25  
Branch: `agent/gpt56-03-c/25-canonical-robin-search`  
Stacked base: PR #24  
Date: 2026-07-23

## Research question

Can T-2002's complete canonical reduction be converted into a finite search artifact whose coverage, every subtree cut, every leaf sign, and global margin are replayed rather than trusted?

## Production result

The deterministically regenerated certificate, bound by the committed production manifest, covers every vector

\[
n=\prod_{i=1}^{K}p_i^{a_i},
\qquad a_1\ge\cdots\ge a_K\ge1,
\qquad n\le10^{54}.
\]

The exact primorial support limit is `K<=33`; the last required prime is 137. The search and replay produced:

| Class | Count |
|---|---:|
| rigorous size-aware subtree prunes | 29,818 |
| individually satisfied leaves above 5040 | 173 |
| leaves at or below 5040 | 43 |
| unresolved leaves | 0 |
| certified violation leaves | 0 |
| reconstructed internal nodes | 37,476 |
| terminal tokens | 30,034 |

The replay verifier exhausted every support stream and independently reproduced all counts, classifications, quantitative summaries, and the canonical-JSON certificate digest

```text
4927ea262cdfe5e455bf06e5af7bad65053e2cbd99561f34b6c7da8f2a7856e6
```

The pretty-printed regenerated file has SHA-256

```text
da4ac520a3bd688aa1f9755aaf5afee9775bba3ea059e82ecee66c442e0c142f
```

No Robin violation and no `Z-####` candidate were found.

## Global canonical margin

T-2501 converts every strict terminal into an exact rational normalized-quotient upper bound and takes their maximum. The controlling terminal is the support-26 subtree prefix

```text
[20, 10]
```

with minimum completion

```text
2403037304674479534031999475991983647519832801280
```

and outward decimal display

\[
C_{\mathrm{can}}<0.999997639970216146706942918996.
\]

The exact numerator and denominator are bound by `results/production-manifest.json` and independently reproduced in `results/verification.json`.

## Conditional all-integer consequence

T-2502 combines the canonical certificate with the proposed parent claims T-2001 and T-2002. The three replayed case bounds are

\[
C_1<0.902862776173950207045935482547
\]

for `5041<=n<=5582`,

\[
C_2<0.999991801829451542482515901233
\]

when `n>=5583` but the canonical image is at or below 5040, and

\[
C_{\mathrm{can}}<0.999997639970216146706942918996
\]

when the canonical image exceeds 5040.

The canonical case controls. Therefore, conditional on the explicitly named structural dependencies, every integer

\[
5041\le n\le10^{54}
\]

satisfies Robin's strict inequality.

This is a finite negative search region, not RH, not an asymptotic result, and not evidence that no larger counterexample exists.

## Exact tree coverage

L-2501 proves the child rule. At support `K`, prefix integer `P`, and next prime `p`, the next exponent is visited exactly when the all-ones completion remains at most the exact integer bound and the exponent does not exceed the previous one. Integer powers determine the range; no rounded logarithm participates in coverage.

The verifier generates primes using a separate routine, recomputes the exact primorial support limit, and derives every child range independently.

## Size-aware prune

L-2502 uses the finite product budget. At a nonempty prefix ending in exponent `A`, every remaining prime `p_i` receives the exact cap

\[
m_i=\min\left(A,\max\left\{e\ge1:Pp_i^e\prod_{\ell\ne i}p_\ell\le10^{54}\right\}\right).
\]

The exact rational ceiling is

\[
U=I(P)\prod_i I(p_i^{m_i}).
\]

If the dyadic lower bound at the all-ones minimum completion `N_min` proves

\[
U<e^\gamma\log\log N_{\min},
\]

then monotonicity proves the entire bounded subtree safe.

## Certificate architecture

The schema is summarized in `CERTIFICATE_FORMAT.md`.

### Untrusted searcher

`search.py` emits compact terminal streams in deterministic DFS order. It may use ordinary binary64 only as a one-sided discovery filter; no prune is emitted until exact rational versus dyadic comparison proves the sign.

### Replay verifier

`verify.py` does not import the search traversal. It independently reconstructs prime generation and the exact support bound, every child exponent range, exact integers and prime-power abundancy factors, every size-aware tail cap and rational ceiling, every dyadic Robin interval and strict sign, complete token coverage and exhaustion, the global canonical bound and three all-integer case bounds, and the full certificate digest.

### Shared arithmetic kernel

Both programs use `certmath.py`, a pure-integer fixed-denominator dyadic kernel. It evaluates logarithms by the positive atanh series with a rational remainder, Euler's constant using

\[
\frac1{2(n+1)}<H_n-\log n-\gamma<\frac1{2n},
\]

and exponentials by a positive Taylor series with a geometric remainder. Every operation is outward rounded.

The shared kernel is a deliberate, recorded common dependency. Acceptance by `verify.py` is a strong independent traversal replay, not a second independent numerical implementation.

## Reproduction

From this directory:

```bash
python -m unittest discover -s tests -v
python -m compileall -q certmath.py search.py verify.py parameter_probe.py parameter_ladder.py make_manifest.py tests

python search.py \
  --n-max 1000000000000000000000000000000000000000000000000000000 \
  --bits 256 \
  --log-terms 88 \
  --exp-terms 88 \
  --harmonic-cutoff 250000 \
  --output results/certificate.regenerated.json

python make_manifest.py \
  results/certificate.regenerated.json \
  --output results/production-manifest.regenerated.json

python verify.py \
  results/certificate.regenerated.json \
  --output results/verification.regenerated.json

cmp results/production-manifest.json results/production-manifest.regenerated.json
cmp results/verification.json results/verification.regenerated.json
```

The parameter ladder can be reproduced with

```bash
python parameter_ladder.py results/certificate.regenerated.json --output results/parameter-ladder.regenerated.json
```

The environment's individual command limit required the committed ladder to be run one rung per fresh process. `parameter_probe.py` is the exact rung worker.

## Validation

Eleven unit tests pass. They include exact prime and prime-power controls, `exp(log 2)` interval containment, the 5041 finite-barrier calibration, independent replay acceptance, brute-force one-terminal coverage for every small canonical vector, rejection of missing and reordered tokens, rejection of an unlicensed root prune, and rejection of a forged tightest-terminal summary.

Parameter ladder:

| Rung | Result | All-integer bound display |
|---|---|---:|
| 64 bits, 8 terms, cutoff 100 | rejected: first unsupported prune | — |
| 72 bits, 10 terms, cutoff 200 | accepted | 0.999999723346049113525195510597 |
| 96 bits, 16 terms, cutoff 1,000 | accepted | 0.999997723302014639663473840250 |
| 160 bits, 56 terms, cutoff 30,000 | accepted | 0.999997640061475190585510482156 |
| 256 bits, 88 terms, cutoff 250,000 | accepted | 0.999997639970216146706942918996 |

The deliberately weak rung fails closed, while increasing strength converges to the production bound.

## Recorded resource use

Local production environment:

```text
CPython 3.13.5
Linux x86_64
standard library only
```

Observed run resources:

```text
search:   19.97 s, 114192 KB maximum resident set
verifier: 20.39 s, 114332 KB maximum resident set
```

These are performance observations, not proof dependencies.

## Proof boundary

- The exact finite boundary is `10^54`.
- No conclusion is made above it.
- No counterexample was found.
- The computation is submitted as `PROPOSED` pending independent code and arithmetic review.
- The all-integer consequence inherits the review status of T-2001 and T-2002.
