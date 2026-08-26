# Residual detector mechanisms: start here

## Release status

This is the front door for the bounded successor pass to the L-function
detector atlas in PR #752. The pass deliberately followed several leads at
once, but it now has three coherent theorem stacks rather than a collection of
unrelated experiments:

1. exact marked and ambient genus-two trace laws, inverse-designed character
   filters, and rare-stratum tomography;
2. a corrected physical-squareclass FFPS bridge, sharp complete-frame no-go
   theorems, and constructive correlated restrictions; and
3. three explicitly fenced moonshots: detector renormalization, Frobenius
   interferometry, and guarded cohomology-conjecture generation.

RH and GRH remain open. Nothing here turns an averaged family law into a
statement about the principal zeta member. The branch is best understood as a
mechanism-discovery and theorem-conjecture engine with a strict provenance
boundary.

For a graded proof-strength, novelty, and RH-criticality assessment, read the
[release audit](RESIDUAL_MECHANISMS_RELEASE_AUDIT.md). Its literature
comparison is deliberately more conservative than the discovery notes.

### Frozen dependencies

- Atlas source: PR #752 at
  `10446e8ea9c55162c317810f63c1f7a379466459`.
- Historical corrected RH-bridge snapshot: PR #751 at
  `37d9df4b9b4fb9a8277de6ec1f77278dbbe5b0f2`, whose operative frontier is
  `T-106121 / FFPS106121`, not the retracted owner-only summary.
- Live PR #751 was separately audited at
  `98af0db6ec7f77d6333a77a3dac53c4698852f43`. The `L-106024` Gram source is
  unchanged, `T-106121` remains exact, the former `BTMS106121` and
  `BTDS106121` routes are withdrawn, and the preferred live bridge repair is
  `T-106140` through `WCADD106140/WCKUM106140`.
- Throughout the FFPS packets the corrected physical coordinates are
  `P*c^2` and `Q*d^2`. Owner-only and fixed-core-to-global promotions are not
  used.

