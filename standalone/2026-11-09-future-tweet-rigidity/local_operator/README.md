# Local arithmetic operators: a stable two-channel adapter

**Main result:** the two distinct-character Kummer transforms in
[TWO_CHANNEL_LOCAL_ADAPTER.md](TWO_CHANNEL_LOCAL_ADAPTER.md) remove the
unit-constant component and retain every other local source with squared
gain at least `(1+1/q)/2`. A single channel has a `1/q` exceptional squared
gain. The explicit paired decoder has norm below `sqrt(2)`.

The main theorem tensorizes over a squarefree conductor, with all sectors
and masks retained:

| Local choices | Channels | Exactly reconstructed source |
|---|---:|---|
| Two distinct character transforms | `2^r` | Mean-zero in every local coordinate |
| Add the unit-constant projector | `3^r` | Entire unit-domain source |
| Omit only the all-constant output | `3^r-1` | Orthogonal complement of the globally constant vector |
| Also retain zero-coordinate projectors | `4^r` | Entire full-residue-domain source |

Here `r` is the number of distinct conductor primes. The inverse squared
loss is at most `2^r`, which is subpower in the conductor for a fixed
number field. These are algebraic reconstruction costs; no uniform
composite-modulus trace-function estimate is inferred from them.

An exact-order-six character and its conjugate are a convenient distinct
pair. For a quadratic native character, its conjugate is the same
character and does not repair the weak mode. A different nontrivial
auxiliary character does give the local algebraic repair, but its actual
new output also needs an analytic estimate.

The separate [SCALAR_FILTER_BUDGET.md](SCALAR_FILTER_BUDGET.md) proves a
finite local-valuation Euler-factor classification and the sharp scalar
price `coth((lambda-beta) log R / 2)` for a support-R probe that kills the
lambda mode and preserves the beta mode. It retains the full prime
divisibility defect of the Mobius sign-flip identity.

## Verification

From the packet root:

```sh
python -I -S -B local_operator/check_local_operator.py
```

[CHECKS.json](CHECKS.json) records 8,205 exact predicates. They include
direct finite-field Gram calculations over F_7 and F_13, local decoder
identities, distinct-character repair of the quadratic mode, full and
partial CRT source reconstruction at norm 91, and nonunit-sector
reconstruction. The CRT test uses a nonseparable complex source in the
72-dimensional unit space and obtains the sharp lower constant 4/13.
Explicit adverse cases retain the mixed constant/nonconstant sector,
single-channel weak mode, and the nonunit coordinate; the scalar checker
finds 145 failures of the maskless Mobius identity in its stated sample.

The checker imports only finite-field and exact cyclotomic arithmetic
classes from `../coupled/verify.py`. It independently reconstructs the
kernel and checks every local Gram entry at its two fields. Its report
binds both the checker and imported module by SHA-256. The sibling
checker separately covers further fields, including F_25 and F_49.

No finite test certifies a global analytic estimate. The proofs establish
the displayed finite-field/tensor statements in general; the local
source must still be matched to the native completed arithmetic weight,
and its actual outputs must be bounded.

## Source provenance and review scope

[SOURCES.json](SOURCES.json) pins the three relevant previous repository
files fetched during this lane. The existing #1002 scalar probes and
#1020 free-column coefficient mismatch are preserved. The local frame is
additional finite algebra, not a claim that those global gaps have closed.

Root and the coupled lane checked the local normalizations and sector
interpretation during development. A separate review records its own
scope and frozen hashes at the packet level; those internal checks are
not external peer review or formal verification.
