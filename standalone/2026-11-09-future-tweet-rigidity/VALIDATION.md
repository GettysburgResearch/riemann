# Verification and review boundaries

9 November 2026. Proposed research package; not an integrated result.

## Claims and acceptance rules

| Component | What is established | What computation authenticates | What remains outside the check |
|---|---|---|---|
| Coupled local kernel | All-field finite-sum, axis, hypergeometric-normalization and Gram identities, with written proofs | Exact evaluations over six specified fields in both sextic orientations | External sheaf geometry, analytic FKMS theorem, native asymptotics |
| Paired local operator | Exact local decoder and CRT sector reconstruction; scalar amplitude bound | Exact small-field matrices, actual complex tensor source, masks and negative controls | Bounds for transformed native sources; a global theta identification |
| Weighted completion | Exact affine and Fourier identities; nuclear-norm sufficient criterion; chirp obstruction | Exact signed complex coefficients, axes, affine masks, Moyal and chirp support | Cheap separation of the actual Mobius/prime weight |
| Inverse/source capture | Covariance and orbit-closure identities, finite-window bound; exact finite packet ranks | Primitive Eisenstein enumeration and symbols, nonzero modular minors with replay | Fixed-source asymptotic capture; a growing natural frame; certified floating energies |

For each exact finite checker, acceptance requires that every integer or
rational cyclotomic equality succeed; failure raises an exception. The
computations do not use floating tolerances for those identities. Their
negative controls deliberately expose missing masks, the wrong character
orientation, erased axes, omitted sectors, and false one-channel claims.
Check counts below count finite predicates, not theorems or independent
pieces of evidence for RH.

The native rank calculation uses exact integer Eisenstein arithmetic and a
nonzero minor modulo 1009. Reduction of an integer cyclotomic minor to a
nonzero residue proves that minor is nonzero in characteristic zero. The
selected minors attain the packet column counts, so the rank conclusions are
exact. Source weights are mathematically nonzero on the open annuli; endpoint
floating underflow does not enter the exact rank certificates.

Gauss phases, projections, condition numbers, and covariance eigenvalues in
the native experiment are computed in ordinary double precision. They are
diagnostics, not interval or directed-rounding certificates. The complete
direct Gauss sums check the CRT phase convention at the sampled composite
moduli; this numerical comparison does not prove a general Gauss identity.

## Reproduction commands

Run these from this package's root. Python 3's standard library suffices for
the first three; the last additionally needs NumPy. There is no network use.

```sh
python -I -S -B coupled/verify.py --output coupled/CHECKS.json
python -I -S -B local_operator/check_local_operator.py --output local_operator/CHECKS.json
python -I -S -B transfer/check_weighted_adapter.py --output transfer/CHECKS.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B inverse/native_projection.py --output inverse/NATIVE_RESULTS.json
```

To preserve the published receipts when comparing another platform, point
`--output` to temporary paths. Each result binds its producer's SHA-256;
dependent local checkers also bind the shared cyclotomic module. On a
different numerical platform, compare native exact data literally and
floating diagnostics numerically, not by an entire-file hash.

## Executed checks

| Run | Finite coverage | Result |
|---|---|---|
| Coupled kernel | F7, F13, F19, F31, F25, F49; both sextic orientations | 9,816 exact predicates passed |
| Local operator and scalar budget | F7, F13; 72-dimensional CRT unit space at norm 91; nonunit sectors; scalar mask/filter controls | 8,205 exact predicates passed |
| Weighted bridge | Prime fields 7, 13, 19; both sextic orientations; signed complex coefficients; two chirps per field/orientation | 2,382 exact predicates passed |
| Native source | D:U = 256:128, 1024:512, 4096:2048; all good squarefree ideals in open annuli | Exact packet ranks 31, 115, 413; full frame ranks; Gauss phase replay and numerical diagnostics completed |

The total of the three exact local suites is **20,403** predicates. The
coupled and local suites were rerun by a separate assistant execution after
their producers finished. The checkers share the same explicit cyclotomic
arithmetic implementation; this is not an independently implemented
arithmetic library. The coupled suite also passed an optimized isolated run
with byte-identical output, as recorded in
[coupled/VALIDATION.md](coupled/VALIDATION.md).

The root reviewer reran the entire native source calculation from primitive
ideal enumeration with one BLAS thread. Comparison with the producer's
receipt found all **3,663 exact scalar leaves identical** and all **3,775
floating leaves** within relative tolerance 1e-10 / absolute tolerance 1e-12.
The largest absolute floating difference was
`1.616484723854228e-13`. This tolerance is a reproducibility criterion, not an
error bound for the reported energies. The root reviewer also executed the
final weighted suite and read its exact receipt.

## Review, authorship and frozen inputs

The package was developed by a coordinating assistant and three parallel
assistant executions. “Independent review” here means a separate execution
reviewing files it did not author. It does not mean external human peer
review or independent acceptance of a new analytic theorem.

- [REVIEW_INDEPENDENT.md](REVIEW_INDEPENDENT.md) reviews the coupled finite
  proofs and native affine match, local frame and tensor sectors, scalar
  budget, and weighted bridge. It explicitly excludes its reviewer's own
  inverse lane and the external analytic proofs.
- [coupled/SIBLING_REVIEW.md](coupled/SIBLING_REVIEW.md) independently reviews
  the local and weighted arguments and binds the files it read. It
  distinguishes read receipts from actual independent reruns.
- The root reviewer read the inverse note and code in full, rederived the
  split/inert norm-sign lemma, continuous-time prime-torus argument,
  finite-window dephasing bound, optimal-extension formula, modular rank
  logic, and finite interpolation scope. No blocking issue was found.
- The root reviewer also directly reread the frozen #1022 arithmetic source,
  the relevant FKMS v2 normalization and Theorems 1.1/9.1, its Remark 1.2 on
  complexity, and the cited standard hypergeometric local-data source. The
  local, coupled and weighted formulas were checked for compatible product
  convention, conjugation, zero extension, and powers of q.

The separately described quadrilinear alternative in the coupled note is
retained as a scoped literature lead. It is not used in any local proof,
numerical result, or asserted native saving.

[MANIFEST.json](MANIFEST.json) records the exact bytes of every other
published file, including the review notes. Its base commit and the frozen
PR head identify the publication. Generated caches and temporary rerun data
are excluded. A future mathematical change requires a new review of the
affected inputs; a previous hash-bound review must not be silently reused.

## Remaining failure point

All local identities can be correct while a global Mobius improvement fails.
The still-unproved step is a uniform estimate for the actual completed signed
weight, including its decomposition cost, all source sectors, fields and
moduli, affine parameters, shifts, and the original D log U normalization.
The package does not claim that step. It also does not infer untwisted
capture from fully dephased covariance, which provably loses the signs.
