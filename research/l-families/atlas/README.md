# Phase-0 L-function detector atlas

Status: **exact finite exploration, exact synthetic algebra, and source-qualified discovery data**.

Scope: one small GL(1)/GL(2) local-Euler corpus; the complete family of 100
monic squarefree cubics over `F_5[T]`; the complete genus-two quintic families
over `F_3[T]`, `F_5[T]`, and `F_7[T]` (162, 2,500, and 14,406 members); exact
rational central-deflation controls; one five-object classical reciprocal-
coefficient filter through `n<=256`; and conductor-coprime quadratic-character
covariance packets for `11.a2`, both pooled and split by the sourced twist root
number. An exact `USp(4)` comparator and proof-backed all-odd-prime-power
coefficient moments, negative-sign density floor, second-moment proof roadmap,
and twelve-moment polynomial sign bound accompany the genus-two scans. Every
atlas record is `DRAFT`. RH
and GRH remain open.

Exact sources or dependencies: classical completed GL(1) normalizations; the
displayed finite-field definitions; LMFDB object identifiers and dynamic
metadata for three elliptic-curve discovery rows; Rohrlich's and Conrey's
quadratic-twist sign formulas; the function-field even-character coefficient
identity cited in the genus-two proof; CPython 3.12.10 standard library; and the
exact repository packets named inside detector contracts.

What was actually run: five finite local-Euler evaluations through `p<=43`;
all four complete function-field families above; exact `F_q/F_{q^2}` character
reconstruction for the three genus-two packets; twelve exact `USp(4)` Haar
moments and degree-six and degree-twelve sign majorants by bounded
Laurent-polynomial arithmetic; a deterministic
1,376,256-cell sign-probability quadrature; 656,024 exact genus-two
member-affine-action checks; five synthetic GL(2)
controls under two kernel conventions; one three-curve rank correction; and
pooled plus root-number-split character covariance summaries formed from at
most 1,142 discriminants and 13 primes. The all-q genus-two certificate uses
2,925 operations in `Q[q]`, while the separate second-moment roadmap enumerates
only 20+54 symbolic signatures; neither enumerates additional fields. The
reciprocal filter evaluates five objects, four endpoints, and every coefficient
through 256. All 214 tests pass both normally and under optimized Python; the
offline validator checks 64 artifact bindings across 15 evaluations. No broad
zero or conductor sweep was run.

Smallest remaining gaps: derive one true source-faithful function-field analogue
of `XD` or `HCNC`; prove higher genus-two moments or effective `USp(4)`
equidistribution; and prove a root-number-conditioned weighted off-diagonal
estimate uniform in a growing prime window.

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
| function field, genus 1 | exhaustive exact `F_5[T]` arithmetic | all 100 cubic members pass reciprocal/root-radius checks; toy sign split is `40/20/40`, mean zero | toy `H_D(1)H_D(2)`, not canonical `XD`/`HCNC` |
| function field, genus 2 | exhaustive exact `F_q/F_{q^2}` arithmetic at `q=3,5,7`; exact all-q proof certificate; exhaustive affine action | normalized means are `-104/243`, `-1994/3125`, `-12340/16807`; all-q mean tends to `-1`, `liminf rho_->=1/20`, five low-weight character means are exact, and the second-moment gap reduces to `chi_(0,4)+chi_(2,2)+2chi_(0,3)` | orbit averages require stabilizer weights; the remaining high-weight decay and full sign law are conjectural; toy coefficient minor |
| exact `USp(4)` comparator | bounded Laurent-polynomial/Weyl arithmetic plus guarded shifted-grid quadrature | `F=(Tr U)^2-e_2(U)^2=-(1+chi_omega2+chi_2omega2)`, range `[-20,4/3]`, exact Haar moments through order 12; a degree-twelve majorant proves `P(F<0)>=0.480701...`; display-only `P(F<0)≈0.738` | the rational value is a lower bound, not the exact probability or a claimed optimal moment bound; finite-field higher-moment/sign-law convergence remains proposed |
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
python research/l-families/atlas/function_field/usp4_toy_minor_moments.py --check research/l-families/atlas/function_field/usp4_toy_minor_moments.json
python research/l-families/atlas/function_field/usp4_toy_minor_character_decomposition.py --check
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
