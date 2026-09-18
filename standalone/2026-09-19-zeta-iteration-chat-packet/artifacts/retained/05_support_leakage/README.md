# Vasyunin support rigidity and source-aware Gram leakage

**Status:** PROPOSED component proofs with exact finite regression checks.
**Scope:** the discrete Nyman--Beurling Hilbert space, support restrictions,
finite-support duality, and the actual weighted (not periodic) Gram matrix.
**Exact sources/dependencies:** main `f99d9e3908dde4865377c75d9ca051c1f545bf4f`;
Vasyunin's biorthogonal system as reproduced by Balazard; Bagchi's formulation
and squarefree-support implication. See [SOURCES](SOURCES.md).
**Actually run:** standard-library exact rational reconstruction, ordinary
and optimized Python, with negative controls; see [VALIDATION](VALIDATION.md).
**Smallest remaining gap:** a source-specific upper estimate forcing the
actual approximation error to vanish, or the prescribed mollifier norm to
have subpolynomial growth. It is not proved in this packet.

No RH proof, new zero-free region, independent acceptance, or priority claim.
The finite-support dual family is classical. The contribution is the explicit
support consequences and exact head/ramp/tail normal form in our coordinates,
with proofs and replayable checks. It continues the conversation about
functional-equation rigidity and non-circular GCD positivity.

## Main deductions

1. A six-coordinate functional gives a permanent squared-error lower bound
   `1/92` for prime-power-only approximants. In the original fractional-part
   basis, every squarefree denominator is indispensable; any successful
   coefficient sequence must approach `-mu(r)` at each fixed index.
2. The finite-support dual Gram is an integer matrix: a common-divisor sum
   **minus adjacent-divisor correlations**. Its positivity is exact, but
   deleting the adjacent terms is invalid.
3. The dual approximation problem is solved explicitly and unconditionally:
   its error is `1/(N+1)+(H_(N+1)-1)^2/(N+1-H_(N+1))`. This is not the
   RH-relevant primal approximation error.
4. Every actual error splits into three nonnegative quantities: coefficient
   mismatch in the inverse dual Gram, one ramp mode, and the full arithmetic
   tail. The actual Gram satisfies `G_N=F_N^(-1)+R_N`, with `R_N>=0` and
   `trace R_N<11`, uniformly in N. The bound does not make the correction
   small on growing Mobius sources.
5. For the logarithmic Mobius mollifier, the first component is exactly a
   best-linear-fit weighted variance of `psi(k)`. A short analytic lemma
   identifies its RH-strength growth threshold; no required upper bound is
   supplied by matrix positivity.

## Read and replay

Read [PROOF.md](PROOF.md), Sections 1--2, 5--7, then 8. The imported
support-classification converse is isolated in Section 3.

From this directory, with Python 3.10 or newer:

```sh
python verify.py --check results.json --self-test
python -O verify.py --check results.json --self-test
```

The checker reconstructs the finite results from definitions. It does not
use a zeta-zero table, floating-point inversion, an assumed RH gate, or a
self-declared acceptance flag. The finite checks are regressions, not a
formal verification of the infinite proofs.

This is an addition-only standalone packet. No canonical claim, predecessor
file, main branch, workflow, or repository scientific status is changed.
