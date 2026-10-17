# Validation and precise limits

## What was actually run

The full standard-library checker ran under ordinary Python and python -O;
both reproduce CHECKS.json byte for byte. It includes:

- Every rational norm coefficient through 4096, checked both by local
  split/inert Euler factors and by the independent integer convolution
  mu*(chi_-3*mu), with the original 2/3 exclusions.
- Every good squarefree ideal through norm 1024: 286 including the unit.
  Split conjugates are distinct ideal labels. All same-norm signs and
  multiplicities are retained.
- Every selected ideal pair in the complete norm-cap-512 covariance box:
  147 ideals, 346 selected pairs in one orientation and 96 distinct norm
  pair keys. Their complete coefficient dictionary is independently
  reconstructed by the ratio/shared-factor formula. Two rational kernels
  test the whole finite sector. The opposite orientation is its transpose.
- 4096 exact normalized-ratio coefficient identities; the actual
  incomparable-ideal example with norms 91 and 7; both signs; and the
  repeated split-prime branch in the pair (49,7).
- The two local square-mass Euler products and 300 exact rational
  square-completion checks for the inherited Gaussian kernel.
- Ten rigorous interval log/exp reciprocal identities at declared integers.

The infinite coefficient certificate uses all rational indices through
65536, with 6293 nonzero b coefficients including the unit. It then applies
the explicit global tail derived from I_K(x)<=3x. No analytic rate is fitted
to those 65,536 indices. CHECKS.json gives exact dyadic numerators and
outward decimal renderings, the finite sums, both analytic tail bounds and
the resulting Lambda and second-log-moment inequalities.

The reported interval for Lambda(0)-C2/400 bounds a LOWER-BOUND EXPRESSION
for the fixed-center band. It is not an enclosure of every Lambda(t) in
that band: at zero Lambda is larger. No such misinterpretation is used.

## Actual corruption tests

run_mutations.py executes four separately corrupted Python -O processes in
isolated temporary directories. All exit nonzero with the recorded
ArithmeticError: collapsed split conjugates, a wrong inert sign, an omitted
shared-prime branch, and omission of the shared factor in b(p). This is
actual executed mutation testing, not merely four conceptual examples.
The finite constructions share ordinary integer factorization conventions;
they are not independent number-field backends or independent referees.

## Development correction

The first full certificate run stopped with a TypeError because the new
interval class lacked reverse division for 1/interval. That method was
added using exact endpoint reciprocals. Both complete execution modes were
then rerun successfully. No failed numerical output was retained as a
successful certificate, and no mathematical statement was inferred from it.

## What these checks do not establish

The finite algebra checks do not certify the infinite contour shift or the
field-count proof. The infinite-constant enclosure is a proof-producing
arithmetic calculation only together with the stated remainder theorems.
It does not certify the entire Gaussian energy or an infinite theta sum.

Proofs and checkers have one author. No independent human/agent review,
proof-assistant build, upstream theta replay, full-repository validator,
remote CI run or authenticated GitHub write took place.

The remaining full fixed-center upper bound was not proved. The explicit
positive lower bound for its complement is not an upper estimate. The
D^(-1/2+epsilon) error belongs only to the selected covariance asymptotic.

## Preserved earlier local work

The separate fourteen-file earlier norm-fiber companion was freshly replayed
in ordinary and optimized Python; both match its archived 34,361-predicate
JSON. Its own manifest also passes. These are same-author replay checks, not
independent mathematical review. All fourteen files are byte-preserved in
the outer companion. They are not silently pushed or included in the new
add-only patch.

## Publication/package verification

The manifest binds every payload in this new standalone directory except
itself. The add-only Git patch is generated from a local empty-tree fixture,
not a claimed complete clone; it is intended for application after checking
out the exact remote base in PUBLICATION.md. A fresh extraction replay and
patch-application check are recorded in the outer packaging receipt. No
remote blob verification can be claimed for files that were not pushed.
