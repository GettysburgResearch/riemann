# Exact function-field L-family laboratory

Status: exact finite exploration, all-odd-`q` coefficient lemmas, compact-group
comparators, and explicitly firewalled conjecture packets for L-family
programmes #737 and #741.

Scope: odd finite fields, elementary polynomial arithmetic, frozen exhaustive
genus-two families through `q=7`, a genus-one cubic regression through `q=13`,
closed symbolic divisor sums, and exact `USp(2g)` character calculations.
Nothing here implies RH or GRH over the integers.

## Files

- `pilot.py` implements dependency-free polynomial arithmetic, factorization,
  quadratic symbols, polynomial Moebius values, `L` coefficients, direct and
  formal reciprocal coefficients, and exact critical normalization in
  `Q(sqrt(q))`.
- `fixtures.json` is the compact frozen output for the cubic `F_5[T]` family.
- `REPORT.md` states the identities, finite theorem, counterexamples, and scope
  firewalls.
- `tests/test_function_field.py` independently exercises the arithmetic and
  replays the frozen fixture.

The genus-one, genus-two, and cross-rank extensions are organized as
source/note/JSON/test packets:

- `GENUS1_CUBIC_FAMILY_LAWS.md` proves the all-odd-`q` marked-model,
  elliptic-stack, and coarse even-moment formulas from the stated standard
  modular-trace input, distinguishes the full affine branch quotient from the
  elliptic quotient, and freezes `q=3,5,7,11,13` as regressions;
- `GENUS2_MOMENT_IDENTITY.md` proves the current all-`q` coefficient moments;
- `FAMILY_MEASURES.md` separates uniform models, affine-stack weights, and
  uniform coarse orbits;
- `HYPERELLIPTIC_AFFINE_BURNSIDE.md` gives the exact affine-orbit divisor sum
  for every odd degree `2g+1` and the rational generating series across all
  degrees, exposing multiplicative and additive automorphism resonances;
- `USP_COEFFICIENT_MINOR_RANK_SCAN.md` identifies which sign patterns are
  forced by symplectic representation theory and constructs the balanced
  control `B=2e_1^2-e_2^2`;
- `BALANCED_CONTROL_FAMILY_SCAN.md` independently enumerates `q=3,5,7`, locks
  the exact mean and raw coefficient sums to a member ledger, and reduces the
  unresolved third moment to the explicit virtual character `R_6`;
- `FROBENIUS_POWER_ECHOES.md` proves the all-power recurrence and two-coordinate
  `(B_1,B_2)` collapse, computes the exact Haar additive-frequency resonances,
  and keeps its three-field `mean(B_2)` formula quarantined as conjectural;
- `GENUS2_TAIL_GEOMETRY.md` resolves the frozen negative tail into split,
  repeated, and simple Frobenius geometries; and
- `GENUS2_HIGH_WEIGHT_CHANNEL_PROBE.md` triangularizes the three unresolved
  raw moments and records a sparse all-`q` conjecture without promoting it to
  a theorem.

## Replay

From the repository root:

```text
python research/l-families/atlas/function_field/pilot.py \
  --check research/l-families/atlas/function_field/fixtures.json
python tests/test_function_field.py

python research/l-families/atlas/function_field/genus2_family_measures.py \
  --check research/l-families/atlas/function_field/genus2_family_measures.json
python research/l-families/atlas/function_field/hyperelliptic_affine_burnside.py \
  --check research/l-families/atlas/function_field/hyperelliptic_affine_burnside.json
python research/l-families/atlas/function_field/genus1_cubic_family_laws.py \
  --check research/l-families/atlas/function_field/genus1_cubic_family_laws.json
python research/l-families/atlas/function_field/usp_coefficient_minor_rank_scan.py --check
python research/l-families/atlas/function_field/balanced_control_family_scan.py \
  --check research/l-families/atlas/function_field/balanced_control_family_scan.json
python research/l-families/atlas/function_field/frobenius_power_echoes.py --check
python research/l-families/atlas/function_field/genus2_tail_geometry.py \
  --check research/l-families/atlas/function_field/genus2_tail_geometry.json
python research/l-families/atlas/function_field/genus2_high_weight_channel_probe.py \
  --check research/l-families/atlas/function_field/genus2_high_weight_channel_probe.json

python -m pytest -q \
  tests/test_genus2_family_measures.py \
  tests/test_hyperelliptic_affine_burnside.py \
  tests/test_genus1_cubic_family_laws.py \
  tests/test_usp_coefficient_minor_rank_scan.py \
  tests/test_balanced_control_family_scan.py \
  tests/test_frobenius_power_echoes.py \
  tests/test_genus2_tail_geometry.py \
  tests/test_genus2_high_weight_channel_probe.py
```

Each packet declares its own resource contract. The Burnside, measure,
cross-rank, tail, high-weight, and power-echo packets enumerate no new finite
field or family member; the echo packet transforms the source-locked
`q=3,5,7` histogram. The balanced-control scan independently visits all
20,175 genus-two candidates at `q=3,5,7`, while the genus-one regression
visits 4,023 cubic candidates at `q=3,5,7,11,13`. The producers retain their
explicit per-field candidate and exact-operation caps. No frozen genus-two
field exceeds `q=7`; the separate genus-one regression stops at `q=13`.

## Scientific boundary

The fixture's signed statistic is the explicitly defined normalized product
`H_D(1) H_D(2)`. It is a deliberately minimal cross-degree probe. It is not the
repository's same-kernel `XD`, oriented `HCNC`, or physical-occupancy predicate.
Its mixed signs establish only that Frobenius root modulus by itself does not
force this toy signed cross-degree statistic memberwise.

The later genus-two statistic `K_D=q a_D^2-b_D^2` is likewise a named
reciprocal-coefficient toy minor. Compact-group identities, affine presentation
counts, and exact finite-family moments do not identify it with a canonical
analytic Pick/Loewner, `XD`, or `HCNC` detector. Uniform equations coincide
with stabilizer-weighted averaging only on the declared marked affine
quotient, not on the full unpointed curve stack. Exact statements, frozen
three-field observations, and conjectural continuations are labeled
separately in every packet.

For genus one, uniform marked cubics equal the normalized elliptic-stack
measure, not uniform coarse elliptic classes. The signed trace descends to the
square-affine elliptic quotient but changes sign under a nonsquare multiplier,
so it does not descend to the full affine branch quotient. The all-odd-`q`
moment laws are exact and use the stated standard modular-stack trace identity
as their sole imported theorem; the `q=3,5,7,11,13` enumeration is only a
frozen regression. The first automorphic correction occurs at raw moment 10.

For the balanced genus-two control, only the displayed mean is proved for all
odd prime powers. The six moments, raw coefficient sums, and `mean(R_6)` values
are exact frozen `q=3,5,7` facts; the identity
`B^3=6B-2chi_(0,3)+R_6` is an exact pointwise reduction, not an all-`q`
evaluation. For Frobenius powers, the recurrence, Haar orthogonality, and
additive-frequency resonance condition are exact, but orthogonality is not
independence. The proposed all-`q` formula for `mean(B_2)` remains a
quarantined three-field conjecture, and periodic echoes do not prove extra
endomorphisms.
