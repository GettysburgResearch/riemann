# A connected 73-spin ten-moment theta realization

**Proposed component proofs and a directed finite existence certificate.
Independent mathematical/code review required. This is NOT an RH proof.**

This is a positive nonuniform-pair continuation of PR #842. One 8-spin core,
one 64-spin halo and one hub form a connected zero-field pair ferromagnet with
2564 positive edges and positive observable weights. There is no independent
bath, unobserved-spin selection, or many-spin interaction.

The complete certificate proves a unique parameter vector in a prescribed
rational box matching the actual standardized theta moments through degree
TEN. The same graph realizes a whole 10^-22 box of nearby standardized moment
vectors. Source moments are recomputed from the literal infinite theta density,
with all omitted indices and physical tails included. The 1170 exact weighted
block states account for all 2^73 configurations.

For EVERY fixed r>=6, the paper also constructs connected (73+r)-spin local
extensions retaining the first ten theta moments EXACTLY, with independently
adjustable higher moment coordinates through degree 2r in a nonempty open
neighborhood. That neighborhood is around the new model's moments, not proved
to contain theta's higher moments. No uniform radius, successful global
continuation, or all-order source realization is asserted.

Read [PROOF.md](PROOF.md), then [REVIEW.md](REVIEW.md) and
[VALIDATION.md](VALIDATION.md). Local NMT labels are not canonical acceptances.

## Reproduce

```
python -I -S -B certify.py --check certificate.json
python -I -S -B -O certify.py --check certificate.json
python -I -S -B test_certify.py --adverse
python -I -S -B -O test_certify.py --adverse
```

Every accepting call recomputes the entire theta moment enclosure, graph law,
parameter-box Jacobian, and contraction inequalities. No NumPy/SciPy/mpmath,
zero table, special-function oracle or floating-point solve enters acceptance.
The ordinary numerical scout only proposed the EXACT rational centers and
preconditioner in parameters.json. `--emit` is producer-only and does not
authenticate a delivery.

## Scope

The earlier 4104-spin seed matched six moments; this separate 73-spin graph
matches ten. This is not a minimum-spin theorem or a claim of closeness to RH.
All finite pair graphs have a classical Lee--Yang theorem, but a fixed finite
moment match does not identify the whole theta law. The next source-specific
task is certified continuation to the higher theta targets without leaving the
positive-coupling/positive-weight domain. The paper proves no such all-order
continuation and asks no reviewer to supply it as a routine final lemma.

Earlier source files, main, canonical/formal records and workflows are unchanged.
