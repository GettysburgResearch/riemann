# Review checklist after the hostile pass

Attach reviewer, date, exact source version, and evidence path to every checked
item.

> [!IMPORTANT]
> `arXiv:2609.04176v1` must not be promoted. Section J records a completed
> blocking countercheck: the proof's max-summand majorant retains a positive
> `B^2 log B/800` term.

## 0. Blocking verdict

- [x] The max-summand majorant used in Proposition 9.5 was written explicitly.
- [x] The compulsory subset `I_0={0,...,S-1}` was isolated.
- [x] Its Pascal minor was proved to be a nonzero integer for every selected `A`.
- [x] The odd `a_Q` terms were cancelled exactly against `F_B/prod Pi_i`.
- [x] The selected clearing factors were shown to contribute
      `2rho B^2 log B+O(B^2)`.
- [x] The source's own local singular coefficient
      `A_rho=2rho-rho^2/2` was inserted.
- [x] The Cauchy determinant was shown to contribute only `O(B^2)`.
- [x] The tail product was shown to contribute only `O(B log B)`.
- [x] The uncancelled term `(rho^2/2)B^2 log B` was derived.
- [x] At `rho=1/20`, the surviving coefficient was identified as `1/800`.
- [x] The conclusion that the posted proof of Proposition 9.5 is invalid was
      separated from any claim that Catalan's constant is rational.
- [ ] A later source supplies a new signed Cauchy--Binet cancellation theorem,
      stronger common divisor, redesigned completion, or different scalar.

Evidence:

```text
DEEP_HOSTILE_REVIEW.md
HEIGHT_BOUND_COUNTERCHECK.md
diagnostics/catalan_height_hostile_replay.py
diagnostics/height_hostile_replay.json
```

## A. Provenance

- [ ] Attached PDF SHA256 independently equals the source lock.
- [ ] PDF has 20 pages and expected metadata.
- [ ] All pages were rendered and visually inspected independently.
- [ ] Current arXiv version is checked for revisions or errata.
- [ ] A companion source/code repository is searched for again.
- [ ] Any later source is pinned by immutable commit and license.
- [ ] Any v2 receives a new review rather than silently inheriting v1 fixes.

## B. Definitions and dimensions

- [x] `T_m`, `u_m`, and the positive-index recurrence were reconstructed.
- [ ] `T_0=G` is stated where the proof extends to `i=0`.
- [ ] The `T_i`/`T_{i+1}` residual formula and global column sign are corrected.
- [x] `Pi_i` uses the correct `B` consecutive odd factors.
- [x] The residual row and column ranges were reconstructed.
- [ ] Section 3 explicitly defines `D=2B`.
- [x] With that repair, `D+S+3=N`.
- [x] `F_B=product_{r=0}^{2B-1} r!`.
- [x] The three auxiliary columns correspond to the omitted rows.

## C. Full-rank argument

- [x] Polynomial defect degree is at most `2B-3`.
- [x] The finite differences annihilate the required polynomial range.
- [x] `lambda -> P_lambda^*` is injective.
- [x] `D_lambda` is nonzero and has degree at most `2B-1`.
- [ ] The zero sets of `K` and `G_0` are audited with multiplicities line by line.
- [ ] The rational-difference no-solution proof explicitly handles the
      polynomial/no-pole case.
- [ ] Every pole-shift argument is formalized.

## D. Determinant factorization

- [x] Newton transform determinant is `+-1`.
- [x] Reference pivots are the stated factorials after `D=2B`.
- [x] Auxiliary columns become the three exact unit vectors.
- [ ] Cauchy--Binet index and sign conventions are corrected consistently.
- [ ] Lemma 4.1 uses the polynomial product where the factorial quotient is
      outside its literal domain.
- [x] `Psi_A(I)` is an integer when defined by alternant division.
- [ ] Uniform degree and coefficient-height bounds for `Psi_A(I)` are proved.
- [x] Cauchy determinant contributes the second `V(I)`.
- [x] The compulsory `I_0` Pascal minor is nonzero.
- [ ] All powers of two are tracked in a replacement proof.

## E. Local valuation layer

