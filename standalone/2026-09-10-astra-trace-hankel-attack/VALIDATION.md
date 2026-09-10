# Executed evidence and limits

This packet contains proposed proofs, not a formal proof of RH or a referee
acceptance. The exact finite computations support the specific arithmetic
bounds and counterexamples below. The infinite statements require their
written arguments and named imports.

## Complete accepting reconstructions

Both commands completed and produced byte-identical full JSON, also identical
to the retained result.json:

```sh
python3 -I -S -B check.py --expect result.json
python3 -I -S -B -O check.py --expect result.json
```

No repository author module, zeta/gamma oracle, floating quadrature, or actual
zero evaluation enters this reconstruction. The checker uses integers and
Fraction arithmetic. Its atanh logarithms retain full positive remainders;
its Machin arctangent bounds retain the alternating remainder. Displayed
rational decimal enclosures round outward by integer division.

The exact executed mathematical objects are: all 25 interpolation products
and their whole-tail error sum; the separate nine- and ten-node bounds; finite
controls of the written all-shift monotonicity; the Jensen/tail/heat constant
budgets; the positive theta-shift perturbation's complete extra inverse-square
budget; 33 compact-density moments reconstructed in two ways; 16 trace values
reconstructed by cumulants and by log-derivative recursion; the exact negative
H4 determinant; the inverse-factorial determinant; a separate small-shift
25-node countermodel; and 36 Gaussian-rational interpolation domination panels.
These are not counts of analytic theorems or computed actual xi moments.

## Actual rejecting command-line tests

Both test commands completed without skips:

```sh
python3 -I -S -B test_check.py
python3 -I -S -B -O test_check.py
```

Each mode ran 16 methods: one pristine full accepting CLI replay, eleven
actual CLI refusal cases, and four arithmetic/API controls. The stable JSON
summaries are byte-identical and retained in tests.json. Unittest's timing
text is not claimed byte-identical.

The eleven refusal cases are duplicate JSON keys, a float alias, a Boolean
alias, false RH promotion, omission of the complete-tail field, a zero-tail
claim, reversal of the negative determinant, a changed imported ordinate,
a changed imported height, a symbolic-link input and an empty receipt. The
four other controls reject overlapping interpolation intervals and shift zero,
verify failure of inverse-factorial PSD preservation, and distinguish an
incorrect cumulant sign. Passed source-hash refusal tests do not independently
prove the external zero data.

The test runner records counts only after the corresponding CLI assertions
complete. It does not claim eleven executed refusals if setup aborts.

## Source and arithmetic boundaries

INPUTS.json is authenticated by an embedded SHA256 before use. Expected JSON
is decoded with duplicate-key, floating/nonfinite-number and exact-type
controls, then compared against a complete fresh reconstruction. The numerical
source intervals are deliberately coarse hundredth-wide enclosures of the
reported LMFDB values. Their primitive zero-existence/containment statements
and the Platt--Trudgian finite-height theorem are imported, not generated here.

SHA256SUMS authenticates this delivered file set. Hashes do not establish a
mathematical theorem, nor provide a signature from an independent referee.
The executable does not authenticate its own implementation independently;
its identity is recorded in EXECUTION.json and the delivery manifest for review.
No original author package has been silently approved or executed.

## Unsuccessful intermediate invocation, then clean final runs

An intermediate orchestration omitted the required filename after --emit;
its shell redirection emptied the local expected receipt. That invocation and
the resulting setup failures are not counted as successful checks. The receipt
was regenerated with the correct CLI, and then both complete accepting modes
and both complete adverse suites passed as recorded above. No mathematical
bound was changed in response to this delivery-command error.

## Delivery and repository state

The accompanying external delivery receipt records clean ZIP extraction and
an add-only patch roundtrip in temporary Git repositories. Those fixtures
preserve an unrelated sentinel and replay the complete checker and test suite
in both modes. They are transport checks, not a full Riemann checkout or a
validation of main. A local recursive Git subtree hash identifies the packet;
it is not a remote research commit.

GitHub reads were successful. Current main was observed at
f99d9e3908dde4865377c75d9ca051c1f545bf4f; the integration candidate was observed
at a20e80654d33afc128261895291ccc37bb328402. PR #834 advanced from the inspected
determinant checkpoint to 62bd9bbed134e20c1ee9cd92d008562079af9ceb: one commit,
seven additions, no changes to the original determinant packet. Its added
crowding paper was read separately as context and is not used by our theorems.
These reads are not an exhaustive activity census or an atomic repository lock.

No write actions were available from the GitHub connector; direct git ls-remote
failed DNS. Therefore this research packet is **not pushed**, and main, the
integration branch, review branches, source branches, settings and workflows
were not changed. No full-checkout validator, Lean build, native Windows run,
external zero census, parent numerical suite or remote CI execution is claimed.
No source-specific inequality establishing unweighted all-rank positivity or
RH was obtained.
