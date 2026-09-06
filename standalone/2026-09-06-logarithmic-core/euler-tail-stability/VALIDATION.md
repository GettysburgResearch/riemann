# Validation and analytic boundary

The finite checker uses only Python standard-library integer arithmetic,
Fraction, exact prime factorization, and a range-reduced positive atanh series
for eight native slope enclosures. Atanh tails are bounded geometrically and
then rounded outward to 160-bit dyadics. `math` is used only for exact integer
factorial/binomial operations. No floating-point acceptance, numerical root
finder, optimizer, zero table, scipy, mpmath or symbolic package is imported.

## Executed bounded controls

`verify.py` reconstructs 836 controls in 15 named groups:

- exact compact-weight geometry, rational integrals, Mellin-symbol identity,
  derivative-envelope constants and the total-variation comparison;
- prime valuations and complete prime-power coverage in the Chebyshev binomial
  argument for 32 small integers;
- positive ordinary Euler coefficients, the exact logarithmic coefficient
  convolution, and six levels of the Selberg recurrence for 20 rational local
  phase/radius choices through prime-power degree 12;
- the exact native-versus-weighted divisor-identity distinction;
- complete geometric phase-pi remainders and eight outward native derivative
  enclosures at m=j+1/3, j=2,...,9 (all required prime powers <=348).

Native slope receipts are widened outward once more to 64-bit dyadics for
compact reporting; acceptance uses the full rational interval computation.

Both ordinary and optimized interpreters reproduce the same result.json byte
for byte. The two parent proof blobs are authenticated in each replay. The
parent producers and their historical large counts are not newly replayed.

`test_rejections.py` runs ten deliberate corruptions through the actual CLI
in each target interpreter mode. These include re-sealed false RH/native-sign
claims, a fabricated global parameter certificate, a Boolean count alias,
an empty scope, duplicate JSON key, changed proof, missing source lock,
wrong parent head and changed parent proof. All return the expected refusal.
This validates the named contracts, not arbitrary semantic tamper resistance.

The nine-entry SHA-256 manifest covers all ten files except itself; the checker
requires the exact recursive file inventory and rejects symlinks. Its content
identity is additionally bound by the committed Git tree and archive receipt.
An isolated add-only patch roundtrip reconstructs the new packet byte for byte
and reruns both checker modes with the two pinned parent context files.

## Replay

In the PR checkout:

    python -I -S -B standalone/2026-09-06-logarithmic-core/euler-tail-stability/verify.py \
      --check standalone/2026-09-06-logarithmic-core/euler-tail-stability/result.json

Repeat with `-O`. Run `test_rejections.py` normally and with `--optimized`.
For a detached ZIP use `--parent-root <extracted>/context` on both scripts.
The publication archive retains actual execution logs and their hashes.

## What the execution does not establish

The complete analytic proofs, not these finite controls, supply the PNT
passages, arbitrary-order recurrence, torus equidistribution, parameter
existence and excluded-zero conditions, exact global safe-moment equality,
meromorphic continuation, and all-scale Landau excursions. A specific global
eta,tau pair is NOT numerically constructed or certified.

No new positive native annular range, full-window sign, unbounded native sign,
RH proof, external zero-verification replay, Lean/Comparator/kernel build,
remote CI success or independent referee acceptance is claimed. The result
scope encodes these exclusions explicitly and is checked with type-sensitive
comparison. Positive coefficients in an altered Euler product are not the
literal zeta prime-power coefficients.
