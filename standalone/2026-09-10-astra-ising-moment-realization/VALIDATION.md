# Executed validation and review boundary — IMR26

Status: proposed component proofs, not independent mathematical acceptance.
No proof of RH or of the all-order realization (IR) is claimed.

## Exact accepting computation

Executed both commands, with byte-identical stdout and the retained result:

    python -I -S -B check.py --check result.json
    python -I -S -B -O check.py --check result.json

The new standard-library interval implementation uses outward integer endpoints
at denominator 2^256. It reconstructs the normalization and moments 2,4,6,8,10
from the literal theta integrals. Every one of the 84 declared cells is included
at density Taylor degree 80. Analytic bounds include all four individual time
tails and every omitted theta summand n>=5 at every time. These are six raw
moment quantities on the same source cells, not 504 different source regions.
The entire tail is not replaced by a large finite cutoff.

The computation then verifies the quartic endpoint signs, all three cubic root
brackets, positive distinct weights, and the certified tenth-moment mismatch.
The equality of moments through order eight is a consequence of those exact
root definitions and Newton/cumulant algebra. It is NOT equality of rounded
floating coefficients. The complete nonzero-coupling continuation is a paper
implicit-function argument; a specific positive coupling was NOT certified.

Fifty-two bounded rational controls are also reconstructed in each mode:
27 independent-spin moment/reflection identities, 16 complete-square Gibbs
subtractions, six grouped versus individual Ising moment computations, one
rejection of a negative coupling, and two moment-Jacobian determinant identities.
The same cases in two interpreter modes are not independent mathematical checks.

## Actual adverse executions

Both test_rejections.py commands (normal and optimized isolated Python) passed.
Each has one pristine accepting copy and ELEVEN actual changed-copy refusals:
changed source-moment endpoint; false all-order conclusion; missing source-cell
coverage; changed spin multiplicity; float and Boolean integer aliases; duplicate
JSON; resealed producer density coefficient 4 changed to 5; unsealed proof edit;
unlisted file; and symlinked proof. Every refusal uses the actual accepting CLI.
The resealed numerical/producer cases exercise reconstruction rather than merely
hash checking. Linux symlink tests ran. No Windows execution is claimed.

`--emit` is producer-only. It does not authenticate package bytes. Accepting
commands require the exact nine-file inventory and eight SHA256 entries, then
regenerate the primitive calculation. JSON object keys must be unique, numeric
types must match exactly, and no assert statement implements acceptance.

## Reconnaissance, failures, and nonclaims

Ordinary mpmath/numpy/scipy scouts identified candidate moment configurations.
A 20-spin six-moment fit was superseded by the 28-spin eight-moment construction.
Several limited common-coupling/pair-interaction scouts did not solve the next
constraint. No optimality or exhaustive infeasibility conclusion follows.
A high-order derivative scout timed out, and an optional python-flint install
failed DNS resolution. Neither is counted as an executed proof. The accepting
code uses neither those libraries nor a zeta, gamma, xi, or zero oracle.

No all-order graph family, positive-J numeric model, actual Xi spectrum,
negative-heat zero, large ferromagnetic simulation, finite-height zero census,
parent computational campaign, full repository build, Lean/Comparator, remote
CI, or independent referee-identity certification was performed. The theorem
of Lee–Yang and Rodgers–Tao's theorem are explicit classical imports. The
asymptotic moment-realization transfer and implicit-function arguments remain
paper proofs; finite arithmetic does not machine-prove them.

## Publication preparation

The local result was regenerated after the final primitive changes; all exact
check modes and all refusals completed. Local Git blob/subtree identities and
a clean add-only patch roundtrip are recorded in the external publication
receipt. That fixture is not a full Riemann checkout. The downloadable bundle
includes the same proposed packet and the receipt. Neither a successful upload
nor a finite model certifies (IR). Main and historical sources are not edited.
