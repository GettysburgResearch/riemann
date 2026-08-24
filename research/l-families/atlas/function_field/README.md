# Exact function-field L-family laboratory

Status: exact finite exploration, all-odd-`q` coefficient lemmas, compact-group
comparators, and explicitly firewalled conjecture packets for L-family
programmes #737 and #741.

Scope: odd finite fields, elementary polynomial arithmetic, frozen exhaustive
families only through `q=7`, closed symbolic divisor sums, and exact
`USp(2g)` character calculations. Nothing here implies RH or GRH over the
integers.

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

The genus-two and cross-rank extensions are organized as source/note/JSON/test
packets:

- `GENUS2_MOMENT_IDENTITY.md` proves the current all-`q` coefficient moments;
- `FAMILY_MEASURES.md` separates uniform models, affine-stack weights, and
  uniform coarse orbits;
- `HYPERELLIPTIC_AFFINE_BURNSIDE.md` gives the exact affine-orbit divisor sum
  for every odd degree `2g+1`;
- `USP_COEFFICIENT_MINOR_RANK_SCAN.md` identifies which sign patterns are
  forced by symplectic representation theory and constructs the balanced
  control `B=2e_1^2-e_2^2`;
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
python research/l-families/atlas/function_field/usp_coefficient_minor_rank_scan.py --check
python research/l-families/atlas/function_field/genus2_tail_geometry.py \
  --check research/l-families/atlas/function_field/genus2_tail_geometry.json
python research/l-families/atlas/function_field/genus2_high_weight_channel_probe.py \
  --check research/l-families/atlas/function_field/genus2_high_weight_channel_probe.json

python -m pytest -q \
  tests/test_genus2_family_measures.py \
  tests/test_hyperelliptic_affine_burnside.py \
  tests/test_usp_coefficient_minor_rank_scan.py \
  tests/test_genus2_tail_geometry.py \
  tests/test_genus2_high_weight_channel_probe.py
```

Each packet declares its own resource contract. The new Burnside, measure,
cross-rank, tail, and high-weight packets enumerate no finite field or family
member. The original producers retain explicit candidate and exact-operation
caps; no frozen field exceeds `q=7`.

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
