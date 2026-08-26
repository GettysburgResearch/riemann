# PR #757 release audit

Status: **release-candidate audit; current replay green; exploratory PR, not
an integrated proof packet; RH and GRH remain open**

Frozen parent: PR #756 at
`6e4609dfe1b073f1eb58445fdd1d7164dbc450d6`.

Audited mathematical-packet head:
`cf7b10ef5e50693b9150996e3891da8debb6b180`. The final PR head is recorded in
the PR body because a tracked file cannot contain the SHA of the commit which
creates that SHA.

## 1. Release decision

The branch is suitable for a draft exploratory release. It is not suitable
for canonical integration as one object.
Its strongest claims belong to four separately reviewable lanes:

1. complete beta, fixed mollification, and native reflection;
2. physical hard masks, relative projectors, and conductor budgets;
3. closed-place notch boundary theorems;
4. genus-two `Sym^12` arithmetic/cohomological comparison.

No lane proves RH, GRH, a varying-conductor `CYSEL` estimate, or an all-`q`
`Sym^12` Galois correction.

## 2. Claim-grade matrix

| Object | Grade | Audited conclusion | Load-bearing limitation |
|---|---|---|---|
| extra-notched Mellin consumer | exact conditional analysis | off-line zeros create zero-safe poles | original raw premise is refuted and arithmetically vacuous |
| complete beta atomic firewall | exact theorem | raw negative variation is `Omega(sqrt(Y))` with explicit comparator | says nothing negative about the fixed-mollified density |
| fixed-mollified beta criterion | exact equivalence | one-sided negative mass, two-sided mass, and RH are equivalent | the estimate itself is not proved |
| compact boundary primitive | exact identity and equivalence | `h_epsilon=(I-tau_epsilon)G/epsilon`; signed mass is one terminal shell; one-sided mass of `G` is RH-equivalent | the telescope does not control Jordan mass |
| boundary near-correlation | exact positive Gram identity and equivalence | prefix `L2` energy uses only beta pairs with ratio in `[1/16,16]`; its off-diagonal is RH-equivalent | no subpower correlation estimate is proved |
| native reflection/geodesic criterion | exact source identity and equivalence | same detector is a differentiated reflection-odd energy; relative squared endpoint costs `O(T)` | positive reflection estimate remains RH-bearing |
| finite beta scout | bounded floating point | checkpoint values and two-mesh controls are reproducible | no interval certificate or asymptotic inference |
| compact boundary-field scout | bounded floating point plus exact first-difference control | `G` rows reproduce; direct differencing agrees with `h_epsilon` to `2.13e-13` absolute | no asymptotic inference |
| mask Pareto frontier | exact finite Fourier/Gram algebra | leverage and selected leakage share one sharp parameter | fixed support gain is not individualization |
| Kummer invariant audit | exact fixed-fibre geometry | generic invariant criterion and resonant strata identified | no varying-place complex or uniform Betti bound |
| cyclic/abelian torsor projector | exact endomorphism theorem | `C-S=Pi_0`; subgroup quotients compress selected rank | actual FFPS cleanup must be common and equivariant |
| rich-core and closed-place towers | exact source algebra plus ambient counting | formal leverage `<(4/5)^r` on declared rich sources | weighted Boolean transfer is open |
| entropy/conductor phase diagram | exact ambient theorem; conditional loss model | threshold `theta<delta log(5/4)` | typical ambient order statistics do not imply a weighted-source theorem |
| exact cycle-selector mass | exact characteristic-zero representation theorem | every exact full-`S_d` presentation has forced mass `2^(d-1)/d`; product costs multiply | weaker/source-specific selectors and joint geometric cancellation remain open |
| derangement-relaxed selector | **exact finite**, `2<=d<=10` | fixed-point vanishing still has optimum `2^(d-1)/d`, uniquely at the exact cycle indicator | all-`d` optimality is conjectural; no asymptotic or native-source lower bound |
| first notch boundary | exact all-odd-`q` theorem | no first-boundary zeros for `n>=4` | deeper profiles remain |
| second notch boundary | exact reduction and fixed-`q` asymptotic using standard prime-polynomial AP input | density begins at `M^-2`, with exact `M^-3` term | detector zeros only; no individual L-function zero |
| third notch boundary | exact reduction and fixed-`q` asymptotic using the same standard input | density begins at `M^-2`; `D_5+D_3` first enters at `M^-3` | growing-depth aggregate remains open |
| all fixed notch depths | exact residual/profile algebra and fixed-`q,j` asymptotic using the standard fixed-modulus prime-polynomial progression theorem | every fixed depth has a closed `M^-2/M^-3` law and is `O(M^-2)` | stable range and `O_(q,j)(M^-4)` remainder are not growing-`j` uniform |
| local delta-tower anti-concentration | exact all-odd-`q` probability bound | `delta_(j,s,q)=O_q(sqrt(j)q^-j)` uniformly in `s`; displayed `M^-2/M^-3` coefficient towers are absolutely summable | does not justify summing conductor layers or complementary growing-depth profiles |
| full rational aperture | exact all-odd-`q` theorem | supersingular auxiliary curve forces every odd full-place correlation to vanish | not a varying-closed-place FFPS estimate |
| `Sym^12` stable channel | exact semisimplified representation result | `G=0` | does not decide Eisenstein Galois realization |
| `Sym^12` master contradiction | exact source-relative rows at `p=3,5,7` | Shmakov displayed branch differs by `-p`; unique formal repair is `[5,1] tensor L` | three rows do not prove an all-`q` cohomological identity |

