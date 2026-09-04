# Review checklist

Mark each item with reviewer, date, evidence path, and exact SHA.

## A. Provenance

- [ ] Riemann base is `6dda8b5125457ed936330229f8c9eb6491728e76`.
- [ ] Gitlink resolves to `AxiomMath/ZetaZeros@4bcaf70e544506c311d83a5a5b143a134b9fc5f7`.
- [ ] Upstream commit signature is independently verified.
- [ ] Submodule worktree is clean.
- [ ] Apache-2.0 attribution is preserved.
- [ ] Current arXiv version is identified explicitly.
- [ ] Paper PDF SHA256 is recorded.
- [ ] Rendered paper pages were visually inspected.

## B. Build and kernel trust

- [ ] Exact Lean `v4.34.0-rc2` toolchain installed.
- [ ] `lake exe cache get` completed.
- [ ] `lake build ZetaZeros` completed from clean bytes.
- [ ] Production modules contain no `sorry` or `admit`.
- [ ] Challenge placeholders are not imported by production.
- [ ] Comparator succeeds for all six targets.
- [ ] Nanoda succeeds.
- [ ] `#print axioms` output is archived.
- [ ] The minimal upstream CI is not misreported as a Comparator run.

## C. Abstract theorem semantics

- [ ] `IsAdmissible` matches the paper's regularity, support, parity, and normalization.
- [ ] `testKernel eta = Fourier(eta^2)` uses the correct Fourier sign and `2*pi`.
- [ ] `IsConjInvariant` correctly represents a multiset support plus multiplicity.
- [ ] Every support point has positive multiplicity.
- [ ] `simpleRealPart` means real and multiplicity exactly one.
- [ ] The ordered double sum has the correct multiplicity factor.
- [ ] The real part and square placement match Proposition 2.1.
- [ ] The constants `2`, `3/2`, and `1/2` match.
- [ ] Nonemptiness hypotheses are neither missing nor unnecessarily strengthened.
- [ ] The Hilbert/Bessel proof has no hidden finite-dimensionality assumption.
- [ ] Complex-to-real inner-product conversions are checked.
- [ ] All Bochner integral and `MemLp` hypotheses are sufficient.

## D. Zeta transfer semantics

- [ ] Nontrivial zero set is exactly `0 < Im rho <= T`.
- [ ] Zeros are counted with analytic multiplicity.
- [ ] Functional-equation reflection preserves the encoded set and multiplicity.
- [ ] Rescaled point is real iff `Re rho = 1/2`.
- [ ] Difference scale is `i(rho-rho') log T/(2*pi)`.
- [ ] Ordered-pair convention matches BGST.
- [ ] Diagonal pairs are treated consistently.
- [ ] Rational weight is `4/(4-(rho-rho')^2)`.
- [ ] The derivative correction removes the weight exactly.
- [ ] No boundary term is lost in Fourier differentiation.
- [ ] The cutoff approximation preserves admissibility.
- [ ] Riemann-von Mangoldt normalization agrees with `zeroCount`.
- [ ] Eventual denominator positivity is proved.
- [ ] Strict versus non-strict final percentages are correct.

## E. External analytic inputs

- [ ] Titchmarsh/Riemann-von Mangoldt source theorem is pinned.
- [ ] An exact adapter to `ZetaZeros.RiemannVonMangoldt` is proved or the premise remains explicit.
- [ ] BGST paper/version and Lemma 5 are pinned.
- [ ] BGST regularity assumptions imply `IsPairTestFunction` for every used test.
- [ ] BGST error is uniform in exactly the manner encoded.
- [ ] Fourier and zero normalizations match.
- [ ] Off-line zeros and multiplicities are included exactly as required.
- [ ] An exact adapter to `ZetaZeros.PairCorrelation` is proved or the premise remains explicit.

## F. Montgomery-Taylor constant

- [ ] Exact cotangent expression is derived symbolically.
- [ ] Smooth cutoff convergence is justified.
- [ ] The cited extremal theorem applies to the exact admissible class.
- [ ] `montgomeryTaylorConst_lt` is independently replayed.
- [ ] Decimal corollaries prove only `> 0.6725` and `> 0.83625`.
- [ ] No claim says retuning the same scalar class can improve the exact constant.

## G. Riemann integration boundary

- [ ] No file under `canonical/` is modified.
- [ ] No new claim ID is entered into the trusted registry.
- [ ] No formal-v0.1 release module imports Lean 4.34 code.
- [ ] Abstract and zeta-specific theorem layers remain separate.
- [ ] Positive density is not called complete capture.
- [ ] Density one is not called RH.
- [ ] Frame completeness is not inferred from a global count.
- [ ] Aggregate Hilbert positivity is not used as coefficientwise positivity.
- [ ] Links to PR #785 and PR #786 preserve their firewalls.
- [ ] Any future repair receives a new identity and exact-SHA review.

## H. RH-facing proposals

For every proposed architecture:

- [ ] finite-exception dilution is addressed;
- [ ] local/effective thresholds are stated;
- [ ] test-function support is justified;
- [ ] prime-side errors are controlled;
- [ ] the integer step from small defect to zero defect is explicit;
- [ ] low zeros are covered by directed finite verification;
- [ ] no external input equivalent to RH is hidden under generic notation.

## Current disposition

```text
abstract Hilbert theorem: high-priority review candidate
zeta transfer theorem: conditional formal theorem
Riemann-von Mangoldt inside package: not discharged
BGST pair correlation inside package: not discharged
trusted-spine import: not ready
RH: unproved
```
