# Executed validation and review boundary

Date: 2026-09-12. Platform: Linux, CPython3.13.5. Author-executed only; no independent analytic review, formal verification, whole-repository build or remote CI is claimed.

## Accepting reconstruction

Both completed successfully and reconstructed the entire retained JSON:

```
python -S -B check.py --check results.json
python -S -B -O check.py --check results.json
```

Every invocation regenerates eleven native theta moment intervals (M_0 through M_10), including the complete analytically proved alias, theta-tail and spatial-tail allowance. It reconstructs ten ratios, ten Bernstein polynomial coefficient intervals for the full parameter range, 45 scalar finite-difference signs, the exact rational positive-kernel identity, the all-real countercontrol, and the robust perturbation constants. Arithmetic uses288 fractional bits, int/Fraction, Machin pi and a fully bounded exponential series; no float or zeta evaluator is an accepting input.

The exact dyadic Q_0 interval is retained in results.json. Its outward decimal18 enclosure is

```
[-0.000000146710376192, -0.000000146710376191].
```

All ten Bernstein upper endpoints are below -1/2; the largest upper endpoint, displayed outwards to18 decimals, is -0.532382613124399411. These arithmetic claims are conditional on the analytic source/error contract proved in PROOF.md, not an automated independent proof of it.

## Seven test methods, both Python modes

Both `python -S -B tests.py` and `python -S -B -O tests.py` passed all seven methods, including:

- a full second reconstruction at mesh1/96, with overlapping complete moment intervals and the same strict parameter-uniform sign;
- exact positive-kernel and complete-Bernstein controls, and an exact negative value for the all-simple-real-zero control cos(z)cos(4z);
- rational interval operations, elementary identities, input rejection, and independent evaluations of the Bernstein-basis conversion;
- one actual pristine CLI acceptance and four actual altered-record CLI refusals per mode, each after full primitive reconstruction.

The four alterations change the claimed Q interval, a moment endpoint, a polynomial coefficient endpoint, and a witness coefficient respectively. These are four full subprocess refusals, not four labels for the same call. Normal and optimized modes use the same producer and are not independent implementations. Neither are the two meshes independent analytic proofs.

## Packaging and provenance

A clean temporary extraction of the retained packet ZIP passed both full checks and both seven-method test suites. An initial combined validation command hit its execution timeout during the last extracted test run; the complete extracted checks and both suites were then rerun in a separate command. MANIFEST.sha256 lists every other packet file; the manifest itself is not self-hashed. The archive contains only the nine intended UTF-8 files, with no scouting dependencies or bytecode.

The scalar numeric core was adapted from the earlier #851 intervals.py at exact head57726ef9b3bf90561df5a361e3b01169c892a62a. Its8616 source bytes have Git blob032d3693cb5b7828a38d0620ed8d901b1cdaee56, matching the separately fetched authenticated remote identity. Unused complex/logarithmic code was removed and an explicit scalar-point type guard added. This packet's current hashes, not that parent hash, bind the accepting code here.

Noncertifying high-precision scouts suggested a continuous-interpolant failure and then a finite positive-square witness. A continuous-interpolant test would not have excluded all possible interpolants, so it was not accepted as the result. The retained derivative-free rational test resolves that distinction. Scout outputs are not included as certificates or used by check.py. The first CLI print used a lexical maximum of negative decimal strings; it was corrected to select the integer upper endpoint before these final runs. No mathematical acceptance predicate used that display ordering.

## What remains unverified or open

A reviewer must check the full theta normalization, evenness, all contour assumptions and constants, and the inference from the specific complete-Bernstein representation to the finite inequality. Code replay does not establish those independently. No parent full numerical suite, historical branch audit, Lean build, Windows run, or repository-wide validation was performed.

The new result excludes one stronger proposed structural model, including its sufficiently accurate approximants. It does not exclude RH, ordinary non-complete Bernstein models, coupled Lee–Yang constructions or the reflected-family programme. It does not establish the source-specific weighted-defect vanishing or all-height critical-line confinement. No finite numerical observation has been promoted to either assertion.
