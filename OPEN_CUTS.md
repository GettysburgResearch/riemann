# Open cuts

> These are explicit unproved statements. Their presence in a proof graph does not confer evidence or verification.

## Minimal arithmetic cut classes

### Fixed native detector

Prove eventual nonnegativity, an admissible fixed holomorphic correction, or subpower logarithmic negative mass for one fixed zero-safe native detector. The verified Mellin-Landau consumer then excludes off-critical zeros.

Canonical fixed options:

- rows `2` and `3`;
- the fixed scalar `5c_X(2)+3c_X(3)`;
- a fixed annular two-row detector;
- the fixed critical Taylor scalar.

### Critical one-sided variation (`CV`)

Prove subpower weighted downward variation at the critical prime-harmonic scale. This is an exact critical coordinate and is reviewed as RH-equivalent.

### Signed cross-core dispersion (`XD`)

Prove the same-kernel signed largest-prime/Vaughan cross-core estimate. The old `K0/K1` hybrid was false; only the corrected same-`K1` translation is active.

### Near collision and physical occupancy

Prove the oriented signed half-divisor near-collision estimate (`HCNC`), or prove the stronger literal physical occupancy bridge (`BPOE`) that transfers the positive phase/cubic amplitude into the native physical shell.

## Other live frontiers

- Dickman/Bellman: dynamic control of the critical finite block.
- Carry: square-root weighted signed response cancellation.
- Factor-67: `GPC67/CPSL67`.
- C4MBI: global one-sided critical four-band boundary sign.
- Actual-Xi: Pick positivity from order four onward.
- First-Hermite/heat: fixed-center signed heat or constant-four signed prime cancellation.
- Q4: `SACF` or the RH-equivalent `UOSACF`.
- Suzuki/Hardy: coefficient-one completed first-chaos domination.
- Brownian/Weil/Fredholm: a genuinely non-Bohr producer or corrected all-order arithmetic sign.

## Complete open-node inventory

