# Executed reviewer checks and evidence boundary

## Fresh computation

`independent_checks.py` was written for this review. It does not import or execute any research packet. It uses Python integers, Fraction and exact SymPy algebra; even the bounded primality test uses integer square root. Acceptance uses explicit exceptions, not assert statements removed by Python optimization.

```sh
python -I -B independent_checks.py > checks.normal.json
python -I -B -O independent_checks.py > checks.optimized.json
cmp checks.normal.json checks.optimized.json
```

These commands completed on Linux, Python 3.13.5 and SymPy 1.14.0. Both outputs are byte-identical and report `PASS_REVIEWER_EXACT_RECONSTRUCTIONS` with 14,926 checks.

| Group | Checks | Actual scope |
|---|---:|---|
| Jordan | 22 | Rational polynomial identities, endpoint margins, scalar constants and Gamma rational regrouping |
| Arithmetic | 1799 | Möbius/floor and harmonic-work identities through 512; compact-prefix balance in the declared finite panel |
| Hardy | 4 | Safe-jet and projected-kernel rational identities |
| Projection | 58 | Exact finite rational Grams and nonzero-floor countercontrols |
| Square grid | 9 | Cell weights, constants, causal inverse and cumulative-level countercontrol |
| Budgets | 53 | Fractional exponents, finite exceptional-arc budgets and perturbation norm margins |
| Entropy | 14 | Sharp ramp factorization and finite jet-filter variation identities |
| Operator | 3 | General/special residual and periodic dual normalization constants |
| Torsion | 12964 | All 4320 affine residue rows, graph/exception comparison and additional finite progression checks |

The 4320 affine rows represent complete equations F+k Delta=0 for every nonnegative integer k, using the separately reviewed exact rank-period argument. Their successful comparison is more than sampling a large rank cutoff. The checker reports 560 admitted affine families, 24 nongraph families, and zero isolated additional nonnegative quotients. These are finite proof-data counts, not counts of curves or new theorems.

### Exact published computation identities

- `independent_checks.py`: Git blob `ba55815ce21f6aa5716e7b3024a2f9d34fcc0144`; SHA256 `1a9fd82d44c2c70d2328362485d4c2b81b601af3507cd9d21e6f9462548dc26b`; 12742 bytes.
- Each JSON result: Git blob `f48693ed48b5644ecf7265e212f92b7a1414fd79`; SHA256 `61f1689f64f8a73395bbf50e34609bb5308773cbd06c6018ccb86095a3fbb514`; 1904 bytes.

The reviewer implementation is independent of the authors' checker implementations. It is not an independently verified Python/SymPy kernel and is not a formal proof of any infinite analytic statement. Historical author test counts have not been added to these totals.

## External analytic interfaces checked

- [NIST DLMF 25.9](https://dlmf.nist.gov/25.9): the approximate functional equation gives the coarse critical-line convexity input used in the capture discussion. This does not supply a reciprocal-zeta critical bound.
- [NIST DLMF 5.11(ii)](https://dlmf.nist.gov/5.11#ii): complex digamma remainder is bounded by the first omitted term times the stated secant factor. With the paper's shift and right-half-plane argument, its conservative factor is compatible with that contract. All numerical uses in WP still need replay.
- [Yamada, arXiv:2312.16090v1](https://arxiv.org/html/2312.16090v1), introduction: confirms the classical Montgomery--Vaughan C=2 interval Brun--Titchmarsh input. No improved numerical constant or external calculation was imported.
- [Brent, Platt and Trudgian, arXiv:2008.06140](https://arxiv.org/abs/2008.06140): the authors explicitly assume RH for the upper mean-square bound. Only that hypothesis direction was checked here; the numerical constant and its zero computation were not replayed. Full HTML retrieval failed; no full-paper or PDF audit is claimed.

Hardy factorization, outer cyclicity, classical BSY, Riesz/Friedrichs theory, Paley--Wiener/Jensen, Euler--Maclaurin and reductive-group highest weights remain the stated classical analytic/algebraic inputs, not newly formalized theorems. LC's exact Littlewood source confirmation remains in pass two.

## Not performed

No complete repository checkout was obtained: direct Git access failed DNS resolution in this runtime. There was no authenticated full-checkout integration run, no source-package-wide replay, no fresh numerical WP or IE certificate, no Lean/comparator/axiom audit, and no CI success. Mathematical paper review is not replaced by the bounded code, and bounded code is not described as an executed author campaign.

The finite copied-backend certificates in the research submissions require source/rounding/coverage review even when they have good manifests and author rejection tests. That is a concrete second-pass task, not an allegation that their reported results are false.
