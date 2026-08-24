# Phase-0 L-function detector atlas

Status: **exact finite exploration, exact synthetic algebra, and source-qualified discovery data**.

Scope: one small GL(1)/GL(2) local-Euler corpus; complete monic squarefree
cubic regressions over `F_q[T]` for `q=3,5,7,11,13`, including the original
100-member `F_5[T]` pilot; the complete genus-two quintic families over
`F_3[T]`, `F_5[T]`, and `F_7[T]` (162, 2,500, and 14,406 members); exact
rational central-deflation controls; one five-object classical reciprocal-
coefficient filter through `n<=256`; and conductor-coprime quadratic-character
covariance packets for `11.a2`, both pooled and split by the sourced twist root
number. An exact `USp(4)` comparator and proof-backed all-odd-prime-power
coefficient moments, negative-sign density floor, second-moment proof roadmap,
and twelve-moment polynomial sign bound accompany the genus-two scans. Exact
affine-family measures, an all-degree affine Burnside generating series, an
all-odd-`q` elliptic-stack moment theorem, a cross-rank symplectic
reclassification, an independently enumerated balanced-control scan,
Frobenius-power echo laws, a bounded tail-geometry packet, an exact
product-variety tensor family, and an exact `USp(4)` virtual-character
null-direction packet are also included. Every atlas record is `DRAFT`. RH
and GRH remain open.

Exact sources or dependencies: classical completed GL(1) normalizations; the
displayed finite-field definitions; the standard level-one modular-stack
trace identity used by the genus-one all-weight theorem; LMFDB object
identifiers and dynamic
metadata for three elliptic-curve discovery rows; Rohrlich's and Conrey's
quadratic-twist sign formulas; the function-field even-character coefficient
identity cited in the genus-two proof; CPython 3.12.10 standard library; and the
exact repository packets named inside detector contracts.

What was actually run: five finite local-Euler evaluations through `p<=43`;
4,023 candidate cubics across `q=3,5,7,11,13`; all three complete genus-two
families above; exact `F_q/F_{q^2}` character reconstruction for the three
genus-two packets, including an independent 20,175-candidate balanced-control
replay with raw-sum provenance; twelve exact `USp(4)` Haar
moments and degree-six and degree-twelve sign majorants by bounded
Laurent-polynomial arithmetic; a deterministic
1,376,256-cell sign-probability quadrature; 656,024 exact genus-two
member-affine-action checks; five synthetic GL(2)
controls under two kernel conventions; one three-curve rank correction; and
pooled plus root-number-split character covariance summaries formed from at
most 1,142 discriminants and 13 primes. The all-q genus-two certificate uses
2,925 operations in `Q[q]`, while the separate second-moment roadmap enumerates
only 20+54 symbolic signatures; neither enumerates additional fields. The
new high-weight packet adds 23 cubic signatures, while the affine Burnside
packet evaluates a rational all-degree generating series and closed divisor
sums through genus eight without enumerating another field. The power-echo
packet applies exact Newton recurrences through `r=8` to the locked
`q=3,5,7` histograms and independently checks the `C_2` Haar frequencies; it
does not enumerate another family. The reciprocal filter evaluates five
objects, four endpoints, and every coefficient through 256. The two new
packets add nine tests each; all 306 tests pass both normally and under
optimized Python; the
offline validator checks 64 artifact bindings across 15 evaluations. No broad
zero or conductor sweep was run.

Smallest remaining gaps: derive one true source-faithful function-field analogue
of `XD` or `HCNC`; evaluate the single virtual weight-six channel `R_6` left by
the balanced control's exact third-moment reduction; prove or refute the
quarantined all-`q` second-power echo candidate; classify which near-edge Weil
classes are realized by marked genus-two Jacobians; and prove a root-number-
conditioned weighted off-diagonal estimate uniform in a growing prime window.

## What this release contains

The atlas uses three record types:

- `LFunctionSpec` separates analytic continuation, functional equation, central
  order, Euler factors, zero coverage, and data-source rigor.
- `DetectorContract` fixes the mathematical definition, kernel convention,
  central-zero policy, typed inputs/parameters, family adapters, and failures.
- `EvaluationRecord` binds exact spec/detector contents, configuration, input
  artifacts, implementation, raw result, coverage, and interpretation.

