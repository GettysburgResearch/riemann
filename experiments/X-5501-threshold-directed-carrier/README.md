# X-5501 — Threshold-directed piecewise-carrier search and fixed-vector replay

Status: mixed empirical discovery, exact integer manifests, and directed
fixed-vector controls. No counterexample was found.

## Purpose

This experiment implements Issue #55's six requested stages:

1. rank prime-power thresholds by the exact L-5501 endpoint susceptibility;
2. search only first next-threshold microcells and selected full deposition
   endpoints;
3. bound smooth old-prime motion and build the exact L-5502 knot mesh;
4. freeze selected complex modes to exact 48-bit dyadic vectors;
5. replay every admitted prime power with MPFR directed phases and accumulation;
6. compare the exact-vector interval against the `2.5e-10` nonprime gate.

The executed complete control window is

```text
T = 94184072727073 / 20
K = 1024
10^8 < q <= 1.02*10^8
```

The repository does not currently contain the `c=10^11` PR #44 leading vector,
so X-5501 does not fabricate a production replay at that cutoff.

## Main results

### Ranking

`108,536` prime-power thresholds were ranked. The top ordinary-floating
nomination was

```text
q = 100011547
signed endpoint susceptibility = 5.429893639161426e-7
isolated full-first-cell drop   = 9.767867593186754e-9
```

Ranking is empirical because the baseline eigenvector and phases are ordinary
floating data.

### Complete first-microcell exclusion

For

```text
threshold = 100013561
cutoff    = 100013578
```

an exact 48-bit dyadic vector was replayed over all

```text
5,762,210 primes
1,404 higher prime powers
5,763,614 total terms
```

at 192 MPFR bits. The directed right-endpoint leading margin is approximately

```text
[0.0066414786110346293, 0.0066414786110346302].
```

The directed background/event envelope gives

```text
whole first microcell leading margin > 0.0065451574898472229.
```

After the vector-scaled `2.5e-10` gate, this is a certified positive control on
that exact vector throughout the microcell.

### Top-ranked full deposition endpoint

For the top-ranked threshold, the limiting strict integer endpoint is
`101828730`. A separately frozen dyadic vector was replayed over `5,862,050`
terms. Its directed endpoint margin is approximately

```text
[0.0065827830732268066, 0.0065827830732268075].
```

This certifies only the endpoint vector value. Many later thresholds enter
inside that long cell, and the coarse whole-cell bound is unresolved.

## Files

- `discover.py` — ordinary discovery, ranking, microcell search, dyadic export,
  and empirical knot mesh;
- `manifest.py` — exact segmented prime/higher-power manifest and digests;
- `directed_replay.c` — complete MPFR-directed fixed-vector producer;
- `verify.py` — exact standard-library serialization, manifest, vector, gate,
  and sign checker;
- `validate_small.py` — independent 100-decimal small-cutoff formula control;
- `CERTIFICATE_FORMAT.md` — schemas and proof boundary;
- `certificates/` — exact dyadic vectors and manifests;
- `results/` — rankings, directed intervals, summary, tests, and hashes;
- `tests/test_verify.py` — fail-closed exact tests.

No compiled binary is committed.

## Discovery reproduction

Requires Python 3, NumPy, SciPy, mpmath, and enough memory for the `10^8` prime
arrays.

```bash
python discover.py
python manifest.py --cutoff 100013578 \
  --output results/manifest-microcell.json
python manifest.py --cutoff 101828730 \
  --output results/manifest-rank1-endpoint.json
```

Discovery output is not proof.

## Directed producer build

A normal build should use MPFR/GMP development headers:

```bash
gcc -O3 -march=native -fopenmp directed_replay.c \
  -lmpfr -lgmp -lm -o directed_replay
```

The source contains a documented ABI fallback for the repository's current
x86-64 execution image, which supplies `libmpfr.so.6` without headers:

```bash
gcc -O3 -march=native -fopenmp directed_replay.c \
  -Wl,-l:libmpfr.so.6 -lgmp -lm -o directed_replay
```

The exact-int128 backend deliberately accepts only `bits<=48`,
`dimension<=2048`, and coordinate magnitudes at most `2^bits`.

Representative producer command:

```bash
./directed_replay \
  certificates/vector-microcell.txt \
  100013561 100013578 192 5 \
  56aab2547d590e9c3af84c59f7b84ebeabd8aab4ba09b67ba917933c738b3910 \
  76d23c38b2b5cbf45f6d9f018fcb01c68454fb1b05f43f929b504dd396620d8d \
  > results/replay-microcell-p192.json
```

The producer regenerates the complete prime set and every higher prime power.
It evaluates `log`, `sqrt`, `pi`, the exact rational carrier product, sine,
cosine, hat interpolation, and accumulation with outward MPFR rounding.

## Exact checker

```bash
python verify.py \
  results/replay-microcell-p192.json \
  certificates/vector-microcell.json \
  certificates/manifest-microcell.json

python -m unittest discover -s tests -v
python -m compileall -q discover.py manifest.py verify.py validate_small.py tests
```

Nine tests pass. The checker reconstructs the exact vector norm and adjacent
correlation bound, binds manifest/vector digests, checks outward interval
algebra, reconstructs the uniform gate by exact fractions, rejects status
promotion, and checks the independent small control.

## Phase enclosure

For each exact phase interval `[phi_lo,phi_hi]`, the producer evaluates sine and
cosine at the lower endpoint with MPFR and expands by the phase width. Since
both functions are 1-Lipschitz, this encloses the full short arc without
requiring a trusted floating remainder operation.

## Manifest completeness

The committed manifests are generated by an independent segmented Python
implementation and hash:

- every prime as an unsigned big-endian 64-bit integer;
- every higher prime power as `(q,p,a)` in `>QQI` encoding;
- the two sequence hashes, cutoff, and counts into one combined digest.

The replay checker requires exact count agreement and the bound manifest digest.

## Proof boundary

The directed results are finite exact-vector controls conditional on the
proposed L-4202/L-4203 analytic correction formulas. They do not prove the full
matrix positive and do not support RH generally.

A negative result would still require independent verification of:

- D-0801 Guinand--Weil admissibility;
- source signs and normalization;
- an independent directed producer or reproduction.

No `Z-####` candidate is allocated.
