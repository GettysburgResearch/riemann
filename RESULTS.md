# Reviewed results

> **RH remains unproved.** This file lists mathematics accepted at its stated scope. It does not convert finite, local, conditional, or RH-equivalent statements into a global theorem.

## Highlights

| Family | Reviewed contribution | Boundary |
|---|---|---|
| **Mellin-Landau consumers** | Fixed rows 2 and 3, the fixed `5:3` scalar, zero-safe boxes, specialized Landau, and fixed holomorphic-defect transfer. | Consumer theorems only; the source-faithful sign/negative-mass premise is open. |
| **SHARP powers** | Every real SHARP/native boundary power `m>=2` is globally positive in the reviewed scope. | The proof is not a descent to the critical `m=1` theorem. |
| **Minimal Möbius wavelet** | The minimal ratio-eight annihilator, factor-67 antisymmetry, Abel-Mertens frame, and spectral-abscissa classification survive. | The critical energy/dispersion estimate remains RH-equivalent. |
| **Dickman/Bellman** | Exact Stieltjes transfer and hereditary positivity through a mesoscopic corridor. | The dynamic critical finite block is open. |
| **Owner/Vaughan** | Mixed-coboundary telescope, corrected large-divisor form, half-divisor square root, and exact Haar/Gram diagonal. | The signed oriented off-diagonal estimate is open. |
| **Actual-Xi Pick** | Every actual-Xi infinitesimal safe Pick matrix of size at most three is PSD after mandatory local repairs. | Order four and above remain open; distinct-node positive definiteness is not canonicalized. |
| **First-Hermite** | Broad-kernel, fixed-resolution exterior, and `(4-epsilon) log log` regions. | The constant-four signed boundary remains open. |
| **Q4** | Fourier/Haar/Jordan, annular Type-I/II, positive divisor compiler, and stable-filter barrier. | `SACF/UOSACF` remain open. |
| **Direct-main recovered results** | Cauchy/Jordan local identities, nonduplicating causal packet budget, fixed-row Mellin predecessors, activation-zero positivity, and the Euler-Taylor positive remainder ladder. | The associated full proof wrappers remain blocked or RH-equivalent. |

## Verdict counts

| Verdict | Claims |
|---|---:|
| `VERIFIED_WITH_FIXES` | 54 |
| `VERIFIED` | 23 |
| `OPEN_SUFFICIENT_FOR_RH` | 20 |
| `OPEN_RH_EQUIVALENT` | 15 |
| `REFUTED_MECHANISM` | 9 |
| `GAP_BLOCKED` | 6 |
| `CONDITIONAL_EXACT` | 6 |
| `FALSE` | 4 |
| `RETAINED_HEAVY_CERTIFICATE` | 2 |

The complete machine registry is [`canonical/2026-08-22/claims.tsv`](canonical/2026-08-22/claims.tsv). `VERIFIED_WITH_FIXES` rows may be used canonically only with the named repair. Retained heavy certificates are listed separately in [COMPUTATIONS.md](COMPUTATIONS.md).

