# All-order outer-strip companions and protected source transport

Status: exploratory analytic and finite-certificate packets; exact-source
review receipts retain the scope of each individual result.
Scope: the actual `Xi(z)=xi(1/2+iz)`, every fixed integer derivative order,
every fixed positive companion parameter, and every point strictly below an
imported complete zero strip. The source-transport extensions are quantitative
on protected compact subsets of that outer half-plane. A complete finite
real census additionally supplies a full lower companion column, with the
same explicit imported completeness qualification as that census.
Exact sources or dependencies: the normalized actual theta identity in
[R16](../../../../../reviews/D-pass3/PROOFS_AND_REPAIRS.md#r16-xi-cardinal-domain-and-complete-background-capture-s01),
the classical complete xi zero strip and entire order, and the named classical
analytic theorems in [THEOREM.md](THEOREM.md), which contains the complete
outer-strip proof used by this packet.
What was actually run: [check_exact.py](check_exact.py), with its generated
finite arithmetic report in [exact_checks.json](exact_checks.json), and
[check_native_slab.py](check_native_slab.py), with its directed actual-source
report in [native_slab_certificate.json](native_slab_certificate.json).
The first checks rational synthetic polynomial and discrete-source fixtures.
The second replays 8,049 primitive sign brackets and 256 full interval boxes,
using the qualified complete-count library input and a complete analytic
tail. Neither finite checker authenticates an infinite Hadamard product.
Smallest remaining gap: an actual-source signed continuation through
`0<y<=A`, uniformly in the real coordinate and with the necessary endpoint,
pole and winding terms. In particular `A=1/2` is available unconditionally;
an imported smaller complete strip remains a premise.

* [THEOREM.md](THEOREM.md) proves that the entry height is `y>A` for every
  fixed derivative order. No growing-order entry condition is necessary in
  that region. It also gives a quantitative half-plane bound from exact
  imaginary-axis theta moments.
* [SOURCE_TRANSPORT.md](SOURCE_TRANSPORT.md) turns those bounds into explicit
  denominator protection and sufficient source-error budgets on compact outer
  regions. Both full-source additive errors and multiplicative corrections
  are covered, with their distinct meanings retained.
* [FINITE_CENSUS_COMPLEMENT.md](FINITE_CENSUS_COMPLEMENT.md) gives a conditional
  finite-domain continuation into the slab. An authenticated complete simple
  real-zero census supplies a finite polynomial, while the complete high-zero
  tail is bounded by the wave's actual-source count. Explicit margins and a
  strict finite error predicate protect the actual companion denominators.
* [NATIVE_SLAB_CERTIFICATE.md](NATIVE_SLAB_CERTIFICATE.md) instantiates that
  complement for actual Xi at order zero and `lambda=10` on
  `|T|<=2,0<=y<=1/2`. Every candidate root endpoint and every compact interval
  box is replayed with directed Arb. The complete-count library contract and
  its historical finite Gram/Rosser input remain explicitly imported.
* [CENSUS_LOCALIZATION.md](CENSUS_LOCALIZATION.md) proves derivative and
  companion nonvanishing in a central column from the complete census.
  [CENSUS_FULL_COLUMN_SECTOR.md](CENSUS_FULL_COLUMN_SECTOR.md) then proves the
  strict sector for every positive lambda in the entire closed lower column
  `|T|<8192-(r+2)/2`, for every integer `0<=r<=16381`. Its complete complex
  Laguerre argument retains all unknown nonreal tail blocks. The
  [exact algebra controls](column_algebra_controls.json) are synthetic
  controls, separately scoped from this analytic theorem.
* [GAUSSIAN_TAIL_TRANSPORT.md](GAUSSIAN_TAIL_TRANSPORT.md) absorbs the complete
  quadratic tail into an auxiliary Laguerre--Polya Gaussian product. Its
  [13-wide certificate](GAUSSIAN_SLAB_CERTIFICATE.md) protects the whole
  Gaussian-parameter interval; its
  [100-wide certificate](BOUND_GAUSSIAN_SLAB_CERTIFICATE.md) uses a native
  [Taylor tail binding](TAYLOR_TAIL_BINDING.md) and an exact
  [finite-product jet](FINITE_PRODUCT_JET.md), retaining every finite factor
  and the full infinite residual. These are order-zero, lambda-ten slabs.
* [QUARTIC_ABSORPTION.md](QUARTIC_ABSORPTION.md) gives a separate complete
  matched-quartic absorption theorem. It does not itself claim a native
  finite-parameter certificate.
* [check_exact.py](check_exact.py) checks finite sign and perturbation adapters
  and exact sharpness fixtures. The proof's classical analytic inputs remain
  mathematical dependencies, independent of this finite computation.

This does not establish RH or exclude a companion zero at unbounded real
part in the remaining slab.
The positive Fourier counterexample in
[DERIVATIVE_COUNTEREXAMPLE.md](../DERIVATIVE_COUNTEREXAMPLE.md) makes the strip
boundary sharp for the general source class used in the theorem.
