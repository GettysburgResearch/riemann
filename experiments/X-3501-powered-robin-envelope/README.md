# X-3501 — Exact powered Robin tail envelope

Status: exact optimizer-kernel prototype; no RH counterexample and no new finite
Robin region are claimed.

## Purpose

This experiment implements `L-3501` and `L-3502` using only Python integers and
`fractions.Fraction`.

The bounded canonical tail

```text
A >= b_1 >= ... >= b_n >= 1
```

is encoded by nested prefix lengths at exponent levels `2,...,A`. For exact
integers `a>=0,d>=1`, the verifier reconstructs the rational weights

```text
W[r,ell] = G[r,ell]^d / Q[ell]^a
```

and runs the backward max-product recurrence

```text
V[r,m] = max_{0 <= ell <= min(m,n_r)} W[r,ell] V[r+1,ell].
```

The shared residual product budget occurs once as `M0^a`. The resulting proof
object is an upper bound on the `d`-th power of every completion's abundancy.
No logarithm, irrational root, floating ordering, or trusted optimizer table
enters verification.

## Files

- `verify.py` — standalone exact producer/checker for schema
  `riemann.robin-powered-tail.v1`;
- `certificates/synthetic-powered-prune.json` — exact optimizer regression;
- `tests/test_verify.py` — exhaustive and adversarial tests.

## Regression

The committed synthetic regression uses:

```text
prefix        = 2^4
remaining     = 3,5,7
integer bound = 8400
caps          = 2,2,1
a,d           = 1,64
```

The separate-cap ceiling is exactly

```text
12493 / 3150 ~= 3.9660317460.
```

The powered joint envelope is strictly below `(39/10)^64`, while the separate
ceiling is not below `39/10`. Thus the joint method certifies the synthetic
threshold and the separate method does not.

Exhaustive enumeration gives the true maximum `403/105`, attained at exponents
`(2,1,1)`. Exhaustion is used only as a test; the verifier does not rely on it.

The rational target `39/10` is deliberately synthetic. It is not represented as
an enclosure of `exp(gamma) log log(N_min)` and therefore proves no Robin range.
A production certificate must replace it with the existing independently
checked outward lower enclosure.

## Run

From this directory:

```bash
python verify.py certificates/synthetic-powered-prune.json
python -m unittest discover -s tests -v
python -m compileall -q verify.py tests
```

Expected certificate status:

```text
CERTIFIED_PRUNE
separate_alone_prunes = false
powered_strictly_improves_separate = true
```

## Verification boundary

The checker validates:

1. consecutive canonical prime support beginning at `2`;
2. nonincreasing positive prefix exponents;
3. the exact mandatory-tail and residual budgets;
4. all size-aware exponent caps;
5. every prime-power abundancy ratio;
6. every rational dynamic-program maximum;
7. the separate and powered ceilings;
8. the final strict powered comparison.

It rejects altered proof values, support gaps, malformed fractions, invalid
primes, unreachable mandatory tails, and claimed statuses inconsistent with the
exact comparison.

The current prime checker has an explicit unsigned-64-bit contract. This covers
the support sizes in the present finite-region search but must be revisited if a
future canonical support contains larger prime factors.

## Tests

Six tests pass:

- joint-only synthetic prune;
- altered powered numerator rejection;
- nonconsecutive support rejection;
- exact domination of exhaustive optima on three small boxes and three dual
  parameters;
- exact recovery of the `403/105` regression optimum;
- fail-closed behavior for a deliberately weak dual parameter.

## Next production experiment

Integrate the verifier kernel beside X-2501 without importing its traversal.
At each node:

1. compute the old `L-2502` ceiling;
2. try a small deterministic ladder such as `d in {16,32,64,128}` and nearby
   integers `a`;
3. retain the exact minimum of the old and powered ceilings;
4. store a powered certificate only when it strictly improves the prune;
5. have the independent verifier recompute the dynamic program from the node
   prefix and global bound.

The first scientific benchmark is the largest `B` for which the complete
canonical certificate remains finite and independently replayable, compared
against the current `10^54` boundary.