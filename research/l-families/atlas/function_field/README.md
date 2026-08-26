# Exact function-field L-family laboratory

Status: exact finite exploration, all-odd-`q` coefficient lemmas, compact-group
comparators, and explicitly firewalled conjecture packets for L-family
programmes #737 and #741.

Scope: odd finite fields, elementary polynomial arithmetic, frozen exhaustive
genus-two families through `q=7`, a genus-one cubic regression through `q=13`,
its symmetric-cube functorial pushforward, closed symbolic divisor sums, and
exact `USp(2g)` character calculations. Nothing here implies RH or GRH over
the integers.

## Current successor front door

PR #757 adds a large proof-graded successor spanning the fixed-mollified beta
RH equivalence, its compact boundary primitive and native
reflection/geodesic forms, its exact ratio-16 beta near-correlation criterion,
its localization beyond every prescribed subpower primitive-height cutoff,
and exact Möbius--Gram/biased-Boolean normal forms for the remaining
primitive-pair target, now identified as the fixed-height harmonic limit of
the actual incidence Gram together with a stronger dyadic `PRIMCAR` gate and
an exact invertible convolution which proves the `rho`-weighted one-variable
Möbius coefficient has the same positive Mertens exponents as ordinary
Möbius, while the pair zero mode becomes a Boolean-compressed weighted
superposition whose squarefreeness, coprimality, and sieve incidence reassemble
in the same generalized primitive panel with scales `(A,B,q)`. For
each of the three actual `(alpha,0)` channels, fixed squarefree
67-free `q` has
`3^omega(q)` compatible colorings and `d=1` has
`2^omega(q)` saturated rays. The exact positive-norm hierarchy is
`RAYPRIMCAR -> COLLPRIMCAR <- GENPRIMCAR`: the two stronger gates
are formally incomparable, the former pays a convergent
`K_67(epsilon)` cost for `0<epsilon<1`, and the latter a
polylogarithmic height tax. All three estimates remain open. The successor
also proves that all compatible `r/s` colors at fixed `(d,u=rs)` have
one common weight, so their interference can be retained before taking a
norm. The resulting quadratic `AUXCOLORPRIMCAR` gate
(`COLORPRIMCAR` at `D=1`) controls the auxiliary rho-sieved energy
with sharp Hilbert cost `J_67`; `RAYPRIMCAR` implies it, while it is
formally incomparable with `COLLPRIMCAR` and `GENPRIMCAR`. This
fourth estimate is also open and leaves nonzero incidence modes untouched.
Its quadratic energy is exactly a signed primitive-pair support-overlap Gram
with kernel `prod_(p|gcd(N,M))(1+sqrt(p)/(p+1))`; the formula is exact,
but its cross terms are not positive and its local determinant degenerates.
The successor
also includes the exact refutation of the raw Jordan premise,
hard-mask relative projectors and conductor ledgers, odd-notch boundary
densities through every fixed depth, their local anti-concentration law, and
an `O(M^-2)` whole-layer theorem through logarithmically growing depth,
plus a profile chi-square criterion which permits a logarithmic gap to the
residue-entropy wall when its discrete modulus satisfies the displayed gate,
and an exact detector-specific squareclass quotient which crosses that wall
by an additive `log log` depth window,
the forced exponential mass of an exact universal cycle selector, its exact-
finite derangement relaxation through degree ten, a universal degree-shell
ternary norm torsor of physical rank `48` and linear tame boundary cost, and
an exact closed-point Adams extractor which replaces the exponential cycle
selector by `2^(omega(a)+omega(b))` nonzero signed traces for separable
kernels, and
an all-degree `tanh` structural calibration with a sharp nonhook gap,
descent-set rigidity, almost-half-depth two-row propagation, and a stable-tail
theorem which forces exponential transport throughout every fixed edge
neighborhood while leaving the moving-tail bulk gate open,
and the genus-two `Sym^12`
comparison. For `Sym^12`, the exact `p=3,5,7` residual has a unique formal
one-Tate repair inside the displayed carrier ledger; actual compact-support
Galois realization and any all-`q` correction remain open.
Do not try to infer that frontier from the alphabetical packet list below.
Start at:

