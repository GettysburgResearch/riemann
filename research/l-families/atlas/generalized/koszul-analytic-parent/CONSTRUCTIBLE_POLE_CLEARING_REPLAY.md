# Constructible pole clearing: exact source replay

The [source theorem](CONSTRUCTIBLE_POLE_CLEARING_SOURCE.md) defines each
finite grade of a constructible sheaf algebra before taking Euler factors.
It extends the coherent Segre algebra by ordinary j_* first, then adjoins
the actual standard sheaf as polynomial generators in grading degree two.
The resulting full place-Euler function is exactly P_E(z^2) E_chi(z).
It is a new source and function, not a redefinition of the original.

The runtime authenticates the effective resonant source packet at
`e196fa1e4265b482ad1fa495436ed0e4ff088419` before importing its source
chain. It checks actual standard determinants, tensor/symmetric-power
convolutions, and all good and ramified strata. At old C2 inertia the
two orders of extension give degree-three traces23 versus26, with their
actual quadratic sign retained. Split infinity gives degree-four25
versus38; nonsplit infinity gives traces3 versus4. At zero the untwisted
standard generator commutes with central quadratic inertia, as it should.

The first two global coefficients are independently rebuilt from every
rational stalk and the inherited closed-degree-two first-grade trace.
They agree with multiplication by the actual elliptic polynomial.
The three original finite-field panels are reused through degrees one
and two, at field order at most49; no parameter or field is added.

The sharp coefficient dichotomy uses the proved all-grade pole divisor,
not finite coefficient fitting. Actual low-grade relation modules verify
the surviving fourth-grade nonresonant denominator. The existing
F7-to-F49 Frobenius-square source supplies the fully resonant comparison,
without counting F49 anew. Only the fully resonant source has its entire
interior pole set removed. For other sources the new eighth-power growth
is distinct from the original quarter-power growth.

From the repository root with the serialized Python runtime:

```text
python -B research/l-families/atlas/generalized/koszul-analytic-parent/constructible_pole_clearing_replay.py --check
python -B -O research/l-families/atlas/generalized/koszul-analytic-parent/constructible_pole_clearing_replay.py --check
python -B -m unittest discover -s research/l-families/atlas/generalized/koszul-analytic-parent/tests -p test_constructible_pole_clearing.py
python -B -O -m unittest discover -s research/l-families/atlas/generalized/koszul-analytic-parent/tests -p test_constructible_pole_clearing.py
```

Root executed the serialized focused Ruff checks, producer write/check
and optimized check, and all 23 tests in both normal and optimized modes;
all passed. The source proof, runtime and tests have independently been
read without a blocking finding. The exact-freeze review follows final
source binding. The fixture binds all four packet source files and the
complete typed output. No cohomology of one
infinite-rank sheaf, inherited degree-one Koszul parity, or additional
ordinary Fredholm convergence is inferred from this algebra construction.
