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
7. [cyclic source-realization and Wick gate](function_field/FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md).

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
6. the [`Sym^10` rare-event law](function_field/GENUS2_SYM10_RARE_EVENT_TOMOGRAPHY.md)
   and [scalar endpoint realization](function_field/GENUS2_SYM10_SCALAR_ENDPOINT_REALIZATION.md);
7. the [all-rank scalar-endpoint phase diagram](function_field/GENUS2_SCALAR_ENDPOINT_SYMMETRIC_POWER_PHASE_DIAGRAM.md).

The exact all-odd-prime-power trace ladder is the main object. It separates
Tate, elliptic level-two, and level-one cusp channels and supplies exact
same-characteristic recurrences. The scalar endpoint packet then exhibits a
named rare geometric stratum whose normalized high moments have an explicit
contribution. The all-rank continuation proves the exact crossover surface
`m log binom(r+3,3) = 3 log q + log 5` for that constructed subtotal and a
full-family fixed-`(q,r)` spectral-radius limit, without claiming an
asymptotic for the remaining family.

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
4. [guarded cohomology inference](function_field/GUARDED_COHOMOLOGY_CONJECTURE_INFERENCE.md)
   followed by the exact [same-characteristic spectroscopy](function_field/GENUS2_EXACT_FROBENIUS_TOWER_SPECTROSCOPY.md);
5. the [high-rank Haar boundary-layer tomography](function_field/HIGH_RANK_HAAR_BOUNDARY_LAYER_TOMOGRAPHY.md).

These packets show both sides of inverse design. Exact character algebra can
remove declared nuisance channels and isolate a named residual, but a filter
optimized on `q=3,5` can reverse on untouched `q=7`. Likewise, three fields
cannot name a Frobenius spectrum, whereas an all-`q` theorem supplies genuine
same-characteristic towers and exact minimal recurrences.

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

### Detector design, phases, and moonshots

| status | result | interpretation |
|---|---|---|
| **PROVED** | the declared low-weight genus-two mean map has determinant `3`, Smith invariants `(1,1,1,1,3)`, and trivial kernel | no nonzero detector in that five-character lattice cancels every known finite-`q` mean channel |
| **PROVED** | `R_6-2chi_(0,3)=-3B_1B_2-2B_3` has separated tensor rank exactly two | matching the five known low moments does not determine its residual mean |
| **PROVED COMPACT-HAAR** | exact interferometers select block `SU(2)xSU(2)`, doubled `SU(2)`, and `Sym^3(SU(2))`; two infinite root-resonance ladders continue the `Sym^3` selector | these are Haar-projection selectors, not pointwise subgroup or motive certificates |
| **EXACT FINITE** | the unique `q=3,5` maximin split filter reverses on held-out `q=7`; rank-stable nulling does not repair it | inverse-designed arithmetic filters require transport theorems, not attractive training histograms |
| **PROVED / FORMAL MODEL** | variance-normalized independent aggregation closes on cumulant jets with eigenvalues `2^(2-j)` | mixed-prime cumulant defects are the missing data; the model does not assert independent Euler factors |
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

1. Prove a varying-owner/conductor estimate for the all-`k` centered cyclic
   projector identity, or prove that its rotated conditioned currents cannot
   be recombined within the live FFPS source discipline.
2. Combine a global mixed-prime contraction theorem with a genuine
   individualization mechanism—positive domination, amplification, Fourier
   inversion with affordable loss, or rigidity of exceptional members.
3. Obtain an independent arithmetic-geometry verification of the marked and
   ambient genus-two ladder and identify precisely which alternating
   cohomology pieces realize its Tate and cusp spectra.
4. Go beyond `Sym^10` using a new arithmetic inventory rather than the now
   self-referential one-step reciprocal descent.
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

## Replay and resource contract

Each packet has a prose note, canonical JSON payload, exact producer, and
focused test. From the repository root the common replay pattern is:

```text
python -B research/l-families/atlas/function_field/<producer>.py --check
python -O -B research/l-families/atlas/function_field/<producer>.py --check
python -m unittest tests.test_<producer> -v
python -O -m unittest tests.test_<producer> -v
```

Use the exact command printed in a packet when its CLI also accepts an
explicit payload path. The release audit runs all focused tests together in
ordinary and optimized Python, recomputes payload hashes, checks source blobs,
runs Ruff, and finishes with `git diff --check`.

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
