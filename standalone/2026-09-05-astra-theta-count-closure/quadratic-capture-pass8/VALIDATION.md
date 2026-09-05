# Executed checks and review boundary

Scientific base: PR #790 at 513d8f206bb597747afcb7a7410cdf768519d548.
Arithmetic class: EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL.

## What was actually run

The final new verifier reconstructs **756 finite exact controls**. It passed
in ordinary Python and under `python -O`; the complete sorted JSON outputs
are byte-identical and match result.json. These counts refer to the clean
suite, not to its reruns inside the rejection harness.

The controls cover generalized Laguerre orthogonality and the differential
operator; the exact exponential-vector projection product; independent raw
Gram solves; the finite weighted-energy identity; endpoint-zero transforms;
the original factorial metric; the safe-moment compiler on a synthetic
five-atom source; its exact negative values and positive three-sparse controls;
and the all-gap interpolation constant. Ordered Gram/orthogonality entries
include their symmetric counterparts, so this is a control count rather
than a count of independent mathematical facts.

The nonescaping endpoint test additionally reconstructs the rational Gram
projection at dimensions 2, 5, and 10. These are GEOMETRIC L2 projections,
not actual-xi form matrices. It encloses their squared approximation errors
using the first 33 exponential-series terms plus the analytic factorial
remainder. It verifies the rational constants in ED11. It did NOT find a
large r with epsilon_r<=10^-7, and did not evaluate a prime sum through or
beyond 10^8. Those are theorem conditions, not execution claims.

`test_rejections.py` ran seven deliberately corrupted records/source cases
in EACH interpreter mode, for **14 expected refusals**: changed RH flag,
integer/float alias, integer/Boolean alias, duplicate JSON key, altered
negative witness, changed proof, changed source lock. Each run was checked
for the intended diagnostic, not just an arbitrary nonzero exit.

The unchanged signed-packets-pass7 284-control suite was extracted from the
user-supplied published snapshot and replayed in both modes with identical
outputs; its twelve manifest entries also passed. Its six Xi endpoint-sign
computations were NOT rerun. The older broad suites, actual-source interval
matrix certificates, and repository-wide tests were not rerun.

## Replay

From this directory:

    python verify.py --check result.json
    python -O verify.py --check result.json
    python test_rejections.py
    sha256sum -c SHA256SUMS

The checker authenticates four new source texts against literal SHA-256
identities before executing. The manifest binds the other packet files.
It does not authenticate the independent analytic truth of any statement.

## Independent review priorities

1. The Laguerre differential scaling, eigenvalues, and factor 2 in time cutoff.
2. Resolvent convergence on a dense set and the moving spectral cutoff,
   including c=0 and c=infinity; no boundary spectral atoms.
3. The codimension-one endpoint condition: both containing spaces converge,
   and the causal multiplier has dense range on the limiting tail space.
4. Trace-norm continuity under strong projection convergence, and the exact
   thermal shift Gamma_(1/c), not Gamma_(1/(2c)).
5. The source matrix's original Gram metric; raw eigenvalues are not used.
6. Multiplicity-aware inherited Hankel inertia; this packet's projection
   proof itself uses no zero data, but the RH interpretation uses that lemma.
7. ED7's sign and 2pi/e factor, ED9's order of limits, and ED10's complete
   continuous/finite-prime/tail budgets. The limiting endpoint must return.
8. The five-atom all-gap three-sparse control, its rank-five negative witness,
   and the fact that neither construction concerns actual nonreal xi zeros.

No actual-xi matrix, zero census, special-function interval proof, PNT
computation, Lean build, remote CI result, independent referee acceptance,
or external novelty claim is supplied. The infinite spectral and prime-tail
arguments are proposed analytic proofs, not machine proofs.

The full source sign at square width, QC17, remains OPEN. The signed endpoint
defect does not establish it, especially on the endpoint-orthogonal subspace.