1. [`SHEAF_AMPLIFIER_FIVE_MINUTE_HANDOFF.md`](../SHEAF_AMPLIFIER_FIVE_MINUTE_HANDOFF.md);
2. [`SHEAF_AMPLIFIER_RESEARCH_MAP.md`](../SHEAF_AMPLIFIER_RESEARCH_MAP.md);
3. [`SHEAF_AMPLIFIER_RELEASE_AUDIT.md`](../SHEAF_AMPLIFIER_RELEASE_AUDIT.md).

Nothing in that successor proves RH or GRH. The native reflection estimate
is an exact RH-equivalent open gate, not a completed estimate.

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
- `ELLIPTIC_SYMMETRIC_FOURTH_SO5_SLICE.md` constructs the degree-five
  `Sym^4 H^1` factor, identifies its rational nodal principal-`SO(3)` curve
  inside `SO(5)`, proves that the node has no rational arithmetic preimage,
  and separates its cubic trace moment from the generic `SO(5)` law;
- `ELLIPTIC_PAIR_RANKIN_SO4_FAMILY.md` constructs the degree-four tensor
  factor of two independent elliptic traces, proves its exact semialgebraic
  `SO(4)` coefficient region, separates the coefficient-map fold from the
  full quartic repeated-root divisor, and locks the all-`q` low moments and
  five finite product laws;
- `ELLIPTIC_SO4_SYM3_SPECTRAL_INTERSECTION.md` factors the symmetric-cube
  curve inside that `SO(4)` region into four signed Frobenius-doubling graphs,
  proves that nonsquare odd prime powers have no integral hits, and classifies
  both the square-`q` Hasse lattice and its Waterhouse-realized sublocus;
- `ELLIPTIC_SYMMETRIC_POWER_TRACE_ALIASING.md` proves the exact mod-six
  dichotomy for recovering an integral elliptic trace from the scalar
  `Sym^m` trace, gives sharp source-witnessed complementary collisions, and
  separates scalar aliases from full-local-factor aliases;
- `ELLIPTIC_SYM5_COLLISION_DIOPHANTINE_PILOT.md` turns the scalar `Sym^5`
  collision equation into a discriminant-first trace-pair sieve, proves its
  zero-fiber and weighted-scaling laws, identifies a positive-rank elliptic
  collision curve, and certifies three locally realized prime-field examples
  while keeping integral and global realization questions open;
- `ELLIPTIC_SYM5_COEFFICIENT_RECOVERY.md` proves over `Q` that the first two
  `Sym^5` coefficients resolve every non-sign scalar collision, the third
  removes the `t^2=q` sign fiber, and only `t^2=3q` remains invisible to the
  complete local factor; it also gives the exterior-power plethystic reason;
- `ELLIPTIC_SYMMETRIC_POWER_FULL_FACTOR_SIGN_ALIASES.md` proves for every
  `m>=1` that a fixed-`q` rational complete-factor collision is a sign pair,
  classifies the exact even- and odd-degree sign stabilizers, and isolates the
  sole nonzero odd-prime-power integral family;
- `ELLIPTIC_SYMMETRIC_POWER_CYCLOTOMIC_SPECTRAL_ALIASES.md` classifies every
  complete-spectrum collision among primitive odd-order torus classes, gives
  the three universal exceptional factors, and certifies the algebraic trace
  examples at orders `5,7,9,11` while preserving the rational boundary;
- `ELLIPTIC_SYMMETRIC_POWER_EVEN_CYCLOTOMIC_ALIASES.md` completes the
  root-of-unity analysis at order `N=2M`, proving the parity-coset affine
  stabilizer theorem, the exact central-sign lifts, all three edge factors,
  and the sharp primitive nonsign exception list `4,6,8,12`;
- `ELLIPTIC_TENSOR_SYM2_SYM5_SPECTRAL_INTERSECTION.md` proves that the
  correctly dilated degree-six `Std(E_A) tensor Sym^2(E_B)` and `Sym^5(E_C)`
  factors meet on exactly two rational Chebyshev graph families, classifies
  their orders `7,12,14` algebraic residuals and every odd-prime-power Hasse
  lattice point, and embeds both graphs in an exact all-`r` torus ladder;