## 3. Independent audit ledger

### Mollified beta and reflection

- `9f29bdb6e` established the fixed-mollified RH equivalence.
- `a678292fd` independently audited the beta/Landau/BV/kernel/source chain,
  strengthened the exact native reflection criterion, and passed normal and
  optimized replay.
- `78e5ce8e7` independently audited the complete atomic coefficients,
  `2`-adic grouping, collision-free horizon, and explicit square-root lower
  comparator.
- `928cf3f3d` independently audited the finite scout's kernel formula, beta
  source, causal truncation, raw comparator, grid semantics, resource caps,
  and numerical claims. Published numerical values were unchanged.
- `c6971721d` proved that the mollified detector is a first difference of a
  compact-BV boundary primitive, established the box-free one-sided RH
  criterion and exact odd-fibre compression, and supplied a countermodel to
  any formal Jordan telescope. Commit `9e19e2761` applies repository-standard
  formatting only; replay remains unchanged.
- `5eb7add32` independently audited the compact boundary-field scout,
  corrected one fit-range guard, and reproduced the direct first-difference
  comparison to `2.13e-13` absolute and `1.05e-15` relative error.
- `5948711a9` independently audited and committed the prefix-energy theorem:
  the Gram shift, ratio-16 support, BV/RH implications, exceptional Euler
  factor, logarithmic diagonal, and off-diagonal equivalence all replay.

### Selector and notch extensions

- `691166b8c` proved the unique hook expansion and forced rank mass of the
  exact cycle selector. A second agent independently rederived every
  coefficient, parity rank, and product rule and found the scope fences
  clean.
- `961603fd0` contains the first third-boundary packet snapshot together with
  the scoped selector-successor update; `d13dfcfcb` contains only the final
  third-boundary precision corrections. Normal/optimized replay, 11 packet
  tests in both modes, 51 neighboring tests, and an independent audit pass.
- `d61323f8c` proves the all-fixed-depth residual and density theorem. Its
  `j=1,2` specializations reproduce both predecessor packets exactly; 12
  packet tests in both modes, 71 related tests, and an independent audit pass.
- `6d9e66033` solves the derangement-supported weighted-`L1` relaxation
  exactly for `2<=d<=10`. Rational primal-dual certificates prove the same
  optimum and unique cycle-indicator minimizer; the packet explicitly leaves
  all-`d` optimality conjectural. Normal/optimized replay, six packet tests in
  both modes, Ruff, and source-lock checks pass.
- `cf7b10ef5` proves uniform local delta-tower anti-concentration and absolute
  summability of the displayed fixed-depth coefficient towers. The packet,
  ten tests in both modes, an 81-test related suite, Ruff, source locks, and an
  independent final audit all pass. It expressly retains the growing-depth
  remainder and stable-range fence.

### Genus-two `Sym^12`

- `4a27bc2f9` fenced the finite scout's central quantities as inventory-
  derived rather than independently enumerated.
- `db57a442b` exposed the contradiction directly in the raw `T_(12,0)` rows.
- `f26a9b869` independently replayed the stack normalization, arithmetic
  inventory, ordered boundary, ambient identity, stable zero, and exact
  three-row residual.
