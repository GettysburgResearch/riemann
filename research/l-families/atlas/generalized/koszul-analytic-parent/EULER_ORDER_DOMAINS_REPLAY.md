# Euler degree order and the exact pole divisor: source replay

The [four-domain proof](EULER_ORDER_AND_FOUR_DOMAINS.md) separates
absolute local-factor convergence, normally convergent good logarithms
grouped by closed degree, the full coherent Taylor radius, and the
meromorphic continuation disk. The [pole-divisor companion](S3_WEIGHT_CIRCLE_POLE_DIVISOR.md)
classifies every interior arithmetic pole, including cancellation of
an even grade's apparent elliptic pole by the principal zero at twice
that grade. Local Segre zeros away from these arithmetic points are
not asserted to be part of that pole classification.

The runtime authenticates the coherent source at
`5104c38614461a3e080c93631b855094d0e5961a` before import. That frozen
chain authenticates the actual curves, first Lie grades, full ramified
source and both finite and analytic predecessor theorems.

For the original three panels, the first two extension histograms
recover the signed old branch divisor. A possible single degree-four
orbit uses the exact base-field norm of a branch root, not a degree-four
field enumeration. The resulting compact first-grade polynomial has
H^1 rank24, split into twelve proper Weil eigenvalues and twelve
boundary eigenvalues. Its first two traces are checked against actual
good fibres; later displayed traces are derived cohomologically and
are not labelled new primitive point counts.

Rational bounds certify the complete grouped-degree tail at radii
outside the absolute Euler disk but inside the Weil log disk. Exact
local logarithm coefficients, the split-place linear lower bound and
the formal even bad-root control keep those domains distinct. The first
good-zero polynomial has degree14; it is explicitly not claimed to be
the zeta numerator of a new genus-seven curve.

The new resonance example counts only the seven-element base field
for the actual generic parameter A=1,B=0. It obtains the F49 Frobenius
polynomials by squaring the established two-dimensional matrices.
It never enumerates F49 for that example. Actual M_4 and M_8 source
multiplicities give exact grade-four cancellation, while the grade-two
pole survives. Nonsquare trace-zero eigenvalues square to -Q and are
kept distinct from the real alpha^2=Q cancellation condition.

From the repository root with the serialized Python runtime:

```text
python -B research/l-families/atlas/generalized/koszul-analytic-parent/euler_order_domains_replay.py --check
python -B -O research/l-families/atlas/generalized/koszul-analytic-parent/euler_order_domains_replay.py --check
python -B -m unittest discover -s research/l-families/atlas/generalized/koszul-analytic-parent/tests -p test_euler_order_domains.py
python -B -O -m unittest discover -s research/l-families/atlas/generalized/koszul-analytic-parent/tests -p test_euler_order_domains.py
```

The root agent executed the serialized focused Ruff checks, producer
write/check and optimized check, and all 27 tests in each normal and
optimized mode; all passed. Both proof notes, the runtime and all
controls have independently been read without a blocking finding.
The exact-freeze review follows the final source binding. The fixture
binds all five packet source files and checks the complete typed payload.
No finite sampling is used as proof of the all-degree pole classification
or a convergence boundary.
