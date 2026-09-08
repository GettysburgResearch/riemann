# Validation and independent-review contract

Status: bounded authoring replay, not an independent mathematical verdict.
RH and all-section positivity remain unproved.

## Executed

`python verify_bridge.py --check result.json` and the same command with `-O` each recomputed **2,188** finite checks. Their complete stdout bytes agree. The output is rebuilt from source calculations, not accepted from a stored PASS field. The final command records and stdout/stderr SHA-256 hashes are in REPLAY_LOG.json.

The suite contains exact rational/Gaussian-rational checks of inverse Laplace identities; gamma telescoping and conservative constants; independent finite-spectrum versus source-jet matrix construction; conserved-form entries; the full partial-trace remainder; simultaneous strip damping; finite LDL reconstruction; the six-node countercontrol; and the actual 4-by-4 interval certificate. Repeated arithmetic checks are not counted as additional theorems.

The actual certificate uses rational outward intervals on a 10^-80 grid, Euler--Maclaurin with N=64 and 12 Bernoulli terms, an explicitly bounded Cauchy-circle remainder for the zeta jet, Machin's identity, and convergent logarithm series. The analytic remainder derivation is in BRIDGE.md. Neither known zeros nor floating-point special-function values enter acceptance. A redundant interval matrix construction is checked for overlap, while exact equality of the two construction formulas is tested separately on rational models.

Twelve corruption runs were rejected with their intended errors: a changed saved pivot, floating-point numeric alias, Boolean alias, duplicate JSON key, changed proof bytes, and changed parent-source lock; each in normal and optimized Python. Two oversized orchestration calls encountered tool time limits after already completed subprocesses. The final execution receipt retains only completed subprocesses and was finished in separate bounded calls. No interrupted command is labeled a completed suite.

An earlier floating-point synthetic scout was used to select a hostile six-node control; its output is not an acceptance certificate and is not included as actual-zeta data. The final control is independently reconstructed using exact Gaussian rationals.

## Source and integrity scope

The GitHub source for #793's R3_HARDY_CAPTURE.md was read at the pinned commit and its returned Git blob was recorded. The #792 parent archive is present locally; its five listed proof blobs match the previously published Git identities. This is source receipt/integrity evidence, not independent certification of parent mathematics. The new checker records SHA-256 hashes of BRIDGE.md, REVIEW.md and SOURCE_LOCK.json. SHA256SUMS binds all final packet files except itself. The checker does not perform network reacquisition of external files.

The previous 29 #792 files are unchanged. Their old test counts are NOT added to this pass. No parent suite, full repository suite, Lean build, zero census, broad prime sweep, remote CI, or independent referee review was executed or claimed.

## Required mathematical review

1. Reconstruct the exact arithmetic kernel, especially the growing exponential, C_b, and both prime shifts.
2. Check the shift-plus-rank-one trace-norm bound, and distinguish it from relative-form domination.
3. Check the bivariate source matrix and the number of safe derivatives needed for each finite section.
4. Check the all-zero multiplicities, the factor 9/8, and the orientation in A*TA=T.
5. Check the exact trace-tail formula before estimates; deleting matrix entries beyond column M-1 is forbidden.
6. Check simultaneous damping when M>=n and the dyadic-shell constant, including low zeros and endpoints.
7. Check predetermined compression convergence and the distinction between existence of a detecting section and a universal lower negative gap.
8. Audit the rational Euler--Maclaurin remainder and interval LDL certificate independently.
9. Retain the negative fifth pivot control and the non-summable sharp relative prime bound. Neither actual positivity nor a new signed prime cancellation estimate follows from the other results.

The smallest statement whose failure would invalidate the proposed new all-degree leverage is the exact trace-tail identity (A13) with its normalization and multiplicities. The smallest still-unproved assertion needed to finish this attempted RH route is positivity of the complete source operator, not finite matrix feasibility or numerical precision.
