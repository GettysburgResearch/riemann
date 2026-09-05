# Validation and publication boundary

## Actually executed

* `python verify.py --check result.json`: 275 exact finite controls passed.
* `python -O verify.py --check result.json`: the same 275 controls passed;
  the complete output bytes agree with normal mode.
* `python test_verify.py` and `python -O test_verify.py`: seven deliberate
  corruption cases were rejected in each mode, with the intended error:
  changed dimension, float alias, Boolean/integer alias, changed source
  enclosure, changed proof bytes, changed parent lock and a duplicate key.
* The three supplied parent proof files have their Git blob hashes recomputed
  and matched to the frozen identities in SOURCES.md.

`REPLAY.json` records commands and output hashes. It is an execution receipt,
not an analytic certificate. Repeated runs are not additional distinct tests.

## Finite mathematical coverage

The checker reconstructs Q_3 from positive rational log-series tails and
integer-square-root bounds; verifies Q_3<9/8 and Q_2<1/2; reconstructs the
m=152 gamma sum and unit-window dimension bound; checks the exact rational
multiplier division, finite gamma identities and explicit threshold formulas;
and verifies primitive endpoint and exponential moment cancellations.

For the illustrative three-frequency primitive family at L=pi/10, the
finite checks retain exact rational frequency coefficients, both endpoint
cancellations, the cosh-tail moment, and the sufficient energy margin. They
are not numerical evaluations of the infinite prime quadratic form.

The artifact checker does not authenticate mathematics merely because a
stored PASS flag is present: it recomputes the finite controls. Conversely,
matching proof-file hashes only binds the exact text that was tested; it is
not a correctness proof for that text.

## Not performed

No infinite prime-form evaluation, high-order actual Gram matrix, new zero
census, PNT computation, directed integration, previous packet suite, Lean
build, remote CI run or independent mathematical review was executed.
The Fourier identity, function-space arguments and spectral-index theorem
are written analytic proofs awaiting review, not machine-proved by the tests.

## Prior-art and remaining sign

Finite-codimension Weil positivity is classical. The proof is a source-matched
quantitative version for this repository's compact resolvent. It does not
bound the exceptional low-frequency sector or its coupling, and does not
prove any RH-equivalent all-order positivity assertion.

## Publication

This packet was NOT pushed. GitHub read tools confirmed PR #792 at
`2c3184545bafb4f5d873d2fa0ffc2c335a25d048`. Searches for available GitHub write,
create-tree and push actions returned none. Plugin discovery identified the
already-connected GitHub integration, not an alternative write tool. A local
`git ls-remote` attempt failed because the runtime could not resolve github.com.

An additive patch and a ZIP are supplied. They do not alter or remove any
predecessor file. A clean application and replay are recorded outside this
receipt in the final delivery; no remote commit identity is invented.
