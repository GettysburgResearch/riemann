# Validation, proof inputs, and review boundaries

Status: proposed research components. These records do not integrate a new
claim into the repository's accepted mathematical baseline.

## What the proofs establish

The shared-family proof supplies finite-horizon mean and covariance limits for
actual discriminants, explicit errors, critical-energy comparisons, a complete
random Euler residual decomposition, a causal correction and an actual-family
fixed-mollifier residual limit in `Re s>3/4`. Its proof uses classical
Pólya--Vinogradov, quadratic reciprocity, quadratic factorization and the
approximate functional equation. The exact finite checker does not certify
those analytic inputs or their limiting arguments.

The strip proof supplies an obstruction to elementary product approximation,
a compactness counterexample, a finite ferromagnetic strip and growth theorem,
an all-order conditional consequence and a finite example. The imported
inputs are the classical theta Fourier identity, multivariate Lee--Yang, and
Li--Radziwill's unconditional arithmetic-progression nonvanishing theorem.
The all-order matching premise is unproved. The conditional local degree-20
continuation additionally assumes the proposed T20D theorem and invertible
Jacobian at the exact #994 source; neither is newly certified here.

No priority claim for a new published theorem is made. The claims are new
components of this packet, with complete arguments for independent review.

## Exact finite checks actually executed

Both authors ran their finite checkers. A separate agent reran both checkers
with optimized Python, and the root agent replayed the assembled packet.
The output artifacts reproduce the committed bytes. The accepting code uses
explicit exceptions rather than relying on Python `assert` statements.

| Check | Complete finite coverage | Arithmetic contract |
|---|---|---|
| Full inverse Dedekind coefficients | Ten actual fields, every integer index through 240 | Exact integers |
| Native mean, covariance and critical energy | All 27 states of the ramified three-prime law; means through 10; all pairs of the listed covariance cutoffs | Exact rational probabilities and integrals of step functions |
| Full residual and causal correction | All 27 states at cutoffs 1, 3, 8, 15, 30; complex conjugations; every finite variance component; common scalar zero; inverse convolution | Exact complex rationals |
| Actual-family observations | All odd squarefree `u` in `(Q,2Q]` for Q=100, 1000, 10000, horizon 20 | Exact finite sums; observations only, not a rate certificate |
| Theta constants for the new example | Fresh reconstruction of the inherited primitive source including its omitted tails | The same inherited outward 320-bit integer backend |
| 18-spin example | Strict positive weights, discriminant, field/weight cap, reference variance and nonreal-zero height | Directed intervals, with exact algebra proving moment equalities |
| Dimer law | All four Gibbs configurations | Exact rational masses |
| Independent small graph check | All 32 spin states and all 16 edge subsets of a five-spin tree; all spin-correlation subsets and weighted variance | Exact rational enumeration |

The theta interface reconstructs moments through 20, but the new directed
example uses and matches **only moments 2 and 4**. The code's interval overlaps
for those moments are diagnostics. The algebraic construction in the proof
establishes exact equality; an overlap by itself would not do so.

The new finite example has 18 observed spins and one positive ferromagnetic
edge. It is not asserted to be a connected 18-vertex graph. Connectedness is
not a hypothesis of the strip theorem.

## Authenticated inherited arithmetic

The strip checker authenticates the following source files before importing
them. They reside in the sibling theta packet on the pinned publication base:

`standalone/2026-10-18-theta20-and-native-cancellation/theta/`

Source commit: `c93ca65a510b6acaf167f929b9bf7e67d742b05a`.

| Source file | Required Git blob SHA |
|---|---|
| `pr886_primitive.py` | `c32015f110d10186538ffabcb4689ba5bbc060d0` |
| `theta_source.py` | `fc51d49fe2bdbbde3fcb3928f1d82fd8baffbf53` |

This is a fresh execution of one inherited transcendental implementation,
not a second independent transcendental backend. The exact graph enumeration
and rational family checks are separate finite calculations.

## Independent mathematical review

The authoring agents worked on separate routes. A third agent audited both
proofs and independently ran the finite checkers. The root agent additionally
read the main arguments, checked the key local algebra, conductor exponents,
normalization and source scope, and performed the final assembled replay.

- [Shared-family independent review](audit/SHARED_INDEPENDENT_REVIEW.md)
- [Strip-model independent review](audit/STRIP_INDEPENDENT_REVIEW.md)
- [Field-specialization and probe audit](audit/FIELD_SPECIALIZATION_AND_PROBE_AUDIT.md)

The first two reviews bind their load-bearing files and artifacts by SHA-256.
The strip review records the inherited source hashes under the author's
temporary `strip/inherited/` layout; those identical bytes are provided by
the pinned sibling packet in the published repository layout.

These are independent-agent reviews within one AI session. They are not
external human referee reports, Lean checks, or integrated approval. The
reviewed finite computations cannot establish the all-horizon Möbius estimate,
a strict residual below one, or cofinal theta-model feasibility.

## Empirical continuations have a separate status

[strip/EXPERIMENT.md](strip/EXPERIMENT.md) describes the ordinary
high-precision searches, dependency identities, model charts, stopping points
and observed discrepancies. Their decimal arithmetic is not directed.
Retuned finite numerical moment equations are not exact root certificates.
These searches are omitted from the accepting packet replay: the scientific
theorems do not depend on their success.

## Reproduce the accepting checks

From the repository root:

```sh
python standalone/2026-10-18-zeta-specific-family-and-strip/verify_packet.py --replay
```

The runner checks the manifest, runs the two checkers with `python -O`, and
then rechecks the manifest so that generated output must agree byte for byte.
Without `--replay`, it only authenticates the listed files. No hash is offered
as a proof of a mathematical statement.

For a different filesystem layout, supply the exact source explicitly:

```sh
python verify_packet.py --replay --theta-source /path/to/exact/theta
```

The standard Python library suffices for the accepting checks, using the
pinned inherited source. The optional numerical experiments also use the
standard library, with ordinary Decimal arithmetic and the inherited source
inputs recorded in their experiment report.

No repository-wide build, remote CI result, numerical zeta-zero census,
independent T20D root replay or full reconstruction of the imported analytic
literature is claimed.