- [ ] Formula (5.7) is checked term by term after the tail-index repair.
- [x] Tail denominator bound (5.11) is structurally correct.
- [x] Taking the minimum after the p-adic triangle inequality is legal.
- [ ] Zero Cauchy--Binet summands are treated as valuation `+infinity`.
- [x] The sum over prime-power layers has finite `O(B)` support.
- [ ] Theorem 5.1 states `S<=B/20`.
- [x] Balanced occupancy minimizes the collision number.
- [ ] Inequality (5.21) is proved for all intended `B,S,Q`.
- [x] The prime-2 denominator argument is separate from odd primes.
- [x] The prime-2 argument was not misread as deleting the real
      `v_2(F_B)log 2` contribution.

## F. Stability

- [x] Actual and ideal upper row indices were compared.
- [ ] Every surplus-row exchange is explicit.
- [ ] Local base-cost change is bounded uniformly.
- [ ] Double-Vandermonde occupancy change is bounded uniformly.
- [x] The literal `5B` cutoff was disproved by `B=100,S=5,Q=503`.
- [ ] A correct support cutoff is proved in the source.
- [ ] Weighted sum of changes is `o(B^2)`.
- [ ] Real-place and `Psi_A` stability are included.
- [x] It was verified that even granting all these items does not remove the
      `B^2 log B` obstruction.

## G. Small-prime certificate

- [x] Independent floating reconstruction found 238 raw cells.
- [ ] Merge to 178 cells is published and checked.
- [ ] `K_v(n+v)` recurrence is proved, not only sampled.
- [ ] Every `Q_0(v)` piece is the claimed rational quadratic.
- [ ] Antiderivative (6.26) differentiates correctly on every cell.
- [ ] Argument shifts by 64 are exact.
- [ ] Bernoulli remainder bounds and signs are checked.
- [ ] Logarithm and `log(2pi)` enclosures are directed.
- [ ] Final interval for `I_odd` is reproduced from clean bytes.
- [x] It was recorded that this certificate affects only the finite `B^2`
      coefficient, not the fatal leading logarithmic term.

## H. Middle-prime certificate

- [ ] Six affine boundaries are complete.
- [ ] Floor-change values are complete.
- [ ] All ordering-crossing events are included.
- [ ] Lowest-`rho` marginal selection is correct on every cell.
- [ ] There are exactly 235 published affine cells.
- [ ] Exact integration recovers the displayed rational from those cells.
- [x] The displayed rational was numerically corroborated.
- [x] It was recorded that this term is only `O(B^2)`.

## I. Large-prime range

- [ ] Seven pieces in (8.1) are derived from exact local minima.
- [ ] Their endpoint conventions do not lose mass.
- [x] Integral (8.2) was checked from the displayed pieces.
- [ ] Raw baseline (8.3) is derived.
- [ ] Higher powers contribute `o(B^2)` with explicit support.
- [x] It was recorded that these corrections cannot cancel a positive
      `B^2 log B` term.

## J. Proposition 9.5

- [x] The exact max-summand majorant was reconstructed.
- [x] The claimed complete `B^2 log B` cancellation was disproved for that
      majorant.
- [x] The source's `2rho-rho^2/2` local coefficient was compared with the
      compulsory `2rho` clearing-factor coefficient.
- [x] The surviving coefficient `rho^2/2` was proved.
- [x] The distinction between the signed determinant and its absolute
      max-summand bound was made explicit.
- [ ] A new proof controls signed cancellation across `sum_I Xi_I`.
- [ ] Or a new proof supplies common divisibility with coefficient at least
      `2rho`.
- [ ] Or the scalar/weights/completion are redesigned.
- [ ] A corrected master ledger has no positive leading term.

## K. Final theorem

- [x] The finite decimal subtraction was checked conditionally.
- [x] `H_B^min` is defined from the same scalar.
- [x] The final integer contradiction would be immediate from a valid negative
      height estimate.
- [x] The posted negative height estimate was shown not to follow.
- [ ] A corrected proof supplies an eventually negative bound.
- [ ] Independent specialist review confirms the corrected argument.

## L. Riemann boundary

- [x] No RH implication is claimed.
- [x] PNT is not described as RH-strength.
- [x] Special-value irrationality is separated from zero distribution.
- [x] Numerical diagnostics are not described as certificates.
- [x] No source theorem is entered in `canonical/` or `research/integrated/`.
- [x] The min-local/max-real mismatch is registered as a reusable proof
      firewall for determinant, Gram, Schur, and divisor-wavelet programs.
