# NRC32 execution and acceptance boundary

Status: proposed component proofs, same-author exact and directed finite checks.
No independent mathematical acceptance or full native coarse-energy bound.

## Publication verification before this pass

The live PR #905 was open and draft, not merged, with head
`98cf588261473724178231c667595fc09cc216fe`, exactly the preceding DMC31 head.
The remote directory contained MELLIN_DENSE.md, its executable checker,
validation and reports. The source archive was available locally. Therefore
no missing predecessor publication was inferred and no duplicate packet was
uploaded. The prior PR description still emphasized ACC29/SFC30; a stale
summary was not mistaken for missing code.

NRC32 is an additive sibling directory, not an edit of any sealed predecessor
packet. The actual new commit identity belongs in the publication comment
and Git history, not as an invented pre-publication value in this document.

## What was run

The complete default campaign was executed in ordinary and optimized Python.
Both reconstruct canonical report SHA-256

    22fd396d1bcbdb0aa4f89c7029c72b89ae463a401fcd25894e646b1e2fb5b04a

The receipt-authenticated command is

```sh
python -I -S -B verify.py --receipt RECEIPT.json --write result.json
python -I -S -O -B verify.py --receipt RECEIPT.json --check result.json
```

Counts are named by what is actually checked, not reported as an invented
number of independently proved theorems. Across ten square steps there are
1,398,095 native coefficient comparisons, including every index through
1,048,575 in the largest panel. Smaller panels overlap those indices.
The producer reads mu only through each previous cutoff Y; the comparison
sieve reads through the full new endpoint. They are separate implementations
but have the same author. Energy accumulation consumes the producer's output,
not the comparison sieve.

Further checks include 4,096 exact harmonic-primitive values; 59 exact
native block-mean formulas; 635 sign-pattern variance examples, each with
pair, bound and orthogonal-decomposition checks; 12 real-integer Mellin
identities; 16 symbolic taper-translation identities; integer cube roots;
complete mesh coverage; and exact base examples for precision parameters
R=1,2,3,4. Infinite-variable claims rest on PROOF.md, not these examples.

## Arithmetic contract

All producer coefficients are integers. Small identities use fractions.Fraction.
For larger panels every reciprocal increment v(n)/n is enclosed on the grid
2^(-96), using integer floor and ceiling. Partial sums retain both endpoints.
Squaring takes the minimum and maximum square, with zero as the minimum when
an interval crosses zero. Block means are summed before squaring; division
by block length is rounded outwards on the 2^(-192) energy grid. Every output
cell is included. The detail interval is derived from the exact orthogonal
identity as annular_F minus coarse_S; it is not an independent third summation.
The Z budget is separately accumulated from the rational mesh formula with
outward rounding. Its LOWER enclosure exceeds the computed detail UPPER
enclosure in every panel. The 12-place displays are rounded outwards using
integers. No floating-point number enters acceptance.

## Actual negative controls

In BOTH ordinary and optimized Python the following actual CLI processes
returned exit status 1:

```sh
python -I -S -B verify.py --quick --mutation drop_mixed_product
python -I -S -B verify.py --quick --mutation drop_primitive_linear_term
```

The first removes the coefficient at d=6, breaking a mixed product; the
native block-mean comparison rejects it. The second omits the indispensable
linear term from the harmonic primitive; the primitive comparison rejects it.
These two mathematical mutations use the explicitly labeled quick campaign,
not a claimed full-million-index altered-source replay.

A separate altered JSON report promotes full_native_coarse_bound_proved to
true. BOTH complete default reconstructions reject it through --check with
exit status 1. These are full-report CLI refusals. Comparing a report with a
receipt does not itself validate infinite mathematics or authenticate an
external primitive oracle; the defining source algorithms and their limits
are described above. The exact executed responses are in RECEIPT.json.

## Reproducible outputs and limitations

The repository stores the compact receipt rather than the large derived
report. The commands above regenerate every directed interval and compare
its canonical hash. The downloadable archive also includes result.json.
A fresh extracted archive is replayed separately before final delivery.

No high-Mellin quadrature, zero computation, imported subconvexity evaluation,
full repository validator, Lean build, remote CI run or independent proof
review was performed. The older ACC29/SFC30/DMC31 complete campaigns and the
concurrent MCB31 campaign were NOT rerun here; their unchanged proofs and
historical receipts are not relabeled as this pass's validation. Scope is
native finite reconstruction and the new, separately proposed component
estimates. No unbounded arithmetic covariance estimate is certified.
