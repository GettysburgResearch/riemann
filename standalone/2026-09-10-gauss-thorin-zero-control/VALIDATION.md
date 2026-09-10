# Validation and limitations — GZC26

Status: author-executed finite directed certificates; independent analytic/code review remains outstanding. No RH proof, global zero census, complementary-region assertion, or formal verification is claimed.

## Executed acceptance path

On Linux with standard-library Python, the full checker was run in normal and optimized isolated modes:

```sh
python -I -S -B check.py --check results.json --self-test
python -I -S -B -O check.py --check results.json --self-test
python -I -S -B tests.py
python -I -S -B -O tests.py
```

Each full mode authenticates the nine-file inventory/eight manifest entries and reconstructs the same complete canonical JSON. Each checks the three strict whole-disk predicates, then accepts the pristine receipt and refuses eight modified receipts through the same acceptance function: false RH status, wrong zero count, zeroed source error, a Boolean count alias, changed centre, wrong source polynomial, removed scope, and duplicate JSON key. These are eight changed-file function calls, not eight full CLI reruns. Resealing a bad receipt cannot make it equal to the source reconstruction.

Seven separate test methods pass per mode. They check rational interval arithmetic; elementary-function identities; gamma's exact normalization and complex recurrence; 21 source moments through a separate Bernoulli formula; the two shape enclosures; an intentionally false primitive root bracket; and a modulus lower bound. They test code consistency, not the correctness of every infinite analytic lemma. Both implementations and tests have the same author.

The receipt's SHA256 is

`21b54911adce8ba24ba8e019014f695abebfb9071edb7223e5a253f5ebdb0cab`.

## Complete finite coverage

The source recurrence regenerates the m=3 and m=10 monic polynomials, the exact error constants, 13 isolated positive nodes and their weights. There are 26 quadrature moment-containment checks. Each of the three complex centre evaluations uses all 2241 logarithmic-grid nodes, with full alias and two discrete-tail bounds and a separate Cauchy derivative bound. The m=10 native-source error uses both real anchors, all 1280 positive real cells and both infinite integral tails. All three curvature costs cover their entire disks.

No zeta value, zero table, floating special function, numerical contour mesh, or downloaded package enters acceptance. The external source identity and analytic error theorems are explicit paper-level dependencies. A positive arithmetic margin cannot authenticate a false analytic adapter.

## Development diagnostics retained in this account

Ordinary mpmath/scipy exploration was used to choose rational disk centres and candidate source brackets. It is not part of the certificate. A raw root search initially mistook exponentially small values at high height for roots; scaling the objective exposed the false success, and no such root is used. Higher-height low-precision scouting was unreliable and is not presented as a zero census. The low m=3 candidates were recomputed at higher ordinary precision before the completely separate directed check.

An attempted optional python-flint installation failed because network/package access was unavailable. Acceptance instead uses the supplied standard-library interval implementation. The first isolated run failed to import the sibling interval module; explicit local-path insertion repaired it. During proof review the gamma remainder was conservatively widened by a factor two and a sector guard was added before the final receipt. The initial narrower-remainder receipt is not the published certificate. Bytecode-cache files generated during development are excluded; the accepting packet has an exact inventory and uses `-B`.

The producer-emitted preliminary receipt was extended with deterministic source polynomial/constant fields and explicit simplicity flags; the final full normal and optimized reconstructions reproduce those fields from the primitive definitions, not from the preliminary receipt.

A documentation-only repair subsequently restored six LaTeX row breaks in equation (4). No mathematical statement, executable or result byte changed. The manifest was regenerated and authenticated; the clean-archive replay below uses these final files.

## Release scope

The contribution is addition-only in a new standalone directory on the existing author research branch. Previous GTP26 files, main, other contributors' branches, canonical acceptance, formal sources and workflows are not altered. The publication response records the exact commit and remote byte verification separately, avoiding self-referential commit hashes in this manifest.

No repository-wide checkout/build, Lean run, parent full checker replay, Windows execution, remote CI, external-source proof audit, or independent referee acceptance was performed. A correct count in three small disks is not an all-height theorem. The reflected all-order zero-confinement target remains open.