| Semantic ID | Family | Status | Statement | First unsupported arrow | RH relationship |
|---|---|---|---|---|---|
| `RH` | **terminal** | `OPEN_RH_EQUIVALENT` | Riemann Hypothesis. | No reviewed-only path reaches this terminal. | terminal |
| `CONSUMER.MELLIN.MOVING_ROW_SELECTION` | **mellin_landau** | `GAP_BLOCKED` | Selecting a sufficiently large row after introducing a hypothetical zero is not a fixed detector. | Detector changes after the hypothetical zero. | invalid proof mechanism |
| `OPEN.ARITH.ROWS23_NATIVE` | **mellin_landau** | `OPEN_SUFFICIENT_FOR_RH` | The literal native source supplies the two fixed rows with eventual nonnegativity or admissible fixed holomorphic defects. | OPEN.ARITH.ROWS23_NATIVE | sufficient for RH with two-row consumer |
| `OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS` | **mellin_landau** | `OPEN_SUFFICIENT_FOR_RH` | The fixed 5:3 scalar has eventual sign or subpower logarithmic negative mass. | OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS | sufficient for RH with fixed scalar consumer |
| `OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS` | **mellin_landau** | `OPEN_SUFFICIENT_FOR_RH` | One fixed zero-safe native detector has subpower logarithmic negative mass. | OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS | sufficient for RH with Mellin API |
| `OPEN.ARITH.FCHD67` | **sharp_native** | `OPEN_SUFFICIENT_FOR_RH` | Future-completed first-owner one-sided control holds for the literal native SHARP source. | OPEN.ARITH.FCHD67 | sufficient for fixed rows and RH |
| `OPEN.ARITH.CV` | **sharp_native** | `OPEN_RH_EQUIVALENT` | Critical one-sided weighted variation is subpower for the literal fixed source. | OPEN.ARITH.CV | equivalent to RH |
| `OPEN.ARITH.XD` | **wavelet_xd** | `OPEN_RH_EQUIVALENT` | The corrected same-kernel signed cross-core dispersion has subpower negative mass/energy after carrier recombination. | OPEN.ARITH.XD | equivalent to RH in the corrected detector class |
| `OPEN.ARITH.HCNC` | **owner_vaughan** | `OPEN_SUFFICIENT_FOR_RH` | The oriented signed ratio-four off-diagonal near-collision has the required subpower one-sided bound. | OPEN.ARITH.HCNC | sufficient for the half-divisor energy and RH |
| `OPEN.ARITH.CFBB` | **conjunctive** | `OPEN_SUFFICIENT_FOR_RH` | A source-faithful subcritical 2x2 Perron matrix controls the carrier-free balanced vector packet. | OPEN.ARITH.CFBB | sufficient for RH |
| `OPEN.ARITH.BPOE` | **conjunctive** | `OPEN_SUFFICIENT_FOR_RH` | Physical observation embeds the source/phase energy into one multiplicative shell at subpower cost. | OPEN.ARITH.BPOE | sufficient through half-divisor energy to RH |
| `OPEN.OPERATOR.XI.PICK_ORDER4_PLUS` | **xi_pick** | `OPEN_RH_EQUIVALENT` | Actual-Xi infinitesimal safe Pick positivity holds for every finite packet size from four upward. | OPEN.OPERATOR.XI.PICK_ORDER4_PLUS | equivalent to RH together with reviewed criterion |
| `OPERATOR.XI.FRACTIONAL_STRING_GROWING_ORDER` | **xi_pick** | `GAP_BLOCKED` | The Xi impedance is eventually matrix monotone to a growing order. | Uniform moving-order control is absent. | invalid as stated |
| `OPEN.OPERATOR.RADIAL_CURVATURE` | **safe_line_operator** | `OPEN_RH_EQUIVALENT` | Completed-Xi radial curvature is nonnegative for every center and 0<t<1/4. | OPEN.OPERATOR.RADIAL_CURVATURE | equivalent to RH |
| `OPEN.OPERATOR.SUZUKI_FIRST_CHAOS_DOMINATION` | **suzuki_hardy** | `OPEN_RH_EQUIVALENT` | The complete positive source-side first chaos dominates the fully polarized coefficient-one output tangent, preserving all delay/orientation/bridge terms. | OPEN.OPERATOR.SUZUKI_FIRST_CHAOS_DOMINATION | equivalent to the complete delayed screw/Weil or Pick sign |
| `OPEN.HEAT.FIXED_CENTER_PHASE` | **heat_hermite** | `OPEN_SUFFICIENT_FOR_RH` | A fixed-center phase-sensitive fractional heat estimate controls the pole-bearing signed source. | OPEN.HEAT.FIXED_CENTER_PHASE | sufficient for RH |
| `OPEN.HEAT.HERMITE_CONSTANT_FOUR` | **heat_hermite** | `OPEN_RH_EQUIVALENT` | Signed prime-power cancellation holds at the First-Hermite constant-four boundary near n~(log\|x\|)^4. | OPEN.HEAT.HERMITE_CONSTANT_FOUR | equivalent to the global criterion/RH |
| `OPEN.Q4.SACF` | **q4** | `OPEN_SUFFICIENT_FOR_RH` | The absolute-polylog balanced separated coprime Type-II correlation satisfies the declared SACF bound. | OPEN.Q4.SACF | sufficient for RH; not proved equivalent in PR #580 |
| `OPEN.Q4.UOSACF` | **q4** | `OPEN_RH_EQUIVALENT` | The one-sided subpower annular coefficient estimate UOSACF holds. | OPEN.Q4.UOSACF | equivalent to RH |
| `METHODOLOGY.BROWNIAN.NEW_PRODUCER` | **brownian_weil** | `GAP_BLOCKED` | A height-dependent or genuinely non-Bohr Brownian producer is a research direction, not a theorem node. | No such producer currently exists. | methodology, not reachability |
| `OPEN.WEIL.CORRECTED_ARITHMETIC_FLOOR` | **brownian_weil** | `OPEN_RH_EQUIVALENT` | The corrected complete arithmetic kernel floor or odd half-line sign is nonnegative at all required scales. | OPEN.WEIL.CORRECTED_ARITHMETIC_FLOOR | equivalent to RH in the reviewed formulation |
| `OPEN.FREDHOLM.ALL_ORDER_PRIME_SIGN` | **brownian_weil** | `OPEN_RH_EQUIVALENT` | All-order prime-side Fredholm positivity holds in the complete capturing hierarchy. | OPEN.FREDHOLM.ALL_ORDER_PRIME_SIGN | equivalent to RH |
| `OPEN.CONJ.REGIONAL_ROW` | **conjunctive** | `OPEN_SUFFICIENT_FOR_RH` | Literal native regional row marginals satisfy the subpower Schur bound. | OPEN.CONJ.REGIONAL_ROW | premise of a conjunctive sufficient criterion |
| `OPEN.CONJ.REGIONAL_COLUMN` | **conjunctive** | `OPEN_SUFFICIENT_FOR_RH` | Compatible literal native regional column marginals satisfy the subpower Schur bound. | OPEN.CONJ.REGIONAL_COLUMN | premise of a conjunctive sufficient criterion |
| `OPEN.CONJ.QMT` | **conjunctive** | `OPEN_SUFFICIENT_FOR_RH` | The first matched-transfer arithmetic estimate holds on the common transfer. | OPEN.CONJ.QMT | premise of a conjunctive sufficient criterion |
| `OPEN.CONJ.AMT` | **conjunctive** | `OPEN_SUFFICIENT_FOR_RH` | The second matched-transfer arithmetic estimate holds on the common transfer. | OPEN.CONJ.AMT | premise of a conjunctive sufficient criterion |
| `OPEN.CONJ.SORR` | **conjunctive** | `OPEN_SUFFICIENT_FOR_RH` | Strict source-owned root return holds with contraction theta<1. | OPEN.CONJ.SORR | premise of a conjunctive sufficient criterion |
| `OPEN.CONJ.RFCP` | **conjunctive** | `OPEN_SUFFICIENT_FOR_RH` | Root-free excess packing is subpower on the same source ledger. | OPEN.CONJ.RFCP | premise of a conjunctive sufficient criterion |
| `OPEN.CONJ.PERRON_CV_ROW` | **conjunctive** | `OPEN_SUFFICIENT_FOR_RH` | The source-faithful critical-variation row of the joint Perron matrix is subcritical. | OPEN.CONJ.PERRON_CV_ROW | premise of a conjunctive sufficient criterion |
| `OPEN.CONJ.PERRON_XD_ROW` | **conjunctive** | `OPEN_SUFFICIENT_FOR_RH` | The source-faithful cross-dispersion row of the joint Perron matrix is subcritical. | OPEN.CONJ.PERRON_XD_ROW | premise of a conjunctive sufficient criterion |
| `OPEN.ARITH.CARRY_WEIGHTED_RESPONSE` | **carry_critical_hinge** | `OPEN_SUFFICIENT_FOR_RH` | Square-root weighted cancellation of the signed linear-hinge response would close the surviving critical-hinge route. | The weighted response cancellation is unproved. | open sufficient coordinate |
| `OPEN.ARITH.NATIVE_ENDPOINT_GAP` | **native_endpoint** | `OPEN_RH_EQUIVALENT` | The literal arithmetic endpoint gap F_Lambda—not merely physical P_Lambda-H packing slack—must be controlled. | Physical packing slack does not determine F_Lambda. | open RH-bearing coordinate |
| `OPEN.ARITH.FACTOR67_GPC_CPSL` | **factor67_lorenz** | `OPEN_RH_EQUIVALENT` | GPC67/CPSL67 is the critical subpower signed Type-II/Lorenz boundary for the surviving factor-67 scalar route. | The critical subpower signed boundary estimate is unproved. | open RH-equivalent coordinate |
| `OPEN.ARITH.C4MBI_BOUNDARY` | **c4mbi** | `OPEN_SUFFICIENT_FOR_RH` | The four-band one-sided critical Möbius boundary sign is the surviving C4MBI conclusion-producing estimate. | Finite campaigns and terminal sectors do not control the global boundary. | open sufficient route |
| `DIRECTMAIN.CJ.T91005` | **direct_main_cauchy_jordan** | `OPEN_RH_EQUIVALENT` | The coefficient-one normalized sixteenfold Cauchy recurrence for every carrier and scale is an exact RH-equivalent criterion. | The recurrence residual sign is itself unproved. | RH-equivalent criterion |
| `OPEN.DIRECTMAIN.CJHI` | **direct_main_cauchy_jordan** | `OPEN_RH_EQUIVALENT` | A lossless completed Cauchy–Jordan first-chaos source-to-Hardy intertwiner would close the direct-main operator route. | CJHI is not constructed. | open RH-equivalent interface |
| `DIRECTMAIN.P79.T91303` | **direct_main_p79** | `GAP_BLOCKED` | The original P79 target-flow factor-54 full proposal is blocked by the invalid finite-cell proof and missing arithmetic-row typing. | Target-exact Hall does not reproduce the native row. | purported RH proof not established |
| `DIRECTMAIN.P79.T91304` | **direct_main_p79** | `GAP_BLOCKED` | The direct Euler-row factor-54 full proposal remains gap-blocked after exact P79 corrections. | False Hall formula, false surplus, hidden-child mismatch, undefined branch weights, and missing provenance. | purported RH proof not established |
| `OPEN.DIRECTMAIN.MELLIN.ALL_ROWS` | **direct_main_mellin** | `OPEN_SUFFICIENT_FOR_RH` | Simultaneous global native positivity of every prime-sieved component row is the open producer premise in T-96000. | The global one-use prime-sieve transport is unproved. | open sufficient producer |
| `DIRECTMAIN.MELLIN.T96000` | **direct_main_mellin** | `GAP_BLOCKED` | T-96000 is a correct conditional architecture but not a proof because its simultaneous native row producer is absent. | PR #544 rejects the producer transport. | open sufficient route, not established |
| `OPEN.DIRECTMAIN.TAYLOR_CRITICAL` | **direct_main_taylor** | `OPEN_RH_EQUIVALENT` | Subpower negative mass or the critical upper-envelope estimate for the fixed Taylor scalar is the remaining RH-equivalent theorem. | The critical signed projection is uncontrolled. | open RH-equivalent criterion |

The review wave deliberately preserves multiple coordinate systems because a source-faithful conjunction may be stronger than either isolated norm. It also records where apparently different frontiers are exact aliases or RH-equivalent restatements.
