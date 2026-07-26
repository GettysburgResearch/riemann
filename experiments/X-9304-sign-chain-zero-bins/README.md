# X-9304 — Total-count-saturated Hardy-Z sign-chain zero bins

Agent: `gpt56-08`  
Issue: #93  
Status: exact checker and proof-producing workflow committed; production sign pending workflow artifact

## Objective

Convert one exact total-zero count and one directed Hardy-Z sign table into a
complete family of pairwise-disjoint critical-line zero bins, then feed those
bins into the existing X-9301 zero-deflated direct-`xi` witness checker.

The central theorem is `L-9305`:

```text
exact total multiplicity m
+ m certified Hardy-Z sign alternations
= exactly one simple critical-line zero in each sign interval.
```

No indexed zero locator is needed.  Each bin is narrowed by exact-dyadic
bisection, retaining only halves whose directed endpoint signs remain opposite.

## Files

```text
verify_sign_chain.py
    Standard-library exact checker.  Evaluates no special function and uses no
    floating point.

build_sign_chain_certificate.py
    Reads an exact X-5604 total-count artifact and an approximate guide list,
    creates exact dyadic sample points, and evaluates directed Hardy-Z balls.
    The guide chooses points only; it cannot manufacture an alternation.

refine_hardy_z_bins.py
    Parallel python-flint/Arb bisection producer.  An interval containing zero
    is unresolved and is never assigned a sign.

build_x9301_from_sign_chain.py
    Converts a verified, strictly separated sign-chain table into the existing
    X-9301 direct-xi zero-deflation certificate schema.

tests/test_verify_sign_chain.py
    Exact fail-closed adversarial tests.

certificates/synthetic-saturated-chain.json
    Three-root exact synthetic control with refinement steps.
```

## Production target

The exact PR #71 data are

```text
slab lower       75347258181331 / 16
slab upper       37673629090985 / 8
target ordinate  20225875608341108140435 / 2^32
exact total N    172
```

The reviewed X-5604 computation found 173 directed nonzero Hardy-Z samples with
172 sign alternations and no undecided sign.  The workflow recomputes rather
than trusting those summary numbers.

## Hosted proof workflow

```text
.github/workflows/pr71-saturated-sign-chain.yml
```

The workflow performs, in order:

1. 192- and 256-bit exact total counts;
2. a fresh 173-sample directed Hardy-Z chain;
3. exact checker replay;
4. 28 rounds of parallel refinement for all 172 bins;
5. strict pairwise-separation verification;
6. 192- and 256-bit direct completed-`xi` rectangle production;
7. nearest-2, 4, 8, 16, 32, 64, 128 and complete-172 zero-deflation ladders;
8. exact X-9301 contractions and precision nesting;
9. a summary that nominates only a strict directed negative.

Every generated source, count, sign table, primitive rectangle, certificate,
verification result, and timing log is hashed and uploaded.

## Local exact control

The standard-library layer needs no third-party package:

```bash
python experiments/X-9304-sign-chain-zero-bins/verify_sign_chain.py \
  experiments/X-9304-sign-chain-zero-bins/certificates/synthetic-saturated-chain.json

python -m unittest discover \
  -s experiments/X-9304-sign-chain-zero-bins/tests -v
```

The production and refinement scripts require python-flint/Arb.

## Certificate semantics

A production chain records:

```text
exact slab endpoints
multiplicity-aware total-count interval isolating one integer
total-count artifact digest
exact ordered dyadic samples
directed Hardy-Z intervals excluding zero
canonical sign-table digest
optional sign-preserving refinement history
optional target ordinate and squared-distance upper bounds
```

The checker reconstructs every sign and every retained half.  It does not trust
declared sign labels or final bin endpoints.

The bridge refuses zero bins that overlap or even touch.  This is stricter than
`L-9305`, whose open bins may share certified nonzero sample endpoints, because
the parent X-9301 transport schema deliberately requires disjoint closed bins.
The production workflow therefore refines every bin before binding.

## Proof boundary

A negative X-9301 row after this pipeline is a finite RH-disproof nomination,
not an automatically verified counterexample.  Promotion still requires:

1. independent review of `L-7501`, `L-7504`, `L-9301`, and `L-9305`;
2. independent total-count and Hardy-Z reproduction;
3. independent completed-`xi` rectangle production;
4. exact normalization review;
5. strict interval nesting and a final upper endpoint below zero.

A positive result excludes only the declared ordinate, node table, row family,
and finite set of 172 certified slab zeros.
