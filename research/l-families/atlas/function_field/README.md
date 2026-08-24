# Exact function-field L-family laboratory

Status: exact finite exploration, all-odd-`q` coefficient lemmas, compact-group
comparators, and explicitly firewalled conjecture packets for L-family
programmes #737 and #741.

Scope: odd finite fields, elementary polynomial arithmetic, frozen exhaustive
genus-two families through `q=7`, a genus-one cubic regression through `q=13`,
its symmetric-cube functorial pushforward, closed symbolic divisor sums, and
exact `USp(2g)` character calculations. Nothing here implies RH or GRH over
the integers.

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
- `ELLIPTIC_SYMMETRIC_CUBE_FAMILY.md` pushes that locked genus-one family
  through the genuine `Sym^3 H^1` representation, derives its nodal rank-one
  coefficient curve inside `USp(4)`, proves odd-`q` integral-trace injectivity,
  and separates compact membership from arithmetic recognition using an
  explicit nodal false positive;
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
  a theorem;
- `PRODUCT_VARIETY_TENSOR_FAMILY.md` treats the primitive degree-eight,
  weight-two `H^1(E)⊗H^1(C)` factor, proves its rank-three coefficient
  hypersurface and product-Haar fingerprints, derives exact all-`q` finite
  mean corrections from locked marginals, and freezes only the `q=3,5,7`
  histogram convolutions; and
- `TENSOR_TRACE_ZERO_SINGULAR_STRATA.md` puts that hypersurface into the
  pinch-point normal form, determines its full reduced singular plane and
  transverse rank-drop line, and pulls both trace-zero branches back to exact
  square restrictions and formal genus-two factorizations;
- `GENUS2_ENDOSCOPIC_SPLIT_LOCUS.md` classifies the integral `+q`
  elliptic-form quadratic-factor locus in the complete frozen coefficient
  histograms, proves that `B`, `F`, and even the complete balanced echo fail to
  identify it, and keeps realization and polarization claims firewalled;
- `GENUS2_PRIMITIVE_EXTERIOR_SQUARE.md` constructs the primitive degree-five
  `SO(5)` factor of `exterior^2 H^1`, separates the canonical ambient
  polarization line from the genuine fiberwise but not forced-common second
  eigenline, derives exact character Gram defects, and records the frozen
  fifth-moment orientation anomaly; and
- `VIRTUAL_CHARACTER_NULL_DIRECTIONS.md` solves the coefficient-square null
  lattice modulo `e_1e_3=e_1^2`, runs the bounded noncentral panels, and
  upgrades their survivors using an independently reconstructed full `C_2`
  Weyl density.

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
python research/l-families/atlas/function_field/elliptic_symmetric_cube_family.py --check
python research/l-families/atlas/function_field/usp_coefficient_minor_rank_scan.py --check
python research/l-families/atlas/function_field/balanced_control_family_scan.py \
  --check research/l-families/atlas/function_field/balanced_control_family_scan.json
python research/l-families/atlas/function_field/frobenius_power_echoes.py --check
python research/l-families/atlas/function_field/genus2_tail_geometry.py \
  --check research/l-families/atlas/function_field/genus2_tail_geometry.json
python research/l-families/atlas/function_field/genus2_high_weight_channel_probe.py \
  --check research/l-families/atlas/function_field/genus2_high_weight_channel_probe.json
python research/l-families/atlas/function_field/product_variety_tensor_family.py \
  --check research/l-families/atlas/function_field/product_variety_tensor_family.json
python research/l-families/atlas/function_field/tensor_trace_zero_singular_strata.py \
  --check research/l-families/atlas/function_field/tensor_trace_zero_singular_strata.json
python research/l-families/atlas/function_field/genus2_endoscopic_split_locus.py --check
python research/l-families/atlas/function_field/genus2_primitive_exterior_square.py \
  --check research/l-families/atlas/function_field/genus2_primitive_exterior_square.json
python research/l-families/atlas/function_field/virtual_character_null_directions.py --check

python -m pytest -q \
  tests/test_genus2_family_measures.py \
  tests/test_hyperelliptic_affine_burnside.py \
  tests/test_genus1_cubic_family_laws.py \
  tests/test_elliptic_symmetric_cube_family.py \
  tests/test_usp_coefficient_minor_rank_scan.py \
  tests/test_balanced_control_family_scan.py \
  tests/test_frobenius_power_echoes.py \
  tests/test_genus2_tail_geometry.py \
  tests/test_genus2_high_weight_channel_probe.py \
  tests/test_product_variety_tensor_family.py \
  tests/test_tensor_trace_zero_singular_strata.py \
  tests/test_genus2_endoscopic_split_locus.py \
  tests/test_genus2_primitive_exterior_square.py \
  tests/test_virtual_character_null_directions.py
