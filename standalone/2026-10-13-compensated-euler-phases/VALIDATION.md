# Validation and review boundaries

## Reproduction

Run from this directory with Python 3 and NumPy:

    python verify_completion.py --output replay.json
    python -O verify_completion.py --output replay.optimized.json
    cmp replay.json replay.optimized.json
    cmp replay.json results.json

Both full executions were performed on the final script, and both outputs
are byte-identical to results.json. Acceptance uses explicit exceptions,
not Python assertions disabled by -O. A SHA-256 and Git-blob manifest binds
all six payload files. Hashes authenticate bytes, not mathematical proofs.

## Actual coverage

- 19,870 explicit checks INCLUDING setup and every ideal-norm count, not
  19,870 independent moment experiments.
- Six complete sizes: D=256,512,1024,2048,4096,8192, each with the exact
  integer ceiling H=ceil(D^(21/20)). Every nonzero element in each norm ball
  is included, and every good ideal in D/2<Nn<=D is enumerated.
- All ideal norms through each cap are separately checked against the
  divisor-coefficient formula for zeta_K with the Euler factors at 3 and 4
  removed. Split conjugate ideals and inert prime ideals remain distinct.
- Moment orders 2,4,6,8 for the native source and the completed common-circle
  family; all nonconstant phase energies are included, not a phase grid.
- Local coefficient identities through norm-power degree 12 for r=1,2,3,4:
  logarithmic-tail and direct factor constructions, both signed inverse
  kernels, retained low powers and the unbiased constant coefficient.
- Uniform local majorant diagnostics at the exact parameters -1, omega,
  1+omega and 1/2. The infinite majorant is proved in PROOF.md, not inferred
  from these finite checks.
- Direct circular Laurent multiplication independently reassembles the
  phase averages at three actual rows for D=256 and 512 and all four orders.
  This shares the same primitive field backend; it is not independent review.
- Three negative controls: an extra coprimality restriction changes the
  p^4 convolution, omitting the quadratic counterterm changes the p^2
  coefficient, and replacing a neutral sixth charge by 1 loses a zero mask.
- Four published complete native fourth moments from #943 are reproduced:
  D=256,512,1024,8192. The D=2048 and 4096 results are also retained, not
  omitted because of their zero/different completed excess.

## Arithmetic

Local series use exact rational polynomial coefficients. Sixth-root values
are pairs in Z[omega], omega^2+omega+1=0, with literal zero as a seventh
value. NumPy only accelerates integer row arrays, guarded against int64
overflow in residue, coefficient and product assembly. Final squared norms
and high moments use unbounded Python integers, with exact rational division.
There are no floating-point character values or sampled phase integrals.
The default and permitted diagnostic cap is D<=8192; this is not a claim
that the implementation has been tested at arbitrary larger input sizes.

The code's bounded hard window is NOT the smooth Mellin detector required
by the analytic extraction. Finite values are not a decay rate, a uniform
bound in k, an RH certificate, or a proof of the proposed analytic statements.

## Authorship and external validation

Proof and code have the same author. No independent mathematical referee,
Lean build, full-repository validation, remote CI result, or full re-proof
of an external analytic theorem is claimed. The primitive source and exact
adaptation scope are in SOURCES.md. Theorems 1--2, the coefficient mean in
(8), and fixed-scale stability (10) are the preferred independent review
objects. A review should check that the profile law, row measure, and
exclusions stay fixed at every shortened scale in Theorem 2.

## Publication method

A local clone attempt failed DNS. Publication uses the connected GitHub
Git-data tools on a dedicated branch, with the existing #943 tree as base.
Only this new standalone directory is added. Remote blob identities and
sizes must match MANIFEST.json before the publication is described as
verified. No claim of a clean cloned worktree or integration into main is made.