- `ELLIPTIC_TENSOR_SYMMETRIC_POWER_SUBTORUS_RIGIDITY.md` proves that those
  two graph families exhaust every integer monomial one-parameter subtorus at
  every rung, including nonprimitive target reparameterizations, and records
  the independent Weyl signs, central-sign parity, and `r=1` swap orbit;
- `ELLIPTIC_TENSOR_SYM3_SYM7_SPECTRAL_INTERSECTION.md` closes the next
  degree-eight rung over integral odd-prime-power raw traces: nonsquare bases
  are empty, square bases have a closed Hasse count, and all off-graph
  algebraic support is isolated on five explicit cyclotomic factors;
- `ELLIPTIC_TENSOR_SYMMETRIC_POWER_MOMENT_LADDER.md` proves closed `SU(2)`
  invariant counts through degree eight and shows that the independent tensor
  and principal symmetric-power laws first separate universally at degree six;
- `ELLIPTIC_TENSOR_SYMMETRIC_POWER_HASSE_GRAPH_COUNTS.md` unifies the
  arithmetic counts of both universal graph loci for every `r`, including
  square bases, the nonsquare odd-prime parity split, central-sign duplicates,
  and the exact Chebyshev-period overlap;
- `ELLIPTIC_SYMMETRIC_POWER_HIGH_RANK_HAAR_LIMIT.md` proves the oscillatory
  high-symmetric-power weak limit, its exact cubic tail, the endpoint
  boundary-layer growth of all higher even moments, and the distinct product
  versus principal limiting tail constants;
- `TENSOR_SYMMETRIC_POWER_RESEARCH_MAP.md` is the compact handoff index for
  the complete dependency chain, theorem/evidence boundary, canonical
  payloads, visibility warnings, replay commands, and five next attacks;
- `GENUS2_SYM3_COEFFICIENT_INTERSECTION.md` intersects the symmetric-cube
  curve with the complete locked genus-two coefficient support, classifies
  the odd-prime arithmetic candidates, and separates 53 witnessed members
  from 398 compact-curve ghosts;
- `SYM3_EXTERIOR_SYM4_PLETHYSM_BRIDGE.md` proves that the primitive exterior
  square of the elliptic symmetric cube is the determinant-twisted symmetric
  fourth, makes the normalized coefficient diagram commute identically, and
  reproduces the seven locked genus-two curve hits by an independent path;
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
- `TENSOR_ENDOSCOPIC_RANK_DROP_BRIDGE.md` proves the exact sum-of-squares
  identity relating that transverse rank drop to the integral `+q` split
  locus, distinguishes reduced containment from the doubled scheme pullback,
  and freezes the complete rank/split incidence tables;
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
python research/l-families/atlas/function_field/elliptic_symmetric_fourth_so5_slice.py --check
python research/l-families/atlas/function_field/elliptic_pair_rankin_so4_family.py --check
python research/l-families/atlas/function_field/elliptic_so4_sym3_spectral_intersection.py --check
python research/l-families/atlas/function_field/elliptic_symmetric_power_trace_aliasing.py --check
python research/l-families/atlas/function_field/elliptic_sym5_collision_diophantine_pilot.py --check
python research/l-families/atlas/function_field/elliptic_sym5_coefficient_recovery.py --check
python research/l-families/atlas/function_field/elliptic_symmetric_power_full_factor_sign_aliases.py --check
python research/l-families/atlas/function_field/elliptic_symmetric_power_cyclotomic_spectral_aliases.py --check
python research/l-families/atlas/function_field/elliptic_symmetric_power_even_cyclotomic_aliases.py --check
python research/l-families/atlas/function_field/elliptic_tensor_sym2_sym5_spectral_intersection.py --check
python research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_subtorus_rigidity.py --check
python research/l-families/atlas/function_field/elliptic_tensor_sym3_sym7_spectral_intersection.py --check
python research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_moment_ladder.py --check
python research/l-families/atlas/function_field/elliptic_tensor_symmetric_power_hasse_graph_counts.py --check
python research/l-families/atlas/function_field/genus2_sym3_coefficient_intersection.py --check
python research/l-families/atlas/function_field/sym3_exterior_sym4_plethysm_bridge.py --check
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
python research/l-families/atlas/function_field/tensor_endoscopic_rank_drop_bridge.py --check
python research/l-families/atlas/function_field/genus2_endoscopic_split_locus.py --check
python research/l-families/atlas/function_field/genus2_primitive_exterior_square.py \
  --check research/l-families/atlas/function_field/genus2_primitive_exterior_square.json