The primary programme handoffs are
[#736](https://github.com/gfreund123/riemann/issues/736),
[#737](https://github.com/gfreund123/riemann/issues/737), and
[#741](https://github.com/gfreund123/riemann/issues/741). The phase-diagram
and physical-source consequences also feed
[#738](https://github.com/gfreund123/riemann/issues/738) and
[#743](https://github.com/gfreund123/riemann/issues/743).

## Five-minute handoff

Choose the route matching the question you want to answer.

### Route A: closest bridge back to the RH programme

Read, in order:

1. [physical-squareclass FFPS adapter](function_field/FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md);
2. [Kummer-transfer spectrum](function_field/FFPS_KUMMER_TRANSFER_SPECTRUM.md);
3. [complete-frame signed-amplifier no-go](function_field/FFPS_TENSOR_SIGNED_AMPLIFIER_NO_GO.md);
4. [correlated-mask amplifier](function_field/FFPS_CORRELATED_MASK_AMPLIFIER.md);
5. [checkerboard source bridge](function_field/FFPS_CHECKERBOARD_SOURCE_BRIDGE.md);
6. [cyclic-character masks](function_field/FFPS_CYCLIC_CHARACTER_MASKS.md);
7. [cyclic source-realization and Wick gate](function_field/FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md);
8. [cyclic closure budget](function_field/FFPS_CYCLIC_CLOSURE_BUDGET.md).

The shortest correct summary is:

- on a complete tensor frame, arbitrary complex reweighting cannot beat the
  uniform coherent tensor;
- a correlated physical restriction changes the Gram metric and can beat the
  complete-frame leverage;
- a raw Legendre label on the core representative is not invariant under the
  corrected physical collapse;
- a quartic-character repair is invariant inside a fixed owner quadratic
  sector and identifies the corresponding soft Fourier mode;
- the same construction extends to common exact-order-`k` masks through an
  exact-order-`2k` root orientation, but every cyclic hard mask that improves
  leverage necessarily leaves a positive Wick atomic residual;
- an exact centered identity removes the literal atoms and names the rotated
  conditioned currents and double-nonprincipal Kummer modes that a global
  proof would have to estimate;
- the declared additive/Kummer gates control exactly the coefficient plane
  `w=u+v` in `(C,S,R)` coordinates, hence the whole principal trace but
  neither cyclic constituent; the one-sided `CYSEL` upper bound is the
  smallest additional cyclic gate;
- converting that hard restriction into a varying-owner global moment and an
  individual principal-member theorem remains open.

This route has the clearest RH relevance because it attacks the
average-to-individual obstruction directly. It is also the route with the
largest remaining source-faithfulness gate.

### Route B: strongest exact standalone mathematics

Read, in order:

1. [marked-Weierstrass stack adapter](function_field/GENUS2_MARKED_WEIERSTRASS_STACK_ADAPTER.md);
2. the exact primitive trace laws for
   [`chi_(0,3)`](function_field/GENUS2_B3_PRIMITIVE_TRACE_AVERAGE.md),
   [`chi_(2,2)`](function_field/GENUS2_M22_TRIANGULAR_TRACE_AVERAGE.md), and
   [`chi_(0,4)`](function_field/GENUS2_B4_TRIANGULAR_TRACE_AVERAGE.md);
3. the marked symmetric-power laws for
   [`Sym^6`](function_field/GENUS2_SYM6_MARKED_TRACE_AVERAGE.md),
   [`Sym^8`](function_field/GENUS2_SYM8_MARKED_TRACE_AVERAGE.md), and
   [`Sym^10`](function_field/GENUS2_SYM10_MARKED_TRACE_AVERAGE.md);
4. the [ambient symmetric-power ladder](function_field/GENUS2_AMBIENT_SYMMETRIC_POWER_LADDER.md);
5. the [inverse cusp filters](function_field/GENUS2_INVERSE_CUSP_TRACE_FILTERS.md)
   and [mixed cohomology filter](function_field/GENUS2_MIXED_COHOMOLOGY_FILTER.md);
6. the [`Sym^12` one-scalar arithmetic inventory](function_field/GENUS2_SYM12_ARITHMETIC_INVENTORY.md),
   [finite cusp-trace scout](function_field/GENUS2_SYM12_FINITE_CUSP_TRACE_SCOUT.md),
   and [conditional endoscopic closure](function_field/GENUS2_SYM12_CONDITIONAL_ENDOSCOPIC_CLOSURE.md);
7. the [`Sym^10` rare-event law](function_field/GENUS2_SYM10_RARE_EVENT_TOMOGRAPHY.md)
   and [scalar endpoint realization](function_field/GENUS2_SYM10_SCALAR_ENDPOINT_REALIZATION.md);
8. the [all-rank scalar-endpoint phase diagram](function_field/GENUS2_SCALAR_ENDPOINT_SYMMETRIC_POWER_PHASE_DIAGRAM.md).

The exact all-odd-prime-power trace ladder is the main object. It separates
Tate, elliptic level-two, and level-one cusp channels and supplies exact
same-characteristic recurrences. The scalar endpoint packet then exhibits a
named rare geometric stratum whose normalized high moments have an explicit
contribution. The all-rank continuation proves the exact crossover surface
`m log binom(r+3,3) = 3 log q + log 5` for that constructed subtotal and a
full-family fixed-`(q,r)` spectral-radius limit, without claiming an
asymptotic for the remaining family.

The ladder no longer ends with an undifferentiated “new input needed” at
`Sym^12`. All lower Euler rows and inherited cusp channels reduce exactly to
one family-specific scalar in the locked method: the normalized
Mobius-weighted aggregate `Hhat_12` of standard central completed
coefficients. Exact finite rows at `p=3,5,7` isolate the Fricke-negative
weight-fourteen level-two newform. The literature comparison sharpens this
to the exact defect identity

`Hhat_12 = -L*f_- + Epsilon_Eis - Genuine`,

where `Epsilon_Eis=e_Eis^(S5)-(2-5L)` and `Genuine` is the positive
stable/general `S5`-invariant channel whose compact-support Euler
contribution is `-Genuine`. The desired all-`q` closure still requires both
the conjectural nonregular Eisenstein continuation `Epsilon_Eis=0` and the
conditionally predicted stable vanishing `Genuine=0`. Shmakov's printed
formula instead gives `Epsilon_Eis=L`, an unresolved one-Tate discrepancy;
the finite rows do not decide it without the stable vanishing. For `q=p^r`,
`-L*f_-` means `-p^r(alpha_{-,p}^r+beta_{-,p}^r)`, not `-q` times a naive
composite-index Fourier coefficient.

This route is the best candidate for independent verification and a focused
paper. It is not currently a direct RH route.

### Route C: detector design and the three moonshots

Read:

1. [detector boundary quotient](function_field/GENUS2_DETECTOR_BOUNDARY_QUOTIENT.md)
   and [`R_6` underdetermination](function_field/GENUS2_R6_PROOF_RECONNAISSANCE.md);
2. [Frobenius subgroup selectors](function_field/FROBENIUS_INTERFEROMETRY_SUBGROUP_SELECTORS.md),
   their [arithmetic pushforward](function_field/GENUS2_INTERFEROMETRY_ARITHMETIC_PUSHFORWARD.md),
   and the [held-out inverse-design failure](function_field/GENUS2_INVERSE_DESIGNED_SPLIT_FILTER.md);
3. [detector renormalization flow](function_field/EULER_DETECTOR_RENORMALIZATION_FLOW.md);
4. its exact arithmetic
   [two-place cumulant defect](function_field/QUADRATIC_FAMILY_TWO_PLACE_CUMULANT_DEFECT.md)
   and [three-place elliptic interference](function_field/QUADRATIC_FAMILY_THREE_PLACE_ELLIPTIC_INTERFERENCE.md),
   followed by the unifying
   [multi-place `L`-function identity](function_field/QUADRATIC_FAMILY_MULTIPLACE_L_FUNCTION_IDENTITY.md)
   and its
   [six-place/weight-ceiling continuation](function_field/QUADRATIC_FAMILY_SIX_PLACE_CONNECTED_SATURATION.md),
   followed by the
   [universal fixed-degree notch](function_field/QUADRATIC_FAMILY_FIXED_DEGREE_WEIGHT_NOTCH.md)
   and its
   [closed-place conductor extension](function_field/QUADRATIC_FAMILY_CLOSED_PLACE_WEIGHT_NOTCH.md),
   then the fixed-`q`
   [structural-zero density law](function_field/QUADRATIC_FAMILY_CLOSED_PLACE_NOTCH_DENSITY.md);
5. [guarded cohomology inference](function_field/GUARDED_COHOMOLOGY_CONJECTURE_INFERENCE.md)
   followed by the exact [same-characteristic spectroscopy](function_field/GENUS2_EXACT_FROBENIUS_TOWER_SPECTROSCOPY.md);
6. the [high-rank Haar boundary-layer tomography](function_field/HIGH_RANK_HAAR_BOUNDARY_LAYER_TOMOGRAPHY.md).

These packets show both sides of inverse design. Exact character algebra can
remove declared nuisance channels and isolate a named residual, but a filter
optimized on `q=3,5` can reverse on untouched `q=7`. Likewise, three fields
cannot name a Frobenius spectrum, whereas an all-`q` theorem supplies genuine
same-characteristic towers and exact minimal recurrences. At three rational
places, the first genuinely geometric interaction is already exact: its raw
triple correlation is `3(q-2)t`, where `t` is the Frobenius trace of the
oriented elliptic curve attached to the three places. Thus Frobenius
interferometry has become an arithmetic theorem rather than only a
compact-group selector. The multi-place packet then proves the all-degree
generating identity behind these correlations and, in degree five, continues
the ladder through four-place elliptic and five-place genus-two traces. The
five-place coefficient forgets the genus-two middle coefficient exactly; it
does not forget the geometry, because the trace remains. Its connected
cumulants retain the same hierarchy: the fourth has a universal `q^-3`
background plus an elliptic correction, while the fifth has genus-two upper
envelope `q^-5/2` and a smaller correction from ten separately labelled
elliptic triples. Across orders two through five the exact/Hasse scales are
`q^-4`, `q^-7/2`, `q^-3`, and `q^-5/2`. This full connected sequence climbs
by a half power: a universal four-place background intervenes before the
genus-two five-place envelope. The trace-dependent `q^-7/2` and `q^-5/2`
entries are upper envelopes, not typical-value theorems. Those ten traces do
not collapse to the five-place trace.

The six-place continuation is a useful stress test rather than just one more
row. It proves the exact raw numerator

`(q^2-21)t_A+(q-6)b_A-q^2+6q-21`

and the complete connected subtraction over the `203` set partitions of six
labels. The leading trace envelope remains `q^-5/2`, the middle genus-two
coefficient re-enters at `q^-3`, and every disconnected correction is
`O(q^-7)` or smaller. Equivalently, this row is the first in the ladder that
sees the second Frobenius power, through
`b_A=(t_A^2-s_(2,A))/2` and the `F_(q^2)` point count.

More importantly, the same exact coefficient extraction has a
representation-ring explanation. Its top weight is
`q^(5/2)(e_3-e_5)`: this is `chi_(omega_1)` in genus two,
`chi_(omega_3)` in genus three, zero in genus four, and
`-chi_(omega_5)` from genus five onward. Thus `q^-5/2` is a fixed-degree
weight ceiling with a genus-four notch, not a monotone rank law. At nine and
ten places the exact leading envelopes improve to `q^-7/2` and `q^-3`, and
connectedization cannot refill the cancelled channel. These remain uniform
upper envelopes for fixed mark count, not sharpness, equidistribution, or
attainment theorems.

The universal continuation shows that this is not peculiar to degree five.
For fixed family degree `n >= 2`, the sole potential top-weight numerator
channel is

`p_n-q p_(n-2)=(-1)^n q^(n/2)(e_n-e_(n-2))`.

As the auxiliary genus varies, this scans fundamental exterior characters of
the same parity as `n`, vanishes at the two interior notch counts
`m=2n-1,2n`, and then stabilizes on `(-1)^n chi_(omega_n)`. The odd notch
drops a full weight and the even split-infinity notch drops a half weight.
Proper connected partitions are `O_(n,m)(q^-n)` and cannot restore the top
channel; `(n,m)=(2,3)` is explicitly exceptional because they instead cancel
the raw scalar leader. This is a fixed-parameter selection rule and aliasing
firewall, not a growing-degree theorem.

The closed-place extension replaces the rational linear factors by a
squarefree primitive conductor `Q=prod_i P_i`, with degree profile `(d_i)`.
It proves

`sum_n S_n(Q)u^n=L(u,psi)(1-qu^2)/prod_i(1-u^(2d_i))`

with the exact reciprocity model `y^2=(-1)^deg(Q)Q`. The top channel and
notch depend only on the primitive conductor degree, while the visible lower
layers are governed by the truncated coefficients of its degree profile. At
the odd notch an irreducible conductor of degree `2n-1` forces the raw family
sum to vanish; at the even notch split infinity leaves a profile-independent
half-weight channel. This also removes the artificial rational-place
constraint `m<=q`, but it does not
supply a varying-conductor equidistribution theorem.

The density sequel answers one fixed-`q` question without invoking
equidistribution. At the odd notch `M=2n-1`, let `Z_(q,n)` count squarefree
primitive conductors all of whose irreducible factor degrees exceed
`floor(n/2)`. Then every counted conductor has exact raw sum `S_(n,Q)=0`,
and

`Z_(q,n)=[x^M] prod_(d>floor(n/2))(1+x^d)^(I_q(d))`.

The strict cutoff permits at most three factors. It yields the rigorous
fixed-`q` law

`Z_(q,n)/q^M=C_0/M+D_epsilon/M^2+O_q(M^-3)`,

where `C_0=4 omega(4)=2.2458329656...`,
`D_even=-4(1+log 2)`, and `D_odd=-(4/3)(1+log 2)`. Conditioning on
squarefreeness multiplies these coefficients by `q/(q-1)`. The Buchstab
rough-polynomial asymptotic is standard; the atlas contribution is its exact
source-locked identification with a structural detector-zero stratum. This
stratum is a certified subset, not a classification of every accidental
raw zero. All 237 bounded DP rows are bound into one canonical digest and
independently recomputed from the one-/two-/three-factor formula; the 45
expanded rows are a sparse readable projection of that authenticated replay.

A separate growing-parameter audit found an important firewall. On rational
marks, the formal compact supremum has a character-dimension entropy
crossover, but `q>=m` makes every proportional `(n,g)` arithmetic regime
superexponentially decaying. The crossover is therefore not a realizable
family phase transition. Closed places make fixed-`q` conductor growth
possible; interpreting it statistically still requires all-channel control
and a genuine family of conductors.

### Extended packet index

The routes above are the shortest digest, not a complete file list. Use this
index when auditing a dependency or continuing a secondary lead.

- **Canonical detector and native port:**
  [norm-lattice obstruction](function_field/CANONICAL_DETECTOR_NORM_LATTICE_OBSTRUCTION.md),
  [uniform dyadic log-phase port](function_field/CANONICAL_DYADIC_LOG_PHASE_PORT.md),
  [native reciprocal-wavelet spectroscopy](function_field/NATIVE_QADIC_RECIPROCAL_WAVELET_SPECTROSCOPY.md),
  [square-tower bifurcation](function_field/NATIVE_QADIC_WAVELET_SQUARE_TOWER_BIFURCATION.md),
  [zero stratum](function_field/NATIVE_QADIC_WAVELET_ZERO_STRATUM.md), and
  [integral spectrum](function_field/NATIVE_QADIC_WAVELET_SQUARE_INTEGRAL_SPECTRUM.md).
- **FFPS controls before correlated restriction:**
  [coherent tensor cost frontier](function_field/FFPS_COHERENT_TENSOR_COST_FRONTIER.md)
  and [conditioned-mask no-go](function_field/FFPS_CONDITIONED_MASK_NO_GO.md).
- **Genus-one calibration and growing rank:**
  [marked two-torsion moment tower](function_field/GENUS1_MARKED_2TORSION_MOMENT_TOWER.md),
  [finite `q`-rank phase diagram](function_field/GENUS1_QR_SYMMETRIC_POWER_PHASE_DIAGRAM.md),
  [high-rank Haar limit](function_field/ELLIPTIC_SYMMETRIC_POWER_HIGH_RANK_HAAR_LIMIT.md),
  [multi-prime collision filter](function_field/ELLIPTIC_SYM5_MULTIPRIME_COLLISION_FILTER.md),
  and [high-genus interferometer stability](function_field/USP_HIGH_GENUS_INTERFEROMETER_STABILITY.md).
- **Genus-two proof inputs and finite anatomy:**
  [third-order primitive inventory](function_field/GENUS2_THIRD_ORDER_PRIMITIVE_INVENTORY.md),
  [`Sym^10` ambient-stack trace](function_field/GENUS2_SYM10_AMBIENT_STACK_TRACE.md),
  [reciprocal-descent boundary](function_field/GENUS2_RECIPROCAL_DESCENT_BOUNDARY.md),
  [toy-minor second moment](function_field/GENUS2_TOY_MINOR_SECOND_MOMENT.md),
  [repeated-factor tomography](function_field/GENUS2_REPEATED_FACTOR_TOMOGRAPHY.md),
  [zero-geometry conditioning](function_field/GENUS2_DETECTOR_ZERO_GEOMETRY_CONDITIONING.md),
  and [rank-stable inverse design](function_field/GENUS2_RANK_STABLE_INVERSE_DESIGN.md).

Every research note introduced by this branch now appears either in a
five-minute route or in this extended index. The index is navigational; the
proof grade and claim boundary still come from the individual packet and the
release audit.

## Claim vocabulary

- **PROVED:** an exact symbolic theorem with declared quantifiers and replay.
- **PROVED FROM LOCKED SOURCES:** an exact consequence whose dependencies are
  hash-locked branch theorems or source files.
- **EXACT CONDITIONAL REDUCTION:** exact algebra that names the unresolved
  imported premises; it is not a theorem asserting those premises.
- **EXACT FINITE:** exhaustive only on the displayed finite support.
- **FORMAL MODEL:** exact inside a declared abstraction, with no automatic
  Euler-product or arithmetic-family promotion.
- **SCOUT/CONJECTURE:** an invitation to prove something, never an input to a
  later proved row.

Every JSON payload records source hashes, caps, and claim class. Optimized
Python replays are mandatory because assertions may not carry correctness.

## Exact result ledger

### Genus-two family arithmetic

| status | result | interpretation |
|---|---|---|
| **PROVED** | monic squarefree quintics modulo the lifted square-affine group give the marked-rational-Weierstrass genus-two stack, with mass `q^3` | fixes the groupoid, twist, stabilizer, and trace normalization before any cohomological interpretation |
| **PROVED** | `T_(0,3)=q^4-2q-1`, `T_(2,2)=2q^3-q^2-2q-2`, and `T_(0,4)=-(2q^2+1)` for every odd prime power | closes the formerly open triangular weight-six and weight-eight primitive channels |
| **PROVED** | the all-`q` formulas give minimal same-characteristic recurrences of orders three and four for the first two traces | this is theorem-derived spectroscopy, not interpolation across `q=3,5,7` |
| **PROVED** | marked symmetric-power traces satisfy `T2=q-1`, `T4=-3`, `T6=-4`, `T8=-Theta_(8,2)-q-6`, and `T10=(q-1)Theta_Delta-Theta_(8,2)-Theta_(10,2)-q-7` | exposes the first level-two and level-one cusp channels in a single exact ladder |
| **PROVED** | ambient traces are `-2q`, `-3q`, `1-3q-q Theta_(8,2)`, `1-4q-q Theta_(10,2)`, and `2-4q-2q Theta_Delta` for `Sym^2,...,Sym^10` | exact boundary cancellation removes the two level-two channels at `Sym^10` |
| **PROVED** | all nuisance-free filters on `r2,r4,r6,r8` form `m(1,-1,-1,1)+k(0,-4,3,0)` and have mean `-m Theta_(8,2)` | inverse design becomes a complete lattice theorem; sparse and minimum-Haar-variance filters are explicit |
| **PROVED** | all filters on `r4,r6,r8,r10` cancelling `q`, constants, and `Theta_(8,2)` form `m(1,-1,-1,1)+k(4,-3,0,0)` and leave `m((q-1)Theta_Delta-Theta_(10,2))` | isolates a mixed level-one/level-two cusp residual and supplies exact order-six prime-power recurrences |
| **PROVED** | the one-step quintic reciprocal descent closes through `Sym^10` and necessarily becomes self-referential from `Sym^12` onward | identifies a real proof-method boundary rather than extrapolating the ladder |
| **PROVED FROM LOCKED SOURCES** | `T_(12,0)=Hhat_12-2q-9-4 Theta_Delta-Theta_(8,2)-Theta_(10,2)`, while the ambient trace is `Hhat_12+2-5q-q Theta_(14,Gamma0(2))` | `Q_5=A_f^*(5)` is standard; its normalized Mobius-weighted degree-twelve aggregate `Hhat_12` is the sole remaining family-specific scalar in the locked method and is not evaluated here |
| **EXACT FINITE** | at `p=3,5,7`, `Hhat_12(p)=-p a_p(f_-)` for the Fricke-negative weight-fourteen level-two newform | a source-locked three-prime identification, not interpolation or an all-prime theorem |
| **EXACT CONDITIONAL REDUCTION** | `Hhat_12=-L*f_-+Epsilon_Eis-Genuine`; Rösner's theorem gives the endoscopic channel, and the exact project ambient identity supplies the reduction; BFG's formal nonregular branch plus predicted stable vanishing gives `Hhat_12=-L*f_-`, while Shmakov's printed branch gives `Epsilon_Eis=L` | a one-Tate Eisenstein discrepancy and the conditional `k=3` stable-space vanishing remain; finite rows force `Tr(F_p,Genuine)=p` under the Shmakov branch rather than contradicting it alone |
| **PROVED + EXACT FINITE** | the exact `Sym^10` law over `q=3,5,7` has both signs, tied-tail contributions, and named local repeated/split factor predicates | high moments require member-level rare-event accounting; those predicates are not endomorphism or endoscopy theorems |
| **PROVED** | `D=T^5+1` over `F_3` has Frobenius polynomial `X^4+9`; over `q=3^(4k)` its twists give two constructed scalar-endpoint orbits, each of density `1/(10q^3)` | total endpoint densities are at least these values; the two-orbit union contributes exactly `286^m/(5q^3)` to the normalized `m`th moment |
| **PROVED** | for every rank `r` and moment `m`, the same two orbits contribute `binom(r+3,3)^m/(5q^3)` in absolute value, with signed cancellation exactly when `rm` is odd | the constructed subtotal has an exact `(q,r,m)` critical surface; the full absolute moment has `m`th-root limit `binom(r+3,3)` at fixed `q,r` |
| **PROVED** | the toy minor has an exact all-`q` second moment and a uniform positive lower bound for the density of negative members | strengthens the original all-`q` mean theorem without creating a memberwise sign law |

### FFPS bridge and individualization geometry

| status | result | interpretation |
|---|---|---|
| **PROVED FROM LOCKED SOURCE** | the local complete-frame Gram block is `pI-J`, with sharp principal squared leverage `(p-1)/(p+1)` | coherent tensor leverages multiply and can contract like `(log x)^-2` under the exact conductor budget |
| **PROVED** | arbitrary local core variation diagonalizes in even Kummer characters but does not improve the complete-owner sharp leverage | extra rank alone is not an amplifier |
| **PROVED** | for every nonempty prime set, `G_S=tensor(pI-J)` and every normalized complex weight has energy `prod((p-1)/(p+1)) + beta*G_S^-1 beta` | uniform weights are the unique complete-frame optimum, even for signed or entangled reweighting |
| **PROVED** | for a restricted joint support `A`, the optimum is `N^2/(1_A^T G_A 1_A)`; balanced masks maximize the two-prime denominator | the `p=5,q=7` four-cell mask has leverage `18/37<1/2`, so correlated physical deletion can beat the complete-frame tensor |
| **PROVED FORMAL FAMILY** | checkerboard and cyclic-character masks have closed exact leverages; at fixed tensor depth their optimal density tends to `2^(d-1)/(2^d-1)` | a constructive restricted-Gram optimizer exists, but a varying-owner/conductor amplifier must still be proved |
| **PROVED SOURCE FIREWALL** | the raw core Legendre checker is not invariant under `P*c^2`; a quartic-character gauge repairs it inside a fixed owner quadratic sector | the soft mode is already a double-nonprincipal Kummer channel, while hard support restriction and global re-inversion remain unproved |
| **PROVED SOURCE FIREWALL** | every exact-order-`k` fixed-sector mask has a physical `2k`-root orientation, yet every leverage-improving cyclic hard mask has a strictly positive Wick residual | the all-`k` centered projector identity, not the uncentered hard inequality, is the next source-faithful analytic coordinate |
| **PROVED CONDITIONAL CLOSURE + NO-GO** | with cyclic coordinates `(C,S,R)`, the live measurements are `A=C+R`, `K=S+R`, and `P=A-K=C-S`; a target `uC+vS+wR` is controlled by scalar WCADD/WCKUM budgets exactly when `w=u+v` | the whole principal trace closes if the two still-open live estimates hold, while neither cyclic constituent does; the one-sided selected-mode upper bound `CYSEL` is the smallest extra cyclic inequality |

### Detector design, phases, and moonshots

| status | result | interpretation |
|---|---|---|
| **PROVED** | the declared low-weight genus-two mean map has determinant `3`, Smith invariants `(1,1,1,1,3)`, and trivial kernel | no nonzero detector in that five-character lattice cancels every known finite-`q` mean channel |
| **PROVED** | `R_6-2chi_(0,3)=-3B_1B_2-2B_3` has separated tensor rank exactly two | matching the five known low moments does not determine its residual mean |
| **PROVED COMPACT-HAAR** | exact interferometers select block `SU(2)xSU(2)`, doubled `SU(2)`, and `Sym^3(SU(2))`; two infinite root-resonance ladders continue the `Sym^3` selector | these are Haar-projection selectors, not pointwise subgroup or motive certificates |
| **EXACT FINITE** | the unique `q=3,5` maximin split filter reverses on held-out `q=7`; rank-stable nulling does not repair it | inverse-designed arithmetic filters require transport theorems, not attractive training histograms |
| **PROVED / FORMAL MODEL** | variance-normalized independent aggregation closes on cumulant jets with eigenvalues `2^(2-j)` | mixed-prime cumulant defects are the missing data; the model does not assert independent Euler factors |
| **PROVED** | for every odd prime power, two rational-place quadratic Euler coefficients in the squarefree-quintic family have a complete `3 x 3` joint law and mixed cumulant defects `Delta_2,...,Delta_6`; every allowed nonzero channel first appears at scale `q^-4` | the renormalization moonshot's first missing arithmetic residual is now an exact theorem; it is fixed-degree family coupling, not an independent-prime model or zero theorem |
| **PROVED** | for three distinct rational places, `sum_D chi(D(a)D(b)D(c))=3(q-2)t`, with `t` the Frobenius trace of `y^2=(a-z)(b-z)(c-z)`; the exact third-cumulant interaction splits into an elementary pair channel and this elliptic channel | the interferometry moonshot now detects a genuine geometric trace; for `q=3 mod 4` the pair channel vanishes, but the result is still a family correlation rather than a motive or zero theorem |
| **PROVED** | for every odd prime power and set of distinct rational places, the squarefree sums in every polynomial degree obey `sum_n sum_(D in H_n) psi_A(D)u^n=L(u,psi_A)(1-qu^2)/(1-u^2)^m`; at degree five the `m=1,...,5` correlations are `0`, `2q-3`, `3(q-2)t`, `q^2-10+(4q-10)t`, and `(q^2-15)t`, with exact connected cumulants through five places | the standard squarefree Euler quotient becomes a source-exact evaluation-character/curve adapter and a geometric interaction ladder; for odd `m` the monic model is `-f_A`, a nontrivial quadratic twist exactly when `-1` is nonsquare, while the even-place infinity factor is also binding; neither the genus-two middle-coefficient cancellation nor the ten complementary elliptic traces may be promoted to a local-factor or motive identity |
| **PROVED FROM LOCKED SOURCE** | the six-place raw sum is `(q^2-21)t_A+(q-6)b_A-q^2+6q-21`, its connected correction is `O(q^-7)`, and the all-`m` top-weight channel is `q^(5/2)(e_3-e_5)`, with an exact genus-four cancellation at `m=9,10` | the second Frobenius-power channel re-enters at six marks, while symplectic exterior algebra exposes a nonmonotone weight ceiling; all scales are fixed-`m` upper envelopes, not distribution or attainment claims |
| **PROVED FROM LOCKED SOURCE** | for every fixed family degree `n>=2`, the marked-place top channel is `(-1)^n q^(n/2)(e_n-e_(n-2))`; it vanishes at `m=2n-1,2n`, with exact odd/even residual expansions and connected correction `O_(n,m)(q^-n)` | mark count is an exact exterior-character spectrometer with a universal interior notch; the `n=2,m=3` connected cancellation is isolated rather than hidden in a generic asymptotic |
| **PROVED FROM LOCKED SOURCE** | for a squarefree primitive closed-place conductor of degree profile `(d_i)`, the squarefree-family kernel is `(1-qu^2)/prod_i(1-u^(2d_i))`; the same top notch depends only on total conductor degree, while lower layers are governed by the relevant truncated profile coefficients | high-degree closed places remove the `m<=q` feasibility wall; an odd-notch conductor with every `d_i>floor(n/2)` gives an exact raw-sum zero, whereas the even notch retains the split-infinity channel |
| **EXACT FINITE + PROVED ASYMPTOTIC** | the support-forced odd-notch zero count is `[x^M]prod_(d>floor(n/2))(1+x^d)^(I_q(d))`; at fixed `q` its squarefree-conditioned density is `q*C_0/((q-1)M)` with explicit parity corrections | the exact DP replays and digest-binds 237 bounded rows, independently checked by factor count, without enumerating a polynomial; `C_0=4 omega(4)` is standard rough-polynomial theory, while the detector-stratum bridge is source-locked and no converse zero classification is claimed |
| **EXACT FINITE + REFUSAL** | three-field data retain the ambiguity module `(q-3)(q-5)(q-7)Q(q)` | the inference engine refuses to name a cohomology or eigenform packet without a tower and geometric adapter |
| **PROVED** | the high-rank `SU(2)` character law has an exact cubic tail; its limiting variance exists but absolute moments of order at least three diverge, while finite-rank `2k` moments grow like `n^(2k-3)` | weak limits, rank limits, and high moments do not commute because of a thin endpoint layer |
| **PROVED** | that endpoint layer has a uniform mesoscopic tail constant `16/(9 pi^2)`, an exact fixed-`lambda` crossover profile, and hard-truncated, Winsorized, and cubic-moment coefficients | rare-event tomography now resolves the rank-scale boundary rather than merely detecting moment divergence |
| **PROVED** | a literal dyadic detector sampled on an odd-`q` norm lattice loses one cancellation order; the explicitly chosen native `q`-adic wavelet restores a double constant zero and removes the carrier | the native port is a new detector, not a silent translation of XD/HCNC/BPOE |
| **EXACT FINITE** | fixed-`q` genus-one supports stay away from Haar endpoints and a bounded multiprime filter separates all twelve frozen scalar `Sym^5` trace collisions | fixed-field moments and one-prime twins cannot be promoted to rank or compatible-system statements |

## What appears most important

1. **Highest RH relevance:** the FFPS restricted-frame mechanism. It proves
   that the earlier complete-frame no-go is not the end of the amplifier
   story, while locating the exact source-invariance and global re-inversion
   gates.
2. **Strongest standalone theorem stack:** the all-`q` genus-two marked and
   ambient trace ladder through `Sym^10`, including exact cusp-channel
   cancellation and same-characteristic recurrences.
3. **Most reusable methodological result:** high moments can be dominated by
   thin geometric strata even when the bulk law is stable; every future atlas
   packet should report bounded transforms, tails, and extreme-member
   provenance alongside raw moments.
4. **Most promising detector-design principle:** solve in the representation
   ring for exact nuisance cancellation and a named surviving arithmetic
   channel, then demand a held-out transport theorem before interpreting the
   filter geometrically.
5. **Sharpest new reconciliation target:** decide whether the nonregular
   Eisenstein coefficient is `2-5L` or the printed `2-4L`, and independently
   determine the stable `S5`-invariant at weight `(12,3)`. The exact defect
   identity prevents these two questions from being conflated.
6. **Most surprising moonshot conversion:** exact connected correlations at
   two through six marked places have successive exact/Hasse scales `q^-4`,
   `q^-7/2`, `q^-3`, `q^-5/2`, and `q^-5/2`. The apparent plateau is then
   resolved by a universal exterior-character law: in every fixed family
   degree `n`, the top channel walks through same-parity fundamental
   characters, vanishes at `m=2n-1,2n`, and returns as
   `(-1)^n chi_(omega_n)`.

## Strongest negative information

- Purity, a functional equation, and function-field RH do not give the toy
  coefficient minors a universal memberwise sign.
- Family means, even exact ones, do not individualize the principal member.
- Complete-frame FFPS weights cannot improve the coherent tensor; a gain is
  possible only after changing the physical support and therefore the Gram
  metric.
- A representative-core character is not automatically a character of the
  physical collision coordinate.
- A finite character truncation is not multiplicatively closed, and complete
  one-place marginals do not determine mixed-prime aggregation.
- Three different characteristics do not constitute a Frobenius tower.
- Three exact `Sym^12` prime rows do not separate an Eisenstein defect from a
  stable/general trace; under the printed one-Tate shift they can be absorbed
  by `Tr(F_p,Genuine)=p`.
- Compact-group selectors do not classify endomorphism or zero strata
  memberwise.
- A scalar trace collision is not equality of local factors, and a local
  factor identity is not a compatible global motive.
- The quintic reciprocal descent does not automatically extend the exact
  symmetric-power ladder beyond degree ten.

These are theorem-design constraints, not failures of the programme.

## Literature and novelty boundary

Finite-field counts for genus-two local systems and their relation to
elliptic and Siegel modular forms are established machinery; see
Faber--van der Geer, [*Sur la cohomologie des systèmes locaux...*](https://arxiv.org/abs/math/0305094),
and Bergström--Faber--van der Geer,
[*Siegel modular forms of genus 2 and level 2*](https://arxiv.org/abs/0803.0917).
Hyperelliptic Frobenius trace averages and symplectic random-matrix comparison
also have a substantial literature; see Rudnick,
[*Traces of high powers of the Frobenius class in the hyperelliptic ensemble*](https://arxiv.org/abs/0811.3649).

The branch's contribution is proof-level rather than a blanket novelty claim:
its marked `Sym^6/8/10` and ambient-ladder identities are exact for every odd
prime power, whereas the audited nonregular rows in the level-two literature
are presented through bounded point counts and conjectural identifications.
That makes the packets serious paper candidates, but it does not establish
external novelty without expert review.

For `Sym^12`, Rudnick's standard notation identifies `Q_5(f)` with the
central coefficient `A_f^*(5)` of the completed even quadratic
`L`-polynomial. The potentially distinctive object is therefore not the
middle coefficient itself, but its project-defined Mobius-weighted
degree-twelve aggregate and the exact affine reductions in which it is the
only unresolved family scalar. Those reductions were not found printed in
the audited primary sources; global novelty remains uncertified.

The follow-up source audit separates three further facts.
[Rösner's Theorem 5.13](https://sites.math.unt.edu/~schmidt/dimension_formulas/papers/2016_Dissertation_Roesner_final.pdf)
and [Shmakov's inner-cohomology calculation](https://openscholar.uga.edu/nanna/record/1979/files/dissertation.pdf)
support the
Fricke-negative endoscopic channel at nonregular weight. BFG's value
`2-5L` is nevertheless an explicitly expected nonregular Eisenstein
continuation, while Shmakov's later printed pieces total `2-4L`; the missing
copy is `[5,1] tensor L`.
[Bergström--Cléry's](https://arxiv.org/abs/2309.04388) `k=3` extension is
conditional on the BFG continuation; combining that extension with the
[official `(12,3)` table](https://smf.compositio.nl/api/Entries/2/2?j=12&k=3&l=0)
predicts the stable `S5`-invariant vanishing. The 2026 covariant construction
of [Cléry--van der Geer](https://arxiv.org/abs/2605.13300) confirms
`A_2[w]=A_2[2]/S5` but does not compute this `(12,3)` invariant. Their
[2018 coefficient tables, pp. 1139--1140](https://ems.press/content/serial-article-files/26421)
separately identify the finite scout's Fricke-negative target
`f_-(Q)=Q+64Q^2+1236Q^3+...`. The branch therefore records a one-Tate
reconciliation gate, not an accusation of error or a closed cohomology
theorem.

Likewise, Howe already records the exceptional curve `y^2=x^5+1`, its
`x^4+9` Weil polynomial, and scalar supersingular endpoint possibilities.
The endpoint packet's distinct content is the elementary reconstruction,
explicit square-affine orbit densities, twist signs, and exact contribution
to the `Sym^10` moment—not discovery of the endpoint's existence.

No novelty is claimed for cohomological spectroscopy, Weyl-character
algebra, Katz--Sarnak comparison, cumulants, or character masks in general.
The exact observables, source adapters, cancellation lattices, and restricted
Gram optimizers recorded here should be treated as candidate contributions
pending a dedicated specialist search.

## Open theorem gates

1. Prove `CYSEL`, the one-sided varying-owner/conductor upper bound for the
   selected cyclic Kummer modes, or prove that this channel cannot be
   recombined within the live FFPS source discipline. Together with the open
   WCADD/WCKUM gates this is the exact cyclic closure frontier.
2. Combine a global mixed-prime contraction theorem with a genuine
   individualization mechanism—positive domination, amplification, Fourier
   inversion with affordable loss, or rigidity of exceptional members.
3. Obtain an independent arithmetic-geometry verification of the marked and
   ambient genus-two ladder and identify precisely which alternating
   cohomology pieces realize its Tate and cusp spectra.
4. Resolve the `Sym^12` defect identity by independently determining both
   `Epsilon_Eis` and the stable `S5`-invariant `Genuine`. A second descent for
   `Hhat_12`, a direct covariant computation at `(12,3)`, or a corrected
   compact-support trace theorem would each provide a non-circular test of
   the one-Tate gate.
5. Prove an all-`q` geometric classification of the rare members dominating
   high symmetric-power moments; the present exact scalar stratum is one
   explicit component, not a full tomography theorem.
6. Port the owner/cross-core orientation of the canonical RH detector into
   the native `q`-adic experiment. The existing port proves normalization and
   finite sign behavior but not source equivalence to XD, HCNC, or BPOE.
7. Replace local collision searches with compatible multi-prime fingerprints
   enforcing determinant, conductor, root number, and prime-power recurrence.
8. Build a bounded `(q,g,r)` phase diagram using characteristic functions,
   trimmed moments, tail counts, and named special strata rather than raw
   moments alone.
9. Continue the exact multi-place connected hierarchy beyond six marks and
   determine whether its trace-dependent Hasse envelopes are sharp on
   generic, endoscopic, or exceptional configuration strata. The general
   generating identity and the universal fixed-degree exterior-character
   classification are proved; distributions and sharpness of the surviving
   character channels are not.
10. Vary closed-place conductors at fixed `q` and test whether the surviving
    exterior characters equidistribute on any rigorously specified
    conductor family. The support-forced odd-notch zero stratum is now
    counted exactly and has a Buchstab density law, but accidental zeros,
    nonzero character channels, and their geometric distribution remain
    unclassified.

## Replay and resource contract

Each packet has a prose note, an exact producer, and a focused test; stored
payload packets also carry canonical JSON. From the repository root the
common stored-payload replay pattern is:

```text
python -B research/l-families/atlas/function_field/<producer>.py --check
python -O -B research/l-families/atlas/function_field/<producer>.py --check
python -m pytest -q tests/test_<producer>.py
python -O -m pytest -q tests/test_<producer>.py
```

Use the exact producer command printed in a packet when it emits to stdout or
accepts an explicit payload path. The focused test command must still be the
printed `pytest` invocation; a zero-test `unittest` exit is not a replay. The
release audit runs all focused tests together in ordinary and optimized
Python, recomputes payload hashes, checks source blobs, runs Ruff, and
finishes with `git diff --check`.

The final bounded checkpoint covers 62 producer/test pairs and 59 stored
JSON companions. All 667 focused tests pass in ordinary and optimized
Python. All 62 producers replay in both modes: 59 use the common `--check`
form, while the renormalization-flow, guarded-inference, and genus-one phase
diagram packets use their printed alternate CLIs. Ruff and formatting pass
on the 119 non-frozen Python files. Five provenance-frozen files retain ten
pre-existing Ruff findings and are listed in the release audit rather than
silently rewritten.

Resource limits are part of the claim:

- no broad finite-field, zero, Gröbner-basis, or trace-cube sweep;
- public enumerators refuse before their declared cap (normally 4,096 source
  atoms or much less);
- symbolic and exact-rational calculations are preferred;
- optimized Python must fail closed without relying on `assert`;
- frozen atlas data are inputs and are never silently regenerated or
  reweighted.

When extending the branch, update this file first enough that a later agent
can identify the exact dependency chain, strongest negative result, replay
command, and smallest remaining theorem without reading commit history.
