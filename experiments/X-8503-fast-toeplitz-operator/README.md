# X-8503 — Hybrid fast/directed Toeplitz source and operator moat

## Purpose

The completed X-2805 production run certifies one recovered `K=1024` vector
strictly positive at

```text
c = 10^11
T = 94184072727073 / 20.
```

X-8503 changes the next target from another scalar replay to a reusable
**vector-independent coefficient artifact**. The desired output is:

1. one exact Gaussian-rational midpoint vector for all 1,024 Toeplitz lags;
2. one complete prime-source operator radius;
3. exact coverage and source-count metadata;
4. canonical parameter, normalization, budget, and shard hashes.

That artifact can feed:

- arbitrary postselected vectors and Gram portfolios through L-7501;
- circulant completions through L-8501;
- the one-direction Schur closure through L-8502;
- the complement congruence producer from L-8504.

No eigenvector belongs in the source computation.

## Mathematical reduction

For stored coefficients `c_d`, with nonzero lags equal to twice the corresponding
upper-diagonal matrix entries,

```text
||S(c)-S(c_mid)||_2
    <= |Delta c_0| + sum_{d=1}^{K-1} |Delta c_d|.
```

This is L-8503. The shift matrices have norm one, so there is no factor `K`.
Every source term deposits into at most two neighboring lags, and their hat
weights sum to one.

L-8505 specializes the reviewed PR #82 arithmetic to vector-independent deposits
and proves the static target-wide late-source budget

```text
B_fast,op < 1 / 17,000,000
          < 5.84e-8.
```

This is conditional on the exact declared arithmetic operation order and ABI. A
midpoint producer with changed code or compilation contract needs a new budget.

## Target source partition

The committed plan is

```text
experiments/X-8503-fast-toeplitz-operator/certificates/
  target-hybrid-source-plan.json
```

and fixes:

```text
directed ordinary segments  [0,2000)
fast ordinary segments      [2000,5000)
higher prime powers         exactly one fully directed stream
```

The complete expected counts are:

```text
ordinary primes             4,118,054,813
higher prime powers             28,156
all terms                   4,118,082,969
```

The prime-source operator gate is `999/1,000,000`. This reserves enough room for
the alpha radius and the nonprime correction while keeping the final L-8502
operator distance below `1/1000`.

## Files

### `fast_toeplitz_shard.cpp`

Vector-independent binary80/binary128 midpoint producer for late ordinary-prime
segments. It reuses:

- MPFR segment setup;
- four positive odd atanh terms for local logarithms;
- degree-five reciprocal-square-root polynomial;
- binary128 phase-grid reduction with `M=32768`;
- cubic phase Taylor reconstruction;
- balanced pairwise binary80 accumulation.

The terminal operation emits two complex lag deposits instead of contracting
against a historical vector.

It refuses segments below 2000 and fails if the support coordinate enters the
declared knot guard.

### `verify_operator_budget.py`

Standard-library exact checker for the L-8505 static budget. It reconstructs

```text
term hardware sum
pairwise accumulation sum
phase-location budget
phase-Taylor budget
algebraic truncation budget
```

and proves their sum is below `1/17,000,000` by rational arithmetic.

### `bind_fast_shard.py`

Binds a raw producer output to the exact source plan. It checks:

- arithmetic contract;
- phase/log/square-root orders;
- parameter and normalization fingerprints;
- licensed segment range;
- lag count and order;
- source counts and zero guarded-boundary count.

It adds the redundant human-readable target fields and a canonical
`binding_sha256`.

### `merge_hybrid_source.py`

Exact base merger for:

- directed coefficient rectangles;
- bound fast midpoint shards;
- exactly one higher-power stream.

It constructs rational coefficient midpoints, converts directed rectangle radii
to coefficient-`l1` operator radius, adds the global fast budget once, and rejects
coverage or count failures.

Lag zero uses only its real component, matching X-0801's Hermitian Toeplitz map.

### `merge_hybrid_source_strict.py`

Proof-facing wrapper. Before calling the base merger it recomputes:

- the exact L-8505 verification self-hash declared by the plan;
- every fast shard's `binding_sha256`;
- every order and arithmetic-contract field.

The final reference hash includes this strict-binding ledger.

## Static reproduction commands

```bash
python experiments/X-8503-fast-toeplitz-operator/verify_operator_budget.py \
  experiments/X-8503-fast-toeplitz-operator/certificates/target-static-budget.json \
  --output /tmp/operator-budget.json

cmp \
  experiments/X-8503-fast-toeplitz-operator/results/target-static-budget.verification.json \
  /tmp/operator-budget.json

python -m unittest discover \
  -s experiments/X-8503-fast-toeplitz-operator/tests -v
```

## Producer build

The reviewed compilation contract is:

```bash
g++ -O3 -std=c++20 -Wall -Wextra -Werror \
  -frounding-math -ffp-contract=off -fno-fast-math \
  experiments/X-8503-fast-toeplitz-operator/fast_toeplitz_shard.cpp \
  -o /tmp/fast_toeplitz_shard \
  -lmpfr -lgmp -lquadmath
```

A target control segment is:

```bash
/tmp/fast_toeplitz_shard \
  --manifest experiments/X-2805-directed-prime-producer/results/target-c1e11/vector/target-autocorrelation.txt \
  --start-segment 2000 \
  --end-segment 2001 \
  --phase-grid 32768 \
  --setup-precision 192 \
  --output /tmp/segment.raw.json

python experiments/X-8503-fast-toeplitz-operator/bind_fast_shard.py \
  /tmp/segment.raw.json \
  experiments/X-8503-fast-toeplitz-operator/certificates/target-hybrid-source-plan.json \
  --output /tmp/segment.bound.json
```

## Full merger shape

After all declared shards exist:

```bash
python experiments/X-8503-fast-toeplitz-operator/merge_hybrid_source_strict.py \
  experiments/X-8503-fast-toeplitz-operator/certificates/target-hybrid-source-plan.json \
  experiments/X-8503-fast-toeplitz-operator/results/target-static-budget.verification.json \
  <all directed and bound-fast shard JSON files> \
  --output /tmp/target-reference.json
```

The merger succeeds only when the exact full counts and the complete half-open
coverage partition are present.

## Trust boundary

Exact in the Python checkers:

- integer and rational parsing;
- canonical hashes;
- coverage and source counts;
- coefficient midpoint addition;
- rectangle-radius conversion;
- static global error composition;
- strict operator-gate comparison.

Producer obligations not proved merely by JSON:

- correctness of prime enumeration;
- adherence to the reviewed C++ straight-line operation order;
- compiler and hardware conformance;
- absence of a shared bug with the reference directed producer;
- complete directed early and higher-power coefficient outputs.

At least one overlapping late range should be independently evaluated by the
fully directed producer and checked against the fast midpoint plus its apportioned
static moat before production acceptance.

## Current status

The theorem kernels, exact budget checker, binder, strict merger, target plan,
producer source, and adversarial tests are committed. The complete hybrid
coefficient run has **not** been claimed. GitHub Actions had not published a run
for the new workflow at the end of the authoring session, so no CI execution is
reported here.

## Completion target

Once the complete reference artifact exists:

1. compute the exact L-8502 projection residual;
2. require it below `1/5000`;
3. produce the L-8504 rational congruence certificate for complement bound
   `7/1000`;
4. compose the complete source, alpha, and correction radii below `1/1000`;
5. invoke L-8502 with the already certified fixed-direction moat.

Those checks settle the entire recovered `K=1024` finite matrix, not merely one
vector.
