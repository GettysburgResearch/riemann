# Validation and exact acceptance semantics

## Analytic proofs and reviews

All universal claims rely on the complete proofs in the component manuscripts across the four lanes, not on a finite run count. Separate internal reviews are provided for the anchor, cofinal Bessel, cosine/native, and local certificate components. Each binds the load-bearing files with SHA-256 digests and states which arguments were reconstructed and which programs were independently replayed. The coordinator's review discloses its contributions and authorship.

No proof assistant or external human referee has certified the packet. The status is proposed research, with the RH-level obligations preserved in `CLAIMS.md`.

## Exact finite replay

`EXACT_REPLAYS.json` records the coordinator's normal and optimized isolated Python executions after copying the frozen files into their publication layout. All four outputs reproduce their stored receipts byte for byte in both modes.

| Checker | Actual scope | Result |
|---|---|---|
| `anchor/verify_anchor_followup.py` | 606 exact checks of cross-projection algebra, Laguerre dilation/weighted Gram identities, pole moments, and rational budget constants. | PASS; independently replayed by the Bessel reviewer and by the coordinator. |
| `bessel/verify_companion_structure.py` | 24 order-versus-differential recurrence identities, 48 coefficient-sign checks, three explicit low-order formulas, concentration remainder constants, and the special-value ODE factor. | PASS; independently replayed normal and optimized by the cofinal reviewer and coordinator. |
| `cosine/verify_cosine_native.py` | 30,783 reported finite checks, including one optimization-configuration check; discrete weights, dilations, source identities, rational enclosures, Mobius prefixes, and the tail-constant simplification. | PASS; independently replayed normal and optimized by the final cosine reviewer and coordinator. |
| `local_gate/verify_local_gate_controls.py` | Exact rejection of the two mathematically incomplete boundary-only models. | PASS; independently replayed by the Bessel reviewer and coordinator. |

These scripts use explicit exceptions and exact integers/Fractions for numerical acceptance. Optimization does not remove their acceptance decisions. Selected source-moment interval-overlap checks are finite corroborations; they are not a substitute for the universal source identities proved in the text.

## Complete local source certificates

`local_gate/certify_bessel_window.py` is both a primitive producer and a checker: it does not accept a saved list of coefficients, roots, or signs. On each run it reconstructs the source and proves all conditions from outward rational enclosures.

The rounding contract is the inherited rational interval class, configured in an isolated namespace to an outward grid of `10^(-130)`. Every primitive operation encloses the corresponding exact operation. Pi is reconstructed using rational alternating Machin sums. Square/fourth roots use integer floors plus an outward upper enlargement. The exponential routine retains its explicit full Taylor remainder and scaling-and-squaring enclosure. Theta indices beyond seven and Bessel-I series terms beyond index 180 are bounded by complete positive tails.

Acceptance requires all of the following:

1. Every actual coefficient weight has a strictly positive lower bound.
2. Repeated interval Graeffe squaring yields a strict coefficient-dominance inequality, proving the exact number of all complex denominator zeros inside the disk and excluding boundary zeros.
3. That many disjoint positive real sign-change intervals exhaust the complex count, proving simplicity and excluding all additional poles.
4. Every full root interval has nonzero numerator and derivative enclosures and a strictly positive residue enclosure. An unresolved sign is refined rigorously or rejected; it is never assigned a convenient sign.
5. Every Bernstein subinterval covering `[-1,1]` has strictly positive coefficient lower bounds for the exact curved-boundary sign polynomial.

The analytic maximum-principle and Weyl-function consumer then turns those accepted predicates into the all-real-zero conclusion. Both interior-pole and residue checks are necessary; the negative controls demonstrate their separate roles.

| Primitive run | Energy radius | Complete denominator count | Whole-boundary certificate | Evidence |
|---|---:|---:|---|---|
| `a=10, M=50` | 500 | 6 | Degree 24, one Bernstein cell, depth zero. | Author run plus independent primitive replay by the Bessel reviewer; byte-identical receipt. |
| `a=20, M=100` | 500 | 8 | Degree 49, five Bernstein cells, maximum depth four. | Author run; independently inspected analytic/code consumer and receipt; coordinator repeated the full primitive run after relocation with `-O`. |

The full rational pole and residue intervals and strict margins are in the two source receipts. `LOCAL_RELOCATED_REPLAY.json` binds the relocated optimized order-100 replay and its byte comparison. The independent reviewer explicitly did not rerun the order-100 case, and the replay uses the same interval backend rather than an independently implemented arithmetic library.

The reported counts are denominator-pole counts. Neither is asserted to equal the transform-zero count. The proved conclusion is reality of every transform zero in the specified disk, not a new zero census for zeta.

## Ordinary diagnostics

`bessel/companion_probe.py` uses NumPy and SciPy binary64 quadrature and root refinement. `COMPANION_PROBE.json` warns about large-energy cancellation. `residue_scaling_diagnostic.py` uses ordinary Decimal arithmetic and the same source polynomial recurrence as the preceding diagnostic, reproduced in `source_polynomials.py`. Its 240- and 360-digit outputs are retained.

Those runs explore the rescaled residue asymptotic on the stated logarithmic cofinal schedule. Their agreement on displayed quantities does not make them directed, does not establish a complete root count, and does not certify the limiting companion ratios. They are not acceptance gates for any theorem in this packet. The exact local certificate has an independent rational implementation and a complete coverage argument.

Optional diagnostic commands from the `bessel` directory are:

```sh
python -B companion_probe.py
python -B residue_scaling_diagnostic.py 240
python -B residue_scaling_diagnostic.py 360
```

The exact checkers in the README need only the standard library. The optional quadrature diagnostic needs NumPy/SciPy. The Decimal diagnostic imports the adjacent source module, so it is intentionally not presented as an isolated `-I` invocation.

## Artifact integrity

`MANIFEST.json` records each delivered file's relative path, byte count, SHA-256, and Git blob SHA-1; it excludes itself to avoid a circular digest. The source reviews bind the specific files they reviewed. `PREFLIGHT.json` records parsing and local-link checks and the consistency of bound source hashes. These integrity checks establish identity and packaging only.

The prepared publication is additive on the exact parent commit. A successful remote write must be followed by checking every local Git blob digest and every inherited parent blob. That publication readback remains pending if the delivery notes report an interrupted upload. No status label or successful replay promotes the proposed components into integrated or globally proved results.
