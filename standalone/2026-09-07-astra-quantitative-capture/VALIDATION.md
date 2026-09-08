# HC26 validation scope

This file records bounded author execution, not independent mathematical
acceptance or machine verification of HC1/HC2. RH and the requested (10)
remain unproved.

## Commands

Run in the packet directory:

```
python -I -B check.py
python -I -B -O check.py
python -I -B test_check.py
python -I -B -O test_check.py
```

The frozen verification contains 1,235 bounded controls:

- 6 exact exponent/Holder bookkeeping checks;
- 280 small-value constant and ceiling identities;
- 624 Fejer coefficient-factor inequalities, raised to integral powers;
- 16 finite degree-split inequalities;
- 40 rational single-Blaschke radial identities with a complete geometric tail;
- 10 finite Blaschke-product inequalities;
- 12 finite Schur-deficit controls;
- 211 synthetic projection controls across five targets and ranks 1 through 12;
- 36 growing-target synthetic controls at j=1,...,12.

The counts are not independent theorem proofs. The tests involving large rank
integers only check scalar budget formulas; they do not construct actual
arithmetic matrices at those ranks. Every numerical value in acceptance is
an integer or Fraction. No zeta/gamma evaluation, zero list, numerical contour
integral, floating-point tolerance or sampled infinite tail enters acceptance.

## Reconstruction and rejection

The synthetic Gram is built from literal polynomial columns for A=1-2w and
solved by rational elimination. The residual is separately reconstructed as
a polynomial and checked against the normal equations and exact continuant
formula. The growing-target controls demonstrate small REMOVABLE error with
large intrinsic error; they are not actual-zeta controls.

The CLI has a fixed nonempty nine-entry manifest and ten-file flat inventory.
It rejects missing/extra entries, package-path symlinks, duplicate JSON,
floating/nonfinite values, boolean aliases, and altered source metadata.
Semantic result mutations are rehashed before execution to reach the primitive
reconstruction comparison, rather than being rejected only by stale hashes.
No acceptance condition is written as an assert.

Four unit-test methods include thirteen distinct non-symlink CLI refusals and
two symlink CLI refusals per successful mode, plus a pristine copied CLI
control. Windows error 1314 produces an explicit skip for the symlink method,
not a claimed execution; no Windows run is claimed by the author here.

## Unperformed work and analytic boundary

No new actual-source energy certificate, rank campaign, optimized controller
at an unbounded horizon, or direct numerical value of the final analytic
rate constants was computed. The clipping, Hilbert/Sobolev, infinite inner
factor and classical zeta assertions are PAPER proofs requiring review.

The implementation's source lock validates declared identities, not a remote
checkout. No parent suite is rerun. No Lean, comparator, kernel, whole-repository
build, remote CI result or independent referee verdict is claimed.

The companion delivery receipt records the final executed modes, hashes,
clean-extraction replay, and temporary-Git patch application. A temporary
application is not a real full-checkout test. Publication status is recorded
outside the scientific packet and must never be inferred from a local tree ID.

## Interrupted invocation

The first aggregate command completed both reconstructions and the normal
unit suite, then reached the tool time limit during the optimized suite.
That incomplete optimized invocation is not counted as a PASS. A separate
optimized run completed all four methods and fifteen refusals. The final
sealed modes are recorded individually in the delivery receipt.
