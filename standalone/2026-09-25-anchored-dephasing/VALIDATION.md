# ADP37 validation

## Successful executions

The final standard-library producer and checker ran normally and optimized:

```sh
python -I -S -B check.py --output receipt.json
python -I -S -B -O check.py --check receipt.json --output /mnt/data/adp37_optimized.json
cmp receipt.json /mnt/data/adp37_optimized.json
python -I -S -B test_replay.py
python -I -S -B -O test_replay.py
```

The full receipts were byte-identical. Both eight-method CLI suites passed with no failures, errors, or skips. Each suite includes pristine normal and optimized FULL child replays; an actual harmonic endpoint changed by one is rejected by a fresh FULL replay. The remaining refusals use a separately labeled quick-control campaign: altered coverage, altered primitive hash, missing field, duplicate key, NaN and malformed JSON. Quick controls never replace the published full campaign.

## Exact finite scope

The full receipt counts **126,102 explicit predicates**, dominated by **123,840 finite alias classifications**. This number is a coverage description, not a confidence score or evidence of proximity to RH.

- Mobius coefficients through 1,024: prime-sieve generation and separately implemented triangular Dirichlet inversion. A genuinely corrupted primitive is passed into the authentication routine and rejected.
- All 256 rectangles 1<=L_1,L_2<=16: complete product-collision enumeration versus gcd/totient formula and harmonic upper bound. Coverage is 18,496 ordered products, separate from predicate counts.
- All unordered index pairs through 128 at anchors Y=2,...,16: canonical alias representatives versus direct integer-power comparison. Perfect-power-base substitution and ungrouped alias diagonals are explicitly rejected.
- Five exact Gaussian-rational Fejer/direct identities at K=1,2,3,5,9, with all 45 Gram entries. These rational unit phases test the finite identity and conjugation; they are NOT claimed to be the actual logarithmic orbit of a single real tau.
- Native cap/product panels Y=3,7,15,31,63,127,255: complete product coefficients, collision-energy budgets, and exact rational product-kernel reconstructions. The rational kernel in these panels is clearly labeled a structural bump, not the centered harmonic kernel.
- Two ACTUAL centered-harmonic panels, H=1 and X=L^2:
  * Y=5, L=6, observations k=36,...,71, K=116;
  * Y=7, L=8, observations k=64,...,127, K=250.
  All nonzero product coefficients and every observation in these blocks are included. There are 620 product/observation cells and 62 off-diagonal phase pairs over the large- and small-K checks. No future native Mobius values are used to define their sources.
- The actual anchored frequencies are 2pi j/log Y. Directed Fejer Gram evaluations meet the finite mean bound. At K=3, direct phase enumeration and the independent Gram expression have overlapping intervals with difference width below 10^(-20). This enclosure consistency checks numerical normalization; finite overlap alone is not a proof of exact identity.
- Rational verification of all final constants in the all-scale negative harmonic rectangle, coefficient cap, cardinality, and invisibility conditions. The all-L counterexample is a written analytic proof, not a numerical simulation at L=8192 or beyond.

The 33,533 ordered source products used in the replay are recorded as arithmetic coverage, not added to the predicate count.

## Actual harmonic results (illustrations only)

The exact 100-bit dyadic endpoints in receipt.json are authoritative. Approximate display values are:

| Native cutoff | Product diagonal D | Principal energy | Principal / D |
|---|---:|---:|---:|
| Y=5 | 0.00035426423165503404 | 0.0005175355459342564 | 1.4608743973854192 |
| Y=7 | 0.0005867230440155246 | 0.0008607514831333905 | 1.4670490479501521 |

The finite large-K means are approximately 0.0003542826655266382 and 0.0005875979014070276 respectively. These two small panels test the implementation; they do NOT suggest an all-scale bound on the native ratio.

## Arithmetic contract

Acceptance uses integer/Fraction arithmetic, exact Gaussian rationals, and outward-rounded dyadic intervals with 100 fractional bits. No float or high-precision black-box special function is used in acceptance.

- Pi is enclosed by 16 arctan(1/5)-4 arctan(1/239), with 48 alternating terms per arctangent and the signed next-term enclosure. Machin's identity fixes the correct branch.
- Logarithms are reduced to [1,2], then evaluated by 64 positive atanh terms. The remaining tail is bounded above by 2(1/3)^129/[129(1-1/9)]. Every addition, multiplication, division and range reduction is outward.
- Sin/cos arguments are reduced modulo one turn, with a certified reduced radian magnitude at most 4. Forward Taylor recurrences run through power 81/80. The absolute remainder bounds are 4^83/83! and 4^82/82! respectively. This avoids unstable fixed-grid Horner rounding of tiny high-degree coefficients.
- The harmonic logarithmic centering is evaluated as 2log(2sin(pi/n)), not dropped or replaced by a finite uncentered sum. Exact phase-log ratios are enclosed before trig evaluation.
- Both normal and optimized modes use explicit runtime guards, never Python assert for checker acceptance. Duplicate JSON keys and nonfinite constants are rejected.

## Development failures caught before publication

An initial producer run failed reciprocal balance because a missing sparse coefficient used integer zero followed by Python division, introducing a float. The fallback was changed to Fraction(0); the balance guard had already rejected the run. A subsequent run failed the actual harmonic envelope because fixed-grid interval Horner evaluation amplified rounding widths catastrophically near pi. Forward Taylor recurrences repaired the interval algorithm; the envelope was not relaxed. Neither failed run produced an accepted final receipt. All successful executions above used the repaired producer.

## Review boundary

The universal averaging estimate and the actual-harmonic nonnative counterexample are written proofs, with the named classical inputs; finite replay alone does not prove them. No independent mathematical review, proof-assistant verification, repository-wide validator, remote CI verdict, other-platform run, complete inherited-campaign replay, native principal-phase upper bound, full-frequency covariance estimate, or RH proof is claimed. Publication hashes authenticate a snapshot, not mathematical truth.