python research/l-families/atlas/function_field/virtual_character_null_directions.py --check

python -m pytest -q \
  tests/test_genus2_family_measures.py \
  tests/test_hyperelliptic_affine_burnside.py \
  tests/test_genus1_cubic_family_laws.py \
  tests/test_elliptic_symmetric_cube_family.py \
  tests/test_elliptic_symmetric_fourth_so5_slice.py \
  tests/test_elliptic_pair_rankin_so4_family.py \
  tests/test_elliptic_so4_sym3_spectral_intersection.py \
  tests/test_elliptic_symmetric_power_trace_aliasing.py \
  tests/test_elliptic_sym5_collision_diophantine_pilot.py \
  tests/test_elliptic_sym5_coefficient_recovery.py \
  tests/test_elliptic_symmetric_power_full_factor_sign_aliases.py \
  tests/test_elliptic_symmetric_power_cyclotomic_spectral_aliases.py \
  tests/test_elliptic_symmetric_power_even_cyclotomic_aliases.py \
  tests/test_elliptic_tensor_sym2_sym5_spectral_intersection.py \
  tests/test_elliptic_tensor_symmetric_power_subtorus_rigidity.py \
  tests/test_elliptic_tensor_sym3_sym7_spectral_intersection.py \
  tests/test_elliptic_tensor_symmetric_power_moment_ladder.py \
  tests/test_elliptic_tensor_symmetric_power_hasse_graph_counts.py \
  tests/test_genus2_sym3_coefficient_intersection.py \
  tests/test_sym3_exterior_sym4_plethysm_bridge.py \
  tests/test_usp_coefficient_minor_rank_scan.py \
  tests/test_balanced_control_family_scan.py \
  tests/test_frobenius_power_echoes.py \
  tests/test_genus2_tail_geometry.py \
  tests/test_genus2_high_weight_channel_probe.py \
  tests/test_product_variety_tensor_family.py \
  tests/test_tensor_trace_zero_singular_strata.py \
  tests/test_tensor_endoscopic_rank_drop_bridge.py \
  tests/test_genus2_endoscopic_split_locus.py \
  tests/test_genus2_primitive_exterior_square.py \
  tests/test_virtual_character_null_directions.py
