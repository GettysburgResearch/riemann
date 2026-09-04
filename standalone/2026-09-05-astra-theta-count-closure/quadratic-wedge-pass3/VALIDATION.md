# Execution and review boundary

Status: exact local execution completed; independent mathematical review pending.

## Executed in this continuation

- `python verify.py --check checks.json`: 657 exact controls passed.
- `python -O verify.py --check checks.json`: the same 657 controls passed.
- The complete normal and optimized output files are byte-identical.
- Two full-result corruption tests, normal and optimized, were refused.
- Two published-parent corruption tests, normal and optimized, were refused
  specifically for a Git blob mismatch.
- The original `verify_exact.py --check exact_result.json` suite was rerun:
  225 controls in each mode and complete output byte equality.
- The local checksum manifest is checked after all packet files are frozen.

The new checker uses only the Python standard library, Fraction, and a small
Gaussian-rational implementation. It checks the combined phase numerator,
saddle cancellation, envelope derivative, critical-strip polynomial algebra,
case thresholds, exact rational error budgets, finite mixed-difference and
row-mass identities, and the retained counterexample. No floating-point
rounding assumption enters these checks. Bounded parameter fixtures are
corroboration of the displayed algebra, not coverage of the theorem's
infinite quantifiers. Explicit exceptions, not assert statements, enforce
failure under optimized Python.

The original low-zero interval certificate and its mpmath interval-Gamma
trust boundary remain inherited. That interval calculation was NOT rerun
in this continuation. The quadratic proof does not require the selected
14--15 zero or the all-time heat lower bound; it uses V100, the parent's
Jensen count, and the exact mixed zero identity. Previous layers retain
all of their original dependencies and execution records.

## What is not certified by the checker

The code does not prove Rosser's theorem, the classical completion remainder,
the normal convergence of the xi product, the infinite count estimates,
Gaussian/integral tail passages, or the complete analytic proof in PROOF.md.
It does not inspect actual zeros at the large saddle heights. It proves
neither the unrestricted mixed inequality nor RH.

No remote CI or Lean execution was requested. No independent mathematical
or code-review verdict has been received. External novelty is unassessed.

## Source review

The published Rosser constants were read from Table 1 on PDF page 1 of
arXiv:1208.5846v2. Equation (2.5) on PDF page 3 supplies the completion
remainder. Both pages were rendered successfully and visually inspected.
The original 1941 Rosser proof is not reproduced in this packet. No PDF
byte hash or first-hand review of that original proof is claimed.

The two load-bearing original repository files are authenticated by their
published Git blob identities inside verify.py. The pass2 head was read
remotely before authoring this extension; its files are left untouched.
The exact new remote head and its file readback receipt are to be recorded
in the PR discussion after publication, not guessed in advance here.

## Independent review priorities

1. Check the full combined phase (3.3) before its bound, including the use
   of a continuous argument rather than a principal-argument shortcut.
2. Check both local zero-count estimates with endpoint multiplicity.
3. Check the positive block near sqrt(r), including its log r mass.
4. Check the negative middle localization and its unit-interval cover.
   Only the numerical Gaussian majorant is extended past the middle range.
5. Check low-tail monotonicity and the high power p=n/3, with the latter
   used only for n>12500.
6. Check the two-case split and the strict integer bounds in (7.2)--(7.3).
7. Check that no changing scale or finite verification is used to claim
   the unrestricted mixed inequality. The remaining index region is infinite.