## Mellin–Landau consumers
Canonical packet: [`research/integrated/mellin_landau/`](research/integrated/mellin_landau/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `CONSUMER.MELLIN.FIXED_ROW` | `VERIFIED_WITH_FIXES` | A fixed row has a reciprocal-zeta Mellin transform after separating initial convergence from continuation. | fixed row; initially convergent half-plane then meromorphic continuation | State z=s+1/2, finite abscissa, positive-real removability, and multiplicity. | PR #652 `24ab64551225` `claims/lemmas/L-99602-exact-two-row-mellin-landau-consumer.md` |
| `CONSUMER.MELLIN.TWO_ROW` | `VERIFIED` | Fixed rows 2 and 3 have no common numerator zero in Re z>0. | Re z>0; two fixed detectors | None | PR #652 `24ab64551225` `claims/lemmas/L-99602-exact-two-row-mellin-landau-consumer.md` |
| `CONSUMER.MELLIN.FIVE_THREE` | `VERIFIED` | The fixed scalar 5c_X(2)+3c_X(3) has numerator -3(2^-z-1)(2^-z-2), zero-free in Re z>0. | Re z>0; one fixed scalar | None | PR #649 `433fd3662f7b` `claims/lemmas/L-99261-five-three-row-zero-free-mellin-witness.md` |
| `CONSUMER.MELLIN.ANNULAR_ROWS23` | `VERIFIED_WITH_FIXES` | The fixed annular rows 2 and 3 retain reciprocal-zeta pole detection and common-zero exclusion. | fixed annular detector family | Use the corrected P_Lambda normalization and split the two source files. | PR #547 `d60f93b0e207` `claims/lemmas/L-96010-fixed-annular-row-reciprocal-zeta-mellin-transform.md\|claims/lemmas/L-96011-exact-two-row-open-strip-noncancellation.md` |
| `CONSUMER.MELLIN.ZERO_SAFE_BOX` | `VERIFIED` | A fixed logarithmic box has a multiplier zero-free in Re s>0. | one fixed width A>1 | None | PR #653 `e928fd615d75` `claims/lemmas/L-99270-zero-free-smoothing-and-negative-mass.md` |
| `CONSUMER.MELLIN.SPECIALIZED_LANDAU` | `VERIFIED_WITH_FIXES` | A nonnegative Mellin density is singular at its finite abscissa; the specialized application handles positive-real removability and multiplicities. | nonzero locally integrable density with finite abscissa | State local integrability, nonzero density, finite abscissa, and functional-equation reflection. | PR #653 `e928fd615d75` `claims/lemmas/L-99272-specialized-landau-and-scalar-firewall.md` |
| `CONSUMER.MELLIN.HOLOMORPHIC_DEFECT` | `VERIFIED_WITH_FIXES` | A fixed signed defect with Mellin transform holomorphic in Re s>0 cannot cancel a reciprocal-zeta pole. | one fixed source, row, and defect | Keep source, row, and signed defect fixed; do not relabel the defect as positive source. | PR #650 `3f9e80f09fe1` `claims/lemmas/L-99282-holomorphic-perturbation-landau-transfer.md` |
| `API.MELLIN.SUBPOWER_NEGATIVE_MASS` | `VERIFIED_WITH_FIXES` | For a fixed zero-safe detector, subpower logarithmic negative mass plus the verified consumer implies RH. | fixed detector; every epsilon>0 | Represent the arithmetic estimate as a separate open premise. | PR #653 `e928fd615d75` `claims/lemmas/L-99270-zero-free-smoothing-and-negative-mass.md\|claims/lemmas/L-99272-specialized-landau-and-scalar-firewall.md` |

## SHARP and native source
Canonical packet: [`research/integrated/sharp_native/`](research/integrated/sharp_native/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `ARITH.SHARP.COMPACT_HALL_RN` | `VERIFIED` | Compact SHARP Hall prefixes have a strict moat, and endpoint restriction is the exact Radon-Nikodym child density and projective cocycle. | finite compact prefix and 1<=W<=Z<=Y | None | PR #652 `24ab64551225` `claims/lemmas/L-99600-exact-compact-sharp-hall-and-rn-cocycle.md` |
| `ARITH.SHARP.SEQUENTIAL_FIRST_OWNER` | `VERIFIED` | The sequential first-owner decomposition preserves every native coefficient, future prime, and accumulated parity. | finite ordered prime set | None | PR #652 `24ab64551225` `claims/lemmas/L-99601-sequential-first-owner-euler-hazard.md` |
| `ARITH.SOURCE.TYPING_FIREWALLS` | `VERIFIED_WITH_FIXES` | Accumulated parity, normalized p^-1 activity, signed observation, positive source, actual response, and full capacity are distinct types. | literal physical source ledger | Include the odd-history fixture, PR #667 normalization, and live q=2 marginal separator. | PR #576 `0f6ea6eae813` `claims/refutations/R-97400-p61-source-interface-firewalls.md` |
| `ARITH.SHARP.ROW_KERNEL` | `VERIFIED_WITH_FIXES` | Each fixed component row factors through a positive SHARP kernel atom. | all fixed rows j>=2 and scales | Keep atom positivity separate from native source promotion. | PR #642 `07aa0d483845` `claims/lemmas/L-99240-sharp-target-positive-row-kernel-factorization.md` |
| `ARITH.SHARP.POWER_M_GE_2` | `VERIFIED` | Every real SHARP boundary power m>=2 is globally positive. | m>=2; all x>=1 | None | PR #663 `fa081e81044a` `claims/lemmas/L-99613-every-sharp-boundary-power-at-least-two-is-globally-positive.md` |
| `ARITH.SHARP.CRITICAL_DESCENT_IDENTITIES` | `VERIFIED` | Distributional differentiation of the quadratic SHARP object yields the linear critical detector, and critical negative mass equals weighted downward variation. | signed Radon measures on finite horizons | None | PR #668 `15719b975115` `claims/lemmas/L-99940-distributional-critical-power-descent.md\|claims/lemmas/L-99942-critical-negative-mass-is-weighted-downward-variation.md` |

## Minimal wavelet and XD
Canonical packet: [`research/integrated/wavelet_xd/`](research/integrated/wavelet_xd/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `ARITH.WAVELET.MINIMAL_RATIO8` | `VERIFIED_WITH_FIXES` | The unique minimal causal dyadic annihilator is (I-sqrt(2)S_2)(I-S_2)^2; its kernel is supported on ratio eight with a factor-67 negative copy. | causal dyadic filters and all shell scales | Use semantic/path-qualified theorem locators and explicit endpoint conventions. | PR #674 `9962f7f712ad` `standalone/2026-08-20-minimal-mobius-wavelet/PROOF.md` |
| `ARITH.WAVELET.ABEL_MERTENS` | `VERIFIED_WITH_FIXES` | The minimal ratio-eight wavelet is an exact compact Abel-Mertens frame. | all X with declared endpoint convention | State Mertens endpoint convention and kernel regularity. | PR #689 `1751b5d63d98` `claims/lemmas/L-100500-exact-abel-mertens-wavelet-frame.md` |
| `ARITH.WAVELET.SPECTRAL_ABSCISSA` | `VERIFIED_WITH_FIXES` | The weighted L2 abscissa of the compact ordinary-Mobius wavelet equals Theta+1/2. | weighted L2 half-planes; abscissa as infimum | State abscissa as an infimum; supply vertical reciprocal-zeta growth, a.e. phase, multiplicity, and nonattainment details. | PR #675 `7b28224ba1b0` `claims/lemmas/L-100131-wavelet-energy-abscissa-equals-rightmost-zero.md` |
| `ARITH.HASSE.WAVELET_REALIZATION` | `VERIFIED_WITH_FIXES` | At native p^-1 activity, signed phase-Hasse divergence realizes the minimal wavelet detector; positive edge variation is not the same object. | native p^-1 activity and signed physical divergence | Do not alias positive variation to the signed detector. | PR #692 `50c4862c801b` `claims/lemmas/L-101002-phase-hasse-is-a-wavelet-realization-not-an-independent-detector.md` |
| `ARITH.XD.SAME_K1_TRANSLATION` | `VERIFIED` | Largest-prime and Vaughan terminal forms rebuilt on the same K1 detector differ by an L1(dX/X) error. | large X; same detector K1 | None | PR #705 `027ea8bd5c87` `claims/lemmas/L-103201-correct-same-k1-largest-prime-vaughan-hybrid.md` |

## Dickman/Stieltjes/Bellman
Canonical packet: [`research/integrated/dickman_bellman/`](research/integrated/dickman_bellman/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `ARITH.DICKMAN.STIELTJES_TRANSFER` | `VERIFIED_WITH_FIXES` | The complete normalized base has an exact source-faithful Stieltjes transfer. | native rough state | State endpoint conventions and the external classical input separately. | PR #607 `a28f8e5b8c90` `claims/lemmas/L-98040-exact-stieltjes-transfer-of-the-complete-p61-base.md` |
| `ARITH.DICKMAN.MESOSCOPIC_BELLMAN` | `VERIFIED_WITH_FIXES` | The native rough state and its one-prime Bellman descendants are positive throughout the declared mesoscopic corridor on standard VK/de Bruijn input. | declared uniform mesoscopic corridor | Pin exact classical Vinogradov-Korobov/de Bruijn statements, ranges, and p^-1 normalization. | PR #608 `f362acf56bbb` `claims/theorems/T-98050-hereditary-mesoscopic-bellman-corridor.md` |

## Owner/Vaughan/half-divisor
Canonical packet: [`research/integrated/vaughan_half_divisor/`](research/integrated/vaughan_half_divisor/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `ARITH.OWNER.DOUBLE_OWNER_COBBOUNDARY` | `VERIFIED` | Least/greatest-owner blocks form an exact bi-triangular decomposition and mixed coboundary; rectangles and staircases telescope to boundary currents. | all finite ordered prime rectangles | None | PR #695 `5b549abb560e` `claims/lemmas/L-100700-double-owner-mixed-coboundary-and-rectangle-telescope.md` |
| `ARITH.CVXD.CARRIER_PRESERVATION` | `VERIFIED` | Power-sized short/long carriers cancel only after projection to the physical sum channel. | common physical source and detector | None | PR #699 `f23dd8174856` `claims/lemmas/L-101101-carrier-preserving-short-long-projection.md\|claims/lemmas/L-101102-exact-sharp-to-minimal-wavelet-derivative-bridge.md` |
| `ARITH.VAUGHAN.LARGE_DIVISOR` | `VERIFIED` | The balanced Vaughan remainder is the exact large-divisor Hankel form with corrected signs and squarefree/gcd constraints. | finite compact kernel | None | PR #696 `f4016db548af` `claims/lemmas/L-102001-balanced-vaughan-large-divisor-hankel-form.md` |
| `ARITH.VAUGHAN.HALF_DIVISOR` | `VERIFIED_WITH_FIXES` | The ratio-four packet factors through two fields and eta*eta=1 reduces them to one field with Hardy norm 3. | finite endpoint fields | Use product AB in the Cauchy gate and truncate before applying the full-line Hardy inequality. | PR #696 `f4016db548af` `claims/lemmas/L-102009-ratiofour-two-field-factorization-of-balanced-vaughan.md\|claims/lemmas/L-102010-half-divisor-symmetric-one-field-reduction.md` |
| `ARITH.VAUGHAN.HAAR_GRAM_DIAGONAL` | `VERIFIED` | The half-completed field has an exact ratio-four Haar autocorrelation Gram, and its diagonal is unconditionally subpower. | finite U<N and dyadic averages | None | PR #702 `89f995450977` `claims/lemmas/L-103100-exact-half-completed-haar-gram.md\|claims/lemmas/L-103101-diagonal-is-unconditionally-subpower.md` |

## Conjunctive APIs
Canonical packet: [`research/integrated/conjunctive/`](research/integrated/conjunctive/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `API.PERRON.ABSORPTION` | `VERIFIED` | A fixed nonnegative subcritical matrix absorbs coupled negative masses. | finite fixed channel system | None | PR #697 `e878c3717cd8` `claims/lemmas/L-101100-positive-completion-negative-mass-absorption.md` |
| `API.CONJUNCTIVE.SPARSITY_ENERGY` | `VERIFIED_WITH_FIXES` | Bad-set length and derivative energy jointly bound negative mass by a Poincare inequality. | locally absolutely continuous log-scale scalar | Do not call subpower log-length an independent key; require power-saving or deep-excursion occupancy for genuine leverage. | PR #698 `a10d6a401051` `claims/lemmas/L-101103-bad-set-sparsity-times-derivative-energy.md` |
| `API.CONJUNCTIVE.REGIONAL_SCHUR` | `VERIFIED_WITH_FIXES` | Source-owned regional row and column Schur masses pair losslessly when partitioned before observation. | finite or subpower source-owned partition | Require literal native row/column marginals and a compatible partition. | PR #698 `a10d6a401051` `claims/lemmas/L-101105-regionwise-two-sided-schur-cover.md` |
| `API.CONJUNCTIVE.MATCHED_TRANSFER` | `VERIFIED` | One common transfer gives an exact infimal negative-part decomposition. | pointwise/measurable common transfer | None | PR #704 `66f755df4321` `claims/lemmas/L-101500-matched-transfer-negative-part.md` |
| `API.CONJUNCTIVE.ROOT_EXCESS` | `VERIFIED` | Strict source-owned root return plus root-free packing controls detector negative mass. | dyadic blocks with strict theta<1 | None | PR #706 `44828a27c63b` `claims/lemmas/L-104101-two-key-root-excess-absorption.md` |
| `ARITH.STAIRCASE.VECTOR_REDUCTION` | `VERIFIED_WITH_FIXES` | The survival-weighted mixed coboundary, one common carrier-free filter, and vector Vaughan identity reduce two channels to one balanced source packet. | finite monotone staircases and identical cutoffs | Use the identical source, cutoff, and zero-safe compact filter in both coordinates. | PR #703 `0a46dba5c74e` `claims/lemmas/L-102100-survival-weighted-mixed-coboundary-and-staircase-telescope.md\|claims/lemmas/L-102103-carrier-free-filter-for-the-quadratic-wavelet-bridge.md\|claims/lemmas/L-102105-vector-vaughan-reduction.md` |
| `ARITH.PHASE.CUBIC_AMPLITUDE` | `VERIFIED` | Carrier-normalized phase homotopy, cubic B-spline autocorrelation, and half-divisor source square root close the source/phase amplitude layer. | finite labelled source and fixed compactifier | None | PR #707 `7bf3308d40ac` `claims/lemmas/L-103300-critical-carrier-normalized-balanced-homotopy.md\|claims/lemmas/L-103303-centered-cubic-bspline-autocorrelation.md\|claims/lemmas/L-103304-half-divisor-field-is-source-square-root.md` |

## Historical native-source assets
Canonical packet: [`research/integrated/native_assets/`](research/integrated/native_assets/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `ARITH.CAUSAL_PACKET_BUDGET` | `VERIFIED_WITH_FIXES` | Constant-mode first-hazard weights give an exact nonduplicating causal packet identity with total recursive child mass below 1/8. | finite ordered-prime packet | Preserve literal physical packet typing; Hall does not commute automatically with the tree. | PR #439 `706445c01d4a` `claims/lemmas/L-91355-constant-mode-hazard-weights-give-a-nonduplicating-causal-packet-budget.md` |
| `ARITH.FINITE_FARKAS` | `VERIFIED_WITH_FIXES` | Atomwise root-ledger sufficiency and the finite rational primal/Farkas alternative. | finite/local declared scope | State that the theorem is a sufficiency/fail-closed finite alternative, not feasibility of the live allocation. | PR #454 `a0409d54250b` `claims/lemmas/L-91671-atomwise-provenance-partition-is-the-exact-native-root-ledger-certificate.md` |
| `ARITH.Y4_REPAIR_CONE` | `VERIFIED_WITH_FIXES` | The Y4-zero repair LP and triangular score-free transfer are exact response-space constructions. | finite/local declared scope | Preserve the response-space/source-ownership distinction and the possible new negative lower rows. | PR #470 `89af3206ea18` `claims/lemmas/L-91687-y4-zero-columns-are-score-free-triangular-repair-directions.md` |
| `ARITH.Y4_RADIAL_NULL_GAUGE` | `VERIFIED_WITH_FIXES` | A Y4-zero detail repair is invisible to the prime-radial dictionary. | finite/local declared scope | Keep dictionary invisibility separate from source-owned feasibility and model allocation. | PR #472 `bb364396e097` `claims/lemmas/L-19881-y4-zero-repair-is-a-null-gauge-for-the-prime-radial-dictionary.md` |
| `ARITH.LIVE_MARGINAL_FARKAS` | `VERIFIED_WITH_FIXES` | The actual live Target-Lorenz marginal is one joint finite primal/Farkas problem, with feasibility open. | finite/local declared scope | State explicitly that the theorem is an exact finite reduction and that feasibility is open. | PR #521 `b4a60a54b1d7` `claims/lemmas/L-94023-the-anchored-native-interface-is-one-exact-joint-primal-farkas-problem.md` |
| `ARITH.VOLTERRA_GREEN` | `VERIFIED_WITH_FIXES` | The factor-67 endpoint inverse has an exact distributional Green formula with both boundary modes and all activation-knot atoms. | finite/local declared scope | Retain both boundary modes and every activation-knot atom; smooth-cell density alone is incomplete. | PR #638 `73ee57ccc684` `claims/lemmas/L-99230-distributional-volterra-green-formula.md` |

## Actual-Xi Pick and Loewner
Canonical packet: [`research/integrated/xi_pick/`](research/integrated/xi_pick/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `OPERATOR.BIRMAN_SCHWINGER.NORMAL_FORM` | `VERIFIED` | Negative index of H=A-G*G equals Birman-Schwinger gains above one under the stated coercive hypotheses. | A>=cI with closed bounded coupling | None | PR #438 `bb7327d21c47` `claims/lemmas/L-91900-birman-schwinger-loop-detects-every-bound-state-and-negative-direction.md` |
| `OPERATOR.XI.PICK_ORDER2` | `VERIFIED_WITH_FIXES` | Every actual-Xi infinitesimal safe Pick packet of size at most two is positive. | all safe real nodes | State centered grouping, differentiated local convergence, multiplicity, and exact external input. | PR #438 `bb7327d21c47` `claims/lemmas/L-91905-every-two-node-infinitesimal-safe-xi-pick-matrix-is-unconditionally-positive.md` |
| `OPERATOR.XI.PICK_ORDER3.DETERMINANT` | `VERIFIED` | The 3x3 Caratheodory determinant factors into reciprocal-p and tp divided-difference curvatures. | three positive safe nodes | None | PR #445 `c079c2ef2102` `claims/lemmas/L-92000-three-node-caratheodory-determinant-factors-into-two-scalar-curvatures.md` |
| `OPERATOR.XI.PICK_ORDER3.TP_CURVATURE` | `VERIFIED_WITH_FIXES` | The companion tp curvature has the required nonpositive second divided-difference sign on the safe axis. | t>1/4; grouped actual-Xi zeros | State grouped convergence and multiplicity summation. | PR #445 `c079c2ef2102` `claims/lemmas/L-92001-the-tp-curvature-of-the-actual-xi-logarithmic-derivative-is-unconditionally-negative.md` |
| `OPERATOR.XI.RECIPROCAL_CONCAVITY.SUM` | `VERIFIED` | Positive reciprocal-concave C2 functions are closed under positive sums and locally C2-convergent positive series. | positive C2 functions | None | PR #446 `880d14cb4bcb` `claims/lemmas/L-92100-reciprocal-concavity-is-closed-under-positive-sums.md` |
| `OPERATOR.XI.RECIPROCAL_CONCAVITY.ONE_ORBIT` | `VERIFIED_WITH_FIXES` | One high off-line orbit is absorbed by an explicit O(m/b^2) fraction of one low critical orbit. | t>1/4; c>r; kappa<1 | State the representative and multiplicity convention and the c>r, kappa<1 hypotheses. | PR #446 `880d14cb4bcb` `claims/lemmas/L-92101-one-high-off-line-orbit-is-absorbed-by-a-small-critical-reserve-fraction.md` |
| `OPERATOR.XI.CRITICAL_RESERVE_BUDGET` | `VERIFIED_WITH_FIXES` | The complete hypothetical off-line curvature budget uses less than one coefficient unit of a fixed verified critical orbit. | all hypothetical off-line representatives above the verified height | Correct the Platt-Trudgian bibliographic/source lock; state N(T) bound and orbit counting; do not claim the external computation was rerun. | PR #446 `880d14cb4bcb` `claims/lemmas/L-92102-the-complete-hypothetical-off-line-curvature-budget-uses-less-than-one-critical-orbit.md` |
| `OPERATOR.XI.RECIPROCAL_CONCAVITY.ACTUAL` | `VERIFIED_WITH_FIXES` | The actual-Xi reciprocal Clark coordinate is concave on t>1/4 after grouped zero-orbit assembly. | t>1/4 | Retain the residual (m0-1)R0 if the selected critical orbit has multiplicity m0; state grouped C2 convergence. | PR #446 `880d14cb4bcb` `claims/lemmas/L-92103-the-actual-xi-reciprocal-clark-coordinate-is-concave-through-order-three.md` |
| `OPERATOR.XI.PICK_ORDER3` | `VERIFIED_WITH_FIXES` | Every actual-Xi infinitesimal safe Pick matrix of size at most three is positive semidefinite. | all safe real packets of size <=3 | Replace the corrupt historical replay; repair external lock; retain residual multiplicity; state PSD canonically and omit distinct-node positive-definite strictness unless separately proved. | PR #446 `880d14cb4bcb` `claims/theorems/T-92100-all-three-node-infinitesimal-safe-xi-pick-matrices-are-unconditionally-positive.md` |
| `OPERATOR.XI.LOEWNER_LOW_ORDER` | `VERIFIED_WITH_FIXES` | Pairwise squared-pole curvature identities and the reciprocal Loewner-Hankel congruence yield the stated low-order Xi monotonicity results. | safe real axis at exact stated orders | Pin exact downstream theorem paths and alias anchor domination to the same critical-reserve ledger as PR #446. | PR #708 `eb1987502ef9` `review/2026-08-21/operator/CLAIMS.tsv` |
| `OPERATOR.XI.FRACTIONAL_STRING_FIXED_ORDER` | `VERIFIED_WITH_FIXES` | For every prescribed fixed order, fractional-string scaling and beta-Hankel high-axis asymptotics hold away from the negative cut. | each fixed order; compact sectors away from cut | Pin the exact source filenames; state derivative uniformity and normalization. | PR #708 `eb1987502ef9` `review/2026-08-21/operator/CLAIMS.tsv` |

## Safe-line transforms
Canonical packet: [`research/integrated/safe_line/`](research/integrated/safe_line/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `OPERATOR.SAFE_LINE.HAUSDORFF_PICK` | `VERIFIED_WITH_FIXES` | Safe-line normalized scalars have exact Hausdorff moment, square-root, and Stieltjes/Pick transforms; the complete positivity criterion remains RH-equivalent. | declared safe-line transform scope | Separate unconditional transforms from the RH-equivalent sign criterion. | PR #393 `ec118df8a133` `claims/lemmas/L-91001-safe-line-beta-finite-difference-kernels.md\|claims/lemmas/L-91002-safe-line-laguerre-euler-weights.md\|claims/lemmas/L-91003-safe-line-square-root-generating-transform.md\|claims/theorems/T-91001-single-safe-line-hausdorff-pick-rh-criterion.md` |
| `OPERATOR.GREEN_REMOVAL_PORTS` | `VERIFIED_WITH_FIXES` | Finite Green orders, Green-removal density, terminal-scale positivity, and the crossed critical-port dictionary survive. | declared finite orders and small/large scales | Keep the crossed hyperbolic-port exclusion open/RH-equivalent and pin the corrected threshold artifact separately. | PR #396 `a7e140614a25` `claims/lemmas/L-91023-weighted-harris-fkg-all-green-jordan-hierarchy.md\|claims/lemmas/L-91026-green-removal-is-one-explicit-boundary-density.md\|claims/lemmas/L-91027-green-removal-is-unconditionally-positive-at-terminal-scales.md\|claims/lemmas/L-91028-green-removal-is-positive-at-all-sufficiently-small-scales.md\|claims/lemmas/L-91033-horizontal-contour-crossing-selects-exactly-zeros-deeper-than-the-cauchy-scale.md\|claims/lemmas/L-91034-krein-langer-cauchy-source-critical-port-decomposition.md` |

## Suzuki/Hardy
Canonical packet: [`research/integrated/suzuki_hardy/`](research/integrated/suzuki_hardy/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `OPERATOR.SUZUKI.AMPLITUDE_EMBEDDING` | `VERIFIED_WITH_FIXES` | Suzuki's completed Jordan-Hankel operator gives the explicit amplitude-level scattering isometry. | published safe range and corrected normalization | Pin the primary source and distinguish amplitude isometry from curvature sign. | PR #400 `7dc9fec9eb5f` `claims/lemmas/L-91035-suzuki-hankel-is-the-explicit-completed-jordan-scattering-isometry.md` |
| `OPERATOR.PRIME_JULIA_ABSORPTION` | `VERIFIED_WITH_FIXES` | The local prime Julia reserve absorbs the fixed-scale long-jump channel with corrected margin 21587/38416. | declared fixed scale | Correct the printed rational margin and preserve source normalization. | PR #408 `ea3948ea21d9` `claims/theorems/T-91501-prime-julia-reserve-absorbs-the-fixed-scale-oscillatory-long-jump-channel.md` |

## Heat and First-Hermite
Canonical packet: [`research/integrated/heat_hermite/`](research/integrated/heat_hermite/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `HEAT.HERMITE.COUNTABLE_CRITERION` | `VERIFIED_WITH_FIXES` | First-Hermite nonnegativity on a countable declared test family is an exact RH criterion. | declared countable family and complete explicit formula | State normal convergence, terminal-pair completeness, and explicit-formula hypotheses; do not inherit upstream Lean status. | PR #379 `589f1c05ccaf` `research/external/anthropic-zeta23/proofs/CONFLUENT_ZERO_HEAT_MONOTONICITY.md` |
| `HEAT.HERMITE.UNCONDITIONAL_REGIONS` | `VERIFIED_WITH_FIXES` | Broad-kernel, fixed-resolution exterior, and q<=(4-epsilon)loglog(2+\|x\|) First-Hermite positivity regions hold. | each epsilon>0; sufficiently large height, with fixed-resolution/broad-kernel companion results from PR #384 | State epsilon dependence, effective-threshold scope, and normalization. | PR #385 `ea2d7c26c1fd` `research/external/anthropic-zeta23/proofs/GROWING_RESOLUTION_FIRST_HERMITE_WEDGE.md` |

## Q4
Canonical packet: [`research/integrated/q4/`](research/integrated/q4/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `Q4.CARRY_FOURIER_CORE` | `VERIFIED_WITH_FIXES` | Every finite carry field has an exact sine-transform and inverse-discrete-Laplacian energy representation. | finite carry fields | Use path-qualified semantic IDs because PR #383 reuses numerical claim IDs. | PR #383 `d764be15bd8e` `claims/lemmas/L-90411-exact-carry-fourier-inverse-laplacian.md` |
| `Q4.HAAR_FINE_SCALE` | `VERIFIED_WITH_FIXES` | The compact-Q4 carry field is an exact reflected discrete bridge; all fine Haar scales close at PIG size. | finite endpoint; Haar scales <=sqrt(N) | Do not conflate with the distinct Brownian-bridge file sharing L-90416. | PR #383 `d764be15bd8e` `claims/lemmas/L-90416-exact-bridge-haar-localization-of-pig.md` |
| `Q4.JORDAN_PERIODIZED` | `VERIFIED_WITH_FIXES` | Complete residue averaging yields the exact Jordan-2 GCD-square covariance model. | complete periodized residue ensemble | Keep the periodized ensemble distinct from the actual fixed-endpoint measure. | PR #383 `d764be15bd8e` `claims/lemmas/L-90417-complete-residue-carry-covariance-is-a-jordan2-gcd-square.md` |
| `Q4.FOURTEEN_ROW_RENEWAL` | `VERIFIED_WITH_FIXES` | The phase-locked factor-16 source has an exact fourteen-row image and corrected one-state Mobius renewal. | finite row compression | Retain the u_1 term, column-one gauge, and factor-two spectral correction. | PR #383 `d764be15bd8e` `claims/lemmas/L-90427-phase-locked-source-has-fourteen-row-carry-image.md\|claims/lemmas/L-90430-normalized-phase-filtered-mobius-renewal.md` |
| `Q4.FOURIER_GOLDBACH` | `VERIFIED_WITH_FIXES` | Q4 compact innovation energy has an exact singular cosine-antiderivative and weighted radix-four Goldbach normal form. | finite/local arithmetic normal form | Keep the source-specific low-frequency/Goldbach cancellation open and distinguish the exact norm-loss no-go. | PR #386 `66e60006bedb` `claims/lemmas/L-90703-q4-innovation-is-singular-cosine-energy-and-goldbach-correlation.md` |
| `Q4.POSITIVE_DIVISOR_COMPILER` | `VERIFIED_WITH_FIXES` | The scale-four inverse has positive coefficients and an exact coefficient-one descending divisor Markov compiler; the source-free reciprocal shortcut is false. | multiplicative source compiler | Do not infer additive critical capacity from macroscopically large positive mass. | PR #540 `d2984600a848` `claims/lemmas/L-95050-scale-four-inverse-has-a-positive-coefficient-one-divisor-compiler.md\|claims/refutations/R-95050-no-source-free-linear-transfer-from-a-log-derivative-to-its-reciprocal.md` |
| `Q4.ANNULAR.TYPE_I_II` | `VERIFIED_WITH_FIXES` | The factor-1024 safe annularization, ten exact bands, and source-preserving Type-I/II normal forms are exact. | finite annular packet and declared sectors | Pin exact kernel certificate, boundary ownership, cutoffs, and distinguish compact log support from compact Fourier support. | PR #580 `812e7fcbaff2` `claims/lemmas/L-95400-safe-triple-annularization-of-the-focc-packet.md\|claims/lemmas/L-95401-exact-band-ratio-gcd-decomposition-and-closed-sectors.md\|claims/lemmas/L-95402-type-i-ii-mellin-and-frequency-normal-forms.md` |
| `Q4.FILTER.EXHAUSTION` | `VERIFIED_WITH_FIXES` | Subpower-invertible finite filters preserve UOSACF; finite-filter weakening is exhausted. | declared endpoint spaces and subpower-invertible filters | State exact normalization, endpoint spaces, and inverse costs. | PR #606 `327c0967c67e` `claims/lemmas/L-95601-subpower-invertible-filters-preserve-the-q4-criterion.md` |
| `Q4.FILTER.CRITICAL_ZERO_BARRIER` | `VERIFIED` | Boundary moments can be added at polylogarithmic cost, but an extra zero at z=1/2 forces power-sized inverse cost. | finite dyadic filters | State the finite-filter/inverse-cost class exactly. | PR #600 `193ca24d4ebe` `claims/lemmas/L-95520-safe-zero-moment-tower-for-q4.md\|claims/refutations/R-95520-polylog-stable-filters-cannot-add-safe-line-zero.md` |

## Review infrastructure
Canonical packet: [`integration/2026-08-22/review-locks/`](integration/2026-08-22/review-locks/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `REVIEW.C.FINAL_COVERAGE` | `VERIFIED` | Reviewer C assigns a disposition to every PR #375–#707, completes 171-issue archaeology, leaves zero targeted-review rows, and records only sequence #417 as having no remote PR object. | PRs 375–707 and 171 issue records | None | PR #712 `a6aa936ba8bf` `review/2026-08-22/coverage/FINAL_REPORT.md\|review/2026-08-22/coverage/PR_CENSUS.tsv\|review/2026-08-22/coverage/ISSUE_CENSUS.tsv` |
| `REVIEW.C.ISSUE_ARCHAEOLOGY` | `VERIFIED` | Reviewer C classifies 171 historical issues and extracts only issue material corroborated by repository claims, reviews, or exact artifacts. | repository issue history through the frozen review range | None | PR #712 `a6aa936ba8bf` `review/2026-08-22/coverage/ISSUE_CENSUS.tsv\|review/2026-08-22/coverage/ISSUE_GENEALOGY.md` |
| `REVIEW.B.DIRECT_MAIN_CENSUS` | `VERIFIED` | The 85 commits directly deposited on main after the August 11 reviewed state are partitioned into 11 contiguous packets with no unclassified commit. | a88bed9..6772039, base exclusive | None | PR #717 `dad61b954dd8` `review/2026-08-22/direct-main/COMMIT_PACKETS.tsv\|review/2026-08-22/direct-main/REPORT.md` |

## Carry critical hinge
Canonical packet: [`research/integrated/carry_hinge/`](research/integrated/carry_hinge/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `ARITH.CARRY.FACTOR64_PAYMENT` | `VERIFIED_WITH_FIXES` | Factor-64 reward prefixes pay every monotone occupation; the actual critical occupation is not monotone. | finite factor-64 occupation prefixes | Separate the finite monotone-payment theorem from the nonmonotone critical occupation. | PR #381 `8b32a5941a34` `claims/lemmas/L-90701-factor64-reward-prefixes-pay-every-monotone-occupation.md\|claims/refutations/R-90702-critical-uniform-pascal-occupation-is-not-monotone.md` |

## Direct-main Cauchy/Jordan
Canonical packet: [`research/integrated/direct_main/cauchy_jordan/`](research/integrated/direct_main/cauchy_jordan/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `DIRECTMAIN.CJ.LOCAL_IDENTITIES` | `VERIFIED_WITH_FIXES` | The direct-main Cauchy/Jordan series contains exact positive-source, scattering, finite-jet, rational-storage, Hardy-factor, and compound-Poisson identities. | safe lines and finite carrier packets | Pin domains, meromorphic exceptions, and one Fourier/Hardy orientation. | PR #MAIN `677203992eb0` `claims/lemmas/L-91014-generalized-jordan-cocycle-divisor-isometry.md\|claims/lemmas/L-91019-positive-anchor-second-jet-anova-closure.md\|claims/lemmas/L-91022-sixteenfold-cauchy-detail-storage-and-three-square-residual.md\|claims/lemmas/L-91029-positive-jordan-channel-is-a-compound-poisson-prime-semigroup.md` |

## Direct-main P79
Canonical packet: [`research/integrated/direct_main/p79/`](research/integrated/direct_main/p79/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `DIRECTMAIN.P79.SPLIT_IDENTITIES` | `VERIFIED_WITH_FIXES` | The exact P79 one-prime Euler row, target, score, and first-moment split identities survive after removing false sign and typing conclusions. | finite one-prime P79 rows | Delete the false uniform surplus and positive typed-splice claims. | PR #MAIN `677203992eb0` `claims/lemmas/L-91351-p79-one-prime-splice-is-a-terminal-child-plus-positive-arithmetic-row.md` |
| `DIRECTMAIN.P79.L91355` | `VERIFIED_WITH_FIXES` | Constant-mode first-hazard weights give an exact nonduplicating packet identity with total canonical child coefficient below 1/8. | finite ordered rough-prime lists | State packet-typing hypotheses explicitly. | PR #MAIN `677203992eb0` `claims/lemmas/L-91355-constant-mode-hazard-weights-give-a-nonduplicating-causal-packet-budget.md` |

## Direct-main Mellin
Canonical packet: [`research/integrated/direct_main/mellin/`](research/integrated/direct_main/mellin/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `DIRECTMAIN.MELLIN.L96000` | `VERIFIED_WITH_FIXES` | Every fixed component row has an explicit reciprocal-zeta Mellin transform. | fixed j>=2; initial half-plane then continuation | Separate convergence, continuation, and producer positivity. | PR #MAIN `677203992eb0` `claims/lemmas/L-96000-fixed-row-mellin-transform-of-the-full-mobius-spline.md` |
| `DIRECTMAIN.MELLIN.L96001` | `VERIFIED_WITH_FIXES` | At any open-strip zero every sufficiently large row numerator is nonzero. | each zero; all sufficiently large fixed rows | State the all-row producer quantifier; prefer fixed rows 2,3 or fixed 5:3 canonically. | PR #MAIN `677203992eb0` `claims/lemmas/L-96001-the-row-kernels-cannot-cancel-an-open-strip-zero.md` |

## Direct-main critical Taylor
Canonical packet: [`research/integrated/direct_main/taylor/`](research/integrated/direct_main/taylor/)
| Claim | Verdict | Reviewed statement | Scope | Required fix | Source |
|---|---|---|---|---|---|
| `DIRECTMAIN.TAYLOR.L99930` | `VERIFIED_WITH_FIXES` | Activation-zero native powers are globally positive for every real m>=2. | X>=1; real m>=2 | Keep activation-zero and ordinary SHARP objects distinct. | PR #MAIN `677203992eb0` `claims/lemmas/L-99930-activation-zero-supercritical-positivity.md` |
| `DIRECTMAIN.TAYLOR.L99931` | `VERIFIED_WITH_FIXES` | Every Euler–Taylor remainder with effective prime exponent at least 3/2 is positive. | integer m>=3; 1<=k<=m-2 | State absolute convergence and labelled-67 multiplicity. | PR #MAIN `677203992eb0` `claims/lemmas/L-99931-euler-taylor-positive-remainder-ladder.md` |
| `DIRECTMAIN.TAYLOR.L99932_KERNEL` | `VERIFIED_WITH_FIXES` | The first uncontrolled Taylor remainder is an explicit positive kernel whose native Möbius projection has a zero-safe reciprocal-zeta Mellin transform. | one fixed m>=2 | Pin the reviewed Mellin–Landau hypotheses. | PR #MAIN `677203992eb0` `claims/lemmas/L-99932-critical-renormalized-kernel-and-zero-safe-consumer.md` |

