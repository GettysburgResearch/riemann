# Source-corrected Segre place Euler product: exact replay

The [theorem](S3_SEGRE_EULER_MEROMORPHIC_BOUNDARY.md) distinguishes the
full invariant-Segre source at every closed place from the ordinary
arithmetic Lie Fredholm object. It proves meromorphic continuation
to the unit disk by classical finite extraction, an exact natural
boundary from surviving split-place zeros, and a positive first-pole
coefficient asymptotic with exact quarter-power residual scale. Its
general finite-group criterion includes
the already constructed S4 source under the proved weight-circle
noncollision condition. No new curve, Estermann mechanism or RH theorem
is claimed.

The runtime authenticates the arithmetic Lie packet at
`83506c9741bded6c8932163ff8e56b78892155b2` and the actual S4 source
adapter at `da203ad2d170835499a0f4f7484f04ff787ee408` before importing
either. Their dependency chains bind the source Lie modules, actual
curves, primitive counts and ramification. No mutable fixture is
imported without that source chain.

All new primitive recounts remain at field orders 5,25,7,49. The exact
degree-two closed-place formula retains the squaring of a transposition
into identity Frobenius. The complete even-quartic branch divisor has
orbits only of degrees1,2,4, so the two existing extension counts determine
its orbit multiplicities, including the degree-four orbit without a new
degree-four field enumeration. The full place-Euler coefficients are
then checked against independent finite Lie cohomology and the actual
bad-place correction.

The finite extraction controls use the actual Lie eigenblocks and
independent Segre character series. The residue certificate combines
the actual open-closure zeta residue, all bad Segre factors, good-place
tails through degree two and a proved positive rational enclosure for
the omitted degrees. The S4 controls construct M_1 from the actual tensor
source and M_2 from exterior-square relations, then check complete
finite-fibre/cohomology traces; its primitive fields also stay below50.
The root-separation certificate is exact algebraic arithmetic, not a
numerical root fit.

The sharper coefficient controls retain the first four actual S3 Lie
characters and their irreducible constituents. They check the full bad
numerators against independently constructed invariant Segre series,
including the algebraic-unit finite-branch polynomial and the different
split-infinity norm. The finite four-grade cohomological product is
checked against its explicit factorization with denominator P_E(z^2).
The all-coefficient sharp limsup follows from the proved noncancellation,
not a fit to the replay's finite coefficient list.

From the repository root with the serialized Python runtime:

```text
python -B research/l-families/atlas/generalized/koszul-analytic-parent/segre_place_euler_replay.py --check
python -B -O research/l-families/atlas/generalized/koszul-analytic-parent/segre_place_euler_replay.py --check
python -B -m unittest discover -s research/l-families/atlas/generalized/koszul-analytic-parent/tests -p test_segre_place_euler.py
python -B -O -m unittest discover -s research/l-families/atlas/generalized/koszul-analytic-parent/tests -p test_segre_place_euler.py
```

The root agent executed the serialized focused Ruff checks, producer
write/check and optimized check, and all 32 tests in each normal and
optimized mode; all passed. The source theorem, sharper quarter-power
proof, runtime and all controls have been independently read without a
blocking finding. The exact-freeze review follows the final source binding.
The all-degree place theorem, meromorphic continuation, noncancellation,
natural boundary and coefficient asymptotic are proved, not extrapolated
from these finite controls. The fixture binds all four source files and
checks complete typed JSON values.
