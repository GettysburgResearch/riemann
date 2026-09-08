# Validation and exact scope

## Executed

The final source ran the following clean checks:

    python verify.py --check checks.json
    python -O verify.py --check checks.json
    python verify_low_zeros.py --check low_zeros.json
    python -O verify_low_zeros.py --check low_zeros.json
    python test_rejections.py
    sha256sum -c SHA256SUMS

The main verifier reconstructed 284 distinct exact rational/Gaussian-rational
controls in each mode, with byte-identical output. This count includes finite
matrix PSD checks for the Jacobi concentration lemma, finite Legendre
orthogonality and complex evaluation controls, exact exponent comparisons,
all rational constants in the actual three-node reservoir bound, and synthetic
negative forms/inertia. Reruns inside rejection tests are not counted as new
controls. The finite fixtures do not prove the universal analytic statements.

The endpoint verifier recomputed all SIX directed signs at 14,15,21,22,25,26
in both modes, with byte-identical output. No floating-point special-function
value is accepted as a proof input. The mpmath 1.3.0 interval Gamma and complex
interval arithmetic remain explicit software trust dependencies. The Euler
eta tail is proved analytically in ACTUAL_BLOCKS.md. This is not an independent
verification of all zeros through height 100.

Twelve deliberate result corruptions were rejected with their intended error:
RH flag, float alias, duplicate key, saved tail margin, endpoint sign, and eta
tail, each in both interpreter modes. Refusals are recorded in refusals.json.
Checks compare canonical freshly generated output, not self-declared PASS flags.

The unchanged predecessor prime-cutoff-pass6 verifier was also rerun: all
16 test cases passed normally and under -O, with identical output. Its local
proof blob matched freshly read remote metadata at the current branch head.
That replay does not independently validate every analytic predecessor claim.
The external publication helper's signed-tail-pass6 ten-dimensional certificate
was read but NOT replayed or promoted to a new review status here.

The external REPLAY_LOG.json in the delivery archive records the clean
subprocess commands, return codes, output hashes, and actual elapsed times.
It is an execution receipt, not a mathematical certificate. The tracked
source files do not attempt to contain their own future commit SHA.

## Authoring correction caught before acceptance

An initial diagnostic run rejected the new checker when a Gaussian-rational
constructor permitted integer components to reach Python's integer division,
producing a float. A post-construction normalization to Fraction and explicit
rejection of nonexact component types fixed this. No output from that failed
run is retained as passing evidence. All reported executions used the repaired
strict exact-arithmetic implementation.

The full-form interpolation constant uses 4/1941 at the second interval;
this is recomputed from 22^2+5/4, not copied from a rounded ordinate. The
all-degree error threshold was sharpened during authoring from a quadratic
condition to 256(d+2)(ceil(log_2(d+2))+1); the manuscript supplies its complete
all-parameter proof and the final checker uses only the sharpened condition.

## Not performed or claimed

No evaluation of the complete prime tail, broad prime or zero scan, all-height
verification, new actual-xi numerical matrix, Lean proof, independent referee
acceptance, source-wide CI run, or external priority search establishing
novelty is claimed. The new analytic source-tail matrix theorem does not use
V100. The actual full three-dimensional theorem does import V100 and the six
endpoint signs, as declared.

The complete RH-strength all-width sign remains open. Neither strict negative
tail matrices nor exponentially small full residuals are labeled full positivity.
The synthetic three-atom negative form is not actual xi and has no original
Euler product.

## Publication boundary

The source was prepared add-only against the verified remote head
f0584f7a49550540eaed005868422a83cb3e1011. This session exposes GitHub read
actions but no write action; a local Git connection failed DNS resolution.
No new remote commit, push, PR edit, or comment was made by this continuation.
The patch and delivery receipt are provided separately for publication.