```

Each packet declares its own resource contract. The Burnside, measure,
cross-rank, tail, high-weight, power-echo, elliptic-symmetric-cube,
product-tensor, tensor-singular, integral-factor-locus,
primitive-exterior-square, and virtual-null
packets enumerate no new finite field or family member. The echo packet
transforms its source-locked `q=3,5,7` histogram; the product packet convolves
only the locked genus-one and genus-two histograms for those same fields; its
singular follow-up transforms the same 2,471 histogram atom pairs; the
integral-factor and exterior-square packets transform the 251 locked
genus-two coefficient atoms; the symmetric-cube packet transforms 55 locked
genus-one trace atoms and performs guarded compact-group algebra; and the
virtual-null packet performs exact compact-group algebra only. The
balanced-control scan independently visits all
20,175 genus-two candidates at `q=3,5,7`, while the genus-one regression
visits 4,023 cubic candidates at `q=3,5,7,11,13`. The producers retain their
explicit per-field candidate and declared-work-unit caps. No frozen genus-two
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

The product-variety packet keeps only the primitive weight-two factor
`H^1(E)⊗H^1(C)`, of degree eight; the two Tate lines in the full
`H^2(E×C)` are separate. Its normalized compact image is
`(USp(2)×USp(4))/diag center` inside `SO(8)`, and every member satisfies
`u^2h-u^4+2u^2v+u^2-2uw-w^2=0`. Exactly at Haar level, its trace fourth
moment is `6` rather than generic-`SO(8)` value `3`, while `mean(h)=mean(uw)=1`
rather than `0`. The bridge to the locked cubic fixture is `A=-t_E`. The
all-`q` finite mean corrections use locked marginal theorems; only the
`q=3,5,7` histogram convolutions are frozen. Their law is the ordered
factor-pair model measure, equivalently the product stabilizer-weighted
curve-stack measure, not uniform measure on coarse product varieties. None of
this asserts equidistribution or generic `SO(8)` monodromy.

The singular-strata follow-up studies the containing coefficient hypersurface,
not singularities of `E`, `C`, or `E x C`. In adapted coordinates it is the
pinch-point family `r^2=u^2*lambda`, with reduced singular plane `u=w=0` and
rank-drop line `h+2v+2=0`. Its two product-parameter branches have the formal
factorizations recorded in the packet, but no Honda--Tate/Tate theorem,
Jacobian splitting, isogeny, or extra-endomorphism conclusion is imported.

The integral-factor packet classifies only factorizations
`(1-rT+qT^2)(1-sT+qT^2)` with integral `r,s`. Its complement is not called
“nonsplit over Z”: at `q=5`, `1-10T^2+25T^4=(1-5T^2)^2` is the explicit
counterexample. Mixed detector fibers cross this precise `+q` elliptic-form
boundary; repeated-versus-distinct collisions within the split locus are
reported separately. Polynomial factorization alone is not a polarization,
curve-product, or geometric-simplicity theorem.

The elliptic symmetric cube is a genuine `l`-adic representation and its
global functorial lift is classical. The packet claims neither as new. Its
coefficient equation detects the compact `Sym^3(SU(2))` image, not arithmetic
origin: the nodal point `(x,y)=(0,0)` lies on that curve but would require
`t^2=2q`, impossible for an odd-`q` integral elliptic trace. The mod-four lemma
proves only that no real trace fiber contains two arithmetic lattice points;
it does not say the lattice misses every real folded fiber.

The primitive exterior square removes the canonical polarization line from
`exterior^2 H^1`. Its remaining ambient `SO(5)` standard factor has a
`(1-qT)` divisor at every good Frobenius element. On each finite-field fiber
that eigenspace is a genuine Frobenius-stable line, but ambient representation
theory forces no second common line. The actual family monodromy is unproved,
and endoscopic loci can acquire one. The formal step is assembling the varying
quartics into a compatible family or cross-prime system. The negative frozen
fifth moments are three-field facts, not evidence against an eventual `SO(5)`
limit.

For virtual-character null directions, quotienting the coefficient-square
lattice by `e_1e_3=e_1^2` leaves the single primitive direction
`B=2e_1^2-e_2^2`. The declared bounded panels isolate `B` among noncentral
directions, but this is deliberately local: globally `B` generates the exact
infinite module `B Z[u^2+v^2,u^2v^2]`, alongside the independently symmetric
center-odd sector. The replay reconstructs the complete `C_2` Weyl density
independently and checks its full support. These are compact-group statements;
the packet makes no arithmetic-family claim.
