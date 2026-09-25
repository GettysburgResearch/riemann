# Validation

## Executed locally

Both of the following ran successfully with Python's standard library only:

```sh
python -I -S -B check.py --output results.json
python -I -S -B completion_certificate.py --output completion_receipt.json
```

Optimized-mode replays also passed:

```sh
python -I -S -B -O check.py --output results_optimized.json
cmp results.json results_optimized.json
python -I -S -B -O completion_certificate.py --check completion_receipt.json
```

The algebra receipts were byte-identical in ordinary and optimized modes. The million-scale completion receipt was reconstructed and compared successfully in optimized mode. The checks do not depend on Python `assert`, which optimized mode could disable.

`check.py` records 210,560 predicates. Its scope is:

- exact gcd/lcm boundary identities and support on every basis vector for cutoffs 1 through 48 and dilation factors 2 through 9;
- exact first-exit and orthogonality identities, including all six factor orders of 2,3,5 at selected cutoffs;
- exact residue Fourier banks for moduli 2 through 16;
- exact cyclotomic change-of-factor-order matrices for 2x3, 2x5 and 3x5;
- literal Möbius Euler coefficients through 4095;
- augmented simplicial chain, filtered basis, and Euler/barcode identities through 4095;
- rational-cell checks of spatial lcm masks and masked dilation products;
- actual rejected shortcuts: omitted boundary, coarse-source replacement, two-prime joint-defect positivity, and an impossible finite normalized tracial state.

The general proofs are in RESEARCH.md. The finite checks alone do not establish their unbounded versions.

## Million-scale quantitative certificate

`completion_certificate.py` reconstructs the prime list through 1,000,000 by an integer sieve, partitions it by exact integer-power tests, and lower-rounds every analytic log-amplitude contribution to a rational with denominator 2^40.

The resulting log-amplitude lower numerator is 45,547,501,421,928. The denominator is 1,099,511,627,776. Rational Taylor lower bounds for exp(14) and exp(414/5), together with the written resonant-interval argument, establish a full completion energy greater than 10^33.

The actual native Möbius coefficients are computed separately. The identity mu * 1 = delta is then authenticated coefficientwise at all one million positions. Outward dyadic summation encloses the native head energy between the exact rationals recorded in the receipt, and verifies that its upper endpoint is below 2.

The optional small-completion scout enumerates up to 2^20 divisors of the first-twenty-prime primorial and computes its full energy as a single exact rational. It is not used to extrapolate or prove the million-scale bound.

A receipt whose claimed lower energy was deliberately altered was rejected by a full recomputation. This is a receipt-consistency test, not a proof assistant checking the analytic lemmas.

## Not executed or not established

No pre-existing repository validator, CI workflow, Lean proof, external certificate suite, or independent mathematical review was run. The note's analytic inequalities and use of Mellin Plancherel are written proofs rather than machine-formalized derivations.

No native asymptotic energy improvement, full covariance estimate, zero-free half-plane improvement, Weil-form positive factorization, or RH proof is claimed.

## Scientific interpretation

The full-prime completion lower bound is an obstruction to a particular auxiliary norm. It does not lower-bound the true infinite Möbius source's energy at that scale. The completed coefficients agree with the native source only through the stated prefix, and the enormous certified excess is explicitly assigned to the non-native tail.
