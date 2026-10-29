# Fixed-face obstruction in the PR #94 scalar return

**Status:** Proposed exact arithmetic lemma, with an executable rational check; independent review pending. This is a limitation of a specified return certificate, not a limitation on zero-free regions or on other methods.

**Source and domain.** Use [PR #94 at commit e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4](https://github.com/GTimG/QuasiRiemannTracker/tree/e5a82f72d8ff39a3cc1ad044e6acd727e77a3fc4/submissions/2026-10-29-arvi-density/src/Submissions/arvi_density), in particular `Return/Constants.lean`, `Return/Formulas.lean`, `Return/Windows.lean`, `ReturnD/Schedule.lean`, and `ReturnD/TransportGeometry.lean`. Retain its 31 counting windows, count and physical faces, `Ebase` and count formulas, and the physical conductor capacity. Allow the physical slot cap and the positive floor reserve to vary arbitrarily. Suppose the remaining `BoundsN` geometry is retained, so `873/1000 < theta <= T*`, with `T* = 8317278773899883959247/9517760867980200000000 = 0.8738692733793095…`, `793/1000 < h < 806/1000`, `ell = 11/3 - 4 theta`, and `kappa = 2 theta - 1`. (The equality for ell is forced by the geometry's signal-boundary and x+y identities.)

**Claim.** The `new_rows` scalar inequality in `PhysicalSchedule` cannot hold throughout its required parameter domain. In fact, it already fails at `d=h`, `delta=223/500`, `p=1/2` even if its positive `rowFee` is removed. Thus this exact source face and window family cannot reach theta at or below `T*` within the stated box by retuning slot cap or floor saving. Relative to PR #94's reported `0.87387234`, that is a strict ceiling of `29187362404488421/9517760867980200000000`, approximately `0.000003066621`, on possible improvement within these interfaces. Other source faces, count windows, parameter boxes, proofs, and zero-free methods are not covered.

**Proof.** `h>793/1000>19/25=dMinus` and `h<dp=h+10^-10`, so `d=h` lies in the new-row range. The selected point is in `[0,3/4] × [0,1/2]`. Inspection of all 31 declared windows shows that precisely windows 7, 12, 14, 15, 16 and 17 are available there, all branch C. These windows have identical branch count. The envelope is attained by either the old count or an available window; the former is at least the C count on the entire stipulated kappa range. Hence the envelope is at least

```text
R_C = 137478360780643/225606975000000.
```

For the old count the derivative in kappa is `225828309 / (1000 (12729 kappa - 1831)^2) > 0`, and at `kappa=373/500` it exceeds `R_C` by `2927366587426695869/864620006308575000000`. This proves the comparison because `theta>873/1000` implies `kappa>373/500`. The old-count denominator is positive throughout this interval. The comparison even remains valid if some or all C windows are discarded.

For any slot cap, `newCapacity(h)` is at most the physical conductor line `(physicalB*h-4*ell)/physicalLambda`, where `physicalB=49283557/50000000` and `physicalLambda=4503/2000`; this follows directly from `y=h-2*ell` and the minimum in the source's capacity. Since `delta*p>0`, replacing the capacity by this upper bound lowers `Ebase`, and replacing the count envelope by `R_C` also lowers `rowAt`. Call the resulting row exponent minus theta `G(theta,h)`. It is affine, with exact slopes

```text
∂G/∂h     = -11447677710517817/1354544277900000000 < 0,
∂G/∂theta = -5273419/1125750 < 0.
```

At the upper corner `(theta,h)=(T*,0.806)`, `G` is exactly zero; because the coefficient of `h` is strictly negative and `h<0.806`, the gap is strictly positive throughout the stated domain. As a concrete example, at `(theta,h)=(0.87386,0.806)` the gap equals

```text
88261806706387247/2031816416850000000000 > 0.
```

Consequently the required `rowAt <= theta-rowFee`, even weakened to `rowAt <= theta`, is impossible. This is a necessary failure of the source's particular sufficient certificate: it does not disprove any underlying analytic estimate, L-function nonvanishing statement, or differently formulated return.

**Reproduction.** With SymPy 1.14.0, run `python research/exploratory/2026-10-29-arvi-return/check_fixed_face_obstruction.py`. It reruns the existing exact edge check, identifies the six matching source windows, checks the two count expressions, derivative and slopes, and verifies the positive rational corner gap and the exact threshold `T*`. The imported `GenericCount.envelope_attained` and source count formula are read from the pinned Lean files; this note does not itself build those analytic or Lean dependencies.

An independent agent checked the source window mapping, envelope choices, kappa and strict h ranges, and affine calculation. Its separately written `independent_obstruction.py` parses the actual pinned `Windows.lean` and reproduces the threshold. This is a source and arithmetic review, not a Lean proof of the obstruction or a review of the underlying analytic estimates.

**Independent source check.** `independent_obstruction.py` separately parses the 31 windows from the pinned source, checks its SHA-256 `3d436434bf8a76f2246f12bb942840f33e4d8ce3d2155660e4572dccab15a799`, reconstructs the count and physical line, and verifies the same threshold. It also verifies that capC's upper-plain-length admission guard is strictly negative at the chosen point; this does not rule out a new analytic count that replaces that guard. With the exact PR94 source file available locally, run:

```text
python research/exploratory/2026-10-29-arvi-return/independent_obstruction.py --windows /path/to/submissions/2026-10-29-arvi-density/src/Submissions/arvi_density/Return/Windows.lean
```

At the illustrative corner `theta=0.87386`, `h=0.806`, the same bin requires capacity at least `2467396034273387/50310355425000000 ≈ 0.04904350235`, whereas the current physical line supplies only `8215820413/168862500000 ≈ 0.04865390725`. With the count envelope held fixed at `R_C`, this one row would require `physicalB >= 80026480008237061661/81100292945100000000 ≈ 0.9867594444` if `physicalLambda` stays `4503/2000`; alternatively, holding physicalB fixed would require `physicalLambda <= 5511211267813337207/2467396034273387000 ≈ 2.233614382`. These are necessary comparisons at this one parameter point, not sufficient conditions for an improved source or a zero-free theorem. Changing source faces or available count branches may invalidate the fixed-envelope assumption.