Atlas records use deterministic `ATLAS.*.H<32 hex>` identities. They do not use
the programme/claim namespaces `LFAM2.*`, `LFAM3.*`, or `LFAM6.*`. Issues
[#737](https://github.com/gfreund123/riemann/issues/737),
[#738](https://github.com/gfreund123/riemann/issues/738), and
[#741](https://github.com/gfreund123/riemann/issues/741) are coordination
references, never misrecorded as source PRs.

The stable canonical contract at `canonical/provenance.schema.json` is unchanged.
An atlas record may become `RELEASED` only after it points to a separate full
canonical provenance sidecar with an exact object ID and content hash. These
first-pass records remain honestly unreviewed `DRAFT` objects. The sidecar hash
is defined over canonical UTF-8 NFC JSON, and the validator checks the canonical
schema, ID, digest, and backlink rather than accepting a path by presence alone.

## Compact result map

| Pilot | Arithmetic | Finite result | Boundary |
|---|---|---|---|
| normalized local Euler moments | exact integer point counts and rational even moments | GL(1) rows have `M2=M4=1`; three GL(2) rows already refute unit-magnitude prime coefficients | tiny prime window; curve metadata is discovery-only |
| classical reciprocal filter | exact integer coefficients and `Q(sqrt(2))` signs | the four-shell filter has mixed signs across objects/endpoints; no common finite sign survives | classical coefficients; unitary map explicit; four endpoints are not an abscissa or zero theorem |
| function field, genus 1 | exact cubic arithmetic at `q=3,5,7,11,13`; all-odd-`q` elliptic-stack trace formula and Burnside laws | every marked-model character and raw trace moment is explicit; full affine branch and elliptic coarse quotients are distinct; the first automorphic correction is at raw moment 10; the original `q=5` toy sign split is `40/20/40` | all-weight theorem uses the stated standard modular-trace input; five fields are frozen regressions, not its proof; toy `H_D(1)H_D(2)` is not canonical `XD`/`HCNC` |
| function field, genus 2 | exhaustive exact `F_q/F_{q^2}` arithmetic at `q=3,5,7`; exact all-q proof certificate; exhaustive affine action | normalized means are `-104/243`, `-1994/3125`, `-12340/16807`; all-q mean tends to `-1`, `liminf rho_->=1/20`, five low-weight character means are exact, and the second-moment gap reduces to `chi_(0,4)+chi_(2,2)+2chi_(0,3)` | orbit averages require stabilizer weights; the remaining high-weight decay and full sign law are conjectural; toy coefficient minor |
| product-variety tensor family | exact primitive degree-eight, weight-two `H^1(E)⊗H^1(C)` factor; all-`q` finite means from locked marginals; exact frozen `q=3,5,7` histogram convolution | compact image `(USp(2)×USp(4))/diag center` lies in `SO(8)`; `u^2h-u^4+2u^2v+u^2-2uw-w^2=0`; product-Haar trace `m4=6` versus generic `SO(8)` value `3`, and `(mean(h),mean(uw))=(1,1)` versus `(0,0)` | `A=-t_E` bridges the stored trace convention; frozen laws use ordered factor-pair model/curve-stack measure, not uniform coarse product varieties; no generic-`SO(8)` or convergence claim |
| exact `USp(4)` comparator | bounded Laurent-polynomial/Weyl arithmetic plus guarded shifted-grid quadrature | `F=(Tr U)^2-e_2(U)^2=-(1+chi_omega2+chi_2omega2)`, range `[-20,4/3]`, exact Haar moments through order 12; a degree-twelve majorant proves `P(F<0)>=0.480701...`; display-only `P(F<0)≈0.738` | the rational value is a lower bound, not the exact probability or a claimed optimal moment bound; finite-field higher-moment/sign-law convergence remains proposed |
| affine hyperelliptic presentation measures | exact Burnside fixed-locus divisor sums and a rational all-degree generating series, no field enumeration | marked affine-stack mass is `q^(2g-1)` in every genus; the universal leading coarse-orbit correction is `(q^g-(-1)^g)/(q+1)`; multiplicative resonances occur in degrees `0,1 mod d` for `d|q-1`, additive resonances in degrees divisible by `char(F_q)` | marked odd-degree equations, not the full unpointed hyperelliptic moduli stack; even degrees are covered by the series but define a different presentation problem |
| cross-rank coefficient minors | exact `USp(2g)` character algebra and bounded Weyl constant terms | the original alternating sign is all-rank Schur negativity; `B=2e_1^2-e_2^2` has symmetric arcsine-times-semicircle Haar law but exact finite mean `q^-1+q^-3-q^-4+q^-5` | no finite-family convergence; odd `B` moments remain arithmetic targets |
| virtual-character null directions | exact coefficient-square lattice, bounded integer panels, and independently reconstructed full `C_2` Weyl density | modulo `e_1e_3=e_1^2`, the only primitive coefficient-square direction is `B`; bounded panels isolate it among noncentral directions, while globally it generates `B Z[u^2+v^2,u^2v^2]` alongside the center-odd sector | bounded isolation is not global uniqueness, and the hardened full-density replay is a compact-group certificate only; no arithmetic-family claim |
| balanced genus-two control | independent exhaustive `q=3,5,7` coefficient scan with a source-locked member ledger | six exact frozen moments, signs, supports, affine orbits, and raw sums; the all-`q` mean is proved; `B^3=6B-2chi_(0,3)+R_6` reduces the first unresolved odd moment to one explicit virtual weight-six average | only the mean is all-`q`; raw sums and `mean(R_6)` are frozen three-field facts, not interpolated formulas |
| Frobenius-power echoes | exact Newton/Cayley--Hamilton transforms of the locked `q=3,5,7` histograms and independent `C_2` constant terms | the entire sequence is determined by `(B_1,B_2)`; distinct Haar frequencies are orthogonal, while mixed cubic moments resonate exactly when `r+s=t`; periodic frozen strata are recurrence-certified | orthogonality is not independence; the displayed all-`q` formula for `mean(B_2)` is a quarantined three-field conjecture; no endomorphism classification follows |
| genus-two tail geometry | exact reciprocal-quartic identities plus frozen support/orbit reconstruction | minima at `q=3,5,7` are split nonisotypic, repeated isotypic, and simple; repeated angles do not explain the dominant `q=7` tail | three fields only; coefficient admissibility is not Jacobian realization |
| high-weight channel probe | exact `C_2` triangularization and 23 bounded cubic signatures | isolates `b^3`, `a^2b^2`, `b^4`; records a sparse candidate implying `q^2 mean(H)->2` | candidate matches only three fields; primitive trace averages are unresolved |
| conductor-coprime twist precursor | exact pooled and sourced root-number-split character Gram/covariance matrices, marginal contrasts, and multiquadratic moments | through `X=2048`, local densities approach explicit comparators; root-sign Gram and character-mean contrast RMS shrink on the four frozen windows but their scaled/weighted corrections do not give a rate | no central ranks, fitted rate, growing-prime theorem, or twist-family limit |
| GL(2) deflation | exact `Fraction` matrices | central atom is rank one; Loewner sign is negative, Pick-sum sign positive; full deflation need not restore positivity | synthetic controls, no arithmetic L-values |
| rank stress | exact algebra on imported discrete metadata | rank 0 and minimal rank 1 give zero parity/full gap; rank 2 gives `25/4` at nodes `(1,2)` | three selected curves, not a twist family |

The detailed scientific synthesis and theorem nominations are in
[`FINDINGS.md`](FINDINGS.md) and [`THEOREM_TARGETS.md`](THEOREM_TARGETS.md).

## Layout

```text
schema/          three atlas schemas plus shared controlled vocabulary
specs/           ten content-addressed L-function/family specifications
detectors/       eleven typed detector contracts and seven raw-result schemas
evaluations/     fifteen content-bound evaluation wrappers
results/         compact derived raw outputs
sources/         compact source-identifier manifest, not a database mirror
core/            generators, exact local arithmetic, and offline validator
function_field/  exact finite-field implementation, fixture, and report
gl2/             exact deflation algebra, controls, verifier, and report
```

## Lightweight replay

From the repository root:

```powershell
python research/l-families/atlas/core/run_pilot.py
python research/l-families/atlas/function_field/pilot.py --check research/l-families/atlas/function_field/fixtures.json
python research/l-families/atlas/function_field/genus2_pilot.py --check research/l-families/atlas/function_field/genus2_f3_quintics.json
python research/l-families/atlas/function_field/genus2_q_scan.py --check research/l-families/atlas/function_field/genus2_q_scan.json
python research/l-families/atlas/function_field/genus2_moment_identity.py
python research/l-families/atlas/function_field/genus2_affine_orbits.py --check research/l-families/atlas/function_field/genus2_affine_orbits.json
python research/l-families/atlas/function_field/genus2_second_moment_reduction.py --check research/l-families/atlas/function_field/genus2_second_moment_reduction.json
python research/l-families/atlas/function_field/genus2_family_measures.py --check research/l-families/atlas/function_field/genus2_family_measures.json
python research/l-families/atlas/function_field/hyperelliptic_affine_burnside.py --check research/l-families/atlas/function_field/hyperelliptic_affine_burnside.json
python research/l-families/atlas/function_field/genus1_cubic_family_laws.py --check research/l-families/atlas/function_field/genus1_cubic_family_laws.json
python research/l-families/atlas/function_field/balanced_control_family_scan.py --check research/l-families/atlas/function_field/balanced_control_family_scan.json
python research/l-families/atlas/function_field/frobenius_power_echoes.py --check
python research/l-families/atlas/function_field/genus2_high_weight_channel_probe.py --check research/l-families/atlas/function_field/genus2_high_weight_channel_probe.json
python research/l-families/atlas/function_field/genus2_tail_geometry.py --check research/l-families/atlas/function_field/genus2_tail_geometry.json
python research/l-families/atlas/function_field/product_variety_tensor_family.py --check research/l-families/atlas/function_field/product_variety_tensor_family.json
python research/l-families/atlas/function_field/virtual_character_null_directions.py --check
python research/l-families/atlas/function_field/usp4_toy_minor_moments.py --check research/l-families/atlas/function_field/usp4_toy_minor_moments.json
python research/l-families/atlas/function_field/usp4_toy_minor_character_decomposition.py --check
python research/l-families/atlas/function_field/usp_coefficient_minor_rank_scan.py --check
python research/l-families/atlas/function_field/usp4_twelve_moment_sign_bound.py --check research/l-families/atlas/function_field/usp4_twelve_moment_sign_bound.json
python research/l-families/atlas/function_field/usp4_sign_probability.py --check research/l-families/atlas/function_field/usp4_sign_probability.json
python research/l-families/atlas/gl2/verify.py --check research/l-families/atlas/gl2/results.json
python research/l-families/atlas/core/wrap_specialist_pilots.py
python research/l-families/atlas/core/wrap_genus2_pilot.py --check
python research/l-families/atlas/core/reciprocal_wavelet.py --check
python research/l-families/atlas/core/twist_character_covariance.py --check
python research/l-families/atlas/core/twist_root_number_covariance.py --check
python research/l-families/atlas/core/wrap_genus2_q_scan.py --check
python research/l-families/atlas/core/wrap_usp4_toy_minor_moments.py --check
python research/l-families/atlas/core/validate_atlas.py
python -m unittest discover -s tests -p "test_*.py"
```

The offline validator uses only the standard library. It rejects duplicate JSON
keys, non-finite numbers, Unicode-normalization drift, unknown fields, stale
identity/configuration/content hashes, unsafe paths, parameter drift, unbound
released records, missing or malformed provenance sidecars, implementation-byte
drift, typed-input/output mismatches, incomplete artifacts, and several
rigor/scope confusions.

## Scientific firewalls

- Finite rows do not imply a prime limit, family law, RH, or GRH.
- Classical reciprocal coefficients for motivic weight one differ from unitary
  coefficients by `sqrt(n)`; their raw magnitudes are not cross-family moments.
- Known function-field root radius does not itself prove a project-specific
  signed detector estimate.
- A family mean is not a memberwise conclusion.
- Positive/negative discriminant strata are not root-number strata; the
  separate root-number packet uses the sourced rule
  `epsilon_d=sign(d)*(d/11)` for conductor-coprime twists of `11.a2`.
- A finite decrease in raw covariance RMS is not a uniform weighted moment bound.
- Three exact fields are not evidence for higher-moment equidistribution. The
  all-q first-moment identity is instead bound to a separate proof and exact
  polynomial certificate.
- The genus-one all-weight formulas use the explicitly stated standard
  modular-stack trace identity; the five frozen prime fields check the formulas
  but do not prove them. Signed trace descends to the elliptic quotient, not to
  the full affine branch quotient.
- The balanced scan independently locks its `q=3,5,7` raw sums and exact
  `R_6` reduction, but supplies no all-`q` formula for `mean(R_6)`.
- Frobenius-power echoes collapse pointwise to `(B_1,B_2)`. Their exact Haar
  frequency orthogonality is not independence, and the proposed all-`q`
  `mean(B_2)` formula remains explicitly conjectural.
- The product-variety packet uses `A=-t_E` to bridge the locked genus-one trace
  convention. Its all-`q` finite mean corrections come from locked marginal
  theorems, while its `q=3,5,7` laws are frozen histogram convolutions under
  ordered factor-pair model/curve-stack measure, not uniform coarse measure.
- The virtual-character panels isolate `B` only inside their declared bounded
  boxes. The infinite module `B Z[u^2+v^2,u^2v^2]`, the separate center-odd
  sector, and the full-density replay are exact compact-group statements, not
  arithmetic-family laws.
- The proved negative-member proportion is a one-sided density floor, not a
  limiting sign law or a canonical detector conclusion.
- The degree-six and degree-twelve `USp(4)` certificates give rigorous Haar
  lower bounds, not the exact sign probability; their finite-family liminf
  consequences assume convergence of the first six or twelve moments.
- A forced central zero is legitimate critical-line geometry, not an off-line
  witness.
- Parity deflation and full-rank deflation use different information.
- `Loewner difference` and `Pick sum/Hankel` have opposite central-atom signs.
- Dynamic LMFDB rank/root metadata remains `DISCOVERY_ONLY` here.
