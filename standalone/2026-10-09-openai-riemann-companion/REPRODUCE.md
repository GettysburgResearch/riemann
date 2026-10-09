# Reproduce the source bundle and finite arithmetic

Run these commands from this companion packet directory. Python checks use the
standard library. The original core packet must be present as its sibling.

## Verify the resident bytes

```sh
python checks/source_bundle.py verify
python checks/check_native_mobius_bridge.py
python checks/check_source_bundle.py
```

Without `--source`, the first command checks resident source hashes, modes,
manifest totals, canonical storage, required entries, internal import closure,
the recorded dependency audit, and the unchanged original core. It cannot
detect an omitted, unreferenced file from a selected upstream directory; full
directory completeness requires comparison against the pinned Git tree.

For the complete selected-set comparison, use an independently fetched copy of
the public upstream repository containing both pinned commits:

```sh
git clone --filter=blob:none --no-checkout https://github.com/openai/math.git /tmp/openai-math-reference
python checks/source_bundle.py verify --source /tmp/openai-math-reference
```

Git may retrieve missing blobs from a partial clone. The checker reads the
hardcoded commit object, not whichever branch happens to be checked out. It
reconstructs the complete selected manuscript directories and internal Lean
import closure, compares every path/blob/mode, and recomputes the dependency
audit. Any checkout file used for source bytes must match its frozen Git blob.

## Recreate an absent supplement

On a checkout that already contains the inherited core but lacks this packet's
`upstream/` source copies, run:

```sh
python checks/source_bundle.py import --source /tmp/openai-math-reference
```

Import preflights the sources and destinations. It refuses to overwrite a
supplement file with different bytes. It never edits the inherited core.

## Assemble a fresh selected upstream view

Use an absent or empty directory outside the tracked source:

```sh
python checks/source_bundle.py assemble --source /tmp/openai-math-reference --output /tmp/openai-riemann-selected
python checks/check_assembled_view.py /tmp/openai-riemann-selected
```

The view contains exactly the manifest entries, taking each from either the
unchanged core or this supplement. It does not copy an entire old source tree
and hope that an overlay removes stale files. Original relative paths,
copyright notices, licenses, and file modes are preserved.

The assembled `lean/` has the pinned Lake configuration, manifest, toolchain,
compatibility patches, selected comparison statements and implementation
closure. External packages are pinned dependencies, not vendored or independently
verified by this import. The entire OpenAI umbrella library is not selected.

## Run a targeted formal comparison separately

Follow the resident upstream `lean/ComparatorChallenges/README.md`. Install the
upstream-required `comparator`, `landrun`, and `lean4export`, with the pinned Lean
toolchain available. Then work **only in the fresh assembled directory**:

```sh
cd /tmp/openai-riemann-selected/lean
lake update
lake exe cache get
lake env comparator ComparatorChallenges/QuasiRiemannHypothesis.json
lake env comparator ComparatorChallenges/DirichletSevenEighths.json
lake env comparator ComparatorChallenges/HeckeSevenEighths.json
lake env comparator ComparatorChallenges/SiegelZeros.json
lake env comparator ComparatorChallenges/OrdinaryElliott.json
lake env comparator ComparatorChallenges/OrdinaryTwoPointCorrelations.json
lake env comparator ComparatorChallenges/JointDickman.json
lake env comparator ComparatorChallenges/Jacobsthal.json
lake env comparator ComparatorChallenges/JacobsthalImproved.json
lake env comparator ComparatorChallenges/PattersonFirstMoment.json
lake env comparator ComparatorChallenges/PrimeGaps.json
lake env comparator ComparatorChallenges/SquareDifference.json
```

The Lake update hooks clone and patch external packages and may change workspace
state. Do not run them in the immutable source mirrors. Do not use an untargeted
`lake build` for the whole OpenAI library: unrelated modules are deliberately
absent. The exact solution-module and theorem mappings are in
[FORMALIZATION.md](FORMALIZATION.md) and the generated dependency audit.

These are reproduction instructions, not claims that those commands were run
in this contribution. The selected upstream configurations have
`enable_nanoda: false`; no additional independent checker execution is implied.

## Arithmetic checks and their scope

`check_native_mobius_bridge.py` constructs ordinary integer Möbius values and
ideal norm coefficients independently. It compares exact convolution, endpoint,
Gram, completion and block-mean identities using integers and `Fraction`.
The default finite ranges and explicit rejected shortcuts appear in its JSON
output. These checks do not prove asymptotic cancellation, authenticate an
upstream analytic theorem, or establish RH.

`check_source_bundle.py` exercises 21 isolated source-integrity and assembly
cases. Its small temporary fixtures mock the inherited core verifier only to
isolate the new checker logic. The separate real-bundle verification runs the
original verifier on all 3,286 historical core files; it does not use that mock.
