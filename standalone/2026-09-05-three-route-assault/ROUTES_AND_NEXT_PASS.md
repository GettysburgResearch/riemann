# End-to-end routes and the next proof tasks

Status: strategy updated by the complete arguments in this packet; final arithmetic gates remain open.

## Route 1 — preserve the scalar, not the wrong microscopic labels

Original target:

```text
literal theta source
  -> positive trace-class K
  -> det(I+uK)=F(u)/F(0)
  -> negative real invariant zeros
  -> RH.
```

What is now closed is the same determinant identity for an explicit **nonpositive** trace-class companion. It is defined from theta coefficients without using zeros. This proves that merely producing a nuclear spectral object is not the missing ingredient: that can be done for counterfeit entire functions as well.

The proposed marked lift is now ruled out for the actual source. The theta fibers share a latent scale, giving strictly positive occupation covariance; a positive determinantal process in those same modes has nonpositive covariance. The split-source vacuum/forced-bit picture gives a second independent two-mode obstruction. A nonatomic direct integral is not an ordinary trace-class repair.

**Next task R1-P:** construct a nonlocal scalar reorganization whose exterior traces match `a_n` while not asserting false marked-marginal preservation. A useful first step would be a source formula for the signed cycle quantities `s_k` in which the actual covariance/cumulant corrections are controlled, not dropped.

A positive metric for the particular companion is not automatically an equivalent target; bounded similarity and multiple zeros can add conditions beyond the scalar determinant problem.

## Route 2 — freeze one small frequency window

The corrected chain is

```text
literal 67-free Möbius coefficients
  -> fixed [1,2] frequency energy, maximal in the original prefix
  -> subpower energy
  -> half-weighted Möbius prefix bound
  -> M(x)=O_epsilon(x^(1/2+epsilon))
  -> RH.
```

The reduction to `[1,2]` is unconditional. It does not discard high frequencies by an absolute estimate; it uses an invertible Abel transport with explicit logarithmic loss. Arbitrary subpower-frequency ensembles have the same power exponent, so changing an ensemble or shrinking its width is not by itself progress in cancellation.

**Next task R2-P:** prove a genuinely arithmetic estimate for the signed off-diagonal in that fixed window, retaining the complete maximal-prefix quantifier. The intended exponent contraction must use information that fails for the positive coefficient control `b_n=n^(-1/2)`. Long-frequency mean values followed by the exact back-transfer do not pay the needed power.

This route is the cleanest diagnostic of any putative geometric gain: translate the gain back into the fixed Möbius energy and check whether its exponent actually improves.

## Route 3 — exploit the horizontal Schur surplus

The revised chain is

```text
one hypothetical off-line zero
  -> a nonzero conditioned horizontal Schur matrix H
  -> quantitative negative direction with gap 2 lambda(H)
  -> source-defined arithmetic estimate/tail error smaller than that gap
  -> contradiction
  -> RH.
```

The first two finite steps and the perturbation theorem are proved here. The exact pair-energy surplus controls both count defect and `8 Tr H+4 Tr(H^2)` in a single budget. That is additional retained information, not a new bound for the budget itself.

The easiest displacement-only lower bound is false. Even one fixed off-line pair can be screened arbitrarily strongly by a growing collection of real modes at fixed bandwidth. A positive density of real zeros does not determine the relevant lower frame bound.

**Next task R3-P:** derive a prime-side expression for `H` or for its Schur-complement quadratic form, with a quantified budget for localization, inversion of the positive Gram block, and omitted zeros. A useful theorem would bound those errors by a source norm that is strictly smaller than an explicitly proved arithmetic Schur gap.

Do not replace this with a bound for the raw odd exponential before projection. The explicit quartet in the screening note disproves that replacement.

## Why the three results do not already combine into RH

Route 1's scalar companion is not positive. Route 2's small frequency window still carries the full unresolved cancellation. Route 3's horizontal matrix is extracted from zero-side data, and no source-side bound has forced it to vanish. No map between these spaces with a favorable uniform norm has been constructed.

A new adapter would have to identify the actual source, preserve the relevant signed form, and control its condition number. Merely composing three existing positivity statements would miss these obligations.

## Ranking after this pass

1. **Route 3** now has the sharpest new constructive theorem to exploit: a complete matrix surplus plus an exact conditioning target.
2. **Route 1** retains the largest structural upside, but the microscopic marked route is closed negatively and the universal companion must not be mistaken for arithmetic positivity.
3. **Route 2** is cleaner and smaller than before but still lacks an estimate beyond the inherited arithmetic exponent.

For a later two-route pass, the natural provisional choice is Routes 3 and 1, keeping Route 2 as the fixed arithmetic comparison standard. This is a research judgment, not a probability of success or a claim that either final gate is small.
