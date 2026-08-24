# Phase-0 L-function detector atlas

Status: **exact finite exploration, exact synthetic algebra, and source-qualified discovery data**.

Scope: one small GL(1)/GL(2) local-Euler corpus, the complete family of 100
monic squarefree cubic quadratic characters over `F_5[T]`, and exact rational
central-deflation controls, plus one five-object classical reciprocal-coefficient
filter through `n<=256`. Every evaluation record is `DRAFT`. RH and GRH remain
open.

Exact sources or dependencies: classical completed GL(1) normalizations; the
displayed finite-field definitions; LMFDB object identifiers and dynamic
metadata for three elliptic-curve discovery rows; CPython 3.12.10 standard
library; and the exact repository packets named inside detector contracts.

What was actually run: five finite local-Euler evaluations through `p<=43`,
18,700 exact function-field character terms, five synthetic GL(2) controls
under two distinct kernel conventions, one three-curve rank correction, 63
unit tests, and an offline schema/content-binding validation of 31 artifact
bindings. The reciprocal filter evaluates
five objects, four endpoints, and every coefficient through 256. No broad zero,
conductor, or twist sweep was run.

Smallest remaining gap: derive one true source-faithful function-field analogue
of `XD` or `HCNC`, and bind one genuine quadratic-twist family strongly enough
to evaluate a deflated logarithmic-derivative or reciprocal-wavelet moment.

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
| function field | exhaustive exact `F_5[T]` arithmetic | all 100 cubic members pass reciprocal/root-radius checks; toy sign split is `40/20/40`, mean zero | toy `H_D(1)H_D(2)`, not canonical `XD`/`HCNC` |
| GL(2) deflation | exact `Fraction` matrices | central atom is rank one; Loewner sign is negative, Pick-sum sign positive; full deflation need not restore positivity | synthetic controls, no arithmetic L-values |
| rank stress | exact algebra on imported discrete metadata | rank 0 and minimal rank 1 give zero parity/full gap; rank 2 gives `25/4` at nodes `(1,2)` | three selected curves, not a twist family |

The detailed scientific synthesis and theorem nominations are in
[`FINDINGS.md`](FINDINGS.md) and [`THEOREM_TARGETS.md`](THEOREM_TARGETS.md).

## Layout

```text
schema/          three atlas schemas plus shared controlled vocabulary
specs/           six content-addressed L-function/family specifications
detectors/       six typed detector contracts and two raw-result schemas
evaluations/     ten content-bound evaluation wrappers
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
python research/l-families/atlas/gl2/verify.py --check research/l-families/atlas/gl2/results.json
python research/l-families/atlas/core/wrap_specialist_pilots.py
python research/l-families/atlas/core/reciprocal_wavelet.py --check
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
- A forced central zero is legitimate critical-line geometry, not an off-line
  witness.
- Parity deflation and full-rank deflation use different information.
- `Loewner difference` and `Pick sum/Hankel` have opposite central-atom signs.
- Dynamic LMFDB rank/root metadata remains `DISCOVERY_ONLY` here.
