# Scope, source identity, and validation

## What was actually proved by replay

`certify_chain.py --emit chain_certificate.json` passed all predicates on
the exact files in this packet. It establishes a unique root in a
nine-coordinate cube of radius 10^-30 for the complete original-theta
cumulant equations through order 18. The box is strictly invariant under
the preconditioned Newton map, and its derivative norm is below one.

The output receipt has SHA-256
`df51d1773b151b6f89b316faa84416507b90cebb6d068ad6bd4947d1ddaac964`.
It reports a residual displacement bound approximately 2.8426492574·10^-41
and a contraction bound approximately 4.3119634818·10^-12. Strict exact
inequalities, rather than these printed decimal approximations, determine
acceptance.

The interval model includes all 281 spins and all 280 edges. Positivity,
the coupling upper bound, observable support, and designated covariance
are checked on the full box. Direct raw moments and cumulants independently
give moment-20 discrepancy in (0.450,0.451). The tighter directed cumulant
interval is approximately (0.4503725305766265,0.450372530578061).

## Source and arithmetic boundary

- `pr886_primitive.py` has the same implementation as the degree-16 source
  primitive from PR #886, exact commit d998605c0718e332ac503baf078704b862f8250e,
  with one additional trailing newline. The local file has 6,534 bytes;
  removing its final newline gives the 6,533-byte source and exact Git blob
  712bb0f0114cbba85e8082c3130ebf09b53e8936. Both byte identities are recorded
  in SOURCES.json. The local SHA-256 is authenticated inside the checker.
- `theta_source.py` inherits the six-index, 98-cell source implementation
  from PR #974, exact commit 89c37b6707cb77fc5a86143ea98d8756759fdcbc, and
  extends the list of even moments from 18 through 20. PROOF.md rederives
  the Cauchy/Taylor bound, six time tails, and complete omitted-index tail
  for every declared order.
- The scalar backend uses integer endpoints at scale 2^320, with outward
  rounding. No NumPy, SciPy, floating-point optimizer, Decimal target, or
  cached source receipt enters acceptance.
- `tree_core.py` supplies inherited exact cumulant identities, a generic
  forward-differentiation scalar, and cumulants of a fair sign. The new
  chain model is defined in `chain_exact.py`.

This is a fresh complete-source replay using an inherited transcendental
implementation. It is not a second, independent implementation of pi,
exponentials, or theta integration. The exact source identities and the
analytic remainder proof are part of the mathematical dependency.

## Independent checks and mathematical review

The author's `chain_controls.py` separately enumerates all 128 configurations
of a seven-spin tree using rational Gibbs probabilities. Every raw moment
through 20 agrees exactly with the chain recurrence. The control also
checks normalization and symmetry and detects deletion of a positive edge.

The coordinating reviewer independently implemented a second transfer
calculation using conditional probabilities, polynomial products, and
integer powers of the leaf generating functions. It agrees exactly with
the authored recurrence for all raw moments 0 through 20 on the complete
281-spin graph at the frozen rational center. A separate 128-state
enumeration using candidate weights agrees with that independent transfer
calculation. Deleting either the strong edge or all twelve weak core edges
changes the variance. This independently checks the graph encoding; the
existence of the nearby exact root still comes from the contraction proof.
The coordinator retains that check and its hashed receipt for inclusion
with the combined publication.

Two other agents read the source-tail proof, model recurrence, interval
arithmetic, contraction argument, and zero-weight-hub justification. The
scoped review is to be bound to the final packet hash and, after publication,
the exact Git commit. This local replay and review do not imply acceptance
into the repository's integrated mathematics.

## Smallest claims whose failure would invalidate T18C

The source intervals must enclose the moments of the displayed original
theta density, not a truncation. The chain recurrence must equal the
complete normalized Gibbs law. The directed operations and exact inverse
must justify the whole-box contraction. The weighted finite Lee–Yang
theorem must apply to arbitrary nonnegative observable weights, including
the zero-weight hub by the stated Hurwitz limit. Every one of these is
made explicit in PROOF.md and the replay inputs.

No claim here supplies a global moment ladder, a zero-preserving limit
identifying the finite model with xi, or a proof of RH.
