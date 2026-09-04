# Validation record: mixed-difference pass 2

Status: local execution completed; independent mathematical/code review
pending. No remote CI, Lean build, or all-height zero census is claimed.

## New exact checker

Executed from the committed-source candidate directory:

    python verify.py > checks.json
    python -O verify.py > optimized.json
    python verify.py --check checks.json
    python -O verify.py --check checks.json

All four result objects are byte-identical. Each executes 875 exact checks.
The total is a count of finite checks, not the number of mathematical theorems.

The standard-library-only checker uses Fraction and rational complex pairs.
It contains no floating-point arithmetic or optimization-removable asserts.
It recomputes:

- heat constants and integer incomplete-gamma bounds;
- cone, column, and cubic-wedge rational comparisons;
- exact strip/modulus fixtures;
- model power sums by a recurrence versus rational complex atoms;
- mixed differences and complete binomial rows;
- row conservation and total variation versus negative mass;
- row polynomials in three independent finite expansions;
- a rational-unit-circle N=100 witness to exponential amplification;
- the integrated one-atom Laguerre identity;
- the prime-kernel Laurent recurrence versus independent Taylor expansion.

Two retained-output corruptions were each tested in normal and optimized
Python: changing rh_proved to true, and changing H_(0,14) to zero. All four
were rejected by recomputation. No self-reported flag is used to prove RH.

## Parent replays in this pass

The existing parent verify_exact.py was rerun in both modes with its
--check exact_result.json comparison: 225 checks per mode, identical output.
The existing verify_low_zero.py was rerun in both modes; the outputs are
byte-identical and their COMPLETE JSON equals low_zero_result.json.
This is only the two-ordinate sign certificate, not a new zero census.
Its mpmath 1.3.0 interval Gamma trust dependency is unchanged.

All eleven entries in the parent's SHA256SUMS passed. All twelve original
files have their Git blob identities preserved. No prior proof, verifier,
result object, or source lock was edited.

## Analytic scope

The infinite tail bounds, all-time derivatives, unbounded index regions,
noncancelling meromorphic poles, and spectral-radius identity are proved in
PROOF.md. They are NOT machine-certified by the finite checker.

V100 remains an imported restriction of Platt--Trudgian's published zero
verification. The only additional theorem import is the explicit weakened
Trudgian zero-count bound, used only for the high-zero reservoir in the
opposite-direction column/wedge result. The two relevant PDF pages were
read and visually checked; no complete-paper independent proof review,
PDF byte hash, or new formalization is claimed.

External novelty has not been established. Review priority is mathematical
quantifiers, sign orientation, the selected-zero/tail split, the high-zero
phase region, and exact meromorphic noncancellation before provenance.

## Reproduction and publication

Run the commands above and `sha256sum -c SHA256SUMS` in this directory.
The ledger covers the seven other files in this add-only subpacket. The
parent directory's ledger still covers its original files unchanged.
Publication commit/tree and remote readback belong to the PR comment and
local publication receipt, not to a recursively self-hashed source file.
