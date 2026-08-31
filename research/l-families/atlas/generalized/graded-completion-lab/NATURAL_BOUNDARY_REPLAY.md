# Exact Frobenius-ladder residue replay

This packet checks the source arithmetic behind
`FROBENIUS_LADDER_NATURAL_BOUNDARY.md`. The continuation, pole accumulation and
unbounded local-monodromy theorem are proved there, not extrapolated from this
finite replay. The proof and this bounded design were fixed before execution.

The producer authenticates the original completion proof and producer at
`64075f1a3f81529f217dee1ae139656dfb9356f3` before importing any source code.
It separately authenticates the two frozen proofs establishing the actual
finite-ladder factor's single-valued meromorphy on the unit disk. No dependency
on the separate regularized-determinant runtime or its pending freeze is needed.

Declared controls:

* Reconstruct `a_j` by the odd-divisor formula, and compare `j=1,...,32` with
  the actual S3 PBW multiplicities in source grades `2,...,64`.
* Multiply literal integer polynomial factors
  `product_(2<=j<=32) (1-b*x^j)^a_j`, retaining all coefficients through degree
  32, for `b=-7,7,-49,49`. Derive their logarithmic derivatives by formal
  division of the resulting polynomials. Compare both the direct divisor sum
  and the separate logarithmic-residue Euler transform. The missing `j=1`
  factor contributes the indispensable `b^n` correction in the latter route.
* Record the exact residues for every `m=1,...,32`, plus dyadic `m=2^v` for
  `v=0,...,8`. Both integral odd/composite controls and nonintegral dyadic
  controls are included. No complex roots or numerical residues are fitted.
* For `r=1/2,3/4,7/8` and `|b|=7,49`, construct exact rational cutoffs `H,J`
  satisfying the two independent convergence inequalities in the proof.
  Record its geometric derivative-tail bound and compare a finite rectangular
  partial sum of the original positive majorant to that bound. This tests the
  bound's arithmetic; normal convergence is the all-grade proof.
* Compute the same two-by-two Frobenius matrix's powers for extension degrees
  one through four. Compare literal finite proper-factor products with
  `F_(-7^e)(z^4)` for odd `e` and
  `F_((-7)^(e/2))(z^2)^2` for even `e`, through degree 32. In particular the
  F7 coordinate is `x=z^4`, not `z` or `z^2`.

All arithmetic is integer or rational. Multiplicity and divisor indices are
capped at 256, coefficient cutoff at 64, cutoff search at 128, integer bit
length at 16384 and the artifact at four MiB. The declared panels use smaller
coefficient cutoff 32 and indices at most 256. They do not enumerate a finite
field, an exponentially large eigenspace, or a complex branch grid.

`--check` reconstructs the complete payload and compares canonical typed JSON.
It rejects changed values, missing or extra fields, integer-to-boolean or
integer-to-float replacements, nonfinite floats, changed source bytes, and
changed proof/producer/test bindings. The artifact is a bounded certificate,
not a substitute for the source proof.

Execution status: not run by the author. The coordinating agent owns all
Ruff, producer and ordinary/optimized test runs under the shared RAM guard.

```text
python research/l-families/atlas/generalized/graded-completion-lab/natural_boundary_replay.py --write
python research/l-families/atlas/generalized/graded-completion-lab/natural_boundary_replay.py --check
python -O research/l-families/atlas/generalized/graded-completion-lab/natural_boundary_replay.py --check
python -m unittest discover -s tests -p test_graded_completion_natural_boundary.py
python -O -m unittest discover -s tests -p test_graded_completion_natural_boundary.py
```