- `482e32c53`, `c463d4896`, `20abcc478`, and `823f38594` normalized one
  line-ending-dependent byte ledger and cascaded all source locks. The
  mathematical payload did not change; all four producers and 30 tests pass
  normally and under `-O`.

### Remaining lanes

The hard-mask, closed-place, and notch packets each contain source locks,
canonical JSON, bounded exact producers, and focused tests. They remain
exploratory review objects rather than independently integrated theorems. The
release front door labels imported prime-polynomial and cohomological inputs
explicitly.

## 4. Critical mathematical checks

The following implications were checked rather than inferred from matching
JSON:

1. `K_ext` is a compact finite signed measure and its multiplier is nonzero
   in `0<Re(s)<1/2`.
2. The box multiplier is nonzero in `Re(s)>0`; an off-line zeta zero therefore
   survives fixed mollification.
3. Under RH, normalized beta partial sums are subpower and compact-BV
   summation gives the mollified `L1` bound.
4. Conversely, one-sided mass plus Landau's theorem gives holomorphy in the
   open right half-plane and excludes off-line zeros.
5. The complete atomic lower bound groups all possible dyadic collisions
   before applying Jordan decomposition.
6. Prefix `L2` energy agrees with the complete causal field below its
   logarithmic horizon; its compact autocorrelation has ratio support 16 and
   only a logarithmic diagonal.
7. The reflection identity uses a causal finite-`L2` fence; it does not assume
   the complete native field lies in global `L2`.
8. The ternary Kummer construction is not misrepresented as one sheaf in two
   different characteristics; its common-base control is separate.
9. The relative projector is an endomorphism identity, not a virtual object
   with fractional multiplicity.
10. The closed-place supply theorem is ambient; the weighted-source transfer
    firewall remains visible.
11. Exact root-incidence cancellation does not make the `d`-cycle selector
    cheap: orthogonality forces its hook coefficients and exponential mass.
12. Through `d=10`, allowing arbitrary non-cycle derangement values does not
    lower that mass; exact strict dual slack makes the cycle indicator the
    unique minimizer. No all-`d` conclusion is inferred.
13. Conditioning on lower-degree signs isolates a coefficient-one top-degree
    Rademacher sum in every local delta channel; central-binomial
    anti-concentration is therefore uniform in the channel index.
14. The `Sym^12` finite rows are raw-`T` plus locked inventory, not an
    independent enumeration of `Hhat_12`.

## 5. Final replay set

Run every command both normally and with `python -B -O` where shown. These
are deliberately focused; the branch avoids a machine-heavy global sweep.

```text
python -B research/l-families/atlas/function_field/ffps_complete_beta_atomic_variation_firewall.py --check
python -B research/l-families/atlas/function_field/ffps_mollified_beta_rh_equivalence.py --check
python -B research/l-families/atlas/function_field/ffps_mollified_beta_boundary_shell_identity.py --check
python -B research/l-families/atlas/function_field/ffps_mollified_geodesic_rh_criterion.py --check
python -B research/l-families/atlas/function_field/ffps_mollified_beta_finite_scout.py --check
python -B research/l-families/atlas/function_field/ffps_boundary_field_finite_scout.py --check
python -B research/l-families/atlas/function_field/ffps_boundary_field_near_correlation_criterion.py --check
python -B research/l-families/atlas/function_field/ffps_exact_cycle_selector_mass_no_go.py --check
python -B research/l-families/atlas/function_field/ffps_derangement_selector_finite_l1_optimization.py --check
python -B research/l-families/atlas/function_field/quadratic_family_third_boundary_trace_zero_density.py --check
python -B research/l-families/atlas/function_field/quadratic_family_fixed_depth_trace_zero_density.py --check
python -B research/l-families/atlas/function_field/quadratic_family_local_delta_tower_anticoncentration.py --check
python -B research/l-families/atlas/function_field/genus2_sym12_arithmetic_inventory.py --check
python -B research/l-families/atlas/function_field/genus2_sym12_finite_cusp_trace_scout.py --check
python -B research/l-families/atlas/function_field/genus2_sym12_conditional_endoscopic_closure.py --check
python -B research/l-families/atlas/function_field/genus2_sym12_master_adapter_contradiction_audit.py --check
```

Focused normal/optimized test modules:

