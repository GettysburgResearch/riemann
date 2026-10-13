# Validation and review boundaries

Status: same-author reconstruction and exact finite diagnostics. Proposed
mathematics, not independent mathematical acceptance or a formal proof.

## Executed finite checks

    python -I -S -B verify.py > results.json
    python -I -S -B -O verify.py > replay.optimized.json
    cmp results.json replay.optimized.json

Both modes completed with byte-identical output. The final report records
183253 explicit predicates, including repeated local cases and setup guards.
These are not 183253 independent analytic cases.

- All seven good squarefree ideal columns in 32<Nn<=64 and all 54 nonzero
  Eisenstein rows Nu<=13 are included in all 2401 ordered quartets. This is
  a complete small hard-window source, not a selected five-prime semigroup.
- The active/neutral split is checked on 129654 tuple-row pairs, with 2401
  neutral-support norm budgets. Distinct equal-norm ideals are retained.
- 1728 direct sharp-row mask sums are compared with exact signed divisor
  dilation sums. The radial identity is true for these finite sharp tests;
  the band-limited annihilation theorem is NOT inferred from them.
- 12960 local power cases retain nonunit zeros when exponents become zero
  modulo six. Inert and split primes both occur.
- 21870 block-criterion cases include eleven valid gap premises. Additional
  exact checks cover dual norms, the annular norm witness, the s=2 finite
  convolution radii, tail separation and uniform-order logarithmic budgets.
- Six explicit counterexample controls cover deleted neutral zeros, false
  zero-to-one sixth powers, sharp-row substitution, squared norm dilation,
  omission of the active-conductor condition, and equal-norm divisor merging.
  These are algebraic counterexample checks, NOT six altered-package CLI runs.

The sharp test gives -6 at active conductor norm 49 and H=49. It confirms
why the exact smooth cancellation cannot be asserted for sharp tuple sums.
The large annular example certifies only primality, norms, unit type and gap
inequalities. No infinite Phi_s-weighted character sum was numerically evaluated.

## Development correction

The first diagnostic draft accidentally multiplied inherited root vectors
in the (1,zeta_6) basis rather than their actual (1,omega) basis. A direct
physical mask-sum comparison rejected it. The multiplication was corrected
to omega^2=-omega-1; all subsequent replays pass. The primitive helper and
the mathematical dilation identity were not modified to fit the output.
The uniform-order cutoff was then sharpened from a crude X^(4k) aggregate
factor to X^(3k), using the actual neutral-support bound NR<=X^k. Its complete
log-budget and support checks are in the final replay.

## Analytic review scope

The author rederived the active-character factorization, both endpoint
bounds, the signed divisor formula, the complete-tuple error, the positive
infinite-convolution construction, and the explicit B_s and order-uniform
cutoff. The proof separates fixed-order power tails from the uniform-order
stretched-exponential tail. The illustrative annular family is unit-trivial
but nonprincipal; it is not vacuously removed by unit averaging.

This is a same-author check. No independent agent or human reviewer, theorem
prover, external theorem reconstruction or complete repository validator was
used. Agreement of finite scripts and hashes does not certify PROOF.md.
The unproved one-sided window estimate remains explicit.

## Source and transport

native_helper.py is byte-identical to #942's census.py, Git blob
2a074ccede483324392a729056ccbf43a1f26eac. The new checker verifies its SHA256
before importing its primitive functions. Optional NumPy census functions in
that helper are not called. No old large census or earlier analytic campaign
was rerun. The new standalone package uses Python's standard library only.

The manifest binds every payload file other than itself. Normal/optimized
replays, syntax parsing, an add-only Git fixture and fresh ZIP extraction are
checked before delivery. Publication must use the exact #943 parent
24cb2cdd6e768c2c35ef87227ed8319cfc2d14ed and only the new standalone directory.
A separate delivery receipt records the actual commit/PR after read-back;
this document does not claim a commit that has not yet been created.
