# Actual validation and limits

## Completed finite reconstruction

On the FINAL source, these four commands pass:

```sh
python -B check.py --check results.json
python -B test_check.py
python -O -B check.py --check results.json
python -O -B test_check.py
```

Both complete reconstructions produce canonical SHA-256

`e3283ada16bf0f8ca184de9430a4ec7a5013bbeb78dfef69efa340e152350857`.

The corpus is exactly Y=7,15,31,63,95. It covers 14,440 new annular cells in
total and checks 14,651 reconstructed Newton coefficients counting overlaps
between panels. The largest native endpoint is 9,215. The largest auxiliary
harmonic argument is below 1,572,864 and belongs to an explicit PERIODIC MODE
activation tail, not a Mobius computation at that height.

All B amplitudes come from the short prefix and its prescribed completion.
The producer uses the gcd/divisibility formula. An independent finite
reconstruction convolves the scaled integer source and checks EVERY recovered
product coefficient. All prime-log centering coefficients cancel exactly.
The Newton prefix is generated from those products and compared coefficient
by coefficient with a separate full sieve. The generated Newton coefficients,
not future sieve values, are then used to accumulate the native energy.

The high-mode values in the finite panels are evaluated by complementary
algebra AFTER those checks. They are not an independent summation of every
large-denominator mode at every observation point. That method and scope are
recorded beside each panel in results.json.

## Arithmetic contract

- Python integers and exact Fraction source/divisor algebra.
- 112-bit dyadic endpoints with explicit floor/ceiling arithmetic.
- Harmonic sums enclose every reciprocal summand; no quadrature or interpolation.
- Logarithms use range reduction and a positive rational atanh series with an
  explicit bound for its complete remaining tail.
- Activation points use integer eleventh roots / exact integer comparisons.
- Every norm and mixed term is outward enclosed. Descriptive README decimals
  are NOT the authoritative enclosures.
- No floating-point, mpmath, zeta oracle, numerical integration or supplied zero
  data enters accepting reconstruction. The exploratory binary64 script used
  before writing the checker is not included or counted as proof evidence.

The finite fixed-sector upper comparison uses the ACTUAL rational Fourier
coefficient mass and an explicit elementary separation bound. It does not
numerically evaluate or optimize the infinite Euler constant C_0 in the proof.

## Twelve-method test suite, in each mode

Tests cover integer roots and independent Mobius/divisor primitives; native
cubic point bounds through 512; exact smooth-prime deletion; native U and B
bounds at five declared small cutoffs; prime-power threshold tensors; exact
Ramanujan period variances and increments; 243 ternary finite tail maps under
three lower endpoints; activation commutators; directed logs/harmonic arithmetic;
exact rational Farey separation row bounds; complete small native decompositions
and typed-result mutations; and one real CLI refusal.

The real CLI test generates and accepts a Y=7-only report, alters its energy,
then reconstructs and rejects it. It is ONE refusal per test mode, not a fresh
full five-panel campaign for every mutation. Additional report mutations are
in-process comparisons with freshly reconstructed data. Duplicate keys and
bool/integer type aliases are rejected. There are zero skips.

## Artifact checks

The DSE27 supplied full proof was authenticated against its Git blob
`ba792e61cb4dcddf1f86e74b286370c2cf0c48dd` before using it as the parent source.
The new packet has a SHA256SUMS inventory. Clean ZIP extraction and an add-only
local Git fixture replay are recorded by the publication receipt in the PR.
Those checks authenticate the exact local deliverable, not the whole repository.

## What was NOT done

No independent mathematical referee, second author, Lean/formal build,
whole-repository checkout/validator, remote CI, Windows/macOS run, full earlier
DSE27/RCB26/NSR26 campaign, or unbounded native high-composite estimate.
The infinite theorems are written proposed proofs; they are NOT inferred from
these tests. Same-author alternate arithmetic paths are not external review.
The previously published larger native mesh calculation was NOT extended.

A packaging-only attempt to look up a directory with Git's index-file syntax
failed. The subtree was then resolved from the actual write-tree object.
No mathematical source or accepting result was changed by that correction.