```

Each packet declares its own resource contract. The Burnside, measure,
cross-rank, tail, high-weight, power-echo, elliptic-symmetric-cube,
elliptic-symmetric-fourth, elliptic-pair-tensor, SO4/Sym3-intersection,
symmetric-power-aliasing, Sym5-collision, Sym5-coefficient-recovery,
rational-full-factor-aliasing, odd-cyclotomic-spectral-aliasing,
even-cyclotomic-spectral-aliasing, tensor-Sym2/Sym5-intersection,
tensor-subtorus-rigidity, tensor-Sym3/Sym7-intersection,
tensor-moment-ladder, tensor-Hasse-graph-counts,
symmetric-cube-intersection, Sym3-exterior/Sym4-plethysm, product-tensor,
tensor-singular, tensor-endoscopic-bridge, integral-factor-locus,
primitive-exterior-square, and virtual-null
packets enumerate no new finite field or family member. The echo packet
transforms its source-locked `q=3,5,7` histogram; the product packet convolves
only the locked genus-one and genus-two histograms for those same fields; its
singular follow-up and rank-drop bridge transform the same 2,471 histogram
atom pairs; the symmetric-cube intersection, integral-factor, and
exterior-square packets transform the 251 locked genus-two coefficient atoms;
the symmetric-cube, symmetric-fourth, and trace-aliasing packets transform 55
locked genus-one trace atoms and perform guarded exact algebra; the plethysm
bridge performs sparse polynomial algebra and replays the same 251 locked
genus-two atoms below its exclusive 512-unit ledger cap; and the
virtual-null packet performs exact compact-group algebra only. The
elliptic-pair packet visits 645 ordered pairs of the 55 locked genus-one
trace atoms, performs no field or curve enumeration, and accounts for 2,661
high-level exact checks below its exclusive 4,000-unit cap; its represented
5,673,644 marked-model pairs remain compressed histogram weights. The
Sym5-collision packet performs a discriminant sieve over 15,931 unordered
Hasse trace pairs, tests 590 signed `q` branches, uses six exact elliptic-group
additions and no curve or field enumeration, and accounts for 16,966 units
below its exclusive 500,000-unit cap. Its frozen census stops at odd prime
powers `q<=2000`, and its large prime is checked by the recorded
Lucas/Pocklington certificate rather than a blind extension of that census.
The SO4/Sym3 packet transforms the same 645 locked atom pairs, checks only
610 tiny synthetic Hasse-lattice points at `q=9,25`, and accounts for
3,334 units below its exclusive 4,000-unit cap. The Sym5 recovery packet
performs a 120-term literal Sylvester determinant, bounded exterior-power
weight checks, and 61 source-row replays for 226 units below its exclusive
25,000-unit cap. The rational full-factor packet accounts for 4,624 exact
residue, factor, and source-lock checks below an exclusive 5,000-unit cap.
The odd-cyclotomic packet accounts for 58,326 stabilizer, autocorrelation,
factor, and minimal-polynomial checks below an exclusive 100,000-unit cap.
The even-cyclotomic packet accounts for 49,735 parity-cycle, affine-interval,
stabilizer, and factor checks below an exclusive 150,000-unit cap. The
tensor-Sym2/Sym5 packet accounts for 12,239 locked-triple, synthetic-lattice,
sparse-reduction, S-pair, and small-certificate units below an exclusive
20,000-unit cap. The generic subtorus packet accounts for 27,938 units below
an exclusive 40,000-unit cap; its exhaustive box stops at `r=16` with 720,816
small weight atoms, while `r=32,64` receive direct canonical checks only. The
tensor-Sym3/Sym7 packet accounts for 19,548 units below an exclusive 25,000-
unit cap, including 7,975 locked triples and 11,458 synthetic `q=9,25`
triples. The moment ladder accounts for 25,317 units below an exclusive
30,000-unit cap and 20,456 bounded Clebsch--Gordan transitions. The all-`r`
Hasse graph packet accounts for 3,071 units below an exclusive 20,000-unit
cap. None of these packets enumerates a field, curve, or model, and none uses
floating point, randomness, or a runtime symbolic package.
The balanced-control scan independently visits all
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

The tensor/endoscopic bridge sharpens only the coefficient-level incidence.
Over the real or integer product law,
`q^2*(h+2v+2)=(A^2+b-2q)^2+(Aa)^2`, so rank drop lies on two integral
`+q` factor branches. The scheme pullback `(Aa,R^2)` doubles the transverse
`R` direction and is not contained as a nilpotent scheme in an asserted
endoscopic moduli locus. Rank drop implies this precise integral
factorization; the converse mostly fails, and no isogeny, polarization, or
geometric splitting theorem is imported.

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

The symmetric-fourth packet likewise uses a classical functorial
representation rather than claiming a new lift. Its normalized coefficient
curve is the principal `SO(3)` slice inside `SO(5)`, not a generic `SO(5)`
family. The middle `q^2` eigenvalue is pointwise and does not force a common
Tate subsystem. The curve's node would require the rational parameter
`a^2/q-2` to satisfy `w^2+w-1=0`, so no rational arithmetic input reaches it.
The symbolic moment laws hold for every odd prime power; automatic numerical
evaluation of `Theta_12(q)` retains the upstream explicit characteristic cap,
with a separate exact supplied-trace API beyond it.

The symmetric-power alias theorem concerns the single scalar
`Tr(Sym^m Frob)`, not the entire degree-`m+1` local factor. For odd `q`, that
scalar recovers the integral base trace exactly when `m=1,3 mod 6`, and up to
the unavoidable sign when `m=2 mod 6`. The complementary construction is
Hasse-admissible for `q=3^(odd)` and source-witnessed at `q=3`; it is not a
general trace-realization theorem. Higher coefficients split the constructed
zero/nonzero aliases, although the special nonzero sign pair at
`m=5 mod 6` can retain the same full factor. The binary quartic attached to
`m=5` is a Diophantine target, not a classification or priority claim.

The elliptic-pair Rankin/SO4 packet uses the ordered product of two independent
locked marked-model measures, equivalently the product elliptic-stack trace
law, not uniform coarse elliptic classes and not a geometrically linked pair
family. Its compact coefficient region is the image of the classical
`(SU(2) x SU(2))/diag center` tensor representation; neither that
representation nor global `GL(2) x GL(2)` Rankin--Selberg theory is claimed as
new. The reconstruction fold is
`D=(p-r)^2`, whereas the exhaustive reciprocal-quartic root discriminant is
`D E^2=(p-r)^2(p-4)^2(r-4)^2`; the endpoint component is absent from the five
locked nonsquare-prime rows but remains part of the all-prime-power theorem.
The local conditions `A=B` and `A=-B` do not prove isomorphism, twisting,
isogeny, a correspondence, or a shared global automorphic representation.
Five exact finite product laws and compact Haar moments prove neither full
arithmetic monodromy nor equidistribution.

The SO4/Sym3 intersection is a compact spectral identity on four signed
torus-doubling graphs, not a representation homomorphism. Its raw tensor and
`Sym^3` factors agree only after the displayed weight-changing variable
dilation when `q` is square. Waterhouse supplies separate local elliptic
isogeny classes on the repeated-root endpoint, unit, and zero-endpoint
strata; it supplies no shared curve, isogeny, cover, compatible system, or
global Euler product. Integral Hasse graph points outside those strata are
explicit arithmetic ghosts, not unclassified elliptic correspondences.

The Sym5 collision pilot studies the single scalar
`E_5(t,q)=Tr(Sym^5 Frob)`, not the complete degree-six local factor. Its 61
collisions at 21 odd prime powers are complete only within `q<=2000`; most
split at the next coefficient, while only the `t^2=3q` sign fiber can retain
the complete factor. Positive rank of `Y^2=X^3-6X+5` supplies infinitely many
rational collision-quartic points, not an integral-point classification,
infinitely many primitive prime or prime-power bases, or even Hasse-integral
data at every multiple. Weighted scaling gives exact Hasse-lattice scalar
identities, but for the three prime bases its nonzero levels over
`p^(2k+1)`, `k>=1`, fail Waterhouse's elliptic-trace realization cases.
Likewise, the algebraic square-`q` zero fiber is not automatically realized:
the traces `+/-sqrt(q)` require `p != 1 mod 3`, and trace zero requires
`p != 1 mod 4`. The three certified prime bases provide separate local
elliptic isogeny classes only; they do not form a compatible family or Euler
product. No literature priority, automorphy, analytic continuation,
zero-free-region, RH, or GRH claim is made.

The Sym5 coefficient-recovery theorem is algebraic over `Q` at fixed
nonzero `q`; it does not require or provide elliptic-trace realization. Its
literal resultant proves that `(E_5,c_2)` has only the two stated sign fibers,
and reciprocity makes `(E_5,c_2,c_3)` equivalent to full-factor equality.
The exterior-power decompositions explain these coefficients locally but do
not assert a new functorial lift, automorphy theorem, compatible family, or
literature priority.

The complete rational symmetric-power collision theorem is likewise local
and fixed-`q`. It excludes `Sym^0`, and its conclusion `x=+/-y` does not
assert that either Hasse-admissible trace is realized by a curve. Universal
sign invariance at even `m` is the central twist quotient, not evidence that
two global objects coincide. The exceptional odd integral family at
`q=3^(odd)` supplies no compatible system or Euler product.

The odd-cyclotomic theorem concerns algebraic semisimple torus classes. The
three universal factors compare classes using one common determinant lift;
changing the lift at odd `m` sends `F(T)` to `F(-T)`. At `N=3` there is only
one primitive class modulo inversion, so the universal collapse is not a
genuine non-sign alias; it becomes genuine for every odd `N>=5`. Even root
orders are handled by the separate parity-coset packet; arithmetic
realization, global families, and literature priority remain outside both.

The even-cyclotomic theorem concerns one primitive parity coset. At even
symmetric power, the two extra lifts available when `4|N` are exactly the
central sign and inversion; they are not a new nonsign phenomenon. The
all-unit edge identities use a common determinant lift and imply neither
elliptic realization nor cross-prime/global compatibility.

The tensor-Sym2/Sym5 theorem is an equality of formal local factors only after
the explicit weight-changing `qT` dilation. Its two rational graph families
exhaust raw rational coefficient solutions, but its Hasse-lattice triples are
not asserted to be simultaneously realized by three elliptic curves. The
orders `7,12,14` residuals are algebraic torus strata, and the all-`r` ladder
gives sufficient spectral loci only; within that packet a complete converse
is proved just for `r=2`. None of this supplies a representation homomorphism,
correspondence, compatible system, automorphic transfer, literature priority,
or RH/GRH consequence.

The tensor/symmetric-power rigidity theorem is exhaustive only for integer
monomial cocharacters. Torsion parameters compare weights modulo their order,
and neither nonmonomial curves nor isolated rational points are classified.
Its elementary all-`r` statement is not a full coefficient-intersection or
arithmetic-realization theorem.

The tensor-Sym3/Sym7 theorem compares weight-four and weight-seven factors
only after the chosen `q^(3/2)` dilation. Its algebraic residual strata at
orders `8,16,20,9/18,7/14` remain genuine even though rational raw descent
excludes them. The square-base Hasse count is a coefficient-lattice count, not
simultaneous realization by three linked elliptic curves, a correspondence,
compatible system, automorphic transfer, literature-priority claim, or
RH/GRH consequence.

The all-`r` moment ladder is exact compact Haar and representation-ring
algebra. It proves neither finite-family equidistribution nor arithmetic
monodromy, and it supplies no curves, motives, compatible systems, or zero
statistics. The generic `USp(2r+2)` comparison retains the displayed low-rank
corrections; its stable moments must not be substituted at small rank. It is
polarization-matched to `Std x Sym^r` only for even `r`; the product is
orthogonal for odd `r`, whereas the principal `Sym^(2r+1)` remains
symplectic. The matched orthogonal comparison is exceptional only at `r=1`,
where `Spin(4)=SU(2)xSU(2)` makes the product exactly standard Haar `SO(4)`.
For every odd `r>=3`, its fourth moment exceeds generic `SO(2r+2)` by
`2r-1`. At `r=3`, `SO(8)` has the boundary eighth moment `106`, not `105`,
because its volume tensor first appears in degree eight.

The all-`r` Hasse theorem counts only the two universal monomial graph loci.
The locked `r=1,2,3` packets separately prove their respective rational or
integral completeness statements, but a full converse remains open in
general: isolated nonmonomial points may still occur for `r>=4`. Counted
triples are not thereby realized by three linked elliptic curves. The
nonsquare theorem is restricted to odd `p`, whereas `p=2` has genuine
Dickson-zero exceptions. Public enumerators fail closed above 4,096 candidate
`C` values; the closed formulas do not enumerate the Hasse interval.
The exact asymptotics also warn against uniform trace-cube sampling: on square
bases graph two dominates for every fixed `r>=2`, while nonsquare arithmetic
removes graph two, retains only a staircase-thin graph one for even `r`, and
removes both for odd `r`. These are visibility statements for raw trace
lattices, not frequencies of realized curves.

The symmetric-cube/genus-two intersection compares normalized coefficient
shapes of different weights; it is not an identity of local factors. Its
all-`q` algebraic curve and odd-prime candidate classification are separate
from the exhaustive `q=3,5,7` census. “Source-witnessed” means that an
elliptic trace with the required parameter occurs in the independent locked
genus-one family, not that the genus-two member is an elliptic symmetric-cube
motive. The three `(0,0)` atoms are compact-image false positives.

The Sym3-exterior/Sym4 bridge is a formal identity in characteristic-zero
representation algebra. The determinant twist and removal of the canonical
line are essential, and the pointwise middle eigenvalue is not a second
common Tate subrepresentation. Its commuting coefficient diagram and equal
finite hit set do not identify genus-two factors with elliptic symmetric-cube
motives, nor do they identify monodromy groups, measures, compatible systems,
or Euler products.

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