```text
tests.test_ffps_complete_beta_atomic_variation_firewall
tests.test_ffps_extra_notched_mellin_landau_consumer
tests.test_ffps_mollified_beta_rh_equivalence
tests.test_ffps_mollified_beta_boundary_shell_identity
tests.test_ffps_mollified_geodesic_rh_criterion
tests.test_ffps_mollified_beta_finite_scout
tests.test_ffps_boundary_field_finite_scout
tests.test_ffps_boundary_field_near_correlation_criterion
tests.test_ffps_exact_cycle_selector_mass_no_go
tests.test_ffps_derangement_selector_finite_l1_optimization
tests.test_genus2_sym12_arithmetic_inventory
tests.test_genus2_sym12_finite_cusp_trace_scout
tests.test_genus2_sym12_conditional_endoscopic_closure
tests.test_genus2_sym12_master_adapter_contradiction_audit
tests.test_quadratic_family_first_boundary_trace_zero_density
tests.test_quadratic_family_second_boundary_trace_zero_reduction
tests.test_quadratic_family_second_boundary_zero_density
tests.test_quadratic_family_second_boundary_zero_density_third_order
tests.test_quadratic_family_third_boundary_trace_zero_density
tests.test_quadratic_family_fixed_depth_trace_zero_density
tests.test_quadratic_family_local_delta_tower_anticoncentration
tests.test_quadratic_family_full_rational_place_notch
tests.test_ffps_cyclic_torsor_relative_projector
tests.test_ffps_finite_abelian_subgroup_mask_compression
tests.test_function_field_block_entropy_conductor_phase_diagram
```

At the audited head, all 16 listed producers passed normally and under `-O`;
the focused set passed 182 tests in each mode; and all 59 branch-added test
modules passed 364 tests in each mode. Ruff check passed over all 125 changed
Python files. Ruff 0.16.1 format-check passed on 113; twelve older source-
locked files have formatter-version-only drift and were deliberately not
rewritten, avoiding a meaningless hash cascade. The two new theorem packets
are among the 113 clean files. Local Markdown references from all six front
doors and `git diff --check` also passed.

## 6. Computation boundary

This successor intentionally avoids a broad enumeration. The proof packets
use exact integer, rational, cyclotomic, representation-ring, or symbolic
coefficient arithmetic under explicit caps. The two coupled floating-point
scouts:

- stop at `262,144` beta coefficients;
- use two meshes of 256 and 512 cells per doubling;
- enumerate no field, curve, conductor family, or L-function zero;
- use only three bounded source passes in the boundary-field replay;
- complete in a few seconds on the development machine; and
- are labelled finite scouts throughout.

The notch packets enumerate degree profiles or finite Rademacher sums, not
polynomials or finite-field elements. The `Sym^12` audit replays three locked
rows and exact source formulas; it does not enumerate another family.

## 7. Known failure and open-gate ledger

Refuted:

- raw complete-current Jordan negative mass is subpower;
- soft character weighting reproduces the hard-mask gain;
- complete-frame positive orthogonal assembly has hidden leverage;
- ambient rich-core density automatically transfers to the weighted source;
- a formal associated-graded Tate ledger alone proves the actual `Sym^12`
  Galois Euler class.
- an alternative exact full-`S_d` semisimple presentation can make the
  universal `d`-cycle selector cheaper than `2^(d-1)/d`.

Open and load-bearing:

- fixed-mollified/native-reflection one-sided subpower mass;
- compact-boundary-field one-sided subpower mass, an equivalent formulation;
- compact-ratio off-diagonal beta correlation, another equivalent formulation;
- global varying-place relative complex and signed trace cancellation;
- a weaker/source-specific or jointly cancelled closed-place selector;
- weighted Boolean/owner rich-core transfer;
- any positive-average-to-principal domination route not using the exact
  signed identities;
- actual Galois realization of the `Sym^12` one-Tate carrier;
- growing-depth profile counting, stable-range control, and a uniform
  `O_(q,j)(M^-4)` remainder; local delta-tower decay is now proved;
- external novelty and priority review.

## 8. Extraction recommendation

Do not merge the entire branch into an integrated theorem packet. Freeze it
as one exploratory PR, then extract four review tracks matching Section 1.
The beta/reflection track needs analytic-number-theory review; the mask track
needs a sheaf/source specialist; the notch track needs function-field
combinatorics review; and the `Sym^12` track needs a genus-two/cohomology
specialist.
